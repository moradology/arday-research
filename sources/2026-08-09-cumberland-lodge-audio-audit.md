---
id: SRC-1045
type: primary event audio audit / machine-assisted timecode navigation
title: "Beyond Tokenism" Cumberland Lodge audio audit
subject: ../entities/jason-arday.md
event_date: 2021-11-03
published: 2021-11-03
accessed: 2026-08-09
status: locally preserved public MP3; targeted ASR navigation completed; human listening pending
evidence_class: first-party event audio / machine transcript derivative / first-person panel remarks
urls:
  - https://www.cumberlandlodge.ac.uk/resource/dialogue-debate-beyond-tokenism/
  - https://soundcloud.com/dialogue-and-debate/beyond-tokenism-with-dr-jason-arday-dr-dayo-eseonu-tamanna-miah-rachael-wilson
assets:
  - ../assets/audio/cumberland-lodge/beyond-tokenism-jason-arday.mp3
related_sources:
  - SRC-618
  - SRC-1008
---

# Cumberland Lodge — targeted audio audit

This is a navigation audit of the 59:10.38 SoundCloud MP3 already preserved under `SRC-618`. It is a four-person panel, not a solo interview. The host introduces Jason Arday as an Associate Professor in Durham’s Department of Sociology at approximately 00:00–02:00. The audit uses `mlx-community/whisper-small.en-mlx` on short extracted WAV windows; the text below is not a verbatim transcript and has not been manually checked against the recording.

## Arday-attributed window

- **Approx. 05:00–07:00** — The ASR output contains a transition from an earlier panelist into Arday’s response, followed by the host’s “Thanks, Jason” hand-off to the next panelist. In the response, Arday discusses tokenism as something that must be understood structurally, including through “whiteness,” while retaining the personal/subjective dimension of experience. He says, in substance, that he would not describe himself as having personally experienced tokenism, but that he has seen examples and does not think people of colour—particularly women of colour—benefit from it in the same way.

This is useful as a source-layer record of Arday’s public position and self-description in a dated panel. It does not independently establish the truth of the structural analysis, identify every speaker in the overlapping audio, or replace the host-written retrospective already recorded as `SRC-1008`.

## Method and limits

- Input: `assets/audio/cumberland-lodge/beyond-tokenism-jason-arday.mp3`, SHA-256 `8e4e2577fd7bcdf0d66639eccff168b25249f6d602bfbe6963d11050a92bd664`.
- Navigation pass: 5-minute windows, mono 16 kHz WAV extraction, `mlx-whisper` small English model; selected passage bounded by approximate offsets because this pass did not retain word-level timestamps.
- Speaker attribution is supported by the event’s host introduction and the immediate host hand-off, but remains a panel-audio attribution rather than a manually verified transcript.
- Reopen for human listening, a lawful caption/transcript track, or a materially different recording. Do not quote the ASR wording as exact speech.
