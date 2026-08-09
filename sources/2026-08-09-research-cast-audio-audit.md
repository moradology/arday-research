---
id: SRC-1027
type: primary audio audit
title: "Research Cast UK — targeted audio audit of Jason Arday interview"
subject: ../entities/jason-arday.md
published: 2025-01-06
accessed: 2026-08-09
status: reproducible machine-assisted audit of canonical MP3; no public transcript found
evidence_class: first-person institutional podcast audio / ASR derivative / deduplicated to SRC-198
urls:
  - https://www.lincolnbishop.ac.uk/podcast-social-justice
---

# Targeted audio audit

The preserved 44:47.54 Research Cast UK MP3 was re-audited with `mlx-community/whisper-small.en-mlx` on 9 August 2026. The higher-capacity pass confirms and sharpens the existing C-117–C-119 navigation windows without creating a second interview record.

## Recovered passages

- **05:30–07:10:** Arday tells the host—an early educator he addresses in the recording—that her teaching about education preparing people to take their place in society became a personal “tagline.” He also describes education as a toolkit for navigating a multicultural, multi-ethnic, diverse society.
- **26:50–27:45:** He says that his entire family works in the NHS and that they are mental-health nurses, while discussing pressure on NHS services. This remains a first-person family statement; no family employment records were sought or found in this audit.
- **27:48–29:50:** He describes sport as an outlet and emphasizes its capacity to create community and belonging, including a “come as you are” form of acceptance. This is reflective testimony, not evidence of a specific sporting career.

## Evidence boundary and correction

The audit confirms audio presence and improves wording navigation for the existing claims. It does not provide a public transcript, human-verified quotation, independent family employment record, or sports record. The prior audit attempts used file-path clipping inconsistently; this pass used streamed, explicitly offset audio windows, and the timecodes above are absolute file times. The MP3 and image remain canonical under `SRC-198`.

## Reproduction

Audio: [canonical MP3](../assets/audio/research-cast-uk-jason-arday-2025.mp3), SHA-256 `50d29c4bce45f85794d3e5d3ef63e1a2fdc3ecc6caed0e7b098e31559a4f56b5`. Model: `mlx-community/whisper-small.en-mlx`; streamed windows covering approximately 05:30–07:10, 26:50–27:45, and 27:48–29:50.
