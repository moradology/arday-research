---
id: SRC-576
---

# SRC-576 — Cambridge Faculty migrated-host profile and directory boundary

Rechecked 2026-08-09: the indexed profile result still exposed the prior Arday biography, while opening the same profile URL redirected to the Faculty home page again. No replacement profile or Arday directory entry was exposed.

## Source identity

- Jason Arday profile route: <https://faculty.educ.cam.ac.uk/people/staff/arday/>
- Migrated Faculty “Our people” route: <https://faculty.educ.cam.ac.uk/about-us/our-people?page=1>

This is a distinct current-host check from SRC-208’s older `www.educ.cam.ac.uk/people/staff/arday/` 404 state and SRC-574’s `www.educ.cam.ac.uk/people/members/` page. Search indexing still exposes the former migrated-host profile as Jason Arday’s page, but direct retrieval on 8 August 2026 redirected the profile route to the Faculty home page. The migrated “Our people” route returned HTTP 200 and a rendered search form, but its response contained no exact `Jason`, `Arday`, or “Professor of Sociology” occurrence.

## Preservation

- [Profile-route response](../assets/captures/2026-08-08-cambridge-faculty-profile-migrated/page.html)
- [Profile-route headers and redirect chain](../assets/captures/2026-08-08-cambridge-faculty-profile-migrated/page.headers.txt)
- [Migrated members-directory response](../assets/captures/2026-08-08-cambridge-faculty-profile-migrated/members.html)
- [Migrated members-directory headers](../assets/captures/2026-08-08-cambridge-faculty-profile-migrated/members.headers.txt)

The direct profile capture’s final response is the Faculty home page, whose canonical link is `https://faculty.educ.cam.ac.uk/home`; the members page’s canonical link is `https://faculty.educ.cam.ac.uk/about-us/our-people`. The web-indexed result remains a separate stale/index manifestation and is not silently substituted for the direct response.

## Evidence boundary

The live migrated host therefore adds a current negative-space observation: the older profile is not directly rendered at its indexed route, and the current “Our people” response does not expose Arday. This strengthens the documented indexed/live mismatch but does not prove that he is no longer employed, that every Cambridge relationship ended, or why the migration and omission occurred.

The indexed profile text is retained only as a source-version lead. It carries qualifications, research projects, and role wording—including “Former Trustee of the Runnymede Trust,” BSA trusteeship, Autism Action, and project co-investigator descriptions—that must be read against direct institutional, regulator, and project records. It is not treated as current-status proof merely because a search engine still displays it.

## Reopen condition

Reopen for a directly rendered replacement profile, a current Faculty directory entry, a formal Cambridge outcome, or a changed redirect/API state. Do not create another record for the same indexed snippet or repeat the same direct route without a material state change.
