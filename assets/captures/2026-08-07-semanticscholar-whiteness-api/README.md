# Semantic Scholar API record for Arday’s *Whiteness and Education* article

- Captured: 2026-08-07
- Endpoint: `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080/23793406.2019.1574211?fields=title,openAccessPdf,externalIds,url`
- HTTP status: 200
- JSON SHA-256: `a754758cd4c1230af5278196f87bcff66783869b2032716c79fa752698add2e6`

The API identifies the DOI, Semantic Scholar paper ID, and an `openAccessPdf` URL at Durham Research Online. It labels the route `GREEN` with a `CCBY` licence. This is a changed retrieval state from the earlier preserved Semantic Scholar HTTP 429 boundary in SRC-450, but it does not expose the PDF itself. The Durham landing page and output route still returned HTTP 403 challenge HTML when probed separately.

The API record is a discovery/index record, not the article text and not evidence about the Cofnas/Rollock comparison. Preserve the Durham route as a lead and do not count the index assertion as full-text recovery.
