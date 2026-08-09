---
id: SRC-334
type: post-event conference media
title: "We Dream the Same Dream: Collective Empowerment in Pedagogy"
date: 2026-06-04
accessed: 2026-08-09
status: earlier official Warwick post-event page and MP4 locally preserved; bounded automatic-audio audit added; caption-track endpoint recheck returned HTTP 404; later live page recheck returned HTTP 429
source_kind: university conference page / direct video
entities:
  - ../entities/jason-arday.md
urls:
  - https://warwick.ac.uk/fac/cross_fac/academic-development/education-conference/
  - https://warwick.ac.uk/fac/cross_fac/academic-development/education-conference/2026-hightlights/
  - https://warwick.ac.uk/fac/cross_fac/academic-development/education-conference/2026-hightlights/session_2-1080p-james-arday.mp4
assets:
  - ../assets/captures/2026-warwick-education-conference-jason-arday/arday-session.mp4
  - ../assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/page.html
  - ../assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/page.headers.txt
  - ../assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/highlights.html
  - ../assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/highlights.headers.txt
  - ../assets/captures/2026-08-08-warwick-keynote-caption-recheck/captions.html
  - ../assets/captures/2026-08-08-warwick-keynote-caption-recheck/captions.headers.txt
  - ../assets/videos/warwick-education-conference-2026/arday-session.tiny-en.vtt
---

# Warwick Education Conference 2026 — Jason Arday keynote

The University of Warwick’s Education Conference page records a conference held on Thursday 4 June 2026 at the Ramphal Building. The post-event highlights page identifies Professor Jason Arday as a keynote speaker from the University of Cambridge and gives his keynote title as **“We Dream the Same Dream: Collective Empowerment in Pedagogy.”** The conference theme was “Learning for a Complex and Hopeful Future: Pedagogies of Empowerment, Equity, and Global Readiness.”

The highlights page exposes a direct MP4 for Arday’s session. The page’s video markup also advertises a captions track, but no separately retrievable caption file was recovered in this capture. A later machine-audio pass produced a navigation-only VTT and a bounded audit; it is not a verified transcript and should not be quoted as exact speech. [Warwick keynote audio audit](2026-08-09-warwick-keynote-audio-audit.md)

## Local preservation

- [Conference page](../assets/captures/2026-warwick-education-conference-jason-arday/page.html) — SHA-256 `cca2d5bded8c5f484b012e435d85e3f783a79773c7c2ad1d8397998cb0b605c5`.
- [Conference response headers](../assets/captures/2026-warwick-education-conference-jason-arday/headers.txt) — SHA-256 `14499ce7a99028fe204d5c316f0b303d71c61842e4a4a12103cc49706ef51b10`.
- [Post-event highlights page](../assets/captures/2026-warwick-education-conference-jason-arday/highlights.html) — SHA-256 `1f5d5064747499b52d9b5900a551532f347c6a78288e467ed693c79733cd1d96`.
- [Highlights response headers](../assets/captures/2026-warwick-education-conference-jason-arday/highlights-headers.txt) — SHA-256 `16c6b48875f71707f641db95ac38acee9e2514664cfdb2c9934e18e26d10b035`.
- [Keynote MP4](../assets/captures/2026-warwick-education-conference-jason-arday/arday-session.mp4) — 138,726,243 bytes; SHA-256 `aa76c9208637513b416c0adb37751a50ebcadb542fc0ab42b84ea2a6b549034c`.
- [Drive-upload parts](../assets/captures/2026-warwick-education-conference-jason-arday/arday-session.mp4.part-000) · [part 001](../assets/captures/2026-warwick-education-conference-jason-arday/arday-session.mp4.part-001) · [part 002](../assets/captures/2026-warwick-education-conference-jason-arday/arday-session.mp4.part-002) — 50 MiB, 50 MiB, and 32,815,843 bytes; SHA-256 `32a949ac05cfdb20a749bcf1eef1fe1fd1d767db9101aad107f1e2df17626b91`, `25404c007142dcc0e65850f60fdff369c3673a3919960db5586c7b2e64a46c26`, and `78d833464c3c99b0e5980ba7d54f5ad1e323230300bc52babf2f3fdd7ecf272e`.
- [MP4 response headers](../assets/captures/2026-warwick-education-conference-jason-arday/arday-video-headers.txt) — server-declared length 138,726,243 bytes; the local file matches that length.
- [Page-linked portrait, JPEG](../assets/captures/2026-warwick-education-conference-jason-arday/arday_jason.jpg) — page-linked 170×204 image; SHA-256 `e87bf6e6d7c2f759025945a9a2abb680426bdaca705651445719400d742b9744`.
- [Highlights portrait, WebP](../assets/captures/2026-warwick-education-conference-jason-arday/arday_jason.webp) — 170×204 image; SHA-256 `54d46cc0eb1ea804ab95a324610e8868612b679d98664c70b6a847df6b960998`.
- [Whisper tiny.en navigation VTT](../assets/videos/warwick-education-conference-2026/arday-session.tiny-en.vtt) — 66,341 bytes; SHA-256 `9d3dc9f2e9aae93638fbcc1ec02bc14b534f29a3b589b4444c573b690f7b8b9e`; automatic speech recognition, not human-verified.

## Evidence boundary

The Warwick highlights page establishes that the university presented the event as post-event material and labels Arday’s session and keynote title. The local MP4 establishes a publicly retrievable video manifestation of that session. The companion audit contains only approximate machine-navigation summaries; it does not contain a human-verified transcript, and its remarks require listening before quotation or fine-grained attribution.

On 8 August 2026, the relative English caption-track endpoint advertised in the highlights page (`1`) redirected to a trailing-slash route and returned HTTP 404 HTML. No caption file or transcript was recovered; the MP4 remains the controlling media artifact.

## Changed live-page state

On 7 August 2026, direct rechecks of both the main conference route and the post-event highlights route returned identical HTTP 429 `Too Many Requests` responses from Warwick’s BigIP front end. This is an access/rate-limit boundary, not evidence that the event was removed, cancelled, or did not occur. The earlier captured 200-page responses and locally preserved keynote MP4 remain the controlling artifacts for this record.

- [Main-route recheck body](../assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/page.html) and [headers](../assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/page.headers.txt) — body SHA-256 `3850dfdbf4489250268b5f0740240a9f4445e7c5c29e1d03aa0c5446808d7507`; headers SHA-256 `fd0768b2b46725466c584acb0ead62f3dbdddf388622304cb79a82d35532c7c9`.
- [Highlights-route recheck body](../assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/highlights.html) and [headers](../assets/captures/2026-warwick-education-conference-jason-arday/recheck-2026-08-07/highlights.headers.txt) — byte-identical body and headers to the main-route recheck.
- [Caption-track endpoint recheck](../assets/captures/2026-08-08-warwick-keynote-caption-recheck/captions.html) — 16,637-byte HTTP 404 HTML response; SHA-256 `e5fb383731b1837c8e5d29706fe631d2b7800b8cfb6caf98ff7bf54c87c80a93`.
- [Caption-track response headers](../assets/captures/2026-08-08-warwick-keynote-caption-recheck/captions.headers.txt) — SHA-256 `e7ccc146455f0f9f2ae992a21b9303c5369dcdc5227199fcd1208310b8250c42`.

### Reassembly

The Drive-safe parts can be reassembled in lexical order:

```sh
cat arday-session.mp4.part-000 arday-session.mp4.part-001 arday-session.mp4.part-002 > arday-session.mp4
sha256sum arday-session.mp4
```

The resulting checksum should be `aa76c9208637513b416c0adb37751a50ebcadb542fc0ab42b84ea2a6b549034c`.
