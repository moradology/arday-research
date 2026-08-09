# Research log

## 2026-08-09 — SRC-1102/C-1302: BBC News NI QUB-report source-version recheck

The canonical BBC News NI article reporting QUB’s review of the 2021 Arday-co-authored paper was fetched again. The 9 August HTML was byte-distinct from the 8 August capture, but the extracted article body was substantively unchanged; only presentation/date formatting and related-link relative timestamps differed. The current page, headers, extracted text, and 1200×675 portrait are preserved. Decision: keep `SRC-610` as the canonical report and register `SRC-1102` as its changed source-version; do not infer a new QUB action or outcome.

## 2026-08-09 — SRC-1101/C-1301: scholarly/library and subject-centred output boundary

Exact-name searches across library catalogues, ISBN/book-chapter results, publisher records, repositories, interviews, childhood profiles, and football/snooker terms were reconciled against the existing source graph. *Cool Britannia*, *The Black PhD Experience*, *We See Things They'll Never See*, and *Great and Unfortunate Things* all returned already-canonical manifestations. A public educational-exam PDF reproduced familiar biography but supplied no independent provenance. Crossref's 2026 exact-author results likewise reduced to the already-canonical OSF v1/v2 records. No new Arday-authored work, full text, interview/video artifact, or independent childhood/sports record was recovered. Reopen only on a concrete new bibliographic key, primary artifact, or independent record; do not rerun the unchanged catalogue queries.

## 2026-08-09 — SRC-1100/C-1300: Soho Agency profile disappearance boundary

The honors/profile search surfaced a Soho Agency expert-page lead for Jason Arday. The canonical route was fetched directly and returned HTTP 404 with a “Page not found” body. A direct WordPress REST search for `Jason Arday` returned an empty array, and an exact-route Wayback CDX request returned no HTTP-200 HTML snapshot. Search indexing still exposes agency-side biography snippets, but no recoverable profile body, portrait, speaker-booking record, or archive replay was found.

Decision: preserve the route as an access/disappearance boundary and do not promote indexed agency copy into the biography. Reopen only after a changed route, lawful archived replay, or concrete cached/print artifact.

## 2026-08-09 — SRC-1099/C-1299: Apple Podcasts manifestation of *Student Sessions*

Apple’s public series page and iTunes Lookup API were captured for the existing 15 December 2023 *Student Sessions* interview. The API identifies the Jason Arday episode by track ID `1000638657541`, gives a 42:04 duration and release timestamp, and points to the already preserved Buzzsprout feed/enclosure. The direct episode route returned HTTP 500; the series page rendered but did not expose the older episode in its current visible shelf. This is a platform-provenance record, not a second interview or independent biography source. No new audio or transcript was recovered.

## 2026-08-09 — SRC-1098/C-1295–C-1298: EDICa team-page capture

The first-party EDICa team page was fetched directly and locally preserved. It lists Arday among the project’s co-investigators, identifies him as Professor of Sociology of Education at Cambridge, states that EDICa was funded from January 2023 through December 2026, and summarizes his associated research areas. A 167×167 page-linked portrait was also captured. The page’s present-tense biography repeats several affiliation fields that are now stale or disputed elsewhere; those are retained as host source-version wording rather than harmonized into current status. This is a distinct project-role record from the earlier EDICa newsletter profile and the UKRI Gateway mismatch.

## 2026-08-09 — SRC-282/C-265 refinement: Arday’s reported BSA-plenary response

The existing *Retraction Watch* record was re-read against the locally preserved HTML. Its article body contains a short quotation attributed to Arday at an April 2026 British Sociological Association plenary: he describes feeling “on the back foot” after an academic-misconduct allegation and says that instruments intended to protect academic integrity, wellbeing, and intellectual property “are weaponised.” The quotation is now represented directly in C-265 and the biography as a reported first-person position. It is not treated as a recovered BSA transcript, an account of the full plenary, or an adjudication of the allegations. Reopen only for the BSA recording/transcript or a materially changed institutional outcome.

The same article reports an earlier email exchange with Dave Harris about alleged similarities in Arday’s 2018 *Social Sciences* article. The reported reply redirects Harris toward anti-racist work and characterizes further contact as bullying/harassment. C-1294 records this as an attributed journalistic reproduction, while the original correspondence, complete thread, and surrounding context remain open.

## 2026-08-09 — SRC-1097/C-1288–C-1293: BBC *Radical* audio audit

The locally preserved 8 May 2025 BBC *Radical with Amol Rajan* MP3 was transcribed with Whisper `tiny.en` and the JSON derivative was copied into the repository with a checksum. The episode’s relevant Arday discussion occupies approximately 15:25–42:48, with subject-centred windows on young people and the present, nostalgia, postwar Britain and Windrush, Churchill and wartime memory, selective “glory days” narratives, and historical complexity. Because the recording is multi-speaker and the ASR has no diarization, claims C-1288–C-1293 are paraphrases with approximate attribution, not quotations or independent verification of the historical propositions discussed. The official transcript remains unavailable. Reopen for human listening, corrected captions, or an official transcript; do not repeat the unchanged transcript search.

## 2026-08-09 — SRC-1094/C-1275–C-1276: Royal Society profile recheck

The Royal Society’s public web-rendered profile was rechecked after the Cambridge resignation. It still presents Arday as a Cambridge Professor and Runnymede/BSA trustee and retains the Diversity and Inclusion Committee term through October 2026. Direct shell retrieval returned the same 1,644-byte HTTP 403 body as the prior capture; only response headers changed, and the new headers are preserved. The profile is retained as a dated institutional biography/source-version and explicitly kept separate from the Companies House/Runnymede termination record, Charity Commission pages, BSA governance page, and Cambridge resignation record. No correction or role-status update was exposed.

## 2026-08-09 — SRC-1093/C-1269–C-1274: Simon & Schuster memoir excerpt recheck

The official Simon & Schuster US page rendered the memoir excerpt through the public web view on 9 August, while direct shell retrieval at 11:19:59 UTC still returned a 403 challenge. The page’s Prologue now supports precise navigation for Arday’s account of the Cambridge appointment call arriving at his Clapham home and Giff’s role; Chapter One supports bounded navigation for the “almost twelve years” language formulation, therapy-room memories, speech therapy beginning around age four three times weekly for the best part of ten years, delayed walking/feeding, fine-motor difficulty, and noise sensitivity. These are self-authored memoir claims. No clinical, school, family, therapist, or Cambridge hiring record was recovered from this recheck, and no new local HTML binary is claimed. The record is deduplicated to SRC-091 and preserves the shell/web access split.

## 2026-08-09 — SRC-1090/C-1266: Eventbrite manifestation of the 27 March 2021 conversation

The public Eventbrite registration page for “Dr Jason Arday — Tackling Racial Inequality in Higher Education” was captured as a distinct manifestation of the existing Black History Month UK listing. Its structured metadata identifies KRIKRAK as organizer, gives event ID `146734225017`, and places the online event at 19:30 UTC on 27 March 2021; the current page marks it ended. The organizer description repeats delayed-speech/literacy, PhD, and platform language, which remains promotional source-version copy rather than independent corroboration. The 2180×1080 event image, HTML, headers, and checksums are locally preserved. No recording, transcript, attendance record, or post-event report was recovered.

## 2026-08-09 — SRC-1091/C-1267: Newcastle lecture Eventbrite manifestation

The Eventbrite link exposed by Newcastle University’s 14 October 2025 lecture page was fetched and preserved. Event ID `1620521697019` identifies “Black History Month Lecture: Sign o’ the times by Professor Jason Arday”; structured metadata gives 17:30–18:30 Europe/London (16:30–17:30 UTC), Curtis Auditorium, and INSIGHTS Public Lectures at Newcastle University as organizer. The page now marks the event ended and sales ended. A 1280×720 promotional image, HTML, headers, and checksums are locally preserved. This is a registration manifestation of SRC-296, not a second event or proof of delivery; no recording, transcript, attendance record, or post-event report was exposed.

## 2026-08-09 — SRC-389/C-1265: publisher abstract recheck for Douglass comparator

Discovery: a current Taylor & Francis search result for DOI `10.1080/13611267.2013.813740` exposed the version-of-record metadata and abstract for Douglass, Dennie L. Smith, and Lana J. Smith’s 2013 article. The abstract describes peer mentoring in undergraduate writing-intensive education courses and survey rankings of mentor characteristics.

Decision: update the existing canonical comparator record and add C-1265 as provenance metadata, not as a new publication node. The publisher page does not expose the full article; the Arday p. 311 “complementarity” row remains open.

## 2026-08-09 — Continuation sweep appended to SRC-895

Subject-centred exact-name searches for 2026 interviews, videos, publications, memoir excerpts, audiobook samples, launch events, Cambridge/QUB process updates, and Cofnas-related responses were rechecked. The publisher result for *Great and Unfortunate Things* exposed the same canonical excerpt already recorded under `SRC-091`; the news and institutional results resolved to existing source families. No new binary, transcript, DOI/title, formal outcome, terms of reference, direct response, or distinct primary comparison was recovered.

Decision: append the boundary to `SRC-895` rather than create duplicate nodes. The next pass should begin only from a changed endpoint or concrete lead, with the Cambridge indexed/live profile mismatch kept separate from current-affiliation proof.

## 2026-08-09 — SRC-1089/C-1263–C-1264: PASSHE participant-witness lead

Discovery: a web search exposed indexed text from Katrina Cochrane’s public LinkedIn post. The post says she attended the PASSHE National Conference and listened to Jason Arday, then attributes a point about rejecting “speed equals excellence” to his remarks in connection with neurodivergent processing and proofreading. Direct LinkedIn retrieval returned a cache miss; the post date, full context, metadata, attachments, and exact wording were not recovered, and no binary was captured.

Decision: register this as participant-witness corroboration for the scheduled PASSHE keynote, not as a first-party delivery record or verified transcript. Add paraphrase-only claims C-1263–C-1264, link the source to the existing PASSHE event family, and keep recording/transcript/slides as open. Reopen only for a changed LinkedIn state, a named attendee artifact, or event media.

## 2026-08-09 — SRC-1088/C-1255–C-1262: Warwick keynote audio audit

The locally preserved 45:25.50 Warwick Education Conference MP4 was processed with Whisper `tiny.en` to create a 66,341-byte VTT for navigation. The audit separates Arday’s keynote and responses from audience questions and records approximate windows covering pedagogy and freedom, generous assumptions and deficit framing, teaching-failure anecdotes, institutional power and fear, humility and safe failure, misrecognition, and intelligence/luck/imposter syndrome. The VTT is automatic speech recognition, not a transcript; no direct quotation is added and human listening remains the next verification step. This is a derivative of `SRC-334`, not a duplicate event node. Google Drive was not updated.

## 2026-08-09 — Newcastle lecture duplicate consolidation

The Newcastle “Sign o’ the times” event had two active source rows (`SRC-232` and `SRC-296`) and two duplicate claims (`C-191` and `C-278`). Their page and portrait checksums are identical. `SRC-296` is retained as the canonical, richer event record because it contains the current-route recheck and complete asset manifest; `SRC-232` and `C-191` were retired from the active graph. Historical log entries retain the earlier ID as provenance of the discovery sequence.

## 2026-08-09 — BOLD and Oxford EDB duplicate consolidation

The active source graph contained two records for the same 25 June 2024 BOLD interview (`SRC-056`/`SRC-218`) and two records for the same 29 October 2025 Oxford EDB lecture (`SRC-185`/`SRC-622`). The richer records already carried the complete local asset or changed-access manifests and were the records used by the current media/claims topology. `SRC-218` and `SRC-622` are now canonical; the older duplicate files and registry rows were retired, while historical research-log entries retain the earlier IDs as provenance. No claims were duplicated or upgraded by this cleanup.

## 2026-08-09 — SRC-607/C-808: OpenAlex scholarly-output recheck

The exact OpenAlex author/work endpoint for `A5048886069` was rechecked directly after a broader 2026 publication sweep. It returned 56 works; the newest unique entries remained the already-canonical OSF v1/v2 narrative-inquiry preprints dated 21 and 23 January 2026. No new DOI/title candidate was found. The raw works JSON and response headers are preserved under `assets/captures/2026-08-09-scholarly-index-audit/`. This is a changed-state recheck of `SRC-607`, not a new publication record.

## 2026-08-09 — SRC-1086/C-1247–C-1251: Cambridge Festival caption audit

The recovered 1:37:40 Cambridge Festival video was mined for subject-centred, attributable windows. The audit separates the host’s biography introduction from Arday’s first-person/public-position passages and records approximate windows on work and opportunity, compassion/restraint, education and multicultural society, political representation, and academic hypersurveillance. YouTube’s English automatic captions contain progressive/duplicated cues and remain navigation only; no direct quotation was added. The audit is a derivative of `SRC-062`, not a second event node. Google Drive was not updated.

## 2026-08-09 — SRC-062/C-1245–C-1246: Cambridge Festival video recovery

The existing Cambridge Festival “Race & Society” record was rechecked after an official YouTube result surfaced for video ID `BAFwM8mIKPk`. The 1:37:40 progressive MP4 was recovered to the local binary archive at `assets/videos/cambridge-festival-race-and-society-2024/race-and-society.mp4` (219,245,637 bytes; SHA-256 `30e7defc871c1d69e24209604e98a1d0c0eb8e9c1a896a92a5addd4c3cb7c972`). YouTube’s English automatic captions were also recovered as a 667,037-byte VTT and are explicitly treated as navigation, not a verified transcript. The source is a changed canonical record, not a duplicate event node; Google Drive was not updated.

## 2026-08-09 — SRC-1085/C-1244: Eventbrite promotional-image recovery

The public Eventbrite manifestation linked from the University of Liverpool’s “Even Flow” listing exposed a 1280×720 promotional JPEG through its CDN. The binary was recovered and checksum-recorded as an addition to the canonical event node. It is preserved as promotional media only: no delivery confirmation, transcript, slides, or Arday portrait was recovered. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1085/C-1241–C-1243: University of Liverpool “Even Flow” keynote

A targeted Liverpool institutional search surfaced the 10 March 2023 University News page advertising Jason Arday’s 13 March keynote, “Even Flow: Understanding and Navigating Neurodiversity,” during Neurodiversity Celebration Week. The page gives a hybrid Teaching Hub/Zoom format and links Eventbrite. The current Eventbrite metadata resolves the event title, 1–2 PM time, Liverpool venue, and event ID `566383697887`, adding a distinct registration manifestation. The University page repeats biography claims about autism, speech, literacy, and Cambridge; these remain host-published biography wording rather than independent records. The event’s recording, transcript, slides, and Arday-specific image were not recovered. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1084/C-1238–C-1240: University of Liverpool race-equity activities

The University of Liverpool Faculty of Health and Life Sciences page “Advancing Race Equity and Celebrating Black History Month: A relay race, not a marathon” was fetched from the first-party site and preserved with its response headers. Published 12 October 2023 and written by Carl Larsen, it includes a photograph captioned “Prof Jason Arday and Carl Larsen.” The article reports Arday’s Liverpool work on “Inclusivity library exhibits,” including a Henrietta Lacks exhibit in the Harold Cohen Library, and a Black Science Bootcamp with Amal Abdulkadir for 55 Black Year 10 students from Liverpool schools. The source is useful evidence of named institutional activities and public-facing race-equity work, but it does not provide an exhibit catalogue, participant register, evaluation, or recording. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1083/C-1235–C-1237: University of Manchester Black History Month listing

Discovery: a targeted institutional-event search surfaced the University of Manchester’s 25 September 2024 StaffNet programme. It schedules Arday for a 30 October panel, “Black History Month, The Bicentenary and Beyond,” with named Manchester academics and a topic frame covering Black contributions, the Race Equality Charter, inclusive teaching, career development, student initiatives, and legacies.

Capture: the StaffNet HTML, response headers, and 700×420 generic programme image were preserved. The linked TicketSource page returned a Cloudflare challenge; no ticket details, recording, transcript, slides, post-event report, or Arday portrait was exposed.

Decision: add a dated first-party event-listing node. Treat delivery and remarks as unresolved; do not infer that Arday attended from the schedule or use the generic image as a portrait.

## 2026-08-09 — SRC-640/C-1229–C-1232: UEL ethnicity-pay-gap report recheck

Discovery: a targeted report search surfaced current indexed text for UEL’s *Bridging the Gap: Closing the Ethnicity Pay Gap in the UK*, which names Arday among contributors and directs readers to Appendix G, page 40. The same indexed text identifies the Office for Institutional Equity as producer and Samson Olagbami as writer/collator.

Capture: the UEL PDF route returned a byte-distinct Akamai 403 response; the linked FlippingBook route returned a publication-unavailable page. Both rechecks are preserved under the existing conference source family. No PDF body, page image, recording, transcript, or speaker-attributed Arday passage was recovered.

Decision: update SRC-640 in place rather than create a duplicate report node. Add only the contributor-listing, report-method framing, and changed-access claims. Keep Arday’s panel role and the report’s general recommendations separate from any verified account of what he said.

## 2026-08-09 — SRC-1081–SRC-1082/C-1224–C-1228: Invesco race/neurodiversity conversation

Discovery: targeted 2024 event/interview searches surfaced Invesco’s report, syndicated by London South East, on a Black History Month conversation with Jason Arday. A separate search surfaced Invesco’s 2023 UK Stewardship Code report, whose Cambridge Judge Business School case study records a Black History Month session with Arday on the same subject.

Capture: the LSE route returned a Cloudflare 403 challenge, which is preserved locally. The indexed article text was read through the public search/open result. The current Invesco PDF route returned 404, while indexed PDF text exposes the relevant printed p. 25 passage; no recording, slides, image, or attendee register was recovered.

Decision: add two documentary source-version records but one event family. Claims are limited to event context, Arday-attributed accounts of Gifty and Sandro Sandri, masking/microaggressions/agency themes, and the report’s fundraising wording. The corporate reports are promotional/documentary witnesses, not independent corroboration or verbatim transcripts. Google Drive was not updated.

## 2026-08-09 — SRC-1080/C-1218–C-1223: 2013 peer-mentoring article page audit

The complete LJMU Open Journals issue PDF was audited at article level. The pass binds the title/byline and printed page coordinates to the article’s own scope statement, distinguishes its literature-based contextual synopsis from original empirical research, maps its reflection/apprenticeship/reciprocity framework, records its discussion of mentoring risks, and captures its explicit caution against a universally superior approach.

The article’s recommendations for peer-mentoring circles, institutional support, roles, trust, communication, and review remain practice arguments without reported implementation or causal outcomes. Added SRC-1080/C-1218–C-1223; Google Drive was not updated.

## 2026-08-09 — SRC-1079/C-1212–C-1217: expanded Bookseller memoir-interview page audit

The current *Bookseller* rendering was rechecked after the archive’s earlier excerpt/login boundary. The retained HTML and current page expose a continuation after the prior “Continues…” marker. The audit adds publishing-process details, Arday’s scrutiny account, the memoir’s interest/ability portrait, a midwife anecdote, and the “less than 1%” structural framing while preserving the BTEC/Sandro overlap as already represented.

The added passages remain trade-publication reporting, memoir content, or attributed self-report. No publishing contract, birth record, sporting record, or underlying professorship statistic was recovered. SRC-1079 is linked to SRC-131 rather than counted as a new interview; Google Drive was not updated.

## 2026-08-09 — SRC-1078/C-1206–C-1211: Guardian black-history curriculum commentary audit

The live Guardian page was audited as a dated authored-commentary source. The pass separates Arday’s education/anti-bigotry framing, cited Macpherson and Windrush policy references, empire and Black-contribution curriculum argument, Olive Morris/intersectionality and attainment claims, Black Curriculum description, and implementation recommendations from independent evidence.

The page is opinion rather than peer-reviewed research; its 15 June 2020 modification date and Durham assistant-professor biography are retained as source-version metadata. The underlying policy reports, curriculum outcomes, and implementation effects remain open research boundaries. Added SRC-1078/C-1206–C-1211; Google Drive was not updated.

## 2026-08-09 — SRC-1077/C-1200–C-1205: BBC Newsnight PhD-offers page audit

The live BBC Newsnight article published 17 November 2020 was audited as a dated source-version. It records the reported FOI scope and response counts, the white/Black offer-rate comparisons, and Arday-attributed passages on being taught by no person of colour, doctoral selection, funding work, inaccessible funding information, and structural inequality.

The article’s figures remain BBC-reported analysis: raw FOI returns, denominators, offer definitions, and the broadcast file are not locally available. Arday’s recollections and positions remain separate from those figures and from later HESA-based scholarship. Added SRC-1077/C-1200–C-1205; Google Drive was not updated.

## 2026-08-09 — SRC-1076/C-1194–C-1199: Social Science Space interview audit

The Sage *Social Science Space* page was audited from its full publisher transcript, with the local MP4 and automatic captions retained as audiovisual source versions. The pass isolates Arday’s interviewer role and speaker-labelled passages: his race/intersection self-description, friendship and series-editor framing, attribution of the “white narcissism” term to Keval, questions about racial inequality and precarity, compassion praise, and closing endorsement. Keval’s answers were excluded from Arday’s claims.

The page’s 9 April 2025 date is publication metadata; no recording date was exposed. Added SRC-1076/C-1194–C-1199; Google Drive was not updated.

## 2026-08-09 — SRC-1075/C-1186–C-1193: Cambridge Student interview page audit

The revised *Cambridge Student* interview was audited as a source-version rather than a new interview. The current page’s revision notice and three archived replays establish that revised wording was already present in the earliest recovered snapshots; the pre-revision text was not recovered. The audit extracts Arday’s modernisation/accessibility agenda, slavery-legacies and reparative-acts position, Simon Woolley parliamentary-scheme narrative, anti-assimilation/belonging position, Foundation Year/outreach view, appointment/Black-women selection critique, and an unverified 45% survey statistic.

Repeated childhood, charity, and appointment biography material was not duplicated. The page’s historical “incoming Fellow” wording remains a source-version, not current appointment evidence. Added SRC-1075/C-1186–C-1193; Google Drive was not updated.

## 2026-08-09 — SRC-1074/C-1179–C-1185: MMU LEED keynote caption audit

The locally preserved Manchester Metropolitan University MMUtube keynote was audited against its official English (British) SRT. The pass binds the recording and 81%-accuracy caption boundary to timecoded passages on Arday’s PE-teacher/Sainsbury’s route, mother and social-causes recollection, relational education and hidden curriculum, Sandro Sandri memory, staff-precarity argument, play/culture pedagogy, and PE-informed teaching philosophy.

These are first-person recollections and public educational positions, not independent employment, family, workload, or outcome records. The SRT remains a navigation aid rather than a verbatim transcript; human listening is still required for quotation. Added SRC-1074/C-1179–C-1185; Google Drive was not updated.

## 2026-08-09 — SRC-1071/C-1161–C-1165: under-represented young people protocol page audit

The already-canonical 2025 BMJ Open protocol was audited at page level using the preserved Oxford Research Archive version-of-record PDF. The audit binds the study’s planned narrative/intersectional design, Work Package 1/2 sampling targets, youth-participation and autism-adjustment structure, ethics/data-management statements, and funding/sponsorship topology to printed pages 1–8.

Most importantly for the subject record, the contributor statement on PDF p. 8 says “JA leads work package 1 with KB” and substantially contributed to writing the application, while also stating that all authors substantially contributed to the protocol. This is direct contribution evidence, not an inference from author order. It does not establish principal-investigator status, Oxford employment, study completion, recruitment, or results. Added SRC-1071/C-1161–C-1165; Google Drive was not updated and GitHub remains the active publication target.

## 2026-08-09 — SRC-1072/C-1166–C-1171: *The black professoriate* page audit

The six-page *On Education* article already had a canonical publication record and local PDF, but its substantive pages had not been audited. The page-level pass classifies it as a succinct synthesis rather than an original empirical study, binds its dated HESA/UK-professor and Black-women figures to pp. 1–3, maps its mental-health argument and recommendations across pp. 2–5, and preserves the final-page 2022 biography as a source-version.

The article is therefore useful for reconstructing Arday’s published public-intellectual position and the evidence he cited, but not as an independently verified dataset or as proof of implementation. Added SRC-1072/C-1166–C-1171; no second publication node was created.

## 2026-08-09 — SRC-1073/C-1172–C-1178: *More to prove and more to lose* page audit

The 22-page Glasgow “Published Version” was audited at printed-page level. The audit records the article’s CRT/epistemological frame, convenience sample of 18 staff of colour across 10 universities, questionnaire/interview/focus-group procedure, three reported themes, positionality discussion, explicit non-generalisability limitation, and recommendations about precarious employment and racism.

The 2020 Durham *Living Hand to Mouth* record remains a separate manuscript lead because its full text is not public in the archive; no version identity or concealment inference was added. The methods sequence is noted as a future comparator route, not converted into a plagiarism or misconduct claim. Added SRC-1073/C-1172–C-1178; Google Drive was not updated.

## 2026-08-09 — Repository publication/link-integrity closure for SRC-036/SRC-921

The canonical root-level records for the 20 March 2021 BBC/Lives Retold transcript and its 28 June 2023 Wayback PDF recovery were present in the working tree but not yet tracked by Git, despite being referenced by the claims ledger, timeline, biography, media index, and source registry. Their provenance and claim bindings were rechecked; root-level `assets/` and `sources/` links were corrected, and the two Markdown records are now included in the published repository. The recovered PDF, extracted text, headers, and live-404 boundary were already tracked and were not duplicated.

## 2026-08-09 — SRC-1067/C-1144–C-1147: LSTM report page-level audit

The locally preserved 21-page LSTM report was read through its substantive pages rather than treated as a single broad source summary. The report says its framework centres lived experience, allows local themes to emerge, and is intended to expose the gap between institutional principles and implementation. Its p. 12 “key points of note” say only a fraction of interviewed staff of colour joined focus groups, suggesting distrust and/or fear of speaking out; the same page notes a gender imbalance across groups and a mismatch between desk-review material and participant experience.

The audit maps pp. 13–19 recommendations across culture, recruitment/progression/promotion, student experience, leadership/communication, academic/professional services, and reporting processes. The conclusion on pp. 20–21 foregrounds exclusion, progression, racism reporting/management, and intersectionality—especially Black women and other women of colour—and says these findings informed an LSTM-specific standards/indicators framework. Added C-1144–C-1147 and SRC-1067. These remain commissioned-report analysis and recommendations, not independently re-audited participant evidence, implementation proof, or evidence about Arday’s personal biography. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1068/C-1148–C-1152: ARU Unlearn video audit

The locally preserved 1:35:35.02 ARU Unlearn/Lightbulb MP4 was sampled with `mlx-community/whisper-small.en-mlx`. The audit isolates Arday’s opening keynote from the host introductions and later material. It adds approximate navigation for his use of music and sport as common ground; belonging and neurodivergence as fluid/action-oriented; academia, exclusion, and praxis; precariousness and neurodivergent experience; an unnamed colleague anecdote; and collectivism as a route to workplace freedom and belonging.

The host introduction was not promoted as biography evidence: the machine pass contains title, affiliation, and honorary-degree errors, including wording apparently placing an honorary doctorate at Cambridge in 2015. Added C-1148–C-1152 and SRC-1068. ASR remains a navigation aid rather than a transcript; human verification is open before quotation, and none of the social claims or anecdote is treated as independently established. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1069/C-1153–C-1155: *The Fire Now* preview audit

The locally preserved PagePlace/Bloomsbury preview was read at printed-page level. It is 31 pages of front matter and opening-book material, not the 26–37 chapter body. The contents identify Arday’s chapter, the contributor page carries dated Roehampton/Ohio State/Runnymede biography wording, and the editors’ introduction says the chapter considers racial microaggressions in academic institutions and their effects on Black academics. Added C-1153–C-1155 and SRC-1069. No chapter argument, evidence, citations, or conclusion was promoted; the missing-body state remains an explicit retrieval lead. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1070/C-1156–C-1160: *Routes to Intellectual Authority* page-level audit

The 29-page QUB publisher/version-of-record PDF was audited at printed-page level. The article’s method section describes a critical quantitative analysis of HESA data covering 24,530 academic staff, uses QuantCrit as a guiding framework, and explicitly discusses category construction, missingness, and the danger of treating administrative data as neutral. Selected results were bound to pages 311–317: the reported composition percentages, junior/senior concentration, and no observed promotions of “black staff” to full professor in Education. The conclusion on pp. 321–323 was recorded as co-authored interpretation about intersecting racial, gendered, geopolitical, and hierarchical inequality and institutional accountability. Added C-1156–C-1160 and SRC-1070; no independent reanalysis or Arday-only attribution was made. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1058/C-1107–C-1110: PBS early-intervention caption audit

The locally preserved 2 September 2023 PBS segment was checked against its official English VTT. The audit adds subject-centred details about continued speech/language work from roughly ages 11–16, Arday’s retrospective interpretation of the non-verbal period as observational, a reported reading age of 12 at university, a 500-words-a-day writing practice over roughly 15 years, and the Sandro Sandri PhD anecdote. These are preserved as first-person testimony and caption-derived source-version claims. PBS host narration and superlatives remain separate from Arday’s account; no therapy, assessment, writing log, or independent mentorship record was found in this pass. The MP4 remains locally available for later human waveform verification before verbatim quotation.

## 2026-08-09 — SRC-1059/C-1111–C-1113: *Neurodivergent Show* caption audit

The locally preserved 4 March 2023 interview was checked against its automatic English VTT. It adds a source-version detail about removing a hearing aid during exercises, a fuller first-word scene in which Arday says his mother prompted him to repeat “hello,” an interpreted perseverance/“unfavourable odds” framing, and a more granular account of being 18 with a reported reading age of eight before Sandro Sandri encouraged a university path. The captioned diagnostic wording is retained as remembered testimony and is not modernized or treated as a clinical record. The machine-rendered mentor name/dialogue and all substantive details remain pending human verification against the MP4.

## 2026-08-09 — SRC-1060: Wellcome Sanger interview source-version audit

The existing Wellcome Sanger Institute interview record was checked against its locally preserved automatic English captions. The audit binds the already-recorded PhD/medical, career, research/counselling, and Black-history-curriculum passages to precise navigation windows and existing claims `C-1030–C-1034`. It creates no duplicate claims and does not upgrade any self-report, host description, medical account, qualification, employment chronology, or educational argument into an independently verified fact. Human audiovisual verification remains open.

## 2026-08-09 — SRC-1061/C-1114–C-1118: UCU decolonisation webinar audit

The opening 00:29–09:40 contribution of the locally preserved 22 July 2020 UCU webinar was checked against its automatic English VTT. It adds a coherent public-position record: decolonisation as changing what institutions teach, learn, and research; Global South knowledge and disciplinary-canon critique; student-led activity and a captioned “Keele” manifesto/events/race-charter account; and an explicit warning against symbolic management-led tick-box work. Later speakers were excluded. The institution/name spellings and implementation claims remain source-versioned pending audiovisual or independent institutional verification.

## 2026-08-09 — SRC-1062/C-1119–C-1122: Royal Greenwich panel audit

The first 00:55–07:22 contribution of the locally preserved 9 October 2020 Royal Greenwich Black History Month panel was checked against its automatic English VTT. Arday’s segment adds a dated public-position record on historical amnesia, Black history as British history, classroom belonging, cited attainment-gap/Census figures, and an education-to-prison “pipeline” framing. The later panelists were excluded. Numerical and causal propositions remain attributed source versions pending identification of the underlying reports or human audiovisual verification.

## 2026-08-09 — SRC-1063/C-1123–C-1127: BETT interview audit

The preserved 28 January 2024 Teachers Talk Radio BETT interview was checked against its automatic English VTT. Arday’s subject-specific passages were separated from the interviewer and recorded as dated source versions: academic self-description, 1990s music preferences, secondary-school-teacher self-report, classroom risk/play and metrics critique, impostor-syndrome advice, and an inclusive-education/teacher-toolkit position. No childhood or qualification claim was duplicated. Captions remain unverified against the MP4.

## 2026-08-09 — SRC-1064/C-1128–C-1132: Speakers Corner interview audit

The preserved 13 December 2023 Speakers Corner interview was checked against its English and original-English SRT tracks. Arday’s answers were separated from the host and expanded from the existing broad C-218 record into five dated public-position nodes covering social stagnation and motivation, constructive disagreement, media responsibility, adaptive education, and belonging/membership. No childhood or qualification claim was duplicated. The caption tracks contain overlap and recognition errors; human listening remains open.

## 2026-08-09 — SRC-1065/C-1133–C-1138: BME ECR keynote audit

The 22 July 2023 BME ECR recording was checked against its automatic English SRT. The first 01:42 host biography was excluded because of substantial recognition/title errors; Arday’s 01:43–12:18 keynote was isolated from the later audience material. The audit adds dated source-version records for his conference-opportunity recollection, collectivist community framing, love/empathy values, sleep-related self-report, Black-women agency argument, and hope/pioneer framing. No current appointment or childhood claim was promoted.

## 2026-08-09 — SRC-1066/C-1139–C-1143: UCL keynote slide audit

The locally preserved UCL “Learning to Fly” PPTX was read at slide level by extracting its text from the OOXML package. The audit expands the existing deck summary into five bounded records covering the declared scope, Whiteness/curriculum argument, practical interventions, the explicitly cited and qualified unconscious-bias discussion, and recommendations on race/racism conversations, representation, BME student voice, and collective responsibility. The deck remains authored presentation material rather than an independent evaluation or transcript of the 42-minute recording.

## 2026-08-09 — SRC-1057/C-1104–C-1106: LBC source-propagation/commentary audit

The locally preserved 8 August 2026 LBC video was checked against its English VTT. It repeats the existing controversy narrative, records presenter James Hanson’s reported shift from an initially nuanced position after the Jack Grove/Met account, and adds commentary framing Arday as a possible victim or symbolic “mascot” of DEI. No new primary document, Arday interview, institutional finding, police record, or appointment record was recovered. The evaluative language is preserved as commentary/reception evidence only.

## 2026-08-09 — SRC-1056/C-1099–C-1103: Channel 4 resignation-report caption audit

The locally preserved 6 August 2026 Channel 4 report was checked against its English VTT. The audit separates Cofnas’s attributed dissertation allegation, Channel 4’s report of the LJMU/PhD-status and journal-correction positions, Cambridge/Jesus process reporting, Arday’s response and academic-standards defence, and the pig-head/Glasgow/Ohio State disputes. Nothing is promoted as an adjudicated finding: the captions are machine-generated, the report is mediated broadcast journalism, and the underlying analysis, procedure files, police record, correspondence, and historical appointment records remain unavailable or unresolved.

## 2026-08-09 — SRC-1055/C-1095–C-1098: Oxford Challenges & Changes caption audit

The locally preserved 25 March 2021 Oxford Physics recording was checked against its automatic English SRT for Arday-attributed passages. He names the Leading Routes collaborators behind the *Broken Pipeline* work, describes presenting it to the Office for Students, presents doctoral-funding and Russell Group pay figures, and states that lived accounts of racism should not be neutralized merely because they are not statistical. The funding figures are preserved as a talk-version alongside the separate 2019 report, whose denominators differ; no figures, OfS response, or BBC-study method are upgraded without the underlying records. Captions remain unverified against the waveform.

## 2026-08-09 — SRC-1054/C-1091–C-1094: Cambridge Neurodiversity Week caption audit

The locally preserved 22 March 2024 Cambridge film was checked against its automatic English SRT. The bounded passage adds Arday’s fluid, experience-sensitive framing of neurodiversity; a retrospective account linking inclusive-curriculum work to school ostracization and opposition to one-size-fits-all pedagogy; a description of his collaboration with Chantelle Lewis on love, compassion, and empathy in learning spaces; and a dated observation of Cambridge interventions for neurodivergent learners. These are distinct professional/public-position details, not new childhood or clinical evidence. Captions remain unverified against the waveform.

## 2026-08-09 — SRC-1053/C-1088–C-1090: Black In Academia public-position caption audit

The locally preserved 5 November 2018 Black In Academia / Leading Routes 65-second response was checked against its automatic English VTT. The short first-person statement records Arday’s account of stereotype pressure on Black men, the representational responsibility he associates with Black academics, and his view that Black presence in academia is a political statement that can reshape narratives and inspire participation. These are distinct early public-position details, not childhood or qualification evidence. The captions remain unverified against the waveform and are not used for verbatim quotation.

## 2026-08-09 — SRC-1052: Beacon College profile access/attribution boundary

The locally preserved 5 September 2023 Beacon College *Difference Makers* profile was rechecked at the page/metadata level. Its description repeats known childhood speech/literacy, autism, and Cambridge-appointment framing, but no public subtitle track was exposed and the available environment had no speech-to-text runtime for a machine-assisted audio pass. The video-only MP4 and separate M4A remain playable local artifacts. No new Arday-attributed wording or biographical claim was promoted; reopen only for human listening, a changed caption/transcript endpoint, or an independently supplied transcript.

## 2026-08-09 — SRC-1051/C-1084–C-1087: St Mary’s address family/mentor caption audit

The locally preserved 26 July 2024 St Mary’s honorary-doctorate address was checked against its automatic English SRT. The captions attribute to Arday a first visit to St Mary’s at 15 during a school-arranged sports day, a major age-18 intervention from a person rendered as “Andrew Sandry,” parents named Gifty and Joseph Addai, and a memory of his mother reading *Invictus* daily until age 18. The mentor name conflicts with the Sandro Sandri rendering in other institutional and interview records; it is preserved as a source-version discrepancy rather than normalized. The claims remain ceremonial first-person testimony and the captions remain unverified against the waveform.

## 2026-08-09 — SRC-1050/C-1080–C-1083: Diversity Seminar childhood-caption audit

The locally preserved 4 February 2025 Diversity Seminar interview was checked against its automatic English SRT for the 05:10–08:55 personal-story passage. Arday gives the “3, 11, 18 and 37” sequence, describes diagnosis/global developmental delay, speech and literacy timing, credits his mother and college tutor Sandro Sandri, and gives a dated Glasgow-at-35/Cambridge-at-37 professorship chronology. The passage is a distinct first-person source-version that materially links the recurring childhood narrative to his own interpretation of observation, learning, and mentorship. Captions contain recognition errors and remain unverified against the waveform; no clinical, school, or appointment claim is independently upgraded. The source is deduplicated to SRC-241.

## 2026-08-09 — SRC-1049/C-1076–C-1079: Cambridge panel childhood-caption audit

The locally preserved Cambridge “Black Men On The Couch” recording was checked against its automatic English VTT for a bounded Arday passage. Between approximately 01:16:24 and 01:20:30, the captions attribute to Arday his age-three diagnosis of global developmental delay and autism, non-speaking until age eleven, and a description of observing the world before speech rather than having ordinary internal dialogue. An earlier passage records his self-description of nighttime stillness and insomnia. These claims are useful subject-centred biography evidence, but the VTT is an imperfect automatic caption track and has not been human-verified against the waveform; no clinical or developmental fact is upgraded from it. The material is deduplicated to SRC-263, with SRC-1049 providing the bounded audit.

## 2026-08-09 — SRC-1048/C-1048–C-1050: Surviving Society E031 opening-window audit

The locally preserved 1:11:45.64 HLS AAC for the 23 April 2019 “Growing up Black in the 90s” episode was sampled with word-timestamped ASR in the opening five minutes. Arday places the proposed book in his childhood in South London/Clapham, recounts an age-14 encounter with a local drug dealer who told him to keep his head in his books, and recalls his mother keeping him and his brothers awake for late-night television to access Black heritage and culture. These are first-person autobiographical and cultural-memory passages; the audio is a podcast conversation and the ASR is not a verbatim transcript. The source adds subject-centred childhood detail to SRC-197 without creating a duplicate episode node. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 15:00. A clearly Arday-attributed window adds his reference to an undergraduate dissertation on the 1993 Millwall by-election and the BNP, followed by a first-rave-in-1993 account and an analysis of racial coding in house/garage scenes. A co-host’s separate childhood-racialization story in the same window was explicitly excluded. Proper names, venue names, and all autobiographical details remain machine-assisted and source-layered rather than independently verified.

The audit was extended again through approximately 20:00. Arday says his first album was Oasis’s *Definitely Maybe*, bought at about age 13, and then gives an explicit Stuart Hall–influenced account of culture as politically and socially consequential, with solidarity as a problem. The former is first-person cultural memory; the latter is public analysis. The remainder of E031 remains unaudited at claim level.

The audit was extended through approximately 25:00. Arday gives a detailed first-person account of a stop-and-search at 14 while with three white friends, and describes the resulting loss of innocence and heightened vigilance. This materially deepens the childhood evidence map, but it remains self-report and overlaps the earlier New Humanist version without independently corroborating it. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 30:00. Arday connects his response to police encounters with a childhood fascination with Björn Borg’s calm temperament, which he says he learned from his father’s videos/cassettes, and describes the dilemma of remaining composed versus resisting. The conversation then shifts to a co-host’s separate account, which was excluded. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 35:00. A clearly attributable Arday passage discusses the social currency he associates with being an educated Black man and the greater racialized burden he says Black women face in academia; he explicitly qualifies this against treating all Black men’s university experiences as privileged. Host testimony in the surrounding interval was excluded. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 40:00. Arday describes approaching police when they pat down children, offering to wait with the child, and says he had done this more than ten times in the preceding month. He also rejects racialized “bad choices” explanations for young Black boys’ treatment and discusses class/racialization. These remain self-report and public-position records; surrounding media statistics were not promoted. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 71:37, covering the substantive close of E031. Arday discusses rooms where women of colour do front-line anti-racist work, says he would ask what support is useful, and describes wanting to use acquired social capital for behind-the-scenes support and elevation of marginalized people. A closing clothing discussion records his interest in tailoring and his self-report that he used to make clothes; the final sign-off adds no claim. The 71:45.64 recording is now navigated nearly to its end, but human verification and a verbatim transcript remain open. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 45:00. Arday argues for engaging youth cultures rather than policing Black young people through assumptions, recounts a family-mediated memory of his father experiencing racism as an Arsenal supporter watching John Barnes, and critiques individual-choice explanations of racialized outcomes. Host discussion and unverified media statistics remain excluded. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 50:00. Arday recounts a recent 2019 London music-event experience involving repeated racist abuse, says he and his younger brother left early, and explains his decision to speak up for the sake of children. He also describes mentoring young people across multiple identities and rejects forced assimilation. Venue/event details remain unverified, and the host’s adjacent account was excluded. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 55:00. After excluding mixed speaker material, the Arday-attributed passage records his account of being challenged at Stone Roses shows and his comparison of inclusion in Black cultural spaces with exclusion signaled by white-coded music scenes. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 59:15. Arday describes his younger brother accompanying him to gigs for safety, identifies rock and roll and its Black origins as central to his music identity, and discusses public-transport racism and the racialization of food. The final minute and earlier mixed-speaker material remain outside the claim ledger. Google Drive was not updated; GitHub remains the active publication target.

The audit was extended through approximately 65:00. Arday’s clearly attributable closing passage describes clarity and temperament as his strengths in challenging racism, and calls on Black men to share anti-racist labor historically carried by women of colour. Earlier mixed-speaker material and the remaining tail were not promoted. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1045/C-1045: Cumberland Lodge audio audit

The locally preserved 59:10.38 SoundCloud MP3 for the 3 November 2021 “Beyond Tokenism” panel was audited with bounded ASR windows. The host introduction places Arday on the panel, and an approximately 05:00–07:00 segment contains an Arday-attributed response on tokenism, structural whiteness, personal experience, and the distribution of benefit to people of colour, especially women of colour. The host’s immediate hand-off supports the attribution, but this remains a machine-assisted navigation result from multi-speaker audio, not a manually verified transcript. It adds a source-layer public-position record to SRC-618 and SRC-1008 without creating a duplicate webinar node. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-1028/C-1028: page-level audit of 2018 mental-health article

The open-access MDPI PDF for “Understanding Mental Health: What Are the Issues for Black and Ethnic Minority Students at University?” was read page by page. The audit records the stated design (32 participants, 14 UK universities, questionnaires, two focus groups, 32 individual interviews), recruitment and analysis details, reported themes, recommendations, and the article’s explicit limitations. It does not treat the article as a clinical finding or as independently reproducible beyond the public text: raw transcripts, coding files, recruitment records, and ethics documentation were not exposed. The artifact is deduplicated to canonical SRC-174. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1029/C-1029: page-level audit of LJMU doctoral thesis

The 401-page LJMU repository PDF of Arday’s 2015 PhD thesis was audited at its abstract, methods, sample-recruitment, epistemology, findings, conclusion, and limitations pages. The thesis reports a four-phase qualitative case study of four intervention participants, drawn from 46 invited final-year PE students and 24 returned questionnaires, with twelve workshops and several qualitative instruments. It explicitly acknowledges the lack of comparison between the 24 questionnaire respondents and four intervention participants and says the design cannot establish causal impact. The raw recordings, questionnaires, coding, and ethics file are not exposed. This is a primary scholarly artifact and a methodology record, not an independent verification of every procedure or a finding about later publications. Google Drive remains the active publication target.

## 2026-08-09 — SRC-1027/C-1027: Research Cast UK audio audit and timestamp correction

The canonical 44:47.54 Research Cast UK MP3 was re-audited with `mlx-community/whisper-small.en-mlx` using streamed windows with explicit offsets. The pass sharpens the educator-values passage at 05:30–07:10, the NHS-family/mental-health-nurse passage at 26:50–27:45, and the sport/community/belonging passage at 27:48–29:50. These remain first-person audio evidence and do not add independent records.

Method note: an earlier file-path clipping attempt could double-count window starts in displayed timestamps. The corrected audit uses absolute file times and records the issue so future derivatives do not inherit it. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1026/C-1026: Student Sessions audio audit

The preserved 42:04.46 *Student Sessions* MP3 was sampled with `mlx-community/whisper-small.en-mlx`. Targeted windows recovered Arday’s account of Sandro Sandri’s repeated phonics and literacy support, his statement that at 21 his reading age was 11, and a remembered Sandri framing of a PhD within 12 years of learning to read and write.

Decision: add timecoded first-person testimony to the existing SRC-156 interview without creating a new media node. The ASR’s 01:34 rendering appears to say he learned to “read” at 11, conflicting with the surrounding speech-at-11 source family; preserve the ambiguity and require human listening before quotation. No reading-age assessment, tutoring record, or qualification chronology was upgraded. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1025/C-1025: How Do You Cope? audio audit

The locally preserved 26 May 2025 *How Do You Cope?* MP3 was sampled with `mlx-community/whisper-small.en-mlx`. Targeted windows recovered Arday’s first-person discussion of his mother not explicitly naming his autism diagnosis to him until less than five years earlier, his extensive speech-therapy and educational-psychology support, learning through non-verbal communication, and his statement that he would have been a professional snooker player.

Decision: preserve these as timecoded first-person audio testimony and keep the episode deduplicated to SRC-129. The host introduction is not promoted as new corroboration; the snooker passage overlaps existing sports claims and does not establish professional status. The full transcript remains inaccessible, and ASR remains a navigation aid pending human listening. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1024/C-1024: New Humanist audio audit

The preserved 2,316.54-second *With Reason* MP3 was audited with `mlx-community/whisper-small.en-mlx` in targeted windows covering the childhood, music, protest, and police-stop passages. The audio broadly matches the host transcript: Clapham and council-estate upbringing; delayed speech/literacy; music, guitar, and movement out of signing; childhood picket lines; and the adolescent police-stop account.

The audit resolves one important ambiguity. The host transcript renders Arday’s statement as “sometimes it can be 345 times a year”; the audible passage at approximately 14:36–14:40 is “three, four, five times in a year.” This is a wording correction, not verification of the underlying police-stop frequency. Decision: preserve the audio as first-person evidence and keep the source deduplicated to SRC-223. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1023/C-1023: anonymous Roehampton teaching-reception lead

Discovery: browser rendering exposed an anonymous `r/UniUK` account alleging an Autumn 2018 student experience on a Roehampton module taught by Arday, including punctuality, preparation, teaching method, feedback, and a complaint to a course leader.

Decision: retain as low-provenance, unverified first-person reception testimony. Direct `www.reddit.com` and `old.reddit.com` shell/JSON requests returned HTTP 403, and no identity, enrollment, module, complaint, marking, recording, or institutional response was recovered. Do not repeat the thread as fact; reopen only for independently checkable records or a named first-hand account. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — C-1022: Cambridge indexed qualification snippet versus recovered records

The Cambridge Faculty profile remained HTTP 404, but search indexing exposed a later qualification snippet listing an LJMU MA Education Studies alongside the St Mary’s MA, Surrey BA, and LJMU PhD. This differs from the January 2020 CV’s MEd/PGCertLTHE formulation and the 2022 Cambridge Reporter’s credential wording.

Decision: preserve as an indexed/live source-version discrepancy under SRC-208/C-1022. Do not promote the snippet to an additional degree, and do not infer fabrication or clerical error. Reopen only for a restored profile, registrar record, certificate, or direct institutional clarification. Google Drive not updated; GitHub active.

## 2026-08-09 — qualification-source audit: LJMU thesis canonical, earlier awards unresolved

Exact-name searches across LJMU, Surrey, St Mary’s, and repository routes recovered no new qualification artifact. The existing LJMU 401-page thesis PDF is primary evidence for a July 2015 PhD submission, institution, and title; the current LJMU repository page is a distinct metadata manifestation already catalogued as SRC-569 and deduplicated to SRC-087. The 2008 BA, 2011 MA/PGCE, and 2013 MEd/PGCertLTHE remain supported by the dated CV and later institutional biographies, not award certificates or registrar records.

Decision: strengthen the ontology’s evidence distinction without creating a duplicate source. Reopen only for an awarding-body certificate, registrar/alumni record, or materially changed repository artifact. Google Drive not updated; GitHub active.

## 2026-08-09 — SRC-255/C-229: Academic Libraries North biography route recheck

The older indexed `/sites/default/files/` route for the already-canonical June 2019 Academic Libraries North biography was rechecked and returned HTTP 404 after redirect. The separately recovered `/wp-content/uploads/2025/04/` mirror remains the canonical artifact under SRC-255; no duplicate source or claim was created.

Decision: retain the route/version boundary under SRC-255 and C-229. No biography claim was upgraded. Google Drive not updated; GitHub active.

## 2026-08-09 — SRC-1020/C-1020: Talking Matters snooker audio audit

The canonical local MP3 was re-transcribed for 00:20:00–00:21:40 using `mlx-whisper` small.en after the earlier Whisper-small navigation pass. The larger model recovers closer-to-professional snooker, age 11–19 / roughly seven hours daily, Pro-Am, Pontins in Prestatyn, a 50–60 versus 87 break comparison, and 12–13 years of non-league football.

Decision: retain as machine-assisted primary-audio navigation/wording evidence, not a human-verified verbatim transcript or independent sports record. Google Drive not updated; GitHub active.

## 2026-08-09 — SRC-1019/C-1019: Crystal Palace sports-search boundary

Discovery: exact-name searches targeted Crystal Palace’s official domain for Arday, academy, youth, graduate, football, and contract combinations. The club’s current Academy Graduates roster was captured and contains no `Arday` occurrence; the only Jason entry is a different player, Jason Lokilo.

Decision: record this as a bounded negative-space result in the football evidence map. It narrows the named-club hypothesis but cannot disprove an historical or unindexed youth association, identify the club intended by the first-person account, or establish professional status. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1018/C-1018: Springfields Academy naming record

Discovery: the current Springfields Academy site lists an “Arday Class” among its Explorer classes and links a dedicated class page. The page names Jason Arday, describes him as a sociologist, writer, and fundraiser, and states that he has an autism diagnosis.

Decision: classify this as a first-party specialist-school reception/naming record. It adds a concrete public legacy association but no independent evidence about diagnosis, childhood, schooling, qualifications, or career. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1017/C-1017: QUB blind-copy version boundary

Discovery: QUB’s direct `pureadmin` route exposes a PDF whose filename identifies a blind-copy submission. The 22-page artifact labels itself “Peer reviewed version,” names *Educational Philosophy and Theory*, and preserves submission-style author/affiliation metadata.

Capture: the PDF and extracted text were downloaded and checksummed under `assets/captures/2026-08-09-qub-blind-copy/`. The route was compared with the 8 August QUB manifestation and the 18-page Kent repository PDF. The QUB copies differ only in generated download date; the Kent copy has materially different repository/journal front matter, pagination, typography, and citation punctuation, while the methodology body is materially the same.

Decision: register one new provenance/version record, not a second publication or independent corroborating witness. This sharpens the article-version map and preserves a primary artifact for audit; it does not resolve the QUB review, prove misconduct, or validate the study’s data. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-158/C-1014–C-1016: Ruling Passions transcript extraction

The already-canonical *Ruling Passions* web transcript was reread for subject-centred content beyond the existing childhood claims. Three bounded passages were promoted: motivation/self-training and tailoring (approximately 11:08–11:53), masking and exhaustion (14:03–15:33), and music as an autistic sense-making system plus a critique of rigid academic writing (46:58–50:14).

Decision: these are new claim-level extractions from an existing primary interview, not a new source node. They enrich the biography and public-output ontology while remaining first-person testimony and public intellectual position. No clinical inference or scholarship-quality conclusion was added. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1010–SRC-1012: library distribution and acquisition records

Discovery: a focused search for public-library manifestations of *Great and Unfortunate Things* surfaced Markham Public Library’s BiblioCommons result, Blackstone Library’s audiobook-distributor catalogue, and St. Catharines Public Library’s Spring–Summer 2026 adult nonfiction PDF.

Capture: the Markham HTML/headers, Blackstone HTML/headers, and SCPL PDF/text/headers were downloaded and checksummed under `assets/captures/2026-08-09-library-distribution/`.

Decision: these are new distribution/topology records about Arday’s memoir, not corroboration of its personal narrative. Markham is the strongest answer to whether a library had ordered the book: its catalogue explicitly says “On order.” Blackstone documents a library audiobook format and Arday’s narration; SCPL documents a library-facing selection list. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — C-1010/SRC-596: LJMU bicentenary profile remains a live/indexed mismatch

The exact LJMU bicentenary profile URL returned HTTP 404 again. Its 197,298-byte body is byte-distinct from the 8 August 404 capture and contains no Arday profile text, while public search indexing still exposes the older substantive profile. The new body is preserved locally; response headers remain local-only because they contain transient session cookies. This updates the existing route record rather than creating a duplicate biography source.

## 2026-08-09 — subject-output recheck: Newcastle lecture route remains an unchanged listing

The current Newcastle University archive route for Jason Arday’s 14 October 2025 “Sign o’ the times” lecture returned HTTP 200. The 51,815-byte HTML is byte-identical to the existing capture under `SRC-296`; no recording, transcript, captions, slides, or media endpoint was exposed. The route is closed for this checkpoint and remains a single event record.

## 2026-08-09 — SRC-1009/C-1009: CGHE “transcript” recovered and classified

Discovery: CGHE Webinar 164’s archived event page exposes a “View the transcript” link. The linked PDF was recovered as a two-page document titled with the 3 November 2020 event.

Decision: classify the artifact as a Zoom chat-log transcript, not a speaker transcript. The extracted text contains audience questions and closing messages but no occurrence of “Arday” and no spoken contribution attributed to him. Register it as `SRC-1009`, a distinct primary event/provenance artifact and negative-space boundary related to the event page. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1008/C-1008: Cumberland Lodge retrospective adds attributed remarks

Discovery: the Cumberland Lodge page “Tokenism: a barrier to inclusive diversity,” published 5 January 2022, was identified as a distinct host-written retrospective of the already-canonical 3 November 2021 webinar. Unlike the event listing, it attributes specific remarks to Arday and summarizes his positions on diversity, tolerance, tokenism, meritocracy, positive action, and inclusion.

Decision: create `SRC-1008` as a distinct first-party retrospective related to `SRC-618`, not as a second webinar or transcript. Add one bounded public-position claim; do not promote the article’s summary into verbatim speech or independent policy evidence. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1007/C-1007: STCG Merton profile changed-state recheck

Discovery: a targeted South Thames Colleges Group search for `site:stcg.ac.uk "Jason Arday"` returned only the canonical former-Merton-student profile. A direct recheck of its URL returned HTTP 200, but the body was an anti-bot/cookie challenge rather than the substantive profile captured on 6 August.

Decision: register `SRC-1007` as a changed access-state manifestation deduplicated to `SRC-159`. No new education, qualification, enrolment, or childhood claim was added. The challenge body remains local; transient response cookies are excluded from public publication.

## 2026-08-09 — SRC-1006/C-1006: ARU citation changed-page recheck

Discovery: the current Anglia Ruskin University honorary-degree citation returned HTTP 200. The raw HTML was byte-distinct from the 6 August capture, but normalized visible text was identical at 10,001 characters; no substantive wording, correction, award detail, or new evidence appeared.

Decision: register `SRC-1006` as a changed technical manifestation deduplicated to `SRC-089`. Keep the existing institutional-retelling boundary for its childhood, education, sports, endurance, fundraising, and career language. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — identity-control check: United Response homonym

An exact-name media search surfaced United Response’s “Jason’s life story interview,” dated September 2025. The page identifies a different Devon-based Jason: born in Penzance, raised in St John’s/Newland, associated with Mencap in Penzance, and describing a miner father and different sibling/age history. It was rejected as a homonym and not added to Arday’s ontology. Autism School International’s apparently new result was also reconciled to existing canonical `SRC-330` because the page and portrait were byte-identical to the already-preserved files.


## 2026-08-09 — sports-record boundary extension (no new source node)

Discovery: exact-name searches for `"Jason Arday" footballer`, `"Jason Arday" "Battersea Park Rangers"`, `"Jason Arday" "Southern Sunday Football League"`, and `"Jason Arday" snooker -Wikipedia` returned only the existing propagation family, the canonical Battersea Park Rangers lead, and public discussion of the already-corrected Bath wording.

Decision: extend the canonical sports search boundary (`SRC-151` and linked records) without creating a duplicate source or claim. No named club, academy, contract, senior appearance, ranking, tournament result, or governing-body record was recovered. The unresolved sports claims remain self-reported/source-versioned.

## 2026-08-09 — SRC-938/C-1004: NetGalley catalog recheck

Discovery: direct HTTP-200 rechecks of NetGalley’s US (`783642`) and UK/Australia (`860927`) memoir catalog pages recovered current edition/access metadata. The US page reports an average rating from 98 members; the UK/Australia page reports one member. Both retain the sign-in requirement for request/access and expose no review-copy file.

Decision: register `SRC-938` as a changed source-version of `SRC-337`, preserving the catalog rating state and edition topology without creating a new edition or review node. Cookie values in the response headers were redacted before publication. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-937/C-1003: second StoryGraph access recheck

Discovery: a second direct request to the canonical StoryGraph review route returned HTTP 403 with a Cloudflare challenge at 03:19:54 UTC. The challenge is byte-distinct from `SRC-918`; public indexing continued to report 12 reviews and snippets, but no review body, image, audio, or book file was recovered.

Decision: register `SRC-937` as a changed source-version/access boundary deduplicated to the StoryGraph reception record. Do not count the indexed review count or snippets as independent corroboration. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-936/C-1002: *The Week* controversy roundup

Discovery: *The Week UK* published a public article dated 7 August 2026 summarizing the Arday/Cambridge controversy. Its text explicitly attributes material to Gordon Rayner (*Daily Telegraph*), Jennifer Schuessler and Alexandra Alter (*New York Times*), Guy Adams (*Daily Mail*), Daniella Maison (*Independent*), and Lanre Bakare (*Guardian*). The article and its credited lead image were locally preserved.

Decision: register the item as a secondary source-propagation and reception witness, not a new independent finding. Its summaries of thesis overlap, defence, fundraising, and prior-clearance claims remain linked to the named publications and existing primary records. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — deduplication check: apparent remaining `plag1` row

The extracted `More Z-M - summaries(1).docx` table was checked for the row spanning Arday pp. 352–353 and Zwozdiak-Myers pp. 272–273. It is the same page-bounded comparison already recorded as `SRC-487`, not a distinct later row. The stale “remains open” wording in nearby checkpoint prose was corrected; no new source or claim was created. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-935/C-1001: Goodreads author-page reception snapshot

Discovery: the current Goodreads author route returned HTTP 200 and exposed an author-level catalogue/reception state: 124 ratings, 89 reviews, six distinct works, and a 4.51/82-rating, seven-edition listing for *Great and Unfortunate Things*. The same page listed *We See Things They’ll Never See* at 3.80 from 20 ratings across six editions.

Decision: register the author page as a distinct manifestation from the earlier individual memoir-book record (`SRC-294`). Preserve the counts as volatile reader-platform metadata only; they are not evidence for the accuracy of memoir claims, scholarly quality, or research-integrity allegations. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-933/C-1000 and SRC-934/C-999: current Cambridge institutional records

Discovery: a current search of Cambridge’s official domains surfaced two distinct records not represented by the prior profile/statement captures. The Black Advisory Hub’s 14 April 2026 symposium page names Professor Jason Arday as a practitioner-workshop leader. The Cambridge University Reporter’s 2025–26 college-fellows roster, dated 19 January 2026, lists “Arday Jason phd frsa” among Jesus College’s 2023 fellows.

Decision: register both as first-party institutional witnesses, keeping the event listing separate from the governance roster. They support dated public association with Cambridge professional and college activity, but do not establish event delivery, fellowship terms, current employment, or an investigation outcome. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-932/C-998: Norli memoir-edition access boundary

Discovery: search indexing surfaced a Norli bookseller listing for *Great and Unfortunate Things* under ISBN 9781398542747, matching the distinct 336-page UK edition captured as `SRC-930`. The indexed result exposes catalog-level title, author, format/date, and synopsis snippets.

Capture: the canonical Norli product URL returned HTTP 403 with a 118-byte body. No product HTML, image, price, stock status, or excerpt was recovered.

Decision: register the result as a low-provenance retailer manifestation deduplicated to `SRC-930`, preserving the direct access boundary rather than treating the indexed synopsis as independent corroboration. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-931/C-997: additional 30 in 35 Wayback pages recovered

Discovery: the bounded CDX enumeration associated with `SRC-377` listed successful captures for campaign pages 2, 3, 5, 6, 7, and 8. Direct Wayback replay using the archived original host/port recovered all six pages as HTTP-200 HTML. Plain-text extraction shows marathon reports covering numbers 3–30, many stated completion times, an interim £4,520 total, a “Fundraising target smashed!” post, final-run instructions for 22 August, and a campaign-side Facebook feed statement that marathon 30 took 5 hours 57 minutes and was an “amazing end.”

Decision: register `SRC-931` as an extension of the contemporaneous campaign source rather than create six duplicate event nodes or a separate Facebook source. The pages strengthen the proposition that the campaign represented the challenge as completed, but they do not independently verify route distances, race timing, every start/finish, or final accounting. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-930/C-996: distinct Google Books UK memoir record

Discovery: the indexed Google Books lead resolved to an HTTP-200 edition page for volume `HWfF0QEACAAJ`, ISBN 9781398542747 / ISBN-10 1398542741. The page lists Simon & Schuster Limited, 27 August 2026, and 336 pages, exposes a cover, and repeats the memoir synopsis. Its embedded state says “No eBook available,” `has_flowing_text:false`, `has_scanned_text:false`, and `is_browsable:false`. The Google Books API returned HTTP 429 for this ID and the previously captured 368-page UK ID.

Decision: register a distinct edition-level source linked to the memoir family rather than merge it into `SRC-145`. Preserve the synopsis as publisher/catalog copy and the page’s family-count wording as another witness, without upgrading it to independent corroboration. The record expands edition topology but yields no readable memoir text. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-922/C-988: football-academy lead remains inaccessible

Discovery: current search indexing surfaced a June 2026 Reddit discussion explicitly asking which academy or professional club was meant by the original Bath wording. A direct request returned Reddit’s anti-bot challenge, with no thread body or comments available.

Decision: register SRC-922 as a low-provenance lead and access boundary linked to the existing Bath correction and sports-record search. It adds no club, contract, roster, match, or correction evidence. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-923/C-989: QUB article-page metric recheck

Discovery: QUB’s Research Portal page for *Attempting to break the chain* was byte-distinct from the prior 8 August capture and displayed 1,734 downloads rather than 1,555. DOI, authors, pagination, repository file, and version labels remained unchanged.

Decision: register SRC-923 as a volatile metadata/source-version record deduplicated to SRC-894. The changed counter does not bear on QUB’s reported investigation, article validity, or research integrity. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-924/C-990: PubPeer link-provenance audit

Discovery: the eight PubPeer identifiers linked from 21percent’s Arday commentary resolved to unrelated publications on migration, passports, immigration, and humanities history. None was an Arday publication.

Decision: register SRC-924 as a source-resolution correction. Preserve the HTML and headers as platform records, but do not import their comments into the Arday integrity dossier. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-921/C-987: Lives Retold PDF recovered from Wayback

Discovery: Wayback CDX exposed a 28 June 2023 HTTP-200 capture of the previously unavailable Lives Retold/BBC Lent Talk PDF. The 11-page binary was downloaded, hashed, and text-extracted locally.

Decision: register SRC-921 as a recovered manifestation deduplicated to SRC-036. Preserve its page-level autobiographical wording, including the age-11 speech, age-18 literacy, sports, endurance, and April 2019 interview passages, without upgrading any of those claims to independent fact. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-913/C-978: Foyles memoir-reviews access recheck

Discovery: the direct Foyles reader-reviews route returned HTTP 403 with a 215,038-byte Cloudflare challenge, byte-distinct from the prior 8 August challenge. Indexed review text was not newly recovered and no book/audio file was exposed.

Decision: register SRC-913 as a changed access-state manifestation deduplicated to SRC-437. Preserve the reviews as reception topology only; no autobiographical claim is upgraded. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-276/C-977: RSC caption-route recheck

Discovery: direct public timed-text requests for the RSC Inclusion and Diversity Forum 2025 YouTube recording (`JbyQlddjUJ8`) returned zero-byte responses for `en` and `en-GB`, matching the previously preserved empty-caption response.

Decision: extend the existing RSC media boundary rather than create a duplicate recording or transcript node. The locally preserved 13:24 MP4 remains available for manual listening/timecoding; no spoken-content claim is upgraded. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-895/C-976: adjacent Cambridge and regulator endpoint sweep

Discovery: exact-name searches across Cambridge appointment/tenure and Jesus College routes, plus Charity Commission results, returned existing canonical process, profile, annual-report, and governance records. The direct Cambridge Faculty “Our People” page-1 body was byte-identical to the 8 August SRC-459 capture and still lacked `Jason Arday` and `jaa80`; only cache headers changed.

Decision: extend SRC-895 rather than create duplicate source nodes. Generic statutes, search snippets, and existing regulator reports add no new Arday-specific process or role-status evidence. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-912/C-975: Cambridge investigation statement availability recheck

Discovery: the University of Cambridge’s canonical statement URL returned HTTP 200 on 9 August after the latest preserved fetch had returned a generic 404 page. The page carried a 7 August last-updated timestamp and the same visible investigation/process wording as the earlier live manifestation.

Decision: register SRC-912 as a changed access-state source-version deduplicated to SRC-093. No institutional finding, exoneration, correction, or new process detail was added. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-895/C-974: OpenAlex and public-media sweep extension

Discovery: the current OpenAlex author identifier `A5048886069` returned 56 works when queried with a 100-result page sorted by publication date; the newest DOI-bearing entries were the already-preserved OSF preprint versions. Exact title/DOI comparison and concurrent searches for publications, 2026 DOI output, YouTube/video, and podcasts returned existing records such as the Oxford EDB lecture and *How Do You Cope?* episode, plus homonyms.

Decision: extend SRC-895 with the query and result boundary rather than create duplicate publication or media nodes. No new DOI, full text, recording, transcript, or distinct event artifact was recovered. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-895/C-973: current event and institutional sweep extension

Discovery: a focused sweep of current event-recording, university-event-report, interview/podcast/video, advisory-page, BSA, Cambridge, and scholarly correction searches returned only existing canonical records, byte-identical Cambridge appointment material, the already-preserved Taylor & Francis 403 state, and unrelated homonyms.

Decision: extend the existing SRC-895 bounded-search record rather than create duplicate source nodes. No new recording, transcript, post-event report, DOI, filing, institutional outcome, or distinct biography artifact was recovered. Reopen only with a changed endpoint or concrete new identifier. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-911/C-972: Taylor & Francis correction access recheck

Discovery: the publisher PDF route for the already-canonical correction to *Attempting to break the chain* appeared in a scholarly search result with indexed correction text, but a fresh direct request returned HTTP 403 Cloudflare challenge HTML rather than a PDF. The 5,542-byte body and headers are preserved.

Decision: register SRC-911 as a changed access-state manifestation deduplicated to SRC-297. The body is byte-distinct from the 8 August challenge, so the retrieval history is retained; no new correction text, retraction, or integrity finding is claimed. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-910/C-971: Sanger Excellence Fellowship Advisory Group

Discovery: a current Wellcome Sanger Institute programme page identifies Jason Arday in the Advisory Group for the Sanger Excellence Fellowship and labels him “Professor of Sociology, University of Glasgow.” The direct page returned HTTP 200 and its HTML/headers were preserved.

Decision: register the page as SRC-910. It is a first-party programme relationship and a dated host biography/version witness, not proof of advisory appointment terms, participation, or current Glasgow employment. The title wording is kept separate from direct Glasgow records and from Cambridge current-status evidence. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-909/C-970: Cambridge Faculty staff-contact route boundary

Discovery: search indexing surfaced the University of Cambridge Faculty of Education’s “Faculty Staff Contact List” as an Arday-associated route. The direct URL returned HTTP 404 on 9 August 2026; the generic page-not-found HTML and response headers are locally preserved.

Decision: register SRC-909 as a distinct first-party endpoint/access-boundary record. No live staff entry, role, or contact details were recovered, and no employment or resignation inference is made. This state is kept separate from the “Our People” pagination sweep and the indexed/live directory mismatch records. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-908/C-969: BSA *Network* governance roster

Discovery: a BSA governance/source-version search located the British Sociological Association’s Spring 2025 *Network* issue as a public 78-page PDF. Its masthead (printed p. 4 / PDF p. 4) lists “Dr Jason Arday” among the Board of Trustees.

Decision: register the issue as SRC-908 and preserve the PDF, extracted text, and response headers. This is a dated first-party association roster and establishes what BSA published in that issue; it does not establish appointment terms, attendance, or continuing status after Spring 2025. It is separate from the BSA annual-report and directory records. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-906/C-967 and SRC-907/C-968: The Sociological Review author and book-review records

Discovery: a learned-society search surfaced The Sociological Review’s author profile for Jason Arday and its linked full review of *We See Things They’ll Never See*. Both direct routes returned HTTP 200. The author page contains dated biography/role copy and a 155×240 book image; the review page is a 39,885-byte full HTML article by Alexa MacDermot, dated 9 September 2025, with book and review DOI metadata and a 240×370 cover.

Decision: register the author page as SRC-906 and the review as SRC-907. The profile is a source-version witness for circulated professional roles; the review is a reception and bibliographic record that discusses the book’s autoethnographic, musical, Black-feminist, decolonial, and neurodiversity framing. Neither source independently verifies the memoir/book’s autobiographical claims. The review’s stated Free Access Licence and permission condition are preserved; its full text is not reproduced in Markdown. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-905/C-966: Simon & Schuster `.net` memoir manifestation

Discovery: a fresh publisher-locale search surfaced `simonandschuster.net/books/Great-and-Unfortunate-Things/Jason-Arday/9781668085578`. The direct request returned HTTP 200 and a 122,009-byte HTML page with JSON-LD edition metadata, publisher synopsis, author/contributor links, and CloudFront cover URLs.

Decision: register the page as a first-party locale/source-version deduplicated to SRC-091. It confirms the US hardcover metadata (ISBN `9781668085578`, 37 Ink, 288 pages, 11 August 2026) and preserves a separately downloaded 593×900 cover, but the page’s childhood and career narrative is publisher/memoir marketing copy rather than independent corroboration. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-904/C-965: Amazon Music *A Good Read* manifestation

Discovery: a podcast-platform search surfaced Amazon Music’s dedicated route for the 21 November 2023 BBC *A Good Read* episode featuring Janet Ellis and Jason Arday. The direct capture exposed show UUID `391a33d1-48ae-4a23-b4a5-28fe1337f3cd` and episode UUID `56c9195a-9289-49c5-b418-44c95058f143` in its deep-link metadata.

Decision: register the route as a platform manifestation and access-boundary record deduplicated to SRC-061. The 11,446-byte response is a JavaScript shell with no rendered episode content, transcript, captions, artwork, or audio URL. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-903/C-964: African Allied Health speakers-page recovery

Discovery: the African Allied Health Network’s `/speakers/` route returned HTTP 200 on a fresh direct request after the earlier 403/browser-verification state. It again listed Professor Jason Arday as a keynote speaker and exposed a current organizer biography and portrait.

Decision: register the response as a changed first-party page/source-version linked to SRC-306. The portrait is byte-identical to the earlier SRC-306 image and is not a new media object. The recovered page does not establish delivery of the 23–24 July summit or Arday’s keynote. Reopen only for a post-event report, final programme, recording, transcript, attendance artifact, or another changed organizer state. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-902/C-963: Holding the Space LinkedIn announcement

Discovery: a targeted event search surfaced Dr Yaz Iyabo Osho’s public LinkedIn announcement naming Jason Arday as a keynote for *Holding the Space 2026* at the University of Westminster on 16 April 2026, 09:30–16:30, at Regent Street Campus.

Decision: register the post as a distinct pre-event announcement/source-version deduplicated to the canonical Westminster post-event report `SRC-317`. Preserve the organizer-side role list as promotional copy only. The displayed portrait is Osho’s, not Arday’s; no recording, transcript, or slides were recovered. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-901/C-962: Google Play Books memoir storefront

Discovery: a direct Google Play Books page for *Great and Unfortunate Things* exposed volume `84edEQAAQBAJ`, identifying an August 2026 Simon and Schuster ebook at 368 pages. The visible page included publisher-facing catalogue copy, a short opening excerpt, a 585×900 cover, and the warning “This item isn't available in your country.”

Decision: register the page as a distinct storefront/access manifestation deduplicated to SRC-145, not as a new edition or independent biography witness. No ebook file, page image, or downloadable full-text preview was exposed. Reopen only after a changed availability state, lawful preview/file, or distinct volume identifier appears. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-900/C-961: Topping & Company memoir-event lead

Discovery: a targeted memoir/publication-event search found search-index text for Topping & Company’s Edinburgh listing “Jason Arday for Great and Unfortunate Things,” dated 18 September 2026 at 7 p.m.

Boundary: the direct `https://www.toppingbooks.co.uk/events/edinburgh/` page was captured on 8 August, but its current HTML contained no Arday occurrence, memoir title, or matching detail route. No direct ticket page, event image, recording, cancellation, or attendance evidence was recovered.

Decision: register SRC-900 as an indexed event lead plus current-page negative-space observation. The event is not treated as verified or delivered. Reopen only after a direct route, changed listing, ticket/venue record, cancellation/update, recording, or post-event report appears. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-899/C-960: SRA first-party LinkedIn conference announcement

Discovery: a targeted search for the unresolved 2026 SRA conference media/output lead found the Social Research Association’s own LinkedIn announcement, distinct from the already-catalogued Tina Haux repost and the SRA event/programme/report pages under SRC-188.

Capture: the 5 June 2026 post names Arday’s 8 July session, “Message in a Bottle: Creating safer spaces for marginalised voices in research and policy-making,” and exposes four programme graphics. HTML, headers, and images are preserved under `assets/captures/2026-08-08-sra-conference-2026/`.

Decision: register SRC-899 as a first-party social-media source-version deduplicated to SRC-188. It strengthens announcement provenance and visual programme evidence but does not establish attendance, delivery, a recording, transcript, or substantive remarks. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — recent-source sweep: no new canonical record

Exact-name searches for August 2026 news, memoir reviews, Cambridge process updates, and new interviews returned AP, *The Atlantic*, *The Week*, *Publishers Weekly*, StoryGraph, Retraction Watch, Good Law Project, Guardian, and already-catalogued publisher records. No new formal outcome, primary institutional document, distinct interview, or uncatalogued memoir manifestation was recovered in this pass; Amazon Music’s Talking Matters route is the only new source-version promoted as SRC-897.

## 2026-08-09 — SRC-897/C-913: Amazon Music Talking Matters manifestation

Discovery: an exact-name podcast search surfaced Amazon Music’s catalogue route for the already-canonical *Talking Matters with Nick Halkes* episode. Browser/indexed metadata identifies the 2 August 2024 catalogue date, approximately 1 hour 18 minute duration, episode and show IDs, and the statement that the conversation was recorded in 2021 while Arday was an associate professor at Durham.

Capture: the direct request returned an 8,504-byte JavaScript application shell containing the deep-link path but no rendered episode text, audio URL, transcript, or captions. The HTML and response headers are preserved under `assets/captures/2026-08-09-talking-matters-amazon-music/`.

Decision: register SRC-897 as a platform source-version deduplicated to SRC-184. It adds catalogue topology and a durable platform ID, not a second interview or independent corroboration. Reopen only for a changed rendered page, public transcript/captions, or a distinct audio endpoint.

## 2026-08-09 — archive consistency audit

Read-only audit of the current worktree found 614 source Markdown files with front-matter IDs, no duplicate IDs, 629 unique source paths referenced by the registry, and no registry-referenced source file missing from disk. This validates the canonical-file layer after the Research Cast UK deduplication correction; it does not certify that every local media capture is already published to GitHub.

## 2026-08-09 — SRC-198/C-912: Research Cast UK canonical-source correction

Audit: the fresh Lincoln Bishop page, direct MP3, and episode portrait were initially mistaken for an uncatalogued podcast. The worktree already contained SRC-198, the canonical Research Cast UK record, the same 107,519,809-byte MP3, derivative Whisper JSON, and three timestamp-focused listening clips.

Correction: deleted the duplicate source node and folded the new page/headers/portrait capture into SRC-198. Hash comparison confirms that the fresh MP3 and portrait are byte-identical to the existing canonical local objects. Exact-title, host/guest, filename, and institutional-domain searches found no public transcript or captions; the local ASR remains derivative and unverified.

Decision: retain C-912 as a bounded public-text search result and preserve the episode as SRC-198 only. This is a deduplication correction, not a new interview or new biography evidence.

## 2026-08-09 — SRC-481/C-909: Tapesearch transcript access recheck

Discovery: the unresolved media queue returned to the Tapesearch manifestation for the already-captured 26 May 2025 *How Do You Cope?* episode. The browser/indexed page still supplies the previously logged opening transcript, but no new public transcript route or distinct recording surfaced.

Capture: a fresh direct request returned a Cloudflare managed-challenge page. The HTML and response headers are preserved under `assets/captures/2026-08-09-tapesearch-how-do-you-cope/`; the page contains no episode text beyond the challenge. The login-gated remainder was not accessed or bypassed.

Decision: update SRC-481/C-909 as a current access-boundary recheck and keep the episode deduplicated to SRC-129. No new transcript, audio, video, or independent biographical evidence was recovered. Reopen only for a changed public transcript state, an official caption/transcript endpoint, or a distinct recording.

## 2026-08-08 — SRC-890/C-897–C-898: memoir proposal version lead

Discovery: a current Reddit post surfaced a *Daily Mail* report titled “Jason Arday claimed he survived ‘unrecoverable’ car accident, locked-in syndrome and testicular cancer in newly surfaced book proposal.” The Daily Mail page was directly retrievable and its article body reports alleged differences between a 2024 proposal and the final memoir. The proposal itself was not recovered.

Capture: preserved the Daily Mail HTML and headers, 1200×675 lead image, and embedded 39-second commentary MP4. Reddit was browser-readable through the web research surface but returned HTTP 403 to direct shell/API retrieval; the blocked responses are preserved. The Daily Mail’s Atlantic reference was reconciled to canonical SRC-335.

Classification: secondary source-version reporting and publisher commentary, not medical or autobiographical verification. Reopen only for the proposal/manuscript, a changed SRC-335 version, a correction, or direct author/publisher response. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-891/C-899–C-900: Boris Johnson commentary

Discovery: the Daily Mail article page for the memoir-proposal report linked to Boris Johnson’s separate 7 August 2026 opinion column about the Arday appointment and Cambridge’s institutional incentives.

Capture: preserved the full column HTML and headers, its 1200×675 lead image, and its embedded 32-second video. The item is catalogued as a named political opinion/source-propagation record, distinct from SRC-890’s news report but not independent corroboration.

Classification: the column’s judgments about merit, biography, racism, and institutional responsibility remain attributed to Johnson. Its call for an independent inquiry is a public argument, not evidence that such an inquiry has occurred. Reopen only for a correction, response, changed page, or direct institutional record.

## 2026-08-08 — SRC-889/C-896: Companies House AP01 appointment filing

Discovery: the Companies House filing-history search for Autism Centre of Excellence (company 12435820) exposed a distinct AP01 filing that was not represented by the annual-report or Charity Commission records.

Capture: the filing-history HTML and headers, the two-page AP01 PDF and headers, extracted text, and a rendered first page are locally preserved. The history records receipt on 12 April 2024; the AP01 records appointment on 30 March 2024, names Prof Jason Atta Kwei Arday, states that he consented to act, and gives occupation “ACADEMIC.”

Classification: this is the strongest legal-register artifact in the current Autism Centre appointment chain and independently pins the filed director date to 30 March 2024. It remains a governance record only; no operational activity, remuneration, or end date is inferred. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-888/C-895: Autism Centre of Excellence annual report and trustee appointment

Discovery: a Charity Commission search for public filings surfaced the Autism Centre of Excellence report for the year ended 30 June 2023, a distinct governance artifact not previously represented in the registry.

Capture: the regulator endpoint returned a 28-page PDF on 8 August 2026. The PDF, extracted text, response headers, and a 150-dpi render of printed page 3/PDF page 5 are preserved. The chairman’s report says the board unanimously agreed at its 26 March 2024 meeting to appoint Jason Arday as a trustee, with duties to start after paperwork was finalised during March 2024.

Classification: this strengthens the appointment-decision trail behind the later Charity Commission and Companies House records, while keeping the report’s childhood and Cambridge descriptions in the promotional-biography lane. It does not establish a precise legal effective date, continued service after the 2026 Cambridge resignation, operational work, remuneration, or personal fundraising. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-887/C-894: Jesus College Annual Report and Accounts 2024

Discovery: an exact-name search restricted to the Jesus College domain surfaced the college’s 47-page *Annual Report and Accounts 2024*, a distinct first-party governance/accounting publication not previously represented in the registry.

Capture: the PDF, response headers, extracted text, and a 150-dpi render of printed page 3 are locally preserved. The Fellows list on printed p. 3 includes “Professor J. Arday (from 1 October 2023).” PDF metadata gives a 28 October 2024 creation date and 22 November 2024 modification date.

Classification: this is stronger primary roster evidence than a host biography and is distinct from the *University Reporter* rosters. It establishes a dated fellowship-listing state only; it does not establish post-resignation status or provide any investigation document. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-886/C-892–C-893: *THE* resignation/investigation report

Discovery: the Metropolitan Police follow-up linked *THE*’s 5 August report “Jason Arday resigns after University of Cambridge opens investigation.” No matching source record existed in the registry.

Capture: the public HTML, response headers, and Getty Senate House image are preserved. The report gives a contemporaneous account of Arday’s immediate resignation and attributes Cambridge’s “new information,” academic-misconduct-policy, support, non-comment, and separate Jesus College process wording.

Decision: added `SRC-886/C-892–C-893` as a distinct news manifestation, while deduplicating the underlying Cambridge investigation statement and Good Law Project resignation letter. The report is not an adjudication. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-885/C-889–C-890: Metropolitan Police follow-up via *THE*

Discovery: the editor’s note and reporter account linked a 6 August *Times Higher Education* follow-up reporting the Metropolitan Police response to the Grove contact episode.

Capture: the public HTML, response headers, and Getty police-car image are locally preserved. The report says the Met inquiry lasted four months and was dropped in February 2026; it quotes a spokesperson saying no offence was found without interviewing Grove and that the no-contact instruction was not the right action because it could frustrate legitimate journalism.

Classification: this is a quoted institutional response mediated through *THE*, not a standalone police document. It materially strengthens the process record about the police handling while leaving the complaint file, legal classification, complainant identity, and full chronology unresolved. Google Drive was not updated; GitHub remains the active publication target.

Boundary check: an exact-name search restricted to the Metropolitan Police’s public domain returned no matching Arday/Grove statement or case record. Unrelated locality and generic misconduct results were excluded. The official-domain route is therefore logged as currently unresolved/inaccessible rather than interpreted as a substantive absence.

## 2026-08-08 — SRC-883/C-885–C-886 and SRC-884/C-887–C-888: *Times Higher Education* process artifacts

Discovery: direct retrieval of the two *Times Higher Education* opinion URLs linked from the public controversy discussion returned HTTP 200 pages that were not yet represented in the registry: editor Chris Havergal’s 3 August note and reporter Jack Grove’s 5 August first-person account.

Capture: both full HTML pages, response headers, and their lead images are preserved. The editor’s note was updated on 6 August to add the Metropolitan Police reference; the reporter’s account was likewise updated on 6 August. The pages expose the publication dates, bylines, body text, and image credits.

Classification: these are valuable first-party accounts of *THE*’s editorial and reporting process. The editor records the public-interest rationale for the unpublished inquiry and attributes LJMU/police process claims; Grove records his own contact chronology, stated 63-page report and 97-page submission, and three direct emails. Neither page supplies the underlying LJMU report, police record, unpublished dossier, or final institutional finding. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-882/C-884: Cofnas Substack changed-state recheck

Discovery: the academic-integrity search re-opened Nathan Cofnas’s public 21 July 2026 article, which is already canonically represented by `SRC-379` and the fuller `SRC-476` manifestation.

Capture: a fresh direct request returned byte-distinct HTML and headers. The visible article date and substantive text were unchanged in comparison, while engagement counters moved from the earlier capture’s 1,341 likes / 274 comments / 169 restacks to 1,404 likes / 286 comments / 169 restacks. The new HTML and headers are preserved under `assets/captures/2026-08-08-cofnas-substack-recheck/`.

Decision: added `SRC-882/C-884` as a changed source-version/reception node, not a duplicate article. The article’s allegations, political framing, and quoted correspondence remain attributed; the dynamic counters are reception metadata only. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — Memoir proposal/reception pass: public proposal PDFs reconciled

Discovery: a targeted search for a publicly available proposal for *Great and Unfortunate Things* surfaced the Simon & Schuster Spring 2025 and Spring 2026 rights-catalogue PDFs. Both proposal-level artifacts are already preserved as `SRC-504` and `SRC-321`, respectively; the search produced no new proposal file, manuscript, or review/interview artifact.

Reconciliation: the Spring 2025 catalogue entry is the earlier version labelled “May 2026 | DD,” with a projected 320 pages and “Proposal available”; the Spring 2026 catalogue gives an August 2026 publication month, 288 pages, and “Manuscript Available.” The differences are preserved as publishing-history/source-version metadata. Their childhood, literacy, diagnosis, Cambridge, and audience language remains publisher/trade copy, not independent corroboration.

Boundary: the public proposal trail is covered by the existing local PDF, extracted text, headers, and page render assets. The finished memoir, the 2024 proposal described by *The Atlantic*, and any underlying manuscript remain separate source targets. Reopen only for a new proposal version, lawful manuscript/preview text, or a distinct contemporaneous review/interview. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-881/C-883: SnapJournal low-provenance biography

Discovery: a current exact-name search surfaced SnapJournal’s 24 April 2026 “Career Milestones and Educational Impact 2025–2026” page.

Capture: the public HTML and response headers are preserved. The page has no named author, citations, interview attribution, or primary-document links. It repeats familiar childhood, Cambridge, project, fundraising, WaterAid, and affiliation language and adds generic future-facing claims.

Decision: added SRC-881/C-883 as a source-propagation/reliability node. Its prose and claims remain attributed to SnapJournal; stale or unsupported present-tense assertions are explicitly not promoted to facts. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-880/C-882: Target US memoir-edition manifestation

Discovery: an exact-title retailer sweep surfaced Target’s US product page for *Great and Unfortunate Things*, distinct from the Simon & Schuster publisher page and the Google Books catalogue records already in the archive.

Capture: Target’s public page identifies product ID `A-1007422036`/TCIN `1007422036`, an 11 August 2026 street date, and a 288-page hardcover. The page HTML, headers, and a 1200×1200 Target Scene7 cover image are locally preserved.

Decision: added SRC-880/C-882 as a retailer edition/source-version record and linked it to canonical SRC-091. The listing’s childhood and Cambridge language remains promotional copy; it is not independent corroboration. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — Scholarly/institutional-output sweep: no new node

Discovery: exact-name searches for `Jason Arday 2026 publication DOI`, `Jason Arday 2025 article DOI`, Cambridge 2026 pages, and current university-event/workshop material were cross-checked against the archive. The results surfaced the already-catalogued OpenAlex/Crossref records, the BSA Annual Conference 2026 plenary, Cambridge’s 14 April 2026 Anti-Racism Symposium, and the current Faculty of Education profile.

Reconciliation: the BSA abstract book and conference record are already represented by SRC-187, with delivery evidence under SRC-376; the symposium is SRC-193; and the Faculty profile/version states are already represented by the Cambridge profile records. No new DOI, full-text manifestation, recording, correction, appointment record, or post-event document was found in this pass. Search results for unrelated homonyms and non-Arday works were excluded.

Boundary: this closes the captured query family for the current state. Reopen only with a changed index result, a concrete title/DOI, a distinct institutional page, a recording/transcript, or a post-event artifact. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — C-881: Taylor & Francis correction PDF recheck

Discovery: the correction/retraction search lane reconfirmed the already-catalogued 2024 Taylor & Francis correction to *Attempting to break the chain*; no new correction or retraction record was found.

Capture: a fresh direct request for the publisher PDF returned a 5,563-byte Cloudflare challenge. The body and response headers are preserved under `assets/captures/2026-08-08-educational-philosophy-correction-recheck/`.

Decision: updated SRC-297 in place and added C-881 as a changed access-state observation. This does not create a duplicate correction source or upgrade any allegation. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-879/C-880: *Libero Quotidiano* international commentary

Discovery: a date-qualified search for new international-language Arday coverage surfaced Giovanni Longoni’s 29 July 2026 Italian commentary in *Libero Quotidiano*.

Capture: search indexing exposed the title, byline, date, and article text. The direct AMP route returned a 483-byte HTTP 403 permission response; its HTML and headers are preserved. No article image or full publisher body was recovered.

Decision: added SRC-879/C-880 as a distinct international propagation witness. The article’s rhetoric, numerical claims, and references to the thesis-overlap and biography controversy remain attributed and derivative; no allegation was upgraded to a finding. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-878/C-879: Ruling Passions migrated host and Amazon Music manifestation

Discovery: a fresh exact-title search surfaced the project’s migrated `ruling-passions.com` URL and an Amazon Music episode page for “Ruling Passions: 2. A discussion with Jason Arday.”

Capture: the migrated project page returned the Episode 2 transcript, existing Spotify embed, Padlet embed, and project description. Amazon Music returned an application shell, while indexed metadata supplied a separate episode identifier, 19 March 2022 date, and displayed 51-minute duration. No full audio or new transcript was recovered.

Decision: added SRC-878/C-879 as a source-version/platform-topology record linked to canonical SRC-158. The two manifestations do not create a second appearance or independently verify the interview’s autobiographical content. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-877/C-878: AGCAS UKCGE interview lead and PDF boundary

Discovery: independent podcast/index searching surfaced search-indexed text from AGCAS’s July 2021 *Researchers Matter* bulletin. Its resources section points to an interview with Jason Arday from UKCGE concerning the BME doctoral-student academic-career project.

Capture: the original AGCAS PDF URL returned a 301 to Graduate Futures, whose HTTP-200 response was an HTML fallback rather than a PDF. The redirect/fallback body and headers are preserved; no bulletin binary, interview page, recording, or transcript was recovered.

Decision: created a dated interview-lead/access-boundary record and kept it distinct from the 2017 doctoral-student report. Reopen only for a lawful archive/PDF replay, direct UKCGE interview page, transcript, or recording. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-876/C-877: Surviving Society profile inventory boundary

Discovery: following the Spotlight playlist links, the current Surviving Society SoundCloud profile and `/tracks` route were audited for any additional Arday-named output.

Capture: the public profile exposes ten visible tracks, including the canonical E188 Jason Arday/Chantelle Jessica Lewis episode. No other Arday-named title appears in the visible inventory; the page does not expose a complete historical export or usable pagination beyond the same visible list.

Decision: created a profile-boundary record and deduplicated E188 rather than creating a second episode. The result closes the current-profile route only; older, private, deleted, or playlist-only tracks remain future leads. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-875/C-876: Spotlight Series playlist topology audited

Audit: the compilation links three public SoundCloud playlists. Each current page exposes five titled tracks, for 15 tracks total. The titles identify other guests and topics but do not name Jason Arday.

Decision: preserved all six playlist HTML/header files and added a negative-space claim. The playlist structure does not identify a standalone Arday episode or locate his clip, but it also cannot show that the clip is absent from the compilation. Reopen only for a lawful compilation audio file, transcript/captions, or an Arday-specific segment boundary. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-875/C-875: Surviving Society Spotlight compilation recovered as access-boundary record

Discovery: a SoundCloud search for uncatalogued Arday media surfaced Surviving Society’s “The Spotlight Series Best Bits! (Part One),” published 11 April 2022. The host description names Arday among seven featured contributors and links the three Spotlight Series playlists.

Capture: the 34:46.945 track page, oEmbed JSON, artwork, and page headers were preserved. SoundCloud hydration exposed HLS/progressive routes, but the current direct media request returned HTTP 401; no audio binary, transcript, captions, or Arday-specific segment boundary was recovered.

Decision: created a distinct compilation manifestation and kept it separate from Arday’s individual Surviving Society episodes. The description verifies host representation and series topology, not the content or truth of any Arday remark. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-874/C-874: Hawaii Project memoir listing boundary

Discovery: a fresh retailer search surfaced The Hawaii Project’s product listing for *Great and Unfortunate Things*. Its indexed copy repeats the memoir-side “second youngest of three boys” wording and familiar childhood marketing language.

Capture: a direct retrieval returned HTTP 403 with a 239-byte error body. The response body and headers are preserved locally; no product image, excerpt, edition variant, or full text was exposed.

Decision: created a retailer/source-propagation record and deduplicated it to the existing memoir and catalogue records. The listing is useful for tracking how the biography propagates, but it is not independent corroboration. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-873/C-873: Ruling Passions handbook recovered

Discovery: Sheffield Hallam University Research Archive’s published 2023 *Ruling Passions: A Research Informed Handbook* was found as a distinct project document. The handbook was made for the ESRC Festival of Social Sciences and its printed p. 56 podcast guide names Jason Arday as Episode 2 guest, summarizing race, autistic masking, vulnerability, motivation, academic expectations, and music.

Decision: preserved the 1,929,207-byte PDF, extracted text, and response headers as SRC-873, linked them to the existing interview record, and added C-873. The guide strengthens episode provenance and topic topology but is not a transcript or independent corroboration of the interview’s autobiographical material. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-438/C-872: Glasgow author-index recheck

Recheck: the University of Glasgow Enlighten author page returned HTTP 200 with a byte-distinct HTML body and a generated-page timestamp of 8 August 2026 at 22:32:14 BST. The same four 2022 DOI-linked works remain listed. A diff shows markup-serialization changes and the generated timestamp, not a new output or changed DOI/title set.

Decision: preserved the recheck HTML and headers under SRC-438 and added C-872 as a bounded index-state observation. Existing DOI-level records remain canonical; no publication or authorship claim was upgraded. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-289/C-871: LJMU profile changed-state recheck

Recheck: the LJMU “Black researchers and professionals” URL returned HTTP 200, but the 212,560-byte captured HTML body was byte-distinct from the earlier 213,445-byte page and contained no “Jason” or “Arday” occurrence. The prior page listed Arday as a former lecturer, described LJMU qualifications, and linked a portrait.

Decision: preserved the current response as a changed-page/negative-space state under SRC-289. The archive does not infer removal, disavowal, correction, or an investigation outcome; the earlier page remains the source-version for the published biography wording. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-612/C-870: QUB article-record page-state recheck

Recheck: the canonical Queen’s University Belfast Research Portal record for *Attempting to break the chain* returned a byte-distinct HTML body. The captured page displayed 184 Scopus citations and 1,555 downloads; its title, authors, DOI, dates, pagination, and accepted-manuscript/peer-reviewed-version labels remained unchanged.

Decision: preserved the recheck HTML and headers within SRC-612 and added C-870 as a volatile page-state observation. The metrics are not treated as evidence about article quality, validity, or the separate QUB investigation. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-094/C-958: Good Law Project changed retrieval state

Recheck: the canonical “An update from Jason Arday” page returned HTTP 200. The raw HTML and response headers are preserved under `assets/captures/2026-08-08-good-law-project-update/`. The HTML is byte-distinct from the 6–7 August captures, but extraction after removing script, style, and noscript content produced the same 4,837-character visible text.

Decision: added C-958 as a source-version/retrieval-state observation and retained the earlier capture. No new statement, exoneration, misconduct finding, or institutional outcome was inferred. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-263/C-944: Cambridge panel sidecars and review clip promoted

Archive action: promoted SRC-263’s automatic-caption copies, metadata JSON, thumbnail, and the existing 48,473,641-byte stream-copy review clip covering source interval 01:11:00–01:31:30. The 287,422,026-byte parent MP4 remains local-only because it exceeds GitHub’s 100 MiB hard limit.

Decision: added C-944 as an archive-integrity observation. The sidecars make parent provenance inspectable and the bounded clip improves audiovisual handoff; neither is a human-verified transcript or a new substantive claim. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-08 — SRC-633/C-867–C-868: BERA staff-equality report recovered

Discovery: a BERA report-page search surfaced a distinct public research output not present in the canonical output index: *Education: The State of the Discipline: An exploration of existing statistical data relating to staff equality in UK higher education*.

Capture: the official BERA page, 78-page PDF, extracted text, response headers, and linked XLSX data tables are preserved under `assets/captures/2026-08-08-bera-state-discipline/` and `assets/documents/bera-state-discipline-2023/`. The report names Dina Zoe Belluigi as principal investigator and Jason Arday and Joanne O’Keeffe as authors, and gives a January 2023 publication date.

Decision: added SRC-633 and C-867–C-868 as a distinct first-party report and underlying-data artifact. The report analyzes HESA staff data from 2015–16 through 2019–20 and is kept separate from the later journal article with overlapping themes. Its findings are attributed to the report and are not converted into personal claims about Arday.

## 2026-08-08 — SRC-634/C-869: South Bank Colleges board-minutes award corroboration

Discovery: a public South Bank Colleges Board-minutes PDF surfaced in a search for institutional records of Arday’s honorary fellowship.

Capture: the eight-page PDF, extracted text, response headers, and rendered printed page 4 are preserved under `assets/captures/2026-08-08-sbc-board-minutes-honorary-fellowship/`. Page 4 records that the October 2024 Royal Festival Hall Level 3 and 4 graduation ceremony included the group’s first Honorary Fellowship, awarded to Professor Jason Arday.

Decision: added SRC-634/C-869 as a distinct governance-document manifestation linked to the existing South Bank Colleges graduation record. The award is corroborated by the board’s own minutes; the repeated Cambridge superlative remains host wording and is not upgraded to a current-status claim.

## 2026-08-08 — SRC-106/C-866: BME-participation publisher and full-text manifestation recheck

Discovery: a focused exact-title/DOI search surfaced Cambridge Core’s public article record and ResearchGate’s public full-text manifestation, while confirming that the Liverpool Repository record remains indexed as an accepted-manuscript lead.

Capture: Cambridge’s article HTML and headers, its PDF-request redirect/HTML response, and ResearchGate’s HTTP 429 PDF response are preserved under `assets/captures/2026-08-08-bme-participation-publisher/` and `assets/captures/2026-08-08-bme-participation-researchgate/`. The ResearchGate page renders the article text and identifies Vikki Boliver as the uploader on 8 October 2021, but no local PDF was recovered.

Decision: upgraded SRC-106 and added C-866 without creating a duplicate work. The publisher and ResearchGate records are provenance/version witnesses; the article’s empirical and interpretive claims remain claims made within the scholarly work and are not independently re-adjudicated here. Do not repeat these retrieval URLs without a changed access state or authorized access.

## 2026-08-08 — SRC-631/C-864: PrimeTimes controversy source-version

Discovery: a current exact-name search surfaced PrimeTimes’ 24 July 2026 article by Sunnex Egbu, a secondary summary of the thesis-plagiarism allegations and the reported Cambridge/Liverpool John Moores response.

Capture: the article returned HTTP 200; full HTML and response headers are preserved under `assets/captures/2026-08-08-primetimes-arday-allegations/`. The body contains an unrelated advertising injection, which is excluded from the source record.

Decision: added SRC-631/C-864 as a low-confidence controversy-propagation witness. Its reported “cleared”/valid-PhD wording is deduplicated to direct institutional and broadcaster records and is not treated as an independent finding. Reopen only for a materially changed article, a primary quotation, or the underlying university document.

## 2026-08-08 — SRC-632/C-865: Adnkronos international source-version and image

Discovery: image search surfaced an Adnkronos report published 6 August 2026 about Arday’s resignation and the Cambridge investigation.

Capture: the Italian page returned HTTP 200. Its HTML, headers, and the article-associated 590×442 JPEG still are preserved under `assets/captures/2026-08-08-adnkronos-arday-resignation/`.

Decision: added SRC-632/C-865 as a secondary international journalism/source-version record. The article’s translated/editorial framing and repeated biography, fundraising, and allegations are not independent corroboration; the still is preserved as an image provenance artifact with unknown underlying video and reuse rights.

## 2026-08-08 — New York Times attribution boundary

Recheck: exact-name and domain searches surfaced only secondary outlets attributing parts of the controversy to *The New York Times* and named reporters Jennifer Schuessler and Alexandra Alter. The search layer reported `nytimes.com` blocked by robots; no direct NYT URL, licensed reproduction, archive replay, or locally capturable page was recovered.

Decision: kept the NYT material as an unresolved secondary attribution under SRC-613 and the controversy entity. No new source ID or claim was created. Reopen only for a lawful direct article/source-version or a primary document.

## 2026-08-08 — SRC-182: Liberated Library DOI-pair recheck

Recheck: current DataCite API responses for `10.17613/dc03s-05j04` and `10.17613/635kx-wb026` retain the same presentation title, six creators including Jason Arday, 2018 issued year, Knowledge Commons publisher, and reciprocal version relationship. Normalized bibliographic fields are unchanged. Both Humanities Commons routes still return the same short HTTP 403 shell.

Capture: preserved fresh DataCite JSON/headers and Humanities Commons HTML/headers under `assets/captures/2026-08-08-liberated-library-recheck/`. No presentation binary, transcript, slides, or recording was recovered.

Decision: updated SRC-182 in place; no new claim or duplicate work was created. Reopen only for a changed DOI record, lawful Humanities Commons file, transcript, slide deck, recording, or distinct event artifact.

## 2026-08-08 — SRC-630/C-862: Emerald teacher-education volume manifestation

Discovery: an exact-title search surfaced Emerald’s current bookstore route for *Teaching About Social Justice Issues in Physical Education*. Its indexed publisher rendering identifies Arday’s chapter 15, “Equality and Diversity in Teacher Education: Developing an Understanding of Race and Ethnicity in the Classroom,” and reports the 19 August 2019 hardback ISBN `9781641137201`.

Capture: the live bookstore route returned Cloudflare HTTP 403; HTML and headers are preserved under `assets/captures/2026-08-08-teacher-education-emerald-bookstore/`. No chapter binary was recovered.

Decision: added SRC-630/C-862 as a publisher source-version deduplicated to SRC-074. It strengthens edition/contents provenance without upgrading the unresolved DOI or chapter text.

## 2026-08-08 — SRC-180/C-863: Springer encyclopedia chapter access-topology recheck

Recheck: both official DOI/chapter URLs for the 2020 and 2022 *Encyclopedia of Teacher Education* manifestations now redirect through Springer’s `/rwe/` route and an identity-provider/cookie flow. The resulting pages still expose title, author, edition, and pagination metadata; no PDF or chapter text was exposed.

Capture: preserved current Springer HTML/redirect headers and fresh Crossref JSON/headers under `assets/captures/2026-08-08-springer-mental-health-staff-recheck/`.

Decision: updated SRC-180/SRC-073 in place and added C-863 as an access-topology observation. No new edition or duplicate chapter was created. Reopen only for a lawful full text, author manuscript, changed publisher access state, or correction.

## 2026-08-08 — SRC-629/C-861: Bloomsbury UK manifestation of *The Fire Now*

Discovery: an exact DOI/title search surfaced Bloomsbury’s UK product page as a distinct official publisher manifestation. Its indexed rendering names Arday’s chapter and exposes the host book’s 15 November 2018 date, 304-page extent, ISBN `9781786993793`, Zed Books imprint, and chapter placement.

Capture: the direct UK URL returned a Cloudflare HTTP 403 challenge; its HTML and headers are preserved under `assets/captures/2026-08-08-fire-now-bloomsbury-uk/`. No publisher PDF or chapter text was recovered.

Decision: added SRC-629/C-861 as a publisher source-version deduplicated to SRC-078. The metadata strengthens the canonical chapter record but does not create a second publication or support content claims.

## 2026-08-08 — SRC-109: SEB recording artifact recheck

Recheck: the canonical YouTube page for `H30IeW5J69I` was fetched again. It still renders “Video unavailable”; no playable stream, caption track, or downloadable media route was exposed. The SEB first-party page and Class Central listing remain the strongest public attribution/runtime records.

Capture: preserved the current YouTube HTML and response headers plus a fresh 1280×720 thumbnail under `assets/captures/2026-08-08-seb-video-recheck/`. No video binary or OED22 programme file was recovered.

Decision: updated SRC-109 in place rather than creating a duplicate source. Reopen only for a changed YouTube/SEB state, a lawful archive replay, a direct media file, captions/transcript, or the programme binary.

## 2026-08-08 — SRC-079: Bloomsbury chapter mirror state reconciled

Recheck: an exact-title search again exposed a TransReads PDF result with a contents snippet naming Arday’s “Trying to Break the Monopoly” chapter. The web retrieval layer reported 404 when opening the indexed PDF URL, while a direct shell request returned the already preserved WordPress HTTP 403 authorization response.

Decision: updated SRC-079 in place to separate stale search indexing from the live endpoint. No unofficial full-book binary was downloaded or promoted, and no chapter-content claim was added. Reopen only for a lawful publisher, library, repository, archive, or author-supplied chapter manifestation.

## 2026-08-08 — SRC-423/C-844: broad Crossref author recheck

Recheck: a no-date Crossref Works query using `query.author=Jason Arday` returned the 1,000-item ranking cap from 353,684 results. A strict author-list pass found 47 records with given name beginning “Jason” and family name “Arday”; DOI comparison against all source records found zero unmatched DOI/title keys.

Decision: appended the broad raw response and hashes to the existing SRC-423 search-boundary record. No new publication node was created. The result closes this exact broad Crossref query for the captured state while preserving its ranking/cap limitation.

## 2026-08-08 — SRC-139: ITV press-PDF route checked

Discovery: the ITV press-centre print route surfaced as a distinct five-page PDF manifestation of the already-canonical 30 January 2024 Cultural Advisory Council announcement. The web renderer exposes the membership, council remit, Arday’s dated biography, and his closing quotation.

Capture boundary: the in-app browser refused the PDF route with a client-side block; repeated shell retrievals hung before returning PDF bytes or usable headers. No local PDF is claimed.

Decision: upgraded SRC-139 as a PDF source-version/access boundary without creating a duplicate council appointment or new claim. Reopen only for a changed ITV endpoint or lawful local PDF route.

## 2026-08-08 — SRC-093/C-843: Cambridge statement changed to missing-page state

Recheck: the canonical Cambridge “Statement about Professor Arday” URL, which had returned a live statement on the earlier 8 August check, later returned Cambridge’s generic HTTP 200 page-not-found document titled “Page not found: we need time to evolve.” The response contained no substantive statement copy.

Preservation: restored the earlier live recheck under its original path and preserved the later 404 response under `assets/captures/2026-08-08-cambridge-statement-404-recheck/`.

Decision: upgraded SRC-093 in place and added C-843 as an access-state observation. No institutional outcome, withdrawal, or deletion claim is inferred.

## 2026-08-08 — SRC-157: ARU Unlearn page rechecked

Recheck: the current Anglia Ruskin “Unlearn” page still links the already-catalogued 2 April 2025 Jason Arday Lightbulb recording, YouTube ID `LOZW-J1hcd4`, and the same host description of neurodiversity, race, and education. The current page is byte-distinct from the 6 August capture; no new event, recording, caption track, or substantive claim was found.

Decision: preserved the current page and response headers as a source-version recheck under SRC-157. No duplicate event node or new claim was created.

## 2026-08-08 — SRC-199/C-116: Surviving Society E188 audio recovered

Discovery: a fresh recheck of the already catalogued 2 January 2024 “Jason Arday & Chantelle Jessica Lewis: Surviving Society (then and now)” SoundCloud page exposed current hydration metadata with public HLS AAC and MP3 transcodings, despite the earlier direct progressive route returning HTTP 401.

Capture: preserved the current track HTML/headers, yt-dlp metadata, current artwork, and a 32-MiB HLS AAC manifestation. The metadata reports a displayed duration of 2,779.068 seconds and full duration of 2,779.063 seconds; the local file is 46:19.07 by the host duration convention. Audio SHA-256: `f8fb9538f5ab47b9b712296f02643ce03e63573ad48c3bd44af321355170927f`.

Decision: upgraded SRC-199/C-116 rather than creating a duplicate episode node. No transcript, manual listening audit, or timecoded biographical claim is added yet.

## 2026-08-08 — SRC-197/C-114: Surviving Society E031 audio recovered

Discovery: a fresh SoundCloud page recheck for the already catalogued 23 April 2019 “Growing up Black in the 90s” episode exposed current hydration metadata with public HLS transcodings, despite the earlier direct progressive request’s HTTP 401.

Capture: preserved the current track HTML/headers, yt-dlp metadata, current artwork, and an 83-MiB HLS AAC manifestation. The metadata reports a displayed duration of 4,305.636 seconds and full duration of 4,306.061 seconds; local audio is 1:11:45.64 by the host duration convention. Audio SHA-256: `1f527e382afb9743966774e0edb7db944a6c179d200d3045d3c092781405a355`.

Decision: upgraded SRC-197/C-114 rather than creating a duplicate episode node. No transcript, manual listening audit, or timecoded biographical claim is added yet.

## 2026-08-08 — SRC-620/C-842: Get Further annual report recovered from Charity Commission

Discovery: official Charity Commission search results identified a distinct 2023/24 Get Further trustees’ report and financial statements, separate from the charity’s January 2025 patron announcement.

Capture: the official accounts page, response headers, and 38-page PDF were recovered. The report’s 2024 achievements section states that Get Further appointed its first Patron, Professor Jason Arday, and repeats the late-literacy/professorial biography wording. PDF SHA-256: `c35bb2ee935421b526575a1d6c87c2c5449c9387706a58a65ce4435f4c4672e7`.

Decision: added SRC-620 and C-842 as a distinct regulator-hosted manifestation, linked to SRC-165 rather than creating a duplicate appointment. Charity accounts are not treated as Arday’s personal financial evidence. No role end date or independent verification of the promotional biography was found.

## 2026-08-08 — SRC-619/C-836–C-837: Wonkhe recording recovered through IASPM repository article

Discovery: the Leeds Arts University Repository record for Jason Huxtable’s *IASPM Journal* article “Pragmatic White Allyship for Higher Education Popular Music Academics” exposed a direct alternate PDF route and named the underlying Wonkhe YouTube recording.

Capture: recovered the complete seven-page PDF, extracted text, page-3 render, repository record, YouTube HTML/headers, a 144p MP4, both English automatic-caption variants, and video metadata. The article links Arday’s coded contribution to recording position 30:21.

Decision: added SRC-619 and C-836–C-837. This is a distinct event/media source-version, not a new Arday-authored publication. The local binary makes the event resumable; the captions remain navigation aids pending manual listening, so no caption wording is promoted as a verified verbatim quote.

## 2026-08-08 — SRC-618/C-835: Cumberland Lodge “Beyond Tokenism” media boundary

Discovery: a search for uncatalogued interviews and event recordings surfaced Cumberland Lodge’s first-party resource page for its 3 November 2021 Dialogue & Debate webinar.

Capture: preserved the page, Vimeo player/configuration responses, Vimeo oEmbed metadata, and SoundCloud page/API responses. The page identifies Vimeo video `622494311` and an audio-only SoundCloud manifestation.

Decision: added SRC-618 and C-835. Vimeo currently returns a 403/Cloudflare boundary and SoundCloud’s API returns 401 without authorization, so no binary, transcript, captions, or substantive Arday remarks are claimed. The event is retained as verified media topology and panel participation, not as a recovered recording.

## 2026-08-08 — SRC-617/C-834: *Hindustan Times* sports/biography source-version

Discovery: an exact sports/biography search surfaced Nisha Anand’s 28 February 2023 *Hindustan Times* profile, a distinct public manifestation from the already catalogued BBC, News24, Open Culture, and institutional pages.

Capture: preserved the public AMP HTML, response headers, and 550×309 lead image.

Decision: added SRC-617 and C-834. The article is retained as secondary reporting and a source-propagation witness. Its football/professional-snooker aspiration is not promoted into a verified sports-career claim.

## 2026-08-08 — SRC-614/C-828–C-829: LJMU neurodiversity page current recheck

Recheck: the direct LJMU neurodiversity page returned an HTTP 200 response with byte-distinct raw headers/body capture, but the normalized page body matched the earlier capture after stripping transport whitespace.

Decision: the recheck still lists only five other SoundCloud extracts and contains no Arday occurrence, title, or Arday-specific SoundCloud URL. Added the current headers and normalized body to SRC-614 as a recheck, not a new media or event node. The indexed result remains a stale/direct-response mismatch.

## 2026-08-08 — SRC-616/C-833: *The Times* teaser and access boundary

Discovery: the canonical *The Times* article URL was directly reachable as a publisher teaser. It exposes the headline, Fiona Hamilton byline, public standfirst, and article dates, but stops at the subscription prompt.

Capture: preserved the full teaser HTML and response headers. No article body, interview transcript, image, or downloadable media was recovered.

Decision: added SRC-616 and C-833. The standfirst is logged as a reported self-position, not as evidence that the allegations are true or false. Do not reconstruct the paywalled article from unattributed reposts or social-media quotations.

# 2026-08-08 — SRC-611/C-817–C-823: BBC multi-institution hiring-review report

Discovery: the BBC’s related report on Cambridge’s senior-academic hiring review was publicly accessible at a distinct article URL. It contains attributed statements from Cambridge, Jesus College, the University of Glasgow, and Liverpool John Moores University, plus reported memoir/publication discrepancies.

Capture: preserved the full BBC HTML, response headers, plain-text extraction, and 1200×675 article image. The article records Cambridge’s review/process language, Glasgow’s review of Arday’s appointment, LJMU’s reported “honest and reasonable error” and PhD-standing position, Jesus College’s contingent-fellowship statement, and *The Atlantic*-reported proposal/memoir differences.

Decision: added SRC-611 and C-817–C-823. Overlapping Cambridge process language is treated as corroboration of existing claims; the Glasgow, LJMU, Jesus, memoir-version, and unpublished-book edges are separately typed. No institutional finding or fabrication conclusion was inferred.

# 2026-08-08 — SRC-610/C-813–C-816: BBC report of QUB investigation

Discovery: a BBC News NI article, identified from its public article URL, reports that Queen’s University Belfast is looking into the 2021 Arday-co-authored *Attempting to break the chain* paper. The article quotes a QUB spokesperson saying that the university is liaising with other UK universities.

Capture: preserved the public BBC HTML, response headers, plain-text extraction, and 1200×675 article image. The report also records the paper’s interview/recommendation context and Arday’s reported denial of plagiarism and explanation that autism and inadequate early supervision contributed to errors.

Decision: added SRC-610 and C-813–C-816 as a current institutional-response/reporting edge linked to the existing article and methodology/correction records. No misconduct, fabrication, or outcome claim was created. The next action is direct QUB documentation or a changed publication/investigation state.

# 2026-08-08 — SRC-609/C-811–C-812: full 2013 peer-mentoring article recovered

Discovery: the Durham output record for Arday’s 2013 article linked to LJMU Open Journals volume 8, issue 1.

Capture: downloaded the complete 147-page publisher issue PDF, its response metadata, and the issue page. Extracted the article from PDF pages 37–48 and rendered the opening and closing pages for visual verification.

Decision: upgraded the existing DOI-less bibliographic record with a first-party article source-version. The article’s own abstract and introduction describe a literature-based contextual synopsis of peer mentoring, with an early-career-lecturer focus and discussion of benefits and risks. No duplicate publication node was created and no original participant sample was inferred.

# 2026-08-08 — SRC-608/C-809–C-810: Durham repository manifestation of UKCGE media lead

Discovery: Durham’s indexed Sociology output page surfaced the existing 2019 UKCGE “Research in Focus with Jason Arday” lead as a credited Digital Artefact.

Capture: the direct repository request returned a 403 Cloudflare challenge. The response HTML and headers are preserved; no recording, transcript, duration, or media binary was available.

Decision: add the Durham repository edge as a source-version of SRC-069, strengthening provenance without promoting the index record into substantive media evidence. Reopen only through a lawful page, UKCGE mirror, transcript, or media endpoint.

# 2026-08-08 — SRC-607/C-808: current OpenAlex author/work reconciliation

Discovery: the current scholarly-output audit reached the existing OpenAlex author identifier `A5048886069`.

Capture: preserved the author-search response and headers plus a fresh filtered works response and headers. The works endpoint returned 56 records spanning 2015–2026.

Decision: normalized `{id, DOI, title}` comparison found no new Jason Arday DOI/title key. No publication node was added; this exact index query is closed for the current state. Crossref’s separate recent-output boundary remains SRC-423.

# 2026-08-08 — SRC-602–SRC-604/C-802–C-804: LJMU Reciprocal Mentoring event topology

Discovery: the LJMU annual-report passage led to three first-party programme pages: the 17 November 2022 midpoint report, the 15 September 2023 closing-event report, and the 16 January 2024 project reflection.

Capture: all three LJMU HTML pages, response headers, and hero images are preserved. The 2023 page embeds the official YouTube closing-session video (`0Tr2jP2FNa0`), downloaded locally as an 81 MB MP4 with metadata and thumbnail. The 2024 page embeds the official Mark Power/Kim Johnson reflection (`h9WI5U23QdE`), downloaded locally as a 39 MB MP4 with metadata and thumbnail. The 2022 page reports Arday’s keynote with Chris Lubbe but exposes no recording or transcript.

Decision: promote the 2022 Arday keynote as a dated first-party event-report fact. Keep the 2023 and 2024 videos as project-topology and related media; do not infer that Arday appears in either video from the page embed alone. Reopen only for the midpoint programme/recording/transcript, captions, or content-level review of the closing video.

# 2026-08-08 — SRC-601/C-800–C-801: LJMU Diversity and Inclusion annual report

Discovery: a formal institutional-status search surfaced LJMU’s public Diversity and Inclusion Annual Report, dated September 2023 and covering academic year 2022/23.

Capture: the 29-page PDF, response headers, extracted text, and a rendered copy of printed page 12 are preserved under `assets/captures/2026-08-08-ljmu-edi-annual-report/`. The report says LJMU featured Jason Arday as a speaker during the mid-point session of its Leaders Reciprocal Mentoring project. It calls him “the youngest Black Professor in the UK and a current staff member at Oxford University.”

Decision: promote the event appearance and exact report wording as first-party institutional source facts. Keep the Oxford phrase as a dated source-version requiring reconciliation with the archive’s Cambridge appointment/resignation records; do not treat it as an Oxford HR record, silently correct it, or infer fraud from the discrepancy. Reopen for the event programme/recording, an Oxford appointment record, or a corrected report.

# 2026-08-08 — SRC-605/C-805: LJMU Reciprocal Mentoring launch record

Discovery: the midpoint/closing chain exposed LJMU’s 15 June 2022 launch announcement for the external Leaders Reciprocal Mentoring programme.

Capture: the public LJMU HTML, response headers, and 835×500 hero image are preserved under `assets/captures/2026-08-08-ljmu-2022-launch/`.

Decision: record the announced programme structure—paired university/city leaders, monthly meetings, and planned midpoint/closing sessions—as first-party project context. The launch page does not name Arday, so it is not used to infer either his inclusion or exclusion; the later 17 November 2022 report remains the direct source for his reported keynote.

# 2026-08-08 — SRC-606/C-806–C-807: Oxford Research Archive protocol manifestation

Discovery: an Oxford-domain search for a direct Oxford affiliation record surfaced the Oxford Research Archive item for the already-canonical 2025 BMJ Open narrative-inquiry protocol.

Capture: the ORA HTML record, response headers, public 524.2 KB version-of-record PDF, PDF headers, extracted text, and rendered pages 1 and 8 are preserved under `assets/captures/2026-08-08-oxford-ora-underrepresented-protocol/`.

Decision: add the ORA route as scholarly repository provenance, not a new article. The PDF’s affiliation topology places Arday at Cambridge’s Faculty of Education (superscript 3; printed p. 8), while Oxford affiliations belong to other authors and Oxford is the study sponsor. This materially narrows the interpretation of the LJMU report’s Oxford phrase but does not independently prove it was an error. Preserve the wording conflict and reopen only through a direct appointment record, changed ORA version, or project document specifying Arday’s role.

# 2026-08-08 — SRC-596/C-793: LJMU bicentenary profile route recheck

Discovery: the previously catalogued LJMU bicentenary profile URL was selected as a current institutional-status and source-version follow-up.

Capture: the direct route returned HTTP 404 with a 197,298-byte HTML body. The body and response headers are preserved under `assets/captures/2026-08-08-ljmu-profile-recheck/`.

Decision: record the changed route state without inferring deletion, correction, disavowal, or an institutional finding. Keep it distinct from LJMU’s current Black Researchers page and the older alumni profile. Reopen only after a replacement route or concrete primary record appears.

# 2026-08-08 — SRC-597/C-794: r/sociology peer-reaction discussion

Discovery: a current search surfaced a public r/sociology thread asking whether sociologists have a consensus about the quality of Arday’s work. The thread contains conflicting anonymous reactions, including unverified comments about methodological thinness, ethics language, focus-group feasibility, and possible fabricated data.

Capture: the in-app public page was readable and its observed content was recorded in the source note. A direct shell request returned HTTP 403 with a 1,522-byte challenge body; that body and headers are preserved under `assets/captures/2026-08-08-reddit-sociology-quality-thread/`. No access-control bypass was attempted.

Decision: classify the thread as public reception and allegation propagation, not peer consensus, scholarly review, or adjudication. Use its concrete comments only as leads for named primary texts, methods materials, and institutional records already tracked or still missing.

# 2026-08-08 — SRC-598/C-795–C-796: 2018 *Social Sciences* methods/ethics audit

Discovery: the r/sociology thread supplied a concrete lead about the 2018 mental-health article’s sample and ethics language. The locally preserved publisher PDF was audited directly rather than relying on the thread’s characterization.

Capture: PDF p. 10 reports recruitment across 14 UK-based universities, 32 participants, two roughly three-hour focus groups, 32 individual interviews, informed consent, and audio recording/transcription. A text search of the captured 25-page PDF found no explicit ethics-approval/committee/identifier wording in the audited methods/results text.

Decision: promote the reported methods and consent statement as primary-text facts about what the article says. Record the ethics-language absence as a bounded negative-space observation only; it is not evidence that no approval existed, that the participants were fabricated, or that misconduct occurred. Reopen only for an approval record, correction, author/editor response, or underlying study materials.

# 2026-08-08 — SRC-599/C-797–C-798: PubMed Central protocol manifestation

Discovery: a scholarly-index search surfaced the PubMed Central record for the already-canonical 2025 BMJ Open narrative-inquiry protocol.

Capture: PMC full-text HTML and the NCBI OA API response were preserved. The repository identifies the CC BY article, Jason Arday’s Cambridge affiliation, and a non-retracted record. Linked PDF and reviewer-comment routes returned HTML “Preparing to download” wrappers; the OA package URL returned 404 rather than a tarball.

Decision: add the PMC route as a strong repository provenance manifestation, not a new article. Preserve the HTML as available full text and the binary failures as access boundaries. Do not infer removal, retraction, or completion of the planned study.

# 2026-08-08 — SRC-600/C-799: Sciety preprint manifestation

Discovery: Sciety’s activity page surfaced a distinct public manifestation of the OSF narrative-inquiry preprint family.

Capture: the page lists the 14 contributors, Arday’s position in the contributor list, v1/v2 activity, and abstract recruitment counts. The HTML and headers are local.

Decision: deduplicate to OSF v1/v2. Treat Sciety as discovery/version metadata and abstract text, not independent validation or peer review.

# 2026-08-08 — SRC-093: Cambridge investigation-statement recheck

Discovery: the official Cambridge notice was rechecked during the formal-outcome search. It remains publicly reachable and reports “Last updated: 07 Aug 2026.” The substantive wording remains unchanged: Cambridge’s investigation concerns new information about qualifications and honorary appointments; ongoing academic-misconduct complaints remain under its policy; and Jesus College is taking its own steps.

Capture: preserved the current HTML and headers under `assets/captures/2026-08-08-cambridge-statement-recheck/`. No formal finding, timetable, report, or further primary outcome was exposed.

Decision: keep the investigation and any alleged underlying conduct unresolved. Treat the official page as process evidence only; do not infer an outcome from the unchanged notice or from resignation.

# 2026-08-08 — SRC-595/C-792: Simon & Schuster Canada memoir route

Discovery: a fresh publisher search surfaced Simon & Schuster Canada’s locale-specific route for *Great and Unfortunate Things*, ISBN `9781668085578`. Search indexing exposed the title, 37 Ink imprint, 11 August 2026 timing, 288-page metadata, and publisher synopsis.

Capture: the direct URL returned HTTP 403; the response HTML and headers are preserved under `assets/captures/2026-08-08-simon-schuster-canada-memoir/`. No page body, excerpt, image, audiobook, or full-text asset was recovered.

Decision: preserve this as an access-state/source-version record linked to the canonical memoir family. Do not create a second edition node or treat publisher synopsis as independent biography evidence.

# 2026-08-08 — SRC-429/C-489–C-490: Open University Awan thesis access-state recheck

Discovery: a current search-index result exposed the exact Open Research Online PDF URL previously recorded as a Cloudflare-bound lead. A direct recheck still returned a 6,212-byte Cloudflare challenge HTML response rather than the thesis PDF.

Capture: preserved the current challenge body and response headers under `assets/captures/2026-08-08-open-university-awan-thesis-recheck/`. No bypass or authenticated retrieval was attempted.

Decision: keep the acknowledgement thanking Professor Jason Arday for “sage advice” as indexed-text evidence only. It does not establish formal supervision, examining, employment, or co-authorship. Reopen only after a changed lawful access state or a distinct institutional role record.

# 2026-08-08 — SRC-440: Cambridge Repository exact-phrase follow-up

Discovery: the Cambridge Repository Discover API was queried for the exact phrase `"Jason Arday"` with `size=100`. It returned eight item records. Four were already-canonical Arday-authored manifestations; four additional items contained the phrase in citation/full-text context but did not identify Arday as an author or supervisor in their repository metadata.

Decision: no new publication or role node was created from the four non-author hits. The Henriques thesis remains a distinct SRC-594 record because its role evidence was directly located and page-checked. The exact-phrase query is now a closed, reproducible boundary until the API result changes or a concrete lead appears.

# 2026-08-08 — SRC-594/C-791: Cambridge Repository supervision-role record

Discovery: a current Cambridge Repository search surfaced Sasha Louise May Henriques’s thesis, *Ancestry in the Margins: Justice, Genomics, and the Ethics of Human Classification*. The repository record gives a 9 July 2026 publication date, a January 2026 thesis date, DOI `10.17863/CAM.132081`, and a public 401-page PDF.

Capture: preserved the repository HTML, item JSON, response headers, full PDF, and extracted text. The participant-information appendices name Professor Anna Middleton and Professor Jason Arday as the two PhD supervisors; the wording appears on PDF pages 308 and 312.

Decision: add this as direct first-party supervision-role evidence, distinct from repeated biography pages and current-status records. It does not establish the appointment date, examination outcome, full supervision scope, or post-resignation employment status. The repository marks the thesis all rights reserved; the publicly exposed binary is retained for provenance and citation.

# 2026-08-08 — SRC-235/C-194: BBC *Today* media-state recheck

Discovery: a current-state check of the canonical BBC programme version `m002xp5h` and podcast version `p0nsry2l` was run after the previous 7 August boundary. Both BBC Sounds routes still returned HTTP 404, while the programme JSON remained available at HTTP 200. The canonical episode and date metadata are unchanged; no audio, transcript, captions, or segment-level evidence was exposed.

Capture: preserved both 404 HTML/header pairs and the live programme JSON/header pair under `assets/captures/2026-08-08-bbc-today-2026-recheck/`. This is an access-state update to SRC-235, not a new broadcast source or appearance node.

Decision: retain the SRA/LinkedIn post as the attributed witness to Arday’s reported appearance and topic. Do not promote the approximate 1:52 position or any wording to transcript-level evidence. Reopen only after a changed BBC media state or a lawful public transcript/recording.

# 2026-08-08 — SRC-592/C-789: *tenpencemore* “Black Excellence” analysis

Discovery: the unresolved-biography and post-resignation search surfaced Penny Rabiger’s 25 July 2026 essay, “‘Black Excellence’ as a Fragile Construct: Jason Arday, Racialised Scrutiny, and the Unequal Politics of Mistakes.”

Capture: preserved the full public WordPress HTML, response headers, and 1852×712 article image. The essay treats the controversy as both an academic-integrity dispute and a case study in racialized, gendered, classed, and disability-related scrutiny.

Decision: add a distinct interpretive/commentary node. The article’s defense of applying standards while examining unequal scrutiny is the author’s analysis; it does not establish or disprove plagiarism, fabrication, or any biographical claim.

# 2026-08-08 — SRC-591/C-788: 21percent Carter-Ruck-cost commentary

Discovery: a targeted search for the reported legal-response and police-investigation trail surfaced 21percent.org’s 28 July 2026 post “Who paid for Carter-Ruck …”. It is distinct from the earlier 21percent plagiarism post and from Retraction Watch’s reporting.

Capture: preserved the public HTML, response headers, and attached 1006×1024 PNG. The article body asks whether Arday or Cambridge paid Carter-Ruck and argues that the question bears on institutional transparency. Comments remain in the raw HTML but are excluded from the evidence graph.

Decision: create a commentary/source-propagation node, not a payer or corruption claim. No public invoice, engagement letter, client-identification line, FOI response, or institutional statement resolving the question was recovered.

# 2026-08-08 — SRC-590/C-787: *The Free Press* editorial analysis

Discovery: targeted post-resignation searches surfaced Yuan Yi Zhu’s 5 August 2026 *The Free Press* essay, “Who Had to Lose for Jason Arday to Win?” This is a distinct editorial source, not a duplicate of the Cofnas newsletter, AP report, Guardian coverage, or Vainker commentary.

Capture: the public Substack HTML and response headers were preserved, along with the 1800×1200 hero image. Structured metadata identifies the author, title, date, description, and 8 August modification timestamp. The embedded post state marks the article hidden/paywalled.

Evidence handling: only the public metadata, framing, access state, and image are promoted. No full article text, allegation, institutional finding, or exoneration is inferred from the unavailable body.

# 2026-08-08 — SRC-589/C-786: Stephen Vainker defensive commentary

Discovery: a search for post-event summit evidence also surfaced Stephen Vainker’s 27 July 2026 *The Wreckage* essay, “Leave Jason Arday alone - this is a scandal of academic educational leadership.”

Capture: the full public Substack HTML and response headers were preserved. The article body is 1,177 words and includes links to existing Cofnas/Arday materials and a reproduced passage attributed to Hilary Cremin; platform comments remain in the HTML snapshot but are not treated as evidence.

Evidence handling: this is a distinct defensive commentary/source-propagation node. Its account of managerialism, institutional protection, hiring motives, and racialized criticism remains the author’s analysis. It adds no primary case file, investigation report, or exonerating finding, and the reproduced correspondence remains independently unauthenticated.

# 2026-08-08 — SRC-306/C-784–C-785: African Allied Health promotional video recovery

Discovery: the preserved public LinkedIn HTML for the African Allied Health Network’s Accra summit promotion retained signed 720p MP4 and WebVTT URLs even though the original direct request had returned HTTP 403 `deny-InvalidToken`.

Capture: retrying those embedded URLs yielded a valid 3,690,670-byte 720p MP4 and 1,628-byte WebVTT caption track running to approximately 1:02.94. The earlier 403 body and headers remain preserved as a superseded access state.

Evidence handling: the clip is promotional media. Its machine-generated captions repeat the autism/speech/literacy/Cambridge biography and include a short first-person excerpt, but do not establish clinical, educational, family, employment, attendance, or keynote-delivery facts. The summit outcome remains unresolved.

# 2026-08-08 — SRC-517 follow-up: targeted MBE-podcast non-match

The *Washington Free Beacon* report says that a 2023 podcast included an account of an MBE offer that Arday declined, but does not name the programme. I checked the two locally preserved 2023 interview records most likely to be confused with that lead: Channel 4’s *Ways to Change the World* episode, including its audio/video captions, and WNYC’s *The Takeaway* episode, including its publisher-hosted transcript. Neither contains an MBE, Order of the British Empire, or equivalent award passage.

Decision: this is a bounded non-match, not negative proof. The Free Beacon statement remains attributed secondary reporting; the underlying podcast, offer correspondence, and CV remain uncaptured. Do not repeat these two episode checks unless a new search lead identifies a different programme or a changed transcript/audio state.

# 2026-08-08 — SRC-086/SRC-588/C-779–C-783: Nelson Mandela University CV recovery

Discovery: the canonical January 2020 CV endpoint still returned a page-not-found state, but Internet Archive CDX exposed valid 2021 and 2023 PDF captures. The 30 July 2023 replay was recovered as a valid eight-page PDF.

Capture: preserved the archived PDF, response headers, extracted text, and eight rendered pages. PDF metadata gives a 22 January 2020 creation date. The document lists qualifications, previous and external appointments, professional-service roles, trusteeships, publications, supervision, and the Purley & Woodcote Labour-candidate wording.

Decision: added SRC-588 as a recovered manifestation linked to SRC-086 rather than replacing the current-host access boundary. Updated the existing CV claims and biography to distinguish the now-auditable dated document from independent host verification and current-status evidence. The Free Beacon’s separately reported unpublished CV claiming just over £1.5m remains unresolved; this recovered 2020 CV contains no such fundraising total.

# 2026-08-08 — SRC-530/SRC-587/C-773–C-778: BABAO review recovery and follow-up

Discovery: the earlier BABAO record had only browser-readable PDF text and a direct-retrieval 403 boundary. A University of Derby repository result exposed the same report, and the Internet Archive CDX listed valid 2023 and 2024 captures. BABAO’s own review page and annual reviews supplied commissioning and implementation context.

Capture: recovered the 25-page 29 March 2024 Wayback PDF, extracted text, rendered pages, BABAO’s commissioning and current EDI-resource pages, and 2021/2022 annual-review PDFs with extracted text and selected renders. The recovered PDF’s SHA-256 is `80ca6aa782fe05b1593f97a0a9a8a17f2a8f905ace6a2ec8cb73f1a2aaf2fa80`.

Decision: added SRC-587 as a manifestation/follow-up record linked to SRC-530 rather than creating a duplicate review. The report’s methodology, limitations, 27 recommendations, BABAO’s stated 2021 work-plan adoption, and 2022 mixed KPI status are now auditable. Underlying payment, conference attendance, later completion, and continuing Arday involvement remain unresolved.

# 2026-08-08 — SRC-586/C-769–C-772: RIA–British Council dialogue materials

Discovery: the official British Council event page exposed the 30 January 2020 Royal Irish Academy/British Council dialogue context, programme PDF, discussion-paper PDF, Facebook live lead, and a Kaltura embed for Jason Arday. Direct shell retrieval of the current page returned an Akamai access-denied body, so the browser-readable page state and its access boundary were both retained.

Capture: recovered the valid 8-page programme PDF, valid 12-page discussion report, extracted text, rendered pages, the Kaltura HLS manifest, delivery headers, and the 1:13.61 Arday MP4. The programme schedules his 12:45 keynote and 15:45 plenary participation; the discussion report names him as a keynote speaker and footnotes an Arday presentation at the 30 January 2020 workshop.

Decision: added SRC-586 as the first-party event/media family and linked it to SRC-584 without duplicating the keynote. The official 2020 event materials conflict with SRC-584’s visible 30 January 2019 title-slide date; the discrepancy is preserved as a claim rather than silently resolved. The recovered MP4 is catalogued as a short clip, not the full talk.

# 2026-08-08 — SRC-292/C-274: Aevitas profile changed-state recheck

The canonical Aevitas Creative Management client page was fetched again after the resignation-related source updates. It returned HTTP 200, but the HTML body was byte-identical to the 6 August capture and retained current-tense Cambridge Professorial Chair and “youngest-ever” marketing language. The response headers were newly captured and report a 6 August `Last-Modified` value.

Evidence handling: this is a changed retrieval state with no substantive page change. It strengthens the stale-marketing-copy boundary and does not establish current employment, continued representation, or the superlative.

# 2026-08-08 — SRC-580/C-757: Valid Science commentary and exhibit capture

Discovery: a current controversy search surfaced José Duarte’s *Valid Science* Substack article, “Jason Arday plagiarized other researchers’ DATA – and the journal helped him cover it up,” published 4 August 2026 and modified 6 August.

Capture: preserved the full public HTML, response headers, seven embedded/public image binaries, and the platform-generated text-to-speech MP3. This is a distinct commentary source, not a duplicate of Nathan Cofnas’s Substack or the existing *Analyse That* audit.

Evidence handling: the article’s allegations and evaluative framing remain attributed. Its exhibits are preserved for comparison against the canonical thesis, publication, correction, and page-level audit records; no claim of plagiarism, fabricated data, or fraud is promoted from this source alone.

# 2026-08-08 — SRC-133/C-740: JustGiving legacy-route resolution

The search lead `https://www.justgiving.com/fundraising/400in5days` was directly captured. Its current page title and embedded story identify the page as “The 300 (300 miles in 3 Days),” with the same 2011 campaign context already represented by SRC-133. The route is recorded as an alias/access-state manifestation, not a new fundraiser source.

Evidence handling: no claim is made that a separate 400-mile-in-five-days challenge occurred. The capture resolves a likely search-result ambiguity and prevents the route from being counted twice.

# 2026-08-08 — SRC-305/C-741: UAL *Opening Out* changed access state

The canonical University of the Arts London page for the 4 March 2026 *Opening Out* event was fetched again. It now returns HTTP 403 with a Cloudflare browser-verification challenge; the 5,639-byte response and headers are preserved as a changed state under the existing SRC-305 record. The matching Eventbrite listing remains the usable event/registration manifestation.

Evidence handling: no new claim about attendance, delivery, recording, transcript, or cancellation is made. The changed 403 is an access observation only.

# 2026-08-08 — SRC-144/C-739: direct BBC profile capture upgrade

The canonical BBC `.co.uk` and `.com` URLs for “Cambridge University's Jason Arday becomes youngest black professor” returned the article directly on 8 August 2026. Captured both HTML variants, response headers, the BBC-hosted portrait, and the graduation image. The existing SRC-144 record is upgraded in place; the Walthamstow School for Girls repost remains a separate witness manifestation rather than a duplicate source.

Evidence handling: the direct capture establishes first-party publisher provenance and the page’s current retrievability. The childhood, sports, literacy, education, and career details remain reported interview material and are not thereby converted into independent school, clinical, employment, or sports records.

# 2026-08-08 — SRC-548/C-705–C-706: APPG STEM workforce report

Discovery: a report search surfaced the British Science Association’s current APPG page and official download for the July 2021 *Inquiry into Equity in the STEM Workforce*. The final PDF was captured from the BSA download endpoint, with page HTML, headers, extracted text, and a rendered cover preserved.

Evidence handling: the report’s appendix lists “Dr Jason Arday, Durham University” in the policy group that shaped recommendations through a 13 May 2021 session and lists him among critical reviewers (PDF pp. 80–81). The report says its inquiry used more than 85 written submissions, four roundtables with more than 40 attendees, and desk research covering more than 150 sources. This is a dated contributor/reviewer and policy-output record, not proof of report authorship, a particular evidence submission, or independent validation of the report’s findings.

# 2026-08-08 — SRC-318/C-707: OpenLearn printable access-state recheck

The current OpenLearn course page exposes a PDF download control, and indexed text exposes the `UNI_1` printable manifestation dated 9 December 2025. A direct request to the printable endpoint still returned HTTP 403 Cloudflare HTML; the short-lived signed-object route embedded in the challenge was not treated as a recovered PDF. Updated SRC-318 and preserved the new 8 August response and headers as a changed access-state record.

# 2026-08-08 — SRC-175/C-704: Springer chapter abstract/access boundary

The current Springer chapter page for “Being Black, Male and Academic: Navigating the White Academy” was captured as a distinct source-version. Its official abstract explicitly calls the chapter auto-ethnographic and a counter-narrative about personal experiences of racism, employment opportunities, staff/student perceptions, Whiteness, and racial microaggressions. The page confirms first-online 1 September 2018 and pp. 161–174, but keeps the chapter body subscription-gated. Recorded this as an author/publisher scope description, not independent corroboration.

# 2026-08-08 — SRC-532/C-677: University of Westminster honorary doctorate

Discovery: a focused institutional-report search surfaced Westminster’s award announcement as a distinct first-party manifestation not yet in the registry. The page records the Honorary Doctor of Letters, graduation remarks, and a credited ceremony photograph. Its childhood and Cambridge-superlative wording is retained as repeated institutional biography, not upgraded to independent proof.

Capture: page HTML, response headers, and the 800×450 JPEG were downloaded from Westminster’s canonical URL. No speech recording or transcript was exposed.

# 2026-08-08 — SRC-533/C-678: Daily Sceptic commentary

Discovery: a focused controversy-media search surfaced Will Jones’s 25 July 2026 *Daily Sceptic* article, a distinct public commentary source not yet in the registry. It repeats the public allegations and biography but contributes no new primary audit or institutional finding.

Capture: article HTML, response headers, and the 940×614 article image were downloaded from the canonical URL. The source is retained as a low-provenance propagation witness, with its rhetorical labels kept attributed.

# 2026-08-08 — SRC-534/C-679: EC Science childhood-profile source-version

Discovery: the childhood/education search surfaced EC Science’s 1 February 2024 Black History Month profile by Jacie Chandler. It is a distinct organizational profile not yet in the registry, but its biographical material is uncited and repeats existing public narratives.

Capture: page HTML, response headers, and the 940×726 article image were downloaded. The record is linked into the childhood evidence map as propagation topology, not independent corroboration.

# 2026-08-08 — SRC-535/C-680: Luke Ford commentary and access boundary

Discovery: the controversy search surfaced Luke Ford’s 21 July 2026 long-form article, a distinct synthesis not yet in the registry. The browser-readable article separates corrections, allegations, and unknowns and identifies the primary records needed to resolve them; it adds no adjudication.

Capture: the direct shell endpoint returned a 403/Cloudflare response, which is preserved with headers. The article body remains represented by the browser-readable source and its cited lines, not by a falsely claimed local full-text capture.

# 2026-08-08 — SRC-268 media checkpoint: second reproducibility clip

The outstanding *Neurodivergent Show* caption-window work was advanced without changing claim status: a 37-second local derivative for approximately 05:20–05:57 was extracted and hashed. It remains a listening aid, not a verified transcript. A second attempt to extract the 06:08–07:12 window was killed by the local encoder process; the full MP4 and VTT remain canonical.

# 2026-08-08 — SRC-531/C-676: Avenging Angels Companies House state

Discovery: an official-registry search found a company-status record not represented by the existing personal-appointments snapshot.

Capture: preserved the Companies House overview and filing-history HTML and response headers under `assets/captures/2026-08-08-companies-house-avenging-angels/`.

Evidence handling: the overview states that Avenging Angels Ltd was dissolved on 22 July 2025; the filing history records Arday’s director and person-with-significant-control cessation on 18 March 2024. This resolves company-status topology only and does not support claims about company activity or finances.

# 2026-08-08 — SRC-530/C-675: BABAO Race Equality Review

Discovery: an exact-name professional-output search surfaced the British Association for Biological Anthropology and Osteoarchaeology’s May 2021 Race Equality Review.

Evidence: the browser-readable 25-page PDF names Jason Arday and Lizzy Craig-Atkins as authors and says Arday was commissioned to undertake the review, with Craig-Atkins and Rebecca Redfern supporting him. The report records its mixed-method consultation and organisational findings/recommendations.

Capture boundary: the repository’s direct download redirected to its home and returned a Cloudflare 403 challenge to the shell. The challenge HTML and headers are preserved; the PDF binary is not claimed as locally captured.

# 2026-08-08 — SRC-529/C-674: Acast RSS/audio version boundary

Discovery: the official Acast RSS feed for *How Do You Cope?* exposed the already-canonical 26 May 2025 Arday episode and its direct enclosure.

Capture: preserved the feed, headers, and Acast main MP3 under `assets/captures/2026-08-08-how-do-you-cope-jason-arday/`. The related bonus MP3 was byte-identical to SRC-220 and was not retained a second time.

Evidence handling: the Acast enclosure is materially shorter than the existing Global Player file (about 1:02:05 versus 1:11:49.51), while the feed reports 1:01:22. Both binaries remain source manifestations; the archive does not infer which is complete or edited.

# 2026-08-08 — SRC-528/C-673: Adult Literacy Trust supporters page

Discovery: the current charity site exposes a separate “Our Supporters” page not represented by the existing patron-announcement/governance record.

Capture: preserved the HTML, response headers, and the 225×225 portrait under `assets/captures/2026-08-08-adult-literacy-trust-supporters/`.

Evidence handling: the page publishes an attributed first-person statement about being unable to read or write until 18. It is direct evidence of what the charity published as his statement, not independent verification of the underlying childhood claim or of ongoing patron status.

# 2026-08-08 — SRC-527/C-672: Cambridge Research Integrity Report boundary

Discovery: an official Cambridge research-integrity search surfaced the current reports index and its 2024–25 annual report.

Capture: preserved the reports index HTML/headers, 12-page report PDF, extracted text, response headers, and a rendered copy of PDF p. 12 under `assets/captures/2026-08-08-cambridge-research-integrity/`.

Evidence handling: the report’s p. 12 table gives anonymized aggregate categories/results for investigations undertaken during 2023–24. It names no people and contains no Arday occurrence. This establishes a public-reporting boundary, not evidence about the separate 2026 Cambridge investigation, its scope, or its outcome.

# 2026-08-08 — SRC-526/C-671: Autism Research Centre Autistic VOICES study

Discovery: an exact-name institutional research-role search surfaced the Autism Research Centre’s Autistic VOICES project page.

Capture: preserved the page, response headers, project-plan PDF/text, student-advisory information PDF/text, consent form PDF/text, and visual renders under `assets/captures/2026-08-08-autistic-voices/` and `assets/documents/autistic-voices-study/`.

Evidence handling: the page’s March 2026 publication and June 2026 modification metadata list Professor Jason Arday on the Steering Committee. The project-level documents describe the co-design method, Cambridge ethics approval PRE.2026.047, £27.50/hour advisory compensation, planned 500–3,000-student survey, and expected 2027 results. These establish the project topology and public role listing, not Arday’s authorship, funding, PI status, or results.

# 2026-08-08 — SRC-524/C-669: Wonkhe pre-resignation staff profile

Discovery: an exact-name higher-education-media search surfaced Wonkhe’s dated staff profile for Jason Arday, credited to Jim Dickinson and structured as published 2 January 2026.

Capture: preserved the profile HTML, response headers, and 500×500 portrait under `assets/captures/2026-08-08-wonkhe-jason-arday/`.

Evidence handling: added SRC-524/C-669 as a dated professional-media source-version. It records present-tense Cambridge/Jesus and several patronage/advisory/trustee roles as Wonkhe’s pre-resignation wording, not current employment or legal findings. Reconcile it against later Cambridge, Companies House, charity, and host-page records.

# 2026-08-08 — SRC-525/C-670: PGIM Real Estate retrospective event corroboration

Discovery: a focused search for corporate and investor-sector diversity reports surfaced PGIM Real Estate’s *Real Estate Sustainability Annual Report 2025*.

Capture: preserved the 85-page PDF, response headers, layout text, and a rendered visual witness of PDF page 67 under `assets/documents/pgim-real-estate-stewardship-report-2025/` and `assets/captures/2026-08-08-pgim-report/`.

Evidence handling: the report’s “2024 Highlights of the European Inclusion & Leadership Network” section says PGIM hosted a London Black History Month fireside chat with Cambridge Professor Jason Arday on inclusion, stereotypes, and “reclaiming the narrative.” Added SRC-525/C-670 as retrospective event corroboration, not a new appearance node; exact date, recording, transcript, and detailed remarks remain open.

# 2026-08-08 — SRC-523/C-668: THE RAKE Japan lifestyle profile and photo essay

Discovery: an exact-name international-media search surfaced THE RAKE Japan’s February 2025 “Pocket Guide: Jason Arday,” a Japanese-language profile/interview credited to Tom Chamberlin with photography by Kim Lang.

Capture: preserved the public page, response headers, and six linked editorial JPEGs under `assets/captures/2026-08-08-rake-japan-jason-arday/`. The page’s structured metadata gives `datePublished` as 22 February 2025.

Evidence handling: added SRC-523 and C-668 as a distinct lifestyle/profile/photo-essay record. The attributed bespoke-style details are retained as self-report/profile material; repeated childhood, career, fundraising, torch, and marathon language is host copy and was not promoted as independent corroboration. Image rights and any English/print edition remain unresolved.

# 2026-08-08 — SRC-059/C-667: Cambridge Student Wayback revision audit

Discovery: the canonical Cambridge Student interview page says it was revised after discussion with Arday. A Wayback CDX query for the exact URL returned three successful digest-collapsed snapshots: 14 December 2023, 16 January 2024, and 27 December 2024.

Capture: the CDX JSON, response headers, three replayed HTML bodies, and three replay response-header files are preserved under `assets/captures/2026-08-08-cambridge-student-wayback/`.

Evidence handling: all three recovered replays contain the explicit revision notice and `dateModified` metadata of 4 December 2023. The earliest recovered snapshot is therefore already post-revision; no original pre-revision text was recovered. Upgraded SRC-059 and added C-667 without creating a duplicate interview entity.

# 2026-08-08 — SRC-522/C-666: *Booktime Magazine* memoir-interview lead

Discovery: a current-publication search surfaced The Harbour Bookshop’s product page for the free July–August 2026 issue of *Booktime Magazine*. Its description says the issue includes an interview with Jason Arday about his memoir on printed page 29.

Capture: preserved the product HTML, response headers, Shopify product JSON, JSON headers, and the 1056×1492 PNG cover under `assets/captures/2026-08-08-booktime-jason-arday/`. The product JSON dates the listing to 14 July 2026 and records a zero-price product.

Evidence handling: the title’s “FREE TO DOWNLOAD” wording did not correspond to a public PDF or page-29 file in the captured endpoint. Added SRC-522 and C-666 as a distinct trade-publication lead/source-version, without claiming the interview’s contents. Reopen only for the magazine PDF, page image, lawful mirror, or interview text.

Recheck: the Harbour Bookshop home page, product page, and Shopify `.js` product endpoint were fetched on 8 August 2026. The product is listed at zero price with `requires_shipping: true` and inventory 25; the JSON and rendered page expose only the cover image and no PDF, page-29 image, download URL, or interview body. This narrows the public access boundary but does not establish whether a file could be supplied after checkout or through a private channel. The new HTML/JSON/header captures are attached to SRC-522; no new claim about the interview was promoted.

# 2026-08-08 — SRC-521/C-665: UKRI Gateway identity-mismatch recheck

Discovery: public indexing continued to return the official UKRI Gateway result for Jason Arday and EDICa, while the canonical direct URL had previously rendered “Kevin Wilson.”

Capture: the URL was fetched again on 8 August 2026. It returned the same 37,246-byte HTML and the same visible Kevin Wilson heading; SHA-256 matches the 6–7 August body exactly. No Arday or EDICa content was exposed.

Evidence handling: added SRC-521 and C-665 as an access-state recheck linked to SRC-200/C-120. The indexed Arday/EDICa facts remain bounded to their indexed manifestation; the direct endpoint remains unable to confirm them. Reopen only for a changed official response, stable API/result route, or another first-party UKRI artifact.

# 2026-08-08 — SRC-520/C-664: Apple Podcasts manifestation of *Full Disclosure*

Discovery: an episode-catalogue search found Apple Podcasts’ UK page for the already-canonical 20 April 2023 *Full Disclosure with James O’Brien* interview. The page identifies season 2, episode 133, Global as producer, and a structured duration of 4,038 seconds.

Capture: preserved the Apple HTML and response headers. The page exposes a Captivate stream URL, but the episode’s audio is already locally preserved under SRC-034; no second MP3 was created.

Evidence handling: registered SRC-520/C-664 as a platform manifestation and updated `media.md` to map both routes to one audio entity. The Apple synopsis is host copy; it adds catalogue provenance, not an independent biographical source.

# 2026-08-08 — SRC-519/C-662–C-663: *The Bookseller* memoir preview

Discovery: a memoir-edition search surfaced *The Bookseller*’s public preview URL for *Great and Unfortunate Things*. Its indexed synopsis exposed Simon & Schuster Ltd, £20 price, 27 August 2026 date, ISBN `9781398542747`, and the familiar biographical framing.

Capture: the direct URL redirected to The Bookseller’s login page rather than exposing the preview body. The returned HTML and response headers are preserved under `assets/captures/2026-08-07-bookseller-memoir-preview/`; the indexed synopsis is retained only as a bounded public witness.

Evidence handling: registered SRC-519 and C-662–C-663 as a distinct trade-publication manifestation, deduplicated to the official Simon & Schuster edition records. Repeated childhood and Cambridge language is marketing copy about a self-authored memoir, not independent corroboration. Reopen only for a lawful preview body, changed public endpoint, or distinct edition/source version.

# 2026-08-07 — SRC-434 recheck and deduplication

A current institutional-process search rediscovered the already-canonical *Telegraph* lead. A second direct fetch returned the same HTTP 402/TollBit access boundary; the recapture is attached to SRC-434, not promoted to a duplicate source or claim.

# 2026-08-07 — SRC-518/C-660–C-661: official ASA and Gazette search boundary

Discovery: the adversarial credibility review reopened the MBE and advertising-regulator lead from SRC-517/C-659.

Capture: the exact-name ASA rulings query returned “Rulings (0).” The official Gazette Awards and Accreditations query returned a JSON result with `f:total: "0"` and no entries. HTML, headers, and JSON are preserved under `assets/captures/2026-08-07-official-record-searches/`.

Evidence handling: registered SRC-518 as an official search-state record. The result narrows the tested formal public databases but does not resolve private correspondence, informal offers, complaints, the cited CV, or the underlying podcast. It is not evidence that an MBE offer or advertising-related communication never existed.

Reopen only for a recovered primary artifact, a changed official search result, a named regulator response, or the underlying CV/podcast/correspondence.

# 2026-08-07 — SRC-512/C-637: Andrew Gelman statistical commentary

Discovery: a search for independent analysis of the distinction between the public textual-overlap allegations and the separate participant-evidence question surfaced Andrew Gelman’s 28 July 2026 *Future of Statistical Modeling* post.

Capture: preserved the full public HTML, response headers, and 1024×706 article image. The post discusses the reported duplicated participant quotation, the two journal corrections, the Cofnas/Harris materials, and Cambridge’s public response.

Evidence handling: registered Gelman as a distinct secondary statistical/commentary source. His framing that the central issue may be data fabrication is attributed, not adopted as a finding; the post itself says the decisive recordings, transcripts, consent forms, or institutional records are not publicly available in the captured source family.

Reopen only for primary participant records, a direct institutional finding, a correction/retraction, or a materially changed version of the commentary.

# 2026-08-07 — SRC-334/C-636: Warwick conference live-page 429 recheck

Discovery: a current-status check was made against Warwick’s Education Conference page and its post-event highlights route after earlier captures had established the event page and keynote video.

Capture: both routes returned the same 17-byte HTTP 429 `Too Many Requests` body from Warwick’s BigIP front end. Bodies and response headers are preserved under `assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/`.

Evidence handling: recorded the changed access state in SRC-334/C-636 without treating rate limiting as evidence of removal, cancellation, or non-delivery. The earlier accessible post-event HTML and 138,726,243-byte MP4 remain the durable artifacts.

Reopen only if a changed lawful endpoint, transcript/captions, or additional post-event artifact appears; do not repeat the same live fetch without a changed route or delivery state.

# 2026-08-07 — SRC-511/C-635: RCSL newsletter indexed lead and 404 boundary

Discovery: a conference-programme search surfaced an indexed extract from RCSL Newsletter 2 (2025) naming Jason Arday and Les Back among plenary speakers for the BSA Annual Conference 2026.

Capture: the linked IISJ PDF URL returned an HTTP 404 HTML response with no PDF bytes. The body and headers are preserved under `assets/captures/2025-rcsl-newsletter-2/`.

Evidence handling: registered SRC-511 as a distinct indexed publication lead, separate from existing BSA programme records. The indexed snippet is retained as a discovery witness only; no event delivery or substantive remarks are inferred.

Reopen only if the newsletter PDF, a stable page-level mirror, recording, transcript, or post-event report appears.

# 2026-08-07 — SRC-510/C-634: Black History Year mental-health event listing

Discovery: a search for distinct Arday public-event records surfaced Black History Month UK’s page for the Black History Year discussion “Mental Health in Black Men.”

Capture: preserved the event HTML, response headers, and 800×400 event image. The page records a 7 June 2021 online event with Arday and Damien Ridge and says recording would be limited to the speakers’ audio/video.

Evidence handling: registered SRC-510 as a separate event manifestation from the 27 March 2021 BlakPak conversation. No recording, transcript, slides, or attendance report was exposed, so the record remains scheduled-event evidence only.

Reopen only for the Eventbrite archive, a speaker-only recording, transcript, slides, or post-event report; do not infer delivery from the listing.

# 2026-08-07 — SRC-509/C-633: *Spiked* controversy commentary

Discovery: an exact-name controversy search surfaced Joanna Williams’s *Spiked* column, “Woke privilege still reigns at Cambridge University,” published 27 July 2026 and modified 30 July.

Capture: preserved the public article HTML, response headers, and credited 1536×864 image.

Evidence handling: registered SRC-509 as a distinct opinion-journalism/source-propagation witness. It repeats known allegations and institutional-response framing but adds no primary-text audit, new sports record, institutional report, or adjudication. The article’s evaluative language is retained as commentary, not converted into claims about misconduct or biography.

Reopen only for a correction, materially changed article version, cited primary document, or independent adjudicative record; do not count the repeated allegations as new corroboration.

# 2026-08-07 — SRC-306/C-632: African Allied Health Summit changed access state

Discovery: the live speaker page appeared in search with fuller keynote copy, so the previously captured summit routes were checked again rather than treating the index result as a new source.

Capture: the home, speakers, and schedule URLs all returned the same 6,192-byte HTTP 403 browser-verification challenge. The bodies and response headers are preserved under `assets/captures/2026-08-07-aahn-jason-arday/recheck-2026-08-07b/`.

Evidence handling: updated SRC-306 in place and added C-632 as a changed access-state claim. The earlier 200-page capture remains the controlling historical manifestation for the keynote listing; the later 403 does not establish delivery, cancellation, or non-occurrence.

Reopen only for a real post-event report, final agenda, recording/transcript, or changed lawful site endpoint; do not treat search snippets as recovered event evidence.

# 2026-08-07 — SRC-508/C-630–C-631: The Times Bookshop UK memoir manifestation

Discovery: a fresh memoir-edition search surfaced The Times Bookshop’s public UK hardback record for ISBN `9781398542747`.

Capture: preserved the 694,870-byte product HTML, response headers, and 420×640 retailer cover image. The page lists Simon & Schuster Ltd, 336 pages, 27 August 2026, and a £20 price at capture.

Evidence handling: registered SRC-508 as a distinct retailer manifestation deduplicated to the publisher/Google Books UK edition family. The page’s current-tense Cambridge biography was captured after Arday’s resignation and is explicitly classified as stale promotional copy; it is not used as current-status evidence.

Reopen only for a changed product page, a materially different edition record, or a rights-cleared media asset; do not count retailer metadata as independent corroboration of the memoir’s biography.

# 2026-08-07 — SRC-507/C-629: Reading Blue Coat magazine source-version

Discovery: a PDF-focused search found a first-party Reading Blue Coat School magazine result whose indexed extract names the school’s 2025 Equality and Inclusion Day welcome for Professor Jason Arday FRSA and points to page 21.

Capture: the linked PDF URL returned HTTP 404 from the school host. The HTML response and headers are preserved; no magazine binary or page image was recovered. The school’s separate event report and photographs remain the controlling event record.

Evidence handling: registered SRC-507 as a distinct school-publication manifestation deduplicated to SRC-233, and added only C-629 for the indexed page-level witness. Repeated biography wording is not treated as independent corroboration.

Reopen only if the magazine PDF, page 21 image, or a stable school archive route reappears; do not infer the missing page’s full content from the search snippet.

# 2026-08-07 — SRC-129/C-628: Spotify catalogue manifestation

Discovery: a fresh podcast search surfaced Spotify’s public page for the 26 May 2025 *How Do You Cope?* episode, which was already canonicalized through Global Player, Apple, Acast, and Tapesearch.

Capture: preserved Spotify’s 243,850-byte HTML page and response headers. The page identifies the same title, show, release date, displayed 1-hour-2-minute duration, and host description.

Evidence handling: updated SRC-129 in place and added C-628 as a catalogue/source-version claim. No duplicate interview, new substantive biography, or independent corroboration was created.

Reopen only for a changed Spotify page, public transcript, or distinct audio manifestation; do not count the Spotify item as a separate appearance.

# 2026-08-07 — SRC-276/C-627: RSC report-PDF access recheck

Discovery: a first-party RSC publication search exposed a direct PDF URL for the already-canonical Inclusion and Diversity Forum 2025 report.

Capture: the URL redirected to the RSC news route and then returned an HTTP 429 PALSS response. The 185-byte HTML body and response headers are preserved; no PDF bytes were recovered.

Evidence handling: updated SRC-276 in place and added only C-627 as an access-state observation. The existing RSC HTML report and official YouTube recording remain canonical; no duplicate report version or presentation-content claim was created.

Reopen only after a changed report-PDF endpoint or a lawful downloadable report; do not treat the 429 response as evidence that the report is absent.

# 2026-08-07 — SRC-211/C-626: Durham chapter-index direct recheck

Discovery: a bounded fresh web search again surfaced the existing Durham indexed result for “Decolonising higher learning education in the UK,” alongside no distinct publisher, DOI, ISBN, library, or lawful full-text manifestation.

Capture: fetched the person-page result at `outputs?page=3` directly. The response was a 5,578-byte Cloudflare challenge, with no indexed result body or chapter metadata; HTML and response headers are locally preserved.

Evidence handling: updated SRC-211 in place and added only C-626 as a retrieval-state observation. The Springer/Information Age/La Découverte conflict remains unresolved; no publication record or chapter content was created or inferred.

Reopen only for a changed Durham response or a distinct publisher/library/DOI/archival record; do not repeat the same exact-title and endpoint searches without a changed state.

# 2026-08-07 — SRC-200/C-625: UKRI Gateway identity-boundary recheck

Discovery: the explicit NEXT item called for a recheck only to test whether the official Gateway endpoint had changed.

Capture: fetched the canonical person URL on 7 August 2026 and preserved the HTML and response headers. The response again displayed “Kevin Wilson,” contained no visible `Jason Arday` or `EDICa` text, and was byte-identical to the 6 August HTML capture.

Evidence handling: updated SRC-200 in place and added only the narrow access/state observation C-625. The indexed EDICa facts remain C-120 and remain attributed to the official indexed result; no duplicate source or project claim was created.

Reopen only after a changed Gateway response or a distinct official UKRI project/person record; do not repeat the same endpoint fetch without a state change.

# 2026-08-07 — SRC-506/C-621–C-624: NIHR Be Part of Research CoPICS trial page

Discovery: a participant-facing NIHR search result surfaced the CoPICS trial page with a distinct trial identifier (`25714`), separate from the BMJ protocol and the ARC publication record.

Capture: preserved the live HTML and response headers. The page displayed “Recruiting,” 15 April 2024–30 September 2026 recruitment dates, five UK sites, participant-facing study and eligibility text, and University of Oxford/NIHR NETSCC sponsor-funder wording.

Evidence handling: registered SRC-506 as a project-context record. The page does not name Arday; its methods, sites, dates, and sponsor/funder facts are not used as evidence of his individual contribution, project delivery, or completed findings. It is linked indirectly to SRC-171/SRC-505/SRC-397.

Reopen only for a changed NIHR trial state, a final results/publication record, or a direct project document naming Arday’s role; do not repeat the same trial-page fetch without a state change.


# 2026-08-07 — SRC-505/C-618–C-620: NIHR ARC CoPICS publication manifestation

Discovery: a focused institutional-output search found the NIHR Applied Research Collaboration Oxford and Thames Valley record for the already-canonical CoPICS study protocol. The page was not represented as a separate funder/institutional manifestation in the registry.

Capture: preserved the page HTML and response headers. The plural discovery URL redirected to the singular publication route; the final page lists Arday among the authors, the DOI/date/volume, NIHR study number 151887, the protocol abstract, ethics identifiers, and planned dissemination.

Evidence handling: registered SRC-505 as a distinct first-party source-version deduplicated to SRC-171. Its methods and ethics statements are recorded as bounded protocol/abstract wording; no duplicate PDF, completed study finding, or claim about Arday’s individual contribution was added.

Reopen only for a changed institutional page, a distinct funder/project record, or a completed CoPICS output; do not repeat the same DOI publication search.


# 2026-08-07 — SRC-504/C-616–C-617: earlier Simon & Schuster memoir proposal catalogue

Discovery: a focused memoir-rights search surfaced the distinct `SS_2025_Spring.pdf` catalogue, created in February 2025 and carrying a May 2026 catalogue label. The previously captured Spring 2026 rights catalogue did not contain this earlier proposal version.

Capture: preserved the 78-page PDF, extracted text, response headers, and PDF p. 74 render. The entry gives a projected 320-page length, S&S UK co-publication, Ben Clark at the SoHo Agency and Jennifer Gates at Aevitas as agents, and the phrase “Proposal available.”

Evidence handling: registered SRC-504 as a source-version rather than a new memoir or independent biography. The synopsis and “over half a million emails” statement are catalogue/promotional claims. Page-count, agent, and proposal-state differences are retained as publishing history and not silently reconciled with later editions or the final memoir.

Reopen only for a materially different proposal/version, direct agent or publisher documentation, or a primary record supporting the audience-count claim; do not repeat the later Spring 2026 catalogue fetch.

# 2026-08-07 — SRC-281 recheck: House of Lords Youth Unemployment Committee evidence

Discovery: a fresh parliamentary-output search surfaced the official corrected transcript for the 29 June 2021 Youth Unemployment Committee session, Evidence Session 19, Questions 195–207.

Capture: the official browser-rendered transcript exposed the 20-page corrected text, witness list, date, and Arday’s role introduction. Direct shell requests to the official HTML, PDF, and older Publications Parliament routes returned Cloudflare HTTP 403 challenge pages; those responses and headers are preserved locally, while no transcript binary is claimed.

Evidence handling: updated the existing canonical SRC-281 record in place; no duplicate source or claims were created. The transcript is a strong dated public-role and testimony record. Role descriptions are page-state evidence as of the hearing; the speaker’s statistics and policy arguments remain attributed testimony, not silently upgraded to independent verification.

Reopen only if the official route exposes a downloadable transcript/PDF or a distinct recording, corrections, or related committee artifact.

# 2026-08-07 — SRC-503/C-615: Durham *Whiteness and Education* repository recheck

Discovery: the indexed Durham Worktribe item remains the principal lawful-retrieval lead for Arday’s 2018/2019 *Whiteness and Education* article, whose primary text is needed to audit the preserved Cofnas/Rollock comparison.

Capture: the exact repository item URL returned HTTP 403 and a 6,154-byte Cloudflare “Just a moment…” challenge. The challenge HTML and response headers are preserved under `assets/captures/2026-08-07-durham-whiteness-recheck/`; no article bytes were recovered.

Decision: register SRC-503/C-615 as a changed access-state boundary linked to canonical SRC-043 and prior Durham manifestations. Do not treat this failed retrieval as evidence about the article’s content, plagiarism, intent, or institutional outcome, and do not repeat the same endpoint without a changed state.

# 2026-08-08 — SRC-491: Jack Petchey Speak Out Challenge panelist profile

Discovery: a fresh 2025 biography/event search surfaced the Jack Petchey Speak Out Challenge’s 1 July 2025 profile for its Grand Final judging panel.

Capture: preserved the first-party HTML page and response headers. The page names Jason Arday as a judge and gives the event date and venue, but exposes no recording, transcript, judging result, or downloadable event media.

Evidence handling: added SRC-491/C-594–C-595 as a distinct organizer source-version. The panel role is kept as a dated event record; the repeated speech/literacy and research-interest wording is not counted as independent corroboration and is not merged into the core childhood claims.

Reopen only if the organizer publishes a post-event report, recording, transcript, result, or materially changed page.

# 2026-08-08 — SRC-492: *We See Things They’ll Never See* chapter-level manifestation

Discovery: a fresh DOI/title scholarly-output search surfaced De Gruyter Brill’s chapter record for “I’ll See You on the Dark Side of the Moon: Mental Health and Illness and the Consequences of Neurotypical Hegemony.”

Capture: the publisher URL returned an HTTP 202 Amazon WAF challenge with a zero-byte body. Crossref’s DOI API returned structured metadata, including the title, chapter span 76–101, 2025 date, and an `is-identical-to` relation to DOI `10.2307/jj.26932075.9`; JSON and headers are preserved.

Evidence handling: added SRC-492/C-596–C-597 as a chapter-level manifestation deduplicated to the canonical Lewis/Arday book record SRC-053. The record verifies bibliographic identity and co-authorship only; no chapter text, claims, or substantive argument is extracted from the access-challenged page.

Reopen only if the publisher, JSTOR, or another lawful repository exposes the chapter text or a changed metadata state.

# 2026-08-08 — SRC-494–SRC-495: *We See Things They’ll Never See* chapters 1–2

Discovery: DOI-family enumeration against Crossref exposed identifiers missed by ordinary title search: `10.1515/9780691263946-005` and `10.1515/9780691263946-006`.

Capture: Crossref JSON and headers were preserved for both records. Both publisher chapter endpoints returned HTTP 202 Amazon WAF challenges with zero-byte bodies. Crossref reports chapter 1 “Sowing the Seeds of Love,” pp. 1–41, and chapter 2 “What’s Love Got to Do with It? A Framework of Love to Dismantle Neurotypical Hegemony,” pp. 42–75.

Evidence handling: added SRC-494/C-600 and SRC-495/C-601, plus the shared access-state boundary C-602. Both are chapter manifestations deduplicated to SRC-053; no substantive chapter claims are extracted and Crossref’s missing author arrays are not overinterpreted.

Remaining DOI-family enumeration: chapters 4–6 (`-008`, `-009`, `-010`) and the afterword (`-012`) remain to be captured or logged as unavailable; do not repeat the 005/006 calls without a changed endpoint.

# 2026-08-08 — SRC-496–SRC-499: *We See Things They’ll Never See* chapters 4–6 and afterword

Discovery: the remaining DOI-family identifiers were enumerated through Crossref: `10.1515/9780691263946-008`, `-009`, `-010`, and `-012`.

Capture: Crossref JSON and headers were preserved for all four records. Each publisher endpoint returned HTTP 202 with an Amazon WAF challenge and a zero-byte body. The records identify chapter 4 “The Great Beyond” (pp. 102–129), chapter 5 “A Design for Life” (pp. 130–157), chapter 6 “Everything Is Everything” (pp. 158–184), and the afterword (pp. 207–214).

Evidence handling: added SRC-496–SRC-499/C-603–C-607. All four are component manifestations deduplicated to SRC-053; no substantive chapter or afterword claims are extracted.

The currently enumerated DOI family is now complete for the book components represented by Crossref (`-005` through `-012`, with `-003` separately represented by the foreword record). Reopen only for changed metadata, lawful text access, or a new edition/manifestation.

# 2026-08-08 — SRC-313 changed-state PDF recheck

Discovery: the Taylor & Francis review’s indexed PDF result continued to expose full review text in search, so the previously recorded 6 August publisher access boundary was tested again.

Capture: the direct `/doi/pdf/10.1080/00071005.2026.2620963` request returned HTTP 403 Cloudflare challenge HTML (5,542 bytes), not a PDF. Body and headers are preserved under `assets/captures/2026-08-08-tandf-we-see-review-recheck/`.

Decision: upgrade SRC-313/C-608 in place. The accepted manuscript under SRC-287 remains the locally available full text; the indexed publisher text is not silently represented as a recovered local publisher file.

# 2026-08-08 — SRC-492 related-DOI resolution boundary

Discovery: SRC-492’s Crossref record supplied an `is-identical-to` relation to DOI `10.2307/jj.26932075.9`, suggesting a possible JSTOR/content-platform manifestation of chapter 3.

Capture: resolving that DOI locally followed Crossref’s chooser/content-access flow. The response chain ended in Crossref chooser HTML; no JSTOR chapter page, PDF, or text was exposed. The body and headers are preserved under `assets/documents/research-integrity/degruyter-chapter3-jstor/`.

Decision: add C-609 to SRC-492’s access topology. Keep the relation as metadata only and do not represent it as recovered JSTOR text or verified byte identity.

# 2026-08-08 — SRC-493: *We See Things They’ll Never See* chapter 7 manifestation

Discovery: the DOI-family search for the Lewis/Arday book surfaced De Gruyter Brill’s indexed record for chapter 7, “For Tomorrow: A Manifesto for Dismantling Neurotypical Hegemony.”

Capture: the publisher URL returned an HTTP 202 Amazon WAF challenge with a zero-byte body. Crossref’s DOI API returned the title, 2025 publication date, and pp. 185–206; JSON and headers are preserved.

Evidence handling: added SRC-493/C-598–C-599 as a distinct chapter-level manifestation deduplicated to SRC-053. Publisher-indexed authorship is recorded, while Crossref’s missing author array is preserved as a metadata limitation. No substantive chapter claim is extracted.

Reopen only if the publisher, JSTOR, or another lawful repository exposes the chapter text or a changed metadata state.

# 2026-08-07 — Aderibigbe (2013) ResearchGate manifestation
Discovery: the exact 2013 Aderibigbe DOI surfaced as a ResearchGate indexed page with article metadata, abstract, and a request-full-text state.
Capture: direct shell retrieval returned HTTP 403; the response HTML and headers are preserved. The indexed page says a copy can be requested from the author and exposes no article body or PDF.
Evidence handling: added SRC-452/C-516 as a distinct host manifestation linked to canonical SRC-388. It strengthens the comparator provenance boundary without creating a duplicate publication or upgrading the 2014 open-article comparison into a 2013 full-text finding.

# 2026-08-07 — COXA historical teamsheet archive check
Discovery: a search result surfaced the Clapham Old Xaverian Archive’s 2005–06 football teamsheets PDF as a possible historical sports record.
Capture: downloaded the 20-page PDF and extracted its text. Exact searches for `Arday` and `Jason Arday` returned no matches; unrelated names including Jason Marquis were present.
Evidence handling: added SRC-451/C-515 as a bounded negative-space record. It does not disprove Arday’s sports account or replace the positive 2015 COXA match report; reopen only for a concrete 2014–2016 teamsheet, roster, match report, or registration record.

# 2026-08-07 — CORE/OpenAIRE/Semantic Scholar retrieval boundary
Discovery: a new exact DOI query family was run against CORE, OpenAIRE, and Semantic Scholar for Arday’s *Whiteness and Education* article.
Result: CORE returned one exact Durham Research Online result but no download URL or full-text identifier; OpenAIRE returned DOI-only publisher/unknown-repository instances; Semantic Scholar returned HTTP 429.
Evidence handling: added SRC-450/C-514 as a distinct index/API boundary linked to SRC-043 and SRC-449. No article text was recovered and no absence claim was made; reopen only with a changed index result or a concrete lawful file URL.

# 2026-08-07 — OpenAlex/Durham repository manifestation for *Whiteness and Education*
Discovery: OpenAlex’s DOI work record identifies a Durham Research Online location, classifies the work as green open access, and reports a CC-BY submitted-version location with `any_repository_has_fulltext: true`, but supplies no PDF URL.
Capture: preserved the OpenAlex JSON/headers and the Durham page response. The Durham output page, two plausible OAI-PMH `GetRecord` routes, and the direct `OutputFile/1286002` route returned Cloudflare challenge HTML rather than metadata or an article file.
Evidence handling: added SRC-449/C-513 as a distinct repository/index manifestation of canonical SRC-043. The index’s availability assertion is retained as attributed metadata; no manuscript or full article is claimed locally, and the Cofnas/Rollock comparison remains unresolved on the Arday side.

# 2026-08-07 — Rollock comparator full-text manifestation
Discovery: the public/indexed ResearchGate page for Nicola Rollock’s “Unspoken rules of engagement” exposes the DOI, volume/pages, author-upload attribution, and article text corresponding to the three Rollock excerpts in Cofnas’s comparison image.
Capture boundary: the direct shell endpoint returned HTTP 403 on this pass, so no PDF is claimed locally. The existing ResearchGate access-state capture remains the local boundary artifact.
Evidence handling: added SRC-448/C-512 as a distinct comparator manifestation linked to SRC-424. This strengthens the Rollock-side text trail without treating it as an Arday full-text recovery, plagiarism adjudication, or resolution of intent/citation context.

# 2026-08-07 — REF/ERIC primary-side metadata recovery for *Whiteness and Education*
Discovery: the official REF 2021 output record and ERIC record EJ1365833 surfaced during the Cofnas comparison audit.
Capture: preserved both HTML pages and response headers. REF records Durham output 125762, DOI `10.1080/23793406.2019.1574211`, journal/pages, and “Technical exception” open-access status; ERIC records the 2018 journal metadata, peer-review marker, 21-page extent, and supplied abstract.
Evidence handling: added SRC-446/C-510 and SRC-447/C-511 as distinct metadata manifestations of canonical SRC-043. Neither exposes the article text or resolves the displayed Arday/Rollock comparison; the full-text and intent boundaries remain open.

# 2026-08-07 — Current institutional/scholarly/media discovery boundary
Search: ran focused queries for `Jason Arday 2026 publication interview event`, current profiles, `site:ac.uk` 2026 records, DOI results, 2026 podcasts/interviews/recordings, and YouTube uploads.
Result: no new canonical source was found. Results resolved to the already preserved AP resignation/investigation report, Cambridge profile and changed-page records, the SEB “Things Can Only Get Better” unavailable-video lead, the BSA Annual Conference 2026 programme/abstract book, existing memoir catalogue records, and low-provenance or stale profile pages. The Class Central SEB result is a duplicate manifestation already reconciled under SRC-109; no new video ID or binary was recovered.
Boundary: preserve this query family as exhausted for the current index state. Reopen only for a new title/DOI/video ID, a first-party post-event artifact, a changed institutional page, or a non-duplicate publisher/repository record.

# 2026-08-07 — Integrity-queue checkpoint reconciliation
The existing comparative-audit records SRC-406, SRC-407, and SRC-408 already contain the direct page-level checks for Arday pp. 61–66 against the corresponding Zwozdiak-Myers thesis ranges. Corrected stale unchecked items in `NEXT.md`; no new comparison or claim was created, and the remaining page ranges remain separately bounded.

# 2026-08-07 — Date-bounded 2025–2026 video search boundary
Search: ran focused web searches for `Jason Arday interview video` and `Jason Arday 2026 interview video`, then compared the returned candidates against the source registry and media index.
Result: the Arday results were already canonical (*How Do You Cope?*, the 2025 *Allyship in Action* episode, Cambridge neurodiversity material, and older event listings), duplicate manifestations, or access-boundary pages. Unrelated names and commentary were not promoted. No new video ID, recording, transcript, or changed endpoint was found.
Boundary: do not repeat this exact query pair without a new title, ID, host page, or changed media state; retain the existing host-by-host access boundaries and manual-verification queue.

# 2026-08-07 — ResearchGate manifestation of existing RHHJ interview
Discovery: the changed ResearchGate author index surfaced “Um professor negro em Cambridge: Entrevista com Jason Arday,” a public manifestation of the already canonical *Revista História Hoje* interview (DOI `10.20949/rhhj.v13i29.1268`).
Evidence handling: added the ResearchGate URL as an alias to SRC-216 and the media index. The journal-hosted PDF remains the canonical local artifact; no duplicate source or independent corroboration claim was created.

# 2026-08-07 — Research Cast UK C-117–C-119 listening-clip preservation
Capture: extracted three short MP3 clips from the canonical 44:47.54 Research Cast UK recording around the existing ASR windows: 05:35–06:40 (educator/Bob and education-values passage), 26:50–27:25 (family/NHS mental-health passage), and 27:48–29:45 (sport, community, and belonging passage).
Evidence handling: the canonical full MP3 and Whisper ASR remain authoritative archive inputs. The clips make future manual listening and handoff reproducible, but no claim was upgraded to a human-verified transcript; names, wording, and family details remain subject to direct listening.

# 2026-08-07 — SRC-359/C-509 ResearchGate changed-index recheck
Discovery: a fresh public rendering of the existing ResearchGate Jason Arday output index changed from the preserved “Publications (33)” state to “Publications (34)” and displayed 1,514 citations.
Evidence handling: the page remains an automatically generated, low-provenance discovery index. No new title or DOI was promoted, and the count was not treated as a verified bibliography or citation total. The prior HTML/headers remain the local capture; the direct shell endpoint still presents an HTTP 403/Cloudflare boundary, while the current rendering is retained as a linked source-version observation.

# 2026-08-08 — SRC-444/C-507–C-508 Arasite Boud-framework opening audit
Discovery: rows 44–45 of the preserved `ARDAY FINAL GRID.docx` were identified as a distinct unmapped comparison of Arday printed p. 66 against Zwozdiak-Myers printed pp. 49–50 (PDF pp. 60–61).
Capture: rendered and checksummed Arday PDF p. 66 and Zwozdiak-Myers PDF pp. 60–61 locally. Direct comparison confirms the same Boud four-stage list and immediate look-back/look-forward transition, with compression and wording edits in Arday.
Evidence handling: recorded this as a bounded page-level observation. Adjacent SRC-408 and SRC-409 audits are not re-counted; the record does not determine provenance, intent, applicable standards, or an institutional finding.

# 2026-08-08 — SRC-443/C-506 21percent controversy propagation witness
Discovery: a distinct 21percent.org page, “Sadness and Horror,” was found through the current controversy search. It links the public Arasite dossier and reporting, reproduces a Cremin/Harris correspondence excerpt, and discusses the reported institutional response.
Capture: preserved the page HTML and response headers. The page also contains extensive reader comments, which remain in the local HTML but were not promoted into the claims ledger.
Evidence handling: recorded it as low-provenance commentary and a source-propagation witness. The page’s assertions about a 97-page submission, Cambridge handling, and investigation remain attributed and unresolved; underlying primary and reputable sources are not replaced.

# 2026-08-08 — SRC-442/C-505 UNSW Press catalogue manifestation
Discovery: the February 2026 UNSW Press catalogue surfaced a regional trade manifestation of Lewis and Arday’s *We See Things They’ll Never See* not previously represented by ISBN.
Capture: preserved the 55-page catalogue PDF, response headers, and rendered page 29. The entry lists Haymarket Books, paperback format, 304 pages, ISBN 9798888904503, February 2026, and AU/NZ pricing.
Evidence handling: deduplicated to SRC-039 as an alternate edition and kept the catalogue description separate from independent review or biographical evidence.

# 2026-08-08 — SRC-441/C-504 Taylor & Francis football-chapter manifestation
Discovery: a direct Taylor & Francis chapter page surfaced for Arday’s football chapter, distinct from the DOI/PagePlace catalogue record already represented as SRC-026.
Capture: the publisher page confirms title, author, publisher date 8 February 2023, and printed pages 165–173. The advertised PDF/XML endpoints were tested; both redirected to the landing page and returned HTML rather than chapter files.
Evidence handling: added publisher provenance and retained the access boundary without creating a duplicate publication or claiming access to the chapter text. The publisher date is preserved alongside, not substituted for, existing catalogue dates.

# 2026-08-08 — SRC-440/C-503 Cambridge Repository author-search boundary
Discovery: the Cambridge Repository Discover API search for `Arday` returned 29 textual hits. Item-level metadata inspection found exactly four records with Arday in the author field.
Reconciliation: the four records are the already-canonical correction, CoPICS protocol, women-academics article, and under-represented-young-people protocol. The remaining 25 hits were not promoted because they were textual mentions or unrelated matches.
Capture: preserved the complete JSON response and headers. This closes the exact query as a bounded repository-discovery pass while leaving changed API results, alternate author queries, and future repository additions open.

# 2026-08-08 — SRC-439/C-502 Cambridge Repository manifestation
Discovery: Cambridge’s institutional repository surfaced a distinct item page for the 2025 BMJ Open narrative-inquiry protocol already catalogued as SRC-172.
Capture: preserved the item HTML, response headers, and downloadable article PDF with SHA-256 checksums. The page exposes the handle, DOI metadata, author list, and repository bitstream links.
Evidence handling: deduplicated by DOI/title; this is institutional repository provenance and a local access copy, not a new publication node or an independent biography claim. A transient first request returned 404 before the successful capture; the failed state was not used as evidence.

# 2026-08-08 — SRC-438/C-501 Glasgow Enlighten author-index capture
Discovery: a new institutional repository author page for “Arday, Jason” was found at Glasgow Enlighten. It lists four 2022 outputs with DOI metadata.
Reconciliation: all four DOI/title keys already map to canonical source records for the same publications; no duplicate output nodes were created. The capture adds Glasgow repository provenance and direct item links.
Capture: the author-index HTML and response headers are preserved locally. The page is a bibliographic index, not a full-text or authorship adjudication record.

# 2026-08-08 — SRC-436/C-499 and SRC-437/C-500 reader-review manifestations
Discovery: a changed memoir-reception sweep found distinct StoryGraph and Foyles review pages not represented in the registry. StoryGraph exposes an ARC reviewer’s positive response; Foyles exposes two positive reader reviews for the UK hardcover, one identifying a Waterstones review copy.
Capture: both direct endpoints returned Cloudflare challenge pages; those HTML responses and headers are preserved. The review text is recorded only from public search/index manifestations, not as full local copies.
Evidence handling: these are low-provenance reader-reception and ARC-witness records. They do not independently corroborate the memoir’s biography and remain separate from publisher copy, trade reviews, *The Times*, and *The Atlantic*.

# 2026-08-08 — SRC-435/C-498 *Times* memoir review
Discovery: the open memoir queue produced a distinct 6 August 2026 *Times* review by Sarah Ditum, separate from the publisher page and the *Publishers Weekly* trade review.
Capture: the public teaser and structured metadata expose the headline, reviewer, publication/modification dates, and standfirst; the full article is subscription-gated. The HTML and response headers are preserved locally, and a Reddit post is retained only as a propagation witness.
Evidence handling: recorded the visible language as reviewer judgment and dated critical reception, not as fact-checking or an institutional finding. Do not infer the review’s inaccessible arguments or conclusions; revisit only if the full text becomes lawfully accessible or a separately published excerpt/review appears.

# 2026-08-08 — SRC-434/C-497 Cambridge hiring-process review report
Discovery: a distinct 7 August *Telegraph* article was located by exact headline and direct URL. It reports that Cambridge’s Arday investigation would feed into a review of the process for appointing senior academic roles and would continue examining the circumstances around his appointment and tenure.
Capture: the canonical article URL returned HTTP 402 with a TollBit authorization boundary; the returned HTML and response headers were preserved. A Reddit repost preserves the article title, canonical link, and quoted wording.
Evidence handling: recorded as a reputable-news report and propagation witness, not as a Cambridge primary statement. The review’s scope, methodology, findings, and completion remain unresolved; revisit only if Cambridge publishes a direct statement or review document, or the article becomes directly accessible.

# 2026-08-08 — Archive integrity audit refresh
Re-ran the read-only structural checks after adding SRC-433/C-496. All 409 backticked source-registry paths resolve; 408 source Markdown records carry in-file `SRC-*` identifiers; all 474 claim IDs are unique; no source IDs are duplicated; and 3,576 local Markdown links have no missing targets. The refreshed audit remains structural, not substantive.

# 2026-08-08 — Bounded media-discovery sweep / no new canonical source
Searched exact-name combinations for interviews, podcasts, video profiles, transcripts, and 2025–26 events. The CBS video, New Humanist *With Reason* transcript, Ruling Passions episode, *How Do You Cope?* transcript index, Talking Matters episode, Spotify listing, and Cambridge Neurodiversity film all resolve to existing canonical records in `media.md` and `source-registry.md`. No distinct source, binary, transcript, or changed access state was promoted; repeating these exact searches is not an open action unless a host state changes.

# 2026-08-08 — SRC-433/C-496 Cambridge 2024 Proposed Roll
Discovery: a bounded current-source sweep surfaced Cambridge’s official *University Reporter* Special No. 1, dated 1 October 2024, which was not previously represented in the archive.
Capture: downloaded the 92-page PDF and response headers; rendered PDF page 8 / printed page 9, where the Proposed Roll lists “Arday, Jason Atta Kwei, JE.”
Evidence handling: recorded this as a dated first-party Regent House membership record, distinct from the 2025 proposed/promulgated rolls and from post-resignation status. It does not establish teaching, research activity, qualification validity, or continued membership.

# 2026-08-08 — Source front-matter normalization batch 7

Added `id:` front matter to the final thirteen legacy source notes: SRC-264, SRC-053, SRC-424, SRC-139, SRC-166, SRC-032, SRC-267, SRC-134, SRC-039, SRC-162, SRC-026, SRC-140, and SRC-157. The source bodies and registry mappings were preserved. The in-file source-ID normalization backlog is now zero.

# 2026-08-08 — Source front-matter normalization batch 6

Added `id:` front matter to ten further legacy source notes: SRC-164, SRC-163, SRC-265, SRC-160, SRC-378, SRC-260, SRC-259, SRC-165, SRC-261, and SRC-167. The source bodies and registry mappings were preserved. Thirteen legacy notes remain for later bounded batches.

# 2026-08-08 — Source front-matter normalization batch 5

Added `id:` front matter to ten further legacy source notes: SRC-033, SRC-034, SRC-270, SRC-136, SRC-266, SRC-023, SRC-137, SRC-156, SRC-138, and SRC-135. The source bodies and registry mappings were preserved. Twenty-three legacy notes remain for later bounded batches.

# 2026-08-08 — Source front-matter normalization batch 4

Added `id:` front matter to ten further legacy source notes: SRC-158, SRC-041, SRC-025, SRC-052, SRC-051, SRC-050, SRC-040, SRC-268, SRC-159, and SRC-275. The source bodies and registry mappings were preserved. Thirty-three legacy notes remain for later bounded batches.

# 2026-08-08 — Source front-matter normalization batch 3

Added `id:` front matter to ten further legacy source notes: SRC-046, SRC-031, SRC-036, SRC-161, SRC-141, SRC-029, SRC-038, SRC-049, SRC-048, and SRC-024. The source bodies and registry mappings were preserved. Forty-three legacy notes remain for later bounded batches.

# 2026-08-08 — Source front-matter normalization batch 2

Added `id:` front matter to ten further legacy source notes: SRC-027, SRC-042, SRC-043, SRC-271, SRC-035, SRC-269, SRC-045, SRC-030, SRC-044, and SRC-047. The source bodies and registry mappings were preserved. Fifty-three legacy notes remain for later bounded batches.

# 2026-08-08 — Source front-matter normalization batch 1

Added `id:` front matter to ten legacy source notes whose canonical IDs were already present in `source-registry.md`: SRC-392, SRC-393, SRC-391, SRC-377, SRC-133, SRC-390, SRC-028, SRC-022, SRC-272, and SRC-037. The source bodies and registry mappings were preserved. Sixty-three legacy notes remain for later bounded batches.

# 2026-08-08 — Archive integrity audit

Ran a read-only repository integrity pass. All 422 source-registry paths resolve; all 334 ID-bearing source files are represented in the registry; all 473 claim IDs are unique; no duplicate source IDs were found; and no broken relative Markdown links were found. The audit is preserved at [archive-integrity-audit-2026-08-08](assets/metadata/archive-integrity-audit-2026-08-08.md). These results verify structure, not external-source availability or substantive completeness.

# 2026-08-08 — SRC-426/C-485–C-486 Arasite student-teachers comparison
Discovery: the supplied side-by-side exhibit identified an unmapped comparison block labeled Arday p. 17 and Zwozdiak-Myers printed p. 1.
Capture: checked the underlying PDFs directly and rendered Arday PDF page 17 and Zwozdiak-Myers PDF page 12 / printed p. 1. Preserved the supplied comparison image as a provenance exhibit.
Evidence handling: recorded the close ordered correspondence and the material wording changes separately. The exhibit’s “verbatim copying” note is retained as source-attributed characterization, not an institutional finding or an unqualified archive conclusion.

# 2026-08-08 — SRC-425/C-483–C-484 Cambridge Reporter appointment record
Discovery: a current exact-name search surfaced Cambridge University Reporter No 6680, a 15 December 2022 official PDF not previously represented in the archive.
Capture: downloaded the 14-page PDF and response headers. The relevant notice is printed p. 213 / PDF page 9.
Evidence handling: recorded the notice’s exact election wording, effective date of 6 March 2023, and the credentials/prior title printed in the notice. This is a first-party appointment record; it does not independently validate the qualifications or establish later post-resignation status.

# 2026-08-08 — SRC-396/C-425–C-426 *Mothering at the Margins* foreword
Discovery: a current publisher search found the 2025 Lived Places title *Mothering at the Margins: Black Mothers Raising Autistic Children in the UK*, with Jason Arday credited as foreword author.
Capture: preserved the publisher catalogue HTML/headers and its public sample PDF. The Open University repository supplies an independent institutional bibliographic record and DOI.
Evidence handling: recorded the book-level metadata and foreword credit as a new output family. The sample does not expose Arday’s foreword text; the book’s research claims remain attributed to Malcolm and Green and are not used as evidence for Arday’s biography.

# 2026-08-08 — SRC-397/C-427–C-428 Oxford Co-PICS team page
Discovery: a fresh institutional search found the Oxford Department of Psychiatry Co-PICS team page, which was not yet represented as its own source-version.
Capture: preserved the page HTML and response headers. The page lists Arday as a co-investigator and carries research-area and role-description text.
Evidence handling: added the project-team listing as first-party affiliation evidence. Its Cambridge-chair and trustee wording is retained as a dated, potentially stale biography version; no current employment or trustee status was inferred from it.

# 2026-08-08 — SRC-398/C-429 21percent commentary source
Discovery: a current-state controversy search surfaced 21percent.org’s 22 July commentary, which was not yet represented in the archive.
Capture: preserved the article HTML, headers, and its reproduced comparison image.
Evidence handling: classified the article as a low-provenance propagation witness. It links to Cofnas and Arasite and repeats institutional-response context, but it is not independent corroboration or an adjudication.

# 2026-08-08 — C-430 bounded recheck of unresolved Durham chapter
Discovery: the residual scholarly queue identified “Decolonising higher learning education in the UK” as the next high-value unresolved output.
Search: ran exact-title and host-volume searches across public web results, La Découverte, BnF/WorldCat-indexed results, and the existing Durham/GRIP/Steinmetz witnesses.
Outcome: no chapter-level publisher record, DOI, ISBN, pagination, library record, or full text appeared. Updated SRC-211’s access boundary and retained the lead as unresolved rather than creating a duplicate or inferring non-publication.

# 2026-08-08 — SRC-430/C-491 Bonita Corrie-Lunn viva examiner lead

Discovery: a public search-index result for Dr Bonita Corrie-Lunn’s LinkedIn profile exposed her statement that she had successfully defended a PhD on antisemitism in British football and thanked Professor Jason Arday, Dr Jon Dart, and Dr Matthew Fiander as examiners.

Access boundary: the direct LinkedIn request returned HTTP 999, so only the indexed wording and response headers are preserved. The post’s exact date and the awarding institution were not recovered.

Evidence handling: recorded this as participant-authored evidence of a doctoral-examination role, not as a formal institutional examiner record or a finding about the thesis, viva, or Arday’s broader academic service.

# 2026-08-08 — SRC-431/C-492 Oxford Brookes doctoral-programme corroboration

Discovery: the Oxford Brookes Graduate College Newsletter E19 was found through a follow-up search for Corrie-Lunn’s doctoral record.

Verification: the official PDF lists Corrie-Lunn under Doctor of Philosophy with the dissertation title “Antisemitism in British Football: Examining Good Practice in Anti-discrimination Educational Initiatives” on PDF page 16. PDF metadata gives 23 September 2025 as the creation date.

Evidence handling: this corroborates the doctoral setting and dissertation title behind SRC-430 and supports Oxford Brookes as the awarding-programme context. It does not name Arday, examiners, or the exact viva/award date.

# 2026-08-08 — SRC-432/C-493 Oxford Brookes thesis full-text capture

Discovery: an exact-title search surfaced the Oxford Brookes RADAR full thesis PDF.

Capture: downloaded the 20 MB PDF, preserved response headers, extracted layout text, and rendered the title page. The title page dates the thesis January 2025 and identifies the PhD submission, Director of Studies, and supervisors.

Negative-space check: the extracted thesis text contains no occurrence of “Jason Arday” or “Arday”. This is recorded as a bounded text-search observation, not proof that Arday was not an examiner or that the viva did not occur.

Evidence handling: upgraded the doctoral setting to a directly preserved primary document while keeping the examiner relationship dependent on Corrie-Lunn’s participant statement.

# 2026-08-08 — SRC-399/C-431 Companies House alternate officer identity
Discovery: a current Companies House search surfaced a second officer ID for Jason ARDAY.
Capture: preserved the official alternate appointments page and headers. It shows the same May 1985 birth month/year and the same Runnymede Trust appointment/resignation dates as SRC-099, but only one displayed appointment.
Evidence handling: classified the page as an alternate/duplicate officer identity and linked it to SRC-099. It is not a second person, a second appointment, or evidence that the other Companies House roles disappeared.

# 2026-08-08 — C-432 BSA/Runnymede trustee-edge recheck
Capture: rechecked the BSA governance page and Charity Commission BSA trustee register. BSA’s page was byte-identical to the prior capture and continued to list Arday as a Publications Director; the regulator page retained Arday’s 9 June 2020 trustee row without an end date, despite volatile HTML changes.
Evidence handling: retained these as current page-state observations with an administrative-lag caveat. They support a public BSA governance edge, while Runnymede remains separately closed by Companies House and the charity’s 2024 accounts.

# 2026-08-08 — SRC-400/C-433 Simon & Schuster ARC promotion
Discovery: the memoir sweep found Simon & Schuster’s separate ARC sweepstakes page, which was not represented in the archive.
Capture: preserved the direct HTTP 403/Cloudflare response headers; the public web rendering supplied the promotion title, author, dates, and prize structure.
Evidence handling: recorded it as a publisher-promotion manifestation of SRC-091. No ARC was obtained, and no marketing claim was upgraded to independent biography.


# 2026-08-08 — SRC-395/C-422–C-424 Arasite publication-notes source family

Discovery: a changed-state web search surfaced the public Arasite “J Arday Page” and its linked notes on Arday’s 2022 *British Journal of Sociology of Education* article. These pages are distinct from the four ZIP comparison dossier already preserved as SRC-386, but belong to the same self-published research-integrity source family.

Capture: preserved both HTML pages and response headers locally. The pages present host-authored observations about similar participant quotations, qualitative-method wording, BME-definition wording, repeated paragraphs, and publisher corrections. The main page expressly says it is reporting observations rather than making definitive judgments.

Evidence handling: added SRC-395/C-422–C-424. The nine linked notes are manifestations of the same host/source family and map to existing publication records; they were not promoted to duplicate sources. The page is a provenance/source-map record, not independent corroboration or an institutional finding. Existing primary comparisons (Memon, Arday’s 2018/2021/2022 articles, and publisher correction notices) remain canonical for evidentiary assessment; no new misconduct or fabrication claim was inferred.

# 2026-08-07 — SRC-388/C-415 Aderibigbe publisher-boundary recheck

The official SAGE volume-and-issue listing was checked for Aderibigbe’s 2013 *Management in Education* article. It confirms the title, author, April 2013 issue, volume 27(2), and pages 70–74, while the direct shell request returns a Cloudflare challenge. The ERIC record remains the accessible abstract-level manifestation; no article PDF or body was recovered.

Evidence handling: upgraded SRC-388 in place and added C-415. This is a metadata/access-state refinement of the existing comparator, not a new publication or a substantive plagiarism finding.

# 2026-08-07 — SRC-394 BBC *Radical* transcript boundary

Discovery: Audioscrape’s podcast index exposed a dedicated page for the 8 May 2025 BBC *Radical* episode, including Jason Arday in the description and an episode-specific media URL.

Capture: preserved the page HTML and response headers. The page explicitly states that the episode has not been transcribed yet; no transcript segments, timecodes, or downloadable transcript file were exposed.

Evidence handling: added SRC-394/C-414 as a linked access-boundary record, not a duplicate of SRC-249. No substantive remarks were extracted. Reopen only after a changed transcript or official audio state.

# 2026-08-07 — SRC-081/SRC-176/SRC-385 BAME-leadership title reconciliation

Discovery: an exact-title search surfaced the official Springer chapter page for “Many Rivers to Cross: The Challenges and Barriers Facing Aspiring Black, Asian and Minority Ethnic (BAME) Leaders in the Academy.” The page identifies Jason Arday and Marcia Wilson, first-online date 19 June 2021, pp. 313–324, DOI `10.1007/978-3-030-65668-3_23`, and an abstract with subscription-preview state.

Reconciliation: this publisher record resolves the Durham index title “Understanding, addressing and centring BAME Leadership in Higher Education” to the existing canonical SRC-176 chapter. SRC-081 and SRC-385 remain preserved as Durham title-variant/source-version witnesses; no second chapter is created.

# 2026-08-07 — SRC-388/C-416 repository and index search

Crossref, OpenAlex, and Semantic Scholar were queried for the unresolved Aderibigbe 2013 article. Crossref exposed the abstract, 21-reference metadata, and publisher-declared text-mining PDF/XML links; both direct links returned Cloudflare HTML. OpenAlex marked the article closed access with no repository full text, and Semantic Scholar reported a closed access state with no PDF URL.

Evidence handling: preserved all API responses and TDM access responses, added C-416, and closed this search pass as a triangulated access boundary. No article content was inferred from the abstract or from later papers that cite it.

# 2026-08-07 — SRC-389/C-417 Douglass published-version topology

Crossref, OpenAlex, and Semantic Scholar were queried for the published article corresponding to the public HKU conference PDF. Crossref identifies the three-author version as “An Exploration of the Characteristics of Effective Undergraduate Peer-Mentoring Relationships,” *Mentoring & Tutoring* 21(2), pp. 219–234, DOI `10.1080/13611267.2013.813740`; OpenAlex marks it closed with no repository full text, and Semantic Scholar reports no open-access PDF. Taylor & Francis still returns a Cloudflare challenge.

Evidence handling: upgraded SRC-389 in place and added C-417. The public conference PDF remains a distinct source-version; no wording from the inaccessible version of record was inferred.

This log records completed discovery work so later sessions do not repeat it without a reason.

| 2026-08-06 | UAL *Opening Out* event recovery | UAL indexed event listing, direct UAL endpoint, Eventbrite registration record, and promotional image | Added SRC-305/C-287 for the 4 March 2026 online dialogue with Shân Wareing, Jason Arday, and Silke Lange. Preserved the matching Eventbrite page/image and the UAL 403/changed-state response. | Keep the event as a scheduled/listed appearance only; no delivery, attendance, recording, transcript, or slides are established, and Eventbrite biography copy is not independent affiliation evidence | Reopen only if UAL or an attendee publishes a report, recording, transcript, or slides |

| 2026-08-06 | *Revista História Hoje* provenance upgrade | Official journal article page and PDF endpoint for the already-canonical SRC-216 interview | Reverified the 28 November 2023 interview at the journal’s own host, confirmed the article’s displayed CC BY 4.0 license, and preserved the journal HTML, PDF headers, journal headers, and extracted text. No new source or claim was created; existing C-151–C-155 remain canonical. | Keep the Portuguese translation/edited interview as first-person testimony and source-versioned evidence; do not treat the license as permission to redistribute third-party material quoted in the article | Reopen only if the journal changes the article/license or a non-translated source version appears |

| 2026-08-06 | Cambridge EDI Information Report 2023–24 | Official 144-page report and existing “Black Men on the Couch” video record | Added SRC-304/C-286. PDF p. 8 records the October 2023 panel, more than 100 attendees, and more than 6,000 YouTube views at the report’s snapshot; preserved PDF, text, and headers. | Keep this retrospective audience metric separate from the video transcript and do not treat it as current view count | Reopen only if Cambridge publishes a revised report or a new event metric |

| 2026-08-06 | Cambridge Regent House roll versioning | Official *University Reporter* Special No. 1 proposed roll (1 October 2025) and Special No. 2 promulgated roll (6 November 2025) | Added SRC-302/C-285 and SRC-303/C-284. Both list “Arday, Jason Atta Kwei, JE”; the final roll says it governs until November 2026. Preserved both PDFs, derived text, and headers. | Keep the proposed version as superseded history and the promulgated roll as canonical for the period; do not infer current status after resignation | Reopen only after a new promulgation, correction, or changed Regent House record |

| 2026-08-06 | Cambridge Education Faculty Committee roster | *University Reporter* No. 6763, 11 December 2024, official PDF | Added SRC-301/C-283. Printed p. 188 lists Professor Jason Arday on the Education committee for the Academic Career Pathways 1 October 2025 exercises; PDF, text, and headers preserved. | Keep this dated committee appointment separate from the College Fellows roster and from current Cambridge status | Reopen only after a new committee notice, correction, or changed institutional record |

| 2026-08-06 | Cambridge College Fellows roster | University of Cambridge *Reporter* Special No. 3, 2025–26 PDF and derived text | Added SRC-300/C-282. The Jesus College section on printed p. 32 lists “Arday Jason phd frsa”; preserved 77-page PDF, text extraction, and headers. | Keep the roster separate from the 2023 appointment and 2026 resignation records; do not infer current status | Reopen only if Cambridge publishes a new roster, correction, or post-resignation college record |

| 2026-08-06 | Current legal-role reconciliation: Autism Centre of Excellence | Companies House company 12435820 officers page and existing Charity Commission record | Added SRC-299/C-281; Companies House directly lists Arday as an active director appointed 30 March 2024, with no resignation date shown. Captured HTML and headers. | Keep the company-law snapshot distinct from the Charity Commission trustee record and do not infer post-Cambridge-resignation continuity | Recheck only after a new filing or changed officer state |

| 2026-08-06 | *Telegraph* investigation report | Archived article, original publisher URL, response headers, and linked image endpoints | Added SRC-298/C-280 after deduplicating against the existing *Analyse That*, Associated Press, Guardian, and Retraction Watch records; archived full page, original 403 response, headers, and two images preserved | Keep allegations, comparative examples, and quoted Cambridge/LJMU positions source-versioned; do not convert them into findings | Reopen only on a changed publisher state or newly surfaced primary investigation document |

| Date | Scope/query family | Sources searched | Boundary reached | Result | Next move |
|---|---|---|---|---|---|
| 2026-08-06 | Good Law Project solidarity-letter recovery | Good Law Project site search, canonical petition page, WordPress shortlink, direct HTML, response headers, and credited image | Found the distinct canonical page, published 28 July and modified 6 August; captured the displayed 16,755-signature counter and signatory block. The page’s exoneration and “smear campaign” language is advocacy, not an institutional finding. | Keep the page separate from Arday’s resignation statement and Cambridge’s investigation statement; re-capture only if a version/date or signature-count comparison is needed |
| 2026-08-06 | Publishers Weekly memoir-review capture upgrade | Publishers Weekly review page, direct HTML, response headers, and publisher-hosted cover endpoint | Upgraded existing SRC-117 in place; captured the 7 May 2026 review page, review text, and 331×500 cover. The review preserves memoir versions of age 12, phonics/reading at 18, and St Mary’s admission in 2005, but remains secondary coverage of a self-authored memoir. | Keep C-028/C-029 versioned against the age-11 and “almost twelve years” accounts; do not treat the review as independent childhood corroboration |
| 2026-08-06 | MEA Amazing People Schools changed-state recheck | Search result, canonical MEA page, direct HTML, and response headers | The page previously captured as HTTP 404 returned HTTP 403 on a later same-day recheck; preserved the new body and headers. No underlying educational, school, or sports record became available. | Keep the indexed page as a low-provenance lead and do not repeat the exact-name search family without a new archive or replacement host |
| 2026-08-06 | Cambridge “Black Men On The Couch” recording recovery | Cambridge Black History Month announcement, Cambridge University YouTube upload `F4xI2twHWtY`, yt-dlp metadata, automatic caption endpoints, direct page snapshots, and thumbnail | Added SRC-263/C-236. Preserved the 2:13:48 360p MP4, automatic English VTT, metadata JSON, thumbnail, Cambridge announcement, and YouTube page/header snapshots. The event is distinct from Arday’s solo interviews and existing *Beyond Lonely* material; no substantive claims are extracted until captions are human-verified. | Use the local VTT for navigation and manually verify any selected timecodes before adding discussion claims; do not rerun the same YouTube ID search |
| 2026-08-05 | General biography, current role, research themes | Cambridge, Springer, Durham repository, ORCID | First-party profiles plus selected publisher records | Initial entity and publication map | Normalize individual records |
| 2026-08-05 | Videos, interviews, talks, podcasts | UCL, PBS, ABC, Guardian, Crick, Global Player, podcast indexes, YouTube discovery | Publicly indexed appearances found through exact-name searches | Initial media index created | Create one record per media item |
| 2026-08-05 | Books, reports, articles | ORCID, Durham repository, Cambridge, DOI/Crossref search, The Black Curriculum | Major outputs and DOI-linked works identified | Initial publication map created | Deduplicate by DOI and add publication records |
| 2026-08-05 | Current controversy | Cambridge, Retraction Watch, publisher/correction records, exact-name news search | Current reporting and institutional-policy context located; matter remains unresolved | Claims ledger created | Add dated primary statements only |

| 2026-08-05 | Extraordinary biographical claims | LJMU, St Mary’s, PBS, Guardian, Lives Retold transcript, TES, Straits Times, exact-name sports searches | Speech/literacy claims strongly repeated; football/snooker claims remain autobiographical and under-specified; no club or snooker record located | Verify sports records and fundraising totals |
| 2026-08-05 | Institutional events and newer scholarly output | Oxford event pages, Cambridge University Press, DOI/publisher search, ResearchGate discovery | Added two Oxford lecture records, a 2025 book foreword, and a 2024 article record; recordings for Oxford events remain unresolved | Locate surviving recordings/transcripts and continue DOI registry expansion |
| 2026-08-05 | Local asset preservation | Guardian profile page via browser asset bundling; shell download attempted for transcript PDF | Captured five Guardian image payloads locally with checksums and preserved the browser manifest; direct PDF shell acquisition failed due host resolution; browser PDF bundler exposed no PDF asset | Continue host-by-host acquisition and preserve failures |
| 2026-08-05 | Documentary and forthcoming-book discovery | Cambridge Race Equality archive, Great Big Story, rights-catalog PDF, YouTube link extraction | Added a 2020 Cambridge lecture, a 4:14 Great Big Story video record, and a forthcoming memoir catalog record; video file unavailable through browser asset capture | Verify recordings, publisher/ISBN, and publication status |
| 2026-08-06 | Student Sessions and ARU Unlearn media capture | Buzzsprout episode page/audio; ARU Unlearn page; linked YouTube recording; local ffprobe/hash validation | Added SRC-156–157; preserved one 42:04.46 MP3, one 1:35:35.02 1080p MP4, and both source pages | Continue with genuinely new podcast/event leads; transcribe these recordings only when a timestamped claim or thematic pass is selected |
| 2026-08-06 | Ruling Passions episode 2 capture and transcript extraction | Official WordPress episode page, embedded Spotify ID, Padlet embed, page transcript, and image endpoint | Added SRC-158/C-065; preserved the full 202,193-byte page/transcript and 1,918×593 image. No direct audio file exposed; transcript provides timestamped first-person childhood and autism statements | Keep Spotify as an unresolved audio lead; use the local transcript for non-duplicative claim extraction |
| 2026-08-06 | Named education and mentor follow-up | Exact-name searches for Merton College, BTEC, Southfields, Sandro Sandri, and childhood schooling; South Thames Colleges Group official profile | Added SRC-159/C-066; direct host page confirms former Merton student status and names Sandri as sports lecturer/mentor; preserved page and image. Southfields attendance, GCSEs, football club and snooker tour remain unresolved | Search only for a changed school archive, direct first-person source, or named sporting record; do not rerun the same Merton page |
| 2026-08-06 | BILT 2024 keynote media lead | BILT Conference 2024 first-party page, poster image, linked University of Bristol SharePoint MP4 | Added SRC-259/C-232; page and poster preserved, but linked MP4 returned HTTP 403 requiring SharePoint authentication; no captions or transcript recovered | Do not repeat this endpoint without a changed access state; keep keynote contents unclaimed |
| 2026-08-06 | Memoir/childhood and current-media duplicate audit | Exact-name searches for Arday’s childhood, mother Giff/Gifty, Crystal Palace/football/snooker, *Great and Unfortunate Things*, and 2025–2026 interviews/videos; publisher, Guardian, CBS, Twinkl, Bath, and podcast leads checked against the registry | No new canonical source: the Simon & Schuster memoir page/excerpt is already SRC-091, the trailer is SRC-236, and the sports/audio material is already SRC-184; search results were repeats, mirrors, or low-provenance discussion | Do not rerun this query family without a new named record, changed page, or independently attributable media artifact |
| 2026-08-06 | Simon & Schuster UK memoir-edition reconciliation | Official UK ebook page, indexed/browser text, direct shell endpoint, Cloudflare response, and publisher cover endpoint | Added SRC-260/C-233 as a distinct UK publisher manifestation; 368 pages, ISBN 9781398542761, 27 August 2026, publisher copy and cover preserved; direct page returned HTTP 403, no ebook/sample file exposed | Keep UK edition separate from the US publisher page, Google Books record, audiobook, and rights catalogue; do not treat publisher copy as independent childhood corroboration |
| 2026-08-06 | Simon & Schuster UK hardcover reconciliation | Official UK hardcover page, indexed/browser text, direct shell endpoint, Cloudflare response, and publisher cover endpoint | Added SRC-261/C-234 as a distinct UK hardcover manifestation; 336 pages, ISBN 9781398542747, 27 August 2026, cover preserved; direct page returned HTTP 403, no hardcover/sample file exposed | Keep the hardcover separate from the UK ebook, US edition, audiobook, and Google Books records; do not duplicate its repeated memoir framing |
| 2026-08-06 | 2026 investigation/resignation primary-statement upgrade | Good Law Project canonical resignation page, WordPress metadata, direct HTML, response headers, and credited image | Upgraded existing SRC-094 in place; preserved the 5 August 2026 statement page and portrait locally. No new investigation outcome or adjudication was found. | Keep the statement as Arday’s attributed position; do not infer acceptance, exoneration, or misconduct from resignation or wording |
| 2026-08-06 | Southfields Academy primary-record boundary | Official Southfields Academy exact-name search, current site navigation, and Alumni & School History page | Added SRC-160/C-067; preserved an 80,335-byte official page showing no directly accessible Arday attendance, alumni, register, or examination record | Do not rerun the current page; retry only after a historical archive, school-held response, or new first-person lead appears |
| 2026-08-06 | ARU 2021 keynote recording capture | Official ARU Annual Conference 2021 page, embedded player URL, video ID `312Fb8E6`, repeated shell requests | Added SRC-161/C-068; preserved the 105,995-byte event page. Player host timed out repeatedly; no video, captions, manifest, or transcript was claimed | Retry only after the player host changes state or a new official mirror/download lead appears; keep separate from the locally preserved 2025 ARU recording |
| 2026-08-06 | Royal Society biography reconciliation against BSA records | Royal Society indexed profile, current BSA governance page, BSA-hosted biography PDF, Companies House Runnymede termination, BSA trustee record | Added SRC-162–163/C-069–070. Current BSA governance page confirms Arday as a Publications Director; the BSA PDF says formerly Runnymede trustee for 11 years and presently BSA/Autism Action trustee, clarifying the Royal Society’s stale present-tense Runnymede wording | Directly audit Autism Action, Adult Literacy Trust, Get Further, RSA, and CLASS only through new host records; do not rerun the same BSA/Royal Society pages without changed state |
| 2026-08-06 | Remaining named-role host audit | Adult Literacy Trust governance page and patron announcement, Get Further patron announcement and metadata, exact-name searches for Autism Action/RSA/CLASS | Added SRC-164–166/C-071–073. ALT and Get Further now have direct host confirmations and local page/image captures; no direct Autism Action, RSA or CLASS host record was found in the bounded scope | Keep Autism Action/RSA/CLASS unresolved; retry only after a new host page, archive, or named governance record appears |
| 2026-08-06 | Autism Action identity and trustee verification | Charity Commission full-print record for charity 1191599, working-name field, trustee table, and appointment date | Added SRC-167/C-074; resolved Autism Action as the working name of Autism Centre of Excellence and verified Arday’s trustee appointment on 30 March 2024; preserved the 158,401-byte regulator snapshot | Keep RSA and CLASS unresolved; do not repeat the Autism Action identity search without a changed regulator record |
| 2026-08-06 | RSA/CLASS current-profile version audit | Direct Cambridge Faculty of Education profile fetch; exact-name web results; comparison with earlier Cambridge and third-party biographies | Added SRC-168/C-075; preserved a 63,029-byte current Cambridge HTML snapshot. The current page omits RSA and CLASS wording that remains in older biographies; no direct RSA Fellow directory or CLASS panel page was found | Treat the omission as a changed-page boundary, not role termination; retry only on a new RSA/CLASS host record, archive, or changed page |
| 2026-08-06 | Specialist-school recognition lead | Springfields Academy “Explorer Secondary Classes” page and exact-name search | Added SRC-169/C-076; preserved a 141,008-byte official school HTML page naming an “Arday Class” after Jason Arday among autistic-community achievers | Retain as public recognition only; do not infer school attendance, diagnosis, or childhood history from the page |
| 2026-08-06 | BBC *Beyond Lonely* current-availability/API audit | BBC Sounds episode pages, RMS playable-episode API for series `m002b0hc`, BBC artwork, and contemporary radio listings | Updated SRC-063/C-077; preserved three current episode pages, a 10,436-byte API response, artwork, and two current 404 pages. The API marks downloads DRM with no file URLs; the “Young and Lonely…” synopsis adds dated teenage snooker/solitude wording | Keep the three current records canonical and the 17 April listing as a superseded state; retry only if a non-DRM file, transcript, or changed BBC episode endpoint appears |
| 2026-08-06 | OpenAlex author/works audit | OpenAlex author search for Jason Arday, author `A5048886069`, and filtered works API (`per-page=200`, publication date ascending) | Added SRC-170/C-078; preserved author and works JSON snapshots. OpenAlex returned 56 works, 54 DOI-bearing and 2 without DOI strings; several DOI/title mappings remain queued for publisher-level reconciliation | Reconcile the nine high-priority candidate DOI/title families in SRC-170 against publisher and repository records; do not treat the OpenAlex count as a replacement for ORCID’s 11 or Durham’s 58 |
| 2026-08-06 | OpenAlex DOI candidate verification | University of Birmingham repository PDF and Royal Holloway/DOI metadata for CoPICS; LSE Research Online PDF and BMJ metadata for the 2025 narrative-inquiry protocol | Added SRC-171/C-079 and SRC-172/C-080; preserved two open-access institutional PDFs with DOI, author, date, and article-number verification | Continue with the remaining OpenAlex candidate queue; deduplicate book/foreword manifestations before creating further records |
| 2026-08-06 | OpenAlex DOI candidate verification, second pass | Queen’s University Belfast repository PDF for DOI 10.1002/berj.4047; MDPI publisher PDF for DOI 10.3390/socsci7100196 | Added SRC-173/C-081 and SRC-174/C-082; preserved two article PDFs and verified authorship, journal, date, DOI, and page/article metadata | Continue the remaining DOI queue, especially book chapters and 2026 OSF preprint versions; keep alternate editions deduplicated |
| 2026-08-06 | OpenAlex DOI candidate verification, book-chapter pass | Springer chapter metadata and edited-book pages; Durham repository records for Being Black and Sowing | Added SRC-175/C-083 and SRC-176/C-084; upgraded SRC-080/C-085 with DOI, pagination, and publisher HTML snapshot; reduced the OpenAlex queue to the educational-leadership chapter and two OSF versions | Reconcile 10.5040/9781350068629.ch-008, then audit OSF versioning and remaining book/foreword manifestations |
| 2026-08-06 | OpenAlex DOI candidate verification, educational-leadership and OSF version pass | Bloomsbury book record, Crossref API, OSF API v2, contributor/file metadata, and public OSF primary PDFs | Added SRC-177/C-086 and SRC-178/C-087–C-088; separated the 2019 book chapter from the 2018 journal article, and preserved both OSF preprint PDFs plus metadata; v2 is marked latest | Continue DOI/edition deduplication for remaining forewords, alternate books, and any residual OpenAlex manifestations |
| 2026-08-06 | OpenAlex DOI manifestation and edition pass | Routledge book page/Crossref chapter metadata, Glasgow repository/Pedocs article PDF and record, OpenAlex foreword identifiers, and publisher contents records | Added SRC-179/C-090 and SRC-180/C-092; upgraded SRC-030, SRC-041, SRC-016, and SRC-039; added SRC-181/C-093; preserved the *Black Professoriate* PDF and *Cool Britannia* cover, and collapsed duplicate foreword DOI manifestations into canonical records | Verify the remaining Fire Now DOI, Liberated Library roundtables, Equality and Diversity in Teacher Education, and older encyclopedia/book candidates |
| 2026-08-05 | Public document acquisition | UCL keynote PDF search; Cambridge repository correction PDF search | Added canonical records for two authoritative PDFs; both render publicly but neither is locally writable through the current browser/shell path | Reattempt downloads only when a supported file-transfer path is available |
| 2026-08-05 | Scholarly publication normalization | ORCID 11-work record, Durham repository 58-output record, BMJ Open, SAGE, DOI/Crossref discovery | Added four canonical records: study protocol, Black pupils chapter, football chapter, and 2018 educational-leadership article; DOI deduplication preserved | Continue through remaining Durham output families and separate manuscripts-in-preparation from published work |
| 2026-08-05 | Books and reports normalization | Runnymede Trust, The Black Curriculum, Routledge publisher records, Durham metadata | Added canonical records for *Aiming Higher*, *The Black Curriculum* report, and *Cool Britannia and Multi-Ethnic Britain*; edition and contributor distinctions retained | Normalize *Doing Equity and Diversity*, *Dismantling Race*, and remaining reports; acquire public PDFs only with provenance |
| 2026-08-05 | Media source normalization | UCL, PBS, ABC News, Global Player, Listen Notes, Lives Retold, BBC programme discovery | Added six canonical media records with dates, runtimes, captions/timestamp metadata, and explicit local-acquisition states; confirmed the Lives Retold PDF identifies itself as the 20 March 2021 BBC Lent Talk transcript | Continue institutional/event media discovery and attempt lawful local capture of streams, slides, audio, and transcript PDFs |
| 2026-08-05 | Major books and reports normalization | Springer/Palgrave, Princeton/De Gruyter, Durham, ThinkHigher, Glasgow Enlighten, PeDOCS | Added five canonical records: two edited books, the 2025 neurodiversity book, the ThinkHigher report, and the *Black Professoriate* article; preserved roles, DOI/ISBN differences, and repository availability boundaries | Continue remaining report/article records and DOI-level reconciliation |
| 2026-08-05 | DOI reconciliation | ORCID 11-work boundary, Durham journal-output pages, Crossref/DOI publisher pages, Springer, Taylor & Francis, SAGE, MDPI, Glasgow Enlighten | Added 12 canonical DOI article records (SRC-042–053), including the original 2018 mental-health article and distinct 2021 leadership article; no duplicate DOI IDs introduced | Reconcile Durham’s remaining non-DOI outputs, manuscripts, reports, chapters, and media artefacts |
| 2026-08-05 | Dated media-appearance timeline, institutional event pages, and interview indexes | Advance HE, City St George’s, University of Bristol, BOLD, Manchester Metropolitan University MMUtube, The Cambridge Student | Added six canonical records (SRC-054–059); Bristol’s two URLs were deduplicated as one event; the Cambridge Student page is explicitly marked revised; no local video binaries were acquired | Continue BBC Programme Index/radio discovery, then reconcile Durham non-DOI outputs and attempt lawful local binary preservation |
| 2026-08-05 | BBC and radio appearance reconciliation | BBC Programme Index leads, Radio 4 listings, Cambridge Festival report/programme, Cambridge 105, UEA activity record, podcast indexes | Added four canonical records (SRC-060–063); separated the 2020 *Moral Maze* URL from the 2021 Lent Talk, and kept the 2024 Cambridge Festival event distinct from its related radio listing | Reconcile Durham’s remaining non-DOI outputs and continue local binary preservation |
| 2026-08-05 | Durham non-DOI output reconciliation, first slice | Durham person/output index, Durham output records, CLASS/UCU, BBC Newsnight, Guardian, UKCGE | Added six canonical records (SRC-064–069) spanning a report chapter, broadcast journalism, authored commentary, two submitted manuscripts, and a media lead; publication and recording boundaries remain explicit | Continue remaining Durham report/chapter/digital-artefact families and audit biographical claims |
| 2026-08-05 | Durham non-DOI output reconciliation, report/chapter/digital-artefact slice | Durham type-filtered and year-filtered output indexes, UCU, Leading Routes, Springer, Information Age, Bloomsbury, BSA, Guardian, University World News | Added eight canonical records (SRC-070–077), including 2017 report/media records, 2019 report and chapters, and 2020 journalism/digital artefacts; no DOI duplicates introduced | Continue 2021 chapter/digital-artefact records, then audit claims and local files |
| 2026-08-05 | Durham non-DOI output reconciliation, 2018–2021 chapters and BBC artefacts | Durham book-chapter/year indexes, Bloomsbury, Palgrave, BBC News | Added six canonical records (SRC-078–083), including *The Fire Now*, *Decolonizing Teaching and Learning*, two *Doing Equity* chapters, and two BBC digital-artefact records; direct BBC role/date remains unresolved where the repository does not expose it | Continue remaining forthcoming manuscripts and 2015–2017 outputs; then audit biography claims |
| 2026-08-05 | Biographical claims: sports, fundraising, and education | Lives Retold transcript, JustGiving, TES, Guardian, St Mary’s, LJMU, Nelson Mandela University CV, LJMU thesis, exact-name sports searches | Added four canonical records (SRC-084–087); strengthened the 2010 fundraiser and qualification evidence, preserved the later £5.5m institutional aggregate as a separate claim, and recorded the absence of named sports records | Continue charity-accounting and early-life verification; audit remaining institutional affiliations and controversy sources |
| 2026-08-05 | Childhood and early education chronology | Guardian, Anglia Ruskin honorary citation, PBS, Lives Retold transcript, St Mary’s, Nelson Mandela University CV, LJMU thesis, Twinkl | Added three canonical records (SRC-088–090); separated reported childhood milestones from dated CV/thesis records, added the BTEC transition, and preserved family/background details as reported biography | Seek contemporaneous school, college, sports, or interview records only where publicly accessible; do not treat repeated institutional prose as independent clinical corroboration |
| 2026-08-05 | Forthcoming memoir and biographical versioning | Simon & Schuster, Publishers Weekly, foreign-rights catalog | Added SRC-091 for the official publisher page; found a wording discrepancy between earlier age-11 accounts and the memoir copy’s “almost twelve years without language” formulation | Preserve the memoir excerpt/metadata if lawfully downloadable; compare the published edition against the publisher page after release |
| 2026-08-05 | 2026 controversy: institutional announcement and resignation | University of Cambridge notice URL, Good Law Project, Guardian | Added SRC-092–095; Cambridge’s investigation announcement, Good Law Project copy of Arday’s resignation statement, and Guardian’s investigation/resignation reports are now canonicalized; no final findings located | Locate primary LJMU, Cambridge, Jesus College, publisher, and journal responses; keep investigation and resignation separate from adjudicated outcomes |
| 2026-08-05 | Institutional affiliation and qualification records | Cambridge Faculty profile, London Metropolitan University, Liverpool School of Tropical Medicine, University of Westminster, Ohio State exact-site searches, Guardian investigation | Added SRC-096–098; London Met documents a 2020 Visiting Professor presentation and LSTM preserves a 2020 biography claiming multiple visiting roles; current Ohio State primary confirmation was not found; Guardian’s amended long-form page is now canonicalized | Check archived university staff pages, institutional press offices, and formal appointment records for Ohio State, Glasgow, Durham, Coventry, Nelson Mandela, and London Met; preserve denials or removals as separate records |
| 2026-08-05 | Public filings and charity governance | Companies House officer/filing history, Charity Commission trustee records, British Sociological Association, First Star Scholars UK, Cambridge current profile | Added SRC-099–104; verified dated Runnymede and First Star directorships, BSA trusteeship, and a materially changed Cambridge profile; Charity Commission pages were partly inaccessible to the fetcher, so search-result records and URLs are preserved | Recheck Charity Commission snapshots/PDFs, establish BSA end date and any Autism Action governance record, and keep governance records separate from fundraising accounting |
| 2026-08-05 | Local public-document capture | UCL PDF, Cambridge repository PDF, The Black Curriculum PDF, LJMU thesis PDF, Oxford Brookes RADAR manuscript, PeDOCS mirror, Squarespace transcript host, Durham accepted-manuscript endpoint | Captured five valid PDFs locally with checksums and page counts; BBC transcript and PeDOCS article attempts failed at DNS resolution; Durham’s 2024 accepted-manuscript endpoint returned 403; added an append-only acquisition/failure manifest | Continue host-by-host capture for remaining downloadable PDFs/transcripts; do not claim files for failed hosts |
| 2026-08-05 | Remaining Durham/ORCID scholarly output slice | Durham output pages 1–3 and exact-title searches, Cambridge University Press DOI metadata, Taylor & Francis, Oxford Brookes RADAR, Runnymede | Added SRC-105–108: one 2015 report, two 2021 scholarly articles, and one 2024 open-access article; no duplicate DOI records introduced | Continue page-by-page Durham reconciliation for outputs not exposed in search results, then audit publisher/accepted-manuscript availability |
| 2026-08-05 | Media lead reconciliation: Society for Experimental Biology, IDN, South Bank Colleges, ITV Black Voices, and Crick Institute | Exact-name web searches; Class Central; IDN event page; South Bank Colleges event page; ITV resource page; CrickConnect | Added SRC-109–113. Recorded one 47-minute video listing, one hybrid keynote listing, one embedded-player event page, three ITV clip URLs, and one dated Crick event; no video binary acquired and no event page was promoted to a recording without evidence | Continue original-player discovery and local-preservation attempts for SRC-109–112; separately reconcile remaining event pages and negative-space observations |
| 2026-08-05 | Childhood and early-education version audit | Exact-name searches for childhood, Clapham, special school, Merton College, St Mary’s, LJMU, speech, literacy, and memoir details; Cambridge Faculty, LJMU, St Mary’s, Twinkl, Publishers Weekly | Added SRC-114–117. Captured special-school-to-mainstream and therapist wording, Cambridge’s music/Sandro Sandri narrative, St Mary’s 2023 education and £4.5m version, and the Publishers Weekly memoir review’s age-12, phonics, and 2005 formulations. No school, medical, or family records located. | Continue with named-school/archival searches and preserve any changed or inaccessible childhood pages; keep speech-age and fundraising discrepancies versioned |
| 2026-08-06 | Institution-by-institution affiliation reconciliation | Cambridge current/earlier profiles; BERA; University of Glasgow ELP; UKCGE; Nelson Mandela University CriSHET; University of Leeds Generation Delta; Companies House/Charity Commission; Herald Scotland denial lead | Added SRC-118–123 and created `affiliations.md`. Historical biography claims, preserved PDF evidence, current Durham programme wording, and reported Glasgow/Ohio State denials are separated; no direct host appointment record was found for Ohio State or Coventry, and the Herald page was inaccessible | Continue primary-host verification for Ohio State, Coventry, Durham honorary status, Nelson Mandela title/status, and inaccessible denial sources; preserve current and superseded page states |
| 2026-08-06 | Direct host-domain affiliation search | `site:osu.edu`, `site:coventry.ac.uk`, `site:durham.ac.uk`, `site:mandela.ac.za`; exact-name and role-term searches; review of dated CV and primary institutional PDFs | Added SRC-124. No direct Ohio State or Coventry appointment page; no Durham HR/department record for honorary/visiting wording; Nelson Mandela CriSHET evidence retained; CV’s page-1 historical/external appointment list expanded into the affiliation ledger | Treat SRC-124 as the completed boundary for this pass; next search should target named host archives or newly surfaced direct statements, not repeat the same queries |
| 2026-08-06 | Consolidated negative-space and changed-state audit | Current fetch checks for Cambridge statement, Herald Scotland, Charity Commission, Durham accepted manuscript, BBC transcript, and Nelson Mandela CV; review of all existing source/media/asset failure notes | Added SRC-125 and `negative-space.md`. Separated inaccessible/unsafe URLs, HTTP 403, missing/changed pages, revised pages, streaming-only media, unresolved contribution roles, and defined no-result searches; no missing record was converted into a positive claim | Future work should append new observations only when external state changes; use the ledger before repeating a failed or completed search |
| 2026-08-06 | Durham page-level scholarly audit continuation | Indexed Durham person/output pages, exact-title search, Durham record 1291282, and LJMU journal issue | Added SRC-126 for Arday’s 2013 peer-reviewed peer-mentoring article; direct Durham list remains Cloudflare-blocked, so indexed metadata is used only where matched to a specific output record and publisher link | Continue with uncatalogued outputs only when a specific title can be matched to an authoritative publisher, broadcaster, or institutional record; do not treat repository snippets as proof of publication status |
| 2026-08-06 | Named childhood school search | Exact-name and school-type searches; Cambridge appointment page; ARU citation; Twinkl; LJMU; TEFS account; Guardian appointment profile; 2020 CV; current Southfields Academy site | Added SRC-127 and SRC-128. A secondary 2023 account names Southfields Community College; the *Guardian* independently repeats the two-GCSE detail, while the CV documents later employment at Southfields. Cambridge’s current page does not name the school, so enrollment remains reported rather than independently verified | Search school archives, contemporary records, and direct first-person sources for corroboration; do not repeat general biography queries without a new lead |
| 2026-08-06 | Media and memoir lead continuation | Exact-title searches; Global Player; Tapesearch; BBC programme/listings pages; The Bookseller; publisher/trade search results | Added SRC-129–131: a 2025 podcast interview with a timestamped transcript index, a 2023 BBC *Today* guest-editor programme, and a 2026 *Bookseller* memoir interview. Streaming, transcript, and login boundaries are recorded; no media binary was represented as locally preserved | Continue by testing stable audio/document endpoints only when a new public lead appears; do not copy copyrighted transcript text into the archive |
| 2026-08-06 | Cambridge statement recheck and changed-state capture | Direct curl fetch of the official 5 August investigation notice and linked 2 August media statement; HTML extraction; SHA-256 verification | Added SRC-132, upgraded SRC-093 from inaccessible lead to primary page with local HTML snapshot, and preserved the earlier access failure as a changed-state observation. Cambridge’s wording about prior investigations is kept distinct from any finding | Recheck only on a new institutional update; track Jesus College’s separately mentioned steps and any published investigation outcome |
| 2026-08-06 | 2011 fundraising-page capture | JustGiving page for “The 300 (300 miles in 3 Days)” | Added SRC-133 and preserved the closed HTML page with checksum. The page establishes a planned 2011 treadmill challenge, displayed £380 + £80 Gift Aid, and a retrospective “just over £8,000” wording for 2010; completion and audited totals remain open | Search charity/event archives for independent completion or accounting evidence; do not merge page totals |
| 2026-08-06 | Royal Society institutional-profile and image capture | Royal Society profile page, linked image endpoint, Companies House comparison | Added SRC-134, locally preserved the 546×546 JPEG portrait, and recorded the profile’s awards, committees, and role wording. The profile’s Runnymede trustee statement conflicts with the Companies House termination record; the HTML itself returned 403 to shell capture | Search official award bodies and committee pages for independent confirmation; retain Royal Society wording as a versioned biography rather than extending legal roles |
| 2026-08-06 | First-party award and honorary-degree verification | Genius Within, Southampton Solent University, MBCC Awards, and British Science Association pages; local HTML/image capture and checksum verification | Added SRC-135–138. All four honours named in the Royal Society profile now have direct awarding-body corroboration; exact dates remain unknown for Genius Within and BSA | Continue with individual award pages only if a new lead appears; next open boundary is reconciliation of other current institutional biography claims and remaining local media binaries |
| 2026-08-06 | Current institutional advisory-role reconciliation | ITV Cultural Advisory Council announcement; NHS Race & Health Observatory Academic Reference Group page and 2021–2022 annual report; exact-name RSA/CLASS searches | Added SRC-139–140. ITV and NHS roles now have first-party host records; no direct RSA Fellow or CLASS panel member page was found in the defined search | Search only on a new institutional update or a specific dated lead; next open family is remaining scholarly/media binary preservation and unresolved host-role claims |
| 2026-08-06 | RSA/CLASS host-record access recheck | RSA search endpoint, CLASS search URL, broader dated biography witnesses | Preserved RSA HTTP 403/Cloudflare HTML and headers plus CLASS DNS failure in the SRC-166 boundary metadata. The *Now and Men* page remains a dated secondary witness, not direct host confirmation; no RSA/CLASS governance record was obtained | Keep both claims unresolved; retry only after a changed host page, restored CLASS domain, archived governance record, or newly surfaced named announcement |
| 2026-08-06 | NHS RHO annual-report preservation | Downloaded and text-checked the 40-page 2021–2022 annual report; Arday match located on PDF page 16 | Added SRC-141 and preserved the dated first-party PDF with checksum, strengthening C-043 beyond the current profile page | Keep the advisory role’s end date open; do not infer current membership from the 2021–2022 report alone |
| 2026-08-06 | UCL keynote binary preservation | YouTube canonical recording `2S8JUO3M_04`; public stream metadata and local mux/validation with ffmpeg | Updated SRC-031 and media index; preserved a 248M MP4 with checksum, 42:07 duration, and VP9/Opus stream metadata. Temporary WebM components were not retained in the workspace | Continue media capture only for a new stable public stream; UCL slides remain a separate target |
| 2026-08-06 | Great Big Story documentary binary preservation | YouTube canonical recording `VMotp-PzBAI`; public stream metadata and local mux/validation with ffmpeg | Updated SRC-019 and media index; preserved a 26M MP4 with checksum, 4:14.86 duration, and AV1/Opus stream metadata. Existing source record was updated rather than duplicated | Continue bounded capture with the next verified public media lead; captions and non-video assets remain open |
| 2026-08-06 | India Today childhood/literacy media capture | India Today NewsMo page and exposed first-party MP4 | Added SRC-254; preserved the 1:26 MP4, page snapshot, response headers, and checksums. The video repeats the existing age-18 literacy framing and creates no duplicate claim | Keep the media attached to C-006/C-007; seek a new source only if it adds concrete childhood chronology or a changed-state media lead |
| 2026-08-06 | Dated early-career biography reconciliation | Academic Libraries North PDF indexed in a fresh role/education search; direct PDF retrieval succeeded | Added SRC-255/C-229; preserved the one-page 20 June 2019 biography, derived text, headers, and checksums. It supplies a contemporaneous host-published witness for the school-governor and external-role family already present in the 2020 CV | Treat the roles as dated biography claims; seek named governing-body or committee records only if a new direct host lead appears |
| 2026-08-06 | NoWAL 2019 handbook changed-state check | Indexed conference-handbook lead; direct Academic Libraries North URL redirected and returned HTTP 404 | Added SRC-256; preserved the 404 HTML and response headers. No event, keynote, or affiliation claim was created | Reopen only with an archive, mirror, or changed host state |
| 2026-08-06 | Scholarly residual search: *Decolonizing University Teaching and Learning* | Exact-title search across Durham, Bloomsbury, book metadata, and an indexed public mirror | Updated SRC-079’s access boundary; the TransReads mirror now returns HTTP 404 and is locally preserved as a changed-state record. No unauthorized full text was captured and no new publication node was created | Retry only after a changed official publisher/repository page or authorized preview/full-text lead |
| 2026-08-06 | Publisher check: *Dismantling power and privilege through reflexivity* | Taylor & Francis issue page, article page, DOI, and PDF endpoint | Updated SRC-043; publisher search metadata confirms pages 141–161, online publication 6 February 2019, abstract, and DOI, while direct article/PDF requests return HTTP 403. Preserved both response bodies and headers; no duplicate article or new claim created | Retry only after a changed publisher access state or authorized repository copy |
| 2026-08-06 | LJMU bicentenary profile capture | Current LJMU “Our People” page, response headers, and two linked profile images | Added SRC-257/C-230. Preserved the former-lecturer/alumni profile, November 2022 EDI visit wording, Phil Vickerman quotation, and two images; repeated childhood details remain attributed biography rather than independent records | Keep LJMU’s current page distinct from its 2023 alumni-news article; seek event media only if a new LJMU recording or archive lead appears |
| 2026-08-06 | LJMU “Harvest for the World” audio capture | LJMU neuroinclusivity page, SoundCloud track 1762111230, oEmbed, public progressive resolver, MP3 stream, and artwork | Added SRC-258/C-231. Preserved the 40:37.146 MP3, LJMU/SoundCloud pages, resolver response, headers, and artwork; no transcript or substantive content claims created | Transcribe or listen manually before extracting claims; retain SoundCloud’s all-rights-reserved/non-downloadable metadata and do not assume other LJMU tracks are downloadable |
| 2026-08-06 | PBS biographical interview partial capture | PBS page, embedded transcript material, official English VTT endpoint, thumbnail, and player inspection | Updated SRC-032; preserved page HTML, official timecoded captions, and 1920×1080 thumbnail. Captions provide timecoded first-person and narrated details; the video stream remains unavailable as a stable downloadable file | Continue with the next verified media lead; do not rerun PBS unless the player or endpoint changes |
| 2026-08-06 | ABC News profile binary preservation | ABC canonical video page, embedded schema metadata, direct Akamai HLS manifest, and official thumbnail | Updated SRC-033; preserved a 51M MP4 and 992×558 thumbnail with checksums. The page exposed no caption track, so the recording remains a media asset rather than a transcript source | Continue with the next verified media lead; do not rerun ABC unless its page or manifest changes |
| 2026-08-06 | MMU LEED keynote binary and caption preservation | MMUtube Kaltura page, public flavor-asset API, public 1080p MP4 flavor, English (British) caption asset, and thumbnail endpoint | Updated SRC-058; preserved an 847M MP4, 108,811-byte SRT, and 1920×1080 thumbnail with checksums. Kaltura reports 81% caption accuracy; extracted PE-teacher wording is retained as self-report, not employment verification | Continue with the next verified media lead; do not rerun MMU unless the page, flavor asset, or caption asset changes |
| 2026-08-06 | *How Do You Cope?* episode page and artwork capture | Global Player current page, embedded episode metadata, Apple Podcasts listing, Tapesearch transcript index, and official artwork endpoint | Updated SRC-129; confirmed page/API metadata of 3,682 seconds (1:01:22), preserved the official page and 600×600 artwork, and retained the audio/transcript-unavailable boundary | Continue with the next verified media lead; do not rerun this episode unless its page, player, or transcript state changes |
| 2026-08-06 | Advance HE feature changed-state capture | Current Advance HE page, page metadata, HTML inspection, and linked header-image endpoint | Updated SRC-054; preserved the current HTML and 580×330 header image. The page was modified 30 July 2026 and still references a video, but no video element, media URL, iframe, or caption track is present in the current HTML | Search for the historical video only through a newly surfaced canonical host/archive lead; do not rerun the same current page fetch without a state change |
| 2026-08-06 | South Bank Colleges graduation video preservation | South Bank institutional page, embedded YouTube ID `oLZjjg1j3Bc`, YouTube metadata, official thumbnail, and linked event photograph | Updated SRC-111; preserved a 19.64-second 1080p MP4, 1280×720 YouTube thumbnail, 800×572 event photograph, and page snapshot with checksums. No captions were exposed; page biography claims remain institutional reporting | Continue with the next verified media lead; do not rerun this item unless the page or YouTube asset changes |
| 2026-08-06 | ITV Black Voices clip preservation | ITV resource-page lead, YouTube metadata for `_lykjHjmIZ0`, `HcS7rwhA6jM`, and `J0ToSMSsRGs`, public streams, thumbnails, and UCU caption endpoints | Updated SRC-112; preserved two MP4s (5:14 and 4:50), two thumbnails, and one English VTT caption track. The first linked video is private; the ITV page timed out during current shell capture. Added C-047 for the UCU clip’s first-person career statement | Continue with the next verified media lead; do not rerun the private clip or timed-out ITV page without a state change |
| 2026-08-06 | Society for Experimental Biology recording lead | SEB institutional resource page, linked YouTube ID `H30IeW5J69I`, Class Central listing, Issuu programme link, thumbnail and page endpoints | Updated SRC-109; recovered the stronger first-party page and canonical recording URL, preserved the SEB HTML, 1280×720 YouTube thumbnail, and symposium image. YouTube currently reports the recording unavailable; no video binary or programme file obtained | Continue with the next verified media lead; retry only if SEB or YouTube exposes a new recording state |
| 2026-08-06 | IDN 2024 keynote asset and recording audit | IDN event page, current page HTML/schema, named image endpoints, IDN Vimeo channel HTML, event-host LinkedIn post, Cerberus Nuclear attendee report, visual inspection of gallery files | Updated SRC-110; confirmed the keynote title “You Oughta Know: Inclusion, Intersectionality and Belonging in the Workplace,” preserved the page, named portrait, header, programme image, and two gallery files. Visual inspection found the two gallery files conflict with their Arday alt text and logged C-049; no Jason-specific recording or transcript was exposed; current Vimeo channel contained no IDN24/Jason match | Continue with the next unresolved host family; revisit IDN only if a new recording URL, archive state, or programme file appears |
| 2026-08-06 | Crick “Science and Society” event and biography audit | CrickConnect event index, current shell HTML, exact-title web search, Crick/YouTube search, and public event-page text | Updated SRC-113; preserved a 113,887-byte login-boundary HTML snapshot. The indexed event description confirms date, venue, duration, Q&A, and Zoom live-transcription option; its biography reports PhD funding through Sainsbury’s/Boots and a 600-mile-in-six-days challenge. No recording, transcript, image, or public event asset was found | Continue with the next unresolved host family; retry Crick only if the page becomes publicly retrievable or a new recording/transcript URL appears |
| 2026-08-07 | Crick “Science and Society” changed-state recheck | CrickConnect direct route and current web-rendered event page | Rechecked SRC-113 in place. The web-rendered page exposed the event description and biography, but a fresh direct HTML capture still returned CrickConnect’s login page. Added C-354 for the split access state; no public recording, transcript, image, or downloadable event asset was found | Preserve both access states; retry only after a stable public recording, transcript, or direct page capture appears |
| 2026-08-06 | Glasgow ELP same-title event | University of Glasgow ELP page, EPPE Network events index, linked Zoom registration, and asset endpoints | Distinct 25 May 2022 online seminar recorded; Glasgow page and Zoom URL return 404; EPPE HTML/image preserved; no recording/transcript | [Glasgow record](sources/2022-05-25-glasgow-elp-crossfire-hurricane.md) |
| 2026-08-06 | Memoir publisher excerpt and image preservation | Simon & Schuster official publisher page, publisher excerpt, CloudFront cover and author-photo endpoints, Companies House and Royal Society pages for adjacent profile audit | Updated SRC-091 with first-person excerpt details; preserved cover and Anselm Ebulue author photograph with checksums; publisher HTML returned 403 from shell; Royal Society’s Runnymede trustee wording remains contradicted by the 2024-11-18 Companies House termination | Continue with the next unresolved early-life/early-career lead; do not rerun the publisher shell capture without a new access state |
| 2026-08-06 | BBC profile and school-hosted witness capture | BBC canonical URL, Walthamstow School for Girls repost, page HTML, and two image endpoints | Added SRC-144; preserved 61,369-byte witness HTML and two graduation-portrait derivatives. Added reported formative memories, age-22 postgraduate decision, day/night PE-lecturer-and-sociology account, and c.2015 sociologist reflection. Direct BBC HTML remains uncaptured | Search the named-school lead and remaining sports/early-work claims only through a newly surfaced primary or contemporary source; do not treat reposts as independent corroboration |
| 2026-08-06 | Memoir edition and school-name lead reconciliation | Google Books UK edition record, official US/UK publisher metadata, Scribd upload, exact-name school searches | Added SRC-145 for a distinct 368-page UK edition record and SRC-146 for an unattributed Heath Brook Primary School lead. Edition metadata is not merged across ISBNs; Heath Brook remains unverified and the Scribd file was not locally downloaded | Seek a traceable publisher/school/direct-interview source for Heath Brook; compare edition metadata again only after publication or a changed catalog state |
| 2026-08-06 | St Mary’s 2009 alumni PDF capture | St Mary’s alumni PDF, PDF text extraction, PDF metadata, and visual render of page 11 | Added SRC-147; preserved a 24-page, 321,820-byte PDF. Confirmed Athletics Union President role, charity six-a-side tournament organising, and a quoted group total above £4,000 over three years; no personal professional-sports inference made | Reconcile the dated fundraising record against the 2010/2011 JustGiving pages and later institutional aggregates; retain accounting boundaries |
| 2026-08-06 | Open Culture sports/mentor repost capture | Open Culture feature, embedded YouTube URLs, existing Great Big Story record, related private video, page HTML, and feature-image endpoint | Added SRC-148; preserved a 197,782-byte HTML snapshot and 1532×896 PNG. Named Chris Trace as an early teacher and retained the “really good snooker player” self-description; deduplicated the Great Big Story video and logged the related private item | Search only for a newly surfaced primary/contemporary sports or school record; do not rerun the same repost chain |
| 2026-08-06 | BBC *A Good Read* audio preservation | BBC programme page `m001sm8n`, official media-selector endpoint, page HTML, and ffmpeg validation | Updated SRC-061; preserved a 27,045,718-byte 128 kb/s stereo MP3 (28:05.39) and 164,901-byte page snapshot. No transcript exposed; programme description records the books discussed without upgrading it to independent biography evidence | Test the next BBC/Global Player lead only through a newly exposed official media endpoint; do not rerun this page without a state change |
| 2026-08-06 | BBC *Moral Maze* audio preservation | BBC programme page `m000k3gr`, official media-selector endpoint, page HTML, and download response | Updated SRC-060; preserved a 41,210,368-byte official MP3 and 157,000-byte page snapshot for the 42-minute programme. No transcript exposed; contributor role and broadcast context remain the supported source boundary | Continue with the next verified audio/video lead only through a newly exposed official endpoint; do not infer transcript claims from the binary without timecoded listening work |
| 2026-08-06 | BBC *Beyond Lonely* changed-state recheck | Canonical BBC programme URL `m0029ng`, curl response, prior Radio 4 schedule/listing evidence | Updated SRC-063; confirmed the current programme URL returns 404, preserved a 32,445-byte 404 response body, and retained the broadcast record without claiming local audio | Retry only if a new canonical BBC page or traceable archive/media endpoint appears; do not treat the 404 as evidence that the broadcast did not exist |
| 2026-08-06 | PBS *The Importance of Early Intervention* video preservation | PBS page, viral-player metadata, public HLS/MP4 redirects, existing official VTT, and ffmpeg inspection | Updated SRC-032; preserved a 629,632,856-byte official 26:46 H.264/AAC 1280×720 MP4 and a 9,197-byte player snapshot. Existing captions remain timecoded programme evidence, not independent corroboration | Continue bounded capture of the next verified media lead; do not duplicate the PBS video under its HLS and MP4 aliases |
| 2026-08-06 | Oxford/Kellogg lecture video preservation | Oxford event listing, Kellogg College “Watch the film” page, official YouTube embed `c3iUb-UTpDQ`, temporary downloader metadata, and ffmpeg inspection | Updated SRC-015; preserved a 225,397,461-byte 1:18:58.94 H.264/AAC 640×360 MP4 and a 47,250-byte Kellogg page snapshot; deduplicated it from the distinct 2022 Glasgow event | Continue bounded capture with the next unresolved institutional media lead; extract claims from this recording only with timecodes and attribution |
| 2026-08-06 | Cambridge Annual Race Equality Lecture recording boundary | Cambridge event page, legacy Microsoft Stream channel URL, redirect headers, Microsoft 365 login response | Updated SRC-018; preserved 50,492-byte public event page and 51,441-byte login-boundary HTML; recording link is verified but no unauthenticated video/transcript was exposed | Retry only with a newly public or authorized recording endpoint; do not repeat the same Microsoft Stream login test |
| 2026-08-06 | Bristol/British Academy *Graceland* lecture video preservation | University of Bristol SPAIS and Law event pages, exact-title YouTube search, official University of Bristol video `xBhYvEq3qyU`, and ffmpeg inspection | Updated SRC-057; preserved a 183,882,527-byte 1:09:50.97 H.264/AAC 640×360 MP4 and two institutional page snapshots; canonicalized the two Bristol URLs as one event | Continue bounded capture with the next unresolved media lead; use the existing event record before searching for duplicate Graceland pages |
| 2026-08-06 | City St George’s inclusive-futures access and affiliation pass | City St George’s event URL, indexed institutional text, curl response, and direct-fetch body | Updated SRC-055; confirmed the URL returns 403, preserved a 5,781-byte 403 response, and retained the page’s role wording as indexed biography evidence without promoting it to host/legal confirmation | Retry only if the page becomes directly accessible or a traceable institutional archive/media endpoint appears; do not repeat the same 403 fetch |
| 2026-08-06 | BBC *Today* guest-editor page and image capture | BBC programme page `m001ts2s`, embedded schema metadata, current HTML, official `ichef` image endpoint, and media/download inspection | Updated SRC-130; preserved a 149,053-byte page snapshot and 1200×675 image. The page exposes no current media-selector/download URL or transcript, so the audio remains unresolved | Search for a newly surfaced BBC archive/audio lead or changed programme state; do not rerun the same page fetch without a state change |
| 2026-08-06 | BBC *Today* API and audio-endpoint recheck | BBC `m001ts2s.json`, BBC Sounds UK path, BBC.com audio path, and legacy media-selector endpoint | Added C-174 and preserved the 2,185-byte programme JSON plus 404/410 endpoint bodies and headers. The API confirms a 7,200-second version PID and repeats the 11/18 synopsis, but no playable audio or transcript is exposed. | Keep the API metadata as the strongest current first-party record; retry only after a changed BBC endpoint or new archive/audio lead |
| 2026-08-06 | Shaw Trust Disability Power 100 source upgrade | Disability Power 100 indexed announcement, current canonical URL, WordPress REST search, and ITV corroboration | Added SRC-222/C-175. The awarding-body announcement places Arday fourth overall and as Education category winner in 2023; the live article now redirects to maintenance and REST search returns no result, both preserved as changed states. | Retain the ranking as verified awarding-body source-version; retry only if the article or a downloadable 2023 list reappears, and do not duplicate ITV’s corroborating press release |
| 2026-08-06 | Heathbrook school-name lead identity audit | Exact-name/phrase searches, DfE establishment record, Lambeth Council listing, Heathbrook school website, Ofsted listing, and exact-name Arday searches | Added SRC-149; preserved DfE and school HTML snapshots. Confirmed the official school is spelled “Heathbrook” and located in Lambeth, while no official page linked Arday to it; retained the Scribd lead as unverified and corrected its apparent spelling/location mismatch | Seek only a traceable historical publisher archive, direct first-person account, or school-held historical record; do not rerun current school identity pages without a changed lead |
| 2026-08-06 | Heathbrook social-account claim reconciliation | Exact-name searches, secondary reproduction, quoted Heathbrook Primary account, shortened X link, and direct 404 response | Updated SRC-146/C-058; preserved the secondary reproduction and a 3,656-byte 404 snapshot of the original shortened link. The school-account attribution strengthens the lead, but no directly archived post or attendance record was found; spelling/location discrepancy remains qualified | Retry only if the original post or a traceable school/publisher archive reappears; do not promote the claim to settled attendance |
| 2026-08-06 | Generation Delta affiliation access-boundary capture | University of Leeds Generation Delta advisory page and indexed institutional wording; direct shell retrieval | Updated SRC-120/C-032; preserved a 5,502-byte HTTP 403 response. The current indexed page lists Arday and uses the Durham honorary-professor wording, but no Durham HR/department record or dates were found | Keep the wording as third-party programme evidence; retry only if the page becomes directly retrievable or a Durham host record appears |
| 2026-08-06 | Childhood and sports source-version search | Exact-phrase searches for childhood, football academy, snooker, special-school, and reading/speech claims; University of Bath institutional interview summary; PagePlace memoir-preview false positive | Added SRC-150/C-062. Bath’s indexed summary provides stronger first-person wording about academy/professional football, a professional snooker tour, special-needs schooling, and childhood support; direct page retrieval returned 403. A PagePlace result was a false positive about a different child named Jason and was not added to the Arday corpus | Preserve Bath’s wording as self-report and keep earlier conflicting formulations; seek named club/tour/school records rather than rerunning the same exact-phrase search |
| 2026-08-06 | Bounded sports-record follow-up | Exact-name/exact-phrase web searches for football clubs, academy records, professional football, snooker tour, rankings, tournaments, and school wording; Bath, Lives Retold, Twinkl, News24, Open Culture, St Mary’s, indexed news, Reddit discovery lead | Added SRC-151. No named club, team appearance, contract, snooker tour, ranking, tournament result, or independent record was found; Reddit only confirms public questioning of the Bath wording | Keep the sports claims self-reported and leave the named-record task open for new leads such as archives or first-person material |
| 2026-08-06 | Current affiliation follow-up | Exact-name searches on Ohio State, Nelson Mandela/CriSHET, Coventry, and Durham domains using current visiting/honorary/research-associate terms | Appended a follow-up observation to SRC-124; no new direct host appointment record appeared. Existing CV, CriSHET booklet, and third-party programme records remain the strongest positive evidence for the unresolved roles | Do not rerun this domain scope without a changed page or new named lead; continue with other institutional biographies or genuinely new host evidence |
| 2026-08-06 | ORCID API snapshot and DOI reconciliation | Public ORCID works endpoint for `0000-0002-9822-1068`; 11 work groups and 11 unique DOI values | Preserved the 18,039-byte JSON response and checksum. All 11 DOI values map to existing canonical publication records; no new work was added | Recheck only when ORCID changes or a new repository/publication lead appears; keep ORCID’s 11-work view separate from Durham’s broader output count |
| 2026-08-06 | Durham repository output-list access boundary | Direct requests for output-list pages 1–5; Cloudflare challenge response | Added SRC-152 and preserved a representative 5,599-byte challenge HTML. The current list could not be freshly enumerated; previously matched records remain canonical and no repository absence is inferred | Retry only after a changed access state or a specific newly surfaced title; do not rerun the same blocked page sequence |
| 2026-08-06 | *Now and Men* podcast preservation | Official episode page, Captivate MP3 endpoint, Open Graph artwork, and indexed episode description | Added SRC-153/C-063; preserved the 52,277-byte page, 93,553,902-byte 1:04:58.04 MP3, and 1,200×628 artwork. The episode’s 2022 book-project wording is recorded as a historical project state | Continue bounded podcast discovery from genuinely new catalog leads; do not duplicate the file under alternate podcast indexes |
| 2026-08-06 | Planned-book record reconciliation | Durham indexed records for *Being Young, Black and Male* and *Considering Racialised Contexts in Education*; *Now and Men*; Routledge/ISBN and bookseller catalogs | Added SRC-154–155. The first remains a manuscript-in-preparation record; the second has a 2019 contract/deposit trail, ISBN 9781138217737, and a catalog 2030 placeholder. Neither is promoted to a confirmed published book without stronger publication evidence | Search the ISBN/publisher record only for a changed catalog state or a new edition/ISBN; keep planned projects distinct from published books |
| 2026-08-08 | Planned-book ISBN manifestation recheck | Ex Libris catalogue record and cover for ISBN 9781138217737; indexed retailer/catalogue comparison | Added SRC-583/C-762. The manifestation gives 128 pages, a proposed contents sequence, and a 2030 date; preserved response headers and cover, while omitting page HTML containing unrelated client-side configuration. Publication remains unresolved | Reopen only for a publisher/library/repository manifestation, physical copy, changed ISBN/date, or lawful full text; do not repeat retailer metadata fetches |
| 2026-08-08 | Archived British Council/Royal Irish Academy keynote recovery | Wayback PDF linked from the investigative article; PDF metadata, visible title slide, text extraction, and rendered pages | Added SRC-584/C-763–C-764. Recovered a 14-page deck with visible 30 January 2019 date and recommendations on higher-education inclusion/leadership; retained the filename/date discrepancy and bounded cited statistics as unverified | Search only for a first-party programme/page, recording, transcript, or source-level verification of cited figures; do not repeat the same Wayback PDF fetch |
| 2026-08-08 | Earlier Simon Speakers Bureau biography recovery | Wayback snapshot linked from the Free Beacon article; archived HTML and headers for 10 September 2024 | Added SRC-585/C-765–C-766. Recovered the earlier specific fundraising, athletic, WaterAid, Olympic-Torch, and homeless-drive wording and linked it as a source-version to SRC-517 | Search only for named charity/race/Olympic-torch/relief-work primary records or a changed archived snapshot; do not treat promotional copy as corroboration or repeat the same snapshot fetch |
| 2026-08-06 | *How Do You Cope?* player/API and audio preservation | Global Player page JavaScript, `https://bff-web-guacamole.musicradio.com/playables/7DrrsPK/`, Acast MP3 endpoint, page/API metadata, and ffmpeg validation | Updated SRC-129; preserved a 68,952,519-byte 128 kb/s stereo MP3 probing at 1:11:49.51 and an 846-byte player API response. The page/API duration is 1:01:22, so both source-version durations remain recorded; no transcript file was copied | Search only for a changed player/API state or a newly surfaced transcript/caption endpoint; do not rerun the same endpoint without a state change |
| 2026-08-06 | *Full Disclosure with James O’Brien* player/API and audio preservation | Global Player page `7DrfQkN`, public `playables/7DrfQkN` API, Captivate MP3 endpoint, official page/artwork, and ffmpeg validation | Updated SRC-034; preserved a 67,013,485-byte 128 kb/s stereo MP3 probing at 1:09:48.34, an 801-byte API response, a 50,892-byte page snapshot, and 600×600 artwork. Page/API/file durations are 1:07:00, 1:07:18, and 1:09:48.34; API flags ad-supported playback; no transcript exposed | Test the next verified Global Player lead only through a newly surfaced public player/API endpoint; do not rerun this episode without a state change |
| 2026-08-06 | *Portrait of a Londoner* audio preservation and YouTube state check | Listen Notes structured metadata, direct Simplecast CDN URL, Listen Notes page/image endpoints, ffmpeg validation, and YouTube `YjNQbRKDXbg` inspection | Updated SRC-035; preserved a 37,787,301-byte 128 kb/s stereo MP3 probing at 39:19.30, a 292,306-byte page snapshot, and 300×300 image. Listing duration is 39:17; YouTube currently reports `LOGIN_REQUIRED`/private; no transcript exposed | Search only for a changed YouTube state or a newly surfaced first-party podcast page/transcript; do not rerun the same Listen Notes/CDN capture without a state change |
| 2026-08-06 | BBC Lent Talk transcript changed-state recheck | Canonical Squarespace PDF URL, current Lives Retold `/jason-arday` page, search-indexed transcript text, curl 404 response, and local 404 snapshot | Updated SRC-036; confirmed both the PDF endpoint and current page return 404, preserved a 42,158-byte 404 HTML snapshot, and retained the transcript as indexed/link-backed text only | Retry only if the canonical PDF or a traceable Lives Retold archive URL reappears; do not treat search snippets as a local PDF or independent corroboration |

## Search protocol

For each new research pass, record:

- the exact scope;
- date and time range, if any;
- sites or databases searched;
- query family;
- result boundary (for example, first 5 pages or all ORCID works);
- new source IDs;
- unresolved leads;
- the next action.

Do not rerun a completed scope unless the reason is explicit: new date range, newly surfaced source, changed page, or correction audit.

| 2026-08-06 | OpenAlex residual DOI reconciliation: Fire Now, Liberated Library, teacher education, older manifestations | OpenAlex works snapshot; Durham repository; Bloomsbury/PagePlace previews; Information Age/teacher-education preview; DataCite DOI APIs; Humanities Commons DOI landing pages | Upgraded SRC-078 with DOI `10.5040/9781350225480.ch-003` and a public preview PDF; upgraded SRC-074 with chapter title/pages and a public preview while retaining the publisher-404 DOI boundary; added SRC-182 for the two duplicate Liberated Library DOI records, preserving DataCite JSON and identical Humanities Commons 403 responses. Added C-094–C-096. | Continue only with older encyclopedia/book manifestations or a changed publisher/repository state; do not rerun these DOI endpoints without a new lead or state change |
| 2026-08-06 | Childhood/early-life media audit: newly indexed CBS interview | CBS News written profile and linked HLS video page; exact-name searches for first-person childhood, music, speech, literacy, and school wording | Added SRC-183/C-097–C-098. Preserved the 630,379-byte written profile, 6:39.49 1080p MP4, thumbnail, and portrait. The interview adds first-person material on observing human interaction, maternal use of music/song lyrics, and Enya; no separate captions were exposed. | Continue only with a newly surfaced childhood source, a changed CBS media state, or a named school/sports record; do not rerun this CBS page/stream without a state change |
| 2026-08-06 | Institutional biography/role reconciliation: Royal Society, Generation Delta, dated CV and historical role terms | Royal Society profile, Generation Delta advisory board, Nelson Mandela University CV URL, exact-name searches for RSA/CLASS/Durham/Ohio State/Coventry, indexed institutional biographies and programme PDFs | Existing role records were rechecked. Royal Society still publicly states RSA/CLASS/Runnymede/BSA/NHS/ITV wording; Generation Delta still indexes Arday as Durham Honorary Professor; the January 2020 CV URL now returns host “Page not found,” so its indexed committee/governance claims were upgraded in SRC-086 and C-099, with the response preserved locally. No direct host record resolved the RSA/CLASS/Ohio State/Coventry boundaries. | Do not rerun the same role searches without a changed host page, new filing, or archived governance record; next open family remains bounded media capture or older scholarly manifestations |
| 2026-08-06 | New podcast capture: *Talking Matters with Nick Halkes* | Spotify/Apple listings, Captivate RSS feed, RSS enclosure mapping, Captivate MP3, and show artwork | Added SRC-184/C-100. Corrected an initial enclosure mismatch before cataloguing: the Jason item’s GUID is `c132b81c-769b-401b-b1b2-beed7953e819`, with MP3 URL `podcasts.captivate.fm/.../Jason-01-08-24-Edit-128.mp3`; preserved 1:18:44.82 audio, feed, Apple page, and generic show artwork. | Search only for a newly surfaced transcript or changed feed/media state; do not rerun the same enclosure without a state change |
| 2026-08-06 | *Talking Matters* biographical ASR pass | Local SRC-184 MP3; `mlx-whisper 0.4.3`; `mlx-community/whisper-small.en-mlx`; targeted SRT review | Preserved JSON, SRT, TSV, TXT, and VTT derivatives with checksums. Added C-148–C-150 for source-version leads on special-to-mainstream schooling, the Crystal Palace/non-league account, and snooker practice/Pontins tournaments; added a bounded reading-age note to the biography. ASR is explicitly not treated as a verbatim transcript. | Manually listen to C-148–C-150 before tightening wording or promoting the sports details; do not rerun this transcription unless a better model, human transcript, or changed audio is available |
| 2026-08-06 | New scholarly interview capture: *Revista História Hoje* | Journal DOI/page and public PDF endpoint; local PDF extraction and page-bound review | Added SRC-216 and C-151–C-155. Preserved the 17-page PDF and recorded interview date 28 November 2023. The interview adds source-version details on unilateral hearing loss, Ghanaian/South African parental background, family poverty, parents feeding/hosting people with few resources, childhood shelter visits, the age-18 shelter encounter, and a £5m fundraising account. | Keep these as translated/edited first-person testimony; do not promote hearing, family, shelter, or fundraising details to independent fact without corroboration. Do not duplicate the existing Guardian/Cambridge biography sources. |
| 2026-08-06 | ARU honorary citation current-page upgrade | Current Anglia Ruskin University citation page, web text extraction, local HTML capture, checksum | Upgraded SRC-089 and added C-156. The current institutional version dates the shelter visit to 2003/age 18, lists 30 marathons/35 days, 300 miles/3 days, and 600 miles/12 days, and reports £5.5m for over 70 charities across 20 years. It also preserves malformed “2002 Professorial Chair” wording as a page-state anomaly. | Keep all challenge, completion, charity-count, and aggregate versions separate; do not treat institutional citation wording as audited accounting or independent event proof. |
| 2026-08-06 | Memoir publisher page browser-state upgrade | In-app browser rendering of Simon & Schuster page; expandable excerpt inspection; direct shell 403 comparison | Upgraded SRC-091 and added C-157–C-159. The excerpt is browser-visible and supplies detailed memoir material on Giff’s kitchen, the health-centre therapy room, developmental/sensory baseline, and the Brazil water-pump mission; preserved an access-state note without copying the full copyrighted excerpt. | Keep the excerpt as self-authored memoir evidence; do not treat it as a clinical or travel record. Retry shell capture only after a changed publisher endpoint; the browser-visible excerpt is already logged. |
| 2026-08-06 | Bett family-member and keynote lead | Bett Global article by Joe Arday, article HTML, associated image, and event date | Added SRC-217/C-160–C-161. Joe Arday identifies himself as Jason’s brother, records attendance at Jason’s 24 January 2024 Bett keynote, and summarizes its AI/diversity themes. Preserved the 56,942-byte HTML page and 700×473 image. | Seek the official Bett keynote recording, transcript, slides, or programme if a new public endpoint appears; do not duplicate the family-member reflection as a second childhood source. |
| 2026-08-06 | BOLD educational-journey interview capture | BOLD page, interview text, image endpoint, local HTML/image capture, checksum and dimensions | Added SRC-218/C-162–C-166. The 25 June 2024 interview adds first-person details about nonverbal observation, Dragon NaturallySpeaking/Read and Write Gold, Sandro Sandri’s mentorship, age-18 shelter relief work, and teaching; preserved a 233,306-byte page and 740×494 portrait. No video/audio endpoint exposed. | Keep these as attributed interview testimony and deduplicate against existing Sandri/shelter records; search only for a new primary school, shelter, employment, or assistive-technology record rather than rerunning this interview. |
| 2026-08-06 | Global Research Institute of Paris seminar programme capture | Official GRIP PDF, PDF metadata, text extraction, and checksum verification | Added SRC-219/C-167. The two-page 2020–2021 Dufoix seminar programme lists Arday’s 11 February 2021 presentation “Attempting to break the chain: reimaging inclusive pedagogy and decolonising the curriculum within the academy.” No recording or transcript exposed; it is kept separate from unresolved SRC-211. | Search for a recording, abstract, or speaker page only if a new endpoint appears; do not merge the programme with the unresolved “Decolonising higher learning education in the UK” chapter lead. |
| 2026-08-06 | *How Do You Cope?* bonus episode capture | Tapesearch episode page, Apple Podcasts listing, Acast recording endpoint, local MP3, ffmpeg validation, and shell access-boundary capture | Added SRC-220/C-168. Preserved the 29 May 2025 “The Gratitude List” episode as a distinct 21:13.29 MP3 and Apple page. The partial Tapesearch transcript preview adds a poverty/father’s-charity-principle passage at approximately 1:31.6–1:51.6; Tapesearch returned HTTP 403 to shell retrieval and its generated transcript is not treated as verbatim. | Manually verify the timecoded passage against the local MP3 before tightening the biography; do not duplicate the main SRC-129 interview or copy the restricted transcript. |
| 2026-08-06 | Cambridge Student revised-page capture | Current Cambridge Student HTML, visible revision notice, article text, portrait endpoint, local HTML/image capture, and checksum verification | Upgraded SRC-059/C-169–C-170. Preserved the 409,897-byte current page and WebP portrait. The page explicitly records post-discussion amendments and adds a 2017 Simon Woolley/parliamentary-scheme mentorship account; the original pre-revision version remains unavailable. | Treat the current text as a revised journalistic source; seek a named scheme or host record only if a new lead appears, and do not infer that current wording reproduces the original interview. |
| 2026-08-06 | Oxford EDB lecture media capture | Oxford event page, Vimeo page/player, Vimeo oEmbed API, Vimeo thumbnail endpoint | Added SRC-185/C-101. The 29 October 2025 event page exposes Vimeo video `1132037139`; oEmbed reports 4,315 seconds and yields a thumbnail. The player response did not expose a retrievable stream, so the event page, metadata, thumbnail, and access boundary are preserved without claiming local video. | Retry only if the Vimeo player or Oxford page changes; do not repeat the same player request without a changed state |
| 2026-08-06 | *Allyship in Action* episode 314 audio capture | Libsyn episode page/player, public MP3 endpoint, Amazon Music listing, and ffmpeg inspection | Added SRC-186/C-102. Preserved the 37,721-byte Libsyn page and 24,206,688-byte 31:09.84 stereo MP3 for the 12 October 2025 conversation with Chantelle Jessica Lewis; no public transcript/caption asset was exposed. | Transcribe only if a timecoded thematic pass is selected; do not duplicate the Libsyn/Amazon manifestations as separate interviews |
| 2026-08-06 | SRA Annual Conference 2026 session and post-event report | Official SRA event page, programme, speakers page, post-event report, portrait endpoint, and exact-title/public-video search | Added SRC-188/C-104. The official programme lists Arday’s 4:15–5:00 session “Message in a Bottle” on 8 July 2026; the SRA report summarizes his warning about power structures suppressing critical approaches and researchers. Preserved four HTML pages and the 684×675 portrait; no recording/transcript endpoint exposed. | Retry only if the SRA programme/report changes or a new official recording/transcript lead appears; do not treat the post-event summary as a transcript |
| 2026-08-06 | Forthcoming memoir audiobook edition and media-asset audit | Simon & Schuster US/UK publisher pages, CloudFront cover/photo endpoints, Publishers Weekly catalogue, Audible UK listing | Added SRC-189/C-105. Verified the US audiobook ISBN, narrator, 9:30 runtime, and 11 August 2026 release metadata; preserved a new 3000×3000 cover and deduplicated the existing credited portrait. No public audio sample or audiobook binary exposed. | Retry only after release or a changed publisher/retail media state; do not duplicate the existing memoir publisher record |
| 2026-08-06 | Imperial *Belonging* childhood/source-version and embedded-video audit | Imperial College *Belonging* page, Iframely/Shorthand player, YouTube `YjNQbRKDXbg`, and page image endpoint | Added SRC-190/C-106. Preserved the institutional page, iframe response, and 199×258 portrait. The page adds an age-6/7 “almost sent to a special school” account, spatial-awareness wording, and a speech-at-10 version; the embedded YouTube item is the already-linked *Portrait of a Londoner* video and remains login-required/private. | Retry only if the Imperial page, iframe, or YouTube access state changes; do not duplicate the existing video/audio record |
| 2026-08-07 | Class Central historical catalog manifestation audit | Class Central course/classroom pages, rendered classroom iframe, YouTube `5_TBclFeDWg`, and comparison with Imperial `YjNQbRKDXbg` | Added SRC-445. The catalog exposes a distinct YouTube ID for the same-titled “Expect the unexpected” item; direct YouTube inspection returned “This video isn’t available anymore.” No binary, thumbnail, captions, or transcript was recovered, and the distinct Imperial video was not merged with it. | Revisit only if the Class Central/YouTube record changes or a new archived binary appears; do not treat the unavailable historical ID as proof that the Imperial manifestation is deleted |
| 2026-08-06 | Historical school search follow-up and EuHu educational-resource capture | Exact-name school queries, Southfields/Heathbrook archive searches, EuHu/Amazing People Schools page and Builder metadata | Added SRC-191/C-107. No new school-held attendance record surfaced. Preserved EuHu’s public educational biography, whose metadata dates first publication to 17 May 2025 and update to 30 July 2026; it repeats age-11/18 and two-GCSE wording and adds shop-work and bedroom-wall formulations. | Keep Southfields/Heathbrook attendance unresolved; retry only with a historical school archive, school-held record, or direct first-person source. Do not count EuHu as independent corroboration. |
| 2026-08-06 | Royal Society committee-host verification | Royal Society profile, current Diversity and Inclusion Committee page, exact-name committee search | Added SRC-192/C-108. The first-party committee page directly lists Jason Arday as a member and confirms a current Royal Society governance/committee record; this is distinct from the unresolved RSA fellowship and CLASS panel claims. | Keep the RSA/CLASS host-record boundary open; do not rerun the Royal Society committee URL without a changed page or new term information |
| 2026-08-06 | Cambridge anti-racism symposium event capture | Cambridge Black Advisory Hub announcement and linked Homerton event page | Added SRC-193/C-109. The Cambridge announcement lists Professor Jason Arday as a practitioner-workshop leader for the 14 April 2026 symposium; the announcement and separate Homerton HTTP 403 response are preserved locally. No recording, transcript, or post-event delivery evidence was exposed. | Retry only if the Cambridge/Homerton pages change or a new official recording/transcript appears; do not infer workshop content from the announcement |
| 2026-08-06 | Cambridge Faculty course-team and Global Justice Collective host audit | Education Policy MPhil course page, indexed GJC page, current Faculty GJC URL, and older Faculty OER URL | Added SRC-194/C-110 for the live Education Policy course-team listing. Added SRC-195/C-111 for the indexed GJC member listing and preserved both current 404 states; no current GJC membership is claimed. | Retry GJC only if a replacement/current Faculty research-group page appears; do not repeat the Education Policy capture without a changed page version |
| 2026-08-06 | Cambridge Festival source upgrade and Surviving Society podcast capture | Cambridge Festival programme/report/pages/image; Apple episode page, RSS enclosure, SoundCloud episode page/oEmbed/artwork, and public media endpoints | Upgraded SRC-062 with the official 2024 programme PDF, report PDF, three page snapshots, event image, and the explicit Cambridge 105 audio boundary. Added SRC-196/C-113 with a local 36:33.32 MP3 for the Social Science for Social Justice episode and SRC-197/C-114 with the Growing up Black in the 90s page/artwork and SoundCloud 401 boundary. | Search only for a changed Cambridge 105/SoundCloud media state or a new transcript; do not duplicate the Cambridge Festival event or Surviving Society manifestations |
| 2026-08-06 | Research Cast UK and Surviving Society E188 capture | Bishop Grosseteste/University of Lincoln Research Cast page and direct MP3; SoundCloud E188 page, oEmbed, artwork, and progressive endpoint | Added SRC-198/C-115 with a locally preserved 44:47.54 MP3 and SRC-199/C-116 with the E188 page/artwork and HTTP 401 audio boundary. | Transcribe SRC-198 only as a timestamped follow-up; retry E188 only after a changed SoundCloud media state or new transcript; do not duplicate the Surviving Society series records |
| 2026-08-06 | Research Cast UK timestamped ASR pass | Local SRC-198 MP3, Whisper `base.en` model, generated JSON segments, and targeted term/time-window review | Preserved the 219,055-byte ASR JSON. Added C-117 for Arday’s account of an early educator’s influence and C-118/C-119 as bounded audio leads on family NHS work and sport/community; no claims were promoted beyond what the audio/ASR supports. | Manually listen to C-117–C-119 before tightening names or family-occupation wording; do not treat the ASR JSON as a verbatim transcript |
| 2026-08-06 | UKRI Gateway to Research EDICa project verification | UKRI GtR indexed result for Jason Arday, direct person URL, and local HTML capture | Added SRC-200/C-120. The indexed official result associates Arday with the £3,637,057 ESRC-funded EDICa award (Jan 2023–Dec 2026); direct fetch rendered “Kevin Wilson,” so the mismatch is preserved as an access anomaly. | Recheck only after a changed GtR state or a new official project record; do not treat the mismatched HTML as direct confirmation |
| 2026-08-06 | Childhood-source expansion: Georgian exam booklet and earlier St Mary’s magazine manifestation | NAEC 2025 English exam PDF; St Mary’s *Simmarian* issue 20 PDF; exact-name and childhood/school/sports search queries | Added SRC-201/C-121 for the derivative exam passage; upgraded SRC-147/C-060 with the 2008 issue 20 local PDF as an earlier manifestation of the same charity-football event. No new school register or sports-career record surfaced. | Keep the NAEC passage derivative; do not rerun the same exact-name school/sports search without a new lead, archived school record, or changed host page |
| 2026-08-06 | OpenAlex residual scholarly-output pass: football chapter preview | OpenAlex DOI audit; Routledge catalogue; PagePlace public preview; local PDF extraction and visual contents-page check | Upgraded SRC-026 with a locally preserved 22-page preview. The contents page locates Arday’s chapter at printed pages 165–173; no chapter text was exposed. No new DOI-level work was found. | Continue only with a newly surfaced older-encyclopedia/book manifestation or changed publisher/repository state; do not rerun this preview endpoint without a state change |
| 2026-08-06 | Institute for Equity 2025 conference programme capture | Final and draft programme PDFs, Institute for Equity host-domain search, exact-title/public-video search | Added SRC-202/C-122. Final programme lists Arday as a 15:35–16:10 keynote on 27 June 2025; draft/final date and schedule differences are preserved. No recording, transcript, slides, or delivery evidence surfaced. | Retry only if the host exposes a post-event page, recording, transcript, or changed programme state; do not treat the programme as proof of delivery |
| 2026-08-06 | Crossref exact-author scholarly-output audit | Crossref `query.author=Jason Arday` API response; local exact-name filter; normalized DOI comparison against all source records | Added SRC-203. The 200-item ranked response yielded 47 DOI records with an Arday family name and Jason given name; all matched existing records, with one teacher-education DOI spelling variant. Unrelated Arday-name authors remain excluded from the biography. | Reopen only after a changed Crossref result, new DOI lead, or publisher/repository record outside the existing registry; do not rerun the same ranked query without a state change |
| 2026-08-06 | Crossref 2026 date-filtered scholarly-output recheck | Crossref `query.author=Jason Arday` with 2026 publication-date filter; local exact-name filter; DOI comparison against the registry | Updated SRC-203 in place. The 100-item ranked response yielded two exact-name records, OSF v1/v2 of the already canonicalized narrative-inquiry study; no new DOI/title key surfaced. False matches and ranked-response limits are preserved. | Keep the 2026-only slice closed for this capture date; reopen only with a changed result, concrete DOI, or publisher/repository lead |
| 2026-08-06 | St Mary’s Olympic-torch record | St Mary’s *Simmarian Online* Edition 5, PDF extraction, checksum verification, and visual inspection of page 2; fresh exact-name childhood/sports search | Added SRC-204/C-123. The contemporaneous 2012 magazine identifies Arday as a former Athletics Union President and reports his 23 July Olympic-torch relay in Merton; the page photograph was extracted locally. This adds a dated public milestone but does not resolve the football/snooker claims. | Keep the torch appearance separate from the sports-career evidence; reopen the football/snooker search only with a named club/tour, contemporary record, or new first-person source |
| 2026-08-06 | Memoir rights-catalogue family-count version audit | BGA/Simon & Schuster Spring 2026 rights catalogue, local PDF capture and visual inspection of page 82; comparison with Guardian and NAEC records | Upgraded SRC-020 and added C-124. The catalogue says “second youngest of three boys,” conflicting with the four-brothers wording in the Guardian and derivative Georgian exam passage. The catalogue PDF and checksum metadata are now local. | Preserve the count discrepancy; do not infer family composition from repeated marketing or derivative educational prose; revisit only if the memoir text or a direct family account becomes accessible |
| 2026-08-06 | University of Bristol CHET seminar capture | University of Bristol event page, HTML/image endpoints, local snapshot, checksum, and visual inspection of event graphic | Added SRC-205/C-125. The page records the 4 June 2024 “One to Another” seminar with Arday as speaker and CHET as host; no recording, transcript, slides, or attendance report was exposed. | Retry only if Bristol/CHET exposes a recording, transcript, slides, or post-event report; do not duplicate the distinct November 2024 Graceland lecture |
| 2026-08-06 | Queen’s University Belfast 2019 seminar-visit capture | QUB Pure activity page, listed attachment metadata, direct retrieval, and in-app-browser attachment checks | Added SRC-206/C-126. QUB records Arday’s 8–9 November 2019 Durham-based visit for a seminar and network activities; the listed PDF and DOCX are preserved as Cloudflare challenge boundaries, not claimed binaries. | Retry only after QUB exposes a changed attachment state or a mirrored institutional copy; do not infer seminar content from filenames or attachment classifications |
| 2026-08-06 | *The Bookseller* memoir-interview source-version upgrade | The Bookseller search-index results, two article paths, in-app-browser login redirect, and direct shell retrieval | Upgraded existing SRC-131 and added C-127. The indexed excerpt adds Giff/name-origin and memoir-production context plus Arday’s framing of the “underdog” narrative; the full article remains login-gated and the direct request returned HTTP 429, preserved locally. | Retry only after a changed access state or a licensed/public mirror; do not treat the indexed excerpt as a full interview or independent corroboration |
| 2026-08-06 | *The Bookseller* indexed memoir continuation | Current search-index rendering of the same June 2026 author interview; direct shell request still HTTP 429 | Added C-171. The bounded continuation says Arday left secondary school with two GCSEs and was admitted by a college course leader named Sandro to a BTEC sport course despite his qualifications; this overlaps with the Merton/Sandro record without replacing it. | Keep the full article login-gated and the excerpt bounded; seek a college archive, dated first-person interview, or examination/attendance record before treating the education transition as independently verified |
| 2026-08-06 | UCL 2025 event-biography affiliation witness | UCL Arts and Humanities event search result; direct page request and Cloudflare response | Added SRC-221/C-172. The 23 January 2025 event listing supplies a dated institutional biography that still uses present-tense Runnymede trustee wording and repeats several unresolved visiting/honorary affiliations; preserved its 403 body and headers without treating the indexed text as a full page capture. | Compare only against a new direct host/legal record or a materially changed UCL page; retain the present-tense wording as a dated source-version and do not infer current status from it |
| 2026-08-06 | Memoir catalog manifestation and local preservation | Google Books edition page/HTML, cover endpoint, publisher page comparison, Google Books Books API | Upgraded SRC-145 and added C-182. Preserved the 97,671-byte Google Books HTML response and 128×197 cover thumbnail for the distinct 27 August 2026 UK edition; catalog synopsis adds a “two brothers” family-count witness and repeats age-three/11/18 milestones. The same-volume Books API returned HTTP 429 quota exhaustion, preserved as an access boundary rather than a missing record. | Keep edition records separate and preserve the family-count discrepancy; retry Google Books only after a changed endpoint/quota state or new preview exposure |
| 2026-08-06 | SRC-211 English-host bibliographic reconciliation | Durham person-page and department-of-sociology indexed results; direct orgunit endpoint; Crossref and OpenAlex English-title queries; comparison with IUF and Steinmetz volume witnesses | Added C-183 and upgraded SRC-211. The indexed Durham variants conflict on publisher (“France: Springer” versus “USA: Information Age Publishing”) while retaining the English host title *A World History of Sociology*; La Découverte’s 2024 French-volume hypothesis remains separate. Direct endpoint returned Cloudflare 403; Crossref returned no exact host volume in its ranked results and OpenAlex returned related works only. | Keep the chapter unresolved; retry only with a direct publisher/library record, DOI/ISBN, archive, or changed Durham endpoint. Do not choose a host volume from search-index metadata alone |
| 2026-08-06 | Associated Press resignation/investigation report and image capture | AP article page, article HTML, image URL, and checksum/technical inspection | Added SRC-207/C-128. AP independently records the resignation and Cambridge investigation announcement, preserves attributed positions and allegations, and provides a 2305×1534 AP/PA Olympic-torch image that is deduplicated as a higher-resolution manifestation of the existing 2012 event. | Recheck only after a formal Cambridge/Jesus/LJMU outcome or a changed AP article; do not convert AP’s attributed allegations into findings |
| 2026-08-06 | Post-resignation Cambridge Faculty profile changed-state audit | Live Cambridge Faculty profile with and without trailing slash, Cambridge notices index, and current statement URL; compared against SRC-168 and SRC-093 captures | Added SRC-208/C-129. Both Faculty profile URL forms now return HTTP 404, while the notices index and statement remain live; preserved both 404 bodies and live institutional pages. | Retry only after a replacement Faculty profile, redirect, or formal Cambridge outcome; do not infer why the page disappeared or that every listed role ended |
| 2026-08-06 | Primary-text research-integrity evidence and reproducibility capture | *Analyse That* thesis-overlap analysis, 185-pair appendix, replication script/ZIP, Arday’s local 2015 thesis, and Brunel’s 2009 comparator thesis | Added SRC-209/C-130. Preserved the public computational analysis and underlying comparator document; recorded its reported overlap statistics, disclosure, limitations, and explicit non-adjudication boundary. | Run an independent reproduction only if selected as a dedicated audit; otherwise await formal Cambridge/LJMU/journal outcomes. Do not convert textual derivation measurements into a misconduct finding |
| 2026-08-06 | Sage Social Science Space interview and binary capture | Sage page/transcript, YouTube video `Yu5fr69h32o`, automatic English captions, oEmbed metadata, thumbnail, and ffmpeg inspection | Added SRC-210/C-131. Preserved a 27:18.56 640×360 H.264/AAC video and transcript-bearing publisher page. The item documents Arday as interviewer and series-editor as stated by Sage; timecoded self-description and evaluative comments are separately qualified. | Continue bounded publisher/video discovery only from new series pages or changed endpoints; do not duplicate the video under its YouTube and Sage URLs |
| 2026-08-06 | 2015 Runnymede School Report full-text reconciliation | OpenAlex residual work, University of Manchester Research Explorer record, alternate `pure.manchester.ac.uk` PDF endpoint, `pdfinfo`, and page-level text extraction | Upgraded SRC-105 and added C-132. The 61-page open PDF confirms the report’s ISBN, August 2015 Runnymede publication, three editors, co-edited introduction on printed pp. 4–5, and Arday’s pp. 48–50 mentoring/teacher-training chapter; local PDF preserved. | Continue the OpenAlex residual queue only with another concrete older manifestation or changed publisher/repository state; do not count this as a new duplicate work |
| 2026-08-06 | Older scholarly full-text upgrades: educational leadership and mental-health staff article | Greenwich Academic Literature Archive AAM, Sage published PDF metadata, German National Library accepted manuscript, PDF extraction, and checksums | Upgraded SRC-048 and SRC-049; added C-133/C-134. Preserved a 21-page leadership AAM and a 24-page *No one can see me cry* accepted manuscript. Extracted dated guest-editor/role wording and reported methods/sample while keeping version and current-status boundaries explicit. | Seek only genuinely new publisher versions or repository copies; the 2020 social-mobility PDF remains a publisher 403 boundary and should not be rerun without a changed endpoint |
| 2026-08-06 | 2018 educational-leadership article full-text upgrade | University of Roehampton repository record, accepted-manuscript PDF, `pdfinfo`, text extraction, and checksum | Upgraded SRC-027 and added C-135. Preserved a 16-page accepted author manuscript and extracted its collective-biography method, three-participant scope, and three-UK-institution boundary. | Seek only the published version or a newly exposed repository state; do not create a second work record for the accepted manuscript |
| 2026-08-06 | 2020 *Trying to Break the Monopoly* chapter publisher reconciliation | Bloomsbury official book metadata, Durham indexed chapter record, direct publisher request, Cloudflare response headers/body | Upgraded SRC-079 and added C-136. Publisher metadata confirms the 2021 book, ISBN, chapter 4 title, and Arday/Dunham contribution; direct publisher retrieval returned Cloudflare HTTP 403, preserved locally. No authorized full text captured. | Retry only after a changed publisher access state or authorized repository copy; do not use unofficial mirrors or infer chapter text from search snippets |
| 2026-08-06 | Springer encyclopedia mental-health chapter reconciliation | Springer official chapter pages and metadata for DOI `10.1007/978-981-13-1179-6_396-1` and `10.1007/978-981-16-8679-5_396`; Crossref query; Durham 2019 output lead; legacy Springer URL check | Upgraded SRC-073 and SRC-180 and added C-137. Springer confirms Arday’s chapter title, *Encyclopedia of Teacher Education*, 2020 pp. 1–6 and 2022 pp. 1064–1069. The previously linked `10.1007/978-981-287-532-7_478-1` resolves to an unrelated Wozniak chapter; corrected and preserved as a disproven link. PDF routes redirect to institutional authentication, so no full text is claimed. | Retry only after an authorized repository copy or changed publisher access state; do not treat the Durham working title as a separate work or use the disproven Springer URL |
| 2026-08-06 | Bloomsbury race/leadership title-variant reconciliation | Crossref exact-title/author query, current Bloomsbury catalogue search result, prior canonical SRC-177, Durham title lead, direct current Bloomsbury request | Upgraded SRC-075 and SRC-177 and added C-138. Durham’s “Where do we start?” wording is retained as a source-version lead and linked to the canonical DOI chapter; Bloomsbury’s current 2020 catalogue record lists the same chapter under ISBN 9781350198791. Current publisher retrieval returned Cloudflare HTTP 403, preserved locally. | Retry only after a changed publisher state or authorized chapter copy; do not create a duplicate work record or infer chapter text from the title |
| 2026-08-06 | Routledge *Mental Wellbeing in Schools* chapter upgrade | Routledge live book page, Crossref DOI metadata, Durham repository citation, direct cover image | Upgraded SRC-025 and added C-139. Routledge lists Arday and Laura Morton as chapter 2 authors; Crossref supplies pp. 7–22 and 3 May 2022 chapter publication metadata. Preserved publisher HTML, headers, cover, and Crossref JSON; no chapter text captured. | Retry only after an authorized chapter copy or changed publisher access state; do not infer empirical findings from the title or contents listing |
| 2026-08-06 | *Doing Equity and Diversity* host-volume and BAME-leadership chapter audit | Springer official book page, Durham chapter-list lead, Kent repository book record, local cover and headers | Upgraded SRC-038/SRC-081 and added C-140. Springer confirms the 2021 edited volume, Arday/Thomas editorship, 25-chapter book structure, and ISBN/DOI family. The captured publisher page did not expose the Durham-only BAME-leadership chapter title, DOI, or pages; those fields remain open. | Retry only after a chapter-level publisher page, authorized repository copy, or changed book TOC; do not infer chapter authorship/pagination from the host-volume record |
| 2026-08-06 | Durham residual book-chapter lead: “Decolonising higher learning education in the UK” | Durham indexed book-chapter search result, exact-title search, Crossref bibliographic query, direct Durham request | Added SRC-211/C-141. The indexed result names Arday, Dufoix/Mosbah-Natanson, and Springer, but no date, exact book title, DOI, ISBN, pages, publisher page, or full text was found. Direct Durham retrieval returned HTTP 403; body and headers preserved. | Reopen only with a publisher/library/DOI/archived bibliographic resolution or changed Durham access; do not create a full publication record from the index lead alone |
| 2026-08-06 | SRC-211 exact-title bibliographic boundary pass | Open Library API, Crossref works title query, Google Books API, Durham indexed result, IUF profile, and Steinmetz CV | Added C-173 and three local API responses. Open Library returned zero results, Crossref exposed no exact title in its ranked response, and Google Books returned quota exhaustion; no chapter-level identifier was found. | Keep the Durham/Springer lead and La Découverte volume witnesses unresolved; seek BnF/Sudoc, ISBN, publisher, or archive evidence rather than repeating the same API calls |
| 2026-08-06 | Childhood/adolescence interview expansion | New Humanist *With Reason* transcript, 15 December 2020 | Added SRC-223/C-176–177 and preserved the 97,622-byte host HTML. This is a dated first-person source for Clapham/council-estate upbringing, 1990s age framing, music/guitar, protests with his mother, and reported adolescent police stops; no audio endpoint was exposed | Keep the transcript as an attributed testimony source; seek only a new contemporaneous family, school, police, or audio record for corroboration |
| 2026-08-06 | Channel 4 podcast binary capture | Apple listing, Spotify/Anchor episode page, CloudFront MP3 endpoint, artwork endpoint, local media inspection | Added SRC-224/C-178. Preserved the 603,325-byte page, 45,286,877-byte MP3, and 400×400 artwork. The programme description adds the 2012 PE-teacher goal-list lead; no transcript/captions exposed | Keep the goal-list claim as programme copy/self-report; manually transcribe or listen to the local audio before adding timecoded substantive claims |
| 2026-08-06 | *Talking Matters* sports excerpt preservation | Locally preserved episode MP3, Whisper-small SRT navigation, `ffmpeg` stream-copy extraction, file inspection, and SHA-256 checksums | Updated SRC-184 and C-149/C-150. Preserved 00:19:00–00:20:25 football and 00:20:15–00:21:20 snooker excerpts with parent hash and child hashes; no independent Crystal Palace, ranking, tournament, or match record surfaced in the bounded sports search | Human-listen to the two short excerpts before refining wording; otherwise reopen only with a new named club/tour/archive record or changed source state |
| 2026-08-06 | Precarious-employment article full-text reconciliation | Taylor & Francis DOI metadata, University of Glasgow accepted-manuscript PDF, Crossref response, and Durham 2020 submitted-manuscript record | Upgraded SRC-051 with a 22-page accepted manuscript and added C-179. Linked SRC-067 as a provisional earlier-version candidate because author, journal, and topic align, but kept the records separate pending direct manuscript comparison | Treat SRC-051 as the canonical published work; preserve SRC-067 as a distinct submitted-manuscript version and do not merge without its full text or a stronger publisher/repository statement |
| 2026-08-06 | *Decolonizing University Teaching and Learning* mirror state recheck | Indexed TransReads lead, earlier 404 capture, and later header-only request | Updated SRC-079 and the negative-space ledger: the unofficial mirror changed from an earlier HTTP 404 to a later HTTP 403 response. No mirror body or copyrighted PDF was downloaded; Bloomsbury’s official metadata remains canonical | Retry only after a changed official publisher/repository state or authorized preview/full text; do not use the unofficial mirror |
| 2026-08-06 | WNYC/GBH *The Takeaway* interview capture | WNYC first-party page/transcript, direct Podtrac-resolved MP3, response headers, and local media inspection | Added SRC-275/C-250–C-251. Preserved a 15:56.13 MP3 and the transcript-bearing page; extracted a distinct first-person account of diagnosis, nonverbal experience, observation, and reading age at the University of Michigan while keeping host narration and transcript-revision boundaries explicit | Verify exact quotations against the local audio before quoting; use this source as a distinct media manifestation and do not count its repeated milestone narration as independent medical or school corroboration |
| 2026-08-06 | Full-text upgrade for “The routes to intellectual authority in a prior colonial empire” | Queen’s University Belfast Research Portal publisher PDF, DOI metadata, PDF extraction, and licence/page inspection | Upgraded SRC-017 and added C-252–C-253 without creating a duplicate DOI work. Preserved the 29-page publisher/version-of-record PDF and headers; confirmed final citation, CC BY-NC-ND status, HESA dataset size, methodology pages, and discussion/conclusion page range | Keep the PDF as the canonical local manifestation of SRC-017; do not create a second article record or treat the study’s structural findings as personal biography claims |
| 2026-08-06 | ABI 2025 conference and affiliation-witness audit | ABI indexed speaker-profile variants, ABI Annual Conference 2025 agenda result, direct profile/PDF endpoints, and comparison with Companies House/current host records | Added SRC-225/C-181. ABI’s agenda schedules a 27 February 2025 Arday/Morgan fireside chat; indexed ABI biographies repeat Ohio State, Durham/Glasgow, Runnymede, BSA, CLASS, NHS RHO, and ITV wording. All direct ABI endpoints returned 403, so profile text remains indexed source-version evidence and the agenda remains an event-programme witness without a local PDF. | Keep the ABI biography as dated host-published wording, not appointment proof; seek a changed ABI endpoint or direct Ohio State/CLASS/Coventry record before upgrading unresolved affiliations |
| 2026-08-06 | Competing volume-level witnesses for SRC-211 | Institut Universitaire de France Dufoix profile; University of Michigan-hosted George Steinmetz CV; local HTML/PDF captures | Added SRC-213/C-143 and SRC-214/C-144. IUF describes the Dufoix/Mosbah-Natanson project as an expected La Découverte publication; Steinmetz cites a 2024 La Découverte volume *Une histoire mondiale de la sociologie*. This conflicts with Durham’s Springer field but does not identify Arday’s chapter or establish its publication. | Search La Découverte, national library/catalogue, ISBN, chapter-level DOI, and archived publisher records; preserve SRC-211 as unresolved until chapter identity is explicit |
| 2026-08-06 | University of Bath interview revision and sports correction | In-app browser rendered the current Bath page; shell retrieval continued to return 403; page-level correction notice | Added SRC-215/C-145 and revised C-008/C-009/C-011/C-062. The current page says semi-professional football and non-professional snooker, and explicitly corrects the original professional-level wording. It also preserves first-person schooling, family, stop-and-search, music, and Sandro Sandri material. | Prefer the corrected Bath version when summarizing that source; preserve earlier BBC/Lives Retold and original Bath formulations as source-version history; named club/tour and independent sporting records remain open |
| 2026-08-06 | NFDA 2024 convention programme recovery attempt | Indexed NFDA registration PDF result, canonical PDF URL, direct curl retrieval, local file inspection, and SHA-256 capture | Added SRC-226/C-185 and media/timeline entries. The indexed official witness schedules Arday’s 23 October 2024 closing session; the live URL returned a 114,139-byte NFDA Page Not Found HTML response, preserved locally; no PDF, recording, transcript, or slides recovered | Retry only if NFDA restores the PDF or exposes a convention archive/recording; retain the event as scheduled-programme evidence, not proof of delivery |
| 2026-08-06 | TechLearn 2025 keynote binary preservation | Training magazine/TechLearn brochure and event guide URLs, PDF extraction, page inspection, and SHA-256 checksums | Added SRC-227/C-186. Preserved 13-page brochure and 20-page event guide for the same 7 October 2025 keynote; extracted title, schedule, subject, and programme biography; no recording, transcript, or slides exposed | Keep the two PDFs as one canonical event with separate manifestations; seek a recording or post-event host report only if a new endpoint appears |
| 2026-08-06 | Sheffield Hallam ASPIRE keynote capture | Sheffield Hallam post-event report, direct HTML capture, linked cohort photograph, image inspection, and checksums | Added SRC-228/C-187. The host report says the ASPIRE third-cohort celebration featured an Arday keynote; preserved 48,256-byte HTML and 700×394 group image. No recording, transcript, keynote title, or exact event date exposed | Search only for a new ASPIRE/Sheffield Hallam recording or event programme; do not treat the cohort image as an Arday portrait |
| 2026-08-06 | Glasgow Black History Month 2025 event capture | University of Glasgow event page, BookItBee registration page, UNESCO RIELA past-events index, linked event graphic, direct HTML/image retrieval, and visual inspection | Added SRC-229/C-188. Preserved three HTML manifestations and a 565×800 event poster/embedded Arday image; confirmed the 10 October 2025 date, online format, 2:10–3:15 slot, title, and co-participants; no recording/transcript/slides exposed | Keep the event pages as one canonical event; seek a recording or post-event report only through a newly surfaced host endpoint; do not extract the poster photograph as a standalone portrait |
| 2026-08-06 | DECP Annual Conference 2025 programme capture | Indexed DECP session-brochure result, valid static PDF endpoint, PDF extraction, and incorrect guessed-endpoint response | Added SRC-230/C-189. Preserved a 5-page valid brochure scheduling Arday at 10:45 on Day 2 (10 January) with “Talk Title TBC,” plus the guessed URL’s XML response as an access-boundary artifact; no recording/transcript exposed | Keep the programme listing bounded; seek only a final programme, host report, or recording that resolves the title and delivery; do not treat the guessed endpoint as a duplicate source |
| 2026-08-06 | Additional 2025 institutional event sweep | University of Exeter Neurodiversity Celebration Week, Newcastle University public-lecture archive, Reading Blue Coat school report, direct HTML/image retrieval | Added SRC-231–233/C-190–192. Preserved three first-party event/report pages and one Reading Blue Coat event photograph; Exeter explicitly says its workshop was not recorded; no new video, transcript, or slides exposed | Keep these as distinct host records; use them as dated corroboration only. Continue to newly surfaced institutional or media hosts, not the same event pages |
| 2026-08-06 | University of Bath Doctoral Festival of Ideas 2025 recovery | First-party Bath search result, report URL, timetable URL, direct HTTP retrieval, and response hashing | Added SRC-234/C-193. Indexed Bath text records Arday’s keynote “The Name of the Game: Navigating Academia” and its themes; both current Bath URLs returned 404 and are locally preserved as changed-state boundaries; no recording/transcript/slides recovered | Retry only after Bath publishes a replacement report, archive, or media endpoint; do not treat the indexed witness as a recovered full page |
| 2026-08-06 | SEB OED22 programme recovery attempt | SEB resource page, embedded Issuu programme URL, direct HTTP retrieval, and response hashing | Updated SRC-109. The Issuu endpoint returned HTTP 403 with a short denial body; body and headers are locally preserved. The existing YouTube recording remains unavailable and no programme file was recovered | Retry only after SEB or Issuu exposes a changed public endpoint; do not infer the symposium date from the `oed22` slug alone |
| 2026-08-06 | 2026 BBC *Today* broadcast discovery | Social Research Association LinkedIn post, embedded structured metadata, generic BBC *Today* artwork, and BBC Sounds search boundary | Added SRC-235/C-194. The dated post reports an 18 June 2026 appearance by Arday at approximately 1:52 on proposed GCSE-English thresholds for student-loan access; page and generic artwork are locally preserved, but no BBC episode ID/audio/transcript was recovered | Search BBC programme metadata or a changed BBC Sounds endpoint for the 18 June item; do not quote or promote the post’s summary to transcript-level evidence |
| 2026-08-06 | Childhood evidence-map consolidation | Existing childhood, education, memoir, interview, sports, and changed-state records; no duplicate source discovery | Added `childhood-evidence.md` as a resumable synthesis map. It consolidates the current best-supported formulations, source-version conflicts, and explicit upgrade conditions for family, development, speech, literacy, schooling, football, and snooker claims | Use the map to avoid repeating exact-name searches; reopen only on a changed endpoint, direct memoir/recording access, or a named primary record |
| 2026-08-06 | Residual decolonisation-volume discovery boundary | Exact-title web searches for Jason Arday, “Decolonising higher learning education in the UK,” and “A World History of Sociology”; publisher/catalogue-domain searches for La Découverte, BnF, and Sudoc | No new chapter-level record or identifier surfaced. The Durham indexed lead and existing Springer/Information Age/La Découverte conflict remain canonical under SRC-211/SRC-213/SRC-214; generic La Découverte and BnF search results were false positives and were not catalogued | Do not repeat exact-title web searches. Reopen only with a publisher/library identifier, archived Durham record, DOI/ISBN, or changed endpoint |
| 2026-08-06 | Ruling Passions embedded-audio state recheck | Direct Padlet embed fetch for the `9vuzwdgrah4npk4r` asset, response headers, and comparison with SRC-158 | Updated SRC-158/media index. The embed now redirects to a Sheffield Hallam tenant login and exposes no audio URL or attachment; HTML and headers are locally preserved. The WordPress transcript and Spotify episode lead remain canonical | Do not repeat the same Padlet fetch. Reopen only if the host publishes a public attachment, a new RSS/audio URL appears, or the tenant boundary changes |
| 2026-08-06 | YouTube publisher-video sweep and memoir-trailer capture | Existing media URL inventory; YouTube search HTML; oEmbed metadata; Simon & Schuster Books video page/thumbnail; yt-dlp metadata and progressive MP4 download | Added SRC-236/C-212 and a local 48-second 360×640 MP4 plus thumbnail. The official publisher trailer is distinct from Great Big Story and frames the memoir around Arday’s nonverbal/illiterate childhood and rise to Cambridge; no captions/transcript exposed | Continue only with newly surfaced video IDs or changed host states; do not duplicate the Great Big Story, Imperial, Twinkl, or existing event recordings |
| 2026-08-06 | Twinkl video manifestation capture | Existing SRC-090 interview record; official Twinkl YouTube video `rKsIoOo6oDc`; page/thumbnail metadata and progressive MP4 | Updated SRC-090/media index with a distinct 20-second official Twinkl video, local 360×640 MP4, and thumbnail. No new claim was created because the video repeats the existing interview’s promotional framing and self-reported childhood/sports material | Keep it attached to SRC-090; do not create a duplicate source record. Reopen only if captions, a longer cut, or a materially different interview becomes public |
| 2026-08-06 | Diversity Seminar familiarity-video capture | YouTube search discovery; The Diversity Seminar YouTube clip; Max Tchapeyou LinkedIn post; LinkedIn structured metadata, direct MP4, and auto-caption SRT | Added SRC-237/SRC-238 and C-213. Preserved a 67-second YouTube clip, a distinct 1:42 LinkedIn video, and the LinkedIn auto-caption track. The timecoded record concerns Arday’s organisational-diversity commentary, not childhood biography; captions remain machine-generated pending listening verification | Do not duplicate these two manifestations. Human-verify the SRT against the local MP4 before quoting; reopen only if the seminar exposes a longer interview, transcript, or podcast endpoint |
| 2026-08-06 | Channel 4 News video manifestation and caption capture | Official YouTube video `FA78tV8lar8`, yt-dlp metadata, page/headers, thumbnail, progressive MP4, and English/en-orig automatic captions | Updated SRC-224 and added C-214. Preserved a 32:46 640×360 MP4, thumbnail, metadata, page snapshot, and identical 63,107-byte English caption tracks; timecoded childhood/education/goal-list passages are now navigable but not human-verified | Listen/verify selected segments before quoting; keep the audio and video manifestations attached to one canonical interview source |
| 2026-08-06 | University of Cambridge Neurodiversity Celebration Week film capture | Cambridge LinkedIn post, Bitly redirect, official Cambridge University YouTube video `74okc6ENMuY`, yt-dlp metadata, page/headers, thumbnail, progressive MP4, and English/en-orig automatic captions | Added SRC-239/C-215. Preserved a 4:47 640×360 MP4, thumbnail, LinkedIn/redirect/YouTube snapshots, and identical 10,235-byte caption tracks. The film adds first-person autistic-identity and education commentary but no new childhood chronology | Human-verify C-215’s ~02:59–03:55 passage before quoting; retain as a distinct first-party institutional film and do not repeat the childhood search without a changed lead |
| 2026-08-06 | Fresh non-duplicate YouTube media inventory and capture | `ytsearch` passes for interview/keynote/lecture/podcast/neurodiversity; candidate ID comparison against the local media index; official Oxford Physics and The Diversity Seminar uploads | Added SRC-240/SRC-241 and C-216. Preserved a 56:08 Oxford recording and a 59:44 Diversity Seminar interview, each as 640×360 MP4 plus thumbnail, page/metadata snapshot, and identical English/en-orig automatic captions. The Diversity Seminar personal-story segment adds timecoded source versions for C-006/C-007/C-066; Oxford adds a distinct dated institutional lecture record without new childhood chronology | Do not repeat the same ID inventory. Human-verify the Diversity Seminar 05:10–08:30 captions against the MP4; pursue only newly surfaced IDs, changed host states, or unresolved primary endpoints |
| 2026-08-06 | *Flip Your Script* interview capture | Fresh YouTube ID inventory; official Flip Your Script channel metadata; progressive MP4, thumbnail, page, metadata, and English/en-orig automatic captions | Added SRC-242 and upgraded C-178. Preserved a 13:51 640×360 MP4 and 25,345-byte caption tracks. The local caption navigation records the 2012/age-27 parents’ bedroom goal-list account (~01:48–03:10) and family/Sandro passage (~04:33–07:08) | Human-verify against the MP4 before quoting; retain the surviving wall/list as an unresolved documentary target and do not create a duplicate goal-list claim |
| 2026-08-06 | BME ECR Conference keynote capture | Fresh candidate from the deduplicated YouTube inventory; BME ECR Network channel metadata; progressive MP4, thumbnail, page, metadata, and English/en-orig automatic captions | Added SRC-243/C-217. Preserved a 50:15 640×360 MP4 and 90,880-byte caption tracks. The opening host biography is retained as dated conference copy and its affiliation wording remains versioned against the current institutional audit | Human-verify the opening biography against the MP4 before quoting; use this as a dated event record, not current appointment proof, and do not repeat the same ID inventory |
| 2026-08-06 | Speakers Corner interview capture | Fresh unduplicated YouTube candidate `OpxIsfR1qm8`; Speakers Corner description; MP4, thumbnail, page, metadata, headers, English/en-orig captions | Added SRC-244/C-218. Preserved a 9:14 640×360 MP4 and identical 17,304-byte caption tracks. The interview adds timecoded first-person commentary on social progress, constructive disagreement, media responsibility, adaptable education, and belonging; no childhood chronology | Human-verify C-218 against the MP4; retain as a distinct interviewer-hosted media record and do not repeat the same ID search |
| 2026-08-06 | Sheffield Hallam SoTL Spotlight podcast capture | First-party episode page; Spotify episode and embed pages; Spotify metadata; public CDN preview; episode image | Added SRC-245/C-219. Preserved the 20:17 episode listing, 60-second MP3 preview, page snapshots, and image. The episode is described as a conversation with Arday and Sam Coulby about belonging, mattering, and kindness; no transcript or full-audio file was exposed | Retry only if Sheffield Hallam or Spotify exposes a changed full-audio/transcript endpoint; retain the preview as partial access, not a substitute for the full episode |
| 2026-08-06 | Springer *No one can see me cry* version upgrade | Springer open-access article page and PDF for DOI `10.1007/s10734-020-00636-w`; existing accepted manuscript retained as a separate version | Upgraded SRC-049 and C-133; added C-220. Preserved the publisher page and 19-page local PDF, confirming the open-access version, online publication date, issue pagination, author, DOI, and the same reported 40-participant/methodology scope | Compare the publisher PDF and accepted manuscript only when textual/version questions arise; do not overwrite the accepted-manuscript provenance or treat printed pagination as the local file-page count |
| 2026-08-06 | St Mary’s *Made at St Mary’s* profile and honorary-doctorate address capture | First-party alumni page, structured publication/modification metadata, linked YouTube video `fJoj7zQxn4k`, MP4, thumbnail, page, metadata, automatic captions, and five profile/event images | Added SRC-246/C-221–C-222. Preserved an 11:15 official address and image bundle. The page adds host-published 2005–2008 St Mary’s education, Athletics President, and BUCS first-team wording; the address adds caption-navigated first-person remarks about a school sports day at 15 and pivotal support at 18 | Human-verify C-222 and the captioned mentor/parent names against the MP4; keep this address distinct from the 2024 South Bank Colleges video and retain host biography as source-version evidence |
| 2026-08-06 | St Mary’s *Simmarian 2025* PDF capture | St Mary’s alumni magazine PDF discovered through the current alumni-publication search | Added SRC-247/C-223. Preserved the 15-page issue and recorded its brief timeline mention of Arday as a Cambridge alumnus; no new childhood or sports evidence was extracted | Retain as a dated alumni-publication manifestation; do not create a duplicate event or treat the ranking language as independent verification |
| 2026-08-06 | Childhood/schooling/sport exact-name follow-up | Searched current public results for special-school wording, two GCSEs, Pontins snooker, professional-football phrasing, Southfields, and the MEA Amazing People Schools educational retelling; the MEA canonical URL returned HTTP 404 | No new named school, club, snooker circuit, ranking, match, contract, or examination record found. Added the MEA 404 to the negative-space ledger as a low-provenance changed-state lead; existing self-report and correction records remain canonical | Do not repeat these exact-name queries. Reopen only for a changed page, direct memoir/recording access, named club/tour/archive material, or a school/examination record |
| 2026-08-06 | Teacher-education chapter publisher recheck | Official Information Age/Emerald bookstore search result for *Teaching About Social Justice Issues in Physical Education*; direct Emerald page and legacy Information Age URL tested | Upgraded SRC-074/C-096 without creating a duplicate. The official contents witness confirms Arday’s chapter title and p. 187 start; current Emerald retrieval returned 403/Cloudflare, the legacy URL redirected into a protected endpoint, and the DOI still returns 404. Preserved both local access-boundary snapshots | Keep the public preview and contents witness as the canonical bibliographic evidence. Retry only after a changed publisher endpoint, authorized full text, or library/catalogue record resolves the DOI/edition; do not repeat the same URL fetch loop |
| 2026-08-06 | Contemporaneous fundraising report capture | *Tes* archive result for “Marathon re-runs,” published 13 August 2010; local HTML and response headers | Added SRC-248/C-224. The report independently corroborates the intended 30-marathon/35-day Shelter challenge, Arday’s then-age/occupation, and the £250,000 long-term target. It does not establish completion or audited proceeds; the relevant free text is preserved without copying subscription-gated remainder | Keep *Tes*, JustGiving, St Mary’s, and later institutional totals as separate evidence layers. Reopen accounting only for charity filings, archived campaign records, or a new contemporaneous completion report; do not merge the totals |
| 2026-08-06 | BBC *Radical with Amol Rajan* audio capture | Official BBC programme page `m002bt9b`, BBC podcast RSS, non-DRM MP3 endpoint, page/RSS snapshots, and artwork | Added SRC-249/C-225. Preserved the 8 May 2025 episode featuring Arday and Lucy Noakes on Second World War memory and nostalgia. The RSS reports 51:33; the downloaded file probes at 53:17.28 with an embedded ad-break marker. No transcript exposed | Keep this episode distinct from the 2023 *Today* guest-editor programme and 2026 *Today* lead. Manual listening or a public transcript is required before extracting substantive remarks; do not rerun the same RSS/MP3 endpoint without a changed state |
| 2026-08-06 | *Bookseller* changed-state/browser observation and identity false-positive audit | Web research surface rendered the current *Bookseller* article; direct shell retrieval still HTTP 429. A United Response “Jason” life-story page was checked after name-based discovery and excluded because it identifies a different person born in Penzance, raised in St John’s/Newland, with a miner father and Mencap/Penzance history | Upgraded SRC-131/C-127/C-171 from index-only to dated browser-observed evidence without claiming a local article copy; added C-184 for the Debs/Arsenal-brothers wording. Logged the United Response result as a false-positive boundary rather than contaminating the Arday ontology | Preserve the browser-observed *Bookseller* version as link-backed only; seek a changed shell/access state or licensed copy before local capture. Do not revisit the United Response page unless an explicit surname/identity link appears |
| 2026-08-06 | BBC *Today* 2026 identifier follow-up | Current BBC Sounds search for “Jason Arday,” BBC programme search route, and indexed contemporaneous discussion of the GCSE-English/student-loan proposal | Updated SRC-235. The current Sounds search returned known historical Arday programmes but no 18 June 2026 episode identifier; the programme search route returned HTTP 404. Preserved the Sounds HTML and headers as a changed-state boundary | Keep the SRA report as a dated appearance lead; no BBC audio, captions, transcript, or direct episode page is captured. Reopen only with a new identifier, archive/media lead, or changed BBC endpoint |
| 2026-08-06 | *Pride Magazine* childhood and education profile capture | Direct AMP page, structured metadata, article body, response headers, and linked article image | Added SRC-250 without a new claim row. The page provides a locally preserved 25 July 2023 source-version for the age-3 diagnosis, age-11 speech, age-18 literacy, two GCSEs, BTEC route, Boots/Sainsbury’s work, bedroom-wall goal, and Sandro account; most details overlap existing records | Keep the page as a distinct magazine manifestation and image asset. Do not treat its schooling, employment, clinical, or sports wording as independent records; use it to cross-reference existing claims rather than repeat discovery |
| 2026-08-06 | Newcastle lecture image changed-state follow-up | Existing SRC-232 page, named TerminalFour portrait endpoint, fresh page/image response headers, and JPEG validation | Upgraded SRC-232 without creating a duplicate. The previously commented-out image URL now delivers a 1315×882 portrait; page, image, and headers are locally preserved. No recording, transcript, or slides surfaced | Keep the portrait as an associated event asset only; retry the lecture media boundary only after a new recording, transcript, or changed host endpoint appears |
| 2026-08-06 | Charity accounting changed-state capture | Charity Commission full-print records for First Star Scholars UK and Autism Centre of Excellence/Autism Action; Companies House First Star filing history; official accounts PDFs | Added SRC-252/C-227 and SRC-253/C-228. Both Charity Commission pages returned HTTP 200 after the earlier First Star 403 boundary. Captured First Star’s 2024–25 accounts (£132,127 income; £142,162 expenditure; £120,791 net assets; Arday resigned 16 May 2025) and Autism Action’s 2024–25 accounts (£262,970 income; £215,981 donations; £650,736 expenditure; £973,532 net assets; Arday listed as trustee) | These are charity-level filings, not evidence of Arday’s personal fundraising totals. Keep them separate from the 2010 campaign and later £4.5m/£5.5m institutional aggregates; revisit only for a new filing year or campaign-specific record |
| 2026-08-06 | Routledge “Walls can come tumbling down” chapter resolution | Routledge publisher page, PagePlace public preview PDF, Durham indexed lead, cover image, Crossref exact-title query | Added SRC-212/C-142. Publisher contents identify Arday as chapter 12 author; the 47-page preview places the chapter at printed pp. 143–154 and provides handbook front matter/contents. Durham’s title/host-book variant is retained as an alias; no chapter text or Arday DOI was captured. | Retry only after a changed publisher endpoint or authorized full text; do not use the preview as if it contained the chapter body or create a duplicate Durham record |
| 2026-08-06 | YouTube institutional video follow-up | Fresh exact-name candidates `JWNqOrsUU7A`, `760eNGJDs7o`, and `7JIVefToQG0`; metadata, thumbnails, captions where exposed, page snapshots, and public streams | Added SRC-264–SRC-266/C-237–C-239. Preserved three distinct uploads: BILT keynote teaser, Lancaster commentary talk, and Beacon College profile/interview. The BILT upload is related to but not merged with the full keynote; Lancaster is marked commentary; Beacon’s childhood description overlaps existing claims. Video and audio were preserved as separate streams because local muxing was resource-killed. | Do not rerun these IDs. Human-verify captions/content before extracting substantive claims; next video search should use a new query family or changed host state. |
| 2026-08-06 | New YouTube query-family sweep: interview/podcast/childhood/BETT | `ytsearch30` queries for “Jason Arday interview 2024,” “Jason Arday lecture 2024,” “Jason Arday podcast,” and “Jason Arday childhood”; candidate IDs compared against the local registry | Added SRC-267/C-242 for the 10:25 Teachers Talk Radio BETT interview and SRC-268/C-240–C-241 for the 57:40 *Neurodivergent Show* episode. Preserved complete progressive MP4s, captions, thumbnails, metadata, HTML, and headers. The Neurodivergent Show captions provide new navigable first-person source windows for already-known childhood propositions. | Human-verify C-241 against the MP4 before quoting. Do not repeat these IDs. BBC News/GMA results were treated as manifestations of already-known broadcast source families; inaccessible or commentary-only hits remain unpromoted. |
| 2026-08-06 | Bounded institutional-video sweep: panel and OpenLearn education | New YouTube query family for full interviews/keynotes/talks; candidate comparison against local IDs; OpenLearn collection and transcript URL checked directly | Added SRC-269/C-243 for Royal Greenwich’s 2020 Black History Month panel and SRC-270/C-244 for OpenLearn’s 2023 degree-awarding-gap video. Preserved both MP4s, captions, thumbnails, metadata, page snapshots, and headers; OpenLearn’s current page and linked transcript returned HTTP 403 and are preserved as access boundaries. | Do not rerun these IDs or the same transcript URL without a changed state. Human-verify the panel captions if substantive claims are needed; keep the OpenLearn narrator/author attribution unresolved. |
| 2026-08-06 | Host sweep: UCU and Black In Academia | New YouTube candidates from full-interview/keynote search; caption inspection confirmed a Jason reference in the UCU recording and a short Black In Academia response | Added SRC-271/C-245 and SRC-272/C-246. Preserved the 56:40 UCU webinar and 1:05 Black In Academia video with MP4s, captions, thumbnails, metadata, HTML, and headers. Both are dated public-output records; no childhood claims were promoted. | Human-verify the UCU speaker attribution and selected captions before quoting. Do not rerun these IDs; pursue new host/query families only. |
| 2026-08-06 | Manchester Research Explorer source-version upgrade for 2015 Runnymede School Report | University of Manchester Research Explorer page, direct repository PDF, and response headers | Upgraded SRC-105 without creating a duplicate publication or claim. The 61-page PDF’s extracted text matches the existing local Runnymede PDF, while the repository-generated binary checksum differs; preserved the page snapshot, headers, and second PDF manifestation. | Keep both PDF manifestations as provenance records; do not create a new claim unless a future version exposes materially different text, pagination, or contributor metadata. |
| 2026-08-06 | Roehampton source-version and access-state check for 2018 educational-leadership article | University of Roehampton Research Explorer page, linked PDF endpoint, and response headers | Upgraded SRC-027 without creating a duplicate article or claim. The page confirms the accepted-manuscript citation and 18 September 2018 publication date; the direct PDF endpoint returned a Cloudflare HTTP 403, so the existing local manuscript remains the only captured binary and the failed state is preserved. | Do not repeat the same PDF request without a changed endpoint or authorized access; retain the publisher DOI and SAGE record as version-of-record references. |
| 2026-08-06 | SAGE version-of-record access-state check for 2021 educational-leadership article | SAGE article page and PDF endpoints, response bodies, and headers | Upgraded SRC-048 without creating a duplicate article or claim. Both current SAGE endpoints returned Cloudflare HTTP 403; preserved the page/PDF access-boundary bodies and headers while retaining the Greenwich accepted manuscript as the only local binary. | Do not repeat the same SAGE endpoints without a changed state; use the DOI and repository manuscript as the current bibliographic/version pair. |
| 2026-08-06 | Cool Britannia public-preview capture and edition reconciliation | Routledge current record, PagePlace preview PDF, Crossref chapter metadata, Google Books edition records | Upgraded SRC-179/C-090 and the SRC-030 family without creating duplicate chapters or a second book. Captured an 11-page public preview with title/copyright, contents pagination, acknowledgements, and author page; preserved the Routledge/Google Books 91-versus-106-page edition difference as metadata rather than treating it as a contradiction in the work itself. Added C-247 and a qualified first-person family-name witness to the biography. | Do not seek or redistribute the full commercial book; reopen only for a new lawful preview, library record, or changed publisher manifestation. |
| 2026-08-06 | ResearchCGHE presentation recovered as a distinct *No One Can See Me Cry* source-version | Centre for Global Higher Education-hosted 12-page PDF dated 2 July 2020 | Added SRC-273/C-248. The deck names a broader audience than the later article and labels the staff-focused paper forthcoming/under review; preserved it as a presentation precursor/source-version rather than a duplicate article or a new personal-health claim. | Keep SRC-273 and SRC-049 linked but distinct; compare full text only if a future version-history or authorized manuscript makes that relationship materially testable. |
| 2026-08-06 | Leeds CERS “Stand By Me” recording-boundary capture | First-party event page, linked university Zoom endpoint, and response bodies/headers | Added SRC-274/C-249. The event page verifies the 24 November 2021 title/date/speaker/abstract; Leeds returned a Cloudflare 403 to shell capture and Zoom returned a generic 200 shell without media. No video or substantive claim was promoted. | Retry only after a changed Leeds page, new Zoom media endpoint, transcript, or authorized recording access; do not loop the current URL. |
| 2026-08-06 | SRC-106 repository/PDF access audit | Durham formatted-PDF endpoint, Liverpool Repository indexed accepted-manuscript record, and direct retrieval attempts | Upgraded SRC-106 without creating a duplicate claim or work. Durham’s PDF returned a reproducible HTTP 403 Cloudflare challenge; Liverpool’s record identifies a CC BY-NC-ND accepted manuscript but direct retrieval failed with 406/connection reset. Preserved the Durham boundary and kept the Liverpool manuscript as an unrecovered access lead. | Do not repeat the same Durham/Liverpool retrieval loop without a changed endpoint or authorized access; use the DOI record and current metadata as the bibliographic witness. |
| 2026-08-06 | RSC Inclusion and Diversity Forum 2025 capture | Official RSC event report, official YouTube ID `JbyQlddjUJ8`, local HTML/headers, and 13:24 MP4 | Added SRC-276/C-254 and preserved the full public recording; no substantive claim extracted before manual timecoding | Review the local MP4 for Arday’s segment; do not rerun the same YouTube-ID search |
| 2026-08-06 | Upgrade sports-record search with News24 profile | Current News24 page and its credited CDN image; prior SRC-151 search audit | Added SRC-277/C-255 and preserved the 2018 Battersea Park Rangers image as a dated visual witness. It does not resolve professional-status or club-history questions. | Seek the underlying Southern Sunday Football League post, club archive, or contemporaneous award record only if a new public endpoint appears; do not treat the caption as independent sports verification |
| 2026-08-06 | Battersea Park Rangers contextual-record capture | Official/current club history and 2020 manifesto | Added SRC-278/C-256; preserved the club’s 1999 founding and 2018 league-title context without claiming an Arday roster link | Keep the club history contextual; reopen only for a roster, award document, or contemporaneous post naming Arday |
| 2026-08-06 | BPR-specific roster/award follow-up | BPR/Pitchero exact-name search, current club news index, Southern Sunday League web-indexed results | No roster, match report, award post, or club announcement naming Arday found; the News24 caption remains the only direct association | Treat this as a documented negative-space boundary; reopen only after a new archive, club post, or league record appears |
| 2026-08-06 | Training 2024 programme capture | Official Training magazine conference programme PDF and event search | Added SRC-279/C-257; preserved a 20-page programme documenting the scheduled Orlando keynote and dated host biography; no recording/transcript found | Keep the event as scheduled unless a post-event report or recording appears; do not promote the host biography’s activity labels to independent facts |
| 2026-08-06 | Live Crossref scholarly-output recheck | Crossref `query.author=Jason Arday` API, 100 ranked results, normalized exact-name DOI comparison against the registry | No new Jason Arday work surfaced. The ranked slice repeated existing canonical works and included unrelated Arday-name authors; the current 100-row slice also omitted an already catalogued CoPICS DOI, demonstrating why the preserved 200-row exact-name audit remains the stronger boundary record. | Do not treat the ranked 100-row response as complete; reopen only for a changed result or a DOI/publisher lead outside the existing registry |
| 2026-08-06 | Quality Strategy Network EDI commentary capture | Official page for “The fragile future of EDI demands bold university leadership,” published 7 January 2026; shell HTML/headers and web-retrieval access state | Added SRC-280/C-258. Preserved the title, date, Arun Verma/Jason Arday byline attribution, subtitle, WordPress metadata, and featured-image metadata. The captured HTML exposes no substantive article body; the research surface returned unauthorized access while shell retrieval returned HTTP 200. | Keep the co-authored argument separate from institutional-affiliation and policy-outcome claims. Reopen only after a changed page state or a lawful body/transcript copy appears; do not treat the subtitle as the full article. |
| 2026-08-06 | House of Lords Youth Unemployment Committee transcript capture | Official Parliament oral-evidence HTML/PDF and committee-report routes; web transcript text accessible, shell retrieval challenged by Cloudflare | Added SRC-281/C-259–C-262. Preserved PDF/HTML/report challenge bodies and headers, while recording the official transcript’s witness block, Durham self-introduction, targeted-partnership/mentoring proposal, national role-model databank proposal, ex-PE-teacher statement, and hidden-curriculum remarks with printed-page/Q references. | Keep the transcript as dated public testimony and a historical role witness. Reopen only if the official endpoints expose a locally capturable transcript or webcast; do not represent the challenge pages as the transcript binary. |
| 2026-08-06 | Cambridge Global Justice Collective changed-host follow-up | Indexed `risk.aws.educ.cam.ac.uk/research/groups/gjc/` membership page; ordinary TLS validation failed due to an expired certificate, and diagnostic insecure retrieval returned a Cambridge-branded 404 | Upgraded SRC-195/C-111 without creating a duplicate. The AWS risk-host manifestation is now preserved as a third removed/currently unavailable page state alongside the Faculty and OER 404s; no current membership is claimed. | Do not repeat the expired-certificate/404 request loop. Reopen only if Cambridge publishes a replacement research-group page or a new authoritative membership record. |

## 2026-08-08 — SRC-131 Bookseller memoir-interview access recheck

Capture: the canonical Bookseller article route changed from the previously preserved HTTP-429 boundary to a 302 redirect into the site’s login flow; the final 200 response is a login page and contains no article body. The redirect chain, final HTML, and headers are preserved.

Decision: upgraded SRC-131 in place. This is a changed access-state manifestation, not a new interview or new biography claim; retain the browser-observed article text as source-version evidence and do not claim a locally recovered article.

## 2026-08-08 — SRC-195/C-111 GJC migrated-host recheck

Capture: the migrated Faculty route, OER AWS route, and risk AWS route were checked again. All returned HTTP 404; the AWS responses were inspected with certificate validation disabled after ordinary TLS failed on the expired certificate. No replacement group page or current membership record appeared.

Decision: upgraded SRC-195/C-111 in place and added the six local 8 August response/header captures. No duplicate GJC source or current-membership claim was created.
| 2026-08-06 | Retraction Watch investigation capture | Article published 27 July 2026 and modified 5 August; direct HTML, headers, and featured image captured | Added SRC-282/C-263–C-265. Preserved the investigative report’s allegations, attributed Cambridge response, reported April BSA-plenary remark, publication-correction discussion, and volatile reader-comment layer without treating any of these as adjudicated findings. | Keep this source separate from primary thesis/correction/institutional records. Reopen only for a new modified article state, direct BSA recording/transcript, or authoritative institutional outcome; do not use reader comments as evidence. |
| 2026-08-06 | Cambridge Faculty “Our People” directory boundary | Direct page-1 HTTP 200 capture after a search-index result appeared to list Arday; locally preserved HTML did not reproduce his name or role wording | Added SRC-283 as a bounded indexed-text/direct-response mismatch. No claim was added; the page does not establish current employment or absence from the full directory. | Do not infer a current-role change from this page alone. Reopen only with a changed directory response, confirmed pagination/API route, or directly rendered entry. |
| 2026-08-07 | Cambridge Faculty “Our People” directory recheck | The same page-1 URL returned byte-identical HTML and headers; the body still did not reproduce Arday’s name or role wording despite a current search-index snippet | Updated SRC-283 in place and preserved the second response files. No claim or new source was created. | Treat this as a repeated unchanged boundary; do not rerun without a changed response, confirmed pagination/API route, or directly rendered entry. |
| 2026-08-06 | OpenAlex author/work recheck | Fresh author `A5048886069` and 200-row filtered works requests; 58 works, 1,136 citations, same 56-work set | Added SRC-284. The citation count changed from the earlier snapshot, but no new DOI/title key appeared; no claim or duplicate work was created. | Keep the dynamic API as a discovery boundary. Continue only through publisher/repository reconciliation or a changed OpenAlex work set; do not treat the unchanged index as proof of completeness. |
| 2026-08-06 | Herald affiliation-denial lead upgraded | Direct article, headers, and 1200×630 featured image captured for the 3 August report; prior record preserved only an inaccessible-page/indexed-text state | Upgraded SRC-123 and added C-266. Glasgow’s attributed denial is now a directly readable journalistic source version, while the separate formal Glasgow professorship and unresolved Ohio State lead remain distinct. | Do not collapse “Professor at Glasgow” and “Visiting Professor at Glasgow.” Reopen only for a Glasgow HR/governance record, a direct Ohio State response, or a materially changed article. |
| 2026-08-06 | Ohio State ODI host-state capture | First-party 27 February 2025 reorganization announcement and local response headers | Added SRC-285/C-267. Preserved the ODI sunset date and service/position-change wording as context for the Ohio State affiliation audit, without treating it as an appointment record. | Keep the host reorganization separate from Arday’s individual role. Reopen only for a direct Ohio State appointment/response record or a changed university archive. |
| 2026-08-06 | Lives Retold/BBC Lent Talk recheck after indexed-text resurfacing | Search results again exposed the transcript text, but a fresh direct request to the canonical Squarespace PDF still returned HTTP 404 with a one-byte body | No new source or claim created; SRC-036’s changed-state boundary remains current and no local PDF is claimed. | Do not repeat the canonical PDF request. Reopen only if the file reappears at a changed URL or a traceable archive/mirror provides the document. |
| 2026-08-06 | Memoir paperback edition capture | bol.com indexed listing for ISBN 9781398542754; direct retailer request returned a 403 challenge, locally preserved with headers | Added SRC-286/C-268 as an edition-level manifestation. The 368-page paperback is kept separate from the publisher’s UK hardcover and ebook; no memoir narrative claim was promoted. | Use the publisher records for bibliographic authority. Reopen the retailer page only after a changed access state; do not treat retailer marketing copy as independent biography evidence. |
| 2026-08-06 | BSA governance post-resignation recheck | Fresh first-party request after the Cambridge/Jesus resignation; page body remained byte-identical and continued to list Arday as a Publications Director, while response headers changed | Upgraded SRC-162/C-069 in place; no duplicate source or new claim created. This preserves a dated BSA host-state observation distinct from Cambridge’s changed pages. | Treat the listing as current BSA public wording on 6 August, not a permanent appointment or future outcome. Reopen after a changed BSA governance page or direct BSA statement. |
# 2026-08-06 — White Rose 2026 book-review capture

Discovery: current web search surfaced the University of Sheffield/White Rose Research Online record for Charlotte White and Jessica Bradley’s review of *We See Things They’ll Never See: Love, Hope and Neurodiversity*.

Capture: the repository page and five-page author-accepted PDF were retrieved directly. The record supplies DOI `10.1080/00071005.2026.2620963`, online publication date 4 February 2026, acceptance date 19 January 2026, and CC BY 4.0 status. Local files and hashes are recorded in SRC-287.

Deduplication: this is a review of the already canonicalized 2025 Lewis/Arday book, not a new book manifestation or independent biography. It is therefore recorded as a distinct scholarly review source and does not create new childhood or literacy claims.

Boundary: the repository metadata labels the publisher version restricted, while the accepted manuscript is downloadable under CC BY 4.0. No publisher PDF was needed or claimed.

# 2026-08-06 — Adult Literacy Trust regulator annual-report capture

Discovery: a current search surfaced the Charity Commission annual-report record for the Adult Literacy Trust (charity number 5172504), whose 2024 accounts were approved on 31 January 2025.

Capture: the regulator-hosted 23-page PDF was retrieved directly. Printed page 13 lists Prof. Jason Arday among the charity’s patrons, and printed page 15 names him in the discussion of patron support for the 2025 strategy. The PDF, derived text, headers, and hashes are preserved in SRC-288.

Deduplication: SRC-288 is a dated regulator-hosted witness for the existing SRC-164 patron record, not a new role or appointment. C-270 records the reporting-cycle evidence without inferring an end date, remuneration, trusteeship, or employment.

# 2026-08-06 — LJMU Black researchers page capture

Discovery: a current LJMU resource page for “Black researchers and professionals” surfaced as a distinct first-party institutional profile, separate from the LJMU bicentenary page already in the registry.

Capture: the page and linked 150×150 portrait were retrieved directly. The page lists Professor Jason Arday, calls him a former LJMU lecturer, and states that he gained his PGCert in Teaching and Learning in Higher Education and PhD in Education at LJMU. Local HTML, headers, image, and image headers are preserved in SRC-289.

Deduplication: SRC-289 is a new host-page manifestation, while C-271 records only its current wording. It repeats or compresses existing qualification and former-lecturer claims; it does not add an independent qualification date, current LJMU appointment, superlative verification, or investigation outcome.

# 2026-08-06 — Cambridge Black awarding gaps forum and outputs capture

Discovery: a fresh Cambridge Black Advisory Hub search exposed the 9 March 2023 “Black awarding gap and decolonisation” forum page, its post-event outputs page, and a linked programme PDF. These were distinct from the already catalogued 2026 Anti-Racism Symposium.

Capture: both HTML pages, the 23-page programme PDF, response headers, and the page’s 1809×642 event illustration were retrieved directly. The programme’s printed page 14 identifies Arday as roundtable chair; the outputs page records the student-led workshop recommendations reported to him and the other participants. The page-level record also states that he was in his first week as Cambridge Professor of Sociology of Education.

Deduplication: SRC-290/C-272 is a historical event/output record, not a duplicate of the 2023 Cambridge appointment biography or 2026 symposium. It adds dated event-role and post-event context but no recording, transcript, or current-employment finding.

# 2026-08-06 — FNAC memoir ebook edition boundary

Discovery: a fresh retailer search surfaced an FNAC catalogue record for a distinct ebook ISBN, `9781668085592`, for *Great and Unfortunate Things*.

Capture: the indexed result supplies the 37 Ink imprint, English EPUB format, Adobe DRM, 11 August 2026 availability date, and edition-level marketing synopsis. Direct retrieval returned HTTP 403 with a DataDome challenge; the body and response headers are locally preserved in SRC-291.

Deduplication: SRC-291/C-273 is an edition/provenance record, not a duplicate of the US/UK publisher manifestations, Google Books record, audiobook, or bol.com paperback. No ebook binary or readable sample was exposed.

# 2026-08-06 — Aevitas literary-agency profile capture

Discovery: a fresh representation/agency search surfaced Aevitas Creative Management’s dedicated Jason Arday client page, distinct from the publisher, retailer, and trade-press memoir records.

Capture: the page and response headers were retrieved directly. It names Jennifer Gates as representative, identifies Arday as a social commentator/presenter/public speaker, and lists *Great and Unfortunate Things* as forthcoming from 37 Ink. The page’s current Cambridge Chair and superlative wording is preserved as agency marketing copy, not independent employment evidence.

Deduplication: SRC-292/C-274 is a literary-representation source-version and does not duplicate the publisher’s memoir record or establish a new academic appointment.

# 2026-08-06 — Black History Month UK event listing capture

Discovery: a fresh event-listing search surfaced Black History Month UK’s page for Arday’s scheduled 27 March 2021 online conversation on tackling racial inequality in higher education.

Capture: the 201,995-byte page, response headers, and linked 800×400 promotional image were retrieved directly. The page’s body and schema identify the 2021 publication/event dates and registration-gated Zoom format. Its promotional biography contains delayed-speech/literacy, five-degree, and £1 million fundraising wording, all retained as attributed event copy.

Deduplication: SRC-293/C-275 is a distinct public event listing, not a duplicate of Arday’s other 2021 talks. No recording, transcript, or independent accounting/qualification record was exposed. The page’s 2026 site branding versus 2021 metadata is preserved as a versioning anomaly.

# 2026-08-06 — Goodreads and Audiobooks.com memoir catalogue audit

Discovery: a fresh commercial/catalogue search surfaced Goodreads’ reader record and Audiobooks.com’s audiobook retailer record for *Great and Unfortunate Things*. Kobo and Audible results were checked against existing ISBN/retailer coverage; Kobo repeats ebook ISBN 9781668085592, while Audible repeats the already captured audiobook family.

Capture: Goodreads HTML and headers were preserved. The page identifies record `242978426`, an expected 11 August 2026 publication, a 288-page hardcover, and a reader review attributed to an Edelweiss+ advance copy. Audiobooks.com HTML and headers were also preserved; it lists a forthcoming unabridged audiobook for 27 August 2026, narrator “TBD,” and a country-availability boundary.

Deduplication and anomaly handling: SRC-294 is a distinct reader-platform record without a reliable ISBN in the captured page. SRC-295 is a distinct retailer record but not a new confirmed audio manifestation; its date and narrator fields conflict with the official publisher record and are retained as catalogue version drift. No audiobook binary or sample was exposed.

# 2026-08-06 — Newcastle University lecture archive capture

Discovery: a fresh institutional-event search surfaced Newcastle University’s archive page for Arday’s 14 October 2025 Black History Month Lecture, “Sign o’ the times.”

Capture: the first-party HTML and response headers were retrieved directly. The page records the lecture title, date, time, venue, booking requirement, and a short description focused on racism and higher education. No recording, transcript, slides, image, or downloadable media were exposed.

Deduplication: SRC-296 is a distinct host event record, not a duplicate of the 2025 Glasgow, Oxford, or other Black History Month listings. Its biography repeats several already-known role claims, including the “former Runnymede trustee for 11 years” wording; those are retained as dated Newcastle host copy and not promoted to independent current-status facts.

# 2026-08-06 — Institute for Equity duplicate check and Newcastle portrait capture

Discovery: the programme search surfaced the already canonicalized Institute for Equity 27 June 2025 conference record (SRC-202), including the same 18-page final PDF and page-level keynote schedule. The exact PDF hash matched the existing local canonical asset, so no duplicate source or binary was created.

New asset: the Newcastle University lecture page’s linked image endpoint was retrieved directly and preserved as a 1,315×882 JPEG portrait with response headers. It is attached to SRC-296 and the media index as a page-linked image. The page does not expose photographer, date, license, or recording metadata; those fields remain unknown.

# 2026-08-06 — Educational Philosophy and Theory correction capture

Discovery: a publisher-focused scholarly search surfaced Taylor & Francis’ correction DOI `10.1080/00131857.2024.2350203`, published online 16 May 2024, for Arday, Belluigi, and Thomas’s *Attempting to break the chain* article.

Capture: the publisher’s indexed full-text result supplied the correction’s target article, page 619, amendment scope, and two added references. Direct `/doi/full/` and `/doi/pdf/` retrievals returned Cloudflare HTTP 403 challenge HTML; both challenge bodies and headers, plus accessible Crossref JSON metadata, are locally preserved.

Deduplication: SRC-297 is a correction/source-version record linked to SRC-045, not a duplicate article or a new research work. It is retained as editorial provenance and does not by itself adjudicate research-integrity questions. Crossref’s 11 May 2024 date and the publisher’s 16 May 2024 date are both recorded.

# 2026-08-06 — African Allied Healthcare Summit keynote listing

Discovery: a fresh event search surfaced the African Allied Health Network’s official 23–24 July 2026 summit site and speaker page. The home page places the event at the Cedi Conference Centre, University of Ghana, Legon, Accra; the speakers page lists Arday as a keynote speaker.

Capture: official home, speakers, and schedule HTML plus headers were preserved. A separate public LinkedIn post by Lynn Dadzie-Yeboah promotes Arday for the summit and exposes a poster and auto-captions. The requested LinkedIn MP4 returned HTTP 403 `deny-InvalidToken`; the body and headers are retained as an access boundary. The organizer-linked portrait was captured as a page-linked WebP.

Deduplication and evidence handling: SRC-306 is a distinct organizer/event record, not a duplicate of earlier Arday keynote listings. The record supports a public invitation/listing only; delivery, attendance, keynote content, and any post-event recording remain unresolved. Promotional childhood/literacy wording in the LinkedIn captions is attributed host copy and is not promoted to independent biography evidence.

# 2026-08-06 — BME ECR Conference keynote promotion and video capture

Discovery: a fresh event search surfaced the BME ECR Network’s tenth-anniversary conference at King’s College London on 10 July 2026. The public event listing identifies a keynote address by Jason Arday; the network’s LinkedIn post promotes the same keynote and exposes a public vertical video.

Capture: the event listing and LinkedIn HTML plus headers were preserved. The LinkedIn MP4 returned HTTP 200 and was downloaded locally with its poster; the event page’s 1200×630 banner was also captured. No captions or post-event report were exposed.

Deduplication and evidence handling: SRC-307 is a distinct event/social-media manifestation, not a duplicate of the SRA, BSA, UAL, or African Allied listings. The MP4 is classified as promotional media, not evidence that Arday delivered the keynote. Cambridge affiliation wording remains dated host copy and is not promoted to current-role evidence.

# 2026-08-06 — TechLearn 2025 programme capture

Discovery: an official TechLearn/Training Magazine PDF search surfaced the 2025 event guide and conference brochure. Both documents schedule Arday’s “All Together Now: The Impact of Technology on Learning and Neurodivergence” keynote for 7 October 2025, 9:45–11:00 a.m., in New Orleans.

Capture: both first-party PDFs, response headers, and extracted text were preserved locally. The event guide provides the longer session description and the brochure supplies a distinct programme manifestation. SHA-256 checksums are recorded in SRC-308.

Deduplication and evidence handling: SRC-308 is a programme/document record, not a new media appearance or publication. It establishes the scheduled session and advertised title/description only. Host biography and childhood/literacy wording remain attributed promotional copy; delivery, attendance, and keynote content remain unresolved.

# 2026-08-06 — Jack Petchey Speak Out Challenge journalism capture

Discovery: a search for dated public-facing judging and youth-speaking appearances surfaced an *Enfield Dispatch* report published 16 July 2025 about the Jack Petchey Speak Out Challenge grand final. The article identifies Arday as a judge and attributes a remark about winner Adam Ravat’s confidence and delivery to him.

Capture: the article HTML, response headers, linked 799×533 JPEG, and image headers were preserved locally with checksums. The article’s structured metadata gives publication and modification timestamps on 16 July 2025.

Deduplication and evidence handling: SRC-309 is a distinct secondary journalism record, not a duplicate of the Jack Petchey organizer listing or any Arday interview. It supports a bounded reported judging role and attributed remark only; the exact event date, full judging roster, and an independent recording/transcript remain unresolved.

# 2026-08-06 — Jack Petchey official judging-panel corroboration

Discovery: the organizer’s own Speak Out Challenge page was located from the secondary judging report. It was published 1 July 2025 and announces Arday as a judge for the 7 July Cambridge Theatre Grand Final.

Capture: the organizer page, response headers, and its 1280×720 PNG judging graphic were preserved locally with checksums. The page states the planned judging criteria: content, delivery, structure, and positive impact.

Deduplication and evidence handling: SRC-310 is distinct from SRC-309 because it is the first-party pre-event organizer announcement, while SRC-309 is later local journalism reporting the final and an attributed remark. The organizer page corroborates the planned judging role and exact date but does not establish attendance or independently verify the newspaper quote.

# 2026-08-06 — Jack Petchey official Grand Final round-up capture

Discovery: the organizer’s post-event “Grand Final 2025 Round Up” was surfaced through the Jack Petchey past-event search. Published 8 July 2025, it confirms the 7 July Cambridge Theatre final, the winner and top-four results, and an audience of nearly 1,000.

Capture: the round-up HTML, response headers, linked organizer photo-page URL, and one 799×533 event photograph were preserved locally with checksums. The post-event report is distinct from SRC-310’s pre-event judging announcement and SRC-309’s later secondary report.

Deduplication and evidence handling: SRC-311 closes the event-occurrence boundary but does not name judges or establish Arday’s individual attendance. The three records remain separate by source function: planned role, post-event organizer result, and secondary report/attributed remark.

# 2026-08-06 — British Academy Graceland source-version capture

Discovery: the British Academy lecture index links a dedicated event page for Arday’s 21 November 2024 “I Know What I Know: The Story of Graceland” lecture. The page supplies a direct first-party event manifestation, dated host biography, a linked Vimeo URL, and a page-linked portrait.

Capture: browser/web retrieval exposed the event page; direct shell retrieval returned a reproducible HTTP 403 Cloudflare challenge, which was preserved with headers. The 592×394 portrait was retrieved successfully. The linked Vimeo page was captured but did not expose a usable lecture recording or reliable media metadata.

Deduplication and evidence handling: SRC-312 is a source-version upgrade to the already canonicalized event/recording in SRC-057, not a duplicate lecture. Its biography is retained as dated British Academy host copy; repeated role descriptions are not promoted to current legal, employment, or governance facts.

# 2026-08-06 — Taylor & Francis *We See Things They’ll Never See* review source-version

Discovery: a publisher search surfaced Taylor & Francis’ version-of-record page for the review already captured as a White Rose accepted manuscript under SRC-287. The indexed publisher result supplies the DOI, online publication date, journal volume/issue, and printed pages.

Capture: direct requests to the publisher’s full-text HTML and PDF endpoints returned HTTP 403 Cloudflare challenge responses. Both challenge bodies and headers are preserved; no publisher full text or PDF is claimed.

Deduplication and evidence handling: SRC-313 is a publisher source-version linked to SRC-287, not a new review or Arday-authored publication. The accepted manuscript remains the local text; the publisher record is used for version-of-record metadata and access-state provenance only.

# 2026-08-06 — BSA Network Winter 2025 conference pre-event source-version

Discovery: the BSA’s official Winter 2025 *Network* newsletter surfaced a dated publication record for the 2026 “75 Years of Sociology” annual conference. Page 23 reports the venue move to Manchester and names Arday and Les Back among the planned speakers.

Capture: the 73-page BSA PDF, response headers, derived text, and a rendered image of page 23 were preserved locally with checksums.

Deduplication and evidence handling: SRC-314 is a pre-event newsletter source-version linked to SRC-187’s conference programme, not a duplicate event or proof that Arday delivered the scheduled plenary. The timeline wording was tightened from “delivered” to “scheduled” because the current corpus contains no post-event attendance or recording evidence.

# 2026-08-06 — Aiming Higher PDF recovery and original-host boundary

Discovery: the existing SRC-028 report record explicitly lacked a local PDF. A current public institutional mirror at the Geological Society exposed a 50-page PDF matching the Runnymede report’s title, ISBN, February 2015 publication statement, editors, and contents.

Capture: the mirror PDF, response headers, derived text, and rendered cover were preserved. The canonical Runnymede PDF URL returned HTTP 404; its HTML body and headers are retained as a changed-state boundary.

Deduplication and evidence handling: this is an upgrade to SRC-028, not a new report. The mirror is labelled as a source-version, and the report’s edited structure is retained: Arday’s documented contributions are the co-authored introduction and his chapter beginning on printed p. 40, not every chapter in the volume.

# 2026-08-06 — Reading Blue Coat SRC-233 changed-state gallery upgrade and deduplication

Discovery: overlap checking showed that the Reading Blue Coat report had already been catalogued as SRC-233 during the earlier institutional sweep. The new retrieval is therefore an upgrade to that canonical record, not a new source.

Capture: the changed page HTML and headers were preserved. Its gallery exposed ten event photographs, all downloaded with individual response headers and checksums. The page reports student-facing sessions across the Lower School, Middle School, and Sixth Form and summarizes the themes of Arday’s message.

Deduplication and evidence handling: the temporary SRC-309/C-291 records were removed and their assets merged into SRC-233. The canonical record supports the occurrence of a school visit as reported by the host and the reported session structure, but not a precise visit date, verbatim remarks, student identities, or independent verification of repeated childhood biography wording. Image rights remain unresolved.

# 2026-08-06 — BBC *Today* 18 June 2026 PID recovery

Discovery: a current LinkedIn/Social Research Association post linked the previously unresolved BBC *Today* appearance to BBC Sounds PID `m002xp5j`. The BBC Sounds play page remains HTTP 404, but the official programme JSON endpoint is live.

Capture: the BBC JSON identifies the 18 June 2026 Radio 4 episode, canonical original version `m002xp5h`, and four version durations. Four public `audio-download-gb-aac` media-selector requests for the listed version PIDs returned HTTP 404 `selectionunavailable`; no audio binary or transcript was claimed. The current LinkedIn HTML was preserved as a changed social-post manifestation.

Deduplication: this upgrades SRC-235/C-194 rather than creating a new source. The episode identity/date are now verified through the BBC metadata, while the SRA’s approximate 1:52 segment position and the content of Arday’s remarks remain unresolved.

# 2026-08-06 — University of Greater Manchester and Oxford ORIGIN institutional records

Discovery: a fresh institutional search surfaced the University of Greater Manchester’s VC development programme page and Oxford GLAM’s ORIGIN project page. Neither URL was present in the registry, and both add dated institutional relationships rather than duplicate employment or publication records.

Capture: both HTML pages and response headers were retrieved and preserved locally. The Oxford page’s linked 600×400 portrait was also downloaded with its response headers and checksum.

Evidence handling: SRC-315 records Arday as a named mentor/resource person in the University of Greater Manchester programme whose inaugural cycle concluded 27 June 2025. SRC-316 records his inclusion on the ORIGIN project team for a 2023–2028 project. The pages do not specify session delivery, project workload, funding, authorship, or employment status, so those questions remain open.

The same pass rechecked the indexed Lives Retold/BBC Lent Talk PDF URL. It remains HTTP 404 and returned only a one-byte non-PDF body; that failure is now preserved in the existing SRC-036 record and negative-space ledger rather than treated as a new source.

# 2026-08-06 — University of Westminster Holding the Space post-event report

Discovery: a current institutional-news search surfaced the University of Westminster’s 30 April 2026 report on the 16 April *Holding the Space: Shining a Light on Black Academics* conference. It is distinct from the pre-event LinkedIn/listing record and supplies a post-event participation witness.

Capture: the official HTML page, headers, and seven linked 800×450 GIF images were retrieved and preserved locally. The page reports more than 100 speakers/delegates/advocates and summarizes Arday’s discussion with Stephen Bunbury.

Evidence handling: SRC-317/C-301 records participation and C-302 records the host’s attributed thematic summary. The summary is not treated as a transcript, and the images are page-linked event media with unknown photographer/licence.

# 2026-08-06 — NoWAL Conference 2019 handbook changed-state recovery

Discovery: the official Academic Libraries North NoWAL handbook, previously catalogued under SRC-256 as a 404/indexed lead, reappeared at a changed `/wp-content/uploads/2025/04/` URL in current search results.

Capture: the 24-page PDF returned HTTP 200 and was preserved with headers, derived text, and rendered printed pages 3, 5, 7, and 20. It identifies the 28 June 2019 University of Liverpool event, schedules Arday’s keynote and panel participation, and preserves the conference’s contemporaneous biography wording.

Deduplication and evidence handling: this upgrades SRC-256 rather than creating a new source. The earlier 404 body/headers remain as superseded access-state evidence. The handbook’s role descriptions are dated host copy, not independent appointment records; keynote delivery and exact affiliation validity remain bounded.

# 2026-08-06 — OpenLearn *Introducing Union Black* course-author record

Discovery: a current Open University/OpenLearn search surfaced the distinct *Introducing Union Black* course and its acknowledgements page. The course page gives a first-publication date of 31 October 2024; the indexed printable representation carries a 9 December 2025 date.

Capture: the course introduction and acknowledgements were verified in the in-app browser. The course-author photograph and thumbnail were downloaded through the observed page-asset inventory. Direct shell requests to the course and printable endpoints returned HTTP 403 challenge bodies; those headers/bodies are preserved, and no PDF binary is claimed.

Deduplication and evidence handling: this is SRC-318, distinct from Arday’s 2021 edited-volume chapter with Marcia Wilson and Dave Thomas. The four-person course-author credit establishes participation in creating a public educational resource, but not the division of labour, current affiliation, or a new biographical fact.

# 2026-08-06 — Snapjournal low-provenance biography capture

Discovery: exact-name search surfaced Snapjournal’s 24 April 2026 “Career Milestones and Educational Impact 2025-2026” page. It was not present in the registry and is distinct from institutional, publisher, scholarly, and journalistic records.

Capture: the page HTML, WordPress API JSON, response headers, and linked 1280×720 JPEG were retrieved. Structured metadata identifies the author only as “Snapjournal,” gives 1,783 words, and exposes no named source list or citations.

Evidence handling: SRC-319/C-307 records page existence and its role as a public propagation witness. Its assertions about current Cambridge employment, visiting roles, ORIGIN/CoPICS, fundraising, media appearances, and childhood are not upgraded into biography claims; several are stale or unresolved against the primary-source audit. The linked image is preserved with unknown rights status.

# 2026-08-06 — BACP *Therapy Today* and Spring 2026 memoir rights catalogue

Discovery: a fresh exact-name sweep surfaced two non-duplicate documentary records: BACP’s July/August 2025 issue, which lists *Beyond Lonely* as a five-episode BBC podcast hosted by Arday, and a Spring 2026 literary rights catalogue entry for *Great and Unfortunate Things*.

Capture: both PDFs, response headers, derived text, and relevant rendered pages were preserved locally. The BACP listing is on printed page 19; the memoir entry is on printed catalogue page 82 and gives a 288-page count, August 2026 publication month, agent, Korean rights sale, and manuscript-available status.

Deduplication and evidence handling: SRC-320 is a source-version linked to the canonical BBC *Beyond Lonely* record SRC-063, not a new programme. SRC-321 is trade/agent copy, not the memoir itself or an independent biography. Its “second youngest of three boys” wording is preserved as a discrepancy against other public catalogue copy, and the synopsis’s childhood and Cambridge claims remain attributed rather than promoted.

# 2026-08-06 — Scope Awards 2025 judges page

Discovery: a fresh disability-sector search surfaced Scope’s first-party “Scope Awards 2025 judges” page, which was not present in the registry. It is distinct from the existing Shaw Trust Disability Power 100 record and from other awards/recognition sources.

Capture: the page HTML, response headers, linked 400×400 Arday portrait, and image headers were retrieved and preserved locally. The page lists Arday among the judging panel and publishes a short biography.

Evidence handling: SRC-322/C-311 records the panel listing; C-312 records the dated Scope biography as source-version copy. The Cambridge/Jesus present-tense wording and Disability Power 100 ranking are not independently upgraded by this page, and image rights remain unknown.

# 2026-08-06 — Our Voice Enfield Black History Month handout

Discovery: a fresh community/disability search surfaced a one-page October 2024 Our Voice Enfield handout featuring Arday among Black disabled role models. It was not present in the registry and is distinct from the linked Channel 4 recording and existing institutional biographies.

Capture: the PDF, derived text, response headers, and rendered page were preserved. The host’s TLS certificate could not be validated by the local trust store, so the PDF was retrieved with certificate verification disabled; that boundary is recorded rather than hidden.

Evidence handling: SRC-323/C-313 records the handout and its link to the existing Channel 4 source; C-314 records its repeated age-11/age-18 and 2012-goal-list wording as secondary circulation copy. No new independent childhood or employment fact was promoted.

# 2026-08-06 — Hillingdon SEND & Inclusion Newsletter

Discovery: a public-sector PDF search surfaced Hillingdon’s SEND & Inclusion Newsletter, Volume 18, dated 6 July 2023. The one-page opening message includes Arday as an example for children with SEND and was not present in the registry.

Capture: the 16-page PDF, derived text, response headers, and rendered page 1 were preserved. The Arday passage appears on PDF page 1 in the Director of Education and SEND’s message.

Evidence handling: SRC-324/C-315 records the newsletter and dissemination context; C-316 records its repeated diagnosis, age-11, and Cambridge wording as source-version copy. The underlying linked article is not identified in the captured PDF, so no independent biographical fact was promoted.

# 2026-08-06 — UK Parliament Education Committee SEN 53 written evidence

Discovery: the parliamentary/public-policy sweep surfaced the Education Committee page for “Written evidence from Anonymous (SEN 53)” in the *Solving the SEND Crisis* collection. Its public text mentions Arday as an example in a SEND-policy argument and is distinct from the 2021 Youth Unemployment Committee hearing.

Capture: web retrieval exposed the page text and committee context; direct shell retrieval returned HTTP 403. The response body and headers are preserved locally, with no complete HTML claim.

Evidence handling: SRC-325/C-317 records the anonymous third-party use of Arday’s public literacy narrative. The submission is not attributed to Arday, and its underlying source/date and the literacy claim remain unresolved within this record.

# 2026-08-06 — Advance HE EDI Conference 2025 programme

Discovery: a bounded search for new institutional media and event records found Advance HE’s official “Session abstracts — EDI Conference 2025” PDF. The book schedules Jason Arday as the Day 2 keynote speaker on 3 April 2025, 09:40–10:20, with the title “I am the King of Wishful Thinking: Re-imagining intersectionality.”

Capture: the 24-page PDF, response headers, derived text, and rendered printed page 14 were downloaded and checksummed locally.

Evidence handling: SRC-326/C-318 records a first-party programme and abstract, not proof that the keynote was delivered. No recording, transcript, slides, or attendance record was exposed. It is distinct from the Advance HE 2021 “Proud to be” video and other 2025 event records.

# 2026-08-06 — Birkbeck BAME Doctoral Conference

Discovery: the institutional-event sweep found Birkbeck’s official listing for its 19 June 2024 Black, Asian and Minority Ethnic Doctoral Conference. The programme schedules Professor Jason Arday as keynote speaker at 18:00 in the Clore Management Centre.

Capture: the official HTML page and response headers were downloaded and checksummed locally.

Evidence handling: SRC-327/C-319 records a scheduled keynote only. The page does not expose a talk title, recording, transcript, slides, attendance evidence, or post-event report.

# 2026-08-06 — Goldsmiths EDI Report 2024

Discovery: an institutional-report search found Goldsmiths’ *Equality, Diversity, and Inclusion Report (2024)*, which documents an “In Conversation with Professor Jason Arday” webinar held in March 2024 during Neurodiversity Celebration Week.

Capture: the 46-page PDF, derived text, response headers, and rendered printed page 40 were downloaded and checksummed locally.

Evidence handling: SRC-328/C-320 records the host’s event summary and engagement language. It does not provide an exact event date, recording, transcript, slides, or substantive remarks.

# 2026-08-06 — Cambridge talks.cam ARClub Talks listing

Discovery: the institutional event sweep surfaced a Cambridge talks.cam archive entry for a 7 February 2024 ARClub Talks session titled “Jason Arday.” The event-level page was recoverable at `/talk/index/211924/` when the default archive view no longer showed the 2024 item.

Capture: the event HTML, response headers, and an archive listing requested with `limit=500` were downloaded and checksummed locally. The event page identifies Arday as speaker, gives 11:30–12:30 and a Zoom venue, and states “Abstract not available.”

Evidence handling: SRC-329/C-321 records a first-party scheduled-event witness. No delivery, attendance, talk content, transcript, slides, or recording is claimed; the historical Zoom URL is retained only as a source-field observation.

# 2026-08-06 — Autism School International profile

Discovery: a search for new public biography circulation surfaced Autism School International’s “A Story of Hope: Jason Arday,” dated 3 October 2025.

Capture: the page HTML, response headers, linked 1140×1280 JPEG, and image headers were downloaded and checksummed locally.

Evidence handling: SRC-330/C-322 records the page as a low-provenance advocacy retelling. It repeats childhood, family-support, PhD, Cambridge, and neurodiversity-advocacy language without citations; the page’s faith framing and image are preserved, but no repeated claim is promoted as independent corroboration.

# 2026-08-06 — Charity Commission BSA trustee snapshot

Discovery: the governance reconciliation pass found a current Charity Commission trustee page for the British Sociological Association that still displays Dr Jason Atta Kwei Arday as a trustee appointed 9 June 2020.

Capture: the regulator page and response headers were downloaded and checksummed locally. The page does not show an end date for Arday.

Evidence handling: SRC-331/C-323 is a dated regulator snapshot and a source-version update to SRC-102. It does not prove active service or register freshness after the Cambridge resignation; the absence of an end date is logged as unresolved rather than converted into a negative fact.

# 2026-08-06 — Charity Commission First Star trustee snapshot

Discovery: the public-filing reconciliation found the current Charity Commission trustee page for First Star Scholars UK.

Capture: the current trustee page and response headers were downloaded and checksummed locally. Jason Arday does not appear in the displayed trustee table.

Evidence handling: SRC-332/C-324 records a changed regulator-page state alongside the older First Star annual-accounts and Companies House records that give a 16 May 2025 resignation date. The current omission is not treated as independent proof of that date; both source versions remain visible.

# 2026-08-06 — Charity Commission Autism Action trustee snapshot

Discovery: the public-filing reconciliation found the current Charity Commission trustee page for Autism Centre of Excellence, whose working name is Autism Action.

Capture: the current trustee page and response headers were downloaded and checksummed locally. The page lists Prof Jason Atta Kwei Arday as a trustee appointed 30 March 2024 and shows no end date.

Evidence handling: SRC-333/C-325 is a current regulator source-version distinct from the earlier Charity Commission record, Companies House officers record, and 2024–25 accounts. It establishes the displayed page state, not indefinite active service or post-resignation status.

# 2026-08-06 — Warwick Education Conference 2026 keynote

Discovery: the institutional event sweep found Warwick’s post-event highlights page for its Education Conference 2025/26, held 4 June 2026. The page identifies Professor Jason Arday as a keynote speaker and labels his session “We Dream the Same Dream: Collective Empowerment in Pedagogy.”

Capture: the conference page, post-event highlights page, response headers, page-linked portraits, and direct MP4 were preserved. The MP4 was assembled from verified byte ranges because the server advertises `Accept-Ranges`; the final file is exactly 138,726,243 bytes, matching the server’s declared content length, and hashes to `aa76c9208637513b416c0adb37751a50ebcadb542fc0ab42b84ea2a6b549034c`.

Evidence handling: SRC-334/C-326 records a first-party post-event video manifestation. The page advertises a captions track, but the track endpoint did not yield a separate caption file during this pass. No substantive content is extracted until human verification.

# 2026-08-06 — *The Atlantic* memoir and proposal feature

Discovery: a same-day search surfaced Daniel Engber’s *Atlantic* feature “Icarus in the Faculty Lounge,” a distinct major-journalism source not present in the registry. It is materially different from the existing rights-catalogue synopsis, Guardian/Times coverage, and primary institutional statements because it reports from a copy of the 2024 book proposal and compares it with the forthcoming memoir.

Capture: the article HTML, response headers, lead image, and image headers were retrieved and checksummed locally. The article is metered; the local capture preserves the publicly delivered article state and structured metadata, not an assertion of unrestricted access or a complete primary copy of the memoir/proposal.

Evidence handling: SRC-335/C-327–C-330 records the article’s date, scope, reported memoir content, cross-version discrepancies, and separation between an LMJU statement and reported allegations. New childhood, health, sports, family, and academic-conduct details are retained as attributed source-version material. No memoir/proposal passage, medical record, club record, or investigation finding is promoted to settled fact from this article alone.

# 2026-08-06 — Simon & Schuster *Great and Unfortunate Things* publisher pages

Discovery: the official Simon & Schuster US and UK product pages became the next highest-value lead after the Atlantic feature. They are distinct from the Spring 2026 rights catalogue and expose a first-party synopsis, a public excerpt, edition metadata, and official cover/author-photo resources.

Capture: the US and UK page requests returned Cloudflare HTTP 403 to the local shell; both response bodies and headers were preserved as access-state evidence. The official US and UK cover images and the credited Anselm Ebulue author portrait were downloaded successfully. Browser/indexed page text exposed the excerpt and metadata, but no complete book or audio file was copied.

Evidence handling: canonical SRC-091/C-331–C-335 records the publisher’s first-party memoir status, edition divergence, excerpt self-report, repeated “three boys” wording, and stale present-tense Cambridge biography. The former SRC-336 duplicate is retired as an alias. The excerpt is retained as primary narrative material for source-version comparison, not independent proof of diagnosis, birth date, family count, treatment, or current employment.

# 2026-08-06 — NetGalley review-copy listings and audiobook endpoint recheck

Discovery: the memoir search surfaced two NetGalley catalog records (US and UK/Australia). It also rechecked the official Simon & Schuster Audio page and matching Audible/Apple retailer listings; that audiobook record was already canonicalized as SRC-189/C-105 and is not duplicated.

Capture: both NetGalley pages, response headers, and listing covers were preserved. A fresh audiobook page and header capture returned Cloudflare HTTP 403 and was attached to SRC-189 as a current access-state update. No NetGalley ARC, audiobook file, or preview was downloaded, and no access control was bypassed.

Evidence handling: SRC-337/C-336 records public ARC cataloging and sign-in boundaries. SRC-189/C-105 remains the canonical audiobook record; the new 403 capture does not create a new source or claim. These records establish editions and access states, not review-copy contents or independent biographical corroboration.

# 2026-08-06 — *Publishers Weekly* memoir review

Discovery: a targeted review search found *Publishers Weekly*’s 7 May 2026 review for the memoir, a distinct trade-reception source not present in the current source registry. It is not a duplicate of the publisher page, NetGalley records, Goodreads, or the rights catalogue.

Capture: the review HTML, response headers, cover image, and cover headers were retrieved and checksummed locally. The page exposes the review date, synopsis, edition ISBNs, and agent field.

Evidence handling: SRC-338/C-337–C-338 records the review as secondary reception and preserves its “did not speak until 12” wording, plus reported Debs/phonics/sporting-goods and 2005 St Mary’s details. These are review-level accounts of memoir content, not independent school, clinical, or civil records. The age discrepancy is appended to negative space rather than silently harmonized.

# 2026-08-06 — Simon & Schuster UK ebook edition recheck

Discovery: publisher search exposed a separate UK ebook ISBN, `9781398542761`, with a stated 27 August 2026 release and 368-page length. This is an edition-level update to canonical SRC-091, not a new work or source family.

# 2026-08-08 — SRC-091/SRC-336 memoir-record deduplication

The source audit found that SRC-091 and SRC-336 both represented the same Simon & Schuster publisher page family and excerpt. SRC-091 is now canonical and contains the US/UK edition topology, excerpt boundary, image/access captures, and related claims. SRC-336 is retained only as an explicit retired alias so historical Drive and research-log references remain auditable; it is not counted as a second publisher source.

Capture: the ebook page and response headers were retrieved; the endpoint returned HTTP 403. The current access state is preserved locally alongside the UK hardcover page and its distinct 336-page metadata.

Evidence handling: C-339 records edition topology and the pagination difference only. No new biography or memoir-content claim is inferred.

# 2026-08-08 — SRC-184/C-421 *Talking Matters* sports source-version boundary

The preserved automatic-caption derivative was reread around 00:18:50–00:21:06. The exchange presents both a “professional club” formulation naming Crystal Palace and a subsequent statement that Arday was not good enough to become a professional footballer and instead played non-league football for roughly 12–13 years; the snooker segment describes practice from about 11 to 18/19 and junior tournaments at Pontins in Prestatyn. The audio excerpts remain locally preserved for direct listening.

Evidence handling: added C-421 as an internal transcript-version tension, not a new independent sports record. No professional contract, senior appearance, ranking, or tournament result was inferred. The ASR remains unverified and must not be quoted as verbatim until the audio is manually checked.

# 2026-08-07 — Royal Society profile current-version recheck

Discovery: a current web-rendered Royal Society profile remained indexed and repeated its Runnymede trustee, BSA trustee, CLASS National Advisory Panel, NHS Race and Health Observatory, RSA Fellow, ITV Cultural Advisory Council, and committee-term wording.

Capture: direct shell retrieval returned HTTP 403 from the site gateway. The current body and headers were preserved as source-version evidence under SRC-134; the web-rendered text was inspected through the public page result.

Evidence handling: no new role claim was created. C-037 was updated to record the 7 August host-state observation. The profile remains a public institutional biography, not a substitute for Companies House, Charity Commission, or direct host governance records.

# 2026-08-07 — ABI speaker-profile endpoint recheck

Discovery: a current indexed ABI result continued to expose the older speaker biography, including the Ohio State visiting-professor, Runnymede, CLASS, and related role wording.

Capture: the alternate profile produced a web/browser 404 state, while direct shell requests to the alternate and `/live/` ABI endpoints returned Cloudflare HTTP 403 challenge bodies. Both current response bodies and headers were preserved under SRC-225.

Evidence handling: this is a changed access-state/source-version update, not new confirmation of any appointment or event delivery. No claim was created; the indexed biography remains dated ABI copy and is reconciled against direct host/legal records.

# 2026-08-08 — SRC-225: ABI agenda route recheck

Discovery: a current indexed result exposed a second ABI agenda filename, `annual-conference-2025-agenda-210225.pdf`, alongside the previously catalogued `190225.pdf` route.

Capture: the alternate route returned HTTP 403 challenge HTML rather than a PDF. The response body and headers are preserved under `assets/captures/2026-08-08-abi-agenda-recheck/`; no new agenda, recording, transcript, or delivery evidence was recovered.

Decision: updated SRC-225 with the alternate route and access state. No new source node or claim was created. Reopen only for a lawful agenda binary, post-event report, recording, transcript, or changed endpoint.

# 2026-08-08 — Institutional-outcome search boundary

Discovery: exact-name searches across Cambridge, Liverpool John Moores, Queen’s University Belfast, and general university-investigation results returned the already-catalogued Cambridge statement/AP report, QUB/BBC response, Telegraph process report, and existing commentary/source-propagation records. No new official investigation outcome, terms of reference, inquiry report, appointment-review document, or direct LJMU/QUB/Cambridge case statement was exposed.

Evidence handling: repeated Reddit and commentary results were not treated as institutional evidence. The AP report and Cambridge/QUB statements remain separate canonical records; public claims about clearance, scope, fabrication, or resignation rationale remain attributed to their respective sources.

Decision: no source node or claim was created. Reopen only for a changed official endpoint, named terms of reference, primary inquiry/report document, direct university statement, or adjudicative outcome; do not repeat this exact domain/query family unchanged.

# 2026-08-08 — SRC-628/C-860: ORCID publication-date recheck

Discovery: the current ORCID works API returned the same 11 DOI-linked work groups as the 6 August snapshot, with no new DOI/title key. One existing work, “Same storm, different boats,” changed its ORCID publication-date field from October 2022 to July 2026 while retaining the same put-code and title/DOI.

Reconciliation: Crossref’s current DOI metadata preserves 25 October 2022 as `published-online`/`published` and reports July 2026 as `published-print`. The changed ORCID value is therefore recorded as a later print/metadata manifestation, not as a new publication or correction.

Decision: created SRC-628/C-860, linked the recheck from the public-output index, and retained the canonical article date. Reopen only for a new ORCID DOI/title key, a materially different publisher/repository file, or a changed Crossref/ORCID date topology.

# 2026-08-08 — Residual scholarly-output search boundary

Discovery: exact-title searches for “The Fire Now,” “Diversifying the Ivory Tower and Closing the Student Attainment Gap,” “Understanding Racism within the Academy,” the physical-education teacher-education chapter, and the 2018/2021 educational-leadership outputs returned the already-catalogued Durham, Bloomsbury/PagePlace, Taylor & Francis, SAGE, and Liberated Library records. The results exposed no new DOI, edition, publisher record, repository file, or distinct event recording.

Decision: no new publication node, claim, or binary was created. Existing records remain canonical and their previews/access boundaries remain versioned. Reopen only for a materially different file, concrete new identifier, publisher correction, or distinct recording/transcript; do not repeat this exact residual-output query family unchanged.

# 2026-08-08 — Media-index search boundary

Discovery: exact-name searches for Jason Arday video interviews, podcasts, 2025 lectures, and transcripts returned Newcastle University’s 2025 lecture, the Crick 2024 event, Research Cast UK, Bett 2024, Our Voice Enfield, and the Society for Experimental Biology listing as already-catalogued records. Remaining results were repeated platform manifestations, source-propagation profiles, or homonyms.

Decision: no new media node, video ID, audio binary, transcript, or claim was created. Reopen only for a distinct recording/transcript, changed media endpoint, or concrete uncatalogued event artifact; do not repeat this exact media query family unchanged.

# 2026-08-08 — Legal/governance-register search boundary

Discovery: current exact-name searches across Companies House and the Charity Commission returned the already-catalogued Runnymede termination, First Star resignation, Autism Centre of Excellence active directorship, Crosstown Traffic appointment, BSA governance, and Adult Literacy Trust patron records. No changed officer, trustee, appointment, resignation, confirmation statement, accounts filing, or direct governance explanation was exposed.

Decision: no new legal source node or role claim was created. Reopen only for a changed filing-history state, new filed document, direct charity governance record, or explicit role-end explanation; do not repeat this exact register search family unchanged.

# 2026-08-07 — RSA/CLASS direct-host recheck

Discovery: fresh exact-name searches across RSA/CLASS domains and role phrases returned no direct RSA Fellow directory entry, RSA announcement, or CLASS National Advisory Panel governance page. Results were limited to already-canonical Royal Society profile/committee witnesses and repeated biography copy.

Evidence handling: SRC-166/C-073 were updated in place. No new source or role claim was created; the RSA and CLASS assertions remain unresolved host-record questions, not negative findings.

# 2026-08-07 — Battersea Park Rangers / Southern Sunday Football League named-record recheck

Discovery: exact-name searches for `"Jason Arday" "Battersea Park Rangers"`, `"Jason Arday" "Southern Sunday Football League"`, `"Jason Arday" "Battersea Park" football`, and `"Jason Arday" football "Rangers"` again returned the canonical News24 profile plus unrelated Rangers material. No public roster, league post, award record, match report, or contemporaneous club announcement naming Arday was recovered.

Evidence handling: SRC-151 and C-014 were updated in place. The result is negative space within this named-record boundary; C-255 remains a News24-caption/visual witness and C-256 remains club context. No new source or sports-status claim was created.

# 2026-08-07 — RGS-IBG Annual Conference Jason Arday event state

Discovery: current RGS Chair’s Events HTML records a planned 2 September 2026 conversation with Jason Arday, but also displays “This session has been cancelled at the request of the speaker.” The linked speaker route resolves to the wider conference page; the Ex Ordo endpoint returned an application shell rather than a usable session record.

Evidence handling: SRC-339/C-340 records the first-party event listing and cancellation as one changed event state. No attendance, delivery, livestream, transcript, or recording claim was created. Search-index text exposing the older scheduled wording remains a superseded manifestation.

# 2026-08-07 — AMOSSHE National Conference 2026 keynote lead

Discovery: organizer-attributed LinkedIn promotion announced Jason Arday as the closing keynote for Friday 3 July 2026. AMOSSHE’s official conference landing, programme, and speakers pages confirm the 1–3 July Newcastle conference but the current captured programme/speakers pages omit Arday and do not show a closing-keynote slot.

Evidence handling: SRC-340/C-341 records the promotion and current official page states without inferring delivery, cancellation, or attendance. No recording, transcript, deck, or post-event account was found. The LinkedIn result remains an indexed social-host witness; the AMOSSHE pages are the first-party event-context records.

# 2026-08-08 — AMOSSHE post-event boundary recheck

Discovery: because the advertised 1–3 July 2026 conference had passed, a fresh targeted search checked the AMOSSHE landing, programme, and speakers URLs, exact-title searches, and public video indexing for a final programme, attendee report, recording, transcript, or deck.

Capture: the three official HTML pages and response headers were preserved under `assets/captures/2026-08-08-amosshe-recheck/`. The current programme and speakers pages still contain no Arday match or closing-keynote entry. Search results reproduced the earlier organizer promotion but exposed no post-event artifact.

Evidence handling: added C-434 to the existing SRC-340 record. The result is a dated non-occurrence/access boundary only: it does not establish delivery, attendance, cancellation, or non-occurrence. Do not create a duplicate event source unless a new artifact appears.

# 2026-08-08 — SRC-401 independent thesis-overlap analysis

Discovery: a targeted search for independent work around the Cofnas/Arday thesis comparison surfaced Analyse That’s “Measuring Text Overlap Between Two Doctoral Theses,” dated 24 July 2026. The page identifies itself as a reproducible embedding-based analysis of Arday’s 2015 LJMU thesis and Paula Zwozdiak-Myers’s 2009 Brunel thesis.

Capture: preserved the article HTML and headers, `overlap_analysis.py`, `analysis_v2.zip`, the 185-pair appendix, and the two control-thesis PDFs with headers under `assets/captures/2026-08-08-analysethat/`. The six-encoder bundle contains eight Python files and was not executed in this pass.

Evidence handling: added SRC-401/C-435–C-437. The analysis is treated as a distinct computational source, not as another Cofnas or Arasite manifestation. Its reported overlap metrics and provenance categories are attributed to the author; the article’s own limits, AI-generation disclosure, and explicit non-adjudication of intent/misconduct are retained. The underlying Arday and Zwozdiak-Myers primary PDFs remain canonical for direct textual verification.

# 2026-08-08 — Cambridge investigation-scope policy reconciliation

Discovery: a targeted official-source search found the current Cambridge “Procedure for the Investigation of an Allegation of Research Misconduct (2026)” PDF, and a 29 July 21percent commentary that reports—without publishing a case report—that Cambridge’s Arday process was ruled out of scope rather than exonerating him.

Capture: preserved the 21percent article HTML/headers and the official 22-page Cambridge procedure PDF, extracted text, and headers under `assets/captures/2026-08-08-investigation-scope/`.

Evidence handling: added SRC-402/C-438 and SRC-403/C-439. The policy says the procedure can cover former researchers in appropriate circumstances, expressly includes plagiarism, fabrication, falsification, qualifications/credentials, publication history, and improper handling of allegations, and has screening, preliminary, and formal stages. This makes “out of scope” a procedural category whose case-specific meaning remains unknown; it is not treated as either exoneration or a misconduct finding. The alleged Cambridge/LJMU reports remain unrecovered.

# 2026-08-08 — SRC-404 LJMU misconduct-policy capture

Discovery: the current LJMU research-integrity policy page exposes a public accessible-format DOCX for its “Policy for Alleged Misconduct in Research and Knowledge Exchange.” This is a new primary procedural source, not a duplicate of LJMU’s anonymized 2024–25 annual statement.

Capture: preserved the policy page/headers, DOCX/headers, and extracted text under `assets/captures/2026-08-08-ljmu-policy/`. The document identifies June 2015 introduction, March 2024 modification, June 2024 approval, and September 2026 review timing.

Evidence handling: added SRC-404/C-440–C-441. The policy defines plagiarism/fabrication/falsification/deception, applies to people who have undertaken research on behalf of LJMU, and provides prima-facie, panel, investigating-officer, appeal, and award-revocation pathways. It does not reveal whether or how Arday’s reported confidential review used the policy, so no case outcome was inferred.

# 2026-08-08 — SRC-405 Arasite final-grid page-level audit

Discovery: the remaining `ARDAY FINAL GRID.docx` in the already preserved Arasite `plag4.zip` maps Arday printed pp. 57–69 to Zwozdiak-Myers printed pp. 32–44, a substantially larger segment than the single opening screenshot previously audited.

Capture/comparison: the locally preserved thesis PDFs were checked at Arday pp. 57–60 and Zwozdiak-Myers pp. 32–35. The opening subsection heading, conceptual progression, Habermas discussion, paragraph order, and multiple sentence frames align across the two documents, with edits, added/changed citations, and expanded transitions. Arday cites Zwozdiak-Myers (2009) at the end of one overlapping paragraph, but the captured passage does not use quotation marks around the retained prose.

Evidence handling: added SRC-405/C-442–C-443 as a bounded audit of the existing dossier, not a duplicate source family. The comparison confirms a substantial textual/structural relationship in the checked segment, but does not determine intent, applicable citation standards, intermediate-source provenance, or an institutional finding. The dossier’s “almost unbroken plagiarism” label remains attributed to its authors.

# 2026-08-06 — Durham “Decolonising higher learning education in the UK” index recheck

Discovery: a fresh search-index result for Durham’s person output page (`outputs?page=3`) again exposed the chapter title, Jason Arday as author, S. Dufoix and S. Mosbah-Natanson as editors, *A World History of Sociology* as the host volume, and the indexed publisher field “France: Springer.” A targeted Springer search returned no chapter-level page, DOI, ISBN, pagination, or full text.

Evidence handling: this is an updated discovery witness for SRC-211, not a new source or verified publication record. Direct Durham retrieval remains HTTP 403; the existing La Découverte volume-level witnesses (SRC-213/SRC-214) and the Information Age indexed field remain in the conflict set. No new claim was created and no publisher field was promoted.

# 2026-08-07 — African Allied Healthcare Summit post-event state recheck

Discovery: the event’s advertised 23–24 July 2026 dates had passed, so the official African Allied Health Network home, speakers, and schedule pages were rechecked rather than treated as a settled delivered appearance.

Capture: fresh HTML and response headers were preserved under `assets/captures/2026-07-23-aahn-jason-arday/recheck-2026-08-07/`. The home page still displays the summit dates and says confirmed presentation details will be shared as the programme is finalized; the schedule still says final session times and speaker assignments are coming soon; the speakers page still lists Arday as a keynote speaker.

Evidence handling: SRC-306/C-342 now records a changed post-event page state. It verifies only that the organizer’s public site remained incomplete after the event dates; it does not establish delivery, attendance, cancellation, or non-occurrence. No new media or post-event report was found.

# 2026-08-07 — BME ECR Conference post-event page recheck

Discovery: the 10 July 2026 BME ECR Conference was already captured as a planned appearance under SRC-307, so a fresh post-event check targeted its public event page rather than creating a duplicate source.

Capture: the event HTML returned the same SHA-256 as the 6 August capture (`43958927423e40e46748787855266d9d14e0007320d3d1d38abc6468e38b7c40`). It still used pre-event language and exposed no post-event report, programme, attendee account, transcript, or keynote recording.

Evidence handling: SRC-307/C-343 now preserves an unchanged post-event page state. The absence of an updated page does not establish cancellation, non-attendance, or non-occurrence.

# 2026-08-07 — Companies House personal-appointments current snapshot

Discovery: a current Companies House search exposed Jason Arday’s personal-appointments page with a broader eight-appointment display than the earlier canonical record’s two-role summary.

Capture: the official appointments HTML and response headers were downloaded and checksummed under `assets/captures/2026-08-07-companies-house-jason-arday/`.

Evidence handling: SRC-099/C-344 was upgraded in place. The current page displays four active directorships and four resigned roles. Individual filing histories remain the authoritative route for specific appointment or termination dates; no operational or employment claim was inferred.

# 2026-08-07 — Company-level corroboration for active directorships

Discovery: the expanded Companies House personal-appointments page named Crosstown Traffic Ltd and B.S.A. Publications Limited as active directorships not previously represented by individual company records in the workspace.

Capture: current officers and filing-history pages for both companies were downloaded with response headers and checksums under `assets/captures/2026-08-07-companies-house-active-directorships/`.

Evidence handling: SRC-341/C-345 records Crosstown Traffic’s active director listing and April 2026 filings; SRC-342/C-346 records the B.S.A. Publications active director listing and March 2026 filing state. These records corroborate company-law status only and remain deduplicated under SRC-099.

# 2026-08-07 — Filed accounts PDFs for active company directorships

The two filing-history pages exposed direct “View PDF” links for the latest accounts. The six-page Crosstown Traffic PDF and seven-page B.S.A. Publications PDF were downloaded with response headers and preserved beside the HTML captures. They are scanned image documents with no useful text layer; every page was rendered with Poppler and visually inspected.

The PDFs add company-level context only: Crosstown reports one employee, a £46,615 director’s loan account, and net liabilities of £13,625; B.S.A. Publications identifies Arday among its directors, describes royalties as turnover, reports zero employees, and is limited by guarantee. Claims C-347 and C-348 point to the canonical records. No personal-finance, remuneration, or operational inference was created.

# 2026-08-07 — Contemporaneous named football-club record surfaced

Discovery: a targeted named-school/sports search surfaced the 48-page Autumn 2015 *Concordia* PDF in the Clapham Old Xaverian Archive. Text extraction located a 2 July 2015 match report at PDF pp. 7–8; page 7 was rendered and visually inspected.

Finding: the report names Jason Arday in the COXA 1st XI squad and describes him as the COXA keeper in an 8–0 win over the Manhattan Kickers. This is a new contemporaneous club record and the first named football-match record located in the corpus. It does not prove professional/semi-professional status, academy membership, or Southfields Academy attendance, and the player identity is retained as strong-but-qualified linkage.

Evidence handling: SRC-343/C-349 was created. The PDF and rendered match page are local binary assets; the sports/school boundary in NEXT.md was narrowed rather than treated as fully resolved.

# 2026-08-07 — Distinct Google Books UK memoir volume

Discovery: a fresh catalog search surfaced Google Books volume `HWfF0QEACAAJ`, separate from the previously captured `84edEQAAQBAJ` record. The new page identifies ISBN 9781398542747, a 336-page Simon & Schuster Limited edition scheduled for 27 August 2026, and a non-browsable/no-ebook state.

Capture: the page HTML, response headers, and 128×195 cover were downloaded and checksummed. The synopsis adds a “parents and two brothers” family-count formulation and repeats the age-three/11/18 chronology.

Evidence handling: SRC-344/C-350 records this as an edition-level source-version, not a duplicate memoir record. Catalog copy remains memoir/publisher material; the present-tense Cambridge author biography is preserved as stale promotional wording after the resignation.

# 2026-08-07 — Book-level *Black PhD Experience* record

Discovery: the exact-author publication audit exposed book-level DOI `10.46692/9781447370000`, which was not represented by the existing foreword-only SRC-016 record.

Capture: Cambridge Core’s 204-page book record, contents, ISBNs, DOI, linked cover, and partial-resource inventory were preserved. Policy Press and JSTOR direct shell responses were also preserved as current 403/anti-bot boundaries.

Evidence handling: SRC-345/C-351 adds the edited-volume manifestation and links it to, but does not merge it with, Arday’s foreword record. No full book or complete foreword PDF was downloaded; no claim of sole authorship or autobiographical content was made.

# 2026-08-07 — RSC YouTube caption-state recheck

Discovery: the locally preserved RSC recording remained an open timecoding lead, so the exact canonical YouTube page was checked once through the in-app browser and direct observed page state.

Finding: the page metadata embeds an English (UK) caption track, while the visible player reports captions unavailable. The observed timed-text endpoint returned HTTP 200 with zero content length in both shell and browser navigation. No transcript or substantive timecode was extracted.

Evidence handling: SRC-276/C-254 was upgraded in place with the page, headers, empty caption response, and caption headers. This closes the current caption-recovery attempt as an explicit access boundary; reopen only on a changed state.

# 2026-08-07 — BBC *Best of Today*: “What should children learn?”

Discovery: Apple, Amazon, and Podfollow catalogue pages surfaced a distinct 11 October 2024 *Best of Today* episode about England’s curriculum and assessment review. The listing names Jason Arday among the contributors and credits Sareen Bains as producer.

Capture: Podfollow exposed the BBC non-DRM download URL for VPID `p0jx4b0x`. The 40,197,249-byte MP3, 600×600 artwork, Apple/Podfollow HTML, and response headers were downloaded under `assets/captures/2026-08-07-best-of-today-children-learn/`.

Evidence handling: SRC-346/C-352 records the episode as a distinct manifestation from Arday’s December 2023 guest-editor programme. The MP3 is available for later listening/transcription, but no substantive remark or timecode is asserted yet.

# 2026-08-07 — St Mary's Students' Union Values Talk

Discovery: the St Mary's Students' Union Values Talks page links an official-channel recording titled “Jason Arday - A St Mary's Values Talk.” The YouTube metadata dates the upload to 19 November 2020, reports 46:15, and describes the talk as a discussion of Arday’s journey and hurdles.

Capture: the page, YouTube page, metadata JSON, 1280×720 thumbnail, and separate YouTube video/audio streams were preserved under `assets/captures/2026-08-07-st-marys-values-talks/`. The 137 video stream is 352,212,770 bytes; the 251 audio stream is 47,000,353 bytes. The advertised auto-caption endpoint returned a zero-byte body.

Evidence handling: SRC-347/C-353 records this as a distinct St Mary's media manifestation. The host’s qualification, student-leadership, fundraising, and career wording is retained as institutional promotional copy and not converted into independently verified claims. No transcript or timecode is asserted.

# 2026-08-07 — University of Bristol Black Academic Innovation Symposium

Discovery: the University of Bristol 2024–2025 Equality, Diversity and Inclusion annual report surfaced a post-event feature not represented by the existing Bristol keynote listing.

Capture: the 37-page first-party PDF, response headers, extracted text, and a rendered visual check of printed pages 34–35 (PDF page 18) were preserved under `assets/captures/2026-08-07-bristol-edi-report/`.

Evidence handling: SRC-355/C-355 records the report’s statement that Bristol hosted its first Black Academic Innovation Symposium and names Jason Arday as a keynote speaker. The report supplies no exact event date, keynote title or content, recording, transcript, or attendance details beyond the attribution.

# 2026-08-07 — University of Birmingham equity event changed-state record

Discovery: an exact-name/event search surfaced the University of Birmingham listing “What next for equity in education? A call for action,” scheduled for 3 June 2026, with Jason Arday named as a keynote speaker.

Capture: the current direct URL returned a University of Birmingham 404 page; the 30,054-byte HTML and response headers were preserved under `assets/captures/2026-08-07-birmingham-equity-event/`. Indexed first-party text supplied the historical event description, date, venue, keynote listing, and thematic clusters.

Evidence handling: SRC-356/C-356 records the scheduled event and current missing-page state. No delivery, cancellation, attendance, programme, recording, or transcript is inferred.

# 2026-08-07 — BSA 2026 conference archive completion pass

Discovery: a recheck of the BSA annual-conference archive found official Day 2 and Day 3 abstract books in addition to the already preserved Day 1 book and programme-at-a-glance PDF.

Capture: the current archive HTML, response headers, Day 2 (134 pages) and Day 3 (100 pages) PDFs, response headers, and layout-extracted text were preserved under `assets/captures/2026-08-07-bsa-conference-recheck/`. The PDFs were visually checked at their title pages and text-searched for Arday.

Evidence handling: SRC-187/C-357 was upgraded in place. Day 2 and Day 3 repeat the conference introduction naming Arday among three plenaries but add no new Arday-specific session detail, transcript, or recording. They remain source versions of the one conference rather than duplicate event records.

# 2026-08-07 — Oxford EDB lecture changed-state recheck

Discovery: the current Oxford Department of Education EDB page embeds YouTube video `4Go6LcSGQEM`, and Oxford Social Sciences says a recording of Arday’s lecture is available. This is a new host manifestation of the existing 29 October 2025 event, not a second lecture.

Capture: preserved the Social Sciences page, Department event response, Department videos page, YouTube page, and all response headers under `assets/captures/2026-08-07-oxford-this-is-a-low-recheck/`. The YouTube page reports the video private; the direct event curl returned 404 while the web-rendered event view remained readable with the prior Vimeo embed.

Evidence handling: upgraded SRC-185 in place and added C-358. No local video, transcript, or downloadable stream is claimed. Retry only after a changed YouTube privacy state, direct file/manifest, or newly exposed transcript.

# 2026-08-07 — ResearchGate scholarly discovery-index boundary

Discovery: a current web search surfaced ResearchGate’s automatically generated “Jason Arday’s research works” page, which reports 33 publications and includes the already canonical 2026 OSF narrative-inquiry preprint. This is a discovery/index surface, not a new publication record.

Capture: direct retrieval of the canonical ResearchGate URL returned HTTP 403/Cloudflare challenge HTML. The 21,115-byte response and headers were preserved under `assets/captures/2026-08-07-researchgate-output-index/`.

Evidence handling: added SRC-359/C-359 as a low-provenance index boundary. No ResearchGate attribution, publication count, or completeness claim was promoted; no duplicate OSF source was created. Reopen only after a changed page state or a concrete title/DOI that is not already represented.

# 2026-08-07 — Associated Press resignation report changed-state recheck

Discovery: the AP resignation/investigation report already catalogued as SRC-207 became directly retrievable at its canonical URL with HTTP 200. The response headers report `Last-Modified: Fri, 07 Aug 2026 01:44:59 GMT`; the current article body remains the same public-statement and attributed-allegation report, but its live access/version state differs from the earlier local snapshot.

Capture: preserved the fresh 759,548-byte article HTML and response headers under `assets/captures/2026-08-07-ap-resignation-recheck/`. The earlier 6 August HTML remains untouched.

Evidence handling: upgraded SRC-207 in place and added C-360. No new allegation or investigation outcome was inferred; Cambridge’s process remains unresolved.

# 2026-08-07 — Good Law Project and Cambridge notice status recheck

Discovery: the two primary-status URLs were rechecked after the AP live-state upgrade. Good Law Project returned HTTP 200 with a body byte-identical to the prior capture; Cambridge’s official statement also returned HTTP 200 and displayed a later 6 August page-update timestamp (14:14:27 +01:00 versus 09:32:06 in the prior capture), while its substantive process wording remained unchanged.

Capture: preserved both current HTML responses and headers under `assets/captures/2026-08-07-status-recheck/`.

Evidence handling: upgraded SRC-094 and SRC-208 in place and added C-361. No investigation outcome, exoneration, or misconduct finding was inferred.

# 2026-08-07 — BSA, Charity Commission, and Companies House role-status recheck

Discovery: the current British Sociological Association governance page, Charity Commission trustee page, and Companies House personal-appointments page were rechecked as the next role-verification slice. The BSA and Companies House bodies were byte-for-byte identical to their prior captures. The Charity Commission response changed in volatile frontend/session/resource fields, but the substantive row still listed Dr Jason Atta Kwei Arday as trustee, appointed 9 June 2020, with no displayed end date.

Capture: preserved current HTML and response headers under `assets/captures/2026-08-07-role-status-recheck/`. The BSA body is 40,623 bytes (SHA-256 `a071e0711be95e914c10d918b42c02f172372c65d703448eb2c3a7e837319f37`); the Companies House body is 61,630 bytes (SHA-256 `fcc326ad208f4d2970a13ba8262f3158a50d75dc62179e64f19eeaa1b1767f3e`).

Evidence handling: upgraded SRC-162, SRC-331, and SRC-099 in place and added C-362. This records current public display states only; it does not establish ongoing service, operational activity, an end date, or any relationship to the Cambridge investigation.

# 2026-08-07 — Lewisham Borough football records

Discovery: an exact-name football search surfaced two distinct source manifestations not previously canonicalized: a Kentish Football report dated 15 October 2018 and the public Lewisham Borough (Community) FC Pitchero roster. The report quotes manager Justin Fevrier saying Jason Arday had broken a rib against Lydd and that Inam Kharel came in as goalkeeper. The roster displays “Dr Jason Arday” as a goalkeeper.

Capture: preserved both current HTML responses and headers under `assets/captures/2026-08-07-sports-records/`. Kentish Football HTML is 34,648 bytes (SHA-256 `880c7c43cef40e2e43dc69104bf45cc39e88344778b83bca383319ac95f1bef5`); Pitchero HTML is 333,284 bytes (SHA-256 `57ef3f1e06706d641a3c51feae130d57decbbf70d99457b5d334615556565fcb`).

Evidence handling: added SRC-360/C-364 and SRC-361/C-363. These records strengthen the named-club trail but do not establish that either source’s Jason Arday is the sociologist, identify a registration or contract, prove a 2018 appearance, or upgrade the football narrative to professional/semi-professional status.

# 2026-08-07 — Snooker-specific negative-space recheck

Discovery: after the Lewisham football records were added, a separate exact-name search targeted the unresolved snooker side: tournament, player, Pontins, and billiards queries. The results were limited to already-catalogued autobiographical accounts and propagating summaries; no named snooker record surfaced.

Evidence handling: updated SRC-151 and `negative-space.md` in place. No new source or claim was created, because the search produced no independent material and the surfaced pages were duplicates of existing records. The Pontins/junior-tournament and near-professional accounts remain self-reported and require a named event, ranking, club, governing-body record, or newly accessible first-person audio/transcript to upgrade.

# 2026-08-07 — Companies House First Star officer-ID reconciliation

Discovery: a current exact-name search surfaced a second Companies House officer URL titled “Jason ARDAY.” Its single appointment is First Star Scholars UK, appointed 25 August 2020 and resigned 16 May 2025, with a May 1985 date of birth. These fields match the already canonical First Star termination record and the date-of-birth field on SRC-099’s eight-appointment officer page.

Capture: preserved the alternate officer page and response headers under `assets/captures/2026-08-07-companies-house-name-collision/`.

Evidence handling: upgraded SRC-101 in place and added C-365. The alternate URL is retained as a name-normalization/identity-reconciliation witness; the First Star directorship is not counted twice, and no broader identity conclusion is inferred from matching registry fields alone.

# 2026-08-07 — Cambridge appointment-announcement split state

Discovery: the appointment announcement remained exposed through two legacy Cambridge URLs even after the individual Faculty profile URL returned 404. Both the Faculty and `news.educ.cam.ac.uk` announcement manifestations returned HTTP 200 and retained the 23 February 2023 “will take up” wording.

Capture: preserved both current HTML responses and headers under `assets/captures/2026-08-07-cambridge-appointment-recheck/`. The Faculty response is 463,750 bytes; the news response is 453,805 bytes.

Evidence handling: upgraded SRC-114 in place and added C-366. The announcement is treated as historical institutional page copy, not current-employment evidence. Its coexistence with SRC-208’s profile 404 is a split host-state observation; no reason for removal or investigation outcome is inferred.

# 2026-08-07 — BBC *Today* 18 June 2026 media-state recheck

Discovery: the BBC *Today* lead for Arday’s reported discussion of GCSE-English thresholds was rechecked after the Cambridge host-state pass. The official programme JSON remains available with the same episode/version topology, while the BBC Sounds page remains a 404.

Capture: preserved current programme JSON, Sounds HTML, and response headers under `assets/captures/2026-08-07-bbc-today-2026-recheck/`.

Evidence handling: upgraded SRC-235 in place and added C-367. No audio, transcript, or exact 1:52 segment claim was added; no duplicate appearance record was created.

# 2026-08-07 — Royal Society profile browser-visible split state

Discovery: the Royal Society profile URL remained readable in the browser-rendered public view even though the same-date direct shell request returned HTTP 403. The visible page reproduced present-tense Runnymede, BSA, CLASS, RSA, NHS Race and Health Observatory, and ITV role wording, plus the Royal Society committee dates.

Capture: preserved the browser-visible DOM text under `assets/captures/2026-08-07-royal-society-browser-visible/profile-visible-text.txt`; the raw 403 body and headers remain under SRC-134’s earlier recheck assets.

Evidence handling: upgraded SRC-134 in place and added C-368. The visible institutional biography is retained as a dated source-version and does not override Companies House’s Runnymede termination or later BSA “formerly” wording. No new legal appointment claim was created.

# 2026-08-06 — BAME-leadership chapter residual-output recheck

Discovery: the 2021 Durham lead for “Understanding, addressing and centring BAME Leadership in Higher Education” was rechecked against the Durham output route, the Springer edited-volume page, and Crossref’s exact-title query.

Capture: preserved current Durham, Springer, and Crossref response artifacts under `assets/captures/2026-08-06-bame-leadership-chapter-recheck/`.

Evidence handling: upgraded SRC-081 in place and added C-369. The volume and Arday’s editorship remain verified, but no exact chapter DOI, pagination, chapter PDF, or publisher TOC match was found. The related “Sowing the Seeds” chapter remains a separate canonical record; no duplicate publication was created.

# 2026-08-06 — SRC-211 BnF/Sudoc catalogue boundary

Discovery: the unresolved Durham chapter lead was followed into the exact final-volume title *Une histoire mondiale de la sociologie*. Public BnF SRU and Sudoc SRU exact-title queries each returned zero records.

Capture: preserved both XML responses and response headers under `assets/captures/2026-08-06-world-history-sociology-catalogue-recheck/`.

Evidence handling: upgraded SRC-211 in place and added C-370. This narrows the defined public catalogue boundary without resolving the chapter identity or proving the volume absent; no duplicate publication record was created.

# 2026-08-06 — SRC-362 PASSHE National Conference 2026

Discovery: PASSHE’s official conference timetable was located through a current web search and directly captured. It schedules Jason Arday for an 11:00 keynote with Q&A, “We are where we are…,” on 10 June 2026.

Capture: preserved the first-party HTML and response headers under `assets/captures/2026-06-10-passhe-jason-arday/`.

Evidence handling: added SRC-362 and C-371 as a scheduled-event record. The page exposes no recording, transcript, slides, post-event report, or attendance evidence; no delivery or current-affiliation claim was inferred.

# 2026-08-07 — SRC-363 EDICa affiliation profile

Discovery: current web search located EDICa’s official project site and newsletter, which preserve a public Arday profile with Cambridge, Glasgow, Durham, Ohio State, Runnymede, BSA, CLASS, NHS RHO, and ITV wording.

Capture: preserved home/newsletter HTML and headers plus a 167×167 profile image under `assets/captures/2026-08-07-edica-jason-arday/`.

Evidence handling: added SRC-363/C-372. This is a host-published biography/source-version; it does not override Companies House, Ohio State ODI sunset, Glasgow denial, Cambridge resignation, or current Cambridge/Royal Society profile-state records.

# 2026-08-07 — SRC-364 St Mary’s student newsletter award manifestation

Discovery: a current St Mary’s PDF endpoint exposed the July student newsletter, whose “Things to note” section records that SMU alumnus Professor Jason Arday received an honorary doctorate at that year’s Summer Graduations.

Capture: preserved the nine-page PDF, response headers, and rendered page 9 under `assets/captures/2026-07-st-marys-student-newsletter/`. The PDF’s content and metadata identify the issue as July 2024 despite the current 2026 retrieval date.

Evidence handling: added SRC-364/C-373 as a separate institutional circulation manifestation linked to the 19 July 2024 honorary-doctorate announcement. It adds no second award or new biographical claim.

# 2026-08-08 — SRC-365 Google Books US memoir edition family

Discovery: current catalog search exposed separate Google Books records for the US hardcover volume `x7Ol0QEACAAJ` (ISBN 9781668085578, 288 pages) and US ebook volume `tpmQEQAAQBAJ` (ISBN 9781668085592, 260 pages). These IDs were not represented by the existing UK edition records.

Capture: preserved both catalog HTML/header pairs and both 128px cover JPEGs under `assets/captures/2026-08-08-google-books-memoir-us/`.

Evidence handling: added SRC-365/C-374/C-375. The two records are edition manifestations of one memoir; catalog/publisher copy remains source-version marketing text, and no browsable text or downloadable ebook was claimed.

# 2026-08-08 — SRC-366 PASSHE speakers-page source-version

Discovery: PASSHE’s dedicated National Conference 2026 speakers page was located as a distinct page from the already-captured timetable. It repeats the keynote title, a broad biography, and a current Cambridge/Jesus description.

Capture: preserved the page HTML/headers and the linked 1,758×1,610 portrait plus image headers under `assets/captures/2026-08-08-passhe-speakers/`.

Evidence handling: added SRC-366/C-376. The page is current host copy as of capture, but its present-tense Cambridge/Jesus wording is stale/contested after the 5 August resignation. No delivery, attendance, current employment, or substantive keynote content was inferred.

# 2026-08-08 — SRC-367 UCL BAME Awarding Gap evaluation report

Discovery: a UCL-hosted evaluation PDF surfaced in the public record of the BAME Awarding Gap Project. It is distinct from the already-catalogued UCL keynote page/video and is a retrospective institutional report rather than a duplicate media manifestation.

Capture: downloaded the 27-page PDF, response headers, and layout-preserving extracted text under `assets/captures/2026-08-08-ucl-bame-evaluation/`. The cover says May 2023 while the running footer says July 2023; both date states are retained.

Evidence handling: added SRC-367/C-377. The report records a March 2020 session run by Professor Jason Arday and lists the lecture’s topics. It does not add a transcript, slide binary, attendance list, or independent verification of the lecture’s substantive claims.

# 2026-08-08 — SRC-368 Adult Literacy Trust 2025 annual report

Discovery: the Charity Commission accounts page now lists the Adult Literacy Trust accounts and trustees’ annual report for the year ended 31 December 2025, received on 13 February 2026. This is a new report manifestation after the already-captured 2024 annual report (SRC-288).

Capture: preserved the regulator accounts-page HTML/headers and the 25-page PDF, PDF headers, and extracted text under `assets/captures/2026-08-08-adult-literacy-trust-2025/`.

Evidence handling: added SRC-368/C-378. Printed page 12 lists Prof. Jason Arday among patrons; page 14 repeats his name in the patron-support passage. The report also preserves charity-level 2025 financial totals, which are not attributed to Arday personally. Patron continuity after the report date and after the Cambridge resignation remains unresolved.

# 2026-08-08 — SRC-369 Royal Holloway EDI Annual Report 2023/24

Discovery: a public Royal Holloway annual-report PDF surfaced a distinct institutional record of a Black History Month 2023 “Decolonising the University” conversation hosted by Professor Jason Arday.

Capture: preserved the 52-page PDF, response headers, and layout-preserving extracted text under `assets/captures/2026-08-08-royal-holloway-edi-report/`.

Evidence handling: added SRC-369/C-379. The report names Arday as host and describes lightning talks and the event’s decolonising-higher-education focus; it does not expose the exact day, recording, transcript, attendance list, or substantive remarks.

# 2026-08-08 — SRC-370 St Mary's annual report

Discovery: St Mary's public corporate-information PDF exposed a distinct 2023/24 annual-report manifestation of the July 2024 honorary degree.

Capture: preserved the 78-page PDF, response headers, and layout-preserving extracted text under `assets/captures/2026-08-08-st-marys-annual-report/`.

Evidence handling: added SRC-370/C-380. The report records the honorary degree and repeats St Mary's “one of the youngest ever Professors at Cambridge” wording. This is a source-version of the award and institutional description, not independent ranking evidence or current employment proof.

# 2026-08-08 — SRC-371–SRC-373 Drake Primary School SRB records

Discovery: current Drake pages and an indexed SRB newsletter exposed a school naming record, a school-created biographical display, and a first-party account of a visit by Jason Arday to the Arday Class.

Capture: preserved both current HTML pages, response headers, the linked 1414×2000 display image, and the three-page newsletter with extracted text under `assets/captures/2026-08-08-drake-arday/`. A related 2023 self-evaluation PDF endpoint returned 404 on the shell recheck; no binary was claimed from that failed endpoint.

Evidence handling: added SRC-371–SRC-373/C-381–C-383. The newsletter supports a school-account visit and child quotation. The school's autism, speech, literacy, age, Cambridge, and fundraising wording is retained as host-published repetition and not upgraded to independent corroboration.

# 2026-08-08 — SRC-374 UKCGE Annual Report 2023–24

Discovery: a current search for new institutional/event records surfaced UKCGE's 2023–24 annual report, which was not present in the existing UKCGE interview and brochure records.

Capture: preserved the 9-page PDF, response headers, extracted text, rendered PDF page 7/printed page 12, and extracted keynote portrait under `assets/captures/2026-08-08-ukcge-annual-report/`.

Evidence handling: added SRC-374/C-384. The report retrospectively records Arday's 2–3 November 2023 Sheffield keynote, summarizes remarks, and credits a photograph to Annette Rubery. The report is a host account, not a transcript or independent current-affiliation record.

# 2026-08-08 — SRC-375 London Post UWL/KCL BME ECR report

Discovery: a current-event search surfaced a 20 July 2026 London Post report on the tenth UWL/KCL Black Minority and Ethnic Early Career Researchers Conference.

Capture: preserved the article HTML, response headers, and 1270×924 featured photograph under `assets/captures/2026-08-08-uwl-bme-ecr-conference/`.

Evidence handling: added SRC-375/C-385. The article reports an Arday keynote and inaugural Legacy Leadership Award, but is secondary “Ldn-Post” coverage. The featured image does not identify Arday, and first-party UWL/KCL confirmation remains open.

# 2026-08-08 — SRC-376 Shoba Arun BSA plenary post

Discovery: a targeted post-event search found Shoba Arun's public LinkedIn post, dated 9 April 2026, referring to a BSA plenary with Jason Arday.

Capture: preserved the public HTML and response headers plus all three attached LinkedIn images under `assets/captures/2026-08-08-bsa-plenary-linkedin/`.

Evidence handling: added SRC-376/C-386. Image 1 shows Arday presenting beneath the dated BSA plenary slide, corroborating delivery of the scheduled “Wanted Dead or Alive: The Playbook” session. The post does not expose a recording, transcript, or complete account of the talk.

# 2026-08-08 — SRC-377 30 in 35 Wayback campaign blog

Discovery: the user supplied two 2010 Internet Archive snapshots of `30in35.wordpress.com`, the contemporaneous campaign blog.

Capture: preserved the supplied home and page-4 HTML snapshots, response headers, and extracted embedded-image URL manifest under `assets/captures/2026-08-08-30in35-wayback/`.

Evidence handling: added SRC-377/C-387. The blog gives first-person campaign details that materially strengthen the 2010 marathon record: the £100,000-at-17 goal, seven months of 12–14-mile daily training, Richmond upon Thames College sports-lecturer work, 3 a.m. starts, routes, beneficiary charities, marathon 22 and 29 updates, and planned 22 August finish. These remain contemporaneous self-report, separate from later aggregate totals and independent accounting. Linked photograph binaries were not recovered from the archived endpoints.

# 2026-08-08 — SRC-378 JustGiving current fundraiser source-version

Discovery: the exact canonical JustGiving URL for SRC-084 remains live in a changed platform presentation. Search results and direct retrieval exposed the current “Fundraiser complete” state, donation summary, fuller story, and a page-linked portrait.

Capture: preserved the current page HTML, response headers, 316×630 cover portrait, and image headers under `assets/captures/2026-08-08-justgiving-30in35/`.

Evidence handling: added SRC-378/C-388 as a source-version linked to SRC-084, not a duplicate fundraiser. The current platform display reports £6,285.00, £1,045.77 Gift Aid, and 216 donations. Its self-authored story supplies a December 2002 shelter account and £250,000-before-50 target, which remains distinct from the 2010 blog's £100,000-before-25 wording.

# 2026-08-08 — volatility recheck: Cambridge and AP

Discovery: the current-state search surfaced already-catalogued Cambridge and AP records, so their exact endpoints were rechecked for changed-state evidence rather than promoted as duplicate sources.

Capture: preserved the 8 August AP HTML/headers and the exact Cambridge official-notice and Faculty-profile HTML/headers under `assets/captures/2026-08-08-volatility-recheck/`.

Evidence handling: AP's normalized article paragraphs are unchanged from the 7 August capture; only page chrome/counters changed. Cambridge's official notice remains HTTP 200 and byte-identical to its 7 August body, while the Faculty profile remains HTTP 404 with the same body as the earlier 404 capture. The recheck therefore adds version/access provenance but no new claims or source IDs. An accidentally tested non-canonical Cambridge URL returned 404 and is retained only as a clearly labeled failed endpoint capture, not as evidence about the official notice.

# 2026-08-08 — SRC-335 The Atlantic source-version upgrade

Discovery: a current search resurfaced Daniel Engber's Atlantic feature “Icarus in the Faculty Lounge,” published 6 August 2026. It was already catalogued as SRC-335, so the work was handled as a source-version upgrade rather than a new source.

Capture: preserved the article HTML, response headers, and the credited 2853×1605 grayscale portrait under `assets/captures/2026-08-08-atlantic-icarus/`.

Evidence handling: upgraded SRC-335 and expanded C-327/C-328. The record separates article facts, memoir/proposal self-report, sensitive health/crisis material, narrative discrepancies, attributed allegations, and publisher/contact nonresponse. The article's discussion of the proposal is preserved as a report about a document; no public proposal binary or full text is claimed, and no duplicate source or claim ID was created.

# 2026-08-06 — SRC-379 Nathan Cofnas research-integrity analysis

Discovery: the user supplied a side-by-side comparison image from Nathan Cofnas's 21 July 2026 article, “DEI Fraud and Cover-Up at Cambridge.” Direct retrieval confirmed the article and exposed its linked primary-text targets and publication-correction discussion.

Capture: preserved the public article HTML and response headers under `assets/captures/2026-08-06-cofnas-dei-fraud/`. The article embeds many comparison images; the HTML preserves their source URLs, while no claim is made that every derivative image has been separately downloaded.

Evidence handling: added SRC-379/C-389–C-392. The record treats the displayed overlaps and reported quote/method reuse as serious allegations, keeps Cofnas's political framing separate, and distinguishes specific textual evidence from his broader claim that Arday's qualitative work is not genuine scholarship.

# 2026-08-06 — OpenAlex author-linked scholarly-output recheck

Discovery: the OpenAlex author node `A5048886069` was queried for works dated from 2025-01-01 onward after a fresh exact-name publication search.

Capture: preserved the seven-result JSON response and response headers under `assets/documents/openalex-jason-arday-2025-2026.*`; the response returned two OSF DOI versions, one undated OSF manifestation, the BMJ Open protocol, the 2025 co-authored book, its foreword, and a second book manifestation.

Deduplication and evidence handling: all seven results map to existing canonical records, so no new source or publication claim was created. Updated SRC-203 and added C-393. OpenAlex is retained as a discovery/index boundary, not as independent proof of identity or completeness.

# 2026-08-06 — SRC-380 Runnymede Trust regulator-record reconciliation

Discovery: a Charity Commission search surfaced the Runnymede Trust's full-print record and linked 2024 accounts and trustees' report, a material governance source not previously represented in the registry.

Capture: preserved the regulator HTML, response headers, 48-page accounts PDF, extracted text, and a rendered copy of printed page 33/PDF page 32 under `assets/captures/2026-08-06-runnymede-charity-record/`. The report was submitted on 28 July 2025 and covers the year ended 31 December 2024.

Evidence handling: added SRC-380/C-394. The report lists Professor Jason Arday under “Resigned Trustees 2024” and states “Resigned November 2024,” independently corroborating the Companies House termination filed for 18 November 2024. Updated the affiliation ledger, timeline, biography, and negative-space record. This strengthens the classification of later present-tense Runnymede biographies as stale or contradictory without resolving unrelated RSA, CLASS, or other role claims.

# 2026-08-06 — Royal Society profile shell-state recheck

Discovery: a fresh exact-profile request was made while reconciling the Royal Society biography against the newly captured Runnymede regulator report.

Capture: the canonical shell endpoint again returned HTTP 403. The repeated body and new response headers were preserved under `assets/captures/2026-08-06-royal-society-profile-recheck/` and linked from SRC-134.

Evidence handling: no new claim or source ID was created. The profile’s browser-visible wording remains a dated institutional source-version; the repeated shell 403 is an access boundary, not evidence that the profile or any role has been removed.

# 2026-08-06 — SRC-381 LJMU research-integrity annual statement boundary

Discovery: LJMU's current research-integrity reports page exposed an approved 17-page annual statement for academic year 2024–2025.

Capture: preserved the page, response headers, 17-page PDF, extracted text, PDF headers, and rendered statistics page under `assets/captures/2026-08-06-ljmu-research-integrity-2024-25/`.

Evidence handling: added SRC-381/C-395. The statement reports one plagiarism investigation upheld in full and one misrepresentation investigation not upheld, but names no people or cases. Because public reporting places allegations about Arday in September 2025, after the statement's reporting period, the document is recorded as institutional context and a negative-space boundary rather than attributed evidence. Reopen only when LJMU publishes the 2025–2026 statement, a named official outcome, or a changed institutional case record.
# 2026-08-06 — C-396 direct page-level check of thesis-overlap example

The screenshot example associated with Nathan Cofnas’s 21 July 2026 article was checked against the preserved public PDFs. Arday’s 2015 LJMU thesis PDF p. 17 (printed p. 17) contains the “Although, student teachers on one course may experience a common programme” paragraph. Paula Zwozdiak-Myers’s 2009 Brunel thesis PDF p. 12 (printed p. 1) contains the corresponding “Although student teachers on one course, in very large measure, experience a common programme” paragraph. The two passages preserve the same progression and substantial distinctive wording, with visible edits in Arday’s version. Two page renders were added under `assets/captures/2026-08-06-thesis-overlap-pages/`, with SHA-256 hashes recorded in SRC-209.

Evidence handling: this upgrades the screenshot from a secondary display to a directly checked textual relationship between two public primary documents. It does not establish intent, authorship history, permission, or a university finding. The broader computational analysis and all allegations remain separately classified.

# 2026-08-06 — C-391 correction-text audit

The Cambridge-repository-hosted two-page correction for Arday’s 2018 *Social Sciences* article was checked directly with `pdftotext`. It explicitly says that the original article identified adaptation from Memon et al. (2016) in Section 4 but had omitted overlap in earlier sections; it lists the sections where citations were inserted and states that the scientific conclusions were unaffected and the correction was approved by the Editor-in-Chief. C-391 was tightened to use this primary correction wording rather than relying on Cofnas’s characterization. The 2024 Taylor & Francis correction remains separately classified because its direct publisher HTML/PDF is still blocked and its indexed text is the preserved evidence layer.

# 2026-08-07 — C-392 direct quotation comparison and Memon comparator capture

Direct PDF comparison found an extended shared participant quotation in Arday’s 2018 *Social Sciences* article (PDF p. 14) and 2021 *Higher Education* article (PDF p. 17 / printed p. 95). Both passages discuss improving English, difficulty articulating concerns to university healthcare professionals, reluctance to discuss psychological issues, and fear of heavy medication; the participant descriptors differ: 2018 says “Female, Asian, UG, 4,” while 2021 says “Female, Latin-American, Female, Academic, 38.” The 2016 Memon et al. BMJ Open article, which Arday’s 2018 correction names as an omitted/added citation source, was recovered as a public 9-page PDF and added as SRC-382. Three page renders preserve the two Arday passages and the Memon language/methodology context.

Evidence handling: this upgrades C-392 from a reported allegation to a documented textual relationship with precise pages, while leaving quotation provenance, participant identity, permission, intent, and institutional adjudication unresolved. The 2022 precarious-employment methods comparison remains a separate lead and was not promoted to an equivalent finding.

# 2026-08-07 — C-398 bounded methods-lineage comparison

Compared the methods sections of Memon (2016), Arday (2018), and Arday (2022). All three describe a broadly similar qualitative sequence—anonymous questionnaires, focus groups/interviews, audio recording and transcription, and notes/flipcharts—but their samples, settings, numbers, timing, questionnaire handling, and wording differ. Added SRC-383/C-398 as a bounded audit. This does not establish copied methods; sentence-level comparison and underlying provenance evidence would be required for a stronger conclusion.

# 2026-08-07 — SRC-384 NHS RHO current profile source-version

Discovery: the current NHS Race & Health Observatory Academic Reference Group page was selected as the next institutional-role reconciliation target because the earlier SRC-140 record exposed the page contents but lacked a local HTML capture.

Capture: preserved the current page HTML and response headers under `assets/captures/2026-08-07-nhs-rho-current-profile/`. The HTML is 126,161 bytes with SHA-256 `6c5feb4f400c9c62f739c8da3563d290d81fc44d9b786d945be44ef41621f864`; the headers hash is `55468dba566e827e89b88874f7619c217721b4d7cfac8729dfc8befb0a62708e`.

Evidence handling: added SRC-384/C-399. The page directly establishes the NHS RHO host's current published biography wording, including Ohio State ODI, Glasgow, Durham, ALT, Get Further, BSA, NHS RHO, and ITV descriptions. It does not establish current employment, legal appointment status, post-resignation Cambridge/Jesus status, duration, remuneration, or operational activity. Its omission of Runnymede is preserved as a source-version difference, not treated as a termination finding.

# 2026-08-07 — C-400 Cambridge indexed/live profile split

Discovery: an exact-name search surfaced a newer search-index snippet for Cambridge's canonical Faculty profile. The indexed text used “Former Trustee” for Runnymede, retained BSA/NHS RHO/ITV memberships, named Nelson Mandela University as a visiting-professor role, and omitted Ohio State and Durham honorary-professor wording.

Verification: a direct shell request and the in-app browser both returned the Faculty page's 404 state. The direct 404 body captured in this pass differs from the earlier preserved body and is retained under `assets/captures/2026-08-07-cambridge-faculty-profile-reappeared/` with hashes recorded in SRC-208.

Evidence handling: updated SRC-208 and added C-400. The indexed snippet is retained as an access/version boundary, not as a live Cambridge profile, current employment proof, or institutional outcome. No new source ID was created because the canonical URL and underlying source family are already represented.

# 2026-08-07 — C-401/C-402 bounded caption extraction from preserved videos

The existing local binaries for SRC-264 (BILT keynote teaser) and SRC-265 (Lancaster commentary) were checked against their preserved automatic English captions. BILT's 89-second captions contain first-person remarks about a Bristol relationship beginning in 2018, approximately 15–16 visits in six years, and influential work with Bristol's EDI team. Lancaster's 507-second captions contain Chris Marlow's retelling of Arday's childhood, education, and Nelson Mandela University role, including the “didn't write until 18” wording.

Evidence handling: added C-401/C-402 and expanded both source records. These are timestamped caption-derived source versions, not manually verified quotations. BILT is first-person self-presentation; Lancaster is host commentary. No employment, clinical, school, degree, or role claim was upgraded to independent fact, and the “write until 18” wording remains separate from the “read until 18” family of claims.

# 2026-08-08 — Preserved-media integrity check for SRC-264–SRC-266

Verification: the locally preserved BILT teaser, Lancaster commentary, and Beacon College profile were each passed through the local media decoder. The video-only MP4 and audio M4A for all three sources decoded without errors; preserved metadata gives runtimes of 89 seconds, 507 seconds, and 361 seconds respectively.

Evidence handling: this closes the file-integrity check, not the human-transcription check. BILT and Lancaster remain caption-derived source versions pending listening against the audio; Beacon has no exposed public subtitle track and remains without substantive extraction. No claim was promoted, no stream was remuxed, and the same YouTube IDs should not be searched again unless their access state changes.

# 2026-08-08 — UCL “Learning to fly” keynote deck recovery

Discovery: the current UCL anniversary page still exposes its “Download ‘Learning to fly’ keynote lecture slides” endpoint. The linked first-party PPTX returned HTTP 200 and was captured alongside the page HTML and response headers under `assets/documents/ucl-learning-to-fly-2020/`.

Capture: the 16-slide deck is 67,699 bytes with SHA-256 `7a2d7bac78e9796529f916fd713d72b94d055f96fdfa51a324fcf7e5782e9e73`; the page and download headers are separately preserved. Slide text was inspected from the PPTX package. The deck identifies the 16 March 2020 UCL keynote and records its sequence of themes, including decolonising the curriculum, intersectionality, inclusive pedagogies, unconscious bias, and centring race/racism in curricula.

Evidence handling: upgraded the existing SRC-031 event record rather than creating a duplicate source node. Added C-694 for the deck’s authored presentation content and slide-level attribution. The deck is not treated as an independent evaluation or video transcript, and no long quotation was reproduced.

# 2026-08-08 — Routledge *Cool Britannia* current source-version recheck

Discovery: the unresolved publication-family queue identified *Cool Britannia and Multi-Ethnic Britain* as a candidate for a changed publisher state. The canonical Routledge page returned HTTP 200 on 8 August 2026 and was not byte-identical to the 6 August capture.

Capture: the current HTML, response headers, and the linked 180×284 Routledge Focus cover were preserved. Meaningful product fields remained stable: copyright 2020, 106 pages, the existing paperback/hardback/ebook ISBN family, and the publisher’s present-tense Durham Assistant Professor biography.

Evidence handling: updated SRC-030 in place and added C-695. The page is a new source-version and image manifestation, not a second monograph or independent employment corroboration. The earlier PagePlace preview and chapter DOI family remain canonical for their respective evidence classes.

# 2026-08-08 — Simon & Schuster UK author-page access boundary

Discovery: the publisher’s indexed web presence exposed a distinct Jason Arday author route separate from the memoir’s product pages, audiobook record, and Speakers Bureau biography.

Verification: a direct request returned Cloudflare HTTP 403 with no author-page body, title list, biography, image URLs, or structured metadata. Preserved the response body and headers under `assets/captures/2026-08-08-simon-schuster-author-page/`.

Evidence handling: added SRC-547/C-696 as an access-state record only. No indexed snippet was promoted to content, no duplicate memoir node was created, and the route should not be repeated without a changed endpoint or lawful archive/asset.

# 2026-08-07 — C-403 OpenAlex exact-query closure

The filtered OpenAlex works request for author `A5048886069` was rerun with `per-page=200`. It returned 56 records. A normalized comparison of record IDs, DOI strings, and titles against the 6 August response was byte-identical, so no new work key or DOI/title candidate was added.

Capture: preserved the 805,966-byte JSON response and 1,545-byte response headers under `assets/documents/openalex-jason-arday-works-recheck-2026-08-07.*`, with hashes recorded in SRC-284.

Evidence handling: added C-403 and closed this exact query family for the current pass. This is a discovery-index boundary, not proof of authorship or completeness; future work should use publisher/repository leads or a changed OpenAlex result.

# 2026-08-07 — SRC-385/C-404 Durham chapter index manifestation

Discovery: an exact-title search surfaced Durham's Department of Sociology output index as a second institutional repository URL carrying “Understanding, addressing and centring BAME Leadership in Higher Education” (2021), Jason Arday authorship, and the Thomas/Arday edited-volume context.

Evidence handling: added SRC-385/C-404 as a source-version linked to SRC-081. The direct repository remains Cloudflare-protected, and no DOI, pagination, publisher chapter URL, abstract, or full text was recovered. This strengthens listing-level provenance without duplicating the publication or upgrading unresolved bibliographic fields.

# 2026-08-07 — SRC-074 teacher-education preview recheck

The exact public PagePlace preview endpoint for Arday's 2019 teacher-education chapter was rechecked. It returned HTTP 200 and a 34-page PDF byte-identical to the 6 August capture (SHA-256 `35a9d220cc49c60e49e5b4dba997a5ff81f03e4838d11b5093fd4259c5417460`). No new edition, chapter text, DOI resolution, or publisher/repository manifestation appeared.

Evidence handling: updated SRC-074/C-096 in place and preserved the new response headers. The endpoint is closed for this pass; future work requires a changed binary or concrete new lead.

# 2026-08-07 — SRC-386 Arasite comparison dossier

Discovery: the public Arasite index at `plagmenu.html` states that four files were submitted to Liverpool John Moores University and Cambridge's Research Integrity Office in September 2025. It names Dave Harris and colleagues as compilers, mentions Jack Grove and other academic checkers, and thanks David Sanders of Purdue University.

Capture: downloaded `plag1.zip` through `plag4.zip`, each containing a DOCX comparison file, plus the index HTML/headers and the linked `ardayimage.html` access-boundary page. The image page points only to a local Windows `file:///` path, so no diagram was available at the public URL.

Initial extraction: `plag1` compares thesis passages with Zwozdiak-Myers; `plag2` adds an Aderibigbe et al. teacher-education comparison; `plag3` adds a Douglass/Smith/Smith peer-mentoring comparison; `plag4` is a larger final grid with Zwozdiak-Myers comparisons, near-identical ordered literature lists, and reference-list observations. The archive records these as inspectable leads and preserves the binaries; it does not promote the dossier's labels or submission claims into an institutional finding.

# 2026-08-07 — SRC-387 Aderibigbe comparator verification

The official TEAN Journal PDF was downloaded from the University of Cumbria host. A page-level comparison against Arday's preserved thesis confirms that Arday thesis PDF p. 84 and Aderibigbe et al. printed p. 18 share an unusual “voluminous … concept … applications” scaffold and a “collaborative … personal and professional development” sequence. The full paragraphs are not verbatim: wording, sentence structure, citations, and surrounding context differ. Arday's extracted thesis bibliography contains no `Aderibigbe` entry.

This pass narrows rather than amplifies the dossier's “near-verbatim” label. Because the 2014 article cites Aderibigbe's 2013 *Management in Education* article, that earlier primary source is the next provenance target; its full text was not exposed by the public ERIC/SAGE metadata pass.

# 2026-08-07 — SRC-388 Aderibigbe 2013 provenance boundary

ERIC metadata and abstract identify Aderibigbe's 2013 *Management in Education* article and DOI `10.1177/0892020612471698`. The DOI/SAGE request returned HTTP 403/Cloudflare challenge HTML; ERIC exposed metadata but no full text. The article is recorded as a distinct provenance target, not as a duplicate of the 2014 TEAN comparator.

# 2026-08-07 — SRC-389 Douglass/Smith comparator verification

The Arasite `plag3` lead was checked against a public Douglass/Smith PDF hosted in the HKU 2010 conference archive. Arday thesis pp. 308–310 and the public PDF pp. 1–2 share a long sequence in the same order, including distinctive wording about additional instructional support/outlets, instructor pressure, mentor reflection, the Heirdsfield citation, emotional support, reduced intimidation, “more comfortable with the material,” and writing-intensive courses. The public PDF appears related to the published Douglass/Smith/Smith 2013 article, whose Taylor & Francis full-text endpoint returned HTTP 403; the archive therefore treats it as a source-version/precursor rather than silently substituting it for the version of record.

# 2026-08-07 — SRC-390/SRC-391 Hussain and Kahn comparator verification

The Cofnas article’s two remaining comparison images were extracted from the preserved HTML and downloaded as local PNGs. The linked Hussain article was recovered from ERIC as a public PDF; the linked Kahn article was recovered from the University of Liverpool repository as a public PDF. Direct comparison confirms the Hussain p. 53 / Arday thesis p. 348 relationship across two passages and the Kahn/Arday ordered reflective-practice discussion shown in the image. The Kahn image’s page references point into Kahn’s discussion of Edwards/Nicoll and Fanghanel, so those underlying works remain separate provenance targets. The thesis text contains a different 2006 Khan report but no matching Hussain or Kahn 2008 bibliography entry.

# 2026-08-07 — SRC-392/SRC-393 underlying Kahn provenance audit

Fanghanel’s 2004 author-accepted manuscript was recovered from the University of West London repository. It independently supports the programme/workplace dissonance frame and the practice/structure/ideology/epistemology dimensions, but the recovered Arday passage follows Kahn’s 2008 review more closely than Fanghanel’s wording. Edwards/Nicoll’s 2006 bibliographic record and abstract were verified through ERIC and Stirling; Stirling marks the published-version PDF under embargo, and both attempted full-text routes returned non-article access/error responses. No direct Edwards/Nicoll comparison is claimed.

# 2026-08-07 — SRC-211/SRC-213/C-420 world-history-of-sociology volume boundary

A current Université Paris Cité / Global Research Institute profile for co-editor Stéphane Dufoix was captured. It still describes the Dufoix/Mosbah-Natanson *Histoire mondiale de la sociologie* project as forthcoming from La Découverte in 2023. This is stale project copy, not evidence that the volume was never published. George Steinmetz’s already preserved 2024 CV remains the dated volume-level witness for *Une histoire mondiale de la sociologie* at La Découverte. Neither source names Jason Arday or resolves the Durham-indexed English chapter’s DOI, pages, or full text; the chapter remains an unresolved lead.
## 2026-08-08 — SRC-406/C-444–C-445: next final-grid segment audited

The next distinct mapped segment in the preserved `ARDAY FINAL GRID.docx` was checked directly against the local thesis PDFs: Arday printed pp. 61–62 against Zwozdiak-Myers printed p. 35 onward. The comparison confirms the same critical-reflection/action-research subsection, ordered source cluster, and extended close textual/structural correspondence, with rephrasing, citation changes, and study-specific additions. The dossier’s “near-verbatim” label is retained as an attributed allegation; no plagiarism, intent, or institutional finding is inferred. The pp. 57–60 / 32–35 opening segment remains closed under SRC-405 and was not repeated.

## 2026-08-08 — SRC-407/C-446–C-447: collaborative action-research segment audited

The next distinct final-grid range was checked directly: Arday printed pp. 63–64 against Zwozdiak-Myers printed pp. 45–47. Both texts use the same ordered discussion of collaborative action research, peer trust, equity and social justice, McNiff et al.’s four outcome categories, action research as educational reform, and Price’s study of 11 student teachers with the same four teaching domains and broad findings. Arday rephrases portions and adds or changes citations and study-specific framing. This is logged as a bounded primary-text relationship, not a determination of plagiarism, intent, or institutional responsibility.

## 2026-08-08 — SRC-408/C-448–C-449: self-reflection segment audited

The next distinct final-grid range was checked directly: Arday printed pp. 65–66 against Zwozdiak-Myers printed pp. 47–49. Both texts move through Price’s student-teacher challenges, practitioner self-inquiry, theories-in-use, self-reflection, connected teaching, self-study/identity, reflective conversations, and Palmer’s personal-values account in the same order, with repeated close textual/structural correspondence. Arday rephrases portions and adds or changes citations and study-specific framing. No determination of plagiarism, intent, or institutional responsibility is inferred.

## 2026-08-08 — SRC-409/C-450–C-451: Boud/Korthagen/Kolb segment audited

The next distinct final-grid range was checked directly: Arday printed pp. 67–68 against Zwozdiak-Myers printed pp. 49–50. Both texts present Boud’s four stages, critique numbered reflection recipes, list the same nine Korthagen/Vasolos questions, and move through the same four-stage Kolb cycle in the same order. Arday rephrases portions and adds or changes citations. This is logged as a bounded primary-text relationship, not a determination of plagiarism, intent, or institutional responsibility.

Follow-up capture: rendered the four underlying primary pages locally as `assets/captures/2026-08-08-arasite-self-reflection-67-68/` and attached the images and SHA-256 values to SRC-409. This preserves the page-level evidence without creating a second source or claim pair.

## 2026-08-08 — SRC-410/C-452–C-453: Kolb continuation boundary audited

The next mapped row was checked directly: Arday’s printed p. 69 Kolb-continuation paragraph against Zwozdiak-Myers printed p. 50. The same self-perpetuating experiential-learning, actor/observer, new-experience, non-standardized-practice, and observation-to-improvement sequence appears with rephrasing and citation/study-specific changes. The grid does not map Arday’s subsequent “Learning with Colleagues” section or p. 70, so those pages were not upgraded or treated as audited.

Follow-up capture: rendered the two underlying primary pages locally under `assets/captures/2026-08-08-arasite-kolb-continuation/` and attached their hashes to SRC-410. The unmapped “Learning with Colleagues” section remains outside scope.

## 2026-08-08 — SRC-411/C-454–C-455: autonomy/professional-development segment audited

The next mapped range was checked directly using printed pagination: Arday pp. 75–77 against Zwozdiak-Myers pp. 58–60. Both texts move through Dewey’s responsibility/open-mindedness/whole-heartedness, the Zeichner–Liston professional-development passage, Eraut’s three accountability points, Stenhouse/Hoyle/John, QTS/Standards, autonomy/responsibility, and Nixon’s educational-values passage in the same order. Arday rephrases portions and adds or changes citations. The intervening unmapped Arday pages were not inferred or upgraded.

Follow-up capture: rendered the six underlying primary pages locally under `assets/captures/2026-08-08-arasite-autonomy-professional-development/` and attached their hashes to SRC-411. The printed-page mapping and intervening unmapped boundary remain unchanged.

## 2026-08-08 — SRC-412/C-456–C-457: closing-summary segment audited

The next mapped block was checked directly: Arday pp. 79–81 against Zwozdiak-Myers pp. 80–82. Both summaries use the same ordered synthesis of reflective practice’s complexity, Calderhead, developmental/critical reflection, Schon, the dialogical other and critical friend, self-study/action research, formative evaluation, the “generic pedagogical principle,” and limited empirical evidence. Arday rephrases portions and changes/adds citations. Intervening unmapped pages were not inferred or upgraded.

Follow-up capture: rendered the six underlying primary pages locally under `assets/captures/2026-08-08-arasite-closing-summary/` and attached their hashes to SRC-412. The page mapping remains bounded to the closing-summary block.

## 2026-08-07 — SRC-283/C-458 Cambridge directory exact recheck closed

A fresh direct request to the Cambridge Faculty of Education “Our People” page-1 URL returned the same 72,378-byte body and the same hashes as the 6–7 August captures. The direct body still lacks Jason Arday, `jaa80`, and his professorial title, while search-index text continues to expose a conflicting apparent entry. This is recorded as an indexed/live mismatch and negative-space/source-version boundary, not as evidence about current employment or resignation. Do not repeat this exact endpoint without a changed response, confirmed pagination/API route, or directly rendered entry.

## 2026-08-07 — SRC-413/C-459–C-460 PASSHE conference source

A new first-party PASSHE conference family was captured. The overview and timetable identify a 10 June 2026 hybrid conference at Conference Aston and schedule Arday’s 11:00 keynote/Q&A, “We are where we are…”. The speaker page supplies a host biography and portrait, including formerly-held Runnymede wording and present-tense BSA/other-role wording. The event listing establishes planned participation, not delivery; no recording, transcript, slides, or post-event account was recovered.

## 2026-08-08 — SRC-414/C-461 Vimeo SPAIS video discovery

A fresh Vimeo search surfaced the public manifestation `574903785`, “Decol SPAIS Event 1: What is Decolonising the Curriculum?”. The page description names Jason Arday, Heidi Safia Mirza, and chair Alvin Birdi; oEmbed reports a 59:46 duration and 14 July 2021 upload date. The page, oEmbed JSON, headers, thumbnail, and player access response were preserved. Direct player/config requests returned 401/403 and exposed no downloadable video, captions, or transcript, so the event date and substantive claims remain unresolved.

## 2026-08-08 — SRC-415/C-462–C-463 BSA honorary-fellow annual report

A current Charity Commission accounts-page traversal exposed the BSA Trustees’ Annual Report for 1 April 2023–31 March 2024 as a downloadable PDF. Printed p. 17 lists Jason Arday under “2023 Honorary Fellows.” The later 1 April 2024–31 March 2025 report was also captured; its different 2024 Honorary Fellows list does not repeat Arday. The two report states corroborate the dated honour while preserving the later omission without inferring an end-date or revocation.
## 2026-08-08 — Cambridge Faculty profile changed-state recheck

The exact Cambridge Faculty profile URL was rechecked again and returned HTTP 404 with a 37,526-byte generic Drupal page whose body differs from the 7 August capture. The page contains no Arday profile or replacement link. The new HTML and headers are attached to SRC-208 as another changed-state manifestation, without creating a duplicate source or inferring a personnel outcome.

## 2026-08-08 — SRC-416/C-464–C-465: opening reflective-practice segment audit

Discovery: the preserved Arasite `ARDAY FINAL GRID.docx` contains an earlier mapped block not covered by the prior page audits: Arday printed pp. 35–36 against Zwozdiak-Myers printed pp. 9–10.

Verification: the LJMU and Brunel thesis PDFs were checked directly, and PDF pages 35–36 and 20–21 were rendered for visual inspection. Both texts share the phenomenological reflective-practice definition, the same terminology/reference sequence, and the same debate/systematic-research/absence-of-definition progression, with close wording across multiple paragraphs. Arday’s additions, substitutions, citation changes, and inserted material were retained in the comparison rather than described as uninterrupted verbatim copying.

Evidence handling: added SRC-416/C-464–C-465 as a bounded primary-text audit. This upgrades a specific grid lead to a reproducible page-level relationship but does not determine intent, intermediate sources, quotation standards, supervision, plagiarism, or institutional responsibility. The rendered pages and underlying PDFs remain separate from the dossier’s labels and from the earlier audited page ranges.

## 2026-08-08 — SRC-417/C-466–C-467: Ghaye reflective-practice segment audit

Verification: the next distinct mapped grid block was checked directly: Arday printed pp. 46–47 against Zwozdiak-Myers printed pp. 17–18, corresponding to PDF pages 46–47 and 28–29. Both texts introduce reflective practice as a discourse, cite the same Ghaye and Ghaye typology, reproduce the same five-category descriptive/perceptive/receptive/interactive/critical sequence, and continue through the same critical-versus-descriptive reflection and professional-development guidance argument with a shared reference cluster.

Evidence handling: added SRC-417/C-466–C-467 with four rendered page images. Arday’s additions, substitutions, citation changes, and study-specific wording are retained; the relationship is not characterized as uninterrupted verbatim copying and does not determine intent, intermediate sources, quotation standards, supervision, plagiarism, or institutional responsibility. Earlier audited ranges and unmapped pages remain separate.

## 2026-08-08 — SRC-418/C-468–C-469: Dewey/Van Manen segment audit

Verification: the next distinct mapped grid block was checked directly: Arday printed p. 53 against Zwozdiak-Myers printed pp. 29–31, corresponding to PDF pages 53 and 40–42. Both texts share the Dewey reflective-action question, the professional “doing” and modification sequence, the application to student teachers, the Van Manen practical-activity list, the technical/routine reflection discussion, and the Tinning/Grimmett scaffold, with overlapping references.

Evidence handling: added SRC-418/C-468–C-469 with the rendered primary pages. Arday’s inserted references, study-specific application, wording changes, and quotation-rendering differences remain explicit. The record is a bounded primary-text relationship, not a determination of intent, intermediate sources, citation standard, supervision, plagiarism, or institutional responsibility.

## 2026-08-08 — SRC-420/C-472–C-473: action-research row audit

Audited the distinct Arasite grid row mapping Arday printed pp. 61–62 to Zwozdiak-Myers printed pp. 44–45. The pages share the action-research heading, Whitehead framing, ordered conceptual sequence, and named-source progression, with edits and added citations preserved. Rendered page binaries and hashes are recorded in the source note. The result is bounded primary-text evidence, not an institutional finding or an inference about intent.

## 2026-08-08 — SRC-421/C-474–C-475: power-relations continuation

Audited the distinct grid row mapping Arday printed pp. 66–67 to Zwozdiak-Myers printed p. 48 (PDF p. 59). The short passage shares the prescribed-teaching/power-relations/core-values structure, with Arday’s sentence split, expansion, and citation frame preserved. It is recorded as localized primary-text evidence with a strict surrounding-text boundary. An earlier version of the record incorrectly reported printed p. 123; SRC-428 corrects the pagination without changing the comparison.

## 2026-08-08 — SRC-428/C-488: power-relations pagination correction

The preserved render `zm-059.png` visibly carries page number 48. The earlier “p. 123” label was therefore a source-record pagination error, not a second comparator location. Updated SRC-421, C-474/C-475, the timeline narrative, and Drive archive references; retained the correction as a separately linked source-version record.

## 2026-08-08 — SRC-429/C-489–C-490 Open University thesis acknowledgement lead

Discovery: a current Open University profile for Rehana Awan links her EdD thesis to Open Research Online record 109232. Indexed text from the public PDF exposes an acknowledgement thanking Professor Jason Arday for “sage advice” and knowledge of the academy and challenges faced by scholars of race.

Access boundary: the profile HTML was captured successfully, but the repository landing page and PDF returned Cloudflare HTTP 403. The acknowledgement is therefore recorded as an indexed-text witness, not as a locally inspected thesis page. No formal supervision, examining, employment, or co-authorship claim was added.

## 2026-08-08 — SRC-422/C-476: Coventry false-positive output lead

An exact-title scholarly search lead appeared to associate Coventry’s “Multi-faith in policy only?” article with Arday and Heidi Safia Mirza. Direct inspection of the first-party repository metadata and final published PDF identified Kristin Aune, Tom Fryer, Lucy Peacock, and Mathew Guest as the authors. The PDF, extracted text, repository HTML, headers, and first-page render are preserved; the lead is closed and excluded from Arday’s output bibliography.

## 2026-08-08 — SRC-423/C-477–C-478: Crossref recent-output boundary

Queried Crossref’s Works API for `query.author=Arday, Jason` from 1 January 2024 with a 1,000-item limit. The response yielded 19 surname matches; 13 were genuine Jason Arday records already represented by canonical works or aliases, and six were homonyms/unrelated authors. The raw API response and filtered reconciliation are preserved; no new DOI was added.

## 2026-08-08 — SRC-419/C-470–C-471: Whitehead autonomy continuation audit

Coverage check: the final-grid row spanning Arday pp. 77–78 and Zwozdiak-Myers p. 60 extended beyond SRC-411, which explicitly audited Arday only through p. 77. The newly uncovered p. 78 continuation was therefore selected; p. 77 is retained only as context and is not re-counted.

Verification: Arday printed p. 78 and Zwozdiak-Myers printed p. 60 share the Whitehead (1993) autonomy/personal-values passage, including the ordered elements of professional judgements and decisions, pedagogical strategies, assessment procedures, and the conclusion about personal values in teaching. Arday adds learning-objectives framing and changes the grammatical formulation.

Evidence handling: added SRC-419/C-470–C-471 with the two rendered pages. The record is a bounded primary-text relationship and does not determine intent, intermediate sources, applicable standards, supervision, plagiarism, or institutional responsibility.

## 2026-08-08 — SRC-424/C-479–C-481: Cofnas *Whiteness and Education* comparison images

Preserved two further comparison images from Nathan Cofnas’s 21 July 2026 post. The Rollock image displays three Arday/Rollock excerpts with substantial phrase-level and structural correspondence around racial microaggressions, Whiteness, and faculty-of-colour experience. A pagination/title check identifies the likely comparator as Rollock’s “Unspoken rules of engagement” article in the 2012 volume (p. 520), not the initially surfaced “Invisibility of race” article, whose pages are incompatible. The Hiraldo image displays a broader CRT discussion, but also shows an Arday citation to Hiraldo and explicitly does not label the passage as verbatim copying. The former is stronger as a research lead; the latter is intentionally bounded as a weaker, potentially ordinary-attributed-paraphrase comparison.

Captured the Rollock publisher response, the publisher’s Volume 25 Issue 5 page, the ResearchGate access-state response, and the UVM Hiraldo landing page. The issue page confirms Rollock’s 2012 volume/issue and pp. 517–532, and indexed full text independently exposes the wording shown in the Rollock image. The full Arday article and a downloadable Rollock PDF were not recovered, so the Arday side remains image-mediated and this is not a complete independent audit. Added C-482 with explicit boundaries; no plagiarism, intent, fabricated-participant, or institutional finding was inferred.
# 2026-08-08 — SRC-427/C-487 Cambridge College Fellows 2023–24 roster

Discovery: the official Cambridge University *Reporter* Special No. 3, **Fellows of the Colleges, 2023–24**, was recovered as a 76-page PDF. The publication is dated 21 December 2023 and says its college information was received through 31 October 2023.

Verification: the Jesus College section on PDF page 36 (printed page 33) lists “Arday Jason phd frsa”. This is a distinct institutional roster witness between the 2023 Cambridge appointment notice and the 2025–26 fellows roster. The archive records the roster inclusion only; it does not infer appointment date, continuous fellowship, credential validity, or status after the 2026 resignation.

Preservation: PDF, response headers, and derived layout text were saved under `assets/documents/cambridge-reporter-2023-24-college-fellows/`.
## 2026-08-07 — SRC-453/C-517: Douglass/Smith ResearchGate manifestation

Discovery: an exact-DOI search surfaced ResearchGate's indexed record for the 2013 Douglass, Dennie L. Smith, and Lana J. Smith article, *An Exploration of the Characteristics of Effective Undergraduate Peer-Mentoring Relationships* (DOI `10.1080/13611267.2013.813740`). The indexed record exposes the article metadata and abstract and describes the writing-intensive peer-mentoring study.

Verification: direct retrieval of the ResearchGate URL returned HTTP 403. The archive preserved the HTML and response headers but did not recover a PDF or article body. This is a distinct host manifestation of the article already connected to the public HKU conference precursor under SRC-389, not a second publication.

Decision: add SRC-453/C-517 for the new access-state and metadata witness. Do not claim version-of-record text, do not infer that the conference paper and published article are identical, and do not repeat the direct thesis comparison already bounded under SRC-389.
## 2026-08-08 — SRC-454/C-518: Durham Worktribe *Whiteness and Education* manifestation

Discovery: an exact DOI search surfaced Durham's indexed Worktribe item for Arday's article “Dismantling power and privilege through reflexivity: Negotiating normative Whiteness, the Eurocentric curriculum and racial micro-aggressions within the Academy.” The indexed record supplies the title, author, journal, volume/issue/pages, DOI, acceptance and online-publication dates, a 2018 publication field, and peer-reviewed status.

Verification: a direct request to the exact Worktribe item URL returned HTTP 403 challenge HTML. The challenge page and response headers were preserved locally; no repository PDF, submitted manuscript, or article body was recovered.

Decision: add SRC-454/C-518 as a distinct first-party repository manifestation, deduplicated to SRC-043 and kept separate from the earlier OpenAlex/Durham and CORE/OpenAIRE boundary records. The article text and Cofnas/Rollock comparison remain unresolved.
## 2026-08-08 — SRC-455/C-519: Walthamstow School for Girls biography witness

Discovery: a targeted football search surfaced an undated Walthamstow School for Girls Black History Month page, “Reclaiming Narratives,” with a Jason Arday biography and a linked 400×280 image.

Verification: the page relays the delayed-speech/literacy narrative, Clapham setting, a first-person football/professional-snooker aspiration, and an age-22 account of pursuing postgraduate study while working as a PE lecturer and studying sociology at night. The captured HTML exposes no publication date; the image server reports `Last-Modified: Fri, 04 Jul 2025`, which is treated only as image-server state.

Evidence handling: added SRC-455/C-519 and preserved the page, headers, image, and image headers. The page is a school-hosted biography repost, not evidence that Arday attended the school, and it does not independently establish professional football, professional snooker, employment, or the underlying interview’s date.
## 2026-08-08 — SRC-456/C-520: SAGE *Management in Education* manifestation

Discovery: an exact DOI search surfaced SAGE’s official record and indexed PDF manifestation for Arday’s 2018 *Management in Education* article on BME educational leadership. The publisher page exposes the publication metadata, abstract, article structure, and a contemporaneous author biography.

Verification: the SAGE PDF, EPUB, and alternate PDF routes returned HTTP 403 challenge HTML when requested directly. The challenge HTML and headers were preserved locally. The archive already holds Roehampton’s accepted author manuscript under SRC-027; no publisher version-of-record binary was silently substituted or claimed.

Decision: add SRC-456/C-520 as a distinct publisher manifestation/access boundary deduplicated to SRC-027. Preserve the publication-time Roehampton/Ohio State/Runnymede biography as a dated source-version, not current-role evidence.

## 2026-08-07 — SRC-027 Roehampton manuscript endpoint recheck

The Roehampton accepted-manuscript URL for the 2018 *Management in Education* article was rechecked. The endpoint returned HTTP 403 with a Cloudflare challenge and an HTML body of 5,810 bytes, despite the requested `.pdf` path. The body was renamed with an `.html` extension and preserved with response headers.

Decision: update SRC-027’s dated access-state trail only. No second manuscript, publisher PDF, or new publication node was created; the previously preserved 16-page accepted author manuscript remains the local article text.

## 2026-08-08 — SRC-457/C-521: Glasgow published-version provenance correction

Discovery: following the Roehampton/SAGE manuscript trail, the current University of Glasgow Enlighten item for DOI `10.1080/01425692.2022.2074375` was retrieved at `https://eprints.gla.ac.uk/270719/`. Its document row explicitly labels `270719.pdf` “Published Version” and links a CC BY-NC-ND licence.

Verification: the item page marks the record Published and Refereed, supplies the acceptance date (3 May 2022), first-online-publication date (25 June 2022), journal citation, DOI, and licence. The downloaded 22-page PDF has SHA-256 `f38e339b9f32c27c4ab6d8e1f2d4b47bb0c2dd9e202a42ea76f1167d44c0a735`, matching the PDF already preserved under SRC-051. A direct Taylor & Francis PDF request returned HTTP 403 challenge HTML, which was preserved as an access boundary rather than mislabelled as a PDF.

Decision: add SRC-457/C-521 as a distinct repository manifestation and correct SRC-051, the public-output index, timeline, and biography from “accepted manuscript” to “Glasgow repository published version.” Keep it deduplicated to the same DOI/publication and do not claim byte identity with a publisher CDN object or treat repository provenance as validation of the article’s substantive claims.

## 2026-08-08 — SRC-458/C-522: PASSHE conference post-event state

Discovery: a current PASSHE member-events index was checked against the open conference-delivery boundary under SRC-413. The page places “PASSHE National Conference 2026 (In-Person and Online)” in its past June 2026 events and gives the 10 June date, Conference Aston venue, and hybrid schedule.

Verification: the page says the 2026 conference “was delivered in hybrid format” in response to member feedback. It does not name Arday, identify the scheduled keynote as delivered, or expose a recording, transcript, slides, or attendance record.

Decision: add SRC-458/C-522 as a distinct current source-version for event-level state, deduplicated to the existing conference family. Upgrade only the conference-level state from scheduled to host-described as delivered; retain Arday’s participation as unresolved and do not infer it from the host’s general statement.

## 2026-08-08 — SRC-459/C-523: Cambridge directory changed-state pagination sweep

Discovery: the Cambridge Faculty of Education “Our People” page was returned by a fresh search-index result as a candidate current Arday entry. Unlike the earlier repeated page-1 capture, the live HTTP 200 response changed in size and the rendered staff slice changed.

Verification: the new page-1 body still contains no `Jason Arday` or `jaa80`. A bounded sweep of query states `page=0` through `page=40` likewise found no Arday identifier in any returned body. Page 5 does contain the generic role title “Professor of Sociology of Education,” but the associated person is Jo-Anne Dillabough. All 41 bodies and a checksum manifest were preserved; the page-1 response headers were captured separately.

Decision: add SRC-459/C-523 as a changed directory source-version, not as evidence of a current-role change. Keep the search-index snippet, individual-profile 404, and rendered-directory negative space as separate evidence states. Reopen only with a directly rendered entry, a confirmed API/data route, or another material endpoint change.

## 2026-08-08 — SRC-460/C-524: Dennis McCarthy propagation witness

Discovery: a focused search for additional discussion of the Cofnas examples surfaced Dennis McCarthy’s 24 July 2026 Substack post, “Who Plagiarized More: Jason Arday—or Shakespeare from North?”

Capture: preserved the public HTML, response headers, and page cover image. The post repeats Cofnas’s “36 instances” claim, describes the yellow/green comparison convention, and links the original Cofnas article.

Evidence handling: classified the item as low-provenance secondary commentary. It adds no independent audit or new primary text, so its repeated count is not added to the archive’s comparison tally and its “plagiarism”/“cover-up” language is not adopted as an institutional finding. The primary PDFs and bounded page audits remain canonical.

## 2026-08-08 — SRC-461/C-525: DeepDyve Aderibigbe comparator boundary

Discovery: the unresolved Aderibigbe (2013) comparator search surfaced a DeepDyve indexed manifestation for the exact *Management in Education* article and DOI already identified under SRC-388.

Capture: the public search/index layer supplied the article title and 1 April 2013 date. A direct request to the exact DeepDyve URL returned a Cloudflare challenge; the challenge HTML and headers were preserved and no article text, page images, or PDF was recovered.

Decision: add SRC-461/C-525 as a distinct comparator-side host manifestation, deduplicated to the canonical publication. Keep the 2013 text unresolved and do not expand the Arday comparison beyond the separately recovered 2014 source-version.

## 2026-08-08 — SRC-462/C-526: direct SAGE Aderibigbe publisher boundary

Discovery: the exact publisher URL behind the Aderibigbe (2013) DOI was tested as a separate endpoint after the DeepDyve pass.

Capture: SAGE returned HTTP 403 with a Cloudflare managed challenge. The response contained no article body, preview, XML, page images, or PDF; HTML and headers were preserved.

Decision: add SRC-462/C-526 as a first-party publisher access-state manifestation, deduplicated to SRC-388. The comparator text remains unresolved and no new content comparison is inferred.

## 2026-08-07 — SRC-463/C-527: Audible UK memoir manifestation

Discovery: a current search for a distinct audiobook manifestation surfaced Audible UK’s catalogue page for *Great and Unfortunate Things*.

Capture: the public HTML identifies Jason Arday and Eve Claxton as authors and Jason Arday as narrator. It preserves a publisher synopsis stating that he spoke his first word at eleven and learned to read at eighteen, plus several attributed endorsements. No audio file or public sample was exposed.

Decision: add SRC-463/C-527 as a UK distribution/source-version record linked to the canonical audiobook record SRC-189. Treat the childhood/literacy language as publisher memoir copy and the endorsements as reception evidence; do not count the page as a new work or independent corroboration.

## 2026-08-07 — SRC-464/C-528: Croydon election name match

Discovery: an official-record search surfaced the Croydon 2018 borough-election declaration and the London-wide consolidated results dataset.

Capture: both official manifestations name Jason Arday as a Labour candidate in Purley & Woodcote on 3 May 2018 and record 953 votes. The Croydon declaration is a scanned 31-page PDF; the London dataset is machine-readable and the relevant result appears on PDF page 90. No nomination address or other personal detail is reproduced in the archive.

Decision: preserve SRC-464/C-528 as an identity-disambiguation edge. The name match is not promoted into the subject’s verified biography because the result contains no birth date, photograph, or other identifier linking the candidate to the sociologist. Reopen only for a contemporaneous candidate profile, party record, or identity-bearing civic source.

## 2026-08-07 — C-529: CV corroboration of Croydon candidacy

Discovery: a focused search for identity-bearing corroboration found the indexed text of the January 2020 Nelson Mandela University-hosted CV. Under “Awards and Recognition,” it states that Arday was selected as a Labour candidate for the Purley and Woodcote position in the 2018 local elections.

Capture: the original CV URL currently returns a “Page not found” response, already preserved under SRC-086. The exact indexed extract and its provenance boundary were preserved in a local README; no unofficial PDF or personal address was downloaded or reproduced.

Decision: add C-529 as dated self/hosted CV corroboration. Update the SRC-464 identity edge from unresolved name-only match to source-level same-person corroboration, while retaining independent party/electoral verification as open.

## 2026-08-07 — C-170/C-530: Operation Black Vote scheme corroboration

Discovery: a focused search for the unresolved 2017 parliamentary-scheme lead found Arday’s 2020 Taylor & Francis article pages, whose author biographies identify him as a graduate of the Operation Black Vote MP Parliamentary Scheme. The same wording appears across multiple 2020 publications under his name; the earlier Academic Libraries North biography also records the scheme.

Capture: the canonical SRC-047 article record now preserves the author-biography observation and DOI URL. The revised Cambridge Student interview remains the source for the Simon Woolley mentorship account, while the dated CV remains the source for the July 2017 selection wording. No OBV participant list, MP-office record, or parliamentary administrative record was located in this search slice.

Decision: add C-530 and upgrade C-170 from “scheme independently unresolved” to “scheme name corroborated by repeated publication-time biographies, but independent administrative verification unresolved.” Do not treat repeated publisher biography copy as independent proof of participation or mentorship; reopen only from a new primary record or changed endpoint.

## 2026-08-07 — SRC-465/C-531: Semantic Scholar changed retrieval state

Discovery: a focused retry of the unresolved primary-text route for Arday’s 2018 *Whiteness and Education* article returned a new Semantic Scholar API state. The DOI query changed from the earlier preserved HTTP 429 boundary to HTTP 200 and exposed the article’s Semantic Scholar ID plus a Durham Research Online `openAccessPdf` route labelled GREEN/CCBY.

Capture: the 541-byte JSON response, headers, and SHA-256 were preserved locally. Direct requests to the Durham landing page and output route still returned HTTP 403 challenge HTML; no article PDF or accepted manuscript was recovered.

Decision: add SRC-465/C-531 as a changed scholarly-index manifestation related to SRC-450/SRC-449. This strengthens the lawful retrieval lead but does not constitute full-text recovery or resolve the Cofnas/Rollock comparison. Reopen only after a changed endpoint or concrete manuscript file appears.

## 2026-08-07 — SRC-466/C-532–C-533: East Coast Radio interview

Discovery: a focused search for a South African interview manifestation found East Coast Radio’s 31 March 2024 page, which says Zain Johnson interviewed Arday ahead of World Autism Day.

Capture: the page HTML and headers were preserved, along with the 799×799 host portrait. The browser-readable page attributes statements to Arday about autism/global developmental delay, speech and literacy therapy, learning to read at eighteen, his mother’s anti-apartheid activism, and the 1995 Rugby World Cup. The page invites listeners to scroll up for audio, but no downloadable audio URL or separate file identifier appeared in the static capture.

Decision: add SRC-466 and C-532–C-533 as a dated media/interview source. Add the interview to the media index, timeline, and biography with first-person and access-boundary labels. Do not treat the text as a medical, school, family, or activism record, and do not duplicate the recurring childhood claims as independent corroboration.

## 2026-08-07 — SRC-467/C-534–C-535: contemporaneous sponsor announcement

Discovery: a focused fundraising search found a 14 July 2010 Compress Yourself/Mynewsdesk press release published before the 30in35 challenge began.

Capture: the local HTML preserves the sponsor’s announcement of a 19 July start, 30 marathons in 35 days, Shelter and Shooting Star Children’s Hospice beneficiaries, London and Piccadilly–Teddington route structure, £5,000 target, 30in35 blog, and a reported £100,000 prior-fundraising total.

Decision: add SRC-467 and C-534–C-535 as a contemporaneous sponsor source-version. This strengthens the intended-challenge record independently of the campaign blog and JustGiving page, but does not prove completion, target attainment, or audited accounting. Keep the reported £100,000 separate from later aggregate totals.

## 2026-08-07 — C-536: endurance-distance contradiction

Discovery: a focused search for the unresolved 600-mile claim found the indexed News24 profile and the already-preserved BBC/Lives Retold transcript. Both give a 500-mile Edinburgh-to-London run in six days after the 300-mile treadmill challenge. The Crick biography gives 600 miles in six days, while the current ARU citation gives 600 miles across 12 days.

Capture: the News24 source note and BBC/Lives Retold source note now preserve the 500-mile wording and its evidence class. No race log, timing record, charity receipt, route archive, or explicit institutional correction was located.

Decision: add C-536 and update the biography/timeline/NEXT contradiction boundary. Do not treat the 500/600/6/12 variants as a typographical correction, rounding, separate challenge, or completed feat without stronger primary evidence.

## 2026-08-07 — SRC-468/C-537: `plag1` limitations and recommendations audit

Discovery: the preserved Arasite `plag1.zip` contains distinct rows not covered by the prior screenshot and `plag4` page audits. The rows map Arday thesis pp. 343–350 to Zwozdiak-Myers source-labelled pp. 265 and 269–271.

Capture/comparison: rendered Arday PDF pp. 343, 344, 346, 347, and 350 and Zwozdiak-Myers PDF pp. 276, 279–282. The passages show close textual/structural correspondence in the limitations and interpretation discussion, the reflection/self-study and professional-development passage, and the ordered recommendations to replicate across cohorts/subjects and use a larger sample. Arday’s substitutions, additions, changed framing, and citation/context differences remain explicit.

Decision: add SRC-468 and C-537 as a bounded direct primary-text audit. The supplied `plag1` labels remain attributed dossier characterizations; no intent, authorship history, quotation compliance, plagiarism, or institutional finding is inferred. Preserve the source-labelled pagination separately from visible printed and PDF pagination.

## 2026-08-07 — SRC-469/C-538: Youth Unemployment Committee report manifestation

Discovery: a current public-source sweep surfaced an Edge Foundation PDF mirror of the House of Lords Youth Unemployment Committee report, *Skills for every young person*. The earlier SRC-281 record had preserved the official hearing web text and Parliament access-boundary responses but no local report binary.

Capture: downloaded the 212-page PDF, response headers, extracted text, and rendered PDF pages 124 and 159. Page 124 (report printed p. 122) identifies Arday of Durham University and the Runnymede Trust and summarizes Q198’s mentoring/guidance/coaching recommendation. Page 159 (report printed p. 157) lists him as a Runnymede trustee and witness for QQ 195–207.

Decision: add SRC-469/C-538 as a distinct public manifestation deduplicated to SRC-281. Treat the report summary as committee paraphrase rather than a new verbatim quotation; preserve the 2021 role wording as historical and reconcile it with the later Companies House/Charity Commission termination record.

## 2026-08-07 — SRC-470/C-539: Channel 4 racial-justice interview binary

Discovery: a host-diverse media sweep found Channel 4 News’ 10 April 2023 video page, “Britain ‘not close’ to being ‘racially just society’ says damning report.” The page explicitly names Jason Arday as an interviewee and is distinct from the already-catalogued Channel 4 *Ways to Change the World* podcast.

Capture: preserved the first-party HTML and headers, Brightcove player configuration/API metadata, player JavaScript, public poster, and the clear 1280×720 H.264/AAC MP4. The file is 3:42.40 and has no caption/subtitle track in the public API beyond a thumbnail WebVTT track.

Decision: add SRC-470/C-539, media-index entry, timeline row, and a bounded NEXT item. The page establishes participation and subject framing; no detailed spoken claim is upgraded until the local MP4 is manually listened to and timecoded.

## 2026-08-07 — C-540: Cambridge appointment announcement as integrity-context source

Discovery: while rechecking the surviving Cambridge appointment announcement, the local HTML was searched for its account of Arday’s early academic formation.

Capture: the announcement says he had little practical training or guidance, worked as a PE lecturer while drafting papers and watching lectures, tried to master his discipline by reciting content verbatim, and had no mentor who showed him how to write.

Decision: add C-540 as attributed first-person context under the existing SRC-114 record. It is relevant to the later supervision and textual-overlap evidence, but it is not a causal explanation, defence, or institutional finding. Keep the quote-origin and page state distinct from the primary thesis comparisons.

## 2026-08-08 — SRC-471/C-541: PESA Agora full-text manifestation

Discovery: a focused search for the unresolved full-text route for the canonical *Fighting the tide* article surfaced a public PESA Agora PDF carrying DOI `10.1080/00131857.2020.1777640`.

Capture: downloaded the nine-page PDF, response headers, and an extracted-text derivative. The file contains the article header, online-first date, author metadata, substantive text, and references. Its local PDF hash is `768a3f95291ebe2404915431c00c0c9daebfd0729f5d61d6f095416a9353de7b`.

Decision: add SRC-471/C-541 as a full-text manifestation deduplicated to SRC-044. The PESA host is not treated as the publisher version of record. This closes the current lawful retrieval boundary for this article and creates a reproducible basis for any later page-specific audit; it does not itself create an integrity allegation or finding.

## 2026-08-08 — SRC-472/C-542–C-543: BAME/BME footnote audit

Discovery: the Arasite note for *Fighting the tide* explicitly pointed to a definition of BAME that it said followed the format used elsewhere in Arday’s work. The newly preserved full text made that lead testable.

Capture/comparison: rendered *Fighting the tide* PDF p. 7 and *No one can see me cry* accepted-manuscript PDF p. 2. The footnotes share a distinctive ordered template and near-identical explanatory structure, including the same ethnic-community list and closing statement about participant preference. The acronym, capitalization, citation formatting, and some wording differ.

Decision: add SRC-472/C-542–C-543 as a bounded primary-text relationship. It is not treated as a plagiarism, fabrication, or misconduct finding; provenance, reuse history, permission, and editorial explanation remain unresolved. The audit covers only these two footnotes.

## 2026-08-08 — SRC-473/C-544–C-545: three-publication BME/BAME footnote lineage

Discovery: the 2018 *Understanding Mental Health* PDF was checked as the earlier article named in the correction record and the existing overlap lead.

Capture/comparison: rendered 2018 PDF p. 2 and compared it with the already preserved *No one can see me cry* accepted-manuscript p. 2 and *Fighting the tide* p. 7. The 2018 and 2021 BME footnotes are nearly identical; *Fighting the tide* preserves the same template with BAME substitution and small edits.

Decision: add SRC-473/C-544–C-545 as a three-publication lineage extension. It records repeated text/common-template evidence only. It does not establish plagiarism, fabrication, intent, editorial responsibility, or a research-integrity finding.

## 2026-08-08 — SRC-474/C-546–C-547: Attempting-to-break-the-chain methodology manifestation and audit

Discovery: a focused retrieval search for the article named in the 2024 Taylor & Francis correction found the University of Kent Academic Repository item and its linked public PDF, described by the repository as the publisher PDF.

Capture: preserved the repository record, headers, 18-page PDF, extracted text, and rendered methodology pages. The shell encountered a self-signed certificate and required explicit TLS-verification bypass; the browser-backed direct-document fetch returned 502. These access conditions are retained in the source note.

Comparison: the article’s PDF p. 9 repeats the distinctive “anonymous self-administered questionnaire” / “deposited into a ballot box” sentence found in Arday’s 2018 article PDF p. 10. Samples, subjects, and surrounding study descriptions differ. The 2024 correction independently says the later methodology was amended to clarify its relationship to the 2018 study and Memon et al.

Decision: add SRC-474/C-546–C-547 as a correction-linked, sentence-level primary-text record. Do not collapse it into the earlier broad methods-lineage audit or convert it into a misconduct finding.

## 2026-08-08 — SRC-475/C-548–C-550: UCU BME doctoral-student report manifestation

Discovery: the UCU publisher page identifies Arday’s 8 June 2017 report; its browser-visible PDF route exposed an 11-page document. A public Pih mirror exposed a distinct 13-page Word-derived PDF.

Capture: preserved the mirror PDF, extracted text, four page renders, mirror headers, and UCU landing/PDF access-boundary HTML and headers. Shell requests to the UCU routes returned boundary HTML rather than the page/report body.

Decision: register the UCU page as the canonical publisher record and the Pih PDF as a distinct public manifestation. Add only bounded claims for the report’s stated sample/methodology and themes; do not treat the qualitative findings as population estimates or infer byte identity between the 11-page and 13-page states.

## 2026-08-08 — SRC-476/C-551–C-553: full Cofnas Substack manifestation

Discovery: the existing SRC-379 record preserved an earlier Cofnas article capture and selected comparison exhibits, but not the complete current HTML/image set. The public Substack page remains live and is dated 21 July 2026.

Capture: downloaded the full HTML, headers, embedded-image URL manifest, and 48 linked PNG/JPEG article binaries. The binaries include comparison exhibits and article illustrations; their article-media provenance is retained, and they are not treated as independent primary documents.

Decision: add SRC-476 as a fuller source-version linked to SRC-379. Record the article’s Copyleaks/comparator/correspondence assertions as attributed leads only. Continue underlying-text audits separately and preserve the methodological distinction between a polemical claim, a reproducible primary-text comparison, and an institutional finding.

## 2026-08-08 — SRC-477/C-554: Cambridge statement on Cofnas’s prior investigation

Discovery: Cambridge’s official notices include a separate 2 October 2025 statement about a disciplinary investigation into Cofnas’s own published views. This is a distinct institutional source from Cambridge’s August 2026 Arday statements and the 2026 research-misconduct procedure.

Capture: preserved the page HTML, response headers, and the page’s 885×432 Senate House hero image. The browser-backed page was 403 in the web reader, while direct shell retrieval returned the public HTML.

Decision: register it as source-provenance context only. It records Cambridge’s stated outcome for Cofnas’s prior free-speech inquiry, but does not validate or invalidate the Arday allegations and does not expose the underlying inquiry report.

## 2026-08-08 — SRC-478/C-555–C-557: SAGE manifestation of the 2023 neurodiversity article

Discovery: the unresolved 2023 Lewis–Arday article DOI returned a browser-readable SAGE PDF manifestation with 23 pages and page-level text. Direct shell retrieval of the SAGE PDF returned challenge HTML; OpenAlex exposed the same SAGE PDF URL and a content route that returned an error; Jina also returned a CAPTCHA boundary.

Capture: preserved the OpenAlex JSON record, SAGE PDF boundary and headers, OpenAlex error response and headers, and Jina boundary text/headers. No local article PDF is claimed.

Decision: add SRC-478 as a publisher/index manifestation deduplicated to SRC-053. Extract only bounded publication facts and the separately named BBC *Outlook* retrieval lead; retain the article’s autoethnographic diagnosis/family material as self-authored text rather than independent biography.

## 2026-08-08 — SRC-479/C-558–C-560: BBC *Outlook* episode

Discovery: the BBC Sounds identifier `w3ct4r2y` was cited in the references of the 2023 Lewis–Arday article. Direct BBC programme and Sounds pages resolved, despite the browser search boundary, and the BBC Sounds experience endpoint returned structured episode data.

Capture: preserved the BBC Sounds page, BBC programmes page, player-page manifestation, response headers, Sounds experience JSON, and the BBC episode image. The structured record gives the 29 March 2023 date, 2,430-second runtime, title, synopsis, presenter, producer, and image credit. The API’s low/medium/high downloads are DRM objects with null file URLs; no audio file or transcript was recovered.

Decision: register this as a distinct first-party broadcast manifestation, not as independent corroboration of the biography. Upgrade the prior retrieval lead to a source record, preserve the synopsis as attributed BBC metadata, and keep the local binary claim limited to the episode image.

## 2026-08-08 — SRC-480/C-561–C-565: *Revista História Hoje* interview

Discovery: a DOI search surfaced Amilcar Araujo Pereira’s interview with Jason Arday in *Revista História Hoje*, published 11 December 2024. The article page identifies the interview date as 28 November 2023, provides a public PDF, and marks the work CC BY 4.0.

Capture: preserved the article page and headers, 17-page PDF, extracted text, PDF headers, and rendered pages covering the substantive interview. The publication is in Portuguese and explicitly says that Pereira translated and edited the interview; it is not treated as a verbatim English transcript.

Decision: add SRC-480 as a distinct journal-interview source. Extract the additional first-person material on Ghanaian/South African parentage, poverty, one-sided deafness, childhood shelter visits, the age-18 shelter encounter, charity goals, Sandro’s advice, and intellectual influences, while retaining the source’s autobiographical and translation limits. Do not count the introductory biography’s repeated diagnosis/literacy/Cambridge claims as independent corroboration.

## 2026-08-08 — SRC-481/C-566: Tapesearch transcript-index manifestation

Discovery: the Tapesearch page for the already-captured *How Do You Cope?* episode publicly exposed the episode metadata and a timecoded opening transcript before a login wall.

Capture: preserved the direct shell response and headers as a Cloudflare access boundary. The browser-visible page supplied the opening transcript through approximately 1:57; the full transcript was not copied or claimed because the remainder is login-gated.

Decision: register SRC-481 as a transcript-index source-version deduplicated to SRC-129. Use only the host’s opening narration as attributed, timecoded metadata; do not convert it into Arday’s testimony or count the repeated biographical details as independent corroboration.

## 2026-08-08 — SRC-482/C-567–C-570: Christie `plag2` comparison rows

Discovery: the preserved `Aderibigbe-Christie-Le Cornu.docx` in the Arasite `plag2.zip` maps Arday thesis pp. 108–109 to Hazel Christie’s 2014 peer-mentoring article. A public Edinburgh repository PDF was available at the article-level source URL.

Capture: preserved the Christie PDF, extracted text, response headers, and rendered pages for the mapped article pages, alongside newly rendered Arday thesis pages 108–109. Direct inspection confirmed a long ordered social-learning passage on Arday p. 108 and a repeated agency-versus-passivity formulation on p. 109.

Decision: register SRC-482 as a distinct bounded primary-text comparison. Record the close wording, order, and reference correspondence while retaining Arday’s edits and citation changes. Do not adopt the dossier’s “verbatim” labels as findings, and do not infer intent, intermediate-source history, quotation compliance, supervision responsibility, or institutional misconduct.

## 2026-08-08 — SRC-483/C-571–C-574: Peters–Le Cornu–Collins `plag2` row

Discovery: the next `plag2` table row maps Arday thesis p. 93 to page 3 of Peters, Le Cornu, and Collins’s November 2003 *Towards Constructivist Teaching and Learning* report. The South Australian government PDF is still indexed and text-readable through the web research surface, but direct shell retrieval returned HTTP 403 with a Cloudflare managed challenge.

Capture: preserved both direct 403 HTML states and response headers, plus a rendered Arday thesis p. 93. No report PDF or local full-text extraction is claimed. The indexed text exposes the constructivism passage and the Bruner-attributed “participatory, proactive, communal, collaborative” sequence.

Decision: register SRC-483 as a bounded comparison and access-boundary record. Record the shared conceptual order and phrase sequence, the “given over to”/“submissive to” variation, and the explicit common Bruner attribution. Keep open whether the route was Bruner, the 2003 report, an intermediary, or a combination; do not infer intent or institutional misconduct.

## 2026-08-08 — SRC-484/C-575–C-578: Douglass `plag3` Vygotsky/MKO row

Discovery: the `plag3` comparison table maps Arday thesis pp. 310–311 to the Douglass, Smith, and Smith peer-mentoring article. The locally preserved HKU conference PDF is a public source-version associated with the DOI record and exposes the mapped Vygotsky/MKO passage.

Capture: rendered Arday pp. 310–311 and Douglass conference PDF p. 2 locally. Direct comparison found the same MKO definition sequence and a close continuation about social interaction, comfort, and seeking help from a more knowledgeable peer.

Decision: register SRC-484 as a distinct source-version comparison. Preserve the strong page-level correspondence and Arday’s additions, but do not treat the conference PDF as the version of record. Keep the separate p. 311 complementarity row open because it is not present in the captured precursor; do not infer intent, quotation compliance, or institutional misconduct.

## 2026-08-08 — `plag3` complementarity-row search boundary

Search: exact-phrase and title/DOI searches were run for the remaining p. 311 complementarity passage, including the “concept of complementarity,” Godshalk/Sosik, and Douglass article title/DOI variants. Results repeated the HKU conference precursor, indexed metadata/abstract pages, and unrelated uses of “complementarity.”

Decision: no new lawful published-article full text or distinct comparator binary was found. Keep the complementarity row open and separate from SRC-484; reopen only after a changed publisher/ResearchGate endpoint, a lawful author/repository copy, or a concrete archived file appears.

## 2026-08-08 — SRC-485/C-579–C-582: `plag1` continuation row

Discovery: the remaining `plag1` table contains a distinct row mapping Arday pp. 350–351 to Zwozdiak-Myers printed pp. 270–271. The primary thesis PDFs were already locally preserved; the comparator’s PDF pages are 281–282.

Capture: rendered the newly uncovered Arday p. 351 and reused the existing primary page renders for Arday p. 350 and Zwozdiak-Myers pp. 270–271. Direct inspection found close correspondence in the pedagogical-moments/discursive-history passage, future-research sentence, and university–school cooperation sequence.

Decision: register SRC-485 as a distinct continuation audit. Preserve wording changes, printed/PDF pagination, and adjacency controls; do not re-count SRC-468’s p. 350 recommendations row or infer intent, quotation compliance, authorship history, or institutional misconduct.

## 2026-08-08 — SRC-486/C-583–C-584: `plag1` final-remarks row

Discovery: the next distinct `plag1` table row maps Arday printed p. 352 to Zwozdiak-Myers printed p. 272. The primary thesis PDFs were already locally preserved; the relevant PDF pages are Arday p. 352 and Zwozdiak-Myers p. 283.

Capture: rendered both primary pages locally. Direct inspection found a close ordered sequence covering the conclusion/research-question framing, generalisability caution, complex/multi-dimensional reflective-practice description, study purpose, and literature-gap transition. Arday adds peer-mentoring, constructivist-thinking, and thesis-specific framing.

Decision: register SRC-486 as a distinct page-bounded audit. The adjacent 352–353 row is separately canonicalized as SRC-487; preserve printed/PDF pagination and the dossier’s source-attributed label separately from the evidence assessment, and do not infer intent, quotation compliance, authorship history, or institutional outcome.

## 2026-08-08 — SRC-487/C-585–C-586: `plag1` final-remarks continuation

Discovery: the next distinct `plag1` table row maps Arday printed pp. 352–353 to Zwozdiak-Myers printed pp. 272–273. Arday p. 352 is reused from SRC-486; the new page witnesses are Arday PDF p. 353 and Zwozdiak-Myers PDF p. 284.

Capture: rendered the new primary pages locally and directly compared the row. The texts preserve the ordered classroom-enquiry/literature-gap, learning-process, reflective-practice, and contribution-to-literature sequence, with Arday substitutions for mentoring, collaborative learning, professional practice, and pedagogical practice.

Decision: register SRC-487 as a distinct continuation audit. The extracted table contains no additional later p. 353 row beyond the participant-outcomes row separately canonicalized as SRC-488; preserve printed/PDF pagination and the dossier’s source-attributed label separately from the evidence assessment, and do not infer intent, quotation compliance, authorship history, or institutional outcome.

## 2026-08-08 — SRC-488/C-587–C-588: `plag1` participant-outcomes list

Discovery: the next distinct `plag1` table row maps Arday printed p. 353 to Zwozdiak-Myers printed p. 273. Both relevant primary page renders were already preserved during SRC-487.

Capture: directly compared the numbered outcomes list. The passages share the ordered personal-improvement, systematic-evaluation, alternative-perspectives, critical-reflection, and continued-improvement items. Arday frames the list through enjoyment in peer-mentoring for reflective practice and numbers five items; Zwozdiak-Myers presents six items and includes classroom-research and pupil-learning language.

Decision: register SRC-488 as a distinct localized list-row audit, not a new publication or duplicate media source. Preserve the source-attributed dossier label separately from the evidence assessment and do not infer intent, quotation compliance, authorship history, or institutional outcome.

## 2026-08-08 — `plag1` row-inventory closure

Inventory: a fresh extraction of `More Z-M - summaries(1).docx` counted 13 mapped rows: two at Arday p. 343, three at p. 344, one at pp. 346–347, one at p. 350, two at pp. 350–351, one at p. 351, one at p. 352, one at pp. 352–353, and one at p. 353.

Coverage: SRC-468 covers the earlier pp. 343–350 rows; SRC-485 covers the three pp. 350–351/p. 351 continuation rows; SRC-486 covers p. 352; SRC-487 covers the pp. 352–353 continuation; and SRC-488 covers the p. 353 participant-outcomes list. The 13-row inventory is therefore closed as a page-level audit of the current dossier.

Boundary: this closes only the current table inventory. It does not resolve source provenance, intent, quotation or citation compliance, authorship history, supervision responsibility, or any institutional/adjudicative outcome. Reopen only after a changed dossier, new primary comparator, or institutional record appears.

## 2026-08-08 — `plag4` final-grid row-inventory closure

Inventory: a fresh extraction of `ARDAY FINAL GRID.docx` counted 122 mapped rows. Their Arday page labels span pp. 35–36, 46–47, 53, 57–69, 75–78, and 79–81, with multiple rows within several page blocks.

Coverage: the rows fall within the audited blocks SRC-405–SRC-412, SRC-416–SRC-419, SRC-421, SRC-428, and SRC-444. The block audits preserve the relevant primary thesis PDFs, page witnesses, printed/PDF pagination, and dossier boundaries. No new source node is created by this closure.

Boundary: this closes only the current `plag4` table inventory as a page-level audit. It does not determine whether an intermediate source was used, whether citation or quotation conventions were satisfied, whether the text breached a policy, or whether any institution made a finding. Reopen only after a changed dossier, new primary comparator, or institutional/adjudicative record appears.

## 2026-08-08 — SRC-489/C-589–C-590: Unpaywall boundary for the `plag3` comparator

Discovery: an independent Unpaywall DOI API check was run for Douglass, Smith & Smith’s 2013 article, DOI `10.1080/13611267.2013.813740`, using a route distinct from the previously checked publisher, ResearchGate, OpenAlex, and Semantic Scholar paths.

Capture: the JSON response identifies the article and reports `is_oa: false`, `oa_status: closed`, `has_repository_copy: false`, and no OA or embargoed locations. The raw JSON and response headers are locally preserved under SRC-489.

Decision: register SRC-489 as an independent comparator access-state record deduplicated to the version-of-record node. It strengthens the missing-primary-text boundary but does not audit Arday’s p. 311 complementarity row and does not treat closed access as evidence of plagiarism, intent, or institutional misconduct.

## 2026-08-08 — SRC-490/C-591–C-593: Cambridge Repository article manifestation

Discovery: Cambridge Repository’s item page `245ca7d9-14e2-475d-8608-7f22b52409ee` surfaced a published-version manifestation of Belluigi, Arday, and O’Keeffe’s canonical 2024 *British Educational Research Journal* article, DOI `10.1002/berj.4047`.

Capture: preserved the repository HTML and headers, downloaded the 28-page published PDF, preserved PDF headers, and extracted text. The PDF reports receipt 4 March 2024, acceptance 25 June 2024, Arday as second author with Cambridge Faculty of Education affiliation, and the article’s HESA/QuantCrit method and reported findings.

Decision: register SRC-490 as a distinct repository/version manifestation deduplicated to SRC-173. Preserve the existing QUB PDF separately because it has a different hash and page count; do not create a second publication or infer sole authorship of the study’s methods or findings.

## 2026-08-07 — SRC-268 reproducibility clip

The locally preserved *Neurodivergent Show* MP4 was used to create a 28-second derivative covering the first open caption window (approximately 02:33–03:01, the diagnosis-at-three passage). The clip’s SHA-256 is `7b6c44ff05dbeab2a41f053211f7423e99401c4d55637bb30e174349b0bc6d80`.

The two longer windows (05:20–05:57 and 06:08–07:12) remain available in the full MP4/VTT but their derivative extraction was killed by the local resource limit. No claim was upgraded from machine-captioned to human-verified; listening verification remains open.

## 2026-08-08 — SRC-500–SRC-501/C-610–C-612: Hussain comparator and Ferraro source lineage

Discovery: Cofnas’s preserved comparison image labels the right-hand comparator “Athar Hussain et al. (2011)” and places it against Arday’s thesis p. 348. A direct ERIC PDF retrieval identified the article as Hussain, Mehmood, and Sultana, *An Inquiry into Benefits of Reflective Practice in Open and Distance Learning*, *Turkish Online Journal of Distance Education* 12(2), printed p. 53.

Capture: preserved the Hussain PDF, headers, extracted text, and printed-p. 53 render. Direct comparison confirms the Ojanen teacher-educator passage and Kettle/Sellars peer-reflective-groups passage shown in the exhibit, while Arday p. 348 retains the same ordered sequence with close wording and substitutions. The Arday page render was produced from the locally preserved thesis PDF.

Provenance check: the same passage appears in Joan M. Ferraro’s 2000 seven-page ERIC digest, *Reflective Practice and Professional Development*, printed p. 2, with attribution to Ojanen (1993) and Kettle and Sellars (1996). Hussain’s captured article cites Ojanen and Kettle/Sellars in the passage but does not visibly cite Ferraro in its captured references. This is a source-lineage and citation-surface observation, not a standalone misconduct finding.

Decision: register SRC-500 as the immediate comparator manifestation and SRC-501 as the earlier public antecedent. Keep the image’s yellow/green evaluative labels attributed to Cofnas; do not infer intent, quotation compliance, authorship history, or institutional outcome. The next integrity lead should be a distinct primary-text or institutional audit, not a repeat of this same passage.

## 2026-08-08 — SRC-393/C-613: JSTOR recheck for Edwards/Nicoll

Discovery: Kahn et al. (2008) cites Edwards and Nicoll’s 2006 *British Educational Research Journal* article as the underlying source for the reflective-practice rhetoric discussion in Cofnas’s Kahn comparison. The existing record had Stirling-embargo and ERIC error boundaries but no JSTOR route.

Capture: requested JSTOR stable item `30032661` and `stable/pdf/30032661.pdf`. Both returned HTTP 403 and the same 5,815-byte JSTOR “Access Check” HTML; no article text, preview, or PDF binary was recovered. HTML, headers, and hashes are preserved under `assets/documents/research-integrity/edwards-nicoll-2006-jstor/`.

Decision: update SRC-393 in place and add C-613 as a changed-route access boundary. The underlying primary-text comparison remains open; Kahn’s review and quotation remain separate evidence and are not upgraded into a substitute for Edwards/Nicoll’s version of record.

## 2026-08-07 — public-output sweep: indexed leads deduplicated

Search boundary: ran fresh exact-name searches for Jason Arday across 2026 university events, 2025 interviews/podcasts, public recordings, and recent commentary. The result set surfaced Cambridge’s April Anti-Racism Symposium, UAL’s March *Opening Out* dialogue, the BSA 2026 plenary, the cancelled RGS conversation, the Crick 2024 event, the existing Cambridge neurodiversity film and *How Do You Cope?* episodes, the White Rose 2026 book review, Retraction Watch, and Dennis McCarthy’s Substack.

Deduplication: every substantive result was already represented by SRC-193, SRC-305, SRC-187, SRC-339, SRC-113, SRC-239/SRC-220, SRC-287, SRC-282, or SRC-460. No new recording, transcript, image, document, or materially changed source state was exposed by this search family. Search-result snippets were not promoted to evidence and no claims were upgraded.

Decision: close this exact query family for now. Reopen only after a changed endpoint, a direct event artifact, a new publication identifier, or a distinct interview/recording appears; continue from the first unchecked source family in `NEXT.md` rather than repeating these broad searches.

## 2026-08-07 — SRC-536/C-681–C-682: LSTM report manifestation

Discovery: an institutional-output sweep surfaced LSTM’s public February 2022 PDF, *Equity & Inclusion at LSTM: Improving racial equity in global medicine*. The earlier LSTM announcement under SRC-097 established the consultancy announcement but did not preserve the report binary.

Capture: downloaded the 21-page PDF, preserved response headers and layout-preserving extracted text, and rendered representative pages for visual QA. The title page names Professor Jason Arday as author; PDF p. 4 says LSTM commissioned him as an independent consultant; PDF p. 12 reports the staff/student consultation counts; PDF pp. 12–20 presents themes and recommendations; PDF p. 21 describes the LSTM-specific implementation framework and 14–16-month consultant follow-up.

Decision: register SRC-536 as a distinct professional-output manifestation, not a duplicate of the LSTM announcement. Add C-681 for the commissioned authorship/role and C-682 for the report’s stated methodology/findings. Preserve its author biography as dated host/report copy and do not infer independent participant verification, implementation success, or later institutional outcomes.

## 2026-08-08 — SRC-537–SRC-540/C-683–C-686: LSTM response sequence

Discovery: followed SRC-536’s explicit implementation lead. LSTM’s own records surfaced a 14 February 2022 response, an October 2022 Race Equity Action Plan, and a March 2026 Bronze Race Equality Charter announcement. The LSTM EDI route also produced a changed redirect state rather than its indexed substantive body.

Capture: preserved the 2022 response HTML, headers, and article image; downloaded the 52-page action-plan PDF with extracted text, headers, and representative rendered pages; preserved the 2026 award page, headers, and article image; and captured the EDI-route redirects/final HTML. The response records full acceptance of the review’s findings, an implementation lead, a planned action plan, and six-month reporting. The plan covers 2022–2025, establishes REAG governance, names six themes, and identifies initial priorities with Arday. The 2026 announcement records the Bronze Award and a five-year action-plan framing.

Decision: register SRC-537, SRC-538, and SRC-539 as distinct institutional-response/action/outcome records, not duplicate manifestations of SRC-536. Register SRC-540 as a negative-space/access-state record; do not treat indexed EDI snippets as a current page capture. Add C-683–C-686 and keep implementation commitments, planned actions, accreditation outcome, and individual Arday involvement carefully separated.

## 2026-08-08 — SRC-541–SRC-544/C-687–C-691: LSTM progress and external-register follow-up

Discovery: followed the response sequence into LSTM’s later annual reporting and Advance HE’s own register. The 2023–24 ED&I report documents progress under the Race Equity Action Plan and a planned November 2025 Bronze submission. The 2024–25 annual report documents a new ED&I Strategy and preparation of the submission. Advance HE’s current signatory table lists LSTM at Bronze level. LSTM’s current EDI page provides a live overview of the governance/reporting structure.

Capture: downloaded the 13-page 2023–24 ED&I report and 21-page 2024–25 annual report with extracted text, headers, and representative renders; preserved Advance HE’s register HTML/headers; and preserved the current LSTM EDI page/headers.

Decision: register SRC-541–SRC-544 as distinct progress, annual-report, external-register, and current-page records. Add C-687–C-691. The sequence supports an institutional implementation/accreditation timeline, but does not establish that Arday remained involved after the stated 18-month support period or that every recommendation was completed. The original indexed EDI route remains separately preserved as SRC-540 because it redirected during direct capture.

## 2026-08-08 — SRC-545/C-692: UK Black Stars recognition listing

Discovery: an exact-name public-output sweep surfaced the UK Black Stars 2026 homepage, which lists “Prof Jason Arday” among its “100 Influential British-Ghanaians” and displays a portrait with a “UK Black Star” badge. No individual profile page, selection criteria, nominating body, or substantive biography was exposed.

Capture: preserved the homepage HTML and response headers, plus the linked 524×556 JPEG and image headers. The page is retained as a recognition/listing source-version and image record, with no claims promoted beyond what the page directly displays.

Decision: register SRC-545 and C-692, add the portrait to `media.md`, and mark the lead resumable only for a changed page, individual profile, methodology/award explanation, or rights-cleared image source.

## 2026-08-08 — SRC-546/C-693: Runnymede current team-page boundary

Discovery: the role-reconciliation pass followed the Runnymede trusteeship trail to the organization’s current **Our Team** page. The page has separate Team and Trustees lists and a 14 May 2026 publication marker, but the captured HTML contains no exact “Jason Arday” occurrence.

Capture: preserved the current page and response headers. No image or separate trustee record was needed because the material observation is the page topology and exact-name absence.

Decision: register SRC-546/C-693 as a bounded current-page source-version. It supports current public-list absence only; it does not replace the Companies House TM01 or the Charity Commission 2024 accounts as the stronger evidence for the November 2024 trusteeship end.
# 2026-08-08 — SRC-517/C-656–C-659 Free Beacon fundraising/memoir investigation

Discovery: followed the direct Free Beacon lead from current discussion and recovered Benjamin Ryan’s 4 August 2026 article. The page exposes a 4,186-word article record, publication/modified metadata, and links to the two Wayback speaker-bio snapshots used in its central comparison.

Capture: preserved the article HTML, headers, lead WebP image, and both archived Simon & Schuster Speakers Bureau HTML pages. The 19 May 2025 snapshot states over £5.5m for 80 charities, lists the three endurance feats, and names WaterAid in the South America/West Africa water-point claim. The 24 July 2025 snapshot instead describes fundraising teams raising millions and omits the specific totals and feats. Added SRC-517 and C-656–C-659.

Evidence handling: the page-version difference is directly observable. The article’s claims about a university-job CV, an MBE offer, advertising complaints, publisher proof comparisons, and publisher editing are retained as reported leads because the cited CV, underlying correspondence, podcast capture, and book proofs were not recovered here. Do not turn this source into a final fraud finding or conflate changing biography copy with proof of intent.

# 2026-08-08 — SRC-072/C-702–C-703 Broken Pipeline report capture and extraction

The official Leading Routes PDF for *The Broken Pipeline* was recovered after the registry’s prior record showed no local file. The eight-page September 2019 report names Paulette Williams, Sukhi Bath, Jason Arday, and Chantelle Lewis. It documents a closed February 2019 stakeholder roundtable rather than a survey or peer-reviewed empirical study.

Page-level extraction records the cited HESA/UKRI context, the roundtable’s discussion points, barriers around attainment filters, institutional preferences, data gaps, scholarship criteria, guidance, academic excellence, and supervisory bias, plus recommendations and Leading Routes’ planned 2019–20 follow-up. The report’s statistics remain attributed to their cited sources; its planned activities are not treated as implementation evidence.

# 2026-08-08 — SRC-040/C-700–C-701 ThinkHigher report capture and extraction

The first-party ThinkHigher PDF for *The Black Experience Project* was not previously locally preserved. It was downloaded from the project’s public URL, verified as an 18-page PDF, hashed, and extracted with `pdftotext -layout`. The report identifies Arday as author, says ThinkHigher commissioned the work, and records 11 secondary students aged 15–18 interviewed remotely.

The methodology states that the data were qualitative narrative interviews, convenience-sampled, transcribed, and themed; it explicitly warns that findings may not be generalisable and notes that interviewers were White. The findings are organized into five themes—curriculum, racism, impacts, hair, and opportunities for change—with participant-attributed excerpts and recommendations. Recorded this as a commissioned qualitative report, not a population survey or independent causal study.

# 2026-08-08 — SRC-044/C-699 Fighting the tide full-text classification

The preserved PESA Agora PDF was extracted at page level and compared with the DOI record. The article is explicitly labelled “EDITORIAL,” uses cited HESA/Leading Routes/AdvanceHE figures and literature, and contains recommendations on recruitment, studentships, mentoring, communities of practice, and institutional accountability. No new participant sample, interview protocol, statistical analysis, or original results section appears in the recovered text.

The article’s UCU funding statement and 2020 contributor biography were recorded as dated publication metadata. They should not be used as current affiliation or legal-role evidence. The canonical publication record remains SRC-044; SRC-471 remains the public full-text manifestation.

# 2026-08-08 — SRC-029/C-697–C-698 Black Curriculum report extraction

The preserved first-party 13-page PDF was re-read at page level. It identifies the January 2021 report as authored by Jason Arday, describes a content-analysis corpus spanning reports, policy documents, blogs, newspaper articles, podcasts, videos/vlogs, and academic papers, and explicitly acknowledges limited specific data on Black-history teaching patterns and difficulty sourcing recent data for parts of the education system (p. 7).

The report’s executive summary and recommendations call for a more multicultural History National Curriculum, a broader conception of Britishness, a more diverse history-teaching workforce, and year-round, cross-disciplinary Black History teaching (pp. 4–5, 20–21). Recorded these as primary-output claims and recommendations. The report is not treated as an independently audited systematic review, a new school-level prevalence survey, or evidence of implementation.

# 2026-08-08 — SRC-516/C-654–C-655 National Review Ohio State affiliation report

Discovery: the Guardian podcast’s visiting-professor thread and the existing host-domain audit pointed to the unresolved Ohio State claim. A direct search recovered Abigail Anthony’s 4 August 2026 *National Review* report, which quotes Ohio State spokesperson Benjamin Johnson saying the university had no record of an employee named Jason Arday. The article also reports the announced 28 February 2025 closure of the Office of Diversity and Inclusion and says Arday did not respond to a request for comment.

Capture: preserved the article HTML, response headers, and featured image under `assets/captures/2026-08-08-national-review-arday-ohio/`. Added SRC-516 and C-654–C-655.

Decision: treat this as a materially stronger institutional-response report, but do not convert “no record of an employee” into “no affiliation of any kind.” The open question is whether any formal non-employee visiting, honorary, adjunct, unpaid, or short-term association existed and what Ohio State’s own records say. Preserve the 2019–2022 positive biography witnesses as dated source versions; do not deduplicate them away or treat repetition as independent confirmation.

# 2026-08-08 — SRC-515/C-652–C-653 WaterAid/relief-work search boundary

Follow-up from the Guardian *Today in Focus* listening notes: searched exact-name combinations for Jason Arday with WaterAid/Water Aid, charity, West Africa, South America, and water points, including a direct WaterAid-domain query. No WaterAid-hosted project page, press release, staff/profile record, fundraising page, annual report, or country-programme document surfaced.

Capture: preserved the public Simon & Schuster Speakers Bureau biography, which independently states that Arday undertook and completed relief work in South America and West Africa involving clean-water points. The page supplies no charity name, project, country, date, partner, or source. Added SRC-515 and C-652–C-653.

Decision: treat the Speakers Bureau page as promotional propagation evidence, not direct WaterAid corroboration. Keep the underlying relief-work claim unresolved; the next useful evidence would be a WaterAid record, contemporaneous charity/project documentation, or a named partner. Do not repeat the same exact-name search family without a changed index or new lead.

# 2026-08-07 — SRC-098/C-638–C-640 Guardian source-version recheck

The canonical Guardian interactive investigation was re-fetched on 7 August 2026. The live page displayed a 7 August modification timestamp and a materially useful source-version: it reports Arday’s statement that multiple investigations, including an academic-misconduct panel, concluded there was no plagiarism or misconduct; reports that LJMU reviewed the work and found no plagiarism; describes the Guardian’s checks with named butchers and the Metropolitan police that contradicted parts of the reported severed-pig-head/police-investigation account; and records Arday’s clarification that the 600-mile challenge took 12 days with rest days rather than six consecutive days.

Evidence handling: updated SRC-098 in place and added C-638–C-640. The record treats the panel outcome as an attributed report without the underlying report, the harassment material as a disputed personal account plus journalistic checks rather than a proven fabrication, and the endurance clarification as a source-version that does not reconcile all distance/duration variants. Local HTML and response headers are preserved under `assets/captures/2026-08-07-guardian-longform-scrutiny/`; no duplicate Guardian source was created.
# 2026-08-07 — SRC-513/C-641–C-643 Guardian Cambridge-process follow-up

Captured the Guardian’s 7 August report on Cambridge’s continuing investigation into the circumstances of Arday’s appointment and tenure. The report quotes Cambridge’s statement that findings will feed into a review of senior-academic appointments and that the Research Policy Committee will review the misconduct-in-research policy. It also reports an internal letter signed by nearly 100 Cambridge academics requesting an independent investigation, a clear timetable, and public findings, plus Jesus College’s statement that Arday’s contingent fellowship ended and its parallel process concluded with acceptance of his resignation.

Evidence handling: added SRC-513 and C-641–C-643. The university statement, academics’ request, and college statement are kept as separate institutional layers; none is treated as a misconduct, qualification, appointment, or tenure finding. Article HTML, headers, and the credited lead image are preserved under `assets/captures/2026-08-07-guardian-cambridge-academics/`.
# 2026-08-07 — SRC-514/C-644–C-645 Guardian *Today in Focus* audio capture

Captured the official Guardian episode page, RSS feed, direct audio enclosure, response headers, and lead image for “Plagiarism and a pig’s head: the rise and fall of Jason Arday.” The RSS item and page identify a 37:44 episode published 7 August 2026; the direct MP3 is 55,310,858 bytes and matches the RSS enclosure length. The page synopsis describes the Cambridge appointment, scrutiny of scholarship and life story, and treatment of Black scholars by academia and media.

Evidence handling: added SRC-514 and C-644–C-645. The actual MP3 is preserved as a local binary, but no detailed audio claims or timecodes are made because no transcript/captions were exposed and manual listening has not yet been completed. The next action is bounded manual transcription/listening, not another page or feed fetch.

Update: a local MLX Whisper small-model pass over the MP3 produced 500 English segments. Rather than publish a full machine transcript, added bounded paraphrased listening notes with approximate time ranges. The notes identify new source leads and media provenance for the “7 Up” account, WaterAid/visiting-professor/book claims, fundraising syndicate explanation, TES/Carter-Ruck history, and the Guardian reporter’s checks of alleged intimidation. Added C-646–C-651; all remain appropriately attributed and the original MP3 remains controlling for exact wording.

## 2026-08-08 — SRC-086 CV endpoint recheck

Rechecked the exact Nelson Mandela University URL for the January 2020 CV after a search-index result resurfaced the PDF text. The endpoint returned HTTP 404 with an HTML body, not a PDF; the 30,633-byte response and headers are preserved under `assets/documents/nelson-mandela-cv-2020-08-08/` and documented in `assets/metadata/nelson-mandela-cv-capture-2026-08-08.md`.

Decision: this is a changed access-state observation, not a new CV source or a recovery of the indexed document. The dated indexed extract remains bounded as self/host-published source-level evidence; no current appointment, qualification, or role claim is upgraded from it.

## 2026-08-08 — SRC-549 ASA year-in-review event listing

Discovery: an official American Sociological Association PDF surfaced in search results as a distinct professional-output record. The *Footnotes* Winter 2025 “2024 ASA Year in Review” lists “A Neurodivergent Inclusive Approach to Academic Policies and Practices” among its webinars and names Jason Arday and Chantelle Lewis as speakers.

Capture: preserved the 36-page PDF, response headers, layout-preserving text extraction, and a rendered page showing the listing (PDF p. 12 / printed p. 22).

Decision: added SRC-549 and C-708 as a dated first-party event-listing witness. The record does not establish the exact date, delivery, attendance, recording, transcript, or substantive content; no current-employment inference is made. Future work should seek the session artifact itself rather than repeat the annual-review search.

## 2026-08-08 — SRC-550/C-709 Aziz Foundation / London Met report capture

Discovery: an exact-name PDF search surfaced the official copy of *Institutionalised: The Rise of Islamophobia in Higher Education*, dated January 2021 and produced by London Metropolitan University’s Centre for Equity and Inclusion.

Capture: preserved the 60-page PDF, headers, layout-preserving text extraction, and a rendered copy of printed page 7. The page contains Arday’s foreword, “A New Dawn: Addressing Islamophobia in British Higher Education,” and labels him Visiting Professor at the Centre for Equity & Inclusion, Durham Associate Professor/Deputy Executive Dean, and Runnymede Trust trustee.

Decision: added SRC-550 and C-709. The report is catalogued as an institutional report with an Arday-authored foreword, not as an Arday-authored empirical study. Its role labels are preserved as January 2021 source-version evidence and are not treated as current status.

## 2026-08-08 — SRC-079 access-state recheck

Rechecked the exact indexed TransReads URL for the Bloomsbury chapter after the search index resurfaced a contents preview. The mirror returned HTTP 403 with a WordPress authorization page; the official Bloomsbury US route also returned a Cloudflare HTTP 403. Preserved both response bodies and headers under `assets/documents/transreads-decolonizing-university-teaching-2026-08-08/`.

Decision: updated SRC-079/C-136 in place. No new publication node or chapter-text claim was created; the indexed snippet remains a discovery witness only, and the official publisher metadata remains canonical.

## 2026-08-08 — SRC-229 Glasgow event source-version recheck

Discovery: a search for a new Glasgow Black History Month record surfaced the University’s separate Student News page, first published 9 October 2025, announcing the same 10 October keynote. The linked BookItBee page and event poster were byte-identical to the existing SRC-229 manifestations.

Capture: preserved the student-news HTML and response headers as a new source-version under the canonical event record.

Decision: updated SRC-229/C-188 and `media.md` in place. No duplicate event node or standalone portrait was created; delivery, attendance, recording, transcript, and slides remain unresolved.

## 2026-08-08 — SRC-551 *We Are Out of Office* propagation witness

Discovery: a podcast search surfaced Apple Podcasts episode 55 of *We Are Out of Office*, published 14 March 2026. Its show notes mention Professor Jason Arday and link to an Instagram post, while repeating the familiar delayed-speech/literacy and Cambridge biography.

Capture: preserved the Apple Podcasts HTML and response headers locally. The page exposes the episode’s metadata and the relevant show-note text.

Decision: added SRC-551/C-710 as a low-provenance source-propagation witness. The episode does not feature Arday as a guest, so no media-appearance node, audio binary, or independent biography claim was created.

## 2026-08-08 — SRC-552 linked Instagram source check

Discovery: the Apple episode’s show notes linked an Instagram post dated 14 August 2025 by “The Archbishop of Banterbury.” The post’s caption and displayed image repeat the diagnosis, delayed-speech/literacy, and Cambridge-superlative narrative.

Capture: preserved the public Instagram HTML, response headers, the 640×640 image derivative, and image headers. The page identifies an external account; it does not identify an Arday-authored source or an institutional relationship.

Decision: added SRC-552/C-711 as a separate propagation manifestation and linked it from SRC-551. No new biography fact, media appearance, or independent corroboration was created.

## 2026-08-08 — SRC-553 NEON Summit programme capture

Discovery: a search for distinct 2022 event records surfaced the University of Leeds/NEON Summit agenda, headed “Widening access and increasing success within Postgraduate Taught and Research study” and dated 13 July 2022.

Capture: preserved the two-page PDF, layout-preserving text extraction, response headers, and rendered pages. The agenda lists Arday for an 11:45 keynote and as a participant in the 14:35–15:20 panel on taking forward the NEON strategy blueprint.

Decision: added SRC-553/C-712, `media.md`, the public-output index, and the timeline. The record remains a planned-programme witness; no delivery, attendance, remarks, recording, transcript, or slides are inferred.

## 2026-08-08 — SRC-091/C-713 memoir publisher access-state recheck

Discovery: a current search result resurfaced the official Simon & Schuster US memoir page and exposed publisher metadata in the web-search surface.

Capture: the direct canonical URL was rechecked from the shell. It returned HTTP 403 Cloudflare challenge HTML; the 5,493-byte body and headers were byte-distinct from the 6 August challenge and were preserved under `assets/captures/2026-08-08-simon-schuster-memoir-recheck/`.

Decision: updated SRC-091/C-713 and `negative-space.md` in place. No new memoir edition, publisher record, excerpt, full text, audio file, or independent biography claim was created.

## 2026-08-08 — SRC-211/C-714 exact-title and host-volume search recheck

Discovery: exact-title and English/French host-volume searches were repeated across the public web and known institutional/scholarly witnesses. The Durham indexed person-page result remained the only Arday-specific manifestation. The GRIP profile and Steinmetz CV continued to support the existence/project history of the Dufoix/Mosbah-Natanson volume at volume level, but neither names Arday’s chapter or supplies chapter identifiers.

Evidence handling: updated SRC-211 in place and added C-714. No publisher page, DOI, ISBN, pagination, library record, repository copy, lawful full text, duplicate publication record, or chapter-content claim was created. The Springer/Information Age/La Découverte conflict remains explicitly unresolved.

Next boundary: reopen only after a concrete chapter-level identifier, changed Durham/publisher/catalogue state, or archival record; do not repeat the same exact-title pass.

## 2026-08-08 — SRC-186/C-715 *Allyship in Action* catalogue-topology recheck

Discovery: the episode surfaced again through Amazon Music and Apple’s public catalogue lookup. The canonical Libsyn enclosure was rechecked and matched the existing 24,206,688-byte MP3; Apple supplied track ID `1000731447975`, episode GUID `9abe4023-fd0e-468d-a32d-d35e9efcf675`, exact release timestamp, and 31:10 duration.

Capture: preserved the Apple lookup response and extracted episode row, Amazon client-rendered page shell and headers, Libsyn response headers, and a 600×600 artwork derivative.

Evidence handling: updated SRC-186 in place and added C-715 as a platform-manifestation mapping. No duplicate interview, independent biography claim, transcript, or timecoded audio claim was created.

Next boundary: reopen only for a public transcript/caption asset, materially changed enclosure, or distinct interview manifestation.

## 2026-08-08 — SRC-554/C-716–C-717 Forbes interview-account capture

Discovery: a distinct Forbes article by Julie Kratz was found under the title “Don’t Let The Zeitgeist Slow Down Your Talent Pipeline.”

Capture: preserved the HTTP 200 HTML page, response headers, and its 960×640 generic industrial-pipeline lead image. Page metadata identifies the author, publication/update dates, section, and article ID; the embedded article data exposes the account’s discussion of Arday, Chantelle Lewis, their book, neuroinclusion, and two short quotations attributed to Arday.

Decision: added SRC-554/C-716–C-717 as a secondary journalism/interview source. It is not counted as a new audio/video item or independent corroboration of the quotations. The lead image is retained as an article asset, not as a portrait. Reopen only for a changed page, correction, direct interview artifact, or independently recorded version.

## 2026-08-08 — SRC-555/C-718–C-719 UKCGE project-deck capture

Discovery: a UKCGE-hosted conference PDF surfaced in a search for distinct postgraduate-research and EDI outputs. The deck is titled “New perspectives to improve fairness and equity in PGR assessment criteria” and is dated for the 3 November 2023 UKCGE EDI-in-PGR conference.

Capture: preserved the 51-page PDF, layout-preserving text extraction, response headers, and a render of PDF page 39. That page credits Professor Jason Arday with developing the “Close the Gap” bid and separately names the project sponsor and manager.

Decision: added SRC-555/C-718–C-719 as a first-party, bounded project-role record. It is not counted as a new Arday-authored publication or as evidence that the proposed admissions reforms were funded, delivered, or evaluated. Reopen only for the underlying bid, funding/award record, project page, final report, or changed host artifact.

## 2026-08-08 — SRC-556/C-720–C-721 TEDx profile and linked-video boundary

Discovery: the *Washington Free Beacon* fundraising investigation linked an archived TEDxLadbrokeGrove biography and a TEDx Durham YouTube video. The archive snapshot was distinct from the already-catalogued contemporary campaign pages and current institutional profiles.

Capture: preserved the 8 April 2021 Wayback HTML and headers, the linked-image 404 response, and the current YouTube page, headers, and thumbnail for video ID `xbSX50Wfz6c`. The YouTube page’s embedded state identifies the video as private and requires sign-in.

Decision: added SRC-556/C-720–C-721. The TEDx page is a dated organizer-bio source version, not independent verification of its biography claims; the video is an access-boundary record, not a recovered recording. Reopen only for a lawful archived video/file, transcript, changed YouTube state, or a primary record for one of the repeated claims.

## 2026-08-08 — SRC-557/C-722–C-723 Going Postal *Question Time* review

Discovery: a search for a possible 2024 *Question Time* appearance located Going Postal’s 23 February review of the 22 February programme. The page lists Arday on a Maidenhead panel with Laura Farris, Stella Creasy, and Camilla Tominey.

Capture: preserved the page and its linked 14:36.93 MP3. The file metadata identifies an iMovie-produced MP3 titled “My Movie 2”; it is treated as the site’s review/narration artifact, not as the BBC broadcast or an Arday recording.

Decision: added SRC-557/C-722–C-723 as a low-provenance appearance lead. The page’s biography is source propagation, and its attributed political remarks remain unverified written reporting. Reopen only for an official BBC episode record, transcript/captions, broadcast audio/video, or independent event corroboration.

## 2026-08-08 — SRC-558/C-724–C-725 Broken Vessel Port Elizabeth conversation

Discovery: a focused 2019 interview/video search located Dina Zoe Belluigi’s Broken Vessel page, dated 11 September 2019, describing a roughly 40-minute conversation with Arday during an intellectual gathering in Port Elizabeth, South Africa.

Capture: the original domain now redirects to a ParkLogic expired-domain page. The article body, image, player, and recording URL were not exposed; the current browser state is preserved as a local access-boundary note.

Decision: added SRC-558/C-724–C-725 as a distinct historical media lead, separate from Belluigi’s 2019 Belfast seminar record. No substantive conversation claims or binary recovery are asserted. Reopen only with a lawful archive replay, author/institutional copy, or newly exposed media URL.

## 2026-08-08 — SRC-559/C-726–C-727 HDR UK Black Internship keynote

Discovery: HDR UK’s official 2023 internship retrospective linked a previously uncatalogued Jason Arday keynote video, YouTube ID `CwwpjBSVHKA`, and quoted one sentence from the talk.

Capture: preserved the HDR UK page and headers, the linked YouTube HTML and headers, and the two page-linked photographs. YouTube currently returns `LOGIN_REQUIRED` / private-video state; no video binary, captions, or transcript was recovered.

Decision: added SRC-559/C-726–C-727 as a first-party retrospective event record and access boundary. The quotation remains host-published and not timecoded. Reopen only for a public video state, transcript/captions, exact event-date record, or distinct keynote artifact.

## 2026-08-08 — SRC-560/C-728 and SRC-561/C-729 HDR UK opening ceremony date and delivery

Lead: a changed-state search for the HDR UK 2023 Black Internship Programme opening ceremony surfaced the original event listing and a distinct same-day post-event report, rather than another copy of the September retrospective.

Capture: the 8 June event listing schedules the ceremony for 21 June 2023 at Birmingham City University and lists Arday’s 13:45 keynote title. The 21 June report says the programme launched at the ceremony and identifies Arday as keynote speaker who gave a speech about overcoming personal challenges. Full-resolution event graphic and portrait were downloaded with response headers and hashes.

Decision: added SRC-560/C-728 and SRC-561/C-729 as distinct first-party source versions. The exact date and delivery are now independently represented within the HDR UK source family; no speech transcript, captions, or keynote binary was recovered. Keep the private YouTube manifestation under SRC-559 and do not treat promotional biography wording as independently verified.

## 2026-08-08 — SRC-562/C-730 Advance HE EDI Conference full programme

Lead: a targeted search for the already catalogued Advance HE 2025 keynote found the organizer’s full Day 2 programme PDF, distinct from the previously captured session-abstract book (SRC-326).

Capture: the one-page A3 programme records the 3 April 2025 EDI Conference schedule, placing Arday’s keynote at 09:40–10:20 in the Stephenson Suite and naming David Bass as chair. The PDF, extracted text, response headers, and rendered QA page are preserved locally.

Decision: added SRC-562/C-730 as a source-version record rather than a duplicate event. It refines the planned schedule only; no attendance, delivery, transcript, recording, or substantive keynote claim is added.

## 2026-08-08 — SRC-563/C-731–C-732 THE Campus first-person essay

Lead: a publisher search for older authored public output surfaced Jason Arday’s 28 February 2022 THE Campus essay, “Fool’s gold: career advice for young, Black academics.”

Capture: the full current HTML, response headers, and 593×444 lead image were preserved. The essay contains a direct first-person account of Arday’s self-described academic capabilities and compensatory work habits, plus a dated page biography with Glasgow, Runnymede, and British Sociological Association role labels.

Decision: added SRC-563/C-731–C-732. The first-person passage is retained as self-report, not independent psychological or performance evidence; role labels are preserved as a 2022 source-version and not harmonized with current records.

## 2026-08-08 — SRC-564/C-733 THE Campus Talks podcast page

Lead: the same publisher family exposed a distinct 9 June 2021 panel-podcast page listing Arday as a participant in a discussion of inclusive teaching, anti-racism education, and neurodiversity.

Capture: page HTML, embedded Podbean player HTML, headers, and 2695×2021 lead image were preserved. The player response did not expose a direct audio payload or downloadable media URL.

Decision: added SRC-564/C-733 as a media lead and access boundary. No audio-derived claim is added; reopen only for a direct audio file, transcript, or captions.

## 2026-08-08 — SRC-565/C-734 and SRC-566/C-735 THE 2019 authored essays

Lead: the THE Campus/Times Higher Education authored-output sweep found two distinct 2019 essays by Arday that were not represented in the archive: one on Black staff mental health and one on racial-harassment reporting in universities.

Capture: both current publisher pages, response headers, and 800×533 lead images were preserved. Their closing biographies retain the 2019 Durham, Ohio State, and Nelson Mandela University role wording as dated page versions.

Decision: added SRC-565/C-734 and SRC-566/C-735. The essays are treated as authored policy positions and public outputs, not independent evidence of implementation, clinical history, or current affiliations. The overlapping subject matter is retained as two distinct articles rather than merged.

## 2026-08-08 — SRC-567/C-736 THE 2020 authored essay

Lead: the continuing THE authored-output sweep surfaced Arday’s 3 October 2020 essay, “We must come together to dismantle racism in higher education.”

Capture: the current publisher HTML, response headers, and 724×483 lead image were preserved. The article’s closing biography records the 2020 Durham, Ohio State, Nelson Mandela University, and Runnymede roles as page-state evidence.

Decision: added SRC-567/C-736 as a distinct authored public output. The policy claims remain Arday’s 2020 argument, not proof of implementation or institutional outcomes; the biography is not treated as current.

## 2026-08-08 — SRC-568/C-737–C-738 ABC News profile article

Lead: a source-version audit of the already archived ABC News video found its distinct linked 21 March 2023 article, which had not yet been captured as a text record.

Capture: the article HTML and headers were preserved, along with the 1600×901 lead image and the 1200×1600 supplied photograph captioned as Arday at his 2016 LJMU PhD ceremony. The article’s embedded stream metadata was checked against SRC-033 and kept as an alias rather than a new video record.

Decision: added SRC-568/C-737–C-738. The interview quotation, reported biography, and image caption remain journalism/attribution evidence; they do not replace primary school, degree, employment, or clinical records.

## 2026-08-08 — SRC-088 and SRC-128 Guardian local-capture upgrade

Lead: the archive audit found that two major Guardian biography records were canonicalized in the registry but still had only URL links in their source notes.

Capture: both Guardian pages returned usable HTML and headers. The 11 July 2023 childhood profile now has a local page, portrait, and PhD-ceremony photograph; the 23 February 2023 Cambridge-appointment profile now has a local page, headers, and portrait. Image credits and source boundaries remain those of the Guardian pages.

Decision: upgraded the existing SRC-088 and SRC-128 records in place; no duplicate source IDs or new substantive claim rows were created. The pages remain reported interview/profile evidence, not independent medical, school, degree, or employment records.

## 2026-08-08 — SRC-334/C-742 Warwick keynote caption endpoint boundary

The Warwick post-event highlights page advertises an English caption track for Jason Arday’s locally preserved keynote MP4. The relative `1` endpoint was fetched directly; it redirected to a trailing-slash route and returned a 16,637-byte HTTP 404 HTML page. The response body and headers are preserved under a media access-boundary capture.

Decision: the keynote MP4 remains locally available, but no captions, transcript, or timecoded substantive claims are added. The 404 is not evidence that the video itself was removed or that the event did not occur.

## 2026-08-08 — SRC-569/C-743 LJMU thesis repository record

Lead: the live LJMU Research Online record for the doctoral thesis was identified as a distinct primary provenance layer, separate from the already-preserved thesis PDF.

Capture: the repository HTML and response headers were preserved. The record supplies the title, author form, doctoral-thesis classification, “Published Version” file label, direct PDF link, and a detailed abstract describing the four-phase qualitative study of four student teachers.

Decision: added SRC-569/C-743 as a source-version record and deduplicated it to SRC-087. The abstract is retained as repository metadata; it does not validate the thesis’s findings or resolve any later allegation.

## 2026-08-08 — SRC-570/C-744 ATU EDI programme validation report

Lead: a search for dated institutional service records surfaced ATU’s validation report for its Transformative Practices in EDI programme.

Capture: the official seven-page PDF, response headers, extracted text, and a rendered first page were preserved. Printed p. 1 records the 5 December 2022 review date, the panel membership, and Arday’s then-described Glasgow professorship.

Decision: added SRC-570/C-744 as a distinct service-record source. It is not merged with Glasgow affiliation records or treated as proof of any visiting role, employment beyond the dated description, or programme outcome.

## 2026-08-08 — SRC-571/C-745 NEON Summit 2019 programme

Lead: the conference-programme sweep found an official two-page NEON Summit programme distinct from the already archived 2022 NEON event.

Capture: the PDF, response headers, extracted text, and rendered first page were preserved. Printed p. 1 schedules Arday as a 10:40 keynote speaker on 30 January 2019 and describes him as Senior Lecturer in Education at Roehampton.

Decision: added SRC-571/C-745 as a planned-event/source-version record. No delivery, keynote content, or additional employment conclusion is inferred.

## 2026-08-08 — SRC-206/C-746 QUB attachment recheck

Lead: the older-programme search resurfaced the already catalogued Queen’s University Belfast 2019 academic-visit record, so its two advertised attachments were tested for changed access rather than duplicated.

Capture: both the PDF and DOCX routes returned HTTP 403 Cloudflare challenge HTML. The bodies and response headers were preserved under a dated recheck directory.

Decision: upgraded SRC-206 in place and added C-746. No attachment binary, recording, transcript, or seminar-content claim was added.

## 2026-08-08 — SRC-572/C-747 UKCGE 2023 post-event report

Lead: UKCGE’s first-party post-event article was found as a missing narrative source-version for the already catalogued November 2023 EDI-in-PGR conference.

Capture: the article HTML and headers, embedded YouTube page and headers, video thumbnail, and article hero image were preserved. The article reports Arday’s delivered keynote, summarizes its themes, records a standing ovation, and includes a later audience recollection.

Decision: added SRC-572/C-747 as a distinct post-event delivery record. The programme, deck, annual report, article, and linked video remain separate manifestations; no full video binary, transcript, or unqualified quotation was added.

## 2026-08-08 — SRC-573/C-748 UCL BME attainment conference report

Lead: the UCL 2018 keynote PDF was already preserved, but its first-party post-event narrative had not been captured as a separate source-version.

Capture: the current UCL route redirected to a login page. A 2020 Wayback replay was preserved and exposes the article’s dated account of the 10 April conference, Arday’s attributed remarks, and the planned institutional interventions. The current login-boundary HTML and headers were preserved alongside the archived article.

Decision: added SRC-573/C-748 as an organizer-report record distinct from SRC-022. The article’s 5.8% figure is retained with UCL’s later data-discrepancy note; no independent data validation, transcript, or implementation outcome was added.

## 2026-08-08 — SRC-574/C-749 Cambridge alternate members directory

Lead: search indexing continued to expose an Arday-associated Faculty of Education result after the individual Cambridge profile and paginated “Our People” directory stopped exposing him.

Capture: the alternate `educ.cam.ac.uk/people/members/` directory returned HTTP 200; its full HTML and headers were preserved. No exact Arday name, username, or sociology-of-education title occurred in the body.

Decision: added SRC-574/C-749 as a bounded current directory observation. It strengthens the documented indexed/live mismatch but does not establish resignation consequences, current employment, or the reason for omission.

## 2026-08-08 — SRC-575/C-750 Hiraldo primary-text recovery

Lead: Cofnas’s preserved Arday/Hiraldo comparison image identified Hiraldo (2010), pp. 53–54, but the earlier UVM landing capture was only a repository application shell.

Capture: a DSpace search API query recovered the exact UVM ScholarWorks item, its metadata and bundle records, and a public seven-page PDF. The PDF and extracted text are preserved locally with response headers and SHA-256. Printed pp. 53–54 confirm the CRT passage sequence displayed in the comparison image.

Decision: added SRC-575/C-750 as a primary comparator recovery linked to SRC-424. This strengthens the source-side textual audit while leaving the Arday full-text context, ordinary paraphrase versus deficient attribution, intent, and any institutional finding unresolved. The earlier landing capture is not treated as the primary article body.

## 2026-08-08 — SRC-576/C-751 Cambridge migrated-host profile boundary

Lead: current search indexing exposed a Faculty of Education profile on the migrated `faculty.educ.cam.ac.uk` host, with current-looking profile text and Arday’s Cambridge role.

Capture: the direct profile route redirected to the Faculty home page. The migrated “Our people” route returned HTTP 200 but contained no exact Jason Arday occurrence. Both response bodies and headers are preserved. The indexed profile was treated as a separate stale/index manifestation, not as a substitute for the direct response.

Decision: added SRC-576/C-751 as a current route/version boundary linked to SRC-208 and SRC-574. It strengthens the indexed/live mismatch and preserves the profile’s role wording as a source-version, but it does not establish resignation consequences, current employment, or the reason for the route change.

## 2026-08-08 — SRC-577/C-752 Memon–Arday methods-passage correspondence

Lead: the earlier methods-lineage audit identified a broad shared qualitative-method sequence but left sentence-level comparison as future work.

Capture: Memon (2016) PDF p. 2 and Arday (2018) PDF p. 10 were compared directly. Page renders were added to `assets/captures/2026-08-08-memon-arday-methods/pages/`.

Decision: added SRC-577/C-752 for the ordered questionnaire / facilitator / recording / verbatim-transcription / notes / flipchart / participant-view correspondence. The record is stronger than a generic methods similarity observation, but keeps copying, authorship, intent, permission, plagiarism, fraud, and institutional findings unresolved.

## 2026-08-08 — SRC-578/C-753 National Autistic Society conference announcement

Discovery: a focused first-party event search surfaced the National Autistic Society’s 15 February 2024 announcement of Jason Arday as first plenary speaker for its 14 March Annual Professionals’ Conference.

Capture: the announcement HTML and headers were preserved. The linked conference route now resolves to the current NAS conference page, and the 2026 insights page was captured as a current route/version witness; neither supplies a 2024 recording, transcript, deck, or attendee artifact.

Decision: added SRC-578/C-753. The announcement is strong evidence of a scheduled NAS appearance and preserves a host biography version saying that Arday funded his PhD through part-time Sainsbury’s/Boots work and full-time lecturing. Those employment/funding details remain biography-level claims, not independent records; no delivery inference is made from the missing current artifact.

## 2026-08-08 — SRC-316/C-754 ORIGIN current page and newsletter

Discovery: the Oxford GLAM ORIGIN page appeared in current search results with a February 2026 newsletter link not present in the earlier local capture.

Capture: the live page was preserved as a changed HTML/header version. The eight-page February 2026 newsletter PDF was downloaded from Oxford’s public site, with headers, extracted text, and a first-page render. It reports six work-package streams and planned papers, co-design, trial, and economic-review activity.

Decision: upgraded the existing SRC-316 record and added C-754 rather than creating a duplicate ORIGIN entity. The current page continues to list Arday on the project team, but the newsletter contains no Arday-specific name or contribution. It is retained as project-output context, not individual authorship or employment evidence.

## 2026-08-08 — SRC-579/C-755 Friends of Europe EYL40 profile

Discovery: the Friends of Europe European Young Leaders page surfaced a dedicated Jason Arday profile not previously represented in the registry.

Capture: the current EYL40 page and its 1062×1083 profile portrait were downloaded from the organization’s public site. The page identifies Arday as a 2024 European Young Leader and publishes a short biography with a “over £5 million” fundraising formulation.

Decision: added SRC-579/C-755 as a recognition/profile source. The recognition is a distinct institutional edge; the role, Cambridge, Runnymede, and fundraising statements remain host-published source-version wording and are not upgraded into independent legal, employment, or accounting evidence.

Follow-up: the organization’s 22 January 2024 press release was captured as a related manifestation, with its 19 March 2024 modification metadata and Class-of-2024 banner. Added C-756 to record the dated announcement without creating a duplicate EYL40 recognition node.

## 2026-08-08 — SRC-049/C-758 German National Library manifestation

Discovery: a direct German National Library PDF route for *No one can see me cry* was identified in the public catalogue result.

Capture: fetched `https://d-nb.info/1226555624/34`, preserving the PDF and response headers. The PDF is 24 pages and has the same SHA-256 as the accepted manuscript already stored locally.

Decision: recorded the route as a confirmed public manifestation of the existing accepted-manuscript version. No duplicate publication or independent evidence claim was created.

## 2026-08-08 — SRC-581/C-759 BBC Radio 4 listings manifestation

Discovery: the BBC Radio 4 schedule index exposed a contemporary 12–18 April 2025 listings PDF for *Beyond Lonely*, including the two episode IDs whose current BBC pages are unavailable.

Capture: downloaded the 19-page PDF, extracted its text, preserved response headers, and rendered the five relevant schedule pages. The PDF lists all five episodes, dates, programme IDs, synopses, producer, and presenter wording.

Decision: added the file as a source-version linked to canonical `SRC-063`. It strengthens the episode topology and changed-state record; it does not create a duplicate programme node or upgrade repeated biographical copy into independent evidence.

## 2026-08-08 — SRC-151/C-760 Juno7 sports-lead boundary

Discovery: an indexed Haitian Creole-language Juno7 result repeated the football/snooker ambition wording and appeared to offer another biography manifestation.

Capture: the direct URL returned HTTP 404; response headers are preserved, but no article HTML, image, or source text was recoverable.

Decision: added the result to the existing sports-record search boundary as a failed lead, not a new source node. It adds no corroboration and does not change the conclusion that no named club, ranking, tournament record, or professional contract has been located.

## 2026-08-08 — SRC-280/SRC-582/C-761 Quality Strategy Network full-text recovery

Discovery: Wonkhe’s page for the same 7 January 2026 Verma/Arday commentary exposed the substantive body that the originating Quality Strategy Network capture did not.

Capture: preserved Wonkhe HTML, extracted text, response headers, the 1456×816 Shutterstock feature image, and the 500×500 Arday author image. The extracted-text derivative is 12,694 bytes.

Decision: added `SRC-582` as a full-text manifestation linked to originating record `SRC-280`. The article’s EDI, academic-freedom, and university-autonomy arguments are now attributable and auditable; citations and normative claims remain the authors’ argument, not independently verified findings or implementation evidence.
# 2026-08-08 — SRC-131/C-127/C-171: *Bookseller* memoir interview changed public state

The canonical *Bookseller* memoir-interview URL was rechecked after its earlier HTTP-429 and redirect/login states. The request returned HTTP 200 and a locally preserved public HTML excerpt, plus the credited 1920×1080 Kim Lang portrait. The visible section attributes the diagnosis/speech/literacy and goal-list narrative to the memoir, reports the two-GCSE/BTEC/Sandro passage, includes family/naming and midwife material, and quotes Arday’s scrutiny framing. The page ends with “Continues…”, so this is a public excerpt rather than a complete interview. The record, claims ledger, and source registry were updated without creating a duplicate source or upgrading memoir/interview claims into independent facts.

## 2026-08-08 — SRC-612/C-824–C-825: QUB primary article manifestation

Discovery: QUB’s Research Portal exposed the canonical record for *Attempting to break the chain* and a directly downloadable PDF while the university’s separate 2026 investigation remains open.

Capture: preserved the repository HTML, response headers, PDF, and extracted text. The record gives DOI, journal, pagination, authorship, and early-online metadata. The repository labels the file “Accepted author manuscript”; the PDF front matter calls it the “Peer reviewed version.”

Decision: added a source-version record linked to canonical `SRC-045`, not a duplicate publication. The file strengthens the primary-text/version topology but does not validate the article’s methods or imply an outcome for QUB’s investigation.

## 2026-08-08 — SRC-613/C-826–C-827: *The Week* controversy synthesis

Discovery: a distinct public *The Week* analysis published 7 August 2026 mapped the controversy to Telegraph, New York Times, Daily Mail, Independent, and Guardian coverage.

Capture: preserved the complete public HTML, extracted text, response headers, and the 2000×1125 lead image.

Decision: catalogued it as a source-propagation witness. Its “officially cleared” wording is retained as an attributed lead only; the underlying decision/report was not present in the article and no adjudicative claim was promoted.

## 2026-08-08 — SRC-614/C-828–C-829: LJMU neurodiversity media boundary

Discovery: an indexed LJMU result named an Arday SoundCloud extract, “Harvest for the World: Neurodiversity and Inclusivity in Higher Education.”

Capture: fetched the current LJMU neurodiversity resource page and headers. The direct HTML lists other SoundCloud extracts but omits Arday and the title; no direct audio endpoint was recoverable.

Decision: recorded an indexed/live mismatch and a bounded media lead. The snippet is not treated as a recording, transcript, date, or delivery witness.

## 2026-08-08 — SRC-615/C-830–C-832: Telegraph student-supervision report

Discovery: the Reddit link for “Arday’s students think Cambridge failed them” exposed the canonical Telegraph URL and an Archive.today replay.

Capture: the browser-rendered replay exposed the article headline, standfirst, authors, date, and substantive reporting; a local screenshot preserves the visible article header/lead image. Direct Telegraph retrieval returned HTTP 403. Shell retrieval of the archive returned a CAPTCHA wrapper, so it is retained as an access boundary rather than article text.

Decision: added the report as a distinct source. Student complaints, grade effects, appeals, legal routes, and fee-refund demands remain attributed and unresolved; no student identity or confidential case detail was inferred.

## 2026-08-08 — SRC-264/C-401: BILT teaser caption-range audit

Audit: compared the existing BILT teaser extraction with the locally preserved `JWNqOrsUU7A.en-GB.vtt` file and replaced broad approximate windows with the caption cue ranges.

Decision: retained the extraction as automatic-caption evidence and kept manual listening verification pending. The update improves timecode provenance without upgrading caption text into a manually verified quotation or treating Bristol association as employment.

## 2026-08-08 — SRC-618/C-839: Cumberland Lodge SoundCloud audio recovered

Discovery: the SoundCloud channel page now exposes the exact “Beyond Tokenism” track slug and identifies its 3 November 2021 publication. The previously captured channel/API boundary was therefore rechecked against the direct track route and public oEmbed.

Capture: preserved the track HTML, oEmbed metadata, media-resolution response, response headers, 1080×1080 artwork, and the public 128-kbps MP3. SoundCloud metadata reports a 3,550,380-ms stream and CC BY-NC-SA licence; local audio inspection reports 3,550.38 seconds.

Decision: upgraded SRC-618 rather than creating a duplicate webinar source. The recovered file establishes the public audio manifestation, while Vimeo remains inaccessible and no transcript/captions or substantive timecoded claims are promoted. Manual listening is the next verification step.

## 2026-08-08 — SRC-572/C-840: UKCGE conference video binary recovered

Discovery: the existing UKCGE 8 November 2023 post-event record linked YouTube video `fCOP40WUUSk` but previously preserved only the player page and thumbnail.

Capture: current yt-dlp metadata reports the video as public, uploaded 8 November 2023, and 56 seconds long. The combined 640×360 MP4 and metadata JSON were downloaded; YouTube exposed no English subtitle track.

Decision: upgraded SRC-572 without creating a second event record. The binary is catalogued as a short conference montage/summary, not silently promoted to a recording of Arday’s full keynote. A longer video, manual visual/timecode review, or captions remain open.

## 2026-08-08 — SRC-161/C-841: ARU keynote player timeout recheck

Discovery: ARU’s 2021 Annual Conference page remains the canonical institutional lead for Arday’s anti-racism keynote and embeds player ID `312Fb8E6`.

Capture: reissued a browser-user-agent request to the exact player URL with a 25-second timeout. The host returned no headers or body before the connection timed out; the command result and a dated recheck note are preserved. No media manifest, MP4, HLS stream, captions, or transcript was recovered.

Decision: retained SRC-161 and added C-841 as an access-state update, not a new event. The timeout is not interpreted as deletion, nonexistence, or a recording outcome. Reopen only after a changed endpoint or lawful alternate artifact.

## 2026-08-08 — SRC-223/C-838: New Humanist audio recovered through podcast feed

Discovery: the existing New Humanist *With Reason* transcript record was rechecked against the show’s public Buzzsprout RSS feed. The feed’s episode item identifies the 15 December 2020 Jason Arday episode and exposes a public MP3 enclosure.

Capture: preserved a current New Humanist HTML page and extracted transcript, the Buzzsprout RSS item, Apple’s public podcast lookup response, response headers, and the 27,834,412-byte MP3. The audio is 2,316.54 seconds by local inspection.

Decision: upgraded SRC-223’s access state rather than creating a duplicate source. The transcript remains the auditable text layer; the MP3 is the recoverable primary audio manifestation. Manual listening and transcript comparison remain open, so no new verbatim quotations were promoted.
## 2026-08-08 — SRC-621/C-845 and SRC-262/C-846: Good Law Project solidarity-letter provenance correction

Discovery: while auditing the distinct exhibits embedded in SRC-580, a search result exposed the campaign’s short URL `https://goodlaw.social/jg0w`, which redirects to Good Law Project’s canonical petition page already represented by SRC-262.

Capture: preserved a fresh HTML/headers snapshot and the page’s 2560×1708 JPEG. The page metadata records 28 July publication and 6 August modification; the live counter displayed 17,310 signatures toward 25,000 on this recheck, versus 16,755 in the earlier SRC-262 capture. The embedded 1,077×1,746 image remains preserved as SRC-621.

Decision: corrected the provenance graph rather than creating a duplicate campaign record. SRC-621 now points back to SRC-262 as a visual/source-propagation manifestation. The campaign’s exculpatory and motivational claims remain advocacy assertions; no exoneration finding was added.
## 2026-08-08 — SRC-158/C-847: Ruling Passions preview audio recovered

Discovery: the existing Ruling Passions episode record linked only to Spotify and a Padlet embed; the Padlet route remains Sheffield Hallam tenant-login-bound.

Capture: Spotify’s public episode page exposed a platform-hosted 60.03-second, 96-kbps MP3 clip. The page snapshot and clip are locally preserved. Spotify metadata dates the episode 19 March 2022; the project page dates it 22 March 2022.

Decision: upgraded SRC-158 from transcript/link-only to transcript plus preview-audio manifestation. The clip is not treated as the full interview, and no new biographical claim was promoted from it. Full audio and the transcript’s self-reported claims remain open for future listening/verification.
## 2026-08-08 — SRC-622/C-848: Oxford EDB lecture recording boundary

Discovery: a current search result for Oxford’s 2025 EDB annual lecture identified “This is a Low: Advice for Difficult Times,” while the Oxford event URL itself had since changed to a generic page-not-found response.

Capture: preserved the Oxford 404 page and headers, the Vimeo page/headers for video `1132037139`, Vimeo oEmbed JSON, and a 1280×720 thumbnail. The oEmbed response identifies the Department of Education, Oxford as uploader, gives a 4,315-second duration, and records upload on 30 October 2025.

Decision: created a distinct event/recording node because this is a new university lecture and video manifestation. Direct Vimeo config and download attempts did not expose a lawful local stream; no MP4, transcript, or lecture timecode is claimed. Reopen only after a changed Vimeo/Oxford access state or an authorized transcript/caption artifact.
## 2026-08-08 — SRC-623/C-849–C-850: Channel 4 resignation video recovered

Discovery: a fresh `ytsearch30:Jason Arday` boundary returned Channel 4 News video `WgmVRo-1PA0`, which was not represented by an existing local video ID.

Capture: preserved yt-dlp metadata, 360p video and audio streams merged into a 12:32.12 MP4, English original captions, and the 1280×720 thumbnail. The caption map records report segments at 00:47–01:18, 01:20–01:38, and 03:38–04:00.

Decision: created a distinct broadcast-video source record, separate from Channel 4’s 2023 interview. Claims remain classified as attributed reporting; no institutional finding or truth claim was inferred. The broader YouTube search returned many additional controversy videos; their IDs are retained in the research context, and future work should deduplicate against existing news records before downloading more binaries.
## 2026-08-08 — SRC-624/C-851–C-852: LBC Arday story video recovered

Discovery: the fresh YouTube search boundary returned LBC video `D3xzh6uja_w`, which was not represented by an existing local video ID and is distinct from Channel 4’s report.

Capture: preserved LBC metadata, English original captions, a 360p video/audio merge, and the 1280×720 thumbnail. The video runs 22:54.12 and was uploaded on 8 August 2026.

Decision: catalogued the video as a broadcaster commentary/reporting manifestation. Its strong evaluative language and captioned claims remain attributed to LBC or named speakers; no underlying allegation or institutional outcome was promoted to fact.
## 2026-08-08 — SRC-625/C-853–C-854: Spiked podcast video recovered

Discovery: the fresh YouTube search boundary returned Spiked video `OIkeRnQtXQ4`, a distinct publisher podcast rather than a duplicate of the written Spiked commentary or the Channel 4/LBC reports.

Capture: preserved yt-dlp metadata, English original captions, a 640×360 video/audio merge, and the 1280×720 thumbnail. The video runs 34:18.28 and is dated 7 August 2026 by its metadata.

Decision: catalogued the video as political commentary. Its evaluative title, claims, and institutional-process discussion remain attributed to Spiked’s presenters; no allegation, biography claim, or investigation outcome was promoted to fact.
## 2026-08-08 — SRC-626/C-855–C-856: Talking Matters interview preview recovered

Discovery: a search for distinct interview and podcast manifestations returned Spotify episode `3KJMtYC3cs1gjNOafCQLfj`, a 1:18:00 *Talking Matters with Nick Halkes* episode dated 2 August 2024. Spotify’s description says the conversation was recorded in 2021 and repeats the delayed-speech/literacy and fundraising biography.

Capture: preserved the Spotify page HTML and headers, 640×640 artwork, and a public 60.03-second, 96-kbps MP3 preview. The full interview, transcript, and exact preview content analysis remain unavailable.

Decision: created a distinct Spotify platform manifestation and deduplicated it to the pre-existing full-interview record SRC-184. The description is treated as host copy/source propagation; the locally preserved full MP3 and ASR navigation remain under SRC-184. No new unrecovered interview statement or biographical claim was promoted to fact.
## 2026-08-08 — SRC-627/C-857–C-858: QUB research-misconduct procedure boundary

Discovery: the BBC-reported QUB review of *Attempting to break the chain* made QUB’s institutional research-integrity procedure a relevant primary context source. Public indexing exposes QUB’s Research Misconduct page and a linked Version 8.0, October 2021 regulations PDF.

Capture: direct fetches of both the current page and linked PDF returned CloudFront HTTP 403. The response HTML and headers are preserved. Search-indexed excerpts expose only bounded procedural context: reporting routes, initial screening, and cross-institutional cooperation.

Decision: created a procedural-context/access-boundary record rather than treating the policy as evidence about Arday’s case. Reopen only for a changed QUB endpoint, a lawful policy mirror, terms of reference, direct institutional statement, or case outcome.

## 2026-08-08 — Archive-integrity repair: TEDx path and MMU registry alias

Audit: the media index linked the TEDx local capture under `tedx-ladbroke-grove-arday`, while the existing capture directory and source record use `tedx-ladbrokegrove-arday`. The source registry also listed the single MMU keynote file under both SRC-058 and SRC-142; its front matter declares SRC-058.

Repair: corrected both TEDx links to the existing directory and removed the duplicate SRC-142 registry row, retaining SRC-058 as the canonical MMU record. No source content or claim was changed.

## 2026-08-08 — Focused institutional/media search boundary

Discovery: a bounded search across university event pages, YouTube, institutional domains, and podcast indexes returned Newcastle’s 2025 lecture, Glasgow’s 2025 event, the Oxford EDB lecture, the Ruling Passions episode, the Channel 4 interview, and the 2026 White Rose book review as already-catalogued records. The remaining hits were homonyms or already-preserved manifestations.

Decision: no new source node was created. Reopen only with a changed page, a distinct recording/transcript/binary, or a concrete uncatalogued publication lead; do not repeat these exact queries unchanged.

## 2026-08-08 — SRC-151/C-014: targeted sports-record recheck

Discovery: exact-name searches for football, Crystal Palace, snooker, footballer, and Battersea Park Rangers returned only already-catalogued biography/source-propagation pages, the existing BPR image lead, homonyms, and public discussion of the same unresolved wording.

Decision: extended SRC-151’s negative-space boundary and updated C-014 to cover the 8 August query set. No new source node or professional-status claim was created; reopen only for a named club/academy record, senior contract or appearance, snooker ranking/tournament/governing-body record, or manually verified first-person source.

The indexed Reddit discussion linked from the sports audit was also fetched directly. Reddit returned a JavaScript challenge rather than the thread body; the challenge page and headers are preserved as a changed access state. No Reddit wording is treated as recovered evidence.

## 2026-08-08 — SRC-282/C-859: Retraction Watch comments-state recheck

Capture: the current Retraction Watch page was fetched after its 5 August modification. The article body remains the earlier modified version, while the visible comment count increased from 78 to 93. Newly loaded anonymous comments repeat or expand allegations about biography, sports, fundraising, endurance, affiliations, and the thesis review.

Decision: updated SRC-282 and added C-859 as a page-state/public-reception observation. The comments remain volatile, unnamed, and unverified; no allegation was promoted to fact or institutional finding. Reopen only for named-source evidence, primary-text comparison, direct institutional records, or a materially changed article body.

## 2026-08-08 — Comparator/repository search boundary: Memon, correction, and methodology leads

Discovery: exact-title and author/comparator searches for the Memon-linked 2018 mental-health paper, the 2022 precarious-employment paper, and *Attempting to break the chain* returned the already-catalogued Cambridge correction, Roehampton/Cambridge and Glasgow/Kent repository manifestations, and existing primary-text comparison records. The results did not expose a distinct uncatalogued full text, version, DOI, or institutional finding.

Decision: no new source node or claim was created. Existing records remain canonical: SRC-382/SRC-577 for the Memon comparator and page-level correspondence, SRC-474/SRC-612 for the *Attempting* primary manifestations and comparison, and SRC-457 for the Glasgow published-version manifestation. Reopen only for a materially different primary file, a new lawful repository/publisher manifestation, or a named institutional response/outcome; do not repeat these exact queries unchanged.

## 2026-08-08 — SRC-480: RHHJ alternate PDF route deduplicated

Discovery: a fresh search surfaced the public PDF route at `rhhj.emnuvens.com.br` for Amilcar Araujo Pereira’s *Revista História Hoje* interview with Jason Arday.

Capture: the 17-page PDF was downloaded, rendered, and visually checked. Its SHA-256 is `d1c5b7803c052893630d53563edc697014c3b383918c9ce76559e0d3c8675d7b`, byte-identical to the existing SRC-480/SRC-216 journal PDF. The endpoint therefore adds a current access route and response headers, not a distinct publication or independent corroboration.

Decision: updated SRC-480’s access date and alternate URL; no new claim or source node was created. Reopen only for a materially different file, English transcript/recording, correction, or changed DOI record.
# 2026-08-08 — SRC-890 / C-897–C-898: memoir proposal version lead

## What changed

Captured the *Daily Mail* article [“Jason Arday claimed he survived ‘unrecoverable’ car accident, locked-in syndrome and testicular cancer in newly surfaced book proposal”](https://www.dailymail.com/news/article-16036797/Jason-Arday-claimed-survived-unrecoverable-car-accident.html), published 7 August 2026 and updated 8 August. The article reports alleged differences between a 2024 book proposal and the final *Great and Unfortunate Things*, including the accident/coma/locked-in-syndrome account, testicular cancer versus brain tumours, assault and suicide-attempt timing, and a Brazil prophecy. The proposal itself was not recovered.

The article’s embedded 39-second *Daily Mail* video was downloaded, as was the 1200×675 lead image. A current Reddit post that linked the article was also tested: the browser research surface exposed the post, while direct shell/API retrieval returned a 403 block; the block is preserved as access-state metadata. The article’s *Atlantic* reference was reconciled to the existing canonical `SRC-335` feature, so no duplicate Atlantic source was created.

## Evidence boundary

This records a secondary report about an unpublished proposal, not the proposal or independent medical evidence. The reported discrepancies are not promoted to facts about Arday’s health or life. The embedded video is commentary, not an adjudication. Reddit comments are public-reception material and were not used as factual corroboration.

## Re-entry

Reopen only for the proposal/manuscript itself, a changed `SRC-335` Atlantic version, a publisher correction, a direct author/publisher response, or a materially changed article/video. Do not infer that omitted proposal material was false merely because it is absent from the final memoir, or that its presence in the report proves it occurred.
## 2026-08-08 — SRC-892/C-901–C-902: Roehampton teaching account lead

Discovery: a fresh r/UniUK thread asked for experiences of Jason Arday’s teaching and exposed a long pseudonymous first-person account claiming attendance on a Roehampton module in autumn 2018.

Capture: preserved the public page HTML and response headers. The account alleges lateness, early departures, minimal academic guidance, inadequate feedback, and a disputed marking interaction; it also says a course head observed a lecture after a complaint. No course file, recording, complaint record, named witness, or institutional response was recovered.

Decision: created a distinct public-reception/lead record because it concerns a claimed 2018 Roehampton module rather than the Telegraph’s Cambridge-student report. Every substantive proposition remains an allegation by an unidentified/pseudonymous commenter. Reopen only for a lawful institutional record, contemporaneous module documentation, a direct correction/response, or an independently sourced account; do not harvest anonymous comments as corroboration.
## 2026-08-08 — SRC-893/C-903–C-904: Roehampton profile route boundary

Discovery: searching the new Roehampton teaching lead surfaced a University of Roehampton first-party profile from February 2023. The indexed text describes Arday as a former School of Education lecturer and says he secured a senior lectureship in 2018.

Capture: the historical canonical route was fetched directly. It now returns HTTP 301 to the general `/news/` landing page; the resulting HTML and headers are preserved. The current page contains no Arday article text, image, or replacement record.

Decision: added a distinct institutional source-version/boundary record. The indexed wording is evidence of what Roehampton publicly said in 2023, while the redirect documents only current route state. It corroborates a broad institutional teaching role but does not validate the anonymous Roehampton teaching allegations, any module assignment, or any reason for the route change.
## 2026-08-09 — SRC-894/C-905–C-906: Roehampton repository manifestation

Discovery: a current search for primary Roehampton records surfaced the Research Explorer page for Arday’s 2018 *Social Sciences* article on mental health and BME university students.

Capture: preserved the live metadata HTML, response headers, linked “Final published version” PDF, and PDF headers. The repository PDF is byte-distinct from the existing MDPI file under SRC-174; extracted article text is identical.

Decision: added a distinct host/version manifestation while retaining DOI deduplication. The page provides first-party publication metadata, School of Education association, CC BY wording, and a second public PDF route. It does not constitute a second publication, independent corroboration of the study’s participant narratives, or resolution of the later correction/ethics questions.
## 2026-08-09 — SRC-895/C-907: post-checkpoint source boundary

Discovery: a focused search was run after the Roehampton repository capture across Cambridge and QUB investigation outcomes, new 2026 DOI output, and current charity/governance records.

Result: the material hits were already canonical AP, BBC, *Guardian*, *Telegraph*, Cambridge/QUB procedure and statement records, First Star, Autism Centre of Excellence, BSA, and patron/governance records. No final finding, terms of reference, new DOI/title key, new filing, or distinct recording/transcript was exposed.

Decision: closed the exact query family as a negative-space checkpoint. Reopen only for a changed official endpoint, named inquiry document/outcome, new DOI, new filing, or distinct media/publication artifact; do not repeat unchanged broad queries.
## 2026-08-09 — SRC-099/C-908: Companies House changed-state recheck

Capture: the Companies House personal-appointments page was fetched again. The 61,630-byte HTML body has the same SHA-256 as the 7 August capture and still displays eight appointments, while the response headers changed and are preserved under `assets/captures/2026-08-09-companies-house-jason-arday-recheck/`.

Decision: updated the canonical legal-record note and added C-908 as a page-state observation. No new appointment, termination date, operational activity, or reason for role status was inferred. Reopen only after a changed body or concrete filing.
# 2026-08-08 — SRC-898/C-959: Amfo Talent biography manifestation

Search family: childhood, literacy, football, and snooker claims; professional biography propagation.

Searches for exact-name sports phrases, club references, and named childhood details returned the existing BBC/Lives Retold, Twinkl, News24, Bath correction, COXA, Lewisham, and Pitchero records. No new named professional club, contract, ranking, tournament result, or independent childhood record was located. The uncatalogued Amfo Talent booking profile was captured because it is a distinct public professional biography and image manifestation.

The profile markets Arday as a Cambridge professor and speaker and repeats a broad set of academic, governance, and advisory affiliations, including several stale or contested present-tense labels. It is recorded as promotional propagation evidence; no role or biographical claim was upgraded. The 800×800 portrait is preserved with its displayed EXIF credit. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-895/C-979: ORCID/Crossref scholarly-output reconciliation

Discovery: a fresh public ORCID works request and an exact-name Crossref Works query were used as a distinct scholarly discovery surface after the OpenAlex checkpoint.

Result: ORCID returned the same 11 grouped works already indexed. Crossref returned 100 ranked records from 353,692 broad results; 46 contained an exact Jason Arday author match, and every DOI/title reconciled to an existing canonical output, duplicate chapter/book manifestation, or already captured OSF preprint version. No new full text or repository manifestation was recovered.

Decision: added C-979 as a bounded negative-space checkpoint. Do not repeat these unchanged API queries; reopen for a changed ORCID record, new DOI/title, distinct repository route, or full-text artifact.
## 2026-08-09 — SRC-914/C-980: institutional-repository search boundary

Discovery: exact-name repository searches were run against LJMU Research Online, White Rose Research Online, and Open Research Online as a distinct follow-up to the identifier/index reconciliation.

Capture: LJMU returned three results, including Arday’s known 2015 doctoral thesis and two unrelated records. White Rose returned its search route without a new Arday record. Open Research Online returned an HTTP 403 Cloudflare challenge. HTML and response headers for all three routes are preserved under `assets/captures/2026-08-09-repository-search-boundary/`.

Decision: added SRC-914 and C-980 as a bounded repository search/access record. No new publication or biography entity was created; reopen only with a changed result, direct repository item, new DOI/title, or lawful access route through the blocked host.
## 2026-08-09 — SRC-915/C-981: media and event discovery boundary

Discovery: targeted exact-name searches were run for 2025–26 videos, podcasts, lecture recordings, and event programmes.

Result: UCL, ARU, Newcastle, BSA, Oxford, Bath, Crick, RSC, and Broken Vessel hits all reconciled to existing records or known access gaps. No new recording, audio file, caption track, transcript, programme, or post-event report was found.

Decision: added SRC-915/C-981 as a bounded media-search record. Reopen only with a concrete recording URL, caption/transcript body, downloadable programme or slide deck, post-event report, or materially changed host page.
## 2026-08-09 — SRC-916/C-982: Ohio State affiliation route recheck

Discovery: first-party Ohio State search, former Office of Diversity and Inclusion, and Faculty Affairs routes were checked against the unresolved visiting-role claim.

Capture: the general search route exposed no Arday-specific result; the ODI route redirected to Ohio State’s DEI reorganization announcement; and the Faculty Affairs search returned HTTP 404. HTML and response headers for all routes are preserved under `assets/captures/2026-08-09-ohio-state-role-route-recheck/`.

Decision: retained the Ohio State claim as contested and historically source-versioned. No direct appointment record was promoted, and the route state was added as SRC-916/C-982.
## 2026-08-09 — SRC-917/C-983: public filing search boundary

Discovery: exact-name Charity Commission and Companies House searches were run for appointments, terminations, annual reports, accounts, and governance records.

Result: all material hits reconciled to existing First Star, BSA, Adult Literacy Trust, Autism Centre of Excellence, Runnymede, B.S.A. Publications, Crosstown Traffic, and personal-appointments records. No new filing, annual report, accounts PDF, appointment, or correction appeared.

Decision: added SRC-917/C-983 as a bounded public-record checkpoint; reopen only for a changed regulator page, new filing date, new annual report/accounts PDF, or named appointment/termination record.
## 2026-08-09 — SRC-918/C-984: StoryGraph memoir-reception recheck

Discovery: current review searching surfaced a StoryGraph indexed count of 12 reviews for *Great and Unfortunate Things*, compared with the single ARC review previously captured.

Capture: the direct StoryGraph route returned a fresh Cloudflare challenge; HTML and headers are preserved under `assets/captures/2026-08-09-storygraph-memoir-recheck/`. No new full review body, image, audio, or book file was recovered.

Decision: added SRC-918/C-984 as a changed reception/access state, deduplicated to SRC-436. Reader summaries remain reception evidence only.
## 2026-08-09 — SRC-919/C-985: Cambridge statement availability reversal

Discovery: the canonical Cambridge investigation-statement URL was fetched again after its same-day HTTP 200 reappearance.

Capture: the later response returned HTTP 404 with a generic not-found shell, fresh response metadata, and no statement text or outcome. HTML and headers are preserved under `assets/captures/2026-08-09-cambridge-statement-recheck-404/`.

Decision: added SRC-919/C-985 as a volatile missing-source state linked to SRC-912. The page’s disappearance is not interpreted as a finding, withdrawal rationale, or conclusion.
## 2026-08-09 — SRC-920/C-986: 30 in 35 image partial recovery

Discovery: the archived image URLs listed in SRC-377 were retried to pursue actual campaign binaries.

Capture: three duplicated logo graphics were recovered from both Wayback snapshot timestamps; eight earlier personal-photo URLs returned 404 and five later-photo URLs returned connection failures. The binaries and their hashes are preserved under `assets/captures/2026-08-09-30in35-image-recheck/`.

Decision: added SRC-920/C-986 as a partial recovery linked to the contemporaneous campaign blog. No portrait or marathon photograph was promoted, and no claim about completion or fundraising was upgraded.
## 2026-08-09 — SRC-925/C-991: direct PubPeer search boundary

Discovery: PubPeer’s public search shell accepted the exact-name query `Jason Arday`, but the corresponding API returned a human-verification requirement. Direct publication routes for the 2018 *Social Sciences* DOI and the 2021 *Educational Philosophy and Theory* DOI returned HTTP 404.

Decision: preserve the HTML, API response, headers, and hashes as an incomplete access-state boundary. Do not treat the API challenge or the two 404s as proof that no PubPeer record exists. Reopen only for a human-verifiable result, alternate identifier, direct Arday publication page, or changed response. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-926/C-992: Atlantic source-version and audio recovery

Discovery: the Atlantic feature’s current HTML was byte-distinct from the 8 August capture but substantively unchanged in the compared article text. The page exposed a public Megaphone audio URL; the 18.4 MB MP3 and a cropped/resized lead-image manifestation were recovered.

Decision: register a source-version node deduplicated to SRC-335 and add the audio as a media derivative, not as independent corroboration. The article’s reported memoir/proposal discrepancies and conditional discussion of possible interview-data fraud remain attributed journalism; the proposal and primary case records remain unrecovered. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-927/C-993: Wayback memoir-publisher checkpoint

Discovery: the strongest unresolved memoir lead remained the unpublished 2024 proposal discussed by *The Atlantic* and the *Daily Mail*. Exact-title web searches surfaced no proposal binary. Internet Archive advanced search for the exact title with `Arday` returned zero items; the tested Common Crawl route returned no capture. A correct Wayback CDX query for the Simon & Schuster URL family located one HTTP-200 capture dated 26 July 2026.

Capture: recovered the replayed publisher page, its compressed response body, decoded HTML, headers, CDX JSON/headers, extracted text, and SHA-256 manifest. The page preserves first-party metadata for the US hardcover edition (ISBN `9781668085578`, 288 pages, 11 August 2026 publication date, 37 Ink) and the publisher’s promotional childhood synopsis. It is a historical source-version and not independent corroboration of the synopsis.

Decision: no proposal source was created because no proposal or manuscript was recovered. The archive result is recorded as `SRC-927/C-993`; the proposal remains an explicit unresolved documentary target, and the Atlantic/Daily Mail descriptions remain attributed secondary reports. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-928/C-994: Arasite evidence-file recovery

Discovery: the Arasite home page linked a new public `plagmenu.html` index. The page says four ZIP files were submitted to Cambridge and Liverpool John Moores research-integrity offices in September 2025, were checked visually by named academics/journalists, and complement Nathan Cofnas’s analysis. The page also linked a sentence-relation diagram.

Capture: downloaded `plag1.zip` through `plag4.zip`, extracted the four DOCX files, generated plain-text derivatives, captured the host/index pages and response headers, and wrote a SHA-256 manifest. The artifacts are: a Zwozdiak-Myers summary comparison; an Aderibigbe/Christie/Le Cornu comparison; a Douglass/Smith/Smith Texas A&M source comparison; and a large Arday/Zwozdiak-Myers final grid. The diagram page’s image source points to `file:///C:/Users/darri/OneDrive/Desktop/image.jpeg`, so no diagram binary was claimed.

Evidence handling: the files preserve source-page references, comparison text, and dossier-authored classifications such as “Verbatim,” “Near-verbatim,” and “Close paraphrase.” They are useful primary artifacts of the allegation/reporting chain but are not institutional findings, peer-reviewed analyses, or four independent witnesses. The public page’s September 2025 submission claim and the DOCX core metadata dated 27 July 2026 are both preserved; no explanation for the apparent revision timing was found. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-929/C-995: Simon & Schuster audiobook source-version

Discovery: a current indexed result exposed Simon & Schuster’s dedicated audiobook edition route for ISBN `9781668126523`, which was not directly readable in the earlier audiobook check. The exact `.com`, `.co.uk`, and `.biz` routes returned Cloudflare HTTP 403 responses; the `.net` route redirected and then returned a full HTTP-200 page.

Capture: preserved the `.net` audiobook HTML, extracted text, redirect/response headers, alternate locale bodies and headers, SHA-256 manifest, a 3,000×3,000 cover, and a distinct 212×250 author-photo manifestation. The page identifies Jason Arday as both author and reader, lists “Audio Download,” Simon & Schuster Audio, ISBN `9781668126523`, 9 hours 30 minutes, and 11 August 2026. The cover is byte-identical to the existing audiobook cover and was deduplicated.

Decision: no audio binary, sample, transcript, or new biography claim was promoted. The page’s synopsis and present-tense Cambridge biography remain publisher marketing copy. Its HTML canonical link points to the `.com` hardcover URL despite JSON-LD identifying the audiobook ISBN; this metadata anomaly and the differing locale access states are preserved as source-version topology. Google Drive was not updated; GitHub remains the active publication target.
## 2026-08-09 — SRC-1030/C-1030–C-1034: Wellcome Sanger Institute interview

A new subject-centred lead was recovered as a public Wellcome Sanger Institute YouTube video: “Sanger Institute - Research Excellence - Dr Jason Arday, Durham University,” uploaded 30 November 2021. The 1080p audiovisual file, thumbnail, metadata, and English automatic captions are locally preserved. The interview adds timecoded first-person material on Arday’s PhD/medical account, 2015 and 2019 career milestones, research and counselling claims, and Black-history curriculum argument. It is retained as self-report and host metadata, not independent corroboration. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1035/C-1035–C-1037: RSC recording timecode audit

The canonical 13:23.92 Royal Society of Chemistry Inclusion and Diversity Forum recording was extracted and transcribed with `mlx-community/whisper-small.en-mlx`. The pass separates a likely Arday opening segment (approximately 00:00–01:44) and late interview/remarks segment (approximately 09:09–13:16) from the middle montage of other speakers. It adds navigation for Arday-relevant remarks on intersectionality, evidence, shared responsibility, and community of practice. ASR remains unverified; no verbatim quotation or substantive empirical claim was upgraded. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1038/C-1038–C-1042: Lives Retold page-level audit

The Wayback-recovered 11-page PDF of Arday’s 20 March 2021 BBC Radio 4 Lent Talk was audited by printed/page location. It adds bounded self-report on one-sided deafness, speech/literacy, football/snooker, endurance chronology, fundraising, the April 2019 Durham interview, and a statement that two benign brain tumours were diagnosed after the PhD. The latter materially conflicts with the Sanger interview’s account of a brain tumour removed two weeks before the viva and a post-viva stroke. Both source versions are preserved without medical inference or harmonization. Google Drive was not updated; GitHub remains the active publication target.
# Research log

## 2026-08-09 — SRC-1096/C-1284–C-1287: fundraising chronology reconciliation

The campaign-specific statement in the St Mary's Values Talk was compared with the canonical 2009 St Mary's alumni record, the 2010 JustGiving display, the contemporaneous *Tes* report, the archived 30-in-35 blog, the 2011 JustGiving retrospective, and the 2024 St Mary's/Anglia Ruskin institutional aggregates.

Decision: the record supports multiple fundraising activities and public campaign records, but not a single reconciled accounting series. The 2020 “just over £300,000” statement is retained as a dated first-person account and remains in tension with the lower 2010/2011 campaign totals. Added SRC-1096 and C-1284–C-1287; no fraud or intent conclusion was drawn. Reopen only for beneficiary confirmation, campaign accounts, contemporaneous coverage of the larger figure, or a source defining whether it was personal, team-wide, or cumulative.

## 2026-08-09 — SRC-1095/C-1277–C-1283: St Mary's Values Talk audio audit

The official 46:15 St Mary's Students' Union video was already locally preserved, but its advertised YouTube caption response was zero-byte. A Whisper `base.en` pass over the 640×360 MP4 created a durable JSON navigation derivative. The subject-centred windows cover Arday’s childhood/literacy self-report, claimed university admissions and football scholarship, financial hardship and fatherhood, St Mary's football roles, a specific just-over-£300,000 fundraising account, and public positions on charity and student-union inclusion.

Decision: added SRC-1095 and C-1277–C-1283 without treating ASR as a transcript or any self-report as independent corroboration. The video and derivative JSON are preserved; human listening, corrected captions, and independent admissions/sports/fundraising records remain the next verification layer. Google Drive was not updated; GitHub remains the active publication target.

## 2026-08-09 — SRC-1092/C-1268: Newcastle AllEvents aggregator boundary

The AllEvents page for the 14 October 2025 Newcastle “Sign o’ the times” lecture was fetched after the university and Eventbrite records had already been preserved. It agrees on title, venue, date, local start time, and ended state, and displayed “303+ Interested.” No recording, transcript, slides, named attendee account, or recoverable attendee photograph was exposed. The page is retained as a reception/source-version artifact and deduplicated to the canonical Newcastle event; the counter is not treated as attendance or delivery evidence.
