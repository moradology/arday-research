# *Full Disclosure with James O’Brien: Jason Arday* capture — 2026-08-06

Source record: [SRC-034](../../sources/2023-04-20-global-player-full-disclosure.md)

## Endpoints

- Global Player episode: <https://www.globalplayer.com/podcasts/episodes/7DrfQkN/>
- Global Player player API: <https://bff-web-guacamole.musicradio.com/playables/7DrfQkN/>
- Captivate MP3 exposed by the API: <https://dax.captivate.fm/d5fdd4fc-37f1-4bc8-87ed-fb7114dc3a71/Full-D-jason-arday-encoded.mp3?aw_0_1st.showid=95158cfb-f74f-4f9c-8f47-00bd976ab01d&aw_0_1st.episodeid=b25bda9e-4e3f-494e-8e60-10ecc5cfea14>
- Official artwork endpoint: <https://images.musicrad.io/resizer/?image=aHR0cHM6Ly9hcnR3b3JrLmNhcHRpdmF0ZS5mbS80ZTdkODcwOS0zOTg1LTQ4ZjUtOWE5ZC00ZWQ2YjJjZGZkY2EvSkJRd3ByRjlXaWxEQjR3Uy10LWlSdGxGLmpwZw%3D%3D&width=600&signature=JVdm3z5vLgYReS1Td2OZnixUPro=>

The page and player API were retrieved directly on 2026-08-06. The API’s playback object reported `hasAds: true`; the complete MP3 was downloaded after a long-running transfer and passed ffmpeg decoding without errors. The initially observed shorter transfer was not retained as a separate asset because it was byte-identical to the completed file after the transfer finished.

## Locally preserved files

| File | Description | Technical metadata | SHA-256 |
|---|---|---|---|
| `assets/audio/full-disclosure-jason-arday.mp3` | Captivate MP3 exposed by Global Player | 67,013,485 bytes; 128 kb/s, 44.1 kHz, stereo; file duration 1:09:48.34 | `dd2ef380b6f5a0b528ba0c144bebb4720f1df9327a4438343fc57930619107d9` |
| `assets/documents/full-disclosure-jason-arday-playable-api-2026-08-06.json` | Player API response | 801 bytes; API duration 1:07:18; `hasAds: true` | `255d8f140da2782037f44532bbc2eeb7f7534fcc5b205e1319f5399e2d2015f7` |
| `assets/documents/full-disclosure-jason-arday-page-2026-08-06.html` | Global Player page snapshot | 50,892 bytes; page display 1:07:00 | `da3e3eb8cb5d98a26c848c45b8ac6bfa21f01de3625c2a20afed4b6f298a6f34` |
| `assets/images/full-disclosure-jason-arday.jpg` | Official episode artwork | 600×600 JPEG; 38,640 bytes | `b0aa5100a80025c29135f6b2d33f2384d0b95cd0e7895df442bb4209a40c931f` |

## Evidence boundary

The audio is a preserved interview asset. The page description is host metadata and does not substitute for a transcript or independently verify the biographical details it summarizes.
