---
id: SRC-913
type: bookseller reader-review page / changed access-state record
title: "Great and Unfortunate Things" — Foyles 9 August 2026 recheck
subject: ../entities/jason-arday.md
published: 2026-05-16
accessed: 2026-08-09
status: direct endpoint returned a fresh HTTP 403 Cloudflare challenge; indexed review text remains the prior source-version
evidence_class: bookseller endpoint recheck / reception-source access state
related_sources:
  - SRC-437
assets:
  - ../assets/captures/2026-08-09-foyles-memoir-recheck/page.html
  - ../assets/captures/2026-08-09-foyles-memoir-recheck/page.headers.txt
---

# Foyles reader-reviews page — 9 August 2026 recheck

The direct Foyles route for reader reviews of *Great and Unfortunate Things* returned HTTP 403 with a Cloudflare managed challenge on 9 August 2026. The 215,038-byte challenge body is byte-distinct from the prior Foyles capture under `SRC-437`; it exposes no review body, cover, or downloadable book/audio file. The indexed review text and dates remain the prior source-version and are not re-counted as new reception evidence.

This record preserves a changed retrieval state only. Foyles’ reviews remain bookseller-hosted reader reception, not editorial review, clinical/family evidence, or fact-checking.

## Local preservation

- [Challenge HTML](../assets/captures/2026-08-09-foyles-memoir-recheck/page.html) — 215,038 bytes; SHA-256 `e4f637ddaae322e64430e36bcff5403cad15e9b406bdb27abe04a70eb8b4d0b8`.
- [Response headers](../assets/captures/2026-08-09-foyles-memoir-recheck/page.headers.txt) — SHA-256 `4c76109e0150584dc5cbd70381825b853c9acae13f8c01b6f00320a3d82650a9`.

