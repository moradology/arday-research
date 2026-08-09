---
id: SRC-1129
type: bibliographic index / author-ID recheck
title: "OpenAlex Jason Arday author-ID recheck — 9 August 2026"
subject: ../entities/jason-arday.md
accessed: 2026-08-09
status: changed dynamic index state; no new DOI/title key
evidence_class: bibliographic index metadata and negative-space reconciliation; not publisher verification
updates: sources/2026-08-06-openalex-author-works-recheck.md
urls:
  - https://api.openalex.org/authors/A5048886069
  - https://api.openalex.org/works?filter=author.id:A5048886069&per-page=200&select=id,doi,title,publication_year
assets:
  - ../assets/documents/openalex-jason-arday-works-recheck-2026-08-09-summary.json
---

# OpenAlex author-ID recheck — 9 August 2026

The public OpenAlex author record `A5048886069` returned the display name “Jason Arday,” `works_count` 58, `cited_by_count` 1,139, and an `updated_date` of 8 August 2026. The author-ID-filtered works query returned 56 records spanning 2015–2026.

Normalized comparison against the local DOI/title corpus found no new DOI or title key. The two records without DOI remain the already-canonical 2015 *Ethnic education and labour market position in Britain (1972–2013)* item and the 2026 narrative-inquiry study. The 2025 DOI `10.2307/jj.26932075` is now represented by `SRC-1128`.

## Evidence boundary

This is a dynamic discovery-index state, not independent authorship, publication, or citation verification. `works_count` and `cited_by_count` are volatile OpenAlex metadata. The unchanged work set closes this exact author-ID query for this capture only; it does not prove that OpenAlex’s author linkage or work set is complete.

Reopen only after a changed work set, a concrete no-DOI publisher/repository lead, or a changed author identity record.

## Local preservation

- [Selected author-ID works response](../assets/documents/openalex-jason-arday-works-recheck-2026-08-09-summary.json) — 56 returned work keys plus query metadata.
