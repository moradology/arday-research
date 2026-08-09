---
id: SRC-1024
type: primary audio audit
title: "New Humanist With Reason — targeted audio audit of childhood and adolescence passages"
subject: ../entities/jason-arday.md
published: 2020-12-15
accessed: 2026-08-09
status: reproducible machine-assisted audit of canonical MP3; not a human-verified transcript
evidence_class: first-person audio / ASR derivative / deduplicated to SRC-223
urls:
  - https://newhumanist.org.uk/articles/looking-back-in-anger-at-cool-britannia-w-jason-arday/
  - https://www.buzzsprout.com/1480300/episodes/6800083-looking-back-in-anger-at-cool-britannia-with-jason-arday.mp3
---

# Targeted audio audit

The preserved 2,316.54-second MP3 for the 15 December 2020 *With Reason* interview was re-transcribed with `mlx-community/whisper-small.en-mlx` on 9 August 2026. The audit targeted the host’s childhood/adolescence discussion and compared the machine output with the host-published transcript.

## Reproducible passages

- **05:05–06:15:** Arday says he was born in Clapham, grew up on a council estate in relative poverty, had a good childhood because of his parents, identifies autism/Asperger’s and global developmental delay, and says he did not learn to speak until 11 or read and write until 18. He says his mother used music, and his guitar playing, to help him understand the world and move out of signing with help from speech therapists.
- **06:56–07:55:** He says much of his childhood was spent on picket lines and protests with his mother and that music and socialist movements helped him understand class and social mobility.
- **08:25–09:20:** He says his father warned him and his brothers at 11 that they might be stopped by police; he says the first stop occurred three years later.
- **14:03–15:27:** Asked about the experience, he describes being stopped at 14 while with two white people, says the experience at 15 felt like a possible lifelong pattern, and says he had been stopped by police every year since 14, sometimes three, four, or five times in a year. The transcript’s “345 times a year” rendering is not supported by the audio audit; the audible wording is “three, four, five times in a year.”

## Interpretation boundary

The audit confirms that these statements are present in the preserved audio and broadly match the published transcript. It does not verify the underlying childhood, clinical, family, socioeconomic, or police records. The model output is a navigation and wording aid, not a verbatim transcript; names, diagnoses, and exact phrasing should remain attributed to Arday’s interview account.

## Reproduction

Audio: [canonical MP3](../assets/audio/new-humanist/with-reason-cool-britannia-jason-arday.mp3), SHA-256 `f5f33caf7f839c7beee3db431c2526692059faf6fa4b7ec10f28e3b4e40e1528`. Model: `mlx-community/whisper-small.en-mlx`; targeted `clip_timestamps` windows `180,420`, `420,560`, `560,720`, `720,880`, and `876,930` seconds. This record is a derivative of `SRC-223`, not a second interview.
