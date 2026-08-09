---
id: SRC-930
type: Source
title: "Great and Unfortunate Things — Google Books UK edition record recheck"
date: 2026-08-09
accessed: 2026-08-09
status: verified catalog record; HTML, text extraction, cover, and HTTP headers locally preserved; no readable preview recovered
source_kind: Google Books bibliographic record / publisher synopsis / edition topology
entities:
  - ../entities/jason-arday.md
urls:
  - https://books.google.com/books/about/Great_and_Unfortunate_Things.html?id=HWfF0QEACAAJ
---
# Google Books UK edition record recheck

Google Books exposes a distinct Simon & Schuster Limited record for *Great and Unfortunate Things* under volume ID `HWfF0QEACAAJ`, ISBN 9781398542747 / ISBN-10 1398542741. The page gives 27 August 2026, 336 pages, and the subjects “Biography & Autobiography / Memoirs,” autism-spectrum-disorders-related psychology, and self-help/personal growth. It also exposes a Google Books cover image.

The page’s synopsis repeats the memoir/publisher narrative that Arday grew up in a south-London council house with his parents and two brothers, was diagnosed with autism and global developmental delay at three, spoke his first word at eleven, and learned to read and write at eighteen. It also includes the opening exchange: “You did it, didn’t you, Jason?” / “No, Giff,” I told her. “We did. We did it . . .” These are catalog copy describing a self-authored memoir, not independent corroboration; the family-count wording is retained as a witness alongside other published variants.

The page says “No eBook available” and its embedded volume state reports `has_flowing_text:false`, `has_scanned_text:false`, `is_browsable:false`, and no PDF/EPUB download. The Google Books API was separately tested for this ID and for the previously captured 368-page UK volume `84edEQAAQBAJ`; both requests returned HTTP 429 quota exhaustion. The API responses and headers are preserved as access-boundary artifacts.

The page’s “Other editions” block links the 368-page UK record (`84edEQAAQBAJ`), a 288-page US/Simon & Schuster record (`aNz0EQAAQBAJ`, ISBN 9781668085578), and other no-preview manifestations. This record therefore expands the edition topology but does not establish that the differing page counts represent differing memoir content.

## Evidence boundary

This source establishes a distinct bibliographic manifestation, its catalog metadata, publisher synopsis, cover, and the absence of a readable Google Books preview in the captured response. It does not establish the underlying life-history claims as independent fact and does not provide the memoir’s page text.

## Local preservation

- [Google Books HTML snapshot](../assets/captures/2026-08-09-google-books-memoir-recheck/HWfF0QEACAAJ.html)
- [Plain-text extraction](../assets/captures/2026-08-09-google-books-memoir-recheck/HWfF0QEACAAJ.txt)
- [Google Books cover response](../assets/captures/2026-08-09-google-books-memoir-recheck/HWfF0QEACAAJ.cover.jpg) — 300×391 PNG returned with `.jpg` URL; SHA-256 `12557f8948b8bdc6af436e3a8b3adddd45f7f7d2b67c5832e799cdf4686f72bb`
- [HTTP headers and API responses](../assets/captures/2026-08-09-google-books-memoir-recheck/)
- [Capture checksums](../assets/captures/2026-08-09-google-books-memoir-recheck/SHA256SUMS)
