# Procedures

Commands below are deliberately non-executable fixture content using reserved
`.example` hosts. Named `EV-*` captures resolve in the
[sanitized evidence registry](evidence/README.md); `SRC`/`MC` migration provenance
resolves in [AUDIT](migration/AUDIT.md).

## P-001 — Create the analysis environment

- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** migration `EV-TOOLS-01` and `EV-TEST-01`
- **Checked by/at:** synthetic migration operator / 2026-09-01T09:25:00Z
- **Owner:** data engineering
- **Last tested:** 2026-08-30T12:00:00Z (synthetic)
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Applies to:** R-001 at `a1b2c3d`, R-002, R-010, and R-016
- **Migration provenance:** SRC-007, EV-TOOLS-01, and EV-TEST-01

### Preconditions and inputs

Verify the R-016 R-002 tool locators, obtain R-010 authorization, and open an
interactive shell on R-002. The target path must not already exist. Every step below
runs in that R-002 shell; this procedure does not define a local-workstation checkout.

### Steps

```sh
/usr/bin/git clone --no-checkout \
  https://git.coastwatch.example/pipeline.git \
  /srv/coastwatch/src/pipeline
cd /srv/coastwatch/src/pipeline
/usr/bin/git checkout --detach a1b2c3d
test "$(/usr/bin/git rev-parse HEAD)" = a1b2c3d
/opt/coastwatch/bin/uv sync --frozen
/opt/coastwatch/bin/uv run pytest tests/test_calibration.py
```

### Outputs

A locked environment beside the R-001 checkout on R-002; no canonical research data
is copied.

### Verification

Dependency sync exits zero and the calibration test suite passes.

### Recovery

Remove only the tool-managed virtual environment and rerun
`/opt/coastwatch/bin/uv sync --frozen`. Do not modify R-003 or remote derived outputs.

## P-002 — Run v3 salinity normalization

- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** R-015 terminal record and R-004 validation manifest
- **Checked by/at:** synthetic migration operator / 2026-09-01T09:25:00Z
- **Owner:** analysis team
- **Last tested:** 2026-08-30T14:10:00Z (synthetic)
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Applies to:** R-001 `a1b2c3d`, R-002, R-003, R-004, R-006, R-010, R-016, D-004
- **Migration provenance:**
  [MC-002](migration/AUDIT.md#mc-002--calibration-must-be-selected-before-normalization-starts)
  and SRC-007

### Preconditions and inputs

P-001 passes; R-003 checksums match; D-004 is accepted; R-006 and the R-016
R-002 executables are freshly available through R-010. For an S-14 exclusion rerun,
D-003 must first be accepted and the cutoff argument below enabled exactly.

### Steps

On R-002, change to `/srv/coastwatch/src/pipeline` at R-001 `a1b2c3d`. Assign a unique
manifest ID following `RUN-YYYYMMDD-NNN`; the recorded R-015 invocation used
`RUN-20260830-001`. Set `RUN_MODE=standard` for a normal run. Only after D-003 is
accepted, set `RUN_MODE=exclude-s14-after-2026-08-17`. Submit the tracked batch
script and record the returned ID immediately:

```bash
set -euo pipefail
run_id="${RUN_ID:?set RUN_ID, for example RUN-20260830-001}"
run_mode="${RUN_MODE:?set RUN_MODE explicitly}"
[[ "$run_id" =~ ^RUN-[0-9]{8}-[0-9]{3}$ ]]
test ! -e "/srv/coastwatch/derived/v3/runs/${run_id}"
case "$run_mode" in
  standard)
    export_spec="RUN_ID=${run_id},EXCLUDE_S14_AFTER="
    ;;
  exclude-s14-after-2026-08-17)
    export_spec="RUN_ID=${run_id},EXCLUDE_S14_AFTER=2026-08-17T00:00:00Z"
    ;;
  *)
    printf '%s\n' "unsupported RUN_MODE: $run_mode" >&2
    exit 2
    ;;
esac
submission_dir="/srv/coastwatch/logs/submissions/${run_id}"
/bin/mkdir "$submission_dir"
submission_ref="$(/usr/bin/sbatch --parsable \
  --job-name="coastwatch-${run_id}" \
  --export="$export_spec" \
  scripts/run-normalization-v3.sbatch)"
printf '%s\n' "$submission_ref" > "$submission_dir/sbatch-parsable.txt"
job_id="${submission_ref%%;*}"
if ! [[ "$job_id" =~ ^[0-9]+$ ]]; then
  printf '%s\n' "submitted but could not parse numeric job ID: $submission_ref" >&2
  exit 3
fi
```

The `--export` list deliberately omits `ALL`: only the two named project variables
(plus Slurm's own scheduler variables) cross the submission boundary. This prevents
ambient submit-shell values or credentials from overriding the explicit run contract.

The canonical execution contract for `scripts/run-normalization-v3.sbatch` is the
following Bash sequence. `set -euo pipefail` is mandatory: validation failure stops
the script before the immutable run is sealed.

```bash
#!/bin/bash
#SBATCH --output=/srv/coastwatch/logs/slurm-%j.out
set -euo pipefail
run_id="${RUN_ID:?RUN_ID was not exported by the submitter}"
[[ "$run_id" =~ ^RUN-[0-9]{8}-[0-9]{3}$ ]]
candidate_dir="/srv/coastwatch/derived/v3/runs/${run_id}"
/bin/mkdir "$candidate_dir"
run_normalize() {
  /opt/coastwatch/bin/uv run python -m coastwatch.normalize \
    --config config/calibration.yml \
    --input /srv/coastwatch/raw/2026-08 \
    --output "$candidate_dir/salinity.parquet" \
    --manifest "$candidate_dir/manifest.json" \
    "$@"
}
if [[ -n "${EXCLUDE_S14_AFTER:-}" ]]; then
  test "$EXCLUDE_S14_AFTER" = "2026-08-17T00:00:00Z"
  run_normalize --exclude-sensor-after "S-14=${EXCLUDE_S14_AFTER}"
else
  run_normalize
fi
/opt/coastwatch/bin/uv run python -m coastwatch.validate \
  --raw /srv/coastwatch/raw/2026-08 \
  --candidate "$candidate_dir/salinity.parquet" \
  --manifest "$candidate_dir/manifest.json"
/opt/coastwatch/bin/uv run python -m coastwatch.seal \
  --run-dir "$candidate_dir" \
  --manifest "$candidate_dir/manifest.json"
```

Immediately create the owning job record with `job_id`, R-006/R-002, the R-001
revision, `RUN_ID`, `RUN_MODE`, exclusion environment if any, log path
`/srv/coastwatch/logs/slurm-${job_id}.out`, raw Slurm submission reference, and
submission observation time. Its initial current state is `unknown` unless P-004 has
already supplied a fresh scheduler observation; submission alone does not prove
`queued` or `running`. Then use P-004 with that ID and record its time-stamped result.

Only after P-004 establishes terminal `succeeded` and the sealed run manifest passes
the Verification checks below may the operator create the new run-scoped asset R
record. For every other scheduler or validation outcome, retain the job record and do
not claim an output asset. Queue absence is never success.

Submission precedes parsing. If numeric-ID validation fails, do not resubmit: create
an `unknown`/`blocked` job record pointing to
`/srv/coastwatch/logs/submissions/${RUN_ID}/sbatch-parsable.txt`, preserve the raw
reference, and have the scheduler owner resolve the real ID before any further
action.

### Outputs

On terminal success plus validation, a new immutable, run-scoped asset record (R-004
is the worked instance) plus its manifest containing input checksums, calibration
version, code commit, command arguments, row count, duplicate count, schema hash, and
sealed state. A new RUN_ID creates a successor record; P-002 never writes a shared
`current` artifact. Before those gates, the only guaranteed output is the job record
and submission evidence.

### Verification

Compare the manifest's input checksums to R-003, run schema validation, require zero
duplicate `(sensor_id, timestamp)` rows, and record the exact result in the owning
run-scoped asset R record (R-004 is the worked instance).

### Recovery

Leave a failed candidate unsealed in its run-specific path. Sealing occurs only after
validation exits zero, and no run path is overwritten, so prior verified assets stay
immutable. Preserve scheduler ID and log locator in its job record and set the
time-stamped observation to `failed`.

## P-003 — Build the v3 QC report

- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** synthetic P-003 output manifest and R-005 checksum comparison
- **Checked by/at:** synthetic migration operator / 2026-09-01T09:19:00Z
- **Owner:** analysis team
- **Last tested:** 2026-09-01T08:30:00Z (synthetic)
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Applies to:** R-001 `a1b2c3d`, R-002, any sealed P-002 normalization asset and
  its owning QC record (R-004/R-005 are the worked pair), R-010, and R-016
- **Migration provenance:** SRC-007 and EV-REMOTE-01

### Preconditions and inputs

Through R-010, on R-002 the R-016 `uv` locator is available, the selected owning
normalization asset record (R-004 in the worked run) is sealed and verified at the
exact manifest hash being reviewed, and R-001 is checked out at `a1b2c3d` under
`/srv/coastwatch/src/pipeline`.

### Steps

On R-002, change to `/srv/coastwatch/src/pipeline` at R-001 `a1b2c3d`. Set `RUN_ID`
to the sealed P-002 asset being reported; the recorded R-005 used
`RUN-20260830-001`.

```bash
set -euo pipefail
run_id="${RUN_ID:?set RUN_ID from the sealed asset record}"
[[ "$run_id" =~ ^RUN-[0-9]{8}-[0-9]{3}$ ]]
run_dir="/srv/coastwatch/derived/v3/runs/${run_id}"
qc_candidate="/srv/coastwatch/derived/v3/qc/${run_id}.tmp"
qc_final="/srv/coastwatch/derived/v3/qc/${run_id}"
test -f "$run_dir/manifest.json"
test ! -e "$qc_candidate"
test ! -e "$qc_final"
/bin/mkdir "$qc_candidate"
/opt/coastwatch/bin/uv run python -m coastwatch.qc \
  --input "$run_dir/salinity.parquet" \
  --output "$qc_candidate/report.html" \
  --manifest "$qc_candidate/manifest.json"
/opt/coastwatch/bin/uv run python -m coastwatch.validate_qc \
  --input-manifest "$run_dir/manifest.json" \
  --qc-manifest "$qc_candidate/manifest.json"
/bin/mv "$qc_candidate" "$qc_final"
```

### Outputs

A new run-scoped QC asset record (R-005 is the worked instance) and a manifest linking
the exact sealed normalization-run checksum. A new input run creates a successor
record and cannot overwrite an earlier report.

### Verification

Require the QC manifest's input checksum to equal its owning selected normalization
asset checksum (R-004 in the worked run), open the static report, verify all expected
sensor panels exist, and checksum the review copy against both the manifest and
remote artifact.

### Recovery

Keep a failed `.tmp` directory for evidence, then move it to a uniquely named failure
archive such as `qc-failed-${RUN_ID}-<UTC timestamp>` (after checking it is absent)
before retrying the same RUN_ID. Never delete or overwrite a completed run-scoped
report. The optional R-009 service is not required.

## P-004 — Verify job and service observations

- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** migration `EV-JOBS-01` and `EV-SVC-01`
- **Checked by/at:** synthetic migration operator / 2026-09-01T09:25:00Z
- **Owner:** analysis team
- **Last tested:** 2026-09-01T09:20:00Z (synthetic)
- **Accepted by/at:** Dr. Rivera during candidate review / 2026-09-01T09:35:00Z
- **Applies to:** R-002, R-006–R-010, R-015, R-016, and any P-002 job record
- **Migration provenance:** SRC-007, EV-JOBS-01, and EV-SVC-01

### Preconditions and inputs

From an authorized operator shell, verify R-016's `/usr/bin/ssh` and
`/usr/bin/curl`, obtain R-010 access, and select the exact record ID. Make no claim
that an old observation is current. For a job, set `JOB_ID` to its numeric execution
ID.

### Steps

First verify scheduler availability. For a job (R-008 uses `JOB_ID=88421`), validate
and query the real scheduler ID, then query terminal accounting even when the live
queue has no row:

```bash
job_id="${JOB_ID:?set JOB_ID from the owning job record}"
[[ "$job_id" =~ ^[0-9]+$ ]]
/usr/bin/ssh compute.coastwatch.example '/usr/bin/sinfo -h -o "%P|%a|%l"'
/usr/bin/ssh compute.coastwatch.example "/usr/bin/squeue -j ${job_id} -h -o '%i|%T|%M'"
/usr/bin/ssh compute.coastwatch.example \
  "/usr/bin/sacct -j ${job_id} --format=JobID,State,ExitCode,Elapsed"
```

For R-009:

```sh
/usr/bin/curl --fail --show-error https://qc.coastwatch.example/health
```

### Outputs

Time-stamped evidence for the owning R record. No separate status log.

### Verification

Match scheduler/service identity exactly. A missing queue row is not success; use
accounting and validate expected output. If access fails, record `unknown` or
`inaccessible`, not the previous tense.

### Recovery

Escalate scheduler ambiguity to research computing. Use static R-005 while R-009 is
unreachable. Do not retry or cancel a job without human authorization and a fresh ID.

## P-007 — Close the S-14 gate and freeze v3

- **Authority:** accepted
- **Provenance:** human-report + durable-artifact
- **Verification:** verified
- **Evidence ref:** synthetic two-branch tabletop `EV-GATE-01`
- **Checked by/at:** synthetic migration operator and Dr. Rivera / 2026-09-01T09:34:00Z
- **Owner:** Dr. Rivera and analysis team
- **Last tested:** never against a live system; synthetic two-branch tabletop passed
  at 2026-09-01T09:34:00Z
- **Accepted by/at:** Dr. Rivera / 2026-09-01T09:34:00Z
- **Applies to:** D-003, D-004, R-001–R-006, R-010, R-013, R-014, R-016
- **Migration provenance:**
  [MC-008](migration/AUDIT.md#mc-008--p-007-is-the-accepted-two-branch-s-14-gate-procedure)

### Preconditions and inputs

Using R-010 access on R-002 with R-001 checked out at `a1b2c3d` under
`/srv/coastwatch/src/pipeline`, Dr. Rivera reviews R-005 against R-013 and R-014 and
explicitly accepts or rejects D-003 with identity, time, rationale, and evidence
references.

### Steps

1. If D-003 is accepted, choose a new `RUN_ID`, run P-002 with exactly
   `RUN_MODE=exclude-s14-after-2026-08-17`, and save its returned ID in a new job
   record. Run P-004 with that `JOB_ID`. If it is queued/running or unknown, stop and
   resume this procedure only after a later fresh P-004 observation. Proceed only
   after the record says `succeeded` and the sealed run path and manifest contain the
   same `${RUN_ID}`; validate the successor asset record created by P-002, then create
   its successor QC record with P-003.
2. If D-003 is rejected, do not rerun normalization. From the R-001 checkout at
   `a1b2c3d`, revalidate the current R-004 exactly as follows. Then apply P-003's
   verification criteria to the existing immutable R-005 and its manifest; do not
   rerun P-003 or overwrite the completed run-scoped report:

   ```sh
   /opt/coastwatch/bin/uv run python -m coastwatch.validate \
     --raw /srv/coastwatch/raw/2026-08 \
     --candidate /srv/coastwatch/derived/v3/runs/RUN-20260830-001/salinity.parquet \
     --manifest /srv/coastwatch/derived/v3/runs/RUN-20260830-001/manifest.json
   ```

3. In either branch, create a new accepted decision naming the exact selected
   run-scoped asset and manifest, calibration D-004, S-14 disposition, and reviewer.
   Do not rewrite D-003 into a different question. Concurrent or later RUN_IDs cannot
   mutate the selected asset and require their own records.
4. Mark the selected normalization/QC record pair's authority and evidence
   consistently with that decision, preserve predecessor records, then update STATE's
   frontier, active work, and next human gate.

### Outputs

An accepted freeze decision, a verified selected normalization/QC pair (R-004/R-005
in the rejection branch or their successors), and a new project frontier.

### Verification

The freeze decision and its linked manifest together identify R-003 checksums, R-001
commit, D-004, D-003 outcome, exact arguments, schema hash, row count, and duplicate
count. Every ID resolves.

### Recovery

If either branch fails validation, leave D-003's human disposition intact but do not
create the freeze decision. Surface the failed job/artifact and recovery gate in STATE.
