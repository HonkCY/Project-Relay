# Migration coverage — 2026-09-01-coastwatch

Synthetic, enumerated coverage; no completeness percentage is claimed.

| ID | Domain/source | Locator or scope basis | Track | Criticality | Access | Result | Inspected at | Evidence/output refs | Gap/unknown | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CV-001 | v3 normalization thread | incumbent thread listing, one active thread | operational | blocker | accessible | pass | 2026-08-30T09:30Z | MC-001, MC-002 | none | canonicalized |
| CV-002 | archived pilot thread | one named archive entry | forensic | supporting | inaccessible | unknown | 2026-08-30T09:35Z | U-001 | U-001 | backlog |
| CV-003 | native instructions and auto-memory | listed project scopes | operational | blocker | accessible | pass | 2026-08-30T09:50Z | source notes; MC-001 | none | canonicalized |
| CV-004 | MCPs/tools/connectors | incumbent settings inventory | operational | supporting | accessible | n/a | 2026-08-30T10:00Z | no MCP dependency; R-006 is local CLI | none | canonicalized |
| CV-005 | R-001 Git/worktree | one repo and one active worktree | operational | blocker | accessible | pass | 2026-09-01T09:10Z | R-001 | none | canonicalized |
| CV-006 | R-002 remote topology | host plus three durable roots and scratch | operational | blocker | accessible | pass | 2026-09-01T09:16Z | R-002–R-005, R-012 | none | canonicalized |
| CV-007 | asset lineage | raw, v3 derived/QC, legacy v2 families | operational | blocker | accessible | pass | 2026-09-01T09:19Z | R-003–R-005, R-012 | none | canonicalized |
| CV-008 | R-009 service | single optional dashboard | operational | supporting | accessible | partial | 2026-09-01T09:20Z | R-009, P-004, P-006 | exact restart unverified | risk-accepted |
| CV-009 | scheduler/jobs | all named active/planned/relevant legacy jobs | operational | supporting | accessible | partial | 2026-09-01T09:25Z | R-007, R-008, P-004 | R-008 current state unknown | risk-accepted |
| CV-010 | environment/build/reproduce | v3 critical procedure set | operational | blocker | accessible | pass | 2026-09-01T09:30Z | P-001–P-004 | optional P-006 incomplete | canonicalized |
| CV-011 | dependencies/secret refs | lockfile, scheduler, one credential class | operational | blocker | accessible | pass | 2026-09-01T09:32Z | R-006, R-010, P-001 | none | canonicalized |
| CV-012 | older undiscovered conversations | product cannot prove deleted history | forensic | supporting | inaccessible | unknown | 2026-09-01T09:35Z | scope limitation | unknown denominator | backlog |

## Defensible roll-up

- **Operational blocker rows:** 0
- **Operational supporting partial/unknown rows:** 2 (CV-008, CV-009), both constrained
- **Forensic open rows:** 2 (CV-002, CV-012)
- **Operational `not-attempted` rows:** 0
- **Scope limitations:** the incumbent product cannot enumerate deleted conversations;
  the accessible listing and one denied archive entry define the defensible scope.

## Coverage assertions

- [x] Required domains have scope or justified `n/a`.
- [x] Known operational sources have rows or named bounded sets.
- [x] Inaccessible/unknown operationally relevant results link detailed blind spots.
- [x] Partial results state residual gaps and safe constraints.
- [x] No completeness percentage is claimed.
- [x] Operational and forensic tracks remain distinct.

