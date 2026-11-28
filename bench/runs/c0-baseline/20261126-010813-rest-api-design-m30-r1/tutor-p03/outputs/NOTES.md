# Notes

## What the learner already knows

- Has built small Python web applications and understands basic frontend-backend communication.
- Has sent HTTP requests, worked with JSON responses, and used APIs in small projects.
- Has basic knowledge of REST resources and URI design (O1).

## What the learner does not know yet

- Is unsure when to use GET, POST, PUT, and PATCH for different API operations.
- Does not fully understand idempotency or why repeating a PUT request differs from repeating a POST request.
- Has not learned how to design consistent API error responses (O3).

## Where the learner tends to get stuck

- Assumes POST and PUT are interchangeable because both send data to the server (M1).
- Thinks HTTP 200 should be returned whenever a request successfully reaches the server (M2).
- Asked (session 2) whether a successful POST /users should return 200 or 204 to show creation; offered only those two options, so 201 Created (plus a Location header) was not on their radar. Related to M2. Explained in chat; check later that they can pick 201 vs 200 vs 204 unprompted.
- Struggles to choose the appropriate HTTP method and status code for real-world API scenarios.
