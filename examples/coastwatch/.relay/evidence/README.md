# Sanitized fixture evidence

These captures make the Coastwatch migration dossier inspectable. Every value is
fictional and intentionally non-secret; no command here was run against an external
Coastwatch system. The dossier uses them as worked-example evidence, not proof that a
real migration or remote execution occurred.

## EV-CONV-01 — Initial conversation inventory

- **Observed at:** 2026-08-30T09:35:00Z (synthetic)
- **Scope:** product-provided project listing from 2026-05-01 through the watermark
- **Sanitized result:** one active v3 thread opened; one named pilot archive returned
  `access denied`; deleted threads were not enumerable
- **Supports:** SRC-001, CV-001, CV-002, CV-013

## EV-CONV-02 — Conversation delta inventory

- **Observed at:** 2026-09-01T09:30:00Z (synthetic)
- **Scope:** same listing boundary as EV-CONV-01, after its watermark
- **Sanitized result:** one new proposal for D-003; no additional operational thread
- **Supports:** CUTOVER delta sweep and D-003 discovery time

## EV-MEM-01 — Instructions and memory inventory

- **Observed at:** 2026-08-31T14:30:00Z (synthetic)
- **Scope:** project instruction file, every topic returned by the native memory list,
  and the complete incumbent MCP/connector settings listing
- **Sanitized result:** one stale v2-path recollection isolated as MC-001; a context
  note's assertion that job 88421 was still running was isolated as MC-003; no MCP
  or connector was configured or required; no secret value copied
- **Supports:** SRC-002, CV-003, CV-004, MC-001, MC-003, CF-001

## EV-TOOLS-01 — Required tool inventory

- **Observed at:** 2026-09-01T09:25:00Z (synthetic)
- **Checks:** on R-002, `/bin/bash --version`, `/usr/bin/git --version`,
  `/opt/coastwatch/bin/uv --version`, and discovery of `/bin/{mkdir,mv}` plus
  `/usr/bin/{sbatch,sinfo,squeue,sacct}`; on the authorized operator shell,
  `/bin/bash --version`, `/usr/bin/ssh -V`, and `/usr/bin/curl --version`
- **Sanitized result:** every executable and version/capability in R-016's placement
  table was present; lockfile and SSH configuration locators were recorded in
  R-016/R-010
- **Supports:** R-006, R-016, P-001, CV-005

## EV-JOBS-01 — Scheduler inventory

- **Observed at:** 2026-09-01T09:25:00Z (synthetic)
- **Scope:** account `coastwatch-analysis`; live queue, terminal accounting since
  2026-05-01, scheduler entries, and listed automations
- **Sanitized result:** job `88204|COMPLETED|0:0|00:22:00`; for `88421`, the live
  queue and retained accounting each returned no row, so queue absence did not prove
  success; the only available `88421|RUNNING|00:19:00` capture was from
  2026-08-31T14:22:00Z and had expired; no recurring project entry was found
- **Supports:** R-007, R-008, R-015, P-004, CV-010

## EV-TEST-01 — Calibration test capture

- **Observed at:** 2026-08-30T12:00:00Z (synthetic)
- **Command:** `/opt/coastwatch/bin/uv run pytest tests/test_calibration.py`
- **Sanitized result:** exit 0; `3 passed`; lockfile unchanged
- **Supports:** P-001 verification in the fictional fixture

## EV-SVC-01 — Service inventory and health capture

- **Observed at:** 2026-09-01T09:20:00Z (synthetic)
- **Scope:** `coastwatch-*` unit names, container list, and project endpoint registry on
  R-002
- **Sanitized result:** one optional R-009 service located; health request timed out;
  exact lifecycle procedure absent
- **Supports:** R-009, R-018, P-004, CV-009

## EV-REMOTE-01 — Remote topology and artifact manifest checks

- **Observed at:** 2026-09-01T09:19:00Z (synthetic)
- **Scope:** the five roots listed in R-002 plus manifests for R-003–R-005 and
  R-012–R-015
- **Sanitized result:** roles, lineage, readers/writers, lifecycle, and inherited
  R-010 access were mapped; R-003's declared synthetic logical size was 3.2 TiB;
  R-004 inputs matched R-003, duplicate count was zero, row count was 2,678,400, and
  the fixture schema hash was
  `sha256:73ab91f073ab91f073ab91f073ab91f073ab91f073ab91f073ab91f073ab91f0`
- **Supports:** R-002–R-005, R-012–R-015, SRC-005, CV-007, CV-008

## EV-GIT-02 — Source Git delta check

- **Observed at:** 2026-09-01T09:10:00Z (synthetic)
- **Sanitized result:** R-001 checkout `analysis-v3@a1b2c3d`; working tree clean; no
  source change since the initial watermark
- **Supports:** CUTOVER delta sweep and R-001

## EV-DEC-01 — Human decision delta check

- **Observed at:** 2026-09-01T09:35:00Z (synthetic)
- **Sanitized result:** Dr. Rivera confirmed D-003 remained pending; D-004 remained
  accepted
- **Supports:** CUTOVER delta sweep and STATE's next human gate

## EV-POLICY-01 — Raw-data policy capture

- **Observed at:** 2026-09-01T09:32:00Z (synthetic)
- **Scope:** signed fictional policy `POL-DATA-02`, sections covering source sensor
  exports and maintenance logs under the raw-data root
- **Sanitized result:** source records are immutable; corrections must be versioned
  derived assets with lineage; Dr. Rivera's 2026-06-12 acceptance was present
- **Supports:** SRC-006, MC-009, and D-001

## EV-GATE-01 — S-14 gate tabletop

- **Observed at:** 2026-09-01T09:34:00Z (synthetic)
- **Scope:** both branches of the proposed P-007 procedure, including prerequisites,
  wait/stop conditions, artifact checks, outputs, and failure recovery
- **Sanitized result:** Dr. Rivera accepted the procedure mechanics without deciding
  D-003; the exclusion branch waits for a successful identified job and manifest,
  while the rejection branch revalidates the existing identified manifest
- **Supports:** SRC-007, MC-008, and P-007

## EV-RISK-01 — Candidate residual-risk acceptance

- **Observed at:** 2026-09-01T09:35:00Z (synthetic)
- **Scope:** exact safe constraints for CV-009/R-018 and
  CV-010/U-003/R-008/R-012/R-017 before candidate commit
- **Sanitized result:** Dr. Rivera accepted both constraints as non-blocking for the
  candidate; this was not approval of the later overall cutover boundary
- **Supports:** CV-009, CV-010, the CUTOVER residual-risk rows, and delta sweep

## EV-CANDIDATE-01 — Candidate authority review

- **Observed at:** 2026-09-01T09:35:00Z (synthetic)
- **Scope:** field-level evidence and authority dispositions for R-001–R-003, R-006,
  R-010, R-014–R-016, P-001–P-004, MC-001, MC-003, MC-006, and CF-001
- **Sanitized result:** Dr. Rivera accepted the listed verified operational records
  and procedures, accepted the verified current-v3 claim, and rejected the two stale
  present-tense claims before candidate commit; D-003 and overall cutover stayed open
- **Supports:** the listed acceptance/disposition fields, CF-001, and delta sweep;
  each underlying fact retains its own evidence reference

## EV-DRY-01 — Illustrative fresh-agent capture

- **Observed at:** 2026-09-01T09:37:00Z (synthetic)
- **Candidate commit:** synthetic `ca11dad`
- **Prompt:** `Bootstrap from this folder and report current work and risks.`
- **Freshness condition:** blank fixture conversation with no project explanation
- **Sanitized result:** recovered the S-14 frontier, D-001/D-004 authority, Dr. Rivera
  gate, R-003 → R-015/P-002 → R-004 → P-003 → R-005 lineage, reported `migration
  candidate — not cut over`, identified operational cutover as the current gate and
  D-003 as the proposed post-cutover gate, kept the incumbent project as live
  workspace and its agent only operator/witness, checked R-002/R-006/R-016 execution
  locators through the R-010 reference without reading a secret value, and refused to
  call R-007/R-008 running; it reported R-009 only as last observed unreachable
- **Safe local check shown in capture:**
  `rg --hidden --glob '!.git/**' 'R-007|R-008|R-009|P-004' .relay`
- **Fixture status:** illustrative evidence embedded for review; it does not claim that
  Claude, Codex, Git, or the `.example` systems executed the fictional 2026-09-01 run
- **Supports:** CUTOVER fresh-agent table and P-007 runbook review

## EV-VERIFY-01 — Read-only v3 artifact validation

- **Observed at:** 2026-09-01T09:38:00Z (synthetic)
- **Operator:** fictional fresh-agent fixture session from EV-DRY-01
- **Execution surface/access/tool:** R-002 through the R-010 reference, using R-016
  `/opt/coastwatch/bin/uv`; locator/version checks passed and no secret value was read
- **Command:** `/opt/coastwatch/bin/uv run python -m coastwatch.validate --raw /srv/coastwatch/raw/2026-08 --candidate /srv/coastwatch/derived/v3/runs/RUN-20260830-001/salinity.parquet --manifest /srv/coastwatch/derived/v3/runs/RUN-20260830-001/manifest.json`
- **Sanitized result:** exit 0; R-003 input checksums matched; schema hash
  `sha256:73ab91f073ab91f073ab91f073ab91f073ab91f073ab91f073ab91f073ab91f0`;
  duplicate `(sensor_id, timestamp)` count 0; row count 2,678,400
- **Safety:** read-only verification; no job submission, service mutation, or artifact sealing
- **Fixture status:** inspectable worked-example output, not a claim that an external
  `.example` host was contacted from this repository
- **Supports:** CUTOVER task-relevant fresh-agent verification and R-004
