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
- Quiz 0001 (s1): put HTTP methods in a URI (M1 again) and gave /orders instead of nested /users/15/orders; counts path segments correctly.
- Struggles to choose the appropriate HTTP method and status code for real-world API scenarios.
