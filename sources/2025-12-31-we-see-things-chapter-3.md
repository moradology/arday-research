---
id: SRC-492
type: scholarly book chapter / publisher metadata and access-boundary capture
title: "3 I’ll See You on the Dark Side of the Moon: Mental Health and Illness and the Consequences of Neurotypical Hegemony"
subject: ../entities/jason-arday.md
published: 2025
accessed: 2026-08-08
status: chapter-level DOI and publisher-index metadata verified; direct HTML challenged; no chapter binary claimed
evidence_class: publisher/platform bibliographic record and Crossref metadata; chapter text not locally recovered
urls:
  - https://www.degruyterbrill.com/document/doi/10.1515/9780691263946-007/html
  - https://doi.org/10.1515/9780691263946-007
  - https://api.crossref.org/works/10.1515/9780691263946-007
assets:
  - ../assets/documents/degruyter-we-see-things-chapter-3/page.html
  - ../assets/documents/degruyter-we-see-things-chapter-3/page.headers.txt
  - ../assets/documents/degruyter-we-see-things-chapter-3/crossref.json
  - ../assets/documents/degruyter-we-see-things-chapter-3/crossref.headers.txt
  - ../assets/documents/research-integrity/degruyter-chapter3-jstor/doi.html
  - ../assets/documents/research-integrity/degruyter-chapter3-jstor/doi.headers.txt
---

# Chapter 3 of *We See Things They’ll Never See*

De Gruyter Brill’s publisher/platform record identifies chapter 3, “I’ll See You on the Dark Side of the Moon: Mental Health and Illness and the Consequences of Neurotypical Hegemony,” as a chapter by Chantelle Jessica Lewis and Jason Arday in *We See Things They’ll Never See: Love, Hope, and Neurodiversity*. It gives the chapter span as pp. 76–101 and the DOI `10.1515/9780691263946-007`. The record’s contents list places it after the foreword, preface, acknowledgements, and playlist, and before chapter 4.

This is a chapter-level manifestation of the already canonical co-authored book record [SRC-053](2025-we-see-things-theyll-never-see.md), not a separate book or a sole-authored Arday work. The Crossref record reports a 2025 publication date and an `is-identical-to` relation to DOI `10.2307/jj.26932075.9`; that relation is preserved as metadata, not independently interpreted as byte identity.

## Access boundary

The publisher URL returned an HTTP 202 Amazon WAF challenge with a zero-byte body during local capture. The indexed publisher result remains the evidence for the chapter title, authors, pagination, book, and DOI; no chapter PDF, EPUB, or full-text HTML is claimed locally.

The Crossref `is-identical-to` relation points to DOI `10.2307/jj.26932075.9`, but resolving that DOI locally followed Crossref’s chooser/content-access flow rather than exposing a JSTOR chapter page or file. No JSTOR text or binary is claimed.

## Local preservation

- [Publisher response body](../assets/documents/degruyter-we-see-things-chapter-3/page.html) — zero bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- [Publisher response headers](../assets/documents/degruyter-we-see-things-chapter-3/page.headers.txt) — SHA-256 `810865ada151e05f103a9ce4376d2c8f5034a811e09a027176243d374f687417`.
- [Crossref JSON](../assets/documents/degruyter-we-see-things-chapter-3/crossref.json) — SHA-256 `e39afbac30c945204a27fc0b1fe5732395aa51739e793b8de80e45c068ef9eb4`.
- [Crossref response headers](../assets/documents/degruyter-we-see-things-chapter-3/crossref.headers.txt) — SHA-256 `97a4e0fa53c8636ca2bba37faa73c6b4322861d08d6537d556246cb894bef4bd`.
- [Related DOI resolution body](../assets/documents/research-integrity/degruyter-chapter3-jstor/doi.html) — 5,235-byte Crossref chooser HTML; SHA-256 `18a539bfaf8b29074f1bdea78c72c2ee94b8998b0e559bc2a765c478718f829a`.
- [Related DOI response headers](../assets/documents/research-integrity/degruyter-chapter3-jstor/doi.headers.txt) — SHA-256 `6bd345addb2111296fd741756db2d39b51c7b6e7e9c9bcedd97fefb6263ef697`.
