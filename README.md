# Jason Arday research workspace

This is a living, source-linked knowledge base about Jason Arday. It is designed to preserve public material, document provenance, and distinguish verified records from claims, allegations, commentary, and unresolved questions.

## Versioning and binary assets

This workspace is designed to live in Git. Markdown, source records, claims, ontology files, timelines, research logs, and checksums are the canonical layer. Small research images may be committed directly. Large videos, audio, and PDFs should use Git LFS when it is available, or remain in an external binary archive with the original URL, access date, license/rights note, filename, byte count, and SHA-256 recorded under `assets/metadata/`. Never replace a missing binary with an unmarked link: record its acquisition state explicitly.

## Start here

- [Work state](WORK-STATE.md) — current position, handoff instructions, and anti-loop rules.
- [Next actions](NEXT.md) — ordered backlog; start here after reading work state.
- [Research log](research-log.md) — scopes already searched and their boundaries.
- [Source registry](source-registry.md) — deduplication ledger and canonical source locations.
- [Antimemetics protocol](antimemetics-protocol.md) — preservation, absence-tracking, and epistemic-hygiene rules.
- [Entity record](entities/jason-arday.md) — the central record for the person.
- [Working biography](biography.md) — readable narrative with claim-level caveats and open verification questions.
- [Childhood evidence map](childhood-evidence.md) — compact claim matrix for early life, schooling, literacy, and sports, with anti-loop reopening rules.
- [Ontology](ontology.md) — concepts, relationships, and evidence rules.
- [Timeline](timeline.md) — dated career, media, publication, and controversy events.
- [Claims ledger](claims-ledger.md) — claim-level status and supporting sources.
- [Media index](media.md) — videos, audio, interviews, images, and transcripts.
- [Public-output index](jason-arday-public-output-index.md) — broad discovery list of publications and appearances.
- [Affiliation ledger](affiliations.md) — time-bounded employment, visiting, honorary, governance, and consultancy records.
- [Negative-space ledger](negative-space.md) — missing, inaccessible, changed, superseded, contradicted, and not-locally-captured states.

## Directory layout

```text
entities/     people, organizations, projects, and other named entities
sources/      one Markdown record per source or source bundle
media/        video, audio, image, transcript, and presentation records
publications/ article, book, report, thesis, and correction records
events/       appointments, talks, awards, investigations, and other events
assets/       locally preserved files, screenshots, and downloaded PDFs
templates/    reusable record templates
```

## Evidence conventions

Every substantive statement should be linked to a source record or an external source. Use these status labels:

- `verified` — directly supported by a primary or authoritative record.
- `reported` — published by a reputable secondary source but not independently confirmed here.
- `alleged` — a claim made by a source and not established as fact.
- `disputed` — materially contested by credible sources.
- `unresolved` — evidence is incomplete or an investigation is ongoing.
- `retracted/corrected` — the record has been withdrawn, corrected, or superseded.

Do not collapse a person’s identity, work, and allegations into one undifferentiated narrative. Keep the source, claim, interpretation, and confidence visible.

## Adding a new item

1. Read [WORK-STATE.md](WORK-STATE.md) and take the first relevant item in [NEXT.md](NEXT.md).
2. Check [source-registry.md](source-registry.md) for duplicates before searching.
3. Copy the relevant file from [templates](templates/).
4. Give the record a stable ID and canonical file location.
5. Record the original URL, publisher/host, publication date, access date, and status.
6. Link the record from the relevant index, timeline, or entity page.
7. Update the registry and [research-log.md](research-log.md).
8. If the item changes an existing claim, update [claims-ledger.md](claims-ledger.md) and note the change rather than overwriting history.
