---
id: SRC-895
---

# Post-checkpoint institutional and scholarly search boundary

- Source ID: SRC-895
- Type: bounded search/negative-space record
- Search date: 2026-08-09
- Status: no new source artifact or outcome recovered

## Search family and result

The following focused searches were run after the `SRC-894` checkpoint:

- `Jason Arday August 9 2026 investigation Cambridge` and `Jason Arday Cambridge investigation outcome August 2026`: results resolved to the already-canonical AP, *Guardian*, *Telegraph*, Cambridge statement, and public-reception records. No final finding, terms of reference, or replacement Cambridge statement appeared.
- `Jason Arday QUB investigation outcome August 2026`: results exposed QUB’s general appeals/procedure material and the already-canonical BBC/QUB report, but no named investigator, terms of reference, correction, or outcome concerning the co-authored article.
- `Jason Arday new publication 2026 DOI`: results returned existing memoir/catalogue and unrelated homonyms; no new DOI/title key was promoted.
- `site:register-of-charities.charitycommission.gov.uk Jason Arday 2025`, Companies House exact-name searches, and exact-name Runnymede/Adult Literacy Trust searches: results reconciled to already-captured First Star, Autism Centre of Excellence, BSA, and patron/governance records. No new appointment, termination, annual report, or correction was recovered.
- `Jason Arday August 2026 event recording`, `Jason Arday 2026 university event report`, `Jason Arday 2026 interview podcast video`, and `Jason Arday 2025 institutional page advisory committee`: results resolved to existing BSA conference, Cambridge, Sanger, podcast, and event records, plus unrelated homonyms. No new recording, transcript, post-event report, or institutional artifact was recovered.
- The current BSA organisation page and 2026 conference abstract-book results were checked against the preserved BSA governance and conference records; they add no distinct Arday source node. The current Cambridge appointment announcement body is byte-identical to the 7 August recheck, and the Taylor & Francis correction route remains the already-preserved 9 August HTTP 403 state.
- A fresh OpenAlex works request for the existing author identifier `A5048886069` (`filter=author.id:A5048886069&per-page=100&sort=publication_date:desc`) returned 56 works, with the newest two DOI-bearing records being the already-captured OSF preprint versions `10.31234/osf.io/h8ezv_v1` and `10.31234/osf.io/h8ezv_v2`; exact title/DOI comparison produced no new publication candidate. The accompanying searches for `Jason Arday` publications, 2026 DOI output, YouTube/video, and podcast routes likewise resolved to existing records, including the Oxford EDB lecture and *How Do You Cope?* episode.
- A fresh ORCID public-API request for `0000-0002-9822-1068` returned the same 11 grouped works already represented in the output index. A fresh Crossref Works request for `query.author=Jason Arday` returned 100 ranked items from 353,692 broad results; its 46 exact-name author matches all reconciled to existing DOI/title records, including duplicate book/chapter manifestations and the two OSF preprint versions. No new DOI, title, full-text route, or institutional-repository manifestation was promoted.
- Exact-name repository searches were also fetched from LJMU Research Online, White Rose Research Online, and Open Research Online. LJMU returned three results, with Arday’s known 2015 thesis the only direct Arday-authored item; White Rose exposed no new Arday record; and Open Research Online returned an HTTP 403 Cloudflare challenge. The result and access states are preserved under SRC-914; no new publication or biography entity was created.
- A targeted media/event search for 2025–26 videos, podcasts, lecture recordings, and event programmes reconciled its material results to existing UCL, ARU, Newcastle, BSA, Oxford, Bath, Crick, RSC, and Broken Vessel records. No new recording, caption track, transcript, programme, or post-event report was recovered; the bounded result is recorded under SRC-915.
- Ohio State affiliation routes were rechecked directly: the general search route exposed no Arday-specific result, the former ODI route redirected to the institution’s DEI reorganization announcement, and a Faculty Affairs search route returned 404. No direct appointment record was recovered; the historical/current visiting-role claim remains contested under SRC-916.
- A fresh public-filing search across Charity Commission and Companies House exact-name routes returned only existing First Star, BSA, Adult Literacy Trust, Autism Centre of Excellence, Runnymede, B.S.A. Publications, Crosstown Traffic, and personal-appointments records. No new appointment, termination, annual report, accounts, or correction was recovered; the boundary is recorded under SRC-917.
- StoryGraph’s memoir review route was rechecked and returned a fresh Cloudflare challenge; public indexing now reports 12 reviews, but no new full review body or media was recovered. This is a changed reception/access state under SRC-918, not independent biography evidence.
- A later 9 August direct fetch of Cambridge’s canonical investigation-statement URL returned HTTP 404 after the same-day HTTP 200 capture under SRC-912. The generic 404 shell and headers are preserved under SRC-919; no statement text or outcome can be inferred from the disappearance.
- Adjacent official-endpoint searches for `site:cam.ac.uk Jason Arday August 2026 review appointment tenure`, `site:jesus.cam.ac.uk Jason Arday resignation fellowship`, and exact-name Charity Commission routes returned only the already-captured Cambridge statement/profile states, generic Jesus College material, and existing Adult Literacy Trust, BSA, and Autism Centre of Excellence records. A direct 9 August fetch of Cambridge Faculty “Our People” page 1 was byte-identical to the 8 August SRC-459 body and still contained neither `Jason Arday` nor `jaa80`; its cache-header change adds no new person or role record.
- A 9 August direct caption check for the locally preserved RSC Inclusion and Diversity Forum 2025 YouTube recording (`JbyQlddjUJ8`) again returned zero-byte responses for the public `en` and `en-GB` timed-text routes. No caption text or transcript was recovered; the 13:24 MP4 remains the canonical local media artifact and no new media node was created.
- The Foyles reader-reviews route for *Great and Unfortunate Things* returned a fresh HTTP 403 Cloudflare challenge on 9 August; its body is byte-distinct from the 8 August challenge, but indexed review text and reception classification are unchanged. No new review text, cover, or downloadable book/audio file was recovered, so the state is recorded under SRC-913 rather than promoted as new memoir evidence.

## Boundary decision

No source node was created for the repeated news, search-result, or homonym results. The search family is closed until a changed official endpoint, named inquiry document/outcome, new DOI, new filing, or distinct media/publication artifact appears. Search results remain leads and are not treated as independent corroboration.

## Continuation sweep — 2026-08-09

A subject-centred continuation sweep tested exact-name searches for 2026 interviews, videos, publications, memoir excerpts, audiobook samples, and launch events. The material results resolved to the canonical *Bookseller* interview (`SRC-131`), the Simon & Schuster memoir record and its browser-visible excerpt (`SRC-091`), the already-captured 2026 memoir edition records, or existing video/podcast nodes. The publisher search exposed no new downloadable book, audiobook, transcript, image, or edition identifier.

The same sweep tested exact-name searches for the Cambridge investigation, hiring-process review, QUB review, and Cofnas-related response. Results resolved to the existing Cambridge, BBC, *Guardian*, *Telegraph*, QUB, Retraction Watch, and commentary records. No formal outcome, terms of reference, correction, direct Arday response, or new primary comparison appeared. A search-indexed Cambridge Faculty profile remains in tension with the direct migrated-host redirect/omission already preserved under `SRC-576`; the indexed page is not promoted as a live current-affiliation record.

Decision: extend the existing boundary rather than create duplicate source nodes or claims. Reopen only for a materially changed publisher excerpt/media endpoint, a named inquiry document or outcome, a direct Arday response, a new DOI/title, or a distinct recording/transcript.

## Re-entry

Start from this record and `NEXT.md`; do not repeat the same broad queries unchanged. Reopen only with a concrete changed URL, date-specific filing, title/DOI, official process document, or distinct recording/transcript.

## Subject-centred continuation sweep — 2026-08-09

A further exact-name sweep tested four focused families: `"Jason Arday" interview video 2026`, `"Jason Arday" publication 2026 DOI`, `"Jason Arday" childhood football snooker interview`, and `site:youtube.com "Jason Arday"`. The results reconciled to the existing Great Big Story/Open Culture family, Twinkl, Guardian, the Lives Retold transcript, the canonical memoir/edition records, and already-catalogued podcast/video manifestations. No new recording, transcript, image, DOI/title key, or downloadable publication artifact was recovered.

A separate exact-name memoir-proposal sweep tested `"Jason Arday" book proposal`, `"Jason Arday" "unrecoverable" car accident`, `"Jason Arday" "testicular cancer"`, and `"Jason Arday" "locked-in syndrome"`. Results pointed to the already-preserved *Atlantic* and *Daily Mail* reports and public discussion of those reports. The underlying 2024 proposal, a publisher response, and primary medical records remain unrecovered; no new source node or claim was created.

Decision: extend the existing source boundary rather than duplicate propagation pages or catalogue manifestations. Reopen only for a distinct primary interview/recording, a new DOI or publisher/repository file, the proposal itself, a direct author/publisher response, or a materially changed source endpoint.
