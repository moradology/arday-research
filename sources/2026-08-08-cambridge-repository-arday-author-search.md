---
id: SRC-440
type: institutional repository author-search boundary
title: "Cambridge Repository API search for Arday"
subject: ../entities/jason-arday.md
date: 2026-08-08
accessed: 2026-08-08
status: bounded search captured; four author-level records reconciled; no new publication node
evidence_class: first-party repository API response and item-level metadata inspection
updates: jason-arday-public-output-index.md, claims-ledger.md, NEXT.md
related: sources/2025-11-26-cambridge-repository-underrepresented-young-people.md
---

The Cambridge Repository Discover API was queried for `Arday` with `size=100` on 8 August 2026. The response returned 29 textual search hits. Each hit’s linked item metadata was then inspected for `dc.contributor.author` rather than assuming that a full-text mention represented authorship.

Exactly four items identified Arday as an author:

- the 2023 correction to his 2018 *Social Sciences* article (SRC-023);
- the 2024 CoPICS study protocol (SRC-017 / canonical DOI record);
- the 2024 *British Educational Research Journal* women-academics article (SRC-081);
- the 2025 BMJ Open under-represented-young-people protocol (SRC-172, with Cambridge repository manifestation SRC-439).

The remaining 25 search hits are not promoted to Arday publications: they contain a textual mention or an unrelated name match in repository metadata/full text. The captured JSON preserves the complete result set and the item-level inspection is the basis for this negative-space boundary. This is a repository discovery result, not an independent assessment of the publications’ content or authorship beyond the repository’s metadata.

## Local preservation

- [Cambridge Discover API response](../assets/documents/repositories/cambridge-arday-search-2026-08-08/search.json) — SHA-256 `f37f3090a993d1c902a38f67eb98e62d886faf9859563da627e15366fdc87c9b`
- [Response headers](../assets/documents/repositories/cambridge-arday-search-2026-08-08/response-headers.txt) — SHA-256 `03dbd9a1598a8ff9686748a6159f48cb10ec037bc8c11538b62869c6a6b9847a`
- Query endpoint: `https://api.repository.cam.ac.uk/server/api/discover/search/objects?query=Arday&size=100`

