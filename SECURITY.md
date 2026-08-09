# Repository security notes

Response-header captures retain HTTP status, timing, cache, and cookie-attribute metadata, but cookie values are redacted before publication. This includes `Set-Cookie`, `XSRF-TOKEN`, and session-cookie values.

The repository’s earlier history contains raw cookie values from the original capture commit. Those values were short-lived response cookies rather than intentional API credentials, but they should be treated as compromised. History rewriting and remote cleanup require explicit approval because they would replace the public Git history.
