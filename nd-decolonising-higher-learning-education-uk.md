---
id: SRC-211
type: Source
title: "Decolonising higher learning education in the UK"
date: n.d. (Durham index lead)
accessed: 2026-08-08
status: indexed repository lead; bibliographic conflict; chapter verification unresolved; volume-level boundary refreshed
source_kind: book chapter lead
entities:
  - ../entities/jason-arday.md
urls:
  - https://durham-repository.worktribe.com/person/303473/jason-arday/outputs?Type=Book+Chapter&page=1
  - https://durham-repository.worktribe.com/person/303473/jason-arday/outputs?page=3
  - https://durham-repository.worktribe.com/orgunit/155354/department-of-sociology/outputs?Author=Jason+Arday&Type=Book+Chapter&page=1

# “Decolonising higher learning education in the UK” — unresolved chapter lead

Durham’s indexed book-chapter output list names Jason Arday as author of “Decolonising higher learning education in the UK,” in a volume attributed to S. Dufoix and S. Mosbah-Natanson. The person-page search result says the volume is *A World History of Sociology* and gives “France: Springer,” while a separate department-of-sociology result for the same Durham output gives “USA: Information Age Publishing.” Neither indexed witness exposes a publication year, DOI, ISBN, chapter pages, publisher chapter URL, or full text. Separate public volume-level witnesses identify the likely host as *Une histoire mondiale de la sociologie*, published by La Découverte in 2024, creating a three-way metadata conflict that is not yet resolved at chapter level.

The alternate Durham result is material because it preserves the English host-title wording and a different publisher field, but it remains an indexed repository rendering rather than a directly retrievable record. The current direct endpoint returns a Cloudflare challenge, so the archive does not choose among Springer, Information Age, or La Découverte.

The 2026-08-07 recheck adds a current Université Paris Cité / GRIP profile for co-editor Stéphane Dufoix. It still describes the project as forthcoming from La Découverte in 2023, which is stale project copy rather than a chapter-level publication record. A separate George Steinmetz CV gives a 2024 La Découverte citation for the host volume, strengthening the volume-level hypothesis but not resolving whether Arday’s English-titled chapter was published there.

This is a discovery lead with a competing volume-level bibliographic hypothesis, not a publisher-verified chapter record. No claim is made here about the chapter’s content, final publication status, DOI, pages, or relationship to Arday’s other decolonisation work.

## Search-index recheck — 2026-08-06

A fresh public search-index result for the Durham person output page (`outputs?page=3`) again renders the title, Arday as author, S. Dufoix and S. Mosbah-Natanson as editors, and *A World History of Sociology* as the host volume. The snippet again says “France: Springer.” This is a changed discovery witness only: direct retrieval of the Durham URL still returns HTTP 403, and a targeted Springer search did not expose a chapter page, DOI, ISBN, pagination, or full text. The La Découverte volume-level witnesses in SRC-213 and SRC-214 therefore remain unresolved competitors rather than superseded evidence.

## Access boundary

The Durham book-chapter index returned HTTP 403/Cloudflare protection during direct retrieval on 2026-08-06. The indexed search result is preserved as the discovery witness; the direct response body and headers are preserved locally. A same-day exact-title pass found zero Open Library records, no exact title among the returned Crossref results, and a Google Books API quota-exhaustion response. A fresh Crossref query for the English host title returned related works but no exact volume; an OpenAlex title search returned related sociology-history works, including Dufoix’s 2021 article, but no exact book record in the captured first 20 results. These are bounded search/access observations, not proof that no catalogue or edition exists. A chapter-level source record should be upgraded only if a publisher, library catalogue, DOI registry, repository copy, or archived page resolves the author/title/volume identity. The IUF and Steinmetz witnesses are preserved separately as SRC-213 and SRC-214.

## National-catalogue recheck — 2026-08-06

The exact final-volume title *Une histoire mondiale de la sociologie* was queried through the public BnF SRU and Sudoc SRU catalogue endpoints. Both returned zero records for the exact title string. These negative results narrow the public catalogue boundary but do not prove that the volume is absent from all catalogue indexes, represented under a variant title, or unavailable through a publisher/library interface not covered by these endpoints.

Local captures: [BnF XML](assets/captures/2026-08-06-world-history-sociology-catalogue-recheck/bnf.xml) and [headers](assets/captures/2026-08-06-world-history-sociology-catalogue-recheck/bnf.headers.txt); [Sudoc XML](assets/captures/2026-08-06-world-history-sociology-catalogue-recheck/sudoc.xml) and [headers](assets/captures/2026-08-06-world-history-sociology-catalogue-recheck/sudoc.headers.txt).

## Publisher/catalogue recheck — 2026-08-08

A fresh exact-title sweep searched the public web, the La Découverte site, BnF/WorldCat-indexed results, and the known volume title in French and English. It again returned the Durham indexed lead and the volume-level Steinmetz/GRIP witnesses, but no La Découverte product page, publisher record, library record, DOI, ISBN, chapter pagination, or lawful full text naming Arday. The result narrows the currently discoverable public boundary without proving that the chapter was never published or that the Durham record is erroneous. No new source ID is created; this is a versioned recheck of SRC-211.

## Direct endpoint recheck — 2026-08-07

A direct fetch of the Durham person-page result at `outputs?page=3` returned a 5,578-byte Cloudflare “Just a moment…” challenge. No indexed result body or chapter metadata was delivered. The HTML and headers are preserved below as a changed retrieval-state observation; it does not alter the existing Springer/Information Age/La Découverte conflict.

## Exact-title and host-volume search recheck — 2026-08-08

A fresh exact-title search again returned the Durham indexed person-page result as the only Arday-specific manifestation. Separate searches for the French host title and its English rendering returned the existing Université Paris Cité/GRIP project profile and Steinmetz CV citation, but no publisher product page, DOI, ISBN, chapter pagination, library record, repository copy, or lawful full text naming Arday. The GRIP profile still describes the project as forthcoming from La Découverte in 2023; the Steinmetz CV cites the volume as a 2024 La Découverte publication. These are mutually relevant volume-level witnesses, not chapter-level proof.

The search boundary is therefore unchanged: the Durham title/author/editor tuple remains a live discovery lead, but the publisher field and host volume cannot be selected from the available evidence. No new source ID, publication record, chapter-content claim, or binary was created.

Search witnesses: [Durham indexed output](https://durham-repository.worktribe.com/person/303473/jason-arday/outputs?page=3), [GRIP profile](https://u-paris.fr/global-research-institute-paris/annuaire/stephane-dufoix/), [Steinmetz CV](https://lsa.umich.edu/content/dam/soc-assets/soc-documents/cvs/CV%20George%20Steinmetz%20March%202024.pdf).

## Local preservation

- [Durham 403 body](assets/documents/durham-book-chapter-page1-403-2026-08-06.html) — SHA-256 `af687e0e419c32c078ca3464c0d2949d9c1713edff07a4aeaea0815bccd9419b`
- [Durham 403 headers](assets/documents/durham-book-chapter-page1-403-2026-08-06-headers.txt) — SHA-256 `634dab3a5e6776820182dd521db26d6c865446971f68218a5655e8a2a8e257ff`
- [Open Library exact-title response](assets/documents/openlibrary-une-histoire-mondiale-sociologie-2026-08-06.json) — zero results; SHA-256 `a68a51a345fbaef76433e2dc9c3af3f7f73ee9f366a07aa6e9eec27944a0f069`
- [Crossref title-query response](assets/documents/crossref-une-histoire-mondiale-sociologie-2026-08-06.json) — no exact title among returned ranked results; SHA-256 `698235fe9063591629683de5d6c5383dd9b3b27d2bc1067d13ad6ea1844e3764`
- [Google Books API response](assets/documents/google-books-une-histoire-mondiale-sociologie-429-2026-08-06.json) — HTTP 429 quota boundary; SHA-256 `3391b214f23873e9d8542b810691e46d861c5cef8c580613d2405cbfbbf45618`
- [Durham department-of-sociology 403 body](assets/documents/durham-book-chapter-orgunit-page1-403-2026-08-06.html) — 5,843-byte Cloudflare challenge for the alternate indexed endpoint; SHA-256 `6c176559b79eebec4cda6578bae5f4edb34418d853932e9d5dd3f8f0d2c8d627`
- [Durham department-of-sociology 403 headers](assets/documents/durham-book-chapter-orgunit-page1-403-2026-08-06.headers) — SHA-256 `5135dbce4ad47c8b356158a6f39f19d7ca14167bb20c6b3e2471468d37838c18`
- [Crossref English-title query](assets/documents/crossref-a-world-history-of-sociology-2026-08-06.json) — 38,174-byte response; no exact host volume in the returned ranked items; SHA-256 `3697a05d9e88704224b755ab124d8875072cf1ecd26f963e4e2fc7fb4cd45768`
- [OpenAlex English-title query](assets/documents/openalex-a-world-history-of-sociology-2026-08-06.json) — 301,230-byte response; related works only in the first 20 results; SHA-256 `2279fe8e4170621890d209247d0f1ad89a675b4d04a068259a8aa13496289787`
- [7 August Durham person-page response](assets/captures/2026-08-07-src211-recheck/page.html) — 5,578-byte Cloudflare challenge; SHA-256 `204cbfad17fb22d7fd1782d51fec7da60fb64f9ac917ae1fc36ba387accba294`
- [7 August Durham response headers](assets/captures/2026-08-07-src211-recheck/page.headers.txt) — direct-fetch headers for the changed retrieval state
