---
id: SRC-1020
type: machine-assisted primary-audio audit
title: "Talking Matters snooker passage — reproducible audio-window audit"
subject: ../entities/jason-arday.md
accessed: 2026-08-09
status: local audio window re-transcribed with larger model; not human-verified
evidence_class: primary audio plus reproducible machine transcript; navigation derivative
urls:
  - https://open.spotify.com/episode/3KJMtYC3cs1gjNOafCQLfj
  - https://podcasts.captivate.fm/media/a1f8c899-142e-4b30-a907-a67d376ddedb/Jason-01-08-24-Edit-128.mp3
updates:
  - sources/2024-08-02-talking-matters-jason-arday.md
assets:
  - ../assets/metadata/talking-matters-snooker-window-2026-08-09.txt
---

# *Talking Matters* snooker passage — audio-window audit

The preserved *Talking Matters with Nick Halkes* MP3 was re-transcribed for the 00:20:00–00:21:40 window containing the football/snooker exchange. A larger English Whisper model recovers the existing navigation lead with improved wording: Arday says he was closer to becoming a professional snooker player; describes practising from about age 11 to 18 or 19 for roughly seven hours a day; says he played professionals in Pro-Am; places the junior tournament at Pontins in Prestatyn, Wales; and compares his 50–60 breaks with younger players making an 87 break while standing on boxes.

The same passage contains his account of playing non-league football for roughly 12–13 years after not becoming a professional footballer. This is first-person testimony in a podcast recording, not an independent sports record. The transcription remains machine-assisted: proper nouns and phrases are not promoted as verbatim without human listening. The audit therefore strengthens reproducibility and narrows the wording, but does not establish a professional snooker career, a named tournament result, ranking, club registration, or the truth of the autobiographical account.

## Method

- Parent audio: [local MP3](../assets/audio/talking-matters-jason-arday-2024.mp3), SHA-256 `6cf4940cf121d118dda9661ed20de37943436723be2c6fffdfcec32c787faaad`.
- Audited interval: 00:20:00–00:21:40, converted to mono 16 kHz PCM for transcription; the temporary WAV is not part of the public archive.
- Model: `mlx-community/whisper-small.en-mlx`; output is preserved in [the transcript derivative](../assets/metadata/talking-matters-snooker-window-2026-08-09.txt).

## Boundary

This is a derivative audit of canonical source [SRC-184](2024-08-02-talking-matters-jason-arday.md), not a new interview or independent corroborating source. Reopen for human listening, a publisher transcript/caption file, a named Pontins result, or a governing-body record.
