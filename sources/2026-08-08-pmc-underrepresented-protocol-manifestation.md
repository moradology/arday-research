---
id: SRC-599
type: PubMed Central full-text manifestation / OA-package access audit
title: "Exploring experiences of mental health challenges in under-represented young people — PMC manifestation"
subject: ../entities/jason-arday.md
published: 2025-11-26
accessed: 2026-08-08
status: full-text HTML and OA API captured; linked PDF/package routes bounded
evidence_class: NLM/PMC full-text archive and OA metadata
related: sources/2025-11-26-underrepresented-young-people-protocol.md
urls:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC12658539/
  - https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC12658539
assets:
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/page.html
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/page.headers.txt
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/oa.xml
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/oa.headers.txt
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/article.pdf
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/article.headers.txt
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/reviewer-comments.pdf
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/reviewer-comments.headers.txt
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/package.tar.gz
  - ../assets/captures/2026-08-08-pmc-underrepresented-protocol/package.headers.txt

# PubMed Central manifestation

PubMed Central exposes the complete HTML record for the already-canonical BMJ Open protocol, “Exploring experiences of mental health challenges in under-represented young people (aged 16–24 years) in England: a narrative inquiry protocol” (PMC12658539; DOI `10.1136/bmjopen-2024-098223`). The page identifies Jason Arday as an author affiliated with the University of Cambridge and marks the article as CC BY. The NCBI OA API identifies the record as not retracted and supplies an OA-package link.

This is a distinct repository manifestation, not a new article. It adds a strong public full-text provenance route and an independently checkable non-retraction metadata state. The article’s study methods, ethics/dissemination plan, and author list remain claims about the protocol; they do not establish that planned recruitment or outputs were completed.

## Binary access boundary

The PDF and reviewer-comments links exposed in the PMC HTML returned HTTP 200 HTML wrappers titled “Preparing to download …,” not PDF bytes. The OA API’s package URL returned HTTP 404 XML/HTML rather than the tarball. These are preserved as access states; no PDF or peer-review comments are claimed from them.

## Local preservation

- [PMC full-text HTML](../assets/captures/2026-08-08-pmc-underrepresented-protocol/page.html) — 197,366 bytes; SHA-256 `5bc2ab2d4f788a130b373bd35d3247382e48410d29f0e9c403f8f64a73712674`.
- [OA API XML](../assets/captures/2026-08-08-pmc-underrepresented-protocol/oa.xml) — SHA-256 `8180e18552197c0c7a708fc923a846bd092a07daa179799e78f50a6b7371d030`.
- [PDF download wrapper](../assets/captures/2026-08-08-pmc-underrepresented-protocol/article.pdf) — SHA-256 `b2f5a3ab0e1f258ef924f8664f78560e60b78ad42017b127f4ef450fe97d1f28`; HTML, not PDF.
- [Reviewer-comments wrapper](../assets/captures/2026-08-08-pmc-underrepresented-protocol/reviewer-comments.pdf) — SHA-256 `48144979b17d7bc38dae9a8e5c7f40cf9879b50784ed85884963334037788a62`; HTML, not PDF.
- [OA package 404 response](../assets/captures/2026-08-08-pmc-underrepresented-protocol/package.tar.gz) — SHA-256 `04b10f58e3f1340fc897c7057a0001c82ebd216d8ced1a96a2f05676b5d22494`; XML/HTML, not a tarball.

Reopen only for a changed PMC download state, valid OA package, or distinct public protocol/report output; do not repeat the same wrapper requests.
