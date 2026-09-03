# Migration audit — 2026-09-01-coastwatch

This is a frozen synthetic dossier. Ongoing truth lives in D/R/P records. Named
`EV-*` captures resolve in the [sanitized evidence registry](../evidence/README.md).

## Dossier map

- [AUDIT](AUDIT.md) owns sources, claims, conflicts, unknowns, and normalization.
- [COVERAGE](COVERAGE.md) owns the source denominator and per-surface disposition.
- [CUTOVER](CUTOVER.md) owns the delta sweep, candidate dry run, gate, and fictional
  human transition decision.

## Run boundary

- **Migration ID:** `2026-09-01-coastwatch`
- **Incumbent project/product:** synthetic Claude Code project
- **Operator:** incumbent synthetic agent supervised by Dr. Rivera
- **Started at:** 2026-08-30T09:00:00Z
- **Audit horizon:** active v3 project plus discoverable pilot history since 2026-05-01
- **Source Git state:** R-001 `analysis-v3@a1b2c3d`, clean at initial watermark
- **Initial watermark:** 2026-08-30T09:05:00Z
- **Target workspace:** this example directory

## Source notes

### SRC-001 — Incumbent conversation inventory

- **Coverage rows:** CV-001, CV-002, CV-013
- **Scope actually inspected:** native project listing from 2026-05-01 through the
  watermark; one active v3 thread opened; one named pilot archive denied; product
  could not enumerate deleted threads
- **Inspection method:** synthetic project-thread listing and per-thread open
- **Observed at:** 2026-08-30T09:35:00Z
- **Evidence/output refs:** sanitized inventory `EV-CONV-01`; no transcript copied
- **Limitations:** deleted/undiscoverable history has no count; see U-002

### SRC-002 — Instructions, memory, and connector inventory

- **Coverage rows:** CV-003, CV-004
- **Scope actually inspected:** project instructions, all listed auto-memory topics,
  and the complete incumbent settings inventory for MCPs/connectors
- **Inspection method:** synthetic memory/config/connector listings plus file reads
- **Observed at:** 2026-08-31T14:30:00Z
- **Evidence/output refs:** sanitized inventory `EV-MEM-01`
- **Limitations:** memory is witness material, not authority

### SRC-003 — Scheduler and tool inventory

- **Coverage rows:** CV-005, CV-010
- **Scope actually inspected:** account `coastwatch-analysis`; live queue plus accounting
  since 2026-05-01; scheduler entries, listed automations, and CLI versions/config
- **Inspection method:** synthetic `squeue`, `sacct`, scheduler/automation listing,
  and the exact per-surface executable/version checks in EV-TOOLS-01
- **Observed at:** 2026-09-01T09:25:00Z
- **Evidence/output refs:** sanitized inventories `EV-JOBS-01`, `EV-TOOLS-01`
- **Limitations:** R-008 evidence expired after observation; exact legacy command absent

### SRC-004 — Service inventory

- **Coverage row:** CV-009
- **Scope actually inspected:** `coastwatch-*` systemd units, container list, and the
  project endpoint registry on R-002
- **Inspection method:** synthetic unit/container listing plus P-004 health check
- **Observed at:** 2026-09-01T09:20:00Z
- **Evidence/output refs:** sanitized inventory `EV-SVC-01`; R-009
- **Limitations:** no verified restart procedure; see R-018

### SRC-005 — Remote topology and artifacts

- **Coverage rows:** CV-007, CV-008
- **Scope actually inspected:** R-002 durable roots and scratch; asset manifests named
  in R-003–R-005 and R-012–R-015
- **Inspection method:** synthetic remote listing, manifest/checksum validation, and
  reader/writer configuration review
- **Observed at:** 2026-09-01T09:19:00Z
- **Evidence/output refs:** sanitized topology `EV-REMOTE-01`; R records
- **Limitations:** none for the v3 operational path

### SRC-006 — Git, dependency, and policy-artifact inventory

- **Coverage rows:** CV-006, CV-008, CV-012
- **Scope actually inspected:** the single R-001 repository/worktree, tracked lockfile,
  referenced policy/preregistration artifacts, and credential classes/config locators
- **Inspection method:** synthetic Git status/revision checks, tracked-file inspection,
  dependency lock review, and secret-reference review without reading secret values
- **Observed at:** 2026-09-01T09:32:00Z
- **Evidence/output refs:** `EV-GIT-02`, `EV-TOOLS-01`, `EV-POLICY-01`, R-010, R-013
- **Limitations:** validates locators and required classes, not any secret value

### SRC-007 — Exact operational runbook sources

- **Coverage row:** CV-011
- **Scope actually inspected:** R-001 at `a1b2c3d`: lockfile/environment notes,
  `scripts/run-normalization-v3.sbatch`, QC command documentation, scheduler/service
  verification notes, recovery instructions, and the two-branch P-007 gate draft;
  the batch pipeline has no separate build, deploy, or maintenance function, while a
  pinned checkout plus P-001 owns its update boundary
- **Inspection method:** field-by-field comparison of source commands, inputs, outputs,
  checks, and recovery text against P-001–P-004; Dr. Rivera tabletop-reviewed P-007
  through MC-008
- **Observed at:** 2026-09-01T09:34:00Z
- **Evidence/output refs:** EV-TEST-01, EV-JOBS-01, EV-SVC-01, EV-GATE-01,
  R-004/R-005 manifests
- **Limitations:** legacy sensitivity and dashboard lifecycle gaps remain R-017/R-018

## Candidate claims

### MC-001 — Current normalization output is under `/derived/v2/`

- **Track:** operational
- **Criticality:** critical
- **Authority:** rejected
- **Provenance:** incumbent-recall
- **Verification:** contradicted
- **Evidence ref:** SRC-002 and EV-MEM-01 recalled statement; CF-001; MC-006 current
  evidence; EV-CANDIDATE-01 disposition
- **Checked at:** 2026-09-01T09:19:00Z
- **Checked by:** synthetic migration operator
- **Scope/limitations:** asserted as current path; does not deny historical v2 output
- **Conflict/unknown:** CF-001
- **Destination:** reject; retain as conflict evidence only
- **Disposition:** rejected
- **Authority disposition by/at:** rejected by Dr. Rivera / 2026-09-01T09:35:00Z

### MC-002 — Calibration must be selected before normalization starts

- **Track:** operational
- **Criticality:** critical
- **Authority:** accepted
- **Provenance:** incumbent-recall + durable-artifact + human-report
- **Verification:** verified
- **Evidence ref:** SRC-001; `config/calibration.yml@a1b2c3d`; R-015 manifest
- **Checked at:** 2026-08-30T14:10:00Z
- **Checked by:** synthetic migration operator and Dr. Rivera
- **Scope/limitations:** v3 normalization only
- **Conflict/unknown:** none
- **Destination:** P-002; corroborates pre-existing D-004
- **Disposition:** canonicalized
- **Authority disposition by/at:** accepted by Dr. Rivera / 2026-08-30T15:00:00Z

### MC-003 — Legacy job 88421 is still running

- **Track:** operational
- **Criticality:** supporting
- **Authority:** rejected
- **Provenance:** incumbent-recall
- **Verification:** stale
- **Evidence ref:** SRC-002/EV-MEM-01 recalled assertion; SRC-003/EV-JOBS-01
  stale check; EV-CANDIDATE-01 disposition
- **Checked at:** 2026-09-01T09:25:00Z
- **Checked by:** synthetic migration operator
- **Scope/limitations:** unjustified present-tense assertion
- **Conflict/unknown:** U-003
- **Destination:** audit evidence only; do not promote
- **Disposition:** retained-evidence
- **Authority disposition by/at:** rejected by Dr. Rivera / 2026-09-01T09:35:00Z

### MC-004 — Job 88421 was observed running at 2026-08-31T14:22:00Z

- **Track:** operational
- **Criticality:** supporting
- **Authority:** provisional
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** SRC-003 sanitized queue capture `EV-JOBS-01`
- **Checked at:** 2026-08-31T14:22:00Z
- **Checked by:** synthetic migration operator
- **Scope/limitations:** historical observation valid only until 14:37Z
- **Conflict/unknown:** none
- **Destination:** R-008 historical observation
- **Disposition:** canonicalized
- **Authority disposition by/at:** remains provisional; reviewed by analysis team / 2026-09-01T09:25:00Z

### MC-005 — Current state of job 88421 is unknown after evidence expiry

- **Track:** operational
- **Criticality:** supporting
- **Authority:** provisional
- **Provenance:** inference
- **Verification:** verified
- **Evidence ref:** MC-004 freshness rule plus EV-JOBS-01 live-queue and accounting
  no-row result
- **Checked at:** 2026-09-01T09:25:00Z
- **Checked by:** synthetic migration operator
- **Scope/limitations:** current-state report only; does not negate MC-004 history
- **Conflict/unknown:** U-003
- **Destination:** R-008 current-state constraint
- **Disposition:** canonicalized
- **Authority disposition by/at:** remains provisional; reviewed by analysis team / 2026-09-01T09:25:00Z

### MC-006 — v3 is the current normalization output family

- **Track:** operational
- **Criticality:** critical
- **Authority:** accepted
- **Provenance:** live-environment + durable-artifact + human-report
- **Verification:** verified
- **Evidence ref:** R-001 config, R-004 manifest, D-004, SRC-005;
  EV-CANDIDATE-01 disposition
- **Checked at:** 2026-09-01T09:19:00Z
- **Checked by:** synthetic migration operator and Dr. Rivera
- **Scope/limitations:** current v3 analysis; v2 remains historical only
- **Conflict/unknown:** CF-001
- **Destination:** D-004 and R-004
- **Disposition:** canonicalized
- **Authority disposition by/at:** accepted by Dr. Rivera / 2026-09-01T09:35:00Z

### MC-007 — S-14 exclusion remains a proposal pending PI disposition

- **Track:** operational
- **Criticality:** critical
- **Authority:** provisional
- **Provenance:** durable-artifact + human-report
- **Verification:** verified
- **Evidence ref:** `EV-CONV-02`, `EV-DEC-01`, D-003, R-005, R-013, R-014
- **Checked at:** 2026-09-01T09:35:00Z
- **Checked by:** synthetic migration operator and Dr. Rivera
- **Scope/limitations:** verifies proposal/gate state only, not the scientific outcome
- **Conflict/unknown:** none
- **Destination:** STATE, D-003, and planned R-007
- **Disposition:** canonicalized
- **Authority disposition by/at:** remains provisional; reviewed by Dr. Rivera / 2026-09-01T09:35:00Z

### MC-008 — P-007 is the accepted two-branch S-14 gate procedure

- **Track:** operational
- **Criticality:** critical
- **Authority:** accepted
- **Provenance:** durable-artifact + human-report
- **Verification:** verified
- **Evidence ref:** SRC-007/EV-GATE-01 tabletop capture
- **Checked at:** 2026-09-01T09:34:00Z
- **Checked by:** synthetic migration operator and Dr. Rivera
- **Scope/limitations:** governs closure mechanics; it does not pre-decide D-003
- **Conflict/unknown:** none
- **Destination:** P-007
- **Disposition:** canonicalized
- **Authority disposition by/at:** accepted by Dr. Rivera / 2026-09-01T09:34:00Z

### MC-009 — Raw observations remain immutable under the accepted data policy

- **Track:** operational
- **Criticality:** critical
- **Authority:** accepted
- **Provenance:** durable-artifact + human-report
- **Verification:** verified
- **Evidence ref:** SRC-006/EV-POLICY-01 and synthetic policy `POL-DATA-02`
- **Checked at:** 2026-09-01T09:32:00Z
- **Checked by:** synthetic migration operator
- **Scope/limitations:** R-003 sensor exports and R-014 maintenance log under the raw
  source root; derived outputs are versioned
- **Conflict/unknown:** none
- **Destination:** D-001
- **Disposition:** canonicalized
- **Authority disposition by/at:** accepted by Dr. Rivera / 2026-06-12T15:00:00Z

## Conflict log

### CF-001 — Remembered v2 path conflicts with current v3 configuration

- **Claims/evidence in conflict:** MC-001 versus MC-006
- **Operational impact:** a fresh agent could read or overwrite the wrong result family
- **Freshest checkable evidence:** R-004 at 2026-09-01T09:18:00Z
- **Accepted intent affected:** D-004 confirms v3; no unresolved drift
- **Safe interim constraint:** treat R-012 as legacy and read-only
- **Disposition:** MC-001 rejected; MC-006 canonicalized; history retained
- **Resolved by/at:** Dr. Rivera / 2026-09-01T09:35:00Z
- **Resolution evidence:** EV-CANDIDATE-01
- **Resulting canonical record:** D-002, D-004, R-004, R-012

## Blind spots

### U-001 — Archived pilot-threshold thread inaccessible

- **Coverage row:** CV-002
- **Attempts/evidence:** SRC-001 listing showed the archive; open returned denied
- **Why unknown:** archive permission unavailable during migration
- **Operational consequence:** none; D-004 and v3 procedures do not use the threshold
- **Classification rationale:** only R-012 pilot history depends on it; CV-002 owns
  the resulting track/criticality values
- **Safe constraint/workaround:** never apply the pilot threshold to v3
- **Owner:** Dr. Rivera
- **Next action:** revisit only if pilot results need republication
- **Recheck condition:** archive access returns

### U-002 — Deleted or undiscoverable conversation history

- **Coverage row:** CV-013
- **Attempts/evidence:** SRC-001 used the complete product-provided listing and found
  no API/UI that enumerates deleted threads
- **Why unknown:** the product cannot prove what was deleted before the audit horizon
- **Operational consequence:** no known active record depends on an unlocated thread;
  all active surfaces were corroborated independently
- **Classification rationale:** dependency and open-loop review found no current
  consumer; CV-013 owns the resulting track/criticality values
- **Safe constraint/workaround:** reclassify as operational if a current record later
  references missing rationale or a procedure that cannot be reproduced
- **Owner:** Dr. Rivera
- **Next action:** retain the limitation in forensic coverage
- **Recheck condition:** new archive/discovery access or a missing operational dependency

### U-003 — Legacy sensitivity job terminal state and command unresolved

- **Coverage row:** CV-010
- **Attempts/evidence:** EV-JOBS-01 queried the live queue and retained accounting for
  job `88421`; neither returned a row, while the old running capture had expired;
  SRC-003 found no complete submission script
- **Why unknown:** queue absence proves neither success nor failure, and the exact
  legacy invocation is unavailable
- **Operational consequence:** none for v3; R-012 remains unusable for current work
- **Classification rationale:** it is a named real job, but its only output family is
  superseded; CV-010 owns the resulting track/criticality values
- **Safe constraint/workaround:** never rerun R-008. Do not consume R-012 unless P-004
  obtains a fresh terminal `succeeded` result, the output is independently validated,
  and Dr. Rivera explicitly approves forensic use; it can never support current v3
- **Owner:** analysis team
- **Next action:** recover the submission script and run the forensic-use gate only if
  pilot forensics become valuable
- **Recheck condition:** scheduler history, complete logs, or submission script becomes available

## Normalization ledger

| Candidate | Destination ID | Owning file | Exact claim promoted | Residual limitation | Reviewer |
| --- | --- | --- | --- | --- | --- |
| MC-002 | P-002; corroborates D-004 | `PROCEDURES.md`, `DECISIONS.md` | calibration selected before v3 normalization | none | Dr. Rivera |
| MC-004 | R-008 | `RECORDS.md` | running observation at exact historical time | evidence later expired | analysis team |
| MC-005 | R-008 | `RECORDS.md` | current state unknown after expiry | requires P-004 recheck | analysis team |
| MC-006 | D-004, R-004 | `DECISIONS.md`, `RECORDS.md` | v3 is current output family | D-003 gate still pending | Dr. Rivera |
| MC-007 | STATE, D-003, R-007 | `STATE.md`, `DECISIONS.md`, `RECORDS.md` | exclusion is proposed and gated | scientific outcome pending | Dr. Rivera |
| MC-008 | P-007 | `PROCEDURES.md` | exact accepted two-branch gate procedure | does not decide D-003 | Dr. Rivera |
| MC-009 | D-001 | `DECISIONS.md` | immutable raw-data policy | derived assets remain versioned | Dr. Rivera |

MC-001 and MC-003 were not promoted as asserted. They remain frozen evidence of the
false-memory and stale-tense failure modes.
