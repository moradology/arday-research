---
id: SRC-284
type: bibliographic index / API recheck
title: "OpenAlex Jason Arday author and works recheck"
subject: ../entities/jason-arday.md
accessed: 2026-08-06
status: changed API metadata; no new work key identified
evidence_class: bibliographic index metadata, not publisher verification
updates: sources/2026-08-06-openalex-author-works-audit.md
urls:
  - https://api.openalex.org/authors/A5048886069
  - https://api.openalex.org/works?filter=author.id:A5048886069&per-page=200&sort=publication_date:asc
assets:
  - ../assets/documents/openalex-jason-arday-author-recheck-2026-08-06.json
  - ../assets/documents/openalex-jason-arday-works-recheck-2026-08-06.json

# OpenAlex recheck

A fresh request for OpenAlex author `A5048886069` returned 58 works and 1,136 citations; the filtered works request returned the same 56-work set represented in SRC-170, spanning 2015–2026. The citation count changed from the earlier 1,134 snapshot, but no new DOI/title key was identified after comparison with the registry. The two no-DOI records remain the 2015 *Ethnic education and labour market position in Britain (1972–2013)* item and the 2026 narrative-inquiry study record.

## Evidence boundary

This is a dynamic discovery-index state, not independent authorship or publisher evidence. The unchanged work set does not close the remaining publisher/repository reconciliation queue; it only records that this exact OpenAlex author/work query produced no new candidate on recheck.

## Local preservation

- Author JSON: `assets/documents/openalex-jason-arday-author-recheck-2026-08-06.json` — SHA-256 `6887105204ccef678ab0bf5553704b6a03d4a4a9c73b3fece08ae3729dc91593`.
- Works JSON: `assets/documents/openalex-jason-arday-works-recheck-2026-08-06.json` — SHA-256 `ab7e303c1f2e77aa9d4dd06dc1c195d372031aabcd068423ae586c9650013a30`.

## 2026-08-07 recheck

The same filtered works request returned 56 records. A normalized comparison of `{id, doi, title}` against the 6 August response was byte-identical: no new work key, DOI, or title appeared. The fresh response is preserved separately because dynamic API responses are point-in-time evidence.

- [7 August works JSON](../assets/documents/openalex-jason-arday-works-recheck-2026-08-07.json) — SHA-256 `7022d78b940f309c769274a3eab0bfc09b8946f71542242267e2dcb3f44b76d4`
- [7 August response headers](../assets/documents/openalex-jason-arday-works-recheck-2026-08-07.headers) — SHA-256 `02e7eeb2e133d93162b945c2ebe5064cd40f0e55c3cdf45a655f2b9ddc8ad194`

This closes the exact OpenAlex author/work query for the current pass. Reopen it only after a changed work set or a concrete publisher/repository lead.
