---
id: SRC-208
type: institutional profile changed-state record
title: "Cambridge Faculty of Education Jason Arday profile — post-resignation 404 state"
subject: ../entities/jason-arday.md
published: 2026-08-06 live check
accessed: 2026-08-08
status: profile URL HTTP 404 after prior locally preserved profile version; official notice rechecked live; later 404 body state preserved
evidence_class: first-party host-page changed state / local HTML captures
updates:
  - sources/2026-08-06-cambridge-faculty-profile-current-capture.md
urls:
  - https://faculty.educ.cam.ac.uk/people/staff/arday
  - https://faculty.educ.cam.ac.uk/people/staff/arday/
  - https://www.cam.ac.uk/notices
  - https://www.cam.ac.uk/notices/news/statement-about-professor-arday
---

# Cambridge Faculty profile changed state

On 6 August 2026, both the no-slash and slash forms of the Cambridge Faculty of Education profile URL returned HTTP 404. The no-slash response and slash response are preserved separately because their generated HTML bodies differ slightly. This follows the 6 August profile snapshot in SRC-168, which still presented Arday as Professor of Education and listed several Cambridge-linked roles.

The live Cambridge notices index still listed “Statement about Professor Arday” dated 5 August 2026, and the statement URL itself returned HTTP 200 during the same capture. This supports a narrow changed-state observation: the Faculty profile is no longer available at the captured URLs while the institutional notice remains listed. It does not establish whether the profile was intentionally removed because of the resignation, temporarily moved, or replaced elsewhere.

## Evidence boundary

The 404 responses establish URL state, not the reason for removal and not the termination or continuation of every role formerly listed. The preserved SRC-168 page remains the authoritative record of the earlier public version; this record must not be used to infer facts about Cambridge’s investigation or its outcome.

## Local preservation

- [No-slash 404 response](../assets/documents/cambridge-faculty-arday-profile-404-2026-08-06.html) — SHA-256 `ec7e254cc1d942451e8ae2be2e1a6d5cc3588fef7eedfb5d0ad816c9a2f5c0df`
- [Slash 404 response](../assets/documents/cambridge-faculty-arday-profile-404-slash-2026-08-06.html) — SHA-256 `e26b8b6b0a0dc3becc629ae93045ebd513491979f6908ff727e12788b24dbd90`
- [Cambridge notices index](../assets/documents/cambridge-notices-index-2026-08-06.html) — SHA-256 `3d6f4207ad7c1539834282946b17f483e5740eab8a2e87f7ef83daaf6f2b7f3d`
- [Statement page live capture](../assets/documents/cambridge-statement-about-professor-arday-live-2026-08-06.html) — SHA-256 `4a5936c024e0aa1fc7b0382219c322418f5dd949a413a9a9155a373fb541c584`

## 2026-08-07 recheck

The official statement URL returned HTTP 200 again. Its substantive text remains unchanged: Cambridge says an investigation has begun into new information about qualifications and honorary appointments, ongoing academic-misconduct complaints remain under process, and it will not comment further until the investigation concludes. The current rendered page reports `Last updated: 06 Aug 2026` at 14:14:27 +01:00, later than the earlier 09:32:06 timestamp captured on 6 August. This is a page-version/access observation, not an investigation result.

- [Recheck statement HTML](../assets/captures/2026-08-07-status-recheck/cambridge-notices.html) — SHA-256 `adfb6786a28ac508e5f292a26961c3890856407b5d07c93b06e71b72815c928d`.
- [Recheck response headers](../assets/captures/2026-08-07-status-recheck/cambridge-notices.headers.txt) — SHA-256 `4f921987ec6c314b9ec2aa21cbedbcd64da4ecd662cf4795edf58fb15fd71c92`.

## 2026-08-08 recheck

The exact official notice URL returned HTTP 200 again. Its substantive statement remains unchanged. The page reports `Last-Modified: Fri, 07 Aug 2026 01:33:48 GMT`; the HTML body is byte-identical to the 7 August recheck. The Faculty profile URL also returned HTTP 404, with a body byte-identical to the preserved 6 August no-slash 404 capture. These are access-state observations, not evidence of an investigation outcome.

- [8 August official notice HTML](../assets/captures/2026-08-08-volatility-recheck/cambridge-notices-statement.html) — SHA-256 `adfb6786a28ac508e5f292a26961c3890856407b5d07c93b06e71b72815c928d`.
- [8 August official notice headers](../assets/captures/2026-08-08-volatility-recheck/cambridge-notices-statement.headers.txt) — SHA-256 `c1dd849332cc2185e46a617f763e4629a5f390a6a98debda5abe38b22e6141ea`.
- [8 August Faculty profile 404 HTML](../assets/captures/2026-08-08-volatility-recheck/cambridge-faculty.html) — SHA-256 `ec7e254cc1d942451e8ae2be2e1a6d5cc3588fef7eedfb5d0ad816c9a2f5c0df`.
- [8 August Faculty profile 404 headers](../assets/captures/2026-08-08-volatility-recheck/cambridge-faculty.headers.txt) — SHA-256 `f08fe9f2c925f1fd18aff823cabe1c810a3803eedcb45383e2473d7667b4be91`.

## 2026-08-07 indexed/live split recheck

On 7 August, the web search index exposed a newer snippet for the canonical Faculty profile URL. The indexed text described Runnymede as a “Former Trustee,” retained BSA/NHS RHO/ITV memberships, described Nelson Mandela University as a visiting-professor role, and omitted the older Ohio State and Durham honorary-professor wording. This is an indexed-page observation only: a direct shell request and the in-app browser both returned the Faculty site's 404 page, so the indexed text cannot be treated as a currently live Cambridge profile.

The direct 404 body captured in this recheck is distinct from the earlier no-slash 404 body and is preserved below. The changed body does not alter the 404 classification or establish why Cambridge's profile was removed.

- [7 August direct 404 body](../assets/captures/2026-08-07-cambridge-faculty-profile-reappeared/page.html) — SHA-256 `7bba78496dc22a2d7f739ba7aa9f10898954fd4157864babb2ab99dec253cb04`
- [7 August response headers](../assets/captures/2026-08-07-cambridge-faculty-profile-reappeared/page.headers.txt) — SHA-256 `92d34a53c512ba38a519ec88cc282034643ff3d71e0c123384932c9907228b0d`

## 2026-08-08 direct recheck

A further direct request to the exact slash URL again returned HTTP 404. Its 37,526-byte body is not byte-identical to the 7 August capture, although it remains a generic Drupal “Page not found” response and contains no Arday profile or replacement location. The changed response is preserved as a volatility observation; it does not alter the 404 classification or establish why the profile is unavailable.

- [8 August direct 404 body](../assets/captures/2026-08-08-cambridge-faculty-profile-404/page.html) — SHA-256 `2bcaada4c5e5df8547b8400eb75a10d4d4558f21aad46ecb3151d0bc730977eb`
- [8 August response headers](../assets/captures/2026-08-08-cambridge-faculty-profile-404/page.headers.txt) — SHA-256 `9e4942abc5fa2d2d000bdc647a2477a0b6056617bb34f3749f7b22fbae11e45a`
