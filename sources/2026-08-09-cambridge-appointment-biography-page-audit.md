---
id: SRC-1123
type: page-level institutional appointment audit
title: "Cambridge appointment announcement — page-level audit"
subject: ../entities/jason-arday.md
published: 2023-02-23
accessed: 2026-08-09
status: complete historical-announcement audit; current employment unresolved
evidence_class: first-party university appointment announcement / attributed biography / local HTML source versions
parent_source: SRC-114
related:
  - ../sources/2026-08-06-cambridge-profile-post-resignation-404.md
  - ../sources/2026-08-07-cambridge-appointment-recheck.md
assets:
  - ../assets/captures/2026-08-07-cambridge-appointment-recheck/faculty-announcement.html
  - ../assets/captures/2026-08-07-cambridge-appointment-recheck/news-announcement.html
urls:
  - https://faculty.educ.cam.ac.uk/230223-jason-arday
---

# Scope

This audit reads the surviving Cambridge Faculty/news announcement as a historical appointment artifact. It is deduplicated to [SRC-114](2023-02-23-cambridge-appointment-biography.md) and the 7 August recheck record; it is not a current Faculty profile and does not adjudicate the later Cambridge process.

## Page-level map

- **Appointment identity:** the announcement says Arday would take up the Professor of Sociology of Education post on 6 March 2023 and describes the appointment as a Cambridge professorship. The “youngest Black person ever” wording is institutional announcement framing, not independently established by the page.
- **Biographical framing:** the page presents Clapham, diagnosis/speech/literacy, assisted-living predictions, family/music support, Sandro Sandri, Surrey/PE-teacher training, and the bedroom-wall goal as biography and attributed recollection rather than contemporaneous records.
- **Public mission:** Arday is quoted about opening higher education to disadvantaged backgrounds, democratizing access, and using Cambridge as leverage for national/global change. These are dated public positions, not evidence of institutional outcomes.
- **Academic formation:** the announcement records his account of working as a PE lecturer while learning sociology, watching lectures, drafting papers, and attempting to recite material verbatim; it also preserves his statement that he lacked practical training/guidance and no mentor showed him how to write. This is relevant context for later integrity analysis, not an explanation or finding about textual overlap.
- **Career and research framing:** the page mentions two master’s qualifications, a PhD, the Runnymede *Aiming Higher* report, and race/education interests. These are host-published biography and source-propagation statements; the underlying records remain canonical separately.

## Source-version boundary

On 7 August 2026, both the legacy Faculty and `news.educ.cam.ac.uk` announcement routes returned HTTP 200 with the historical “will take up” wording, while the separate Faculty profile route was 404. This split is preserved as page topology. The surviving announcement establishes what Cambridge published in 2023 and does not establish current employment, the reason for profile removal, or the outcome of the later investigation.

## Local preservation

The Faculty and news HTML and response headers are preserved under `assets/captures/2026-08-07-cambridge-appointment-recheck/`. Existing C-001, C-027, C-366, and C-540 remain canonical; this audit adds page navigation and source-version boundaries without duplicating those claims.
