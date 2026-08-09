---
id: SRC-904
type: podcast-platform manifestation / access-boundary source-version
title: "A Good Read — Janet Ellis and Jason Arday — Amazon Music"
subject: ../entities/jason-arday.md
published: 2023-11-21
accessed: 2026-08-08
status: episode identifier and URL preserved; direct page is JavaScript shell with no rendered metadata or audio
evidence_class: Amazon Music catalogue manifestation / local HTML and headers
related_sources:
  - SRC-061
---
# Amazon Music manifestation

Amazon Music exposes a distinct platform URL for the canonical BBC Radio 4 *A Good Read* episode featuring Janet Ellis and Jason Arday. The route identifies podcast UUID `391a33d1-48ae-4a23-b4a5-28fe1337f3cd` and episode UUID `56c9195a-9289-49c5-b418-44c95058f143` in its public deep-link metadata.

The direct 8 August 2026 response is an 11,446-byte JavaScript application shell. It does not render the episode title, description, duration, transcript, captions, artwork, or an audio URL in the captured HTML. Search-indexed Amazon metadata identifies the 21 November 2023 episode and its familiar book-discussion synopsis, but those details remain deduplicated to the BBC source record SRC-061 rather than treated as a second transcript or recording.

## Local preservation

- [Amazon Music HTML shell](../assets/captures/2026-08-08-amazon-good-read/page.html) — 11,446 bytes; SHA-256 `77717b9af462034998f7e92a9fbe33842e1f4ce303e05d6505b53acbff00886a`
- [Amazon Music response headers](../assets/captures/2026-08-08-amazon-good-read/page.headers.txt) — SHA-256 `d173bd220a986620b804e3bcc4604a34f435a1667af4b0bffbe9aab6cf3cf938`

## Canonical URL

- [Amazon Music episode](https://music.amazon.com/podcasts/391a33d1-48ae-4a23-b4a5-28fe1337f3cd/episodes/56c9195a-9289-49c5-b418-44c95058f143/a-good-read-janet-ellis-and-jason-arday)

## Evidence boundary

This record establishes a distinct Amazon platform manifestation and its episode identifiers. It adds no independently readable episode content and no audio binary. The BBC programme page and local MP3 remain canonical for the appearance; reopen only after a rendered Amazon transcript, captions, artwork, or audio endpoint becomes publicly exposed.
