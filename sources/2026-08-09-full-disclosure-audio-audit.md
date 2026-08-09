---
id: SRC-1148
type: primary audio audit
title: "Full Disclosure — Jason Arday opening biography and education-policy audit"
subject: ../entities/jason-arday.md
published: 2023-04-20
accessed: 2026-08-09
status: bounded machine-assisted audit of canonical MP3; guest passages separated from host introduction; not a human-verified transcript
evidence_class: Global Player podcast audio / first-person biography and public-position source-version / ASR derivative
urls:
  - https://www.globalplayer.com/podcasts/episodes/7DrfQkN/
related:
  - SRC-034
---

# Bounded opening audit

The locally preserved 1:09:48 MP3 was sampled after the advertisement and opening material. A corrected-mono `small.en` pass covers source offsets 180–420 seconds. The host’s introduction at approximately 338–359 seconds is excluded from guest claims; Arday’s responses begin around 184 seconds and resume after the host’s questions.

## Reproducible passages

- **03:04–05:32:** Arday describes Cambridge as a surreal environment, discusses meeting Simon Baron-Cohen, and says he has been fortunate to work with exceptional people. These are first-person professional recollections, not appointment or correspondence records.
- **05:08–05:32:** He describes his work as focused on the democratization of education and redistribution of higher-education resources toward ethnic-minority and socioeconomically disadvantaged groups. This is an attributed account of his professional mission, not evidence of implementation or effect.
- **06:04–06:59:** Responding to the host’s question, he distinguishes autism-spectrum disorder from global developmental delay, says the autism diagnosis occurred in 1988 and the developmental-delay diagnosis followed months later, and connects the latter with delayed speech and literacy. These are self-reported medical/developmental details; the host’s preceding biography is not independent corroboration.
- **06:44–07:00:** He frames the non-speaking period as a stillness that enabled distinctive observation of the world and human interaction. This is a first-person interpretation, not a clinical finding.

## Evidence boundary

The audit establishes approximate navigation to a dated public interview and separates guest speech from host framing. The JSON is automatic speech recognition; exact wording, dates, proper names, and speaker attribution require human listening against the MP3. The audit does not establish diagnoses, Cambridge status, professional outcomes, or the host’s “youngest” formulation independently.

## Preservation

- [Canonical MP3](../assets/audio/full-disclosure-jason-arday.mp3) — SHA-256 `dd2ef380b6f5a0b528ba0c144bebb4720f1df9327a4438343fc57930619107d9`
- [Whisper `small.en` JSON, source offset 180–420 seconds](../assets/documents/full-disclosure-jason-arday-2023-whisper-small-en.json) — SHA-256 `c7706a2797700a70b70d41debd8128d0ed81ede5a6e0fa00737bdc4703755c08`
