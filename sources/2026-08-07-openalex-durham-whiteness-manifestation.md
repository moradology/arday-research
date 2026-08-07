---
id: SRC-449
type: repository and scholarly-index manifestation
title: "OpenAlex and Durham repository manifestation of Arday (2018/2019), Dismantling power and privilege through reflexivity"
subject: ../entities/jason-arday.md
published: 2026-08-07 capture
accessed: 2026-08-07
status: repository-listed green-OA record; Durham page and OAI probes returned Cloudflare challenges; article file not recovered
evidence_class: scholarly-index metadata plus first-party repository access-state capture; not article-text evidence
urls:
  - https://api.openalex.org/works/https://doi.org/10.1080/23793406.2019.1574211
  - https://durham-repository.worktribe.com/output/1286002/dismantling-power-and-privilege-through-reflexivity-negotiating-normative-whiteness-the-eurocentric-curriculum-and-racial-micro-aggressions-within-the-academy
  - https://doi.org/10.1080/23793406.2019.1574211
assets:
  - ../assets/documents/research-integrity/arday-2018-whiteness/openalex.json
  - ../assets/documents/research-integrity/arday-2018-whiteness/openalex.headers.txt
  - ../assets/documents/research-integrity/arday-2018-whiteness/durham-repository/page.html
  - ../assets/documents/research-integrity/arday-2018-whiteness/durham-repository/response.headers.txt
  - ../assets/documents/research-integrity/arday-2018-whiteness/durham-repository/oai-6267dc7f85bc.headers.txt
  - ../assets/documents/research-integrity/arday-2018-whiteness/durham-repository/oai-6267dc7f85bc.body
  - ../assets/documents/research-integrity/arday-2018-whiteness/durham-repository/oai-1c7ec1fef87c.headers.txt
  - ../assets/documents/research-integrity/arday-2018-whiteness/durham-repository/oai-1c7ec1fef87c.body
  - ../assets/documents/research-integrity/arday-2018-whiteness/durham-repository/oai-239f6c63b61e.headers.txt
  - ../assets/documents/research-integrity/arday-2018-whiteness/durham-repository/oai-239f6c63b61e.body

---

# OpenAlex/Durham repository manifestation

The OpenAlex work record for Arday’s article identifies the DOI, title, journal, and two locations: the Taylor & Francis published-version location and a Durham Research Online repository location. OpenAlex classifies the work as green open access, reports `any_repository_has_fulltext: true`, and describes the Durham location as a CC-BY submitted version; neither location supplies a PDF URL in the captured JSON.

The Durham repository page itself returned an HTTP 403 Cloudflare challenge on 7 August 2026. Two plausible OAI-PMH `GetRecord` routes and the direct `OutputFile/1286002` route were also probed and returned challenge HTML rather than repository metadata or an article file. These responses are preserved as access-state artifacts. The repository page’s indexed search manifestation remains useful metadata, but the archive does not claim that the article text or an accepted manuscript was downloaded.

This is a distinct metadata/access manifestation of canonical SRC-043, not a new publication. It strengthens the record that a repository-held version is indexed and classified as available while documenting the current inability to retrieve it. It does not resolve the Cofnas/Rollock comparison, establish quotation context, or constitute an institutional research-integrity finding.

## Checksums

- `openalex.json`: SHA-256 `39b9e2381d4686a82df925286167125c50a01c53712ae69ed13e2ffc0248322e`
- Durham page challenge: SHA-256 `fd8ac5e9741c3ba8dabc75d88b8bc48e7ecd1692dd9ed5053ac4d4a26216d38e`
- Durham `OutputFile` challenge: SHA-256 `fbc1d71112dd830910164e9d8c72f261b0dd9977c7468225eb1c2be719a2ef84`
