---
id: SRC-1152
type: primary audio audit
title: "BBC Radio 4 A Good Read — Jason Arday audio audit"
subject: ../entities/jason-arday.md
published: 2023-11-21
accessed: 2026-08-09
status: bounded machine-assisted audit of canonical MP3; not human-verified transcript
evidence_class: first-party broadcast audio / self-description and literary-judgment source-version / ASR navigation
related_sources:
  - SRC-061
claims:
  - C-1433
  - C-1434
  - C-1435
assets:
  - ../assets/audio/bbc-good-read-janet-ellis-jason-arday.mp3
  - ../assets/documents/bbc-good-read-jason-arday/bbc-good-read-jason-arday-whisper-small-en.json
urls:
  - https://www.bbc.co.uk/programmes/m001sm8n
---

# BBC Radio 4 *A Good Read* — bounded audio audit

The preserved 28:05 BBC episode was converted to corrected mono WAV and transcribed in three windows with `mlx-community/whisper-small.en-mlx`. The audit separates Arday’s guest remarks from Janet Ellis’s and Harriett Gilbert’s discussion. It targets Arday’s own book preferences and literary analysis rather than treating book discussion as independent biography.

## Arday-attributed windows

- **09:43–12:28:** Introducing Siya Kolisi’s *Rise*, Arday says he generally gravitates toward biographical books about people who do phenomenal things. He presents Kolisi’s story through leadership, unity, faith, sport, and South Africa’s history, and describes the captaincy of a Black South African man as a powerful symbol of change.
- **23:16–24:54:** Discussing Colin McCann’s *Let the Great World Spin*, Arday identifies a tension in a white male author writing from the perspectives of Black women. He emphasizes the uniqueness of Black women’s lived experience, notes that some descriptions may not chime with a Black woman reader’s experience, and still recognizes an empathetic attempt to situate that experience.

## Evidence boundary

These windows preserve Arday’s public self-description, reading preference, and literary judgment. They do not independently establish his biography, the truth of the books’ contents, or a general theory of representation. The ASR and speaker boundaries require human listening before quotation.

## Reproduction

- Audio: [canonical MP3](../assets/audio/bbc-good-read-janet-ellis-jason-arday.mp3), SHA-256 recorded in `assets/metadata/bbc-good-read-capture-2026-08-06.md`.
- Navigation derivative: [Whisper JSON](../assets/documents/bbc-good-read-jason-arday/bbc-good-read-jason-arday-whisper-small-en.json), SHA-256 `43eb8db611fb59c8cf3aa3990b96b260f090dd4a47d0a38d63017b9b2796eed3`.
- Model: `mlx-community/whisper-small.en-mlx`; corrected-mono 16 kHz windows at source offsets 0–600, 600–1200, and 1200–1690 seconds.
