---
id: SRC-276
type: institutional event report and video
title: "Royal Society of Chemistry Inclusion and Diversity Forum 2025"
subject: ../entities/jason-arday.md
published: 2025-04
event_date: 2025-03-25
accessed: 2026-08-07
status: Official RSC event report and official YouTube recording locally preserved; complete cellular derivative committed to GitHub; current caption endpoint empty
evidence_class: first-party professional-body event report and host-published video
urls:
  - https://www.rsc.org/events/detail/80493/inclusion-and-diversity-forum-2025
  - https://www.rsc.org/news/inclusion-and-diversity-forum-2025
  - https://www.youtube.com/watch?v=JbyQlddjUJ8
assets:
  - ../assets/documents/rsc-inclusion-diversity-forum-2025-article.html
  - ../assets/documents/rsc-inclusion-diversity-forum-2025-article.headers.txt
  - ../assets/videos/rsc-inclusion-diversity-forum-2025.mp4
  - ../assets/captures/2026-08-07-rsc-youtube-recheck/page.html
  - ../assets/captures/2026-08-07-rsc-youtube-recheck/page.headers.txt
  - ../assets/captures/2026-08-07-rsc-youtube-recheck/caption.empty
  - ../assets/captures/2026-08-07-rsc-youtube-recheck/caption.headers.txt

# Royal Society of Chemistry Inclusion and Diversity Forum 2025

The Royal Society of Chemistry’s event page dates its 2025 Inclusion and Diversity Forum to 25 March 2025 at Burlington House, London, and lists Jason Arday among the speakers. Its post-event report says that Arday delivered a presentation titled “Sign O Times: Trying to convey hope in challenging times.” The RSC’s official YouTube upload is locally preserved as a 13:24 MP4; the downloaded recording is the full event video rather than an Arday-only extract, so the relevant segment still requires manual timecoding.

## Evidence boundary

This source verifies a first-party event record and a first-party recording. It does not by itself establish the contents of Arday’s presentation beyond the title and the RSC’s report that it occurred. The event-page biography is host copy and should be treated as a dated affiliation witness, not a complete current biography. The MP4 is a research-preservation copy of a public YouTube upload; redistribution remains subject to the host’s rights and terms.

## 2026-08-07 changed-state recheck

The current YouTube page embeds an English (United Kingdom) caption-track URL in its player metadata, but the visible player reports “Subtitles/closed captions unavailable.” A direct request to the timed-text endpoint returned HTTP 200 with `content-length: 0`; the browser opened the same observed endpoint without exposing caption text. This is preserved as a missing-source/access-state observation, not as a usable transcript or timecoded evidence.

The direct report-PDF URL surfaced by the RSC publication search was also rechecked. It redirected to the RSC news route and then returned HTTP 429 from the host’s PALSS layer; no PDF bytes were delivered. This is an additional access boundary for the same first-party report, not a separate report version.

## Local capture

- Article HTML: 169,011 bytes; SHA-256 `eaa3c0c77e31a00cba319d5fd78f899ce1994398fabca29dfd4d82e85d4595c7`.
- Article response headers: SHA-256 `e37eefe947a59f2c1fcdef14d6bcf305bd7c1ac8badffcf097996f60b182ecdb`.
- YouTube MP4: 106 MiB; SHA-256 `9428506234ca3255221ec08fa3a2da652c9c97dda45b1bc0c32d1548c6652aa3`; yt-dlp metadata reported 13:24.
- [YouTube recheck page](../assets/captures/2026-08-07-rsc-youtube-recheck/page.html) — 1,287,393 bytes; SHA-256 `95b29a0de59ac68b39e6042a8424a31bf7b0b5bd27905b391f7e1257b0ffeb48`.
- [Empty caption response](../assets/captures/2026-08-07-rsc-youtube-recheck/caption.empty) — 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; [response headers](../assets/captures/2026-08-07-rsc-youtube-recheck/caption.headers.txt) record HTTP 200 and zero content length.
- [Report-PDF recheck response](../assets/documents/rsc-inclusion-diversity-forum-2025-report-429.html) — 185-byte HTTP 429 HTML response; SHA-256 `9d00b41a7b98a9eb4f7a3d3fb7610790bbbcbf24487ef6cf6efb10bd84c47392`; [headers](../assets/documents/rsc-inclusion-diversity-forum-2025-report-429.headers.txt).
- [Complete cellular derivative](../assets/videos/derivatives/rsc-inclusion-diversity-forum-2025-cellular.m4v) — 26,236,081 bytes; SHA-256 `4d8d06ffc4cecd7df6f24676bb41a5818b795166b4fda9fc5663709a6e3ae4f7`.

The derivative preserves the complete 13:24 event video in lower-quality form; it is not the source master or a transcript. The 111,253,519-byte master hash remains `9428506234ca3255221ec08fa3a2da652c9c97dda45b1bc0c32d1548c6652aa3` and the original remains local-only because it exceeds GitHub’s 100 MiB hard limit. The zero-byte caption endpoint and untimecoded Arday segment boundary remain unchanged.
