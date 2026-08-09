---
id: SRC-1131
type: library catalogue search boundary
title: "Library and national-catalogue search boundary for Jason Arday"
subject: ../entities/jason-arday.md
accessed: 2026-08-09
status: exact-name catalogue routes tested; no new record recovered
evidence_class: catalogue access-state and negative-space record; not proof of nonexistence
urls:
  - https://search.worldcat.org/search?q=%22Jason%20Arday%22
  - https://explore.bl.uk/primo-explore/search?query=any,contains,Jason%20Arday&vid=BLVU1
  - https://www.libraryhub.jisc.ac.uk/search?query=Jason%20Arday
  - https://www.loc.gov/books/?q=%22Jason+Arday%22&fo=json&c=100
assets:
  - ../assets/documents/library-catalogue-search-boundary-2026-08-09.json
---

# Library and national-catalogue search boundary

Exact-name catalogue routes were tested for WorldCat, the British Library Explore catalogue, Library Hub Jisc, and the Library of Congress books API. No new Jason Arday edition, library holding, thesis manifestation, or catalogue record was recovered in this pass.

WorldCat returned HTTP 200 but only a JavaScript/Cloudflare shell that stated JavaScript was required; no parsed result was claimed. The British Library Explore route returned HTTP 400 with an empty body. The tested Library Hub Jisc hostname did not resolve. The Library of Congress exact-query API route returned HTTP 403 to the scripted request. These are retrieval boundaries, not evidence that the catalogues contain no Arday records.

Existing public-library records for *Great and Unfortunate Things*, the 2015 LJMU thesis, and Arday’s co-authored works remain canonical. Reopen this lane only for a changed catalogue endpoint, a direct record identifier, or a lawful browser-rendered result.

## Local preservation

- [Selected route states](../assets/documents/library-catalogue-search-boundary-2026-08-09.json)
