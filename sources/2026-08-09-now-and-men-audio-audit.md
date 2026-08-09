---
id: SRC-1144
type: primary audio audit
title: "Now and Men — bounded Jason Arday audio audit"
subject: ../entities/jason-arday.md
published: 2022-01-26
accessed: 2026-08-09
status: reproducible machine-assisted audit of canonical MP3; not a human-verified transcript
evidence_class: first-party podcast audio / first-person testimony and public-position source-version / ASR derivative
urls:
  - https://nowandmen.net/episode/jason-arday
  - https://podcasts.captivate.fm/media/310b0de1-09c0-48e8-b232-9d97e814fe76/nam-jason-arday-final.mp3
---

# Bounded audio audit

The locally preserved 64:58 *Now and Men* episode was sampled on 9 August 2026 with `mlx-community/whisper-small.en-mlx`. The audit covers approximately 05:00–10:00, after the host introduction, and maps Arday-attributed discussion of racial-justice momentum, institutional change, measured radicalism, and a reported racist banana incident. It is navigation support, not a complete transcript.

## Reproducible windows

- **05:00–06:00:** Arday discusses the importance of practice alongside theory and the tension between colonial histories and contemporary institutional spaces. The machine output includes a likely reference to “Rhodes Must Fall”; human listening is required before using the name.
- **06:00–07:00:** He describes a perceived slowing of racial-justice momentum and locates that reflection in his own life experience, saying he is 36 at the time of recording. This is a dated self-description, not an independently verified birth-date record.
- **07:00–08:00:** He says diversification is visible in arts, education, sport, and media but questions whether institutions have removed underlying “toxic soil” rather than temporarily placing new initiatives on top of it. This is an attributed public position, not an outcome measure.
- **09:00–10:00:** He frames radicalism as carrying unequal consequences and describes a banana being sent to his workplace as a recent racist incident. The episode’s audio supports preserving this as first-person testimony; no sender, workplace record, or contemporaneous incident report is established here.

## Evidence boundary

The source establishes that these passages occur in a dated public interview and supports approximate navigation to them. The JSON files are automatic speech-recognition derivatives; wording, speaker boundaries, proper names, and exact timecodes require human listening against the MP3 before quotation. The audit does not independently verify the incident, institutional conditions, or the historical claims discussed.

## Reproduction

Audio: [canonical MP3](../assets/audio/now-and-men-jason-arday-2022-01-26.mp3), SHA-256 `70426b63fa40b92764aa7e081a1ff14ef52d9dd9203bf49018e067a017734996`. Model: `mlx-community/whisper-small.en-mlx`; 60-second corrected-mono windows sampled from source offsets 300–360, 360–420, 420–480, and 540–600 seconds.

- [300–360 JSON](../assets/documents/now-and-men-jason-arday-2022/window-300-360.json) — SHA-256 `3478bc45becb306e669c4b9ff155a6e62f9cacd0c5a1e5d771e389977f4070a3`
- [360–420 JSON](../assets/documents/now-and-men-jason-arday-2022/window-360-420.json) — SHA-256 `88da066ea326c8d6b457c6b5e368b7c18f7364bf5a1ec80f7a9115b9ab8ca9e7`
- [420–480 JSON](../assets/documents/now-and-men-jason-arday-2022/window-420-480.json) — SHA-256 `072bf0d6ca43ec44405ab56f6eee0cf77fea3955133089c9bd258ec594069571`
- [540–600 JSON](../assets/documents/now-and-men-jason-arday-2022/window-540-600.json) — SHA-256 `73b99e364239836e343125814c53c90a0668487a9719752dab3cf6628fc333ba`
