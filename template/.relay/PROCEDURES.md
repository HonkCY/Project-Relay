# Procedures

Use stable IDs (`P-001`, `P-002`, …). A claim that work is reproducible is not a
procedure; exact steps, validation, and recovery make it one.

No procedures yet.

## Procedure shape

```markdown
## P-001 — Action-oriented title

- **Authority:** accepted | provisional | superseded | rejected | unresolved
- **Provenance:** live-environment | durable-artifact | incumbent-recall | human-report | inference | unknown
- **Verification:** verified | unverified | contradicted | stale | inaccessible
- **Owner:** human/role or unknown
- **Last tested:** ISO-8601 timestamp/date or never
- **Applies to:** R/D IDs and version scope

### Preconditions and inputs

Exact requirements, dependency IDs, working directory, revision, and secret refs.

### Steps

Numbered commands/actions. Never embed secret values.

### Outputs

Expected artifacts and owning R IDs.

### Verification

Exact checks and pass criteria.

### Recovery

Safe rollback, retry, troubleshooting, escalation, and human gate.
```

