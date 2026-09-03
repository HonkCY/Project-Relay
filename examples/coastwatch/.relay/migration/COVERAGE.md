# Migration coverage — 2026-09-01-coastwatch

Synthetic, enumerated coverage; no completeness percentage is claimed. The columns
use the vocabulary and valid combinations in `migration-kit/COVERAGE.md`. Named
`EV-*` captures resolve in the [sanitized evidence registry](../evidence/README.md).

| ID | Domain/source | Locator or scope basis | Track | Criticality | Access | Result | Inspected by/at | Evidence/output refs | Gap/unknown | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CV-001 | v3 normalization thread | SRC-001, one active thread through delta sweep | operational | critical | accessible | pass | operator / 2026-09-01T09:30Z | MC-001, MC-002, MC-007, EV-CONV-02 | none | canonicalized |
| CV-002 | archived pilot thread | SRC-001, one named archive entry | forensic | supporting | inaccessible | unknown | operator / 2026-08-30T09:35Z | U-001 | U-001 | backlog |
| CV-003 | native instructions/auto-memory | SRC-002, all listed project scopes/topics | operational | critical | accessible | pass | operator / 2026-08-31T14:30Z | MC-001, MC-003, EV-MEM-01 | none | canonicalized |
| CV-004 | MCPs/connectors | SRC-002 complete incumbent settings inventory | operational | supporting | accessible | n/a | operator / 2026-08-31T14:30Z | SRC-002, EV-MEM-01: none configured or required | none | not-applicable |
| CV-005 | required CLI tools | SRC-003; uv, SSH, curl, Slurm | operational | critical | accessible | pass | operator / 2026-09-01T09:25Z | R-006, R-016, EV-TOOLS-01 | none | canonicalized |
| CV-006 | R-001 Git/worktree | one repo and one active worktree | operational | critical | accessible | pass | operator / 2026-09-01T09:10Z | SRC-006, R-001, EV-GIT-02 | none | canonicalized |
| CV-007 | R-002 remote topology | SRC-005; four durable roots plus scratch | operational | critical | accessible | pass | operator / 2026-09-01T09:16Z | R-002 topology, R-010 | none | canonicalized |
| CV-008 | asset lineage | raw, policy/maintenance, v3 result/QC, legacy v2 | operational | critical | accessible | pass | operator / 2026-09-01T09:19Z | R-003–R-005, R-012–R-015 | none | canonicalized |
| CV-009 | R-009 service | SRC-004 unit/container/endpoint inventory | operational | supporting | accessible | partial | operator / 2026-09-01T09:20Z | R-009, P-004, R-018, EV-RISK-01 | R-018 | constrained |
| CV-010 | scheduler/jobs | SRC-003 account queue/accounting since 2026-05-01 and automation list | operational | supporting | accessible | partial | operator / 2026-09-01T09:25Z | R-007, R-008, R-015, U-003, EV-RISK-01 | U-003: R-008 terminal state and R-017 spec | constrained |
| CV-011 | batch pipeline lifecycle | SRC-007: P-001 environment/test/update-by-pinned-checkout, P-002 run, P-003 reproduce/QC, P-004 verify, P-007 decision/recovery; no separate batch build/deploy/maintenance function | operational | critical | accessible | pass | operator / 2026-09-01T09:34Z | SRC-007, P-001–P-004, P-007, EV-GATE-01 | none; R-009 service lifecycle is separately constrained by CV-009 | canonicalized |
| CV-012 | dependencies/secret refs | lockfile, toolchain, scheduler, credential class | operational | critical | accessible | pass | operator / 2026-09-01T09:32Z | SRC-006, R-006, R-010, R-016, P-001 | none | canonicalized |
| CV-013 | deleted/undiscoverable conversations | SRC-001 product discovery limit | forensic | supporting | inaccessible | unknown | operator / 2026-09-01T09:35Z | U-002, R-019 | U-002 | backlog |

## Defensible roll-up

- **Operational critical rows (total):** 8 (CV-001, CV-003, CV-005–CV-008,
  CV-011–CV-012)
- **Unresolved operational critical rows:** 0
- **Operational supporting partial/unknown rows:** 2 (CV-009, CV-010), both constrained
- **Forensic open rows:** 2 (CV-002, CV-013)
- **Operational `not-attempted` rows:** 0
- **Scope limitations:** deleted conversations have an unknown denominator; SRC-001
  records the complete available listing method and U-002 explains its classification.

## Coverage assertions

- [x] Required domains have scope or justified `n/a`.
- [x] Known operational sources have rows or named bounded sets.
- [x] Every inaccessible/unknown result links a detailed blind spot.
- [x] Partial results state residual gaps and safe constraints.
- [x] Every row uses a valid result/disposition combination.
- [x] Every row uses a valid access/result combination.
- [x] No operational row uses the forensic-only `backlog` disposition.
- [x] Constrained rows have human-acceptance entries in CUTOVER.
- [x] No completeness percentage is claimed.
- [x] Operational and forensic tracks remain distinct.
