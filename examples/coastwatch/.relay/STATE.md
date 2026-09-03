# Current state

Snapshot boundary: 2026-09-01T09:45:00Z (synthetic fixture).
Migration basis:
[MC-007](migration/AUDIT.md#mc-007--s-14-exclusion-remains-a-proposal-pending-pi-disposition)
and synthetic cutover tag `relay-cutover-2026-09-01-coastwatch`.

- **Frontier:** decide whether sensor S-14 should be excluded before freezing the
  v3 salinity normalization result.
- **Active work:** human review of [R-005 QC report](RECORDS.md#r-005--v3-qc-report).
- **Next human gate:** Dr. Rivera accepts or rejects
  [D-003](DECISIONS.md#d-003--exclude-sensor-s-14-from-v3).

## Accepted governing decisions

- [D-001](DECISIONS.md#d-001--raw-observations-are-immutable) — raw observations are immutable.
- [D-004](DECISIONS.md#d-004--use-calibration-registry-v3) — use calibration registry v3.

## Provisional choices requiring review

- [D-003](DECISIONS.md#d-003--exclude-sensor-s-14-from-v3) — proposed S-14 exclusion.

## Urgent blockers and unknowns

- No operational blocker prevents manual QC review.
- [R-011](RECORDS.md#r-011--pilot-threshold-rationale) is an inaccessible forensic
  rationale; it does not control v3 normalization.
- [R-008](RECORDS.md#r-008--legacy-sensitivity-job) and R-012 remain unusable; follow
  R-008's owning record for every forensic-use gate.

## Background execution

No job has evidence fresh enough to be called queued/running, and no service has
evidence fresh enough to be called running/healthy. Follow R-007 through R-009 and
P-004 for the owning observations and verification steps.
