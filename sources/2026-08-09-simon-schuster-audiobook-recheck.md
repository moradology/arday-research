---
id: SRC-929
---

# Simon & Schuster audiobook page — `.net` source-version recovery

- Source ID: SRC-929
- Type: first-party publisher source-version / audiobook edition metadata / image recovery
- Accessed: 2026-08-09
- Status: current `.net` locale returned HTTP 200 after the exact `.com` route returned HTTP 403; current page says 8 hours 41 minutes, while the earlier `.net` manifestation said 9 hours 30 minutes; no audio binary or sample recovered
- Canonical edition record: [Great and Unfortunate Things audiobook](2026-08-11-great-and-unfortunate-things-audiobook.md)
- URL tested: <https://www.simonandschuster.net/books/Great-and-Unfortunate-Things/Jason-Arday/9781668126523>

## Changed manifestation

The exact `.com` audiobook URL returned HTTP 403. The `.net` URL returned a full HTTP-200 publisher page. Its title is “Great and Unfortunate Things Audiobook by Jason Arday,” and its structured metadata identifies ISBN `9781668126523`, “Audio Download,” Simon & Schuster Audio, a listed price of $26.99, and an 11 August 2026 release date. The current page visibly identifies Jason Arday as both author and reader and lists a runtime of 8 hours 41 minutes.

An earlier `.net` capture in this same source family listed 9 hours 30 minutes. Both values are retained as publisher source versions; the archive does not infer whether the difference reflects an edit, regional/mastering difference, or metadata correction. The current page exposes a “Resources and Downloads” section but no public playable audio URL, sample, transcript, or downloadable audiobook file.

The page repeats publisher synopsis and author biography copy, including the nonverbal/illiteracy narrative and present-tense Cambridge superlative. Those statements remain publisher/memoir marketing copy, not independent corroboration. The page exposes no playable audio URL, sample, transcript, or downloadable audiobook file.

The 3,000×3,000 audiobook cover is byte-identical to the existing audiobook-cover asset and is deduplicated. The page also exposes a distinct 212×250 author-photo manifestation; its embedded EXIF description says “Jason Arday poses for a portrait in the Cambridge Faculty of Education library.” The image is a publisher asset, not independent confirmation of the location or date.

## Access boundary and metadata anomaly

The `.net` page’s HTML canonical link incorrectly points to the `.com` hardcover URL while its JSON-LD and visible metadata identify the audiobook ISBN. This is preserved as a page-topology/version detail, not silently normalized. The `.com` 403 capture and `.net` 200 capture are both retained.

## Preserved artifacts

- [`.net` page HTML](../assets/captures/2026-08-09-simon-schuster-audiobook/simonandschuster_net.html)
- [Extracted text](../assets/captures/2026-08-09-simon-schuster-audiobook/simonandschuster_net.txt)
- [`.net` response headers](../assets/captures/2026-08-09-simon-schuster-audiobook/simonandschuster_net.headers.txt)
- [Exact `.com` audiobook 403 body and headers](../assets/captures/2026-08-09-simon-schuster-audiobook/page.html)
- [Alternate locale bodies and headers](../assets/captures/2026-08-09-simon-schuster-audiobook/)
- [Distinct author-photo manifestation](../assets/captures/2026-08-09-simon-schuster-audiobook/author-photo.jpg)
- [Duplicate audiobook cover](../assets/captures/2026-08-09-simon-schuster-audiobook/cover.jpg)
- [SHA-256 manifest](../assets/captures/2026-08-09-simon-schuster-audiobook/SHA256SUMS)

## Current source-version capture (2026-08-09)

- [Current `.net` HTML](../assets/captures/2026-08-09-simon-schuster-audiobook-current/net.html) — HTTP 200; SHA-256 `60b6369e102570383c0f62afc2704217e35344f68f2883868670c4cdbe134eae`
- [Current `.net` response headers](../assets/captures/2026-08-09-simon-schuster-audiobook-current/net.headers.txt) — SHA-256 `b97878cadee91efc4d7808c03260f7769bc928aba27690941ec4e49353390982`
- [Current exact `.com` body](../assets/captures/2026-08-09-simon-schuster-audiobook-current/page.html) — HTTP 403; SHA-256 `6da7e42ae62f228f1c053cf9614d3ef171c14cb5c13af0b77af1bfdec6e45bc9`
- [Current exact `.com` response headers](../assets/captures/2026-08-09-simon-schuster-audiobook-current/page.headers.txt) — SHA-256 `1ebec715d686caf7c74374a6f65530f7b47fc5c1017e77459bd0012238112fd2`

Reopen only for a public audio sample, downloadable audiobook, transcript, materially changed edition metadata, or a changed publisher route. Do not repeat the same locale requests unchanged.
