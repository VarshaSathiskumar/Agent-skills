"""The keys guard: a PreToolUse hook that keeps the answer keys in keys/ away from the main conversation.

tutor/.claude/settings.json registers it for Read, Grep, Glob, Bash and PowerShell, with
"onFailure": "block", so a crash or a missing Python blocks the call instead of letting it through.
Claude Code sends the call as JSON on stdin. Exit 0 lets it run; exit 2 blocks it, and the model
reads the message printed on stderr.

Who may read keys/: only the subagents in ALLOWED, told apart by the input's agent_type, which
Claude Code sets inside a subagent and leaves out in the main conversation.
- grader: grading compares each answer with the key, so the grader cannot do its job without it.
No other agent is allowed. The quiz reviewer reviews the draft key in drafts/, the tutor never needs
a key, and every extra agent allowed is one more place an answer could leak from.

What counts as touching keys/, for any other caller:
- Read: a file_path with a folder or file named keys (any case, / or \\, relative or absolute).
- Glob: a pattern or path naming keys, or a wildcard segment such as k* that matches it
  (a bare * or ** only lists file names, so it is allowed).
- Grep: a path or glob naming keys, or a search in "content" mode whose scope holds keys/
  (no path, or the workspace or a folder above it), which would print the keys' lines.
- Bash and PowerShell: any word in the command whose path parts name keys or match it as a
  wildcard (cat k*/0001.json, cat */0001.json), and any recursive search (grep -r, rg, git grep,
  Select-String -Recurse, Get-ChildItem -Recurse) over the workspace or with no folder named.
Input that cannot be read is blocked on purpose rather than allowed.

Known gaps: a command that builds the name at run time (a variable, $(...), brace expansion,
base64, a script in python -c or node -e), find . | xargs cat, and a symlink to keys/ made under
another name. A plain word "keys" in a Bash command is blocked even when it is not a path.
"""

from __future__ import annotations

import fnmatch
import json
import os
import re
import shlex
import sys

ALLOWED = {"grader"}
FOLDER = "keys"
WILDCARD = re.compile(r"[*?\[]")
SPLIT = re.compile(r"[/\\=:,;|&<>()'\"`{}\s]+")
ROOTISH = {"", ".", "./", ".\\", "..", "/", "\\", "~", "*", "**", "$pwd", "${pwd}", "$claude_project_dir",
           "${claude_project_dir}", "$env:claude_project_dir"}
SEARCHERS = {"rg", "ag", "ack", "ripgrep"}
GREPS = {"grep", "egrep", "fgrep", "zgrep"}
PS_RECURSE = {"select-string", "sls", "get-childitem", "gci", "ls", "dir"}

MESSAGE = ("Blocked by the keys guard: the answer keys in keys/ are for the grader subagent only, "
           "and the main conversation and other agents may not read, search or list them. "
           "Do not look for the answer another way. To grade a submission, start the grader subagent; "
           "to search the workspace, name a folder that is not keys/, such as quizzes/ or lessons/.")


def names_keys(part: str, wildcards: bool) -> bool:
    """Whether one path segment is keys, or, with wildcards, a pattern that matches keys."""
    part = part.strip().lower()
    if part == FOLDER:
        return True
    return wildcards and bool(WILDCARD.search(part)) and fnmatch.fnmatchcase(FOLDER, part)


def path_names_keys(value: object, wildcards: bool, bare_stars: bool = True) -> bool:
    """Whether any segment of a path or pattern names keys/."""
    if not isinstance(value, str):
        return False
    for part in SPLIT.split(value):
        if not bare_stars and part.strip() in {"*", "**"}:
            continue
        if names_keys(part, wildcards):
            return True
    return False


def holds_keys(path: object, base: str) -> bool:
    """Whether a search rooted at path would reach base/keys: no path, the workspace, or above it."""
    if not isinstance(path, str) or path.strip().lower() in ROOTISH:
        return True
    root = os.path.normcase(os.path.normpath(base or os.getcwd()))
    where = os.path.normcase(os.path.normpath(os.path.join(root, os.path.expanduser(path))))
    return root == where or root.startswith(where.rstrip(os.sep) + os.sep)


def words(command: str) -> list[str]:
    """The command's words, with shell punctuation as words of its own."""
    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=True)
        lexer.whitespace_split = True
        return list(lexer)
    except ValueError:
        return [w for w in re.split(r"\s+|([;|&<>()])", command) if w]


def recursive_search(segment: list[str], powershell: bool) -> bool:
    """Whether one simple command searches recursively over the workspace or an unnamed folder."""
    if not segment:
        return False
    name = os.path.basename(segment[0].replace("\\", "/")).lower().removesuffix(".exe")
    args = segment[1:]
    if name == "git" and args and args[0].lower() == "grep":
        name, args = "rg", args[1:]
    if powershell or name in PS_RECURSE:
        if name in PS_RECURSE and any(a.lower().startswith("-r") for a in args):
            folders = [a for a in args if not a.startswith("-")]
            return not folders or any(holds_keys(f, "") for f in folders)
        return False
    if name in GREPS:
        recursive = any(a in {"--recursive", "--dereference-recursive"} or
                        (a.startswith("-") and not a.startswith("--") and ("r" in a or "R" in a)) for a in args)
        if not recursive:
            return False
        operands = [a for a in args if not a.startswith("-")][1:]  # the first is the pattern
    elif name in SEARCHERS:
        operands = [a for a in args if not a.startswith("-")][1:]
    else:
        return False
    return not operands or any(holds_keys(o, "") for o in operands)


def command_reaches_keys(command: object, powershell: bool) -> bool:
    if not isinstance(command, str):
        return False
    # the raw text too: a POSIX shell parser reads PowerShell's .\keys\0001.json as escapes and loses the name
    if path_names_keys(command, wildcards=False):
        return True
    tokens = words(command)
    if any(path_names_keys(t, wildcards=True) for t in tokens):
        return True
    segment: list[str] = []
    for token in tokens + [";"]:
        if token in {";", "|", "||", "&&", "&", "|&", "(", ")", "\n"}:
            if recursive_search(segment, powershell):
                return True
            segment = []
        else:
            segment.append(token)
    return False


def reaches_keys(tool: str, args: dict, cwd: str) -> bool:
    if tool == "Read":
        return path_names_keys(args.get("file_path"), wildcards=False)
    if tool == "Glob":
        return any(path_names_keys(args.get(k), wildcards=True, bare_stars=False) for k in ("pattern", "path"))
    if tool == "Grep":
        if any(path_names_keys(args.get(k), wildcards=True, bare_stars=False) for k in ("path", "glob")):
            return True
        return args.get("output_mode") == "content" and holds_keys(args.get("path"), cwd)
    if tool == "Bash":
        return command_reaches_keys(args.get("command"), powershell=False)
    if tool == "PowerShell":
        return command_reaches_keys(args.get("command"), powershell=True)
    return False


def decide(raw: str) -> int:
    try:
        call = json.loads(raw)
    except ValueError:
        print("Blocked by the keys guard: its input could not be read, so the call was not checked.", file=sys.stderr)
        return 2
    if not isinstance(call, dict):
        print("Blocked by the keys guard: its input was not a JSON object.", file=sys.stderr)
        return 2
    if call.get("agent_type") in ALLOWED:
        return 0
    args = call.get("tool_input")
    if not isinstance(args, dict):
        args = {}
    cwd = call.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or ""
    if reaches_keys(str(call.get("tool_name", "")), args, cwd):
        print(MESSAGE, file=sys.stderr)
        return 2
    return 0


def main() -> int:
    try:
        return decide(sys.stdin.read())
    except Exception as error:  # decide on purpose, never crash
        print(f"Blocked by the keys guard: it failed to check this call ({type(error).__name__}).", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
