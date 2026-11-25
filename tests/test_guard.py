"""Tests of the keys guard, tutor/.claude/hooks/keys_guard.py.

Each test writes one sample PreToolUse hook input to the script's stdin, the way Claude Code does,
and checks the exit code: 2 blocks the call, 0 lets it run. No test calls Claude.
"""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

GUARD = Path(__file__).resolve().parent.parent / "tutor" / ".claude" / "hooks" / "keys_guard.py"
WORKSPACE = "/tmp/p3-workspace"


def run_guard(tool: str, tool_input: dict, agent_type: str | None = None) -> subprocess.CompletedProcess:
    call = {"session_id": "test", "cwd": WORKSPACE, "hook_event_name": "PreToolUse",
            "tool_name": tool, "tool_input": tool_input}
    if agent_type is not None:
        call["agent_type"] = agent_type
        call["agent_id"] = "agent-test"
    return run_raw(json.dumps(call))


def run_raw(stdin: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(GUARD)], input=stdin, capture_output=True, text=True, timeout=30)


class GuardTest(unittest.TestCase):
    def assertBlocked(self, tool: str, tool_input: dict, agent_type: str | None = None) -> None:
        result = run_guard(tool, tool_input, agent_type)
        self.assertEqual(result.returncode, 2, f"{tool} {tool_input} by {agent_type or 'main'} should be blocked")
        self.assertIn("keys guard", result.stderr, "a block must tell the model why on stderr")

    def assertAllowed(self, tool: str, tool_input: dict, agent_type: str | None = None) -> None:
        result = run_guard(tool, tool_input, agent_type)
        self.assertEqual(result.returncode, 0,
                         f"{tool} {tool_input} by {agent_type or 'main'} should be allowed; stderr: {result.stderr}")


class MainConversationBlocked(GuardTest):
    """The main conversation (no agent_type) never reaches keys/, with any of the five tools."""

    def test_read(self):
        self.assertBlocked("Read", {"file_path": "keys/0001.json"})

    def test_read_absolute(self):
        self.assertBlocked("Read", {"file_path": f"{WORKSPACE}/keys/0001.json"})

    def test_read_dot_slash(self):
        self.assertBlocked("Read", {"file_path": "./keys/0001.json"})

    def test_read_windows_separator(self):
        self.assertBlocked("Read", {"file_path": "keys\\0001.json"})

    def test_read_other_case(self):
        # macOS and Windows file systems ignore case, so KEYS/ is the same folder
        self.assertBlocked("Read", {"file_path": "KEYS/0001.json"})

    def test_grep_path(self):
        self.assertBlocked("Grep", {"pattern": "correct", "path": "keys"})

    def test_grep_glob(self):
        self.assertBlocked("Grep", {"pattern": "correct", "glob": "keys/*.json"})

    def test_grep_content_over_workspace(self):
        # no path: a content search over the whole workspace would print the keys' lines
        self.assertBlocked("Grep", {"pattern": "correct", "output_mode": "content"})

    def test_glob(self):
        self.assertBlocked("Glob", {"pattern": "keys/*.json"})

    def test_glob_wildcard_folder(self):
        self.assertBlocked("Glob", {"pattern": "k*/0001.json"})

    def test_bash_cat(self):
        self.assertBlocked("Bash", {"command": "cat keys/0001.json"})

    def test_bash_wildcard(self):
        self.assertBlocked("Bash", {"command": "cat k*/0001.json"})

    def test_bash_in_a_pipeline(self):
        self.assertBlocked("Bash", {"command": "ls quizzes && head -n 5 ./keys/0001.json | tail -n 2"})

    def test_bash_cd_then_cat(self):
        self.assertBlocked("Bash", {"command": "cd keys; cat 0001.json"})

    def test_bash_recursive_grep(self):
        self.assertBlocked("Bash", {"command": "grep -rn correct ."})

    def test_bash_ripgrep(self):
        self.assertBlocked("Bash", {"command": "rg correct"})

    def test_powershell_get_content(self):
        self.assertBlocked("PowerShell", {"command": "Get-Content keys/0001.json"})

    def test_powershell_windows_path(self):
        self.assertBlocked("PowerShell", {"command": "Get-Content .\\keys\\0001.json"})

    def test_powershell_recursive_search(self):
        self.assertBlocked("PowerShell", {"command": "Get-ChildItem -Recurse . | Select-String correct"})


class OtherAgentsBlocked(GuardTest):
    """Only the grader is allowed: any other subagent is blocked like the main conversation."""

    def test_grade_reviewer(self):
        self.assertBlocked("Read", {"file_path": "keys/0001.json"}, agent_type="grade-reviewer")

    def test_quiz_reviewer(self):
        self.assertBlocked("Bash", {"command": "cat keys/0001.json"}, agent_type="quiz-reviewer")

    def test_name_close_to_grader(self):
        self.assertBlocked("Read", {"file_path": "keys/0001.json"}, agent_type="Grader")


class GraderAllowed(GuardTest):
    """The grader subagent reads the keys with every tool."""

    def test_read(self):
        self.assertAllowed("Read", {"file_path": "keys/0001.json"}, agent_type="grader")

    def test_read_absolute(self):
        self.assertAllowed("Read", {"file_path": f"{WORKSPACE}/keys/0001.json"}, agent_type="grader")

    def test_grep(self):
        self.assertAllowed("Grep", {"pattern": "M1", "path": "keys"}, agent_type="grader")

    def test_glob(self):
        self.assertAllowed("Glob", {"pattern": "keys/*.json"}, agent_type="grader")

    def test_bash(self):
        self.assertAllowed("Bash", {"command": "cat keys/0001.json"}, agent_type="grader")

    def test_powershell(self):
        self.assertAllowed("PowerShell", {"command": "Get-Content keys/0001.json"}, agent_type="grader")


class OtherReadsAllowed(GuardTest):
    """The main conversation's ordinary reads still work."""

    def test_read_quiz(self):
        self.assertAllowed("Read", {"file_path": "quizzes/0001.json"})

    def test_read_mission(self):
        self.assertAllowed("Read", {"file_path": "MISSION.md"})

    def test_read_absolute_submission(self):
        self.assertAllowed("Read", {"file_path": f"{WORKSPACE}/submissions/s1.json"})

    def test_read_name_containing_keys(self):
        # a file whose name only contains the word is not the folder
        self.assertAllowed("Read", {"file_path": "lessons/0004-api-keys-and-secrets.html"})

    def test_read_draft_key(self):
        # the quiz's draft key lives in drafts/, where the quiz reviewer reads it
        self.assertAllowed("Read", {"file_path": "drafts/0002-key-v1.json"})

    def test_glob_everything(self):
        # a bare ** only lists names, so it stays allowed
        self.assertAllowed("Glob", {"pattern": "**/*.md"})

    def test_grep_files_over_workspace(self):
        # the default mode lists file names, not lines
        self.assertAllowed("Grep", {"pattern": "agent"})

    def test_grep_content_in_a_folder(self):
        self.assertAllowed("Grep", {"pattern": "agent", "path": "lessons", "output_mode": "content"})

    def test_bash_ls(self):
        self.assertAllowed("Bash", {"command": "ls lessons"})

    def test_bash_recursive_grep_in_a_folder(self):
        self.assertAllowed("Bash", {"command": "grep -rn agent lessons"})

    def test_powershell_get_content(self):
        self.assertAllowed("PowerShell", {"command": "Get-Content quizzes/0001.json"})

    def test_tool_outside_the_matcher(self):
        # Write is not matched, so the quiz skill can still write a new key once
        self.assertAllowed("Write", {"file_path": "keys/0002.json", "content": "{}"})


class BadInputBlocked(unittest.TestCase):
    """Input the guard cannot read is blocked on purpose, never let through by a crash."""

    def test_not_json(self):
        self.assertEqual(run_raw("not json").returncode, 2)

    def test_empty(self):
        self.assertEqual(run_raw("").returncode, 2)

    def test_not_an_object(self):
        self.assertEqual(run_raw("[1, 2]").returncode, 2)


class Registration(unittest.TestCase):
    """settings.json registers the script the tests run, for all five tools, and fails closed."""

    def test_settings(self):
        settings = json.loads((GUARD.parent.parent / "settings.json").read_text())
        entries = settings["hooks"]["PreToolUse"]
        self.assertTrue(entries)
        entry = entries[0]
        self.assertEqual(set(entry["matcher"].split("|")), {"Read", "Grep", "Glob", "Bash", "PowerShell"})
        hook = entry["hooks"][0]
        self.assertEqual(hook["type"], "command")
        self.assertEqual(hook.get("onFailure"), "block")
        self.assertIn("$CLAUDE_PROJECT_DIR/.claude/hooks/keys_guard.py", hook["command"])

    def test_no_deny_rule_for_keys(self):
        # a deny rule would block the grader too, and a hook cannot lift it
        settings = json.loads((GUARD.parent.parent / "settings.json").read_text())
        self.assertFalse(any("keys" in rule for rule in settings["permissions"].get("deny", [])))


if __name__ == "__main__":
    unittest.main()
