---
id: SRC-130
type: radio broadcast
title: "Today — Professor Jason Arday guest editor"
subject: ../entities/jason-arday.md
published: 2023-12-30
accessed: 2026-08-06
status: programme record and API metadata locally preserved / audio unavailable through tested public endpoints
evidence_class: BBC programme listing and contemporary radio listing
---

# Record

BBC Radio 4’s *Today* programme listing identifies Professor Jason Arday as guest editor on 30 December 2023. The listing describes his focus on the stigma and shame associated with low adult literacy. A contemporaneous Radio 4 listings PDF independently identifies the same programme and guest-editor role.

The current BBC programme JSON endpoint (`m001ts2s.json`) remains publicly retrievable and identifies the item as a BBC Radio 4 audio episode. It gives the first-broadcast time as 30 December 2023 at 07:00 UTC, the canonical version PID as `m001ts2q`, and a nominal duration of 7,200 seconds. Its long synopsis repeats the public biography version that Arday was diagnosed with global developmental delay and autism at three, learned to speak at eleven, and learned to read and write at eighteen; it also says the programme looked at 1990s culture. These are BBC programme-copy claims, not a transcript or independent developmental record.

## Evidence boundary

The programme record verifies the broadcast listing and role, not the survival or completeness of the audio. On 6 August 2026, the BBC Sounds UK path returned a 404 page, the BBC.com audio path returned 404, and a legacy BBC media-selector request returned HTTP 410. The JSON metadata exposed no playable media URL, selector link, or transcript. The official page and its 1200×675 episode image were locally preserved on 2026-08-06; the audio remains unresolved.

## Links

- BBC programme page: https://www.bbc.co.uk/programmes/m001ts2s
- Radio 4 listings archive: https://www.radio-lists.org.uk/r4/R4_2023_1230-0105_3columns_6pt_19pages.pdf
- Local preservation copy: `../assets/documents/bbc-radio4-listings-2023-12-30.pdf`
- Local BBC page snapshot: `../assets/documents/bbc-today-jason-arday-page-2026-08-06.html`
- [Programme JSON](../assets/documents/bbc-today-jason-arday-programme-2026-08-06.json) — SHA-256 `e4998a8bbfaf8f875db1c0820e453541253dfa0497e2ce8fad6c357d459a4851`
- [BBC Sounds 404 body](../assets/documents/bbc-today-jason-arday-sounds-404-2026-08-06.html) and [headers](../assets/documents/bbc-today-jason-arday-sounds-404-headers-2026-08-06.txt)
- [BBC media-selector 410 body](../assets/documents/bbc-today-jason-arday-mediaselector-410-2026-08-06.html) and [headers](../assets/documents/bbc-today-jason-arday-mediaselector-410-headers-2026-08-06.txt)
- [BBC.com audio 404 body](../assets/documents/bbc-today-jason-arday-bbccom-404-2026-08-06.html) and [headers](../assets/documents/bbc-today-jason-arday-bbccom-404-headers-2026-08-06.txt)
- Local BBC episode image: `../assets/images/bbc-today-jason-arday.jpg`
- Capture metadata: `../assets/metadata/bbc-today-jason-arday-capture-2026-08-06.md`
