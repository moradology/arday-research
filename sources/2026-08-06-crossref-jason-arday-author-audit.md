---
id: SRC-203
type: bibliographic index / API snapshot / scholarly-output audit
title: "Crossref exact-author audit for Jason Arday"
subject: ../entities/jason-arday.md
accessed: 2026-08-06
status: public API snapshot and 2026 date-filtered recheck; deduplication boundary
evidence_class: bibliographic index metadata, not identity or publisher verification
updates: ../jason-arday-public-output-index.md, ../research-log.md, ../NEXT.md
---

# Record

Crossref was queried on 6 August 2026 with `query.author=Jason Arday`, `rows=200`, and a limited metadata field selection. The API reported 353,521 results for the broad query and returned 200 ranked items in the preserved response. A local filter retained items with an author whose family name is `Arday` and whose given name begins `Jason`; this produced 47 DOI-bearing records.

A changed 2026-only recheck used `from-pub-date:2026-01-01,until-pub-date:2026-12-31` and returned 100 ranked items. The exact-name filter retained two records: OSF `10.31234/osf.io/h8ezv_v1` and `10.31234/osf.io/h8ezv_v2`, both versions of the already canonicalized under-represented-young-people narrative-inquiry study (SRC-178). No new DOI/title key was found. The complete date-filtered response and the exact-name filtered derivative are preserved separately.

The 47-record exact-name set was compared against the existing source records by normalized DOI. No new Jason Arday work was found. The only literal-text miss was Crossref’s `10.1108/978-1-64113-721-820251018`, which corresponds to the existing teacher-education record’s hyphenated form `10.1108/978-1-64113-7218-20251018` (SRC-074). This is treated as a metadata normalization issue, not a new work.

The broader result set also contains unrelated authors named Arday, including David R. Arday, Anna Arday, Lajos Arday, and A. Arday. The exact-name filter therefore improves recall but does not establish identity. Crossref is a discovery and metadata-reconciliation source, not proof of authorship, publication status, or completeness.

## OpenAlex author-linked recheck

On 6 August 2026, OpenAlex author `A5048886069` was queried for works from 2025-01-01 onward. The response returned seven works: the OSF v1/v2 preprint versions and an undated OSF work manifestation already represented by SRC-178, the BMJ Open protocol already represented by SRC-172, the 2025 book and foreword already represented by SRC-181 and related book records, and a second book manifestation already deduplicated in the *We See Things They'll Never See* edition family. No new Jason Arday publication record was promoted. OpenAlex's author linkage is treated as a discovery index rather than independent identity proof.

## Local preservation

- [Crossref API response](../assets/documents/crossref-jason-arday-author-works-2026-08-06.json) — SHA-256 `ffb6e86011d88b43a7685db7656ed688a3f3f26e185ac65181d8ef3a5d656a09`
- Query URL: <https://api.crossref.org/works?query.author=Jason%20Arday&rows=200&select=DOI,title,author,published,published-online,type,container-title,URL>
- 2026 date-filtered API response: `../assets/documents/crossref-jason-arday-2026-query.json` — SHA-256 `5deaf789f12ed899da71cb8da46b3cce919100084f94ea5d924e116c517263ad`
- 2026 exact-name filtered derivative: `../assets/metadata/crossref-jason-arday-2026-exact-filter.json` — SHA-256 `9a99a025baf4475a9d78056a5413e5f1d03d2a8dc43aaa196205c0284933c74d`
- Recheck URL: <https://api.crossref.org/works?query.author=Jason%20Arday&filter=from-pub-date:2026-01-01,until-pub-date:2026-12-31&rows=100&select=DOI,title,author,published,published-online,container-title,type,URL>
- [OpenAlex 2025–2026 author-linked response](../assets/documents/openalex-jason-arday-2025-2026.json) — SHA-256 `b76aa230ebffbad872ce13bab01a963dfcf251ce2a25729ce7c520b214857543`
- [OpenAlex response headers](../assets/documents/openalex-jason-arday-2025-2026.headers.txt) — SHA-256 `0d939b95a7efa019433007c5b9221d8d5578d163ca3c3e6883745dd7b2ff2af2`
- OpenAlex query URL: <https://api.openalex.org/works?filter=author.id:A5048886069,from_publication_date:2025-01-01&per-page=200&sort=publication_date:desc>

## Boundary and next action

These are ranked Crossref responses, not a complete Crossref export, and OpenAlex is an author-linked discovery index rather than a complete publication register. The 2026-only Crossref slice and the OpenAlex 2025–2026 slice are closed for this recheck date; reopen either only after a changed result, a new DOI/title lead, or a publisher/repository record that is not already represented in the registry.
