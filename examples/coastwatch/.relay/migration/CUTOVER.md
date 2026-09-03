# Migration cutover — 2026-09-01-coastwatch

This is synthetic evidence for the acceptance fixture, not a claim that external
systems or agents were actually run from this repository. Named `EV-*` captures
resolve in the [sanitized evidence registry](../evidence/README.md).

- **Fresh-agent candidate commit:** synthetic `ca11dad`
- **Coverage/records reviewed at:** synthetic pre-cutover evidence commit `c0ffee1`
- **Cutover tag:** synthetic `relay-cutover-2026-09-01-coastwatch`

The gate verdict below is derived from COVERAGE at that named boundary. Synthetic
`c0ffee1` differs from tested candidate `ca11dad` only by the recorded dry-run
evidence and contains no material operational-state change.

## Delta sweep

- **Previous watermark:** 2026-08-30T09:05:00Z
- **Sweep completed at:** 2026-09-01T09:35:00Z
- **Operator:** synthetic incumbent agent supervised by Dr. Rivera

| Volatile surface | Check performed | Checked by/at | Evidence | Change since watermark | Canonical update |
| --- | --- | --- | --- | --- | --- |
| Git/dirty state | branch/status check | operator / 09:10Z | R-001, `EV-GIT-02` | none | R-001 |
| Recent conversations | SRC-001 delta listing | operator / 09:30Z | `EV-CONV-02` | D-003 proposed | STATE, D-003 |
| Jobs | SRC-003 queue/accounting/automation inventory | operator / 09:25Z | `EV-JOBS-01` | R-008 evidence expired | R-007, R-008, R-015 |
| Service health | SRC-004 plus P-004 | operator / 09:20Z | `EV-SVC-01` | dashboard unreachable | R-009, R-018 |
| Remote outputs | SRC-005 manifest checks | operator / 09:19Z | R-004/R-005 manifests | v3 QC generated | R-004, R-005 |
| Human decisions | PI candidate, gate-procedure, and residual-risk review | Dr. Rivera / 09:35Z | `EV-DEC-01`, `EV-GATE-01`, `EV-RISK-01`, `EV-CANDIDATE-01` | D-003 still pending; candidate objects, stale-claim dispositions, P-007 mechanics, and CV-009/CV-010 constraints accepted | STATE, D-003, D/R/P authority, MC-001/MC-003/MC-006/CF-001, CV-009/CV-010 |

## Fresh-agent dry run

- **Agent/product:** synthetic clean Codex fixture run
- **Exact prompt:** `Bootstrap from this folder and report current work and risks.`
- **Freshness condition:** no bespoke context; no useful prior chat
- **Started from:** example directory at synthetic candidate commit `ca11dad`
- **Records read:** START, STATE, D-001/D-003/D-004, R-002–R-010,
  R-013–R-016, P-002/P-004/P-007
- **Capture ref:** illustrative sanitized capture `EV-DRY-01`; this fixture field is
  inspectable but not evidence of a real external execution

| Question/task | Expected canonical source | Fresh-agent result | Evidence | Pass? |
| --- | --- | --- | --- | --- |
| Candidate frontier and active work | candidate STATE | S-14 decision; manual R-005 review | `EV-DRY-01` | yes |
| Cutover, current gate, and incumbent boundary | candidate STATE | migration candidate, not cut over; operational cutover was current; incumbent project stayed live workspace and agent stayed operator/witness | `EV-DRY-01` | yes |
| Accepted decisions | D-001, D-004 | did not promote D-003 | `EV-DRY-01` | yes |
| Proposed post-cutover next human gate | candidate STATE, D-003 | Dr. Rivera decides D-003 | `EV-DRY-01` | yes |
| Critical procedure | P-002, P-007 | found exact cutoff and both gate branches | `EV-DRY-01` | yes |
| Remote lineage | R/P chain | R-003 → R-015/P-002 → R-004 → P-003 → R-005 | `EV-DRY-01` | yes |
| Job/service truth | R-007–R-009 | planned; current unknown; last unreachable | `EV-DRY-01` | yes |
| Safe verification | P-002 verification contract and R-004 manifest | ran the read-only v3 manifest validation; checksum/schema/duplicate checks passed | `EV-VERIFY-01` | yes (fixture) |

Discrepancies: none.

## Operational gate

- [x] No operational/critical source is `not-attempted`.
- [x] No operational row is `pending` or `backlog`; no row is `blocked`.
- [x] No forensic row is `pending`; each open item is in the forensic backlog below.
- [x] No unresolved critical unknown permits unsafe continuation.
- [x] Current coordination state and required runbooks are canonical.
- [x] Critical remote resources and lineage are locatable.
- [x] Job/service tenses match time-stamped evidence.
- [x] False-memory conflict CF-001 has an explicit disposition.
- [x] The illustrative delta sweep and fresh-agent fixture have internally consistent
  expected results; real acceptance evidence belongs to the repository-level test run.
- [x] Fixture public-safety check passed with reserved domains and synthetic values.

## Human cutover authority

### Residual non-blocking risks

| Coverage/unknown IDs | Safe constraint | Residual rationale | Accepted by/at |
| --- | --- | --- | --- |
| CV-009, R-018 | use static R-005; do not invent dashboard restart | dashboard is optional | Dr. Rivera / 2026-09-01T09:35Z (`EV-RISK-01`) |
| CV-010, U-003, R-008, R-012, R-017 | never rerun; consume only after fresh P-004 terminal success, output validation, and explicit human forensic approval; never use for v3 | legacy sensitivity work does not control v3 | Dr. Rivera / 2026-09-01T09:35Z (`EV-RISK-01`) |

### Forensic backlog

| Coverage/unknown IDs | Value/reason | Owner | Next action | Recheck condition |
| --- | --- | --- | --- | --- |
| CV-002, U-001 | preserve pilot-threshold rationale if republishing pilot | Dr. Rivera | retry archive only when needed | archive access returns or pilot republication |
| CV-013, U-002 | preserve honest discovery limit | Dr. Rivera | reclassify if a current dependency appears | new discovery access or missing operational rationale |

### Decision

- **Decision:** approved for the synthetic fixture
- **Authorized human:** Dr. Rivera (fictional)
- **Decision at:** 2026-09-01T09:45:00Z
- **Reviewed state:** synthetic pre-cutover commit `c0ffee1`
- **Cutover tag:** synthetic `relay-cutover-2026-09-01-coastwatch`

The fictional cutover tag identifies the decision boundary without embedding a
self-referential commit hash.
