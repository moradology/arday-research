# Antimemetics research protocol

This workspace uses “antimemetics” in the research-method sense: preserve the things most likely to be forgotten, omitted, overwritten, or rediscovered without context. The reference is to qntm’s *There Is No Antimemetics Division* and the SCP antimemetics tradition.

This is not a claim that Jason Arday or any source is anomalous. It is a protocol for epistemic hygiene.

## Epistemic machinery in the source text

An LLM does not retain the whole archive or the whole conversation. It works from a bounded, changing context assembled from retrieved fragments. These principles make that limitation explicit and turn it into a design constraint: preserve provenance, externalize state, separate observation from inference, and make every conclusion recoverable.

### 1. Negative knowledge: describe the boundary, not the object

An LLM is especially vulnerable to treating an unreturned search, omitted passage, or missing artifact as if it were absent from the world. Negative descriptions prevent that collapse: they preserve what the current context rules out without inventing a positive account.

> “we can only record what it isn’t.” — qntm, “We Need To Talk About Fifty-Five.”

For this archive, “no matching Gazette notice in the tested query” is a bounded result, not “the event did not happen.” State the search boundary and the live alternatives. [Source text](https://scp-wiki.wikidot.com/we-need-to-talk-about-fifty-five) · [local capture](assets/captures/2026-08-07-antimemetics-reference/scp/we-need-to-talk-about-fifty-five.html)

### 2. Provenance before belief: interrogate the file

Context compression makes repeated, polished, institutionally formatted text look more trustworthy than it is. Provenance checks stop the model from confusing a document’s appearance with independent evidence for its claims.

For every contested item, record:

- Who authored the biography, correction, CV, transcript, comparison, or institutional statement?
- What was the source’s path from event to publication?
- Is the quoted speaker identified, and is the quotation independently recoverable?
- What does the artifact establish about its own existence, versus what it asserts about the world?
- What would a hostile or mistaken source look like if it carried perfectly plausible metadata?

### 3. Asynchronous research: design for rediscovery

An LLM session is inherently asynchronous: the next session will not share the same working context, and retrieval may return a different slice. The failure mode is therefore repeated discovery and circular research. `WORK-STATE.md` is the re-entry point; `research-log.md` records completed work; `NEXT.md` records what not to repeat; the registry and hashes identify artifacts. [Source text](https://scp-wiki.wikidot.com/case-colourless-green) · [local capture](assets/captures/2026-08-07-antimemetics-reference/scp/case-colourless-green.html)

### 4. Pattern recognition is inference, not revelation

An LLM is good at completing patterns from partial evidence. That makes a coherent pattern a hypothesis, not a discovery. List included and excluded records, possible common sources, counterexamples, and the inferential step still unresolved. [Source text](https://scp-wiki.wikidot.com/case-colourless-green)

### 5. Reconstruct from first principles when memory is compromised

When prior context is missing or contaminated, summaries become false memory. Rebuild the claim from the artifact outward: proposition, earliest public manifestation, versions, source class, then interpretation. The compact line is:

> “If I were me, what would my plan have been?” — qntm, “Your Last First Day.”

Do not let a remembered summary, repeated biography, or existing conclusion substitute for the underlying record. [Source text](https://scp-wiki.wikidot.com/your-last-first-day) · [local capture](assets/captures/2026-08-07-antimemetics-reference/scp/your-last-first-day.html)

### 6. Externalize memory before interpretation

Anything left only in the model’s active context disappears when the session ends. External notes therefore have higher evidentiary value than fluent recollection: they preserve failed routes, uncertainty, next actions, and stopping conditions for a later context.

> “I should write an SCP.” — qntm, “Introductory Antimemetics.”

Write the source map while uncertainty is still present. [Source text](https://scp-wiki.wikidot.com/introductory-antimemetics) · [local capture](assets/captures/2026-08-07-antimemetics-reference/scp/introductory-antimemetics.html)

### 7. Protocols are containment, not decoration

Protocols are containment against context loss. They make it harder for a later model—or the same model after retrieval—to mistake fluency, repetition, or a surviving fragment for the full evidential record:

- preserve the source before summarizing it;
- keep primary text, secondary report, interpretation, and hypothesis in separate records;
- use negative-space entries for failed acquisition and changed pages;
- record the chain of custody for every quote, image, transcript, and comparison;
- make repeated public wording count as propagation, not corroboration;
- require a new artifact or changed state before reopening a closed search;
- leave a compact re-entry note after every research session.

The target is a recoverable chain from artifact to proposition to inference, with missing links named.

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
