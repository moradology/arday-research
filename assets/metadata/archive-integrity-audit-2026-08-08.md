# Archive integrity audit — 2026-08-08

Read-only structural checks run from the repository root:

- Markdown relative-link check: **0 missing targets** across 3,661 local Markdown links.
- Source registry: **448 `SRC-*` entries** and **431 backticked source paths**; every backticked source path resolves to an existing file.
- ID-bearing source files: **431**; every `SRC-*` identifier is represented in `source-registry.md`.
- Claim ledger: **498 `C-*` identifiers**; no duplicate claim IDs detected.
- Source IDs: no duplicate `SRC-*` identifiers detected.

The source-note front-matter normalization backlog remains **zero**: all 431 source Markdown files carrying a source record have an in-file `SRC-*` identifier, and each identifier is represented in `source-registry.md`. Seven bounded batches normalized seventy-three legacy notes without changing their source bodies or registry mappings; later source additions also carry front matter.

The two pre-existing unstaged thesis extracts remain outside this audit’s mutation scope:

- `assets/documents/ljmu-thesis.txt`
- `assets/documents/research-integrity/zwozdiak-myers-2009-thesis.txt`

This audit verifies structural integrity only. It does not establish that external URLs remain live, that every source claim is true, or that the archive is substantively complete.
