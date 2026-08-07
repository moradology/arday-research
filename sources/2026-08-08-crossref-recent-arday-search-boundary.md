---
id: SRC-423
type: scholarly-index search audit
title: "Crossref recent-output search boundary for Jason Arday"
subject: ../entities/jason-arday.md
published: 2026-08-08
accessed: 2026-08-08
status: 2024-present Crossref query preserved; no new Jason Arday DOI promoted
evidence_class: bibliographic-index discovery and deduplication record; not proof of completeness
urls:
  - https://api.crossref.org/works?query.author=Arday%2C+Jason&filter=from-pub-date%3A2024-01-01&rows=1000&select=DOI%2Ctitle%2Cauthor%2Cpublished%2Cissued%2Ccontainer-title%2Ctype%2CURL
assets:
  - ../assets/captures/2026-08-08-crossref-recent-arday/response.json
  - ../assets/captures/2026-08-08-crossref-recent-arday/arday-family-matches.json
  - ../assets/captures/2026-08-08-crossref-recent-arday/arday-family-matches.tsv
---

# Crossref recent-output search boundary

The Crossref Works API was queried on 8 August 2026 with `query.author=Arday, Jason`, `from-pub-date:2024-01-01`, `rows=1000`, and a metadata field selection. The response contained 1,000 ranked items—the requested maximum—of which 19 contained an author family name matching `Arday`.

## Reconciliation

Thirteen of the 19 surname matches are genuine Jason Arday records or known manifestations: the 2024 *Elite schools and slavery* article, the two 2024 Belluigi articles, the CoPICS and under-represented-young-people BMJ protocols, OSF versions 1 and 2, the *We See Things They’ll Never See* book/foreword records, and the *Black PhD Experience* foreword identifiers. Every one maps to an existing canonical source record or version/alias in this archive.

The remaining six matches are homonyms or unrelated surname matches, including Anna Arday, Arday Budaya, and other works whose titles and author lists do not identify Jason Arday. They are not added to the ontology.

## Boundary

This closes the exact query for the captured Crossref state without claiming that a 1,000-result relevance-ranked response exhausts all Crossref records. The search should be reopened only with a changed API response, a narrower concrete title/DOI lead, or a different bibliographic index. The raw response and filtered reconciliation are preserved to prevent circular re-searching.

## Local preservation

- Raw response SHA-256: `bdaf0caca8c239d2d14016c35ecd66770deffdf490353c9d36f2dd1dc1d00c3f`
- Filtered JSON SHA-256: `a5a790742f758d17089acc495b13d5a4d2d7921e6ffda77489ebd35f90977d54`
- Filtered TSV SHA-256: `f0fe5b2eb3cb4f0b7ea66025a3e3eabde308777f4bde55333686908656da0f97`
