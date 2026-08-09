---
id: SRC-1151
type: primary audio audit
title: "BBC Radio 4 Moral Maze — Racial Justice audio audit"
subject: ../entities/jason-arday.md
published: 2020-06-18
accessed: 2026-08-09
status: bounded machine-assisted audit of canonical MP3; not human-verified transcript
evidence_class: first-party broadcast audio / public-position source-version / ASR navigation
related_sources:
  - SRC-060
claims:
  - C-1428
  - C-1429
  - C-1430
  - C-1431
  - C-1432
assets:
  - ../assets/audio/bbc-moral-maze-racial-justice.mp3
  - ../assets/documents/bbc-moral-maze-racial-justice/bbc-moral-maze-racial-justice-whisper-small-en.json
urls:
  - https://www.bbc.co.uk/programmes/m000k3gr
---

# BBC Radio 4 *Moral Maze* — bounded audio audit

The preserved 42:56 BBC broadcast was converted to corrected mono WAV and sampled in five long windows with `mlx-community/whisper-small.en-mlx`. The audit locates Arday’s contribution at approximately 18:06–25:28 of the source audio and separates it from the presenter, panel, and other witnesses. It is a navigation derivative, not a complete transcript.

## Arday-attributed windows

- **18:06–19:27:** The presenter introduces Dr Jason Arday as a Durham sociology assistant professor and asks what should be done if racism is institutional, systemic, and structural. Arday answers that responsibility should not be assigned only to people of colour and advocates collective responsibility and evaluation/change of major institutions.
- **19:20–21:43:** Asked about the school curriculum, Arday argues that the issue is not only what a curriculum formally lists but how teachers implement it and position Black people and their contributions. He says Black and ethnic-minority students do not necessarily see themselves reflected and that Black history is often framed around slavery rather than broader positive contributions to British history.
- **22:15–23:23:** Discussing Shakespeare and curriculum breadth, Arday says education should prepare people to take their place in society and provide a toolkit for engaging with people from different backgrounds. He argues that canonical, Black, and Indigenous histories should all be represented.
- **23:32–25:27:** On the removal of Edward Colston’s statue and “hard work,” Arday treats the statue as symbolically significant but warns against a seasonal focus that displaces the wider, sustained work of dismantling institutional racism. He frames racism as a collective problem and calls for long-term engagement, including recognition and use of white privilege.

## Evidence boundary

These are dated public positions and an attributed account of the programme’s exchange. The ASR text and time boundaries require human listening before quotation; no empirical conclusion, curriculum outcome, or claim about the programme’s other contributors is inferred. The broadcast does not independently verify Arday’s biography, credentials, or the social claims discussed.

## Reproduction

- Audio: [canonical MP3](../assets/audio/bbc-moral-maze-racial-justice.mp3), SHA-256 recorded in `SRC-060`.
- Navigation derivative: [Whisper JSON](../assets/documents/bbc-moral-maze-racial-justice/bbc-moral-maze-racial-justice-whisper-small-en.json), SHA-256 `afb2c9844bdef40dffee6205c3a1442ccbd24a7ad1c7ba159cefb2b7fa47226e`.
- Model: `mlx-community/whisper-small.en-mlx`; corrected-mono 16 kHz windows at source offsets 0–600, 600–1200, 1200–1800, 1800–2400, and 2400–2580 seconds.
