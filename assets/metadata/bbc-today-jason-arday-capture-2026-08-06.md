# BBC Radio 4 *Today* guest-editor capture — 2026-08-06

Source record: [SRC-130](../../sources/2023-12-30-bbc-today-guest-editor.md)

## Endpoints

- BBC programme page: <https://www.bbc.co.uk/programmes/m001ts2s>
- BBC programme JSON: <https://www.bbc.co.uk/programmes/m001ts2s.json>
- Episode image endpoint: <https://ichef.bbci.co.uk/images/ic/1200x675/p0h14fvk.jpg>
- BBC Sounds URL tested: <https://www.bbc.co.uk/sounds/play/m001ts2s>
- BBC.com audio URL tested: <https://www.bbc.com/audio/play/m001ts2s>
- Legacy media-selector URL tested: <https://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/audio-primary-passthrough/proto/https/vpid/m001ts2s>

The BBC programme page and JSON were retrieved directly on 2026-08-06. The JSON exposes canonical version PID `m001ts2q` and nominal duration 7,200 seconds. The HTML and JSON were inspected for media-selector/download URLs, audio file references, and transcript material, but no current playable audio or transcript endpoint was exposed. BBC Sounds and BBC.com returned 404; the tested legacy selector returned 410.

## Locally preserved files

| File | Description | Technical metadata | SHA-256 |
|---|---|---|---|
| `assets/documents/bbc-today-jason-arday-page-2026-08-06.html` | BBC programme-page snapshot | 149,053 bytes | `6d02f1715564e49d653244e0dbe5d0ef2ae6557af79d5ac1d8c8d529920628f7` |
| `assets/images/bbc-today-jason-arday.jpg` | Official episode image | 1200×675 JPEG; 144,659 bytes | `c7b4f8e773d98ebbb9ddaace319bd33642f1f5c4020f56f8af162032586d0f36` |
| `assets/documents/bbc-today-jason-arday-programme-2026-08-06.json` | BBC programme API response | 2,185 bytes | `e4998a8bbfaf8f875db1c0820e453541253dfa0497e2ce8fad6c357d459a4851` |
| `assets/documents/bbc-today-jason-arday-sounds-404-2026-08-06.html` | BBC Sounds 404 body | 135,104 bytes | `7830583bacbd0471b7a9c82c38c7361d078366f27a4b5ed43b4cfa11bac4f852` |
| `assets/documents/bbc-today-jason-arday-mediaselector-410-2026-08-06.html` | Legacy media-selector 410 body | 152 bytes | `ffe7a0f1f23ee4478db605fc9201d3b51d0a24c497a66376e72a38cf2f459d08` |
| `assets/documents/bbc-today-jason-arday-bbccom-404-2026-08-06.html` | BBC.com audio 404 body | 247,362 bytes | `9844f87a9f93411e7b5a00566ddbf42a54576754fabe666f3aa0d76be63d3016` |

## Evidence boundary

The page confirms the programme listing and guest-editor role and preserves the BBC’s biographical description as attributed institutional copy. It does not provide a current audio binary or transcript in this capture.
