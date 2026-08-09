---
id: SRC-932
type: Source
title: "Great and Unfortunate Things — Norli catalog lead and access boundary"
date: 2026-08-09
accessed: 2026-08-09
status: indexed catalog lead; direct page returned HTTP 403; HTML and headers locally preserved
source_kind: bookseller catalog / search-index manifestation / access boundary
entities:
  - ../entities/jason-arday.md
urls:
  - https://www.norli.no/boker/dokumentar-og-fakta/historie-og-dokumentar/biografier-og-memoarer/great-and-unfortunate-things-9781398542747
---
# Norli catalog lead

Search indexing exposes a Norli bookseller listing for *Great and Unfortunate Things* under ISBN 9781398542747, the distinct 336-page Simon & Schuster Limited edition already represented by `SRC-930`. The indexed result gives the title, author, English hardcover format, expected 27 August 2026 sale date, and publisher-synopsis wording including the council-house/two-brothers formulation.

A direct HTTP request to the canonical Norli URL on 9 August 2026 returned HTTP 403 with a 118-byte body. No product HTML, cover, price, stock state, or additional excerpt was recovered locally. The indexed snippet is therefore preserved as a discovery/topology witness only; it does not independently corroborate the memoir’s autobiographical claims and does not create a second edition node.

## Local preservation

- [Direct HTML response](../assets/captures/2026-08-09-norli-memoir-edition/page.html)
- [Response headers](../assets/captures/2026-08-09-norli-memoir-edition/page.headers.txt)
- [Plain-text extraction](../assets/captures/2026-08-09-norli-memoir-edition/page.txt) — 403 body only
- [Checksums](../assets/captures/2026-08-09-norli-memoir-edition/SHA256SUMS)

## Evidence boundary

Treat this as a low-provenance retailer manifestation of an already-canonical edition. Reopen only for a changed direct page, a lawful product image/excerpt, or a distinct ISBN/format; do not repeat the same request unchanged.
