# SEB “Things Can Only Get Better” capture — 2026-08-06

Source record: [SRC-109](../../sources/2026-seb-things-can-only-get-better.md)

## Canonical endpoints

- SEB resource page: <https://www.sebiology.org/resource/the-decolonising-and-diversifying-biosciences-education-recordings-are-available-on-demand.html>
- YouTube recording linked by SEB: <https://www.youtube.com/watch?v=H30IeW5J69I>
- Issuu programme link embedded by SEB: <https://issuu.com/societyforexperimentalbiology/docs/oed22-programme-final>
- Class Central index: <https://www.classcentral.com/course/youtube-jason-arday-things-can-only-get-better-182693>

## Locally preserved files

| File | Retrieval result | SHA-256 |
|---|---|---|
| `assets/documents/seb-decolonising-biosciences-page-2026-08-06.html` | SEB HTML snapshot, 58,595 bytes | `2b163ae240a989610a6a4ccdf1ef0457b20cd2baf370de9ce6c488297c9de75f` |
| `assets/images/seb-things-can-only-get-better-youtube.jpg` | Official YouTube thumbnail, JPEG 1280×720, 39,094 bytes | `0decb4fe27835c3285ef0fa94a6cd983921c462e74b1d458a9533b6276263b9c` |
| `assets/images/seb-oed-symposium.jpg` | SEB page image, JPEG 400×265, 12,272 bytes | `ccef05e450e7272009e7ac9ca2f46bb07ee45b97c7a455bd84f55629e57b1710` |
| `assets/documents/seb-oed22-programme-issuu-403-2026-08-06.html` | Issuu response body, 43 bytes, HTTP 403 | `9882cea81cd0d6edbd3a6a3c9bceafe2a507b631ebfb1fed3518a4cc0961ded8` |
| `assets/documents/seb-oed22-programme-issuu-headers-2026-08-06.txt` | Issuu response headers, 317 bytes | `b1867be1f773f9fcccc265dc4617cdb6b93e6f8d3faf3cb42ef31b63b6f4193e` |

## Availability boundary

The SEB page was retrieved with `curl` on 2026-08-06 and contains the exact YouTube ID and full talk title. `yt-dlp 2026.07.04` returned `This video is not available` for the linked recording. The thumbnail endpoint remained available. The Issuu programme request returned HTTP 403 and is preserved above; no video binary, captions, transcript, or programme file was retained.
