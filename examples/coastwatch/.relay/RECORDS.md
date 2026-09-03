# Records registry

All records and evidence below are synthetic fixture data. `SRC`/`MC`/`CF`/`U`
provenance resolves in [AUDIT](migration/AUDIT.md), `CV` denominator state in
[COVERAGE](migration/COVERAGE.md), and sanitized captures in the
[evidence registry](evidence/README.md).

## R-001 — Analysis repository

- **Kind:** repository
- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Purpose/claim:** source for v3 normalization and QC
- **Locator:** `https://git.coastwatch.example/pipeline.git`
- **Role:** source
- **Important contents:** v3 configuration, normalization/QC code, tests, and service config
- **Status or last observation:** branch `analysis-v3` at synthetic commit `a1b2c3d`
- **Evidence ref:** synthetic `git -C /srv/coastwatch/src/pipeline rev-parse HEAD`
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:10:00Z
- **Migration provenance:** SRC-006 and EV-GIT-02
- **Valid until / recheck rule:** recheck after branch change
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Owner:** data engineering
- **Inputs / outputs / dependencies:** R-003; produces R-004 and R-005 through P-002/P-003
- **Producer/version:** Git history; recorded execution revision `a1b2c3d`
- **Readers/writers:** P-001/P-002/P-003 read; data engineering writes through Git
- **Access/secret ref:** synthetic HTTPS clone; no credential required in this fixture
- **Risks/limitations:** working tree must be checked before reruns

## R-002 — Compute host

- **Kind:** host
- **Authority:** accepted
- **Provenance:** live-environment
- **Verification:** verified
- **Purpose/claim:** Slurm execution and canonical research-data storage
- **Locator/access:** SSH alias `compute.coastwatch.example`; credential via R-010
- **Important topology:** see the per-root table below
- **Status or last observation:** reachable
- **Evidence ref:** migration `EV-REMOTE-01` and synthetic `ssh ... hostname` result
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:19:00Z
- **Migration provenance:** SRC-005 and EV-REMOTE-01
- **Valid until / recheck rule:** recheck before remote mutation
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Owner:** research computing
- **Inputs / outputs / dependencies:** R-006 and R-010
- **Risks/limitations:** never commit the real SSH configuration or key

| Root | Role/key contents | Inputs and outputs | Producer/lifecycle | Readers/writers | Access |
| --- | --- | --- | --- | --- | --- |
| `/srv/coastwatch/src/pipeline` | source checkout for R-001 | remote Git → checked-out code → P-001/P-002/P-003 | Git clone/update; pin `a1b2c3d` for the recorded run | procedures read; data engineering writes through Git | SSH to R-002 via R-010 |
| `/srv/coastwatch/raw` | canonical immutable acquisitions, including R-003/R-014 | acquisition service → manifests/CSV → P-002/P-007 | acquisition release `2026.8`; immutable under D-001 | field operations writes; P-002/P-007 read | SSH to R-002 via R-010 |
| `/srv/coastwatch/derived` | immutable run-scoped R-004/R-005 assets plus legacy R-012 | raw/config/code → validated sealed run → run-scoped QC | P-002/P-003; a new run creates successor records and never overwrites a prior run | analysis procedures write new run paths; analysts/R-009 read | SSH to R-002 via R-010 |
| `/srv/coastwatch/logs` | scheduler and service evidence | R-006/R-009 → timestamped logs | scheduler/service runtime; synthetic 90-day retention policy | runtimes write; P-004 and operators read | SSH to R-002 via R-010 |
| `/scratch/coastwatch` | disposable job scratch | job-local input shards → temporary intermediates | jobs create; synthetic seven-day purge; never canonical | jobs read/write; operators troubleshoot | SSH to R-002 via R-010 |

## R-003 — August raw sensor export

- **Kind:** asset
- **Authority:** accepted
- **Provenance:** live-environment
- **Verification:** verified
- **Purpose/claim:** immutable raw input for the v3 analysis
- **Locator:** `compute.coastwatch.example:/srv/coastwatch/raw/2026-08/`
- **Role:** canonical
- **Important contents:** daily CSV exports plus acquisition manifest
- **Status or last observation:** 31 daily partitions; declared synthetic logical size
  3.2 TiB; manifest checksum set present
- **Evidence ref:** synthetic remote listing and checksum verification
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:19:00Z
- **Migration provenance:** SRC-005 and EV-REMOTE-01
- **Valid until / recheck rule:** immutable policy D-001; recheck checksum before rerun
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Owner:** field operations
- **Inputs / outputs / dependencies:** source input; read by P-002; produces R-004
- **Producer/version:** acquisition service release `2026.8`, run IDs in manifest
- **Readers/writers:** acquisition service and field operations write; P-002 reads
- **Access/secret ref:** R-002 via R-010
- **Risks/limitations:** dataset remains remote; no bulk copy belongs in Relay

## R-004 — v3 normalized salinity table

- **Kind:** asset
- **Authority:** provisional
- **Provenance:** live-environment
- **Verification:** verified
- **Purpose/claim:** current derived table awaiting S-14 disposition
- **Locator:** `compute.coastwatch.example:/srv/coastwatch/derived/v3/runs/RUN-20260830-001/salinity.parquet`
- **Role:** derived
- **Status or last observation:** present; input checksums match R-003, duplicate-key
  count is zero, row count is 2,678,400, and schema hash is synthetic
  `sha256:73ab91f073ab91f073ab91f073ab91f073ab91f073ab91f073ab91f073ab91f0`
- **Evidence ref:** `/srv/coastwatch/derived/v3/runs/RUN-20260830-001/manifest.json`
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:18:00Z
- **Migration provenance:**
  [MC-006](migration/AUDIT.md#mc-006--v3-is-the-current-normalization-output-family)
  and SRC-005
- **Valid until / recheck rule:** sealed artifact evidence is immutable; recheck only
  its `current candidate` role after D-003 disposition or explicit successor selection
- **Owner:** analysis team
- **Inputs / outputs / dependencies:** input R-003; P-002; R-001 at `a1b2c3d`; feeds R-005
- **Producer/version:** R-015, calibration v3, R-001 `a1b2c3d`
- **Readers/writers:** P-002 writes; P-003 and optional R-009 read
- **Access/secret ref:** R-002 via R-010
- **Risks/limitations:** not final until the next human gate closes

## R-005 — v3 QC report

- **Kind:** asset
- **Authority:** provisional
- **Provenance:** durable-artifact
- **Verification:** verified
- **Purpose/claim:** PI-facing diagnostics for D-003
- **Locator:** `compute.coastwatch.example:/srv/coastwatch/derived/v3/qc/RUN-20260830-001/report.html`
- **Role:** derived
- **Status or last observation:** generated and checksum-matched to the review copy
- **Evidence ref:** `/srv/coastwatch/derived/v3/qc/RUN-20260830-001/manifest.json`; synthetic report
  checksum `sha256:4c910a2e4c910a2e4c910a2e4c910a2e4c910a2e4c910a2e4c910a2e4c910a2e`
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:19:00Z
- **Migration provenance:** SRC-005 and EV-REMOTE-01
- **Valid until / recheck rule:** valid for the exact R-004 checksum; a newly selected
  normalization asset requires a successor QC record
- **Owner:** analysis team
- **Inputs / outputs / dependencies:** input R-004; generated by P-003 at `a1b2c3d`
- **Producer/version:** P-003 at R-001 `a1b2c3d`; manifest links R-004 checksum
- **Readers/writers:** P-003 writes; Dr. Rivera and optional R-009 read
- **Access/secret ref:** R-002 via R-010
- **Risks/limitations:** section `S-14 drift` requires human interpretation

## R-006 — Slurm scheduler

- **Kind:** tool
- **Authority:** accepted
- **Provenance:** live-environment
- **Verification:** verified
- **Purpose/claim:** required batch execution mechanism on R-002
- **Identity/config:** Slurm fixture; host config `/etc/slurm/slurm.conf`
- **Required/optional:** required for batch P-002; not used by interactive P-001
- **Dependent project functions:** P-002 submission and P-004 job verification
- **Capabilities used:** `sbatch`, `squeue`, `sacct`
- **Status or last observation:** commands available on R-002
- **Evidence ref:** synthetic `sinfo` result
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:25:00Z
- **Migration provenance:** SRC-003 and EV-TOOLS-01
- **Valid until / recheck rule:** recheck on scheduler error
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Owner:** research computing
- **Inputs / outputs / dependencies:** used by P-002 and P-004; auth via R-010
- **Authentication/secret ref:** R-010 SSH access to R-002
- **Replacement/recovery:** research computing owns scheduler recovery; do not emulate
  queue state or resubmit without a fresh scheduler check
- **Risks/limitations:** interactive shell output alone does not prove a named job exists

## R-007 — S-14 exclusion rerun

- **Kind:** job
- **Authority:** provisional
- **Provenance:** human-report + live-environment
- **Verification:** verified
- **Purpose/claim:** proposed rerun after D-003 is decided
- **Status or last observation:** `planned`; not submitted
- **Execution mechanism/host:** R-006 on R-002, if approved
- **Execution ID:** none — therefore this job is neither queued nor running
- **Command/spec ref:** P-002 with exclusion option; working revision R-001 `a1b2c3d`
- **Inputs / outputs / dependencies:** R-003; D-003; would produce run-scoped
  successor records to R-004 and R-005
- **Outputs/logs:** none until submission
- **Submitted/started at:** not applicable
- **Evidence ref:** MC-007 proposal/gate record and EV-JOBS-01 verified absence of an execution
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:25:00Z
- **Migration provenance:**
  [MC-007](migration/AUDIT.md#mc-007--s-14-exclusion-remains-a-proposal-pending-pi-disposition),
  SRC-003, and EV-JOBS-01
- **Valid until / recheck rule:** re-evaluate after D-003 disposition
- **Owner / next human gate:** analysis team / Dr. Rivera decides D-003
- **Risks/limitations:** no execution exists; submitting before D-003 acceptance is forbidden
- **Recovery:** no execution exists to cancel or recover

## R-008 — Legacy sensitivity job

- **Kind:** job
- **Authority:** provisional
- **Provenance:** durable-artifact + inference
- **Verification:** verified
- **Purpose/claim:** optional sensitivity analysis unrelated to the immediate QC gate
- **Status or last observation:** observed `running` at 2026-08-31T14:22:00Z;
  current state `unknown`
- **Execution mechanism/host:** R-006 on R-002
- **Execution ID:** synthetic Slurm job `88421`
- **Command/spec ref:** R-017; exact legacy specification is unknown
- **Inputs / outputs / dependencies:** R-003; writes only to legacy R-012
- **Outputs/logs:** `/srv/coastwatch/logs/slurm-88421.out`
- **Submitted/started at:** 2026-08-31T14:03:00Z
- **Evidence ref:** MC-004 archived queue observation plus MC-005/EV-JOBS-01 live
  queue-and-accounting check
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:25:00Z
- **Migration provenance:**
  [MC-004](migration/AUDIT.md#mc-004--job-88421-was-observed-running-at-2026-08-31t142200z)
  and [MC-005](migration/AUDIT.md#mc-005--current-state-of-job-88421-is-unknown-after-evidence-expiry)
- **Valid until / recheck rule:** the old running evidence expired at
  2026-08-31T14:37:00Z; current state stays unknown until P-004 obtains a fresh matching
  live or terminal scheduler result. Consumption additionally requires terminal
  success and output validation
- **Owner / next human gate:** analysis team / Dr. Rivera approves any forensic use
- **Risks/limitations:** do not claim running or consume output unless P-004 obtains
  fresh terminal success, output validation passes, and Dr. Rivera explicitly approves
  forensic use; never use it for current v3

## R-009 — QC dashboard

- **Kind:** service
- **Authority:** provisional
- **Provenance:** live-environment
- **Verification:** verified
- **Purpose/claim:** optional browser view of R-005
- **Host/runtime/endpoint:** R-002; synthetic container; `https://qc.coastwatch.example/`
- **Desired state:** running during PI review
- **Status or last observation:** unreachable at 2026-09-01T09:20:00Z
- **Source/config:** R-001 `services/qc/`; remote config reference only
- **Lifecycle/deploy procedures:** none verified; gap R-018
- **Health evidence:** synthetic HTTP timeout recorded by P-004
- **Evidence ref:** P-004 synthetic health-check result at the checked time
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:20:00Z
- **Migration provenance:** SRC-004 and EV-SVC-01
- **Valid until / recheck rule:** recheck before dashboard use
- **Dependencies:** R-002, R-005, R-010
- **Logs/persistent state:** `/srv/coastwatch/logs/qc-dashboard/`; no unique persistent state
- **Owner:** analysis team
- **Risks/limitations:** desired state is not observed state; use static R-005 meanwhile

## R-010 — Compute SSH credential reference

- **Kind:** secret-ref
- **Authority:** accepted
- **Provenance:** human-report
- **Verification:** verified
- **Purpose/claim:** authorized access to R-002
- **Secret class:** SSH private key and host configuration
- **Configuration/acquisition ref:** organization secret manager item `coastwatch/hpc-ssh`;
  access granted by research computing
- **Status or last observation:** reference confirmed; no value inspected or stored
- **Evidence ref:** synthetic onboarding procedure
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-08-30T11:00:00Z
- **Migration provenance:** SRC-006 dependency and secret-reference review
- **Valid until / recheck rule:** follow organization rotation policy
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Owner:** research computing
- **Inputs / outputs / dependencies:** enables R-002 access for P-001–P-004 and P-007;
  outputs only authorization, never a secret value
- **Risks/limitations:** secret values never belong in Git or Relay Markdown

## R-011 — Pilot threshold rationale

- **Kind:** unknown
- **Authority:** unresolved
- **Provenance:** unknown
- **Verification:** inaccessible
- **Purpose/claim:** rationale for a pilot-only alert threshold may exist in an
  inaccessible archived native-agent thread
- **Status or last observation:** unknown; explicitly not governing v3
- **Evidence ref:** migration coverage CV-002 and blind spot U-001
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T08:40:00Z
- **Migration provenance:** U-001 and CV-002
- **Valid until / recheck rule:** recheck if archive access is restored
- **Owner:** Dr. Rivera
- **Operational impact:** none for v3; only historical R-012 rationale is missing
- **Safe constraint/workaround:** never apply the pilot threshold to v3
- **Next action:** retry archive access only if pilot results need republication
- **Inputs / outputs / dependencies:** historical R-012 only; no v3 dependency
- **Risks/limitations:** forensic gap, not an operational cutover blocker

## R-012 — Pilot v2 sensitivity output

- **Kind:** asset
- **Authority:** superseded
- **Provenance:** durable-artifact
- **Verification:** stale
- **Purpose/claim:** historical output governed by D-002
- **Locator:** `compute.coastwatch.example:/srv/coastwatch/derived/v2/sensitivity/`
- **Role:** legacy
- **Status or last observation:** partial files observed by EV-REMOTE-01 at
  2026-09-01T09:19:00Z; producer terminal state unknown after EV-JOBS-01 at
  2026-09-01T09:25:00Z
- **Evidence ref:** EV-REMOTE-01 for files; R-008/EV-JOBS-01 for producer state
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:25:00Z
- **Migration provenance:**
  [CF-001](migration/AUDIT.md#cf-001--remembered-v2-path-conflicts-with-current-v3-configuration)
  and SRC-005
- **Superseded by:** R-004 for the current output family; retained as non-equivalent
  pilot history
- **Valid until / recheck rule:** unusable unless P-004 obtains fresh terminal
  `succeeded`, output validation passes, and Dr. Rivera explicitly approves forensic use
- **Owner:** analysis team
- **Inputs / outputs / dependencies:** R-003, D-002, R-008
- **Producer/version:** R-008 at an unrecovered legacy revision; exact procedure is R-017
- **Readers/writers:** no current writer or authorized operational reader; forensic inspection only
- **Access/secret ref:** R-002 via R-010
- **Risks/limitations:** not a current result and must never be substituted for R-004;
  absent every forensic-use gate above, do not consume it

## R-013 — Preregistered sensor-drift tolerance

- **Kind:** asset
- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Purpose/claim:** defines the drift tolerance used to evaluate D-003
- **Locator:** R-001 `docs/preregistration.md` at `a1b2c3d`, section `Sensor exclusion`
- **Role:** source
- **Status or last observation:** threshold text matches the signed review record
- **Evidence ref:** synthetic signed protocol manifest `POL-ANALYSIS-03`
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T08:50:00Z
- **Migration provenance:** SRC-005 remote-artifact inspection
- **Valid until / recheck rule:** immutable for the v3 decision
- **Accepted by/at:** Dr. Rivera / 2026-06-12T15:00:00Z
- **Owner:** study lead
- **Inputs / outputs / dependencies:** informs D-003; read by P-007
- **Producer/version:** signed preregistration `POL-ANALYSIS-03` in R-001 at `a1b2c3d`
- **Readers/writers:** study lead writes under sign-off; P-007 reads
- **Access/secret ref:** R-001 checkout; no secret required for the fixture
- **Risks/limitations:** applies only to the v3 preregistered analysis

## R-014 — S-14 maintenance log

- **Kind:** asset
- **Authority:** accepted
- **Provenance:** live-environment
- **Verification:** verified
- **Purpose/claim:** records the reference-probe service event relevant to D-003
- **Locator:** `compute.coastwatch.example:/srv/coastwatch/raw/maintenance/S-14.csv`
- **Role:** source
- **Status or last observation:** service event recorded at 2026-08-17T00:00:00Z
- **Evidence ref:** synthetic remote checksum and field-operations signature
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T08:52:00Z
- **Migration provenance:** SRC-005 remote-artifact inspection
- **Valid until / recheck rule:** recheck checksum if source changes unexpectedly
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Owner:** field operations
- **Inputs / outputs / dependencies:** informs D-003 and P-007
- **Producer/version:** field-operations acquisition log, signed synthetic export
- **Readers/writers:** field operations writes; P-007 reads
- **Access/secret ref:** R-002 via R-010
- **Risks/limitations:** establishes service timing, not the scientific disposition

## R-015 — v3 normalization job

- **Kind:** job
- **Authority:** accepted
- **Provenance:** live-environment + durable-artifact
- **Verification:** verified
- **Purpose/claim:** batch run that produced the current R-004 candidate
- **Status or last observation:** `succeeded` at 2026-08-30T14:03:00Z; output validated
- **Execution mechanism/host:** R-006 on R-002
- **Execution ID:** synthetic Slurm job `88204`
- **Raw submission reference:** synthetic `88204;coastwatch-cluster`
- **Command/spec ref:** P-002 at R-001 `a1b2c3d`, submitted with
  `RUN_ID=RUN-20260830-001`, `RUN_MODE=standard`, and
  `EXCLUDE_S14_AFTER` explicitly empty (no cutoff value)
- **Inputs / outputs / dependencies:** R-003 and D-004; produced R-004
- **Outputs/logs:** `/srv/coastwatch/logs/slurm-88204.out`; sealed run-scoped R-004
  and its manifest
- **Submitted/started at:** 2026-08-30T13:40:00Z / 2026-08-30T13:41:00Z
- **Evidence ref:** synthetic `sacct` terminal record plus R-004 manifest validation
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:25:00Z
- **Migration provenance:** SRC-003 scheduler inventory and SRC-005 artifact inspection
- **Valid until / recheck rule:** terminal observation is historical; revalidate R-004
  manifest before use
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Owner / next human gate:** analysis team / D-003 disposition
- **Access/secret ref:** R-002/R-006 via R-010
- **Risks/limitations:** historical success does not authorize reuse after inputs or code change
- **Recovery:** P-002 stages a new run; never mutate this historical execution record

## R-016 — Required execution CLI toolchain

- **Kind:** tool
- **Authority:** accepted
- **Provenance:** live-environment + durable-artifact
- **Verification:** verified
- **Purpose/claim:** required tools at each execution surface for setup, batch work,
  report generation, and safe remote checks
- **Identity/config:** exact synthetic placement is listed below; Python dependency
  pins live in the R-001 lockfile and SSH host config is referenced through R-010
- **Required/optional:** required for P-001–P-004 and P-007
- **Dependent project functions:** environment/test, normalization, QC, scheduler
  inspection, artifact verification, and service health
- **Capabilities used:** strict Bash contract, pinned Git checkout, locked `uv`
  execution, unique-path filesystem operations, Slurm submission and inspection, SSH
  transport, and HTTPS health checks
- **Status or last observation:** every named executable was observed at its stated
  surface and locator at 2026-09-01T09:25:00Z
- **Evidence ref:** migration `EV-TOOLS-01`
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:25:00Z
- **Valid until / recheck rule:** recheck after host or lockfile change
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Owner:** data engineering
- **Inputs / outputs / dependencies:** R-001 lockfile, R-002/R-006, R-010; supports
  P-001–P-004 and P-007
- **Authentication/secret ref:** SSH only, through R-010; uv and curl use no project secret
- **Replacement/recovery:** install organization-supported versions, rerun P-001, and
  stop before remote work if host-key or TLS verification fails
- **Migration provenance:** SRC-003 tool inventory
- **Risks/limitations:** version presence does not prove host, credential, or remote health

| Tool | Execution surface and safe locator | Observed version/capability | Consumers |
| --- | --- | --- | --- |
| Bash | R-002 `/bin/bash` | 3.2-or-newer; `set -euo pipefail` | P-001–P-003, P-007 |
| Bash | authorized operator shell `/bin/bash` | 3.2-or-newer; ID validation | P-004 |
| Git | R-002 `/usr/bin/git` | synthetic 2.x; clone/detached revision verification | P-001 |
| uv | R-002 `/opt/coastwatch/bin/uv` | synthetic 0.8.x; locked sync/run | P-001–P-003, P-007 |
| Slurm CLI | R-002 `/usr/bin/{sbatch,sinfo,squeue,sacct}` | explicit export allowlist and job/accounting queries | P-002, P-004 |
| Filesystem CLI | R-002 `/bin/mkdir`, `/bin/mv` | unique-directory creation and atomic rename | P-002, P-003 |
| OpenSSH | authorized operator shell `/usr/bin/ssh` | synthetic 9.x; R-010 host config | P-001–P-004, P-007 |
| curl | authorized operator shell `/usr/bin/curl` | synthetic 8.x; TLS health request | P-004 |

## R-017 — Legacy sensitivity procedure gap

- **Kind:** unknown
- **Authority:** unresolved
- **Provenance:** durable-artifact + incumbent-recall
- **Verification:** inaccessible
- **Purpose/claim:** exact command, revision, and validation contract for R-008/R-012
  were not recoverable
- **Status or last observation:** no runnable P record exists; do not rerun the legacy job
- **Evidence ref:** SRC-003 inventory; R-008 log locator lacks the full invocation
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:25:00Z
- **Valid until / recheck rule:** recheck if the submission script or complete log is recovered
- **Owner:** analysis team
- **Operational impact:** none for v3; exact R-008/R-012 reproduction is unavailable
- **Safe constraint/workaround:** never rerun R-008 or use R-012 for current work;
  forensic use still requires fresh P-004 terminal success, output validation, and
  Dr. Rivera's explicit approval
- **Next action:** recover a complete submission script only if pilot forensics are needed
- **Inputs / outputs / dependencies:** affects only superseded D-002 and legacy R-012
- **Risks/limitations:** forensic use requires every stated gate; it cannot support v3
- **Migration provenance:** SRC-003, CV-010, and
  [U-003](migration/AUDIT.md#u-003--legacy-sensitivity-job-terminal-state-and-command-unresolved)

## R-018 — QC dashboard lifecycle procedure gap

- **Kind:** unknown
- **Authority:** unresolved
- **Provenance:** durable-artifact
- **Verification:** unverified
- **Purpose/claim:** exact safe start, stop, restart, deploy, and recovery steps for R-009
  are not verified
- **Status or last observation:** source/config were located, but no executable lifecycle
  procedure was promoted
- **Evidence ref:** SRC-004 service inventory and R-009 health observation
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:20:00Z
- **Valid until / recheck rule:** recheck when an operator validates the container runbook
- **Owner:** analysis team
- **Operational impact:** optional R-009 cannot be safely restarted or redeployed
- **Safe constraint/workaround:** use static R-005 and do not invent lifecycle commands
- **Next action:** validate the container runbook before promoting a P record
- **Inputs / outputs / dependencies:** optional R-009 only; static R-005 is the fallback
- **Risks/limitations:** do not invent or execute restart commands
- **Migration provenance:** SRC-004 and CV-009 constrained gap

## R-019 — Undiscoverable historical-conversation boundary

- **Kind:** unknown
- **Authority:** unresolved
- **Provenance:** unknown
- **Verification:** inaccessible
- **Purpose/claim:** records that deleted conversations cannot be exhaustively enumerated
- **Status or last observation:** product-provided discovery surface exhausted; denominator unknown
- **Evidence ref:** SRC-001 and U-002
- **Checked by:** synthetic migration operator
- **Checked at:** 2026-09-01T09:35:00Z
- **Valid until / recheck rule:** recheck if discovery access changes or a current dependency
  exposes missing rationale
- **Owner:** Dr. Rivera
- **Operational impact:** none known; reclassify immediately if a current dependency appears
- **Safe constraint/workaround:** rely only on corroborated current D/R/P records
- **Next action:** preserve the discovery limit; retry only when the recheck rule fires
- **Inputs / outputs / dependencies:** no known operational dependency; forensic boundary only
- **Risks/limitations:** must be reclassified if later evidence connects it to current work
- **Migration provenance:** CV-013 and U-002
