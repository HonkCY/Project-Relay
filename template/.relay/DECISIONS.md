# Decisions

Use stable IDs (`D-001`, `D-002`, …). Accepted decision text is preserved; replace it
with a new accepted decision and mark `superseded by` instead of rewriting history.

No decision records yet.

## Record shape

```markdown
## D-001 — Concise title

- **Kind:** decision
- **Authority:** accepted | provisional | superseded | rejected | unresolved
- **Provenance:** live-environment | durable-artifact | incumbent-recall | human-report | inference | unknown
- **Verification:** verified | unverified | contradicted | stale | inaccessible
- **Evidence ref:** safe locator, record ID, or none
- **Checked at:** ISO-8601 timestamp/date or unknown
- **Checked by:** human/agent/tool identity or unknown
- **Accepted by/at:** identity/time when authority is accepted
- **Supersedes / superseded by:** D ID or none
- **Decision:** exact normative choice
- **Why:** concise rationale and rejected alternative when operationally useful
```
