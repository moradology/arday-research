---
id: SRC-878
type: podcast source-version / migrated project host / platform manifest / local HTML and headers
title: "Ruling Passions Episode 2 — migrated host and Amazon Music manifestation"
subject: ../entities/jason-arday.md
published: 19–22 March 2022 episode; host migration state accessed 2026-08-08
accessed: 2026-08-08
status: distinct host/platform manifestations; deduplicated to canonical interview SRC-158
evidence_class: first-party project-page source-version and platform catalogue metadata/access boundary
urls:
  - https://ruling-passions.com/2022/03/22/podcast-launch-episode-2/
  - https://music.amazon.in/podcasts/fda77f9e-b8c9-4576-af16-74c2f066dc1f/episodes/e8465482-92dd-477c-8999-4bffacbd515a/ruling-passions-ruling-passions-2-a-discussion-with-jason-arday
related:
  - SRC-158
  - SRC-873
assets:
  - ../assets/captures/2026-08-08-ruling-passions-migrated/ruling-passions.html
  - ../assets/captures/2026-08-08-ruling-passions-migrated/ruling-passions.headers.txt
  - ../assets/captures/2026-08-08-ruling-passions-migrated/amazon.html
  - ../assets/captures/2026-08-08-ruling-passions-migrated/amazon.headers.txt

# Ruling Passions — changed host and platform topology

The project’s migrated `ruling-passions.com` URL returned the Episode 2 page while retaining the older WordPress-hosted transcript, project description, Spotify embed (`1O33ppNFEct0Xv8HIyg8VY`), and Padlet embed. The migrated page therefore preserves the canonical interview’s transcript and episode identity but is a new host-state capture, not a second interview.

Amazon Music exposes a separate catalogue manifestation titled “Ruling Passions: 2. A discussion with Jason Arday,” with episode identifier `e8465482-92dd-477c-8999-4bffacbd515a`, a 19 March 2022 date, and a displayed duration of 51 minutes in indexed metadata. The direct Indian Amazon page returned an 8,409-byte JavaScript application shell; no audio URL, transcript, image, or additional episode content was exposed in the captured HTML. The indexed Amazon description repeats the project’s existing episode synopsis and is not treated as independent biography evidence.

## Deduplication and state boundary

This record strengthens the episode’s host migration and platform identity map. It does not create a new appearance, new transcript, new biography claim, or full-audio capture. The full transcript and 60-second Spotify preview remain canonical under [SRC-158](2022-03-22-ruling-passions-jason-arday.md); the 2023 handbook remains the separate project-document corroboration under [SRC-873](2022-03-22-ruling-passions-jason-arday.md).

## Local preservation

- Migrated project page: `assets/captures/2026-08-08-ruling-passions-migrated/ruling-passions.html` — 202,194 bytes; SHA-256 `47006740e68eab1fa4eed7b99cda9b29acca2570aca6a8080fa28dce2fc372f3`.
- Migrated project response headers: `assets/captures/2026-08-08-ruling-passions-migrated/ruling-passions.headers.txt` — SHA-256 `469bbf8509d68d0fda1b292b4636f28976220aa90c92bc3bdaabb333de4b8031`.
- Amazon Music shell: `assets/captures/2026-08-08-ruling-passions-migrated/amazon.html` — 8,409 bytes; SHA-256 `49e8eb5c667fec637180006d2ab781465f1bb3e536cfbea46c406b8e5ad243cb`.
- Amazon Music response headers: `assets/captures/2026-08-08-ruling-passions-migrated/amazon.headers.txt` — SHA-256 `32670c3838911cdd7f0d21133295d13214d5cbcfd5c6ef14c98e1cfcb780995c`.
