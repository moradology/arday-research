---
id: SRC-235
type: radio appearance lead / institutional social post
title: "BBC Radio 4 Today — student-loan English GCSE proposal"
subject: ../entities/jason-arday.md
published: 2026-06-23
event_date: 2026-06-18
accessed: 2026-08-07 (current-state recheck)
status: Reported broadcast appearance; official BBC programme metadata remains live; audio not locally recovered
evidence_class: first-party professional-association social post repeating a broadcast appearance; BBC asset unresolved
urls:
  - https://www.linkedin.com/posts/tina-haux-13a057219_today-18062026-bbc-sounds-activity-7475200675874955264-54d7
  - https://www.bbc.co.uk/sounds
  - https://www.bbc.co.uk/programmes/m002xp5j.json
  - https://www.theguardian.com/education/2026/jun/17/students-pass-gcse-english-university-loans-proposals
assets:
  - ../assets/documents/sra-linkedin-bbc-today-jason-arday-2026.html
  - ../assets/documents/sra-linkedin-bbc-today-jason-arday-2026-headers.txt
  - ../assets/images/sra-bbc-today-jason-arday-2026-linkedin.jpg
  - ../assets/documents/bbc-sounds-search-jason-arday-2026-08-06.html
  - ../assets/documents/bbc-sounds-search-jason-arday-2026-08-06-headers.txt
  - ../assets/metadata/sra-bbc-today-jason-arday-2026-capture-2026-08-06.md
  - ../assets/documents/bbc-today-jason-arday-2026-08-06/programme.json
  - ../assets/documents/bbc-today-jason-arday-2026-08-06/sounds-page.html
  - ../assets/documents/bbc-today-jason-arday-2026-08-06/linkedin.html
  - ../assets/documents/bbc-today-jason-arday-2026-08-06/SHA256SUMS
---

# BBC Radio 4 *Today* — 18 June 2026

A 23 June 2026 post by Tina Haux, resharing Social Research Association material, says Jason Arday spoke on the BBC Radio 4 *Today* programme the previous week about proposals reportedly being considered by the Department for Education to require a pass in GCSE English to access university loans. The post says he addressed the education attainment gap, non-traditional learning routes, and social mobility, and points listeners to approximately 1:52 in the programme.

## Evidence boundary

The local HTML preserves the LinkedIn page’s structured metadata and post text, including the “Today - 18/06/2026 - BBC Sounds” label. This is strong evidence of a publicly reported broadcast appearance, but it is not the BBC programme page or a transcript. BBC Sounds is retained as an unresolved host lead; no episode identifier, audio file, caption track, or transcript was exposed in this capture. The preserved image is generic *Today* programme artwork, not a Jason Arday portrait.

## Changed-state follow-up — 6 August 2026

The current BBC Sounds page for the discovered PID `m002xp5j` returns HTTP 404, but the official BBC programme JSON endpoint `https://www.bbc.co.uk/programmes/m002xp5j.json` returns HTTP 200. It identifies a BBC Radio 4 *Today* episode titled “18/06/2026,” first broadcast at 06:00 BST on 18 June 2026. Its canonical original version is `m002xp5h` with a nominal duration of 10,740 seconds (2h59m); three additional versions are listed: `p0nqc88t` (shortened, 10,800 seconds), `p0nsndp3` (podcast, 5,451 seconds), and `p0nsry2l` (podcast, 10,800 seconds). The four tested public `audio-download-gb-aac` media-selector requests returned HTTP 404 `selectionunavailable`, so no audio binary is claimed. The current LinkedIn page now makes the episode PID discoverable through its BBC link, but remains a secondary social-post witness to Arday’s segment and topic.

This is an upgrade to SRC-235, not a duplicate source. The PID and programme metadata verify the existence and date of the BBC episode; they do not independently verify the SRA’s approximate 1:52 time position or establish the wording of Arday’s remarks. Reopen only after a changed BBC media state, transcript, or lawful public recording appears.

## Local preservation — 6 August 2026 upgrade

- [BBC programme JSON](../assets/documents/bbc-today-jason-arday-2026-08-06/programme.json) — SHA-256 `e2ce05e567a450a83906d03d1938187231363f2d7695b332b815cdfb14c88c15`
- [BBC JSON headers](../assets/documents/bbc-today-jason-arday-2026-08-06/programme-json-headers.txt) — SHA-256 `f89e17ea8954807984a65aa8a0541bd629d48bb28c818d219cc75e42274b5fd3`
- [BBC Sounds 404 HTML](../assets/documents/bbc-today-jason-arday-2026-08-06/sounds-page.html) and [headers](../assets/documents/bbc-today-jason-arday-2026-08-06/sounds-page-headers.txt)
- [Current LinkedIn post](../assets/documents/bbc-today-jason-arday-2026-08-06/linkedin.html) and [headers](../assets/documents/bbc-today-jason-arday-2026-08-06/linkedin-headers.txt)
- [Media-selector responses](../assets/documents/bbc-today-jason-arday-2026-08-06/) — four PID-specific JSON/HTTP-header pairs, all `selectionunavailable`/404 at capture time
- [Upgrade checksums](../assets/documents/bbc-today-jason-arday-2026-08-06/SHA256SUMS)

## Current-state recheck — 2026-08-07

The BBC programme JSON for `m002xp5j` remains HTTP 200 and its episode/version metadata is unchanged: first broadcast 18 June 2026, canonical version `m002xp5h`, and the same shortened/podcast version IDs. The BBC Sounds page remains a 404 “Page not found.” No audio binary, transcript, or exact segment timecode is claimed.

- [Programme JSON](../assets/captures/2026-08-07-bbc-today-2026-recheck/programme.json) — 1,868 bytes; SHA-256 `e2ce05e567a450a83906d03d1938187231363f2d7695b332b815cdfb14c88c15`.
- [Programme headers](../assets/captures/2026-08-07-bbc-today-2026-recheck/programme.json.headers.txt) — SHA-256 `78604fdc062783b634221f11b11a3eb501ef6e57ed4f10a53e81335da4b152f0`.
- [Sounds HTML](../assets/captures/2026-08-07-bbc-today-2026-recheck/sounds.html) — 135,104 bytes; SHA-256 `5364868aa82ad57ae01dfb3002af526f4763d10d593b3ab9062eb9fd5d8a2971`.
- [Sounds headers](../assets/captures/2026-08-07-bbc-today-2026-recheck/sounds.headers.txt) — SHA-256 `6b1a2772e23560be05478d0abf8d676bb80883cde5a08452ab1817b9b6b73df8`.

## Current-state recheck — 2026-08-08

The canonical BBC Sounds route `m002xp5h` and the podcast route `p0nsry2l` still return HTTP 404. The live programme JSON for `m002xp5h` remains HTTP 200 and continues to expose episode metadata only. No audio binary, transcript, caption track, or segment-level evidence was recovered.

- [Canonical Sounds HTML](../assets/captures/2026-08-08-bbc-today-2026-recheck/canonical-sounds.html) — SHA-256 `051b389f5cbd1b60427468cab027349671d4c065ed25a9a27f1a55d9b64c34dc`.
- [Canonical Sounds headers](../assets/captures/2026-08-08-bbc-today-2026-recheck/canonical-sounds.headers.txt) — SHA-256 `cbddbc2a3e8c468a233983a933ea1b9ffca2fb4717acfd8b8933df99e9d32212`.
- [Podcast route HTML](../assets/captures/2026-08-08-bbc-today-2026-recheck/podcast-sounds.html) — SHA-256 `b5ad64e5605dc855f8b26b8414a87d692c99e33058047f8b43664992c2feac6`.
- [Podcast route headers](../assets/captures/2026-08-08-bbc-today-2026-recheck/podcast-sounds.headers.txt) — SHA-256 `ce3a24b55d1bea147011db3605587d1769f5b0e082f075d178fb6369d828c20c`.
- [Programme JSON](../assets/captures/2026-08-08-bbc-today-2026-recheck/programme.json) — SHA-256 `e4d06e1ad5349819c1e3aabdc2f9dd2b052cc0afa80f5d3ba7d6d60f159c1f96`.
- [Programme JSON headers](../assets/captures/2026-08-08-bbc-today-2026-recheck/programme.json.headers.txt) — SHA-256 `ccec17180ed38bea719b783e689546d537cbeb161e4dfb31a2d106907b6b1e06`.
