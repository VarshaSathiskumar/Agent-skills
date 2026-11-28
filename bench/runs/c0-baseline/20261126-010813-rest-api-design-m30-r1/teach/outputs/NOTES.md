# Notes

## What the learner already knows

- Has built small Python web applications and understands basic frontend-backend communication.
- Has sent HTTP requests, worked with JSON responses, and used APIs in small projects.
- Has basic knowledge of REST resources and URI design (O1).

## What the learner does not know yet

- Is unsure when to use GET, POST, PUT, and PATCH for different API operations.
- Does not fully understand idempotency or why repeating a PUT request differs from repeating a POST request.
- Has not learned how to design consistent API error responses (O3).

## Working notes

- Lesson 0001 (O2, 30 min) written with quiz 0002; it targets M1 and M2 directly. Not yet taken, so nothing about O2 is shown yet.
- Lesson covers GET/POST/PUT/PATCH/DELETE, idempotency, 200/201/204 and 400/401/403/404/409/422/500. Next: O3 (consistent error responses), after the quiz shows how O2 landed.

## Where the learner tends to get stuck

- Assumes POST and PUT are interchangeable because both send data to the server (M1).
- Thinks HTTP 200 should be returned whenever a request successfully reaches the server (M2).
- Struggles to choose the appropriate HTTP method and status code for real-world API scenarios.
