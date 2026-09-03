# Migration audit — 2026-09-01-coastwatch

This is a frozen synthetic dossier. Ongoing truth lives in D/R/P records.

## Run boundary

- **Migration ID:** `2026-09-01-coastwatch`
- **Incumbent project/product:** synthetic Claude Code project
- **Operator:** incumbent synthetic agent supervised by Dr. Rivera
- **Started at:** 2026-08-30T09:00:00Z
- **Audit horizon:** active v3 project plus discoverable pilot history since 2026-05-01
- **Source Git state:** R-001 `analysis-v3@a1b2c3d`, clean at initial watermark
- **Initial watermark:** 2026-08-30T09:05:00Z
- **Target workspace:** this example directory

## Candidate claims

### MC-001 — Current normalization output is under `/derived/v2/`

- **Track/impact:** operational / blocker if accepted
- **Authority:** provisional
- **Provenance:** incumbent-recall
- **Verification:** contradicted
- **Evidence ref:** CF-001; live config and R-004 show `/derived/v3/`
- **Checked at:** 2026-08-30T10:20:00Z
- **Destination/disposition:** rejected as current; historical R-012 retained

### MC-002 — Calibration must be selected before normalization starts

- **Track/impact:** operational / blocker
- **Authority:** accepted
- **Provenance:** incumbent-recall + durable-artifact + human-report
- **Verification:** verified
- **Evidence ref:** accessible thread CV-001, `config/calibration.yml@a1b2c3d`, synthetic
  dry-run manifest, Dr. Rivera acceptance
- **Checked at:** 2026-08-30T14:10:00Z
- **Destination/disposition:** canonicalized as D-004 and P-002
- **Accepted by/at:** Dr. Rivera / 2026-08-30T15:00:00Z

### MC-003 — Legacy job 88421 is still running

- **Track/impact:** operational / supporting
- **Authority:** provisional
- **Provenance:** incumbent-recall + durable-artifact
- **Verification:** stale
- **Evidence ref:** R-008 observation expired at 2026-08-31T14:37:00Z
- **Checked at:** 2026-08-31T14:22:00Z
- **Destination/disposition:** R-008 says last observed running, current unknown

## Conflict log

### CF-001 — Remembered v2 path conflicts with current v3 configuration

- **Claims/evidence in conflict:** MC-001 versus R-001 config and live R-004
- **Operational impact:** a fresh agent could read or overwrite the wrong result family
- **Freshest checkable evidence:** R-004 at 2026-09-01T09:18:00Z
- **Accepted intent affected:** D-004 confirms v3; no unresolved drift
- **Safe interim constraint:** treat R-012 as legacy and read-only
- **Disposition:** current observation chosen; old claim retained as contradicted history
- **Resolved by/at:** Dr. Rivera / 2026-08-30T15:00:00Z
- **Resulting canonical record:** D-002, D-004, R-004, R-012

## Blind spots

### U-001 — Archived pilot-threshold thread inaccessible

- **Coverage row:** CV-002
- **Attempts/evidence:** incumbent listing showed the archive entry; open returned denied
- **Why unknown:** archive permission unavailable during migration
- **Track/impact:** forensic / supporting
- **Operational consequence:** none; D-004 and v3 procedures do not use the threshold
- **Safe constraint/workaround:** never apply the pilot threshold to v3
- **Owner:** Dr. Rivera
- **Next action/recheck:** revisit only if pilot results are republished or access returns
- **Disposition:** forensic backlog, represented by R-011

## Normalization ledger

| Candidate | Destination ID | Owning file | Fields promoted | Residual limitation | Reviewer |
| --- | --- | --- | --- | --- | --- |
| MC-001 | R-004, R-012, D-002 | `RECORDS.md`, `DECISIONS.md` | current versus legacy path | pilot completion unknown | Dr. Rivera |
| MC-002 | D-004, P-002 | `DECISIONS.md`, `PROCEDURES.md` | calibration order and exact procedure | none | Dr. Rivera |
| MC-003 | R-008 | `RECORDS.md` | last observation and expiry | current job state unknown | analysis team |

