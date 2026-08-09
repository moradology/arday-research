---
id: SRC-925
---

# Direct PubPeer search and DOI-route boundary for Jason Arday

- Source ID: SRC-925
- Type: post-publication-platform search / access-state boundary
- Accessed: 2026-08-09
- Status: search shell recovered; API blocked by human verification; tested DOI routes returned 404
- Related source: [PubPeer link-resolution audit](2026-08-09-pubpeer-link-resolution-audit.md)
- Search query: `Jason Arday`

## Result

PubPeer’s public search route accepted the exact-name query and returned its normal search-page shell. The server-rendered page includes the query but does not expose a usable result list in the captured HTML. The search API request, made using the page’s CSRF token, returned `{"code":"turnstile_required","message":"Human verification required."}`. This prevents a reliable enumeration of search results from the shell capture.

Two direct publication routes were also tested:

| Tested item | Route result |
|---|---|
| Arday, “Understanding Mental Health: What Are the Issues for Black and Ethnic Minority Students at University?” — DOI `10.3390/socsci7100196` | HTTP 404 from `pubpeer.com/publications/10.3390/socsci7100196` |
| Arday, Belluigi & Thomas, “Attempting to break the chain” — DOI `10.1080/00131857.2020.1773257` | HTTP 404 from `pubpeer.com/publications/10.1080/00131857.2020.1773257` |

The 404 responses do not prove that no PubPeer record or comment exists under another identifier or search route. The human-verification response likewise cannot be treated as a no-results response. This checkpoint therefore records an incomplete but reproducible public-access boundary, not a negative finding about PubPeer coverage of Arday’s work.

## Preserved capture

- [Search HTML and headers](../assets/captures/2026-08-09-pubpeer-direct-search/)
- [SHA-256 manifest](../assets/captures/2026-08-09-pubpeer-direct-search/SHA256SUMS)

Reopen only for a human-verifiable search result, a direct PubPeer publication page for an Arday DOI, an alternate stable identifier, or a changed platform response. Do not repeat the same shell/API/DOI requests unchanged.
