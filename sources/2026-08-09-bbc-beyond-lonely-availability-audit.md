---
id: SRC-1150
type: Source
title: "BBC Beyond Lonely availability recheck"
date: 2026-08-09
accessed: 2026-08-09
status: verified current metadata / unchanged playable JSON / media selector unavailable
entities:
  - ../entities/jason-arday.md
updates: ../claims-ledger.md, ../NEXT.md, ../research-log.md
urls:
  - https://www.bbc.co.uk/programmes/m0029zbb
  - https://www.bbc.co.uk/programmes/m0029zbb.json
  - https://rms.api.bbc.co.uk/v2/programmes/playable?container=m002b0hc&sort=sequential&type=episode&experience=domestic
  - https://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/audio-dash/proto/https/vpid/m0029zb9
---

# BBC Radio 4 *Beyond Lonely* — availability recheck

The current BBC programme page for “Young and Lonely in the Connected World” (`m0029zbb`) returned HTTP 200 on 9 August 2026. Its JSON identifies the canonical original version as `m0029zb9`, with an 840-second duration. The current playable-episode API response was byte-identical to the locally preserved 6 August response (`sha256 c259335eb65f9b44935475268c86603ceaf4ea96377d90475543a3f4b09c2307`).

The page/API metadata continues to say that, as a teenager, Arday spent hours practising snooker shots, valued the focus and solitude of the snooker hall, and later connected this experience to loneliness. This remains BBC synopsis wording about Arday’s autobiographical account, not a transcript or independent sporting record.

The BBC media-selector request for the episode’s canonical version (`m0029zb9`) returned HTTP 410 on 9 August 2026. No lawful public audio file, caption track, or transcript was recovered. The existing local HTML, API JSON, artwork, and contemporary listings remain the preservation set; no duplicate media node or new biographical claim was created.

## Evidence boundary

- `C-1427` records the current availability/version state only.
- The snooker and loneliness details remain under the canonical *Beyond Lonely* record (`SRC-063` / `C-077`).
- Reopen only for a changed BBC media selector, a lawful local recording, a first-party transcript/caption file, or a distinct episode artifact.
