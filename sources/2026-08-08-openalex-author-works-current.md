---
id: SRC-607
type: bibliographic index / API snapshot
title: "OpenAlex current Jason Arday author/work snapshot"
subject: ../entities/jason-arday.md
accessed: 2026-08-08
status: unchanged 56-work set; no new DOI/title key identified
evidence_class: bibliographic index metadata, not publisher verification
updates: sources/2026-08-06-openalex-author-works-recheck.md
urls:
  - https://api.openalex.org/authors?search=Jason%20Arday
  - https://api.openalex.org/works?filter=author.id:A5048886069&per-page=200&sort=publication_date:desc
assets:
  - ../assets/captures/2026-08-08-scholarly-index-audit/openalex.json
  - ../assets/captures/2026-08-08-scholarly-index-audit/openalex.headers.txt
  - ../assets/captures/2026-08-08-scholarly-index-audit/openalex-works.json
  - ../assets/captures/2026-08-08-scholarly-index-audit/openalex-works.headers.txt
---

# OpenAlex current snapshot

The 8 August 2026 OpenAlex author search returned the existing Jason Arday identifier `A5048886069`. The filtered works request for that identifier returned 56 records, spanning 2015–2026. Normalized comparison of the returned `{id, doi, title}` keys against the existing publication registry found no new Jason Arday DOI/title candidate. The two no-DOI records remain the 2015 labour-market item and the 2026 narrative-inquiry study record.

## Evidence boundary

This is a point-in-time discovery-index result, not independent authorship or publisher evidence. The unchanged result closes this exact OpenAlex query for the current pass; further scholarly discovery should proceed through a changed index result or a concrete publisher, repository, catalogue, or full-text lead.

## Local preservation

- Author search JSON: `assets/captures/2026-08-08-scholarly-index-audit/openalex.json` — SHA-256 `4735add19de70134af9108ca7b2bf41febd6790c6b54446f5b11b5fc62683951`.
- Author search headers: `assets/captures/2026-08-08-scholarly-index-audit/openalex.headers.txt` — SHA-256 `24271b966f84ebc81169aff51a0979daec957aeca46277dbfeed5e672ea71170`.
- Works JSON: `assets/captures/2026-08-08-scholarly-index-audit/openalex-works.json` — SHA-256 `726b02536de505db4fb85f4f3dadd4060808074717e4b94a036c50ed4157804c`.
- Works headers: `assets/captures/2026-08-08-scholarly-index-audit/openalex-works.headers.txt` — SHA-256 `0ac0c4a966e73830d2dbf4e0c2af57795bdd39eca12a8d5fb60d13d60d685264`.
