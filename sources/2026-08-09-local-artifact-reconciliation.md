---
id: SRC-1139
type: archive-integrity audit
title: "Jason Arday archive — local artifact reconciliation"
subject: ../entities/jason-arday.md
audited: 2026-08-09
status: reconciled; large media remains local-only
evidence_class: repository provenance and access-boundary audit
---

# Local artifact reconciliation

This audit closes the gap between the source ledger and the working archive. The snapshot contained 53 untracked files totalling 5,276,566,985 bytes. The large set is not a new body of evidence: it is the local preservation layer for already-canonical Arday records.

## Canonical media already represented

The following local files map to existing source records and should not be opened as new people, events, or claims:

- Research Cast UK MP3 — `SRC-198` / `SRC-1027`.
- St Mary’s Values Talk streams — `2020-11-19-st-marys-values-talk.md` and its audio audit.
- Warwick Education Conference keynote, including the MP4 and upload parts — `2026-06-04-warwick-education-conference-jason-arday.md` / `SRC-1088`.
- CBS interview, MMU keynote, PBS interview, Bristol Graceland lecture, Cambridge “Black Men On The Couch,” Oxford talks, UCL keynote, ARU *Unlearn*, RSC forum, Diversity Seminar, *The Neurodivergent Show*, OpenLearn, and UCU webinar recordings — their existing event/media records and caption audits.
- Channel 4, LBC, GuildHE/Wonkhe, and Spiked video derivatives — their existing broadcast/commentary records; derivatives are not independent witnesses.
- Recheck pages for Cambridge, Durham, Taylor & Francis, Hindustan Times, UAL, Vimeo, and OpenAlex — source-version/access-boundary material already covered by the corresponding source records.

## Promotion rule

Small, clean public artifacts may be committed when their parent source record identifies them: captions, metadata JSON, thumbnails, rendered pages, and page bodies. Response-header files are excluded from promotion because they can contain cookies or other transient request material. The MP4/MP3 files remain local-only unless a separate storage decision is made; ordinary GitHub commits are not an appropriate transport for multi-hundred-megabyte media.

## Explicit quarantine

`tmp/`, `tmp-fighting.txt`, and `tmp-football.txt` are scratch or intermediate extraction material without a stable source-record role. They remain unpromoted. The archive does not treat their presence as evidence, and future work should not re-audit them unless they are attached to a named source with provenance.

## Boundary

This audit establishes provenance and prevents duplicate discovery. It adds no new biographical, employment, sporting, publication, or misconduct claim. Reopen it only when a local artifact lacks a canonical source record, a lawful binary-storage destination is chosen, or a source-version changes materially.
