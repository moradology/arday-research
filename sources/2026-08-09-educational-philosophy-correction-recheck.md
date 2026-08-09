---
id: SRC-911
type: publisher correction / changed access-state record
title: "Attempting to break the chain" correction — 9 August 2026 publisher PDF recheck
subject: ../entities/jason-arday.md
published: 2024-05-16
accessed: 2026-08-09
status: direct PDF route returned HTTP 403 Cloudflare challenge; no correction PDF recovered
evidence_class: publisher endpoint recheck / changed access state / local HTML challenge and headers
related_sources:
  - SRC-297
  - SRC-044
assets:
  - ../assets/captures/2026-08-09-educational-philosophy-correction-recheck/challenge.html
  - ../assets/captures/2026-08-09-educational-philosophy-correction-recheck/challenge.headers.txt
---

# Publisher correction — 9 August 2026 recheck

A direct request to Taylor & Francis’ PDF route for the correction to Arday, Belluigi, and Thomas’s “Attempting to break the chain: reimaging inclusive pedagogy and decolonising the curriculum within the academy” returned HTTP 403 with a Cloudflare managed challenge on 9 August 2026. The response body is HTML, not a PDF, and no new correction text was recovered.

This is a changed access-state manifestation of the canonical correction record `SRC-297`, not a second correction or a new publication. The current body is byte-distinct from the 5,563-byte challenge preserved on 8 August, so the state is retained for retrieval history. The indexed correction text and prior source record remain the controlling evidence for the correction’s stated amendment scope; this recheck adds no substantive claim.

## Local preservation

- [Challenge HTML](../assets/captures/2026-08-09-educational-philosophy-correction-recheck/challenge.html) — 5,542 bytes; SHA-256 `fb0048a5944af3f0357c296f6102cf2013e4d11af7d1afb50ee70b1b6a1eec5f`.
- [Response headers](../assets/captures/2026-08-09-educational-philosophy-correction-recheck/challenge.headers.txt) — SHA-256 `e10561cb59209a5d07d0ae883fc0e650cd601558c064f89a11c9516204adf656`.

## Links

- [Taylor & Francis PDF route](https://www.tandfonline.com/doi/pdf/10.1080/00131857.2024.2350203)
- [Canonical correction record](2024-05-16-educational-philosophy-correction.md)

## Evidence boundary

The artifact verifies only the 9 August 2026 access response. It does not establish removal, retraction, correction content beyond the canonical record, or any research-integrity finding.
