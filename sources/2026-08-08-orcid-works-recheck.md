---
id: SRC-628
type: researcher-identifier API recheck and DOI date reconciliation
title: "ORCID works recheck — Jason Arday"
subject: ../entities/jason-arday.md
published: 2026-08-08
accessed: 2026-08-08
status: current 11-work ORCID response preserved; all DOI/title keys already canonical; one publication-date metadata change reconciled against Crossref
evidence_class: ORCID public API metadata and Crossref DOI metadata; bibliographic provenance, not independent authorship or content evidence
urls:
  - https://orcid.org/0000-0002-9822-1068
  - https://pub.orcid.org/v3.0/0000-0002-9822-1068/works
  - https://api.crossref.org/works/10.1007/s10734-022-00939-0
assets:
  - ../assets/captures/2026-08-08-orcid-works-recheck/works.json
  - ../assets/captures/2026-08-08-orcid-works-recheck/works.headers.txt
  - ../assets/captures/2026-08-08-orcid-works-recheck/crossref.json
  - ../assets/captures/2026-08-08-orcid-works-recheck/crossref.headers.txt

# ORCID works recheck

The public ORCID API returned 11 work groups for `0000-0002-9822-1068` on 8 August 2026. Every DOI/title key matches an existing canonical publication record; no new publication node was created.

## Date-version discrepancy

The ORCID work summary for “Same storm, different boats: the impact of COVID-19 on Black students and academic staff in UK and US higher education” now reports a publication date of July 2026. The same ORCID put-code was dated 25 October 2022 in the 6 August snapshot, and the ORCID record’s modification timestamp changed while its creation timestamp remained unchanged.

The contemporaneous Crossref DOI record distinguishes the dates: `published-online` and `published` are 25 October 2022, while `published-print` is July 2026. The canonical article record therefore retains 25 October 2022 as the online/version-of-record publication date and records the July 2026 value as a later print/metadata manifestation. This is a bibliographic metadata update, not evidence that a new article or correction was published.

## Boundary

The ORCID 11-work view remains a researcher-identifier boundary, not an exhaustive bibliography. Reopen only for a changed ORCID work group, a new DOI/title key, or a materially different publisher/repository manifestation.

## Local preservation

- ORCID JSON: SHA-256 `56d481b5d494c893b700f5890fff5e70a2219c4177058a3043a9c5382eb2297e`.
- ORCID response headers: SHA-256 `7d9820af6383a63655ea1030eea54a321386d12a71ac97bc28fa93c68b2da130`.
- Crossref JSON: SHA-256 `bc4e66c0abc2092f9f853348ad73b98a2917cd21b5ee17134b3d3b156ddfe116`.
- Crossref response headers: SHA-256 `aa9b0d1ebfadfe322114e00ca2deebca8e025c864f10bffca83b84bea985a7fd`.
