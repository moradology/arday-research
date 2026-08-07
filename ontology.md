# Ontology and data model

## Core entities

| Type | Meaning | Examples |
|---|---|---|
| `Person` | named individual | Jason Arday, co-authors, critics, editors |
| `Organization` | institution, publisher, charity, media outlet | Cambridge, Durham, Runnymede Trust, Battersea Park Rangers |
| `Publication` | book, article, report, thesis, correction | *The Black Curriculum* report |
| `Media` | video, audio, interview, transcript, image, slide deck | UCL keynote, PBS interview |
| `Event` | appointment, talk, award, investigation, resignation | Cambridge appointment |
| `Claim` | a proposition about a person, work, or event | “appointed professor at Cambridge in 2023” |
| `Source` | a public record supporting or contesting a claim | university page, DOI record, news report |
| `Project` | research, policy, charity, or public-engagement activity | Black Student Wellbeing Study |
| `Affiliation` | time-bounded employment, visiting, honorary, governance, consultancy, or programme relationship | Glasgow professorship, Ohio State visiting-role claim, Runnymede directorship |
| `NegativeSpaceObservation` | a missing, inaccessible, changed, superseded, contradicted, or not-locally-captured public record | Cambridge statement URL, revised Guardian page, failed PDF acquisition |

## Relationships

Use plain-language relationship names in Markdown links and optional structured metadata:

- `Person --authored--> Publication`
- `Person --appears-in--> Media`
- `Person --employed-by--> Organization`
- `Person --played-for--> Organization` (retain sport, team level, match date, and source boundary)
- `Person --has-affiliation--> Affiliation --with--> Organization`
- `Person --trustee-of--> Organization`
- `Person --spoke-at--> Event`
- `Publication --published-by--> Organization`
- `Media --hosted-by--> Organization`
- `Claim --supported-by--> Source`
- `Claim --contested-by--> Source`
- `Claim --about--> Person|Publication|Event|Organization`
- `Source --updates--> Source`

## Record metadata

Each record should use YAML front matter where practical:

```yaml
---
id: source-YYYYMMDD-short-name
type: Source
title: ""
date: YYYY-MM-DD
accessed: YYYY-MM-DD
status: verified
source_kind: primary | institutional | publisher | journalism | commentary
entities:
  - entities/jason-arday.md
urls:
  - "https://example.org"
---
```

## Evidence rules

1. A source can establish what it says; it does not automatically establish that every statement in it is true.
2. Primary records are preferred for appointments, publication metadata, corrections, charity filings, and institutional decisions.
3. Journalism is useful for chronology, interviews, and public reaction; label it `reported` when not independently confirmed.
4. Commentary, social media, similarity analyses, and AI-detection tools are discovery inputs, not final findings.
5. Preserve corrections and retractions as separate records. Never silently replace the earlier record.
6. For contested claims, record both the allegation and the response, with dates and exact source links.
7. Record absences and changed pages as `NegativeSpaceObservation` records or notes; never convert missing evidence into a positive claim.
8. Preserve superseded versions and link them; the archive is append-oriented.

## Suggested controlled vocabulary

`academic-integrity`, `race-and-higher-education`, `neurodiversity`, `mental-health`, `decolonising-curriculum`, `social-mobility`, `charity`, `fundraising`, `athletics`, `media-appearance`, `appointment`, `award`, `correction`, `investigation`, `resignation`.
