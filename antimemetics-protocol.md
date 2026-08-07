# Antimemetics research protocol

This workspace uses “antimemetics” in the research-method sense: preserve the things most likely to be forgotten, omitted, overwritten, or rediscovered without context. The reference is to qntm’s *There Is No Antimemetics Division* and the SCP antimemetics tradition.

This is not a claim that Jason Arday or any source is anomalous. It is a protocol for epistemic hygiene.

## Epistemic machinery in the source text

The useful reference is not merely the atmosphere of qntm’s *There Is No Antimemetics Division*. The linked SCP text repeatedly turns epistemology into procedure: what can count as evidence when memory, observation, records, and even the existence of the research project may be unstable. The passages below are the parts worth importing into this archive.

### 1. Negative knowledge: describe the boundary, not the object

In **“We Need To Talk About Fifty-Five,”** SCP-055 is treated as something that can be characterized only by exclusions. The staff can preserve what it is not—its shape, color, competence, and classification—while the positive description defeats itself. The method is not “we know nothing”; it is a constrained, auditable negative description.

> “we can only record what it isn’t.” — qntm, “We Need To Talk About Fifty-Five.”

For this archive, a negative description is a real research product. “No matching Gazette notice in the tested query,” “the current directory does not reproduce the indexed role,” and “the named comparator text was not recovered” are different from “the event did not happen.” Every negative-space observation must state the search boundary and the alternative explanations still open. [Source text](https://scp-wiki.wikidot.com/we-need-to-talk-about-fifty-five) · [local capture](assets/captures/2026-08-07-antimemetics-reference/scp/we-need-to-talk-about-fifty-five.html)

### 2. Provenance before belief: interrogate the file

The same conversation refuses to accept a file merely because it has the right institutional appearance. It asks who wrote it, how the interview was conducted, who the named participants were, and how the witness still retains knowledge of it. Date stamps, signatures, access credentials, and a coherent interface are evidence about the record—not automatic proof of the record’s contents.

Apply this directly to every contested Arday item:

- Who authored the biography, correction, CV, transcript, comparison, or institutional statement?
- What was the source’s path from event to publication?
- Is the quoted speaker identified, and is the quotation independently recoverable?
- What does the artifact establish about its own existence, versus what it asserts about the world?
- What would a hostile or mistaken source look like if it carried perfectly plausible metadata?

### 3. Asynchronous research: design for rediscovery

In **“CASE COLOURLESS GREEN,”** the Division’s research is explicitly asynchronous: the subject is forgotten between iterations and rediscovered repeatedly. The failure is not only memory loss; it is the loss of an obvious entry point. A room full of notes, diagrams, dates, and familiar handwriting can still be unusable if no one knows which document should be read first.

That is the exact justification for the workspace’s handoff architecture: `WORK-STATE.md` is the re-entry point; `research-log.md` records the last completed pass; `NEXT.md` says what not to repeat; the registry and hashes make the recovered artifacts recognizable. A future researcher must be able to rediscover the project without rediscovering the same sources from scratch. [Source text](https://scp-wiki.wikidot.com/case-colourless-green) · [local capture](assets/captures/2026-08-07-antimemetics-reference/scp/case-colourless-green.html)

### 4. Pattern recognition is inference, not revelation

The case describes raw manifestations as data points and the larger threat as a pattern that becomes visible when those points are arranged in conceptual space. That is a useful model for this dossier’s controversy entity: individual biography changes, corrections, affiliation conflicts, fundraising versions, and textual comparisons can be plotted together without pretending that the pattern itself proves motive.

The anti-overfitting rule is equally important. A pattern may be a genuine common cause, ordinary institutional copying, a shared upstream source, a mixture of unrelated errors, or an artifact of selective collection. Every pattern claim therefore needs: the included records, the excluded records, the possible common sources, the counterexamples, and the inferential step that remains unresolved. [Source text](https://scp-wiki.wikidot.com/case-colourless-green)

### 5. Reconstruct from first principles when memory is compromised

In **“Your Last First Day,”** Wheeler responds to memory destruction by examining her own cognition, distinguishing what she remembers from how she knows it, and rebuilding a plan from first principles. The compact line is:

> “If I were me, what would my plan have been?” — qntm, “Your Last First Day.”

The research analogue is to rebuild a claim from the primary artifact outward: identify the exact proposition, locate the earliest public manifestation, compare later versions, classify the source, and only then assess the pattern. Do not let a remembered summary, a repeated biography, or an already-written conclusion substitute for the underlying record. [Source text](https://scp-wiki.wikidot.com/your-last-first-day) · [local capture](assets/captures/2026-08-07-antimemetics-reference/scp/your-last-first-day.html)

### 6. Externalize memory before interpretation

In **“Introductory Antimemetics,”** a junior researcher realizes that direct communication has failed and writes an SCP entry as a message to a future reader. The document is not a polished conclusion; it is an emergency handoff containing the next action and the conditions under which the reader should proceed.

> “I should write an SCP.” — qntm, “Introductory Antimemetics.”

This is the right flavor for our records: write the source map while the uncertainty is still present. A handoff should preserve the failed route, the tempting but unsupported inference, the exact next verification, and the point at which the researcher may safely stop. [Source text](https://scp-wiki.wikidot.com/introductory-antimemetics) · [local capture](assets/captures/2026-08-07-antimemetics-reference/scp/introductory-antimemetics.html)

### 7. Protocols are containment, not decoration

The Division’s procedures exist because ordinary observation is not reliable enough: notes can vanish, a researcher can forget the reason for a visit, and a record can be formally valid while its provenance is inaccessible. Translated into this project, containment means:

- preserve the source before summarizing it;
- keep primary text, secondary report, interpretation, and hypothesis in separate records;
- use negative-space entries for failed acquisition and changed pages;
- record the chain of custody for every quote, image, transcript, and comparison;
- make repeated public wording count as propagation, not corroboration;
- require a new artifact or changed state before reopening a closed search;
- leave a compact re-entry note after every research session.

The fiction’s epistemology is therefore a practical discipline: knowledge is not the feeling that a story is coherent. It is a recoverable chain from artifact to proposition to inference, with the missing links named.

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
