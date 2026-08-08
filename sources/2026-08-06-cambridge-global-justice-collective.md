---
id: SRC-195
type: institutional research-group record
title: "Global Justice Collective — Cambridge Faculty of Education"
subject: ../entities/jason-arday.md
published: indexed page version; accessed 2026-08-06
accessed: 2026-08-06
status: indexed first-party membership record / current host URLs 404; 8 August 2026 recheck adds migrated-host boundary
evidence_class: first-party university research-group page with changed-page boundary
---

# Record

The Cambridge Faculty of Education’s indexed Global Justice Collective page listed Jason Arday as one of six GJC members. The indexed page described the group as working on transnational solidarities and alternatives to educational systems that reproduce global domination, with research areas including intersectionality, decoloniality, Global Critical Race Theory, informal education, political philosophy, critical and cultural theory, and arts in education.

On 2026-08-06, both the Faculty URL and the older `oer.aws.educ.cam.ac.uk` URL returned HTTP 404 when retrieved directly. The membership and research-group description are therefore preserved as a dated first-party indexed page version, not asserted as a current membership state.

On 2026-08-08, the migrated Faculty route `https://faculty.educ.cam.ac.uk/research/groups/gjc/` also returned a Cambridge-branded HTTP 404. The OER and risk AWS variants again returned HTTP 404; the AWS hosts were inspected with certificate validation disabled only after ordinary TLS failed on the expired certificate. No route exposed a replacement membership page or current group record.

## Changed host-state follow-up

The indexed result was also served from `risk.aws.educ.cam.ac.uk/research/groups/gjc/`. A direct request on 2026-08-06 failed ordinary TLS validation because the host certificate was expired; a diagnostic `curl -k` request then returned a Cambridge-branded HTTP 404 page stating that the path was unavailable. This is a third changed/removed host manifestation, not evidence that the membership never existed.

## Local preservation

- Faculty URL: https://www.educ.cam.ac.uk/research/groups/gjc/
- Older Faculty OER URL: https://oer.aws.educ.cam.ac.uk/research/groups/gjc/
- [Faculty 404 snapshot](../assets/documents/cambridge-gjc-page-404-2026-08-06.html)
- Faculty 404 SHA-256 after normalization: `e89c441db8f78e9f10839c1cb2cefe1dc107730452542d1834bb5ece6649a587`
- [OER 404 snapshot](../assets/documents/cambridge-gjc-oer-page-404-2026-08-06.html)
- OER 404 SHA-256 after normalization: `b590bc9e85e1ffb7409b422d56ae2ce580be0c212f3aabec907931273817e74d`
- [AWS risk-host 404 snapshot](../assets/documents/cambridge-gjc-risk-2026.html) — SHA-256 `ff6ff80e7d3f9b1ddc6d6775a9dd5a93763b2e936c81e87a85f974c54e2184b`.
- [AWS risk-host response headers](../assets/documents/cambridge-gjc-risk-2026.headers.txt) — SHA-256 `6076adb73b5656a2cac6eca45ab861c61cd846c98129775a722ad928d333f9f3`.
- [8 August 2026 migrated Faculty 404 response](../assets/captures/2026-08-08-cambridge-gjc-aws/faculty_educ_cam_ac_uk_research_groups_gjc_.html)
- [8 August 2026 migrated Faculty headers](../assets/captures/2026-08-08-cambridge-gjc-aws/faculty_educ_cam_ac_uk_research_groups_gjc_.headers.txt)
- [8 August 2026 OER response](../assets/captures/2026-08-08-cambridge-gjc-aws/oer.aws.educ.cam.ac.uk.html)
- [8 August 2026 OER headers](../assets/captures/2026-08-08-cambridge-gjc-aws/oer.aws.educ.cam.ac.uk.headers.txt)
- [8 August 2026 risk-host response](../assets/captures/2026-08-08-cambridge-gjc-aws/risk.aws.educ.cam.ac.uk.html)
- [8 August 2026 risk-host headers](../assets/captures/2026-08-08-cambridge-gjc-aws/risk.aws.educ.cam.ac.uk.headers.txt)
