---
id: SRC-1145
type: source-version / access-state recheck
title: "Ruling Passions Episode 2 — current WordPress transcript recheck"
subject: ../entities/jason-arday.md
published: 22 March 2022
accessed: 2026-08-09
status: current WordPress page HTTP 200; byte-distinct HTML but text-identical transcript; full audio remains unresolved
evidence_class: first-party project page / transcript source-version / access-state capture
urls:
  - https://rulingpassions.wordpress.com/2022/03/22/podcast-launch-episode-2/
related:
  - SRC-158
---

# Current page recheck

The canonical WordPress episode page returned HTTP 200 on 9 August 2026. Its raw HTML is byte-distinct from the earlier local capture, but Pandoc-normalized page text is byte-identical, including the episode description, speaker labels, timestamps, and transcript. No new transcript passage, correction, image, or full-audio URL was exposed.

The migrated `rulingpassions.com` route did not return a response within the bounded direct-fetch window. This is an incomplete access attempt, not evidence that the project page or recording has been removed. The full interview remains represented by the public transcript and 60-second Spotify preview under canonical `SRC-158`; no duplicate interview or claim was created.

## Preservation

- [Current HTML](../assets/captures/2026-08-09-ruling-passions-recheck/episode.html) — SHA-256 `14f232c202975376fa8795261bd5892268f114c1af80f88fda461a98a639c80b`
- [Response headers](../assets/captures/2026-08-09-ruling-passions-recheck/episode.headers.txt) — SHA-256 `d4a6bf4c0cf3f9b7eb0b466f7d28564a237b1b6851cbf1958ebc8abdbd34c05b`
- [Normalized transcript text](../assets/captures/2026-08-09-ruling-passions-recheck/episode.txt) — SHA-256 `18e34cdabb21842892d6886bc01daec4ee8223f417f3186c4f13e329fd59a0dc`
