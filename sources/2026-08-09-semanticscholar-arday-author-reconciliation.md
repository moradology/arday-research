---
id: SRC-1130
type: scholarly index / author-identity and paper-topology reconciliation
title: "Semantic Scholar Jason Arday author reconciliation"
subject: ../entities/jason-arday.md
accessed: 2026-08-09
status: four same-name author profiles; one new thesis DOI edge; authorship remains index-attributed
evidence_class: bibliographic index metadata / identity-split and identifier reconciliation
urls:
  - https://api.semanticscholar.org/graph/v1/author/search?query=Jason%20Arday&limit=20&fields=authorId,name,paperCount,citationCount,hIndex
assets:
  - ../assets/documents/semanticscholar-jason-arday-author-reconciliation-2026-08-09.json
---

# Semantic Scholar author reconciliation

Semantic Scholar’s public author search for “Jason Arday” returned four profiles with the exact same displayed name:

| Profile | Reported papers | Reported citations | Reconciled observation |
|---|---:|---:|---|
| `118040777` | 30 | 728 | Main profile; includes the 2015 LJMU thesis and most canonical DOI records |
| `2273134908` | 1 | 0 | Correction DOI, already canonical |
| `2270388304` | 1 | 5 | Book chapter DOI, already canonical |
| `2288194599` | 5 | 13 | 2024–25 co-authored outputs, already canonical |

The paper lists collectively expose the known publication family plus one DOI not previously present in the local DOI corpus: `10.24377/ljmu.t.00004552`, “An exploration of peer-mentoring among student teachers to inform reflective practice within the context of action research.” It is the DOI-bearing Semantic Scholar manifestation of the canonical 2015 LJMU thesis, not a new work. The thesis PDF, repository record, and page-level audit remain the controlling primary artifacts.

## Evidence boundary

This source documents Semantic Scholar’s author splitting and paper-key output. Same-name profile linkage, paper counts, citation counts, and DOI attribution are index metadata, not independent authorship or citation verification. The four profiles are not treated as four people or as a complete author record.

Reopen only for a changed profile merge/split, a new identifier, a thesis-version discrepancy, or a primary publisher/repository record.

## Local preservation

- [Author search and profile/paper reconciliation](../assets/documents/semanticscholar-jason-arday-author-reconciliation-2026-08-09.json)
