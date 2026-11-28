# REST API and Rate Limiting Resources

## Knowledge

- [Token bucket rate limiter with Redis and redis-py](https://redis.io/docs/latest/develop/use-cases/rate-limiter/redis-py/)
  Official Python token bucket with a Lua script, EVALSHA caching and trade-offs. Use for: the reference implementation and comparing algorithms.
- [Token bucket rate limiter with Redis](https://redis.io/docs/latest/develop/use-cases/rate-limiter/)
  Overview of the rate limiter use case across algorithms. Use for: choosing between token bucket and window algorithms.
- [Redis programmability](https://redis.io/docs/latest/develop/programmability/)
  Official statement of atomic script execution and blocking. Use for: why Lua gives atomic updates.
- [Scripting with Lua (Redis docs)](https://redis.io/docs/latest/develop/programmability/eval-intro/)
  EVAL, KEYS/ARGV, script cache. Use for: script mechanics.
- [RFC 6585](https://datatracker.ietf.org/doc/html/rfc6585)
  Defines status 429 Too Many Requests. Use for: the rate-limit rejection response.
- [MDN: 429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Reference/Status/429) and [MDN: Retry-After](https://developer.mozilla.org/docs/Web/HTTP/Headers/Retry-After)
  Readable references. Use for: header formats and semantics.

## Wisdom (Communities)

- Redis community channels, reachable from redis.io
  Use for: review of limiter scripts and load-testing advice. (Exact URL not yet verified.)

## Gaps

- A high-trust source on REST error response formats (O3) and HTTP methods (O2) is still to be found.
