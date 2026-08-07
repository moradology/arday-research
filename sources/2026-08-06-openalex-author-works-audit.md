---
id: SRC-170
type: bibliographic index / API snapshot / scholarly-output audit
title: "OpenAlex author and works snapshot for Jason Arday"
subject: ../entities/jason-arday.md
accessed: 2026-08-06
status: public API snapshot; coverage audit; candidate reconciliation queue
evidence_class: bibliographic index metadata, not publisher verification
updates: jason-arday-public-output-index.md, claims-ledger.md, research-log.md, NEXT.md
---

# Record

OpenAlex author search identified `https://openalex.org/A5048886069` as Jason Arday, with 58 works and 1,134 citations in the author result. A filtered works request for that author returned 56 works: 54 with DOI strings and 2 without DOI strings, covering 2015–2026. The result is a discovery index, not proof that every record is correctly attributed or that every work is independently verified.

## Reconciliation result

The DOI-bearing set was compared against the existing source records by DOI suffix. Many apparent unmatched items are alternate manifestations of already-catalogued books, chapters, repository copies, or records whose local notes did not yet carry the DOI. The queue was updated after publisher-level checks on 6 August 2026.

Canonical records now exist for Being Black (SRC-175), Many Rivers (SRC-176), Sowing (SRC-080), the separate 2019 educational-leadership chapter (SRC-177), the OSF v1/v2 versions (SRC-178), the Cool Britannia chapter family (SRC-179), the mental-health staff encyclopedia editions (SRC-180), the We See foreword (SRC-181), Understanding Mental Health (SRC-174), CoPICS (SRC-171), the women-academics article (SRC-173), and the 2025 BMJ Open protocol (SRC-172). The Black Professoriate and Black PhD foreword records were upgraded with alternate identifiers and local preservation. The remaining concrete reconciliation queue is:

- The Fire Now chapter, Liberated Library DOI pair, and teacher-education chapter are now canonical or upgraded records (SRC-078, SRC-182, and SRC-074). The football chapter (SRC-026) now also has a locally preserved PagePlace preview, which confirms its contents-page location but not its text. The remaining queue is limited to older encyclopedia/book manifestations and any records requiring a changed-state or publisher-level check.

OpenAlex also reports multiple manifestations of already-captured books and articles. DOI aliases and edition variants are retained in their canonical records rather than promoted as duplicate people or works.

## Local preservation

- [OpenAlex author search](../assets/documents/openalex-jason-arday-author-search-2026-08-06.json) — SHA-256 `82ff576e82001476f68c3ddff63716a087c12a0cc005f0fa0adc6a7c9a4dd00a`
- [OpenAlex works response](../assets/documents/openalex-jason-arday-works-2026-08-06.json) — SHA-256 `706edde5a5ee961e2efc39f6b7613e2ff40e500b12ea61c28bbe92ec6c54eb7c`

## Boundary

This snapshot covers one OpenAlex author identifier and one API response sorted by ascending publication date. It does not establish completeness beyond OpenAlex, does not replace ORCID or Durham counts, and does not prove publication status where OpenAlex has only inferred metadata.
