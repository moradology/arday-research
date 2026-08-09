---
id: SRC-1026
type: primary audio audit
title: "Student Sessions — targeted audio audit of Jason Arday interview"
subject: ../entities/jason-arday.md
published: 2023-12-15
accessed: 2026-08-09
status: targeted machine-assisted audit of canonical MP3; not a human-verified transcript
evidence_class: first-person podcast audio / ASR derivative / deduplicated to SRC-156
urls:
  - https://www.buzzsprout.com/997477/episodes/14074459-overcoming-barriers-and-self-celebration-jason-arday
---

# Targeted audio audit

The preserved 42:04.46 *Student Sessions* MP3 was sampled with `mlx-community/whisper-small.en-mlx` on 9 August 2026. The audit targeted the biographical opening, the Sandro Sandri discussion, and the later literacy/academic-progression passages; it does not claim a complete transcript.

## First-person passages recovered

- **01:12–02:09:** Arday describes being diagnosed with autism spectrum disorder and global developmental delay, and describes delayed literacy and his route from college into Glasgow and Cambridge. The ASR renders one sentence as saying he learned to “read” at 11, which conflicts with the surrounding public source family’s speech-at-11 formulation; this ambiguity is preserved, not resolved or promoted as a new claim.
- **05:38–07:54:** He attributes a major part of his literacy development to college tutor Sandro Sandri, describing hours of phonics and reading-and-writing exercises and saying he would not have gone on to do what he did without meeting Sandri. This is first-person attribution, not an independently checked tutoring or college record.
- **11:21–11:33:** He says that at age 21 his reading age was that of an 11-year-old.
- **12:25–12:37:** He recalls Sandri framing it as remarkable that someone who learned to read and write at 18 could obtain a PhD within 12 years. This is a remembered quotation/biographical framing and remains subject to the same source-version and self-report caveats.

## Evidence boundary

The audit verifies that the sampled audio contains these passages and supplies approximate timecodes. ASR is a navigation and wording aid, not a verbatim transcript; the ambiguous 01:34 passage should not be quoted without human listening. The original page and MP3 remain the canonical interview under `SRC-156`; this is a derivative audit, not a second interview or independent corroboration.

## Reproduction

Audio: [canonical MP3](../assets/audio/student-sessions-jason-arday-2023-12-15.mp3), SHA-256 `69354937c70aa066afd46245780b6276f8d9c406daa32715203a2de393181a0b`. Model: `mlx-community/whisper-small.en-mlx`; targeted 300-second windows across the 42:04.46 file. `mlx_whisper` returned absolute segment times for file-path clipping; the initial draft incorrectly added each window start a second time, and the ranges above are corrected.
