---
id: SRC-1146
type: primary audio audit
title: "BBC Best of Today — Jason Arday contribution audio audit"
subject: ../entities/jason-arday.md
published: 2024-10-11
accessed: 2026-08-09
status: bounded machine-assisted audit; Arday window located, wording and speaker attribution require human verification
evidence_class: BBC-distributed podcast audio / public-position source-version / ASR derivative
urls:
  - https://podfollow.com/best-of-today/episode/5daf35e300a06e4fe3ff32de29dc231cb30c7caf/view
  - https://podcasts.apple.com/gb/podcast/best-of-today-what-should-children-learn/id73330187?i=1000672697102
related:
  - SRC-346
---

# Bounded Arday audio window

The locally preserved 2,509-second BBC MP3 was sampled to locate the named contributor. A 60-second window beginning at approximately **05:00** contains a coherent first-person contribution, following the programme’s opening material. The window was transcribed from corrected-mono 16 kHz audio with `mlx-community/whisper-small.en-mlx`.

## Navigation

- **05:00–05:40:** Arday appears to argue that communication, speaking, knowing when not to speak, and active/critical listening should be treated as a fundamental entitlement for every young person rather than a “nice to have.” The ASR renders the key term as “ORC” in several places; this is likely “oracy” from context but must be checked against the MP3 before quotation.
- **05:35–05:48:** He describes the proposed skill as a “fourth R” alongside reading, writing, and arithmetic, then connects a broader curriculum with preparing young people for life and work. This remains an attributed policy position, not evidence of implementation or educational outcome.

## Evidence boundary

The programme metadata establishes the episode and names Arday as a contributor; the bounded audio window supplies approximate navigation to a likely Arday segment. The JSON is an automatic speech-recognition derivative. It does not establish exact wording, speaker identity, the intended spelling of “oracy,” or the programme’s underlying policy evidence. No claim is made about the other contributors’ remarks.

## Preservation

- [Canonical BBC MP3](../assets/captures/2026-08-07-best-of-today-children-learn/audio.mp3) — SHA-256 `4088be05b5cdf0ed120a3b4f872422415fdb47ffd76d59ff8356a4d9153fe720`
- [Whisper `small.en` JSON, source offset 300–360 seconds](../assets/documents/bbc-best-of-today-children-learn-arday-whisper-small-en.json) — SHA-256 `5a320385cd674b250c8a99eb9200e8216866a0e57603947f955fffc5998a1293`
