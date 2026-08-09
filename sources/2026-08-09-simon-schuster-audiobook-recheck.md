---
id: SRC-929
---

# Simon & Schuster audiobook page — `.net` source-version recovery

- Source ID: SRC-929
- Type: first-party publisher source-version / audiobook edition metadata / image recovery
- Accessed: 2026-08-09
- Status: `.net` locale returned HTTP 200 after `.com`, `.co.uk`, and `.biz` routes were challenged or redirected; no audio binary or sample recovered
- Canonical edition record: [Great and Unfortunate Things audiobook](2026-08-11-great-and-unfortunate-things-audiobook.md)
- URL tested: <https://www.simonandschuster.net/books/Great-and-Unfortunate-Things/Jason-Arday/9781668126523>

## Changed manifestation

The exact `.com` audiobook URL returned HTTP 403, as did the `.co.uk` and `.biz` variants. The `.net` URL first returned a redirect and then a full HTTP-200 publisher page. Its title is “Great and Unfortunate Things Audiobook by Jason Arday,” and its structured metadata identifies ISBN `9781668126523`, “Audio Download,” Simon & Schuster Audio, a listed price of $26.99, and an 11 August 2026 release date. The page visibly identifies Jason Arday as both author and reader and lists a runtime of 9 hours 30 minutes.

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

Reopen only for a public audio sample, downloadable audiobook, transcript, materially changed edition metadata, or a changed publisher route. Do not repeat the same locale requests unchanged.
