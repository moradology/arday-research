# Crossref Jason Arday author audit — capture metadata

- Captured: 2026-08-06
- Endpoint: `https://api.crossref.org/works`
- Query: `query.author=Jason Arday`, `rows=200`, selected DOI/title/author/date/type/container/URL fields
- Broad API total reported: 353,521
- Items returned and preserved: 200
- Local exact-name filter: author family `Arday`; given name begins `Jason`
- Exact-name DOI records: 47
- SHA-256: `ffb6e86011d88b43a7685db7656ed688a3f3f26e185ac65181d8ef3a5d656a09`
- File: `assets/documents/crossref-jason-arday-author-works-2026-08-06.json`

The broad result contains unrelated Arday-name authors. The exact-name slice was compared against the existing source records by normalized DOI and produced no new Jason Arday work. Crossref’s teacher-education DOI spelling is missing a hyphen relative to the canonical source record; it is an alias, not a duplicate work.
