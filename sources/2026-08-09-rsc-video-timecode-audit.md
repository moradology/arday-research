---
id: SRC-1035
type: audiovisual audit of existing institutional video
title: "Royal Society of Chemistry Inclusion and Diversity Forum 2025 — local timecode audit"
subject: ../entities/jason-arday.md
published: 2025-04
event_date: 2025-03-25
accessed: 2026-08-09
status: machine-assisted time map; human listening still pending
evidence_class: first-party event recording / local ASR navigation / bounded source audit
related_sources:
  - SRC-276
assets:
  - ../assets/videos/rsc-inclusion-diversity-forum-2025.mp4
---

# RSC Inclusion and Diversity Forum — timecode audit

The existing 13:23.92 RSC YouTube recording was extracted to mono 16 kHz audio and transcribed locally with `mlx-community/whisper-small.en-mlx`. The resulting map identifies a coherent opening segment from approximately **00:00–01:44** and a later interview/remarks segment from approximately **09:09–13:16** in the recording. The middle section is a montage of other speakers and attendees.

The speaker attribution is based on the RSC event record, the recording’s sequence, and the content’s continuity with the reported Arday presentation; the words below are machine-assisted navigation text, not human-verified quotations. No claim is made about pauses, exact wording, or every speaker transition until the MP4 is listened to manually.

## Navigation map

- **00:17–01:44 — opening remarks:** the ASR renders the speaker describing progress in equality, diversity and inclusion work, saying the work is not easy, and arguing that people can continue with those who agree even without universal agreement.
- **09:09–11:07 — evidence and intersectionality remarks:** the ASR renders discussion of intersectionality, the importance of granular data, and the difference between experiences across racial and disability positions. The exact start/end of individual answers remains approximate.
- **11:11–12:28 — research, evidence, and inclusion:** the ASR renders the speaker saying that “the data doesn’t lie,” that inclusion requires understanding exclusion and taking concrete measures through research, and that equality work is everyone’s responsibility.
- **12:28–13:16 — community of practice:** the ASR renders remarks that events provide focus, shared practice, networking, collaboration, and a way to strengthen responses to social challenges.

## Evidence boundary

This audit upgrades the existing recording from “not yet timecoded” to “machine-timecoded for navigation.” It does not establish a verbatim transcript, independently verify the presentation’s arguments, or prove that every mapped sentence belongs to Arday without manual audiovisual review. The RSC event report remains the first-party source for the event and presentation title; this derivative does not create a second event or recording node.

## Reproducibility

The audio was extracted from the canonical local MP4 with FFmpeg and transcribed using `mlx-community/whisper-small.en-mlx`, with absolute file offsets retained. The full recording remains at [the canonical MP4](../assets/videos/rsc-inclusion-diversity-forum-2025.mp4). Reopen this audit for manual listening, a first-party transcript, a non-empty caption track, or a materially different recording.
