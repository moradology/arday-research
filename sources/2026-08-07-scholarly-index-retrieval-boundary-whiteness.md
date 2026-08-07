---
id: SRC-450
type: scholarly-index retrieval boundary
title: "CORE, OpenAIRE, and Semantic Scholar retrieval checks for Arday’s Whiteness and Education article"
subject: ../entities/jason-arday.md
published: 2026-08-07 capture
accessed: 2026-08-07
status: exact CORE/OpenAIRE metadata found; no full-text URL; Semantic Scholar rate-limited
evidence_class: scholarly index/API metadata and access-state responses; not article-text evidence
urls:
  - https://api.core.ac.uk/v3/search/works/?q=doi%3A10.1080%2F23793406.2019.1574211
  - https://api.openaire.eu/search/publications?doi=10.1080%2F23793406.2019.1574211
  - https://api.semanticscholar.org/graph/v1/paper/DOI:10.1080%2F23793406.2019.1574211
assets:
  - ../assets/documents/research-integrity/arday-2018-whiteness/indexes/core-doi.json
  - ../assets/documents/research-integrity/arday-2018-whiteness/indexes/core-doi.headers.txt
  - ../assets/documents/research-integrity/arday-2018-whiteness/indexes/openaire.xml
  - ../assets/documents/research-integrity/arday-2018-whiteness/indexes/openaire.headers.txt
  - ../assets/documents/research-integrity/arday-2018-whiteness/indexes/semantic-scholar.json
  - ../assets/documents/research-integrity/arday-2018-whiteness/indexes/semantic-scholar.headers.txt

---

# Scholarly-index retrieval boundary

An exact CORE API query for DOI `10.1080/23793406.2019.1574211` returned one result matching the article title and author. CORE identifies Durham Research Online as the data provider, but the result has an empty `downloadUrl` and no `fullTextIdentifier`; it therefore adds index corroboration without exposing a file.

An OpenAIRE API query returned one DOI-deduplicated result, with the article hosted by *Whiteness and Education* and an additional “Unknown Repository” instance. Both instances resolve only to the DOI; no repository file or direct full-text URL is present in the response. A Semantic Scholar DOI lookup returned HTTP 429 (“Too Many Requests”) and no paper record on this pass; this is preserved as a rate-limit state, not interpreted as absence.

This is a distinct retrieval-boundary record for canonical SRC-043/SRC-449. CORE and OpenAIRE independently reinforce that Durham is the indexed repository source, while neither exposes the manuscript. The result does not resolve the Cofnas/Rollock comparison, citation or quotation context, authorship provenance, intent, or any institutional research-integrity finding.

## Checksums

- CORE exact DOI JSON: SHA-256 `840e28dd26792005183156c56b386b95e2d4a9112acaddb6c2df796ec1032bfe`
- OpenAIRE XML: SHA-256 `5a31a4c4a3e4a444d2c067095ebbfbc5d0cc30ab97349f2889431c79929dab27`
- Semantic Scholar 429 JSON: SHA-256 `65ab993d12c5c2cc9b68e6da2bb79b326930283e520363ffcdc145f88cd5a148`
