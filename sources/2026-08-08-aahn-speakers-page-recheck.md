---
id: SRC-903
type: official event site / changed speaker-page source-version
title: "African Allied Healthcare Summit 2026 — speakers page recheck"
subject: ../entities/jason-arday.md
event_date: 2026-07-23/2026-07-24
accessed: 2026-08-08
status: verified HTTP 200 changed page state; keynote listing remains; event delivery unresolved
evidence_class: organizer first-party speaker page / local HTML, headers, and image / changed access state
updates: sources/2026-07-23-african-allied-health-summit-jason-arday.md
---
# African Allied Healthcare Summit — speakers-page recheck

On 8 August 2026, the African Allied Health Network’s `/speakers/` route returned HTTP 200 after the site-wide HTTP 403/browser-verification state preserved in [SRC-306](2026-07-23-african-allied-health-summit-jason-arday.md). The page again names **Professor Jason Arday** as a **Keynote Speaker** and describes his work as concerning education, equity, and social mobility. It also lists the other keynote speakers, convener, and confirmed speakers.

The current page exposes a first-party speaker biography and a 417×458 portrait. The portrait bytes are identical to the earlier organizer-linked portrait under SRC-306, so it is not duplicated as a new image object. The page does not provide a post-event report, final agenda, recording, transcript, attendance confirmation, or evidence of delivery; the route’s recovery is an access-state change only.

## Local preservation

- [Current speakers HTML](../assets/captures/2026-08-08-aahn-speakers-recheck/page.html) — 126,264 bytes; SHA-256 `b5a803089364f97e7d9192c0a0f41836514858e659ae7fd08f496813de6c78db`
- [Current response headers](../assets/captures/2026-08-08-aahn-speakers-recheck/page.headers.txt) — SHA-256 `06aedbcf3651fe2c8190c7a8ba7eca0f6b25ab2ce4dbeea25b76a1d07751018c`
- [Speaker portrait](../assets/captures/2026-08-08-aahn-speakers-recheck/arday-portrait.webp) — 417×458 WebP; SHA-256 `dd60e75a53486b57b8ad371f9185cbc597095e4b5c23550637610ebf87e68835`; byte-identical to the SRC-306 portrait
- [Portrait response headers](../assets/captures/2026-08-08-aahn-speakers-recheck/arday-portrait.headers.txt) — SHA-256 `25da51bdd30db8f332957e2f806e932adfa4a9ce9156d63e6b49c26ab722cd28`

## Canonical URL

- [African Allied Health Network speakers page](https://africanalliedhealthnetwork.org/speakers/)

## Evidence boundary

The recovered page strengthens current organizer-side provenance for the planned keynote and records a changed access state. It does not establish that the July summit or Arday’s keynote occurred. Reopen only for a post-event report, final programme, recording, transcript, attendance artifact, or another changed organizer state.
