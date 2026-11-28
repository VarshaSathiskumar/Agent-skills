# REST API Design Resources

## Knowledge

- [MDN: HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
  Each method with safety, idempotency and cacheability. Use for: choosing a method and explaining how it behaves.
- [MDN: HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
  Every status code with a short definition. Use for: picking a code such as 201, 204, 409, 422.
- [MDN glossary: Idempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)
  Precise definition of idempotency. Use for: PUT versus POST retries.
- [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes?obref=obinsite)
  Official list pointing to the defining RFC section. Use for: checking whether a code is standard.
- [Microsoft Azure Architecture Center: web API design](https://learn.microsoft.com/azure/architecture/best-practices/api-design)
  Practitioner guide to resource-oriented API design. Use for: whole-API design decisions beyond single operations. Only its landing description was seen in search; read it before citing specifics.

## Wisdom (Communities)

- Stack Overflow, tags `rest` and `api-design` (searched, no verified direct link)
  Many real "PUT or PATCH?" and status-code debates. Use for: seeing how practitioners justify choices.

## Gaps

- No verified link yet to the normative RFC 9110 text; find and read it for a future lesson on exact method semantics.
