---
id: SRC-283
type: institutional directory access-boundary capture
title: "Cambridge Faculty of Education Our People directory — direct page-1 capture"
subject: ../entities/jason-arday.md
accessed: 2026-08-07
status: direct page-1 HTML rechecked; byte-identical response still does not reproduce Arday entry
evidence_class: first-party directory state / bounded negative observation
urls:
  - https://faculty.educ.cam.ac.uk/about-us/our-people?page=1
assets:
  - ../assets/documents/cambridge-faculty-our-people-2026-08-06.html
  - ../assets/documents/cambridge-faculty-our-people-2026-08-06.headers.txt

# Cambridge Faculty “Our People” directory

The direct page-1 response was captured on 6 August 2026 after a search-index result appeared to list Jason Arday as Professor of Sociology of Education. The locally preserved HTML is a 72,378-byte HTTP 200 Drupal page, but its page-1 body does not reproduce “Jason Arday,” “jaa80,” or “Professor of Sociology of Education.” This is a response-state observation, not evidence that the Faculty directory contains no Arday entry: pagination, rendering, indexing lag, and alternate query states remain possible.

## Recheck — 2026-08-07

A fresh direct request to the same page-1 URL returned the same 72,378-byte HTML and the same 433-byte response-header file. SHA-256 hashes are identical to the 6 August captures (`6cd3766e2af4da5623661766b68df54f91c450df68abe1ed6eea6a5946567624` and `b7d62ff157b71d08b7481d972690c257949de2679fee00d19a98d30d10756b27`); the body still contains no `Jason Arday`, `jaa80`, or role match. The current search-index snippet therefore remains an indexed/direct-response mismatch, not a newly verified Cambridge appointment record.

## Evidence boundary

Keep this record separate from the already captured individual-profile 404 state (SRC-208) and from search-index text. The captured directory page does not independently confirm current employment, resignation, or any other role. Reopen only with a changed directory page, a confirmed pagination/API route, or a directly rendered Arday entry.

## Local preservation

- HTML: `assets/documents/cambridge-faculty-our-people-2026-08-06.html` — SHA-256 `6cd3766e2af4da5623661766b68df54f91c450df68abe1ed6eea6a5946567624`.
- Headers: `assets/documents/cambridge-faculty-our-people-2026-08-06.headers.txt` — SHA-256 `b7d62ff157b71d08b7481d972690c257949de2679fee00d19a98d30d10756b27`.
- Recheck HTML: `assets/documents/cambridge-faculty-our-people-2026-08-07.html` — byte-identical to the 6 August capture.
- Recheck headers: `assets/documents/cambridge-faculty-our-people-2026-08-07.headers.txt` — byte-identical to the 6 August capture.

## Recheck — 2026-08-07 current indexed/live mismatch

A fresh direct `curl` request to the canonical page-1 URL returned the same 72,378-byte HTML as the 6–7 August captures, with identical body SHA-256 `6cd3766e2af4da5623661766b68df54f91c450df68abe1ed6eea6a5946567624` and header SHA-256 `b7d62ff157b71d08b7481d972690c257949de2679fee00d19a98d30d10756b27`. The body still contains no “Jason Arday,” `jaa80`, or “Professor of Sociology of Education.” Search-index text that exposes an Arday entry is therefore not a live-page confirmation and does not establish current Cambridge employment or resignation status.

This exact endpoint is closed for the current pass. Reopen only after a changed direct response, confirmed pagination/API route, or a directly rendered entry.
