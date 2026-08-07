---
id: SRC-459
---

# Cambridge Faculty of Education “Our People” — changed pagination recheck

- Source ID: SRC-459
- Type: first-party institutional directory source-version / bounded pagination sweep
- Accessed: 2026-08-08
- Status: verified direct-response change; directory sweep did not render an Arday entry
- Related records: [SRC-283](2026-08-06-cambridge-our-people-directory-boundary.md), [SRC-208](2026-08-06-cambridge-profile-post-resignation-404.md)

## Record

The live Cambridge Faculty of Education “Our People” endpoint returned a changed HTTP 200 response on 8 August 2026. The page-1 body was 72,739 bytes at the response level (71,972 bytes after decompression) and began with a different set of staff entries from the 6–7 August captures. It still did not contain `Jason Arday`, `jaa80`, or “Professor of Sociology of Education.”

A bounded sweep of the same endpoint’s `page=0` through `page=40` states found no `Jason Arday` or `jaa80` occurrence in any returned body. The generic role title does appear on page 5, but it belongs to Jo-Anne Dillabough, not Arday. This documents a changed directory/pagination state and a defined negative-space search; it does not establish that Arday is no longer employed by Cambridge, that he resigned from the Faculty, or that the search covers every dynamically loaded record. Search-engine snippets remain a separate indexed/live mismatch.

## Local preservation

- [Changed page-1 HTML capture](../assets/captures/2026-08-08-cambridge-our-people-recheck/page.html) — SHA-256 `a4ae611d7d62843829cfaeb5e82921ed557f745a34ba0f8bd15759cd06d9a73f`.
- [Changed page-1 response headers](../assets/captures/2026-08-08-cambridge-our-people-recheck/page.headers.txt) — SHA-256 `914bd671c17815b42a65bbddb4b611cf39aa03e487ccf3e1162791c6fb8df018`.
- [Pages 0–40 pagination sweep](../assets/captures/2026-08-08-cambridge-our-people-pagination/) — 41 HTML responses and [SHA-256 manifest](../assets/captures/2026-08-08-cambridge-our-people-pagination/SHA256SUMS); no response body matched `Jason Arday` or `jaa80`; page 5’s generic professorial title is attached to Jo-Anne Dillabough.
- [Current directory endpoint](https://faculty.educ.cam.ac.uk/about-us/our-people?page=1)
