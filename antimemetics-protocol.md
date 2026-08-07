# Antimemetics research protocol

This workspace uses “antimemetics” in the research-method sense: preserve the things most likely to be forgotten, omitted, overwritten, or rediscovered without context. The reference is to qntm’s *There Is No Antimemetics Division* and the SCP antimemetics tradition.

This is not a claim that Jason Arday or any source is anomalous. It is a protocol for epistemic hygiene.

## Reference passages and flavor

The literary reference is qntm’s *There Is No Antimemetics Division*. The quotations below are deliberately short excerpts from the publisher’s authorized sample, retained as a mnemonic interface rather than as a substitute for the book. The sample’s printed pages are noted so the wording can be rechecked. [Publisher sample PDF](https://cdn.penguin.co.uk/dam-assets/books/9781529953176/9781529953176-sample.pdf) · [local capture](assets/captures/2026-08-07-antimemetics-reference/sample.pdf)

> “We don’t have an Antimemetics Division.” — qntm, *There Is No Antimemetics Division*, publisher sample, printed p. 13.

> “There are ideas that cannot be spread.” — qntm, *There Is No Antimemetics Division*, publisher sample, printed p. 14.

> “In the Antimemetics Division, we have the opposite problem.” — qntm, *There Is No Antimemetics Division*, publisher sample, printed p. 16.

The flavor to borrow is procedural dread, not supernatural certainty: a missing record may be ordinary loss, deliberate revision, access friction, or a genuinely unresolved contradiction; the investigator’s first task is to make the gap visible. The archive should feel like a field manual assembled under pressure—case files, timestamps, hashes, redactions, cross-checks, and handoff notes—while every factual statement remains tied to an ordinary source and an explicit evidence status.

Use the book’s atmosphere in headings, prompts, and mnemonic labels only. Do not imitate its prose at length, present fiction as a factual model of Arday, or let theatrical language replace source criticism.

### Literary motif → research operation

| Motif | Operational translation in this archive |
|---|---|
| An idea that cannot be spread | A claim that appears in one source but fails to survive ordinary copying, indexing, citation, or retrieval; preserve the exact source and label the boundary. |
| The division that “doesn’t” exist | A role, committee, investigation, or publication pathway present in one biography but absent from the host’s current records; track both states without inferring why. |
| The opposite problem | When the archive has too much repeated public copy but too little independent provenance; deduplicate circulation and seek the underlying record. |
| Mnestic medication | Redundant checkpoints: `WORK-STATE.md`, `NEXT.md`, the research log, source hashes, local captures, and Drive/Git mirrors. |
| Unknowns and case files | Separate `Source`, `Claim`, `NegativeSpaceObservation`, `Hypothesis`, and `Controversy` records rather than compressing them into one narrative. |
| Redaction and damaged memory | Preserve inaccessible, superseded, partially captured, and corrected states; never silently fill the blank with inference. |

### Antimemetic writing rules

- Write the recovery path into the record: URL, date, query, response state, local filename, and checksum.
- Treat repetition as a propagation signal, not independent corroboration.
- Prefer a small, exact quotation with a page or timecode over a large unverified transcript.
- When a source changes, preserve both versions and describe the observable change before interpreting it.
- Make the handoff legible: a future researcher should know what to reopen and what not to repeat.
- Keep the dramatic label subordinate to the evidence. “Unknown,” “missing,” “contested,” and “unresolved” are statuses, not villains.

## Operating principles

### 1. Preserve the memory of the investigation

Every session leaves a checkpoint in [WORK-STATE.md](WORK-STATE.md), a completed-search entry in [research-log.md](research-log.md), and a next action in [NEXT.md](NEXT.md).

### 2. Treat absence as data

Record missing pages, removed videos, changed biographies, inaccessible records, unreturned requests, and unexplained gaps. “Not found” is not “did not happen.”

Use the phrase `negative-space observation` for a documented absence and record:

- what was expected;
- where it was searched;
- when it was searched;
- whether the absence is reproducible;
- plausible explanations.

### 3. Never let one source become reality

Separate:

1. what a source says;
2. what can be independently verified;
3. what follows as an interpretation;
4. what remains unknown.

The [claims ledger](claims-ledger.md) is the containment boundary between those layers.

### 4. Preserve superseded states

Do not silently edit away an earlier biography, affiliation, publication page, correction, or institutional statement. Create a dated record and link it with `updates`, `supersedes`, or `contests`.

### 5. Use mnemonics, not intuition

Stable IDs, repeated metadata fields, source hashes where local files exist, and explicit timestamps are more reliable than remembering that something “looked familiar.”

### 6. Assume the archive can lose context

Every record should remain intelligible if read months later by someone who has never seen the surrounding conversation. Avoid “as above,” unexplained pronouns, and uncited conclusions.

### 7. Minimize exposure and amplification

Collect only public material relevant to the research question. Do not add private contact details, family information, home addresses, or unverified personal allegations. Link to sensitive claims only when they are materially relevant and responsibly sourced.

### 8. Resist narrative infection

Keep biography, scholarship, public impact, criticism, and allegations in separate records. Do not let a compelling life story prove scholarship, or let a controversy erase the existence of prior work. Each domain gets its own evidence trail.

## Antimemetic check before closing a session

- What did we learn?
- What did we fail to find?
- What changed since the last checkpoint?
- Which source is most likely to disappear or change?
- Which claim is currently being carried by only one source?
- What is the single next action?

## Red flags

Flag a record for review when:

- a page changes without a dated explanation;
- a source is cited but cannot be located;
- multiple records repeat the same wording without independent provenance;
- a claim appears only in search snippets or social posts;
- a correction is mentioned but the original and corrected versions are not preserved;
- an absence is being treated as disproof;
- a source’s apparent authority is doing more work than its actual evidence.

## Required record footer

For high-value or contested records, add:

```text
Antimemetic check:
- First observed:
- Last checked:
- What could disappear or change:
- Negative-space observations:
- Single-source dependencies:
- Next verification:
```
