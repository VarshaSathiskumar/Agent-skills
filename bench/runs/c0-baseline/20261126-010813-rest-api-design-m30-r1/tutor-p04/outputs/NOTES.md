# Notes

## What the learner already knows

- Has built small Python web applications and understands basic frontend-backend communication.
- Has sent HTTP requests, worked with JSON responses, and used APIs in small projects.
- Has basic knowledge of REST resources and URI design (O1).

## What the learner does not know yet

- Is unsure when to use GET, POST, PUT, and PATCH for different API operations.
- Does not fully understand idempotency or why repeating a PUT request differs from repeating a POST request.
- Has not learned how to design consistent API error responses (O3).
- Has not yet been tested on distributed rate limiting (O4); lesson 0001 and quiz 0002 are ready.

## Where the learner tends to get stuck

- Assumes POST and PUT are interchangeable because both send data to the server (M1).
- Thinks HTTP 200 should be returned whenever a request successfully reaches the server (M2).
- Struggles to choose the appropriate HTTP method and status code for real-world API scenarios.

## Objectives and misconception ids

- O1 resources and URIs; O2 methods, idempotency, status codes; O3 consistent error responses.
- O4 (new, 2026-11-25): rate-limit a REST API across many servers with Redis, Lua and a token bucket.
- M3: each Redis command is atomic, so a read-then-write in application code is safe.
- M4: per-server in-memory counters are enough across several servers.
- M5: each API server can supply its own clock to a shared limiter.

## Working notes

- 2026-11-25: the learner is building a small Python REST API and asked for a distributed rate limiter. This is an applied side-topic for the mission: the 429 response ties to O2 and O3. No length was given, so the lesson used 15 minutes. Framework unknown (Flask used as an example). Not yet asked: which framework, and whether Redis is already running.
