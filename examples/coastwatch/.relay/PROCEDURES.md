# Procedures

Commands below are deliberately non-executable fixture content using reserved
`.example` hosts.

## P-001 — Create the analysis environment

- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Owner:** data engineering
- **Last tested:** 2026-08-30T12:00:00Z (synthetic)
- **Applies to:** R-001 at `a1b2c3d`

### Preconditions and inputs

Clone R-001, check out `analysis-v3`, and obtain only the R-010 access reference if
remote tests are required.

### Steps

```sh
uv sync --frozen
uv run pytest tests/test_calibration.py
```

### Outputs

A locked local environment; no canonical research data is copied.

### Verification

Dependency sync exits zero and the calibration test suite passes.

### Recovery

Remove only the tool-managed virtual environment and rerun `uv sync --frozen`. Do
not modify R-003 or remote derived outputs.

## P-002 — Run v3 salinity normalization

- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Owner:** analysis team
- **Last tested:** 2026-08-30T14:10:00Z (synthetic)
- **Applies to:** R-001 `a1b2c3d`, R-003, R-004, D-004

### Preconditions and inputs

P-001 passes; R-003 checksums match; D-004 is accepted. For an S-14 exclusion rerun,
D-003 must first be accepted and `--exclude-sensor S-14` added explicitly.

### Steps

On R-002, from the R-001 checkout at the recorded commit:

```sh
uv run python -m coastwatch.normalize \
  --config config/calibration.yml \
  --input /srv/coastwatch/raw/2026-08 \
  --output /srv/coastwatch/derived/v3/salinity.parquet
```

For batch execution, submit through R-006 and immediately create/update the job
record with the real returned ID, log path, revision, and observation time.

### Outputs

R-004 plus a manifest containing input checksums, calibration version, code commit,
command arguments, row count, and schema hash.

### Verification

Compare the manifest's input checksums to R-003, run schema validation, require zero
duplicate `(sensor_id, timestamp)` rows, and record the exact result in R-004.

### Recovery

Write a failed attempt to a run-specific temporary path. Never overwrite the last
verified R-004 until verification passes. On failure, preserve the scheduler ID and
log locator in its job record and set observed state `failed`.

## P-003 — Build the v3 QC report

- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Owner:** analysis team
- **Last tested:** 2026-09-01T08:30:00Z (synthetic)
- **Applies to:** R-004 and R-005

### Preconditions and inputs

R-004 verification passes at the exact manifest hash being reviewed.

### Steps

```sh
uv run python -m coastwatch.qc \
  --input /srv/coastwatch/derived/v3/salinity.parquet \
  --output /srv/coastwatch/derived/v3/qc/report.html
```

### Outputs

R-005 and a manifest linking the R-004 checksum.

### Verification

Open the static report, verify all expected sensor panels exist, and checksum the
review copy against the remote artifact.

### Recovery

Regenerate from the last verified R-004. The optional R-009 service is not required.

## P-004 — Verify job and service observations

- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Owner:** analysis team
- **Last tested:** 2026-09-01T09:20:00Z (synthetic)
- **Applies to:** R-006, R-007, R-008, R-009

### Preconditions and inputs

Authorized R-010 access; exact record ID; no claim that an old observation is current.

### Steps

For R-008, query the real scheduler ID and then terminal accounting if absent from
the live queue:

```sh
ssh compute.coastwatch.example 'squeue -j 88421 -h -o "%i|%T|%M"'
ssh compute.coastwatch.example 'sacct -j 88421 --format=JobID,State,ExitCode,Elapsed'
```

For R-009:

```sh
curl --fail --show-error https://qc.coastwatch.example/health
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

## P-005 — Run pilot sensitivity analysis

- **Authority:** superseded
- **Provenance:** incumbent-recall
- **Verification:** stale
- **Owner:** analysis team
- **Last tested:** unknown
- **Applies to:** legacy D-002, R-008, and R-012 only

This historical procedure is intentionally not expanded: it is irrelevant to the
v3 frontier and its exact recovered steps remain forensic backlog. Do not run it.

## P-006 — Operate the QC dashboard

- **Authority:** provisional
- **Provenance:** durable-artifact
- **Verification:** unverified
- **Owner:** analysis team
- **Last tested:** unknown
- **Applies to:** optional R-009

The exact container restart procedure is still operational supporting work. Until it
is verified, use static R-005; do not invent a restart command.

