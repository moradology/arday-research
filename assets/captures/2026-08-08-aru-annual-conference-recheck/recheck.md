# ARU Annual Conference player recheck

Date: 2026-08-08

URL: `https://myplayer.aru.ac.uk/player?autostart=n&videoId=312Fb8E6&captions=y&chapterId=0`

Result: a direct `curl` request using a browser user-agent and a 25-second timeout did not receive response headers or a player body; it terminated with `curl: (28) Connection timed out after 25003 milliseconds`. The zero-byte `player.headers.txt` is retained as the raw command output boundary. No media manifest, MP4, HLS stream, captions, or transcript was recovered.

This is a changed-date recheck of the existing `SRC-161` lead, not evidence that the recording has been deleted or never existed.
