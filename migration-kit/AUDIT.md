# Migration audit — `<migration-id>`

Copy this file into the empty active dossier path selected in MIGRATE Phase 0,
alongside that run's `COVERAGE.md` and `CUTOVER.md`. On an explicit same-run resume,
use the existing files without recopying. Replace angle-bracket placeholders; when a
value cannot be known, write `unknown` and create a blind-spot entry. This is a
candidate-claim dossier, not a destination-state database.

## Dossier map

- [AUDIT](AUDIT.md) owns sources, candidate claims, conflicts, unknowns, and the
  normalization ledger.
- [COVERAGE](COVERAGE.md) owns the denominator and each surface's disposition.
- [CUTOVER](CUTOVER.md) owns the delta sweep, candidate dry run, gate, and human
  transition decision.

## Run boundary

- **Migration ID:** `<YYYY-MM-DD-project>`
- **Incumbent project/product:** `<project and native agent environment>`
- **Operator:** `<human or incumbent agent identity>`
- **Started at:** `<ISO-8601 with timezone>`
- **Audit horizon:** `<what dates/surfaces this run attempts to cover>`
- **Source Git state:** `<repo, branch, commit, dirty-state evidence>`
- **Initial watermark:** `<time the first inventory describes>`
- **Target workspace:** `<safe locator>`

The surface denominator and result for every source live only in
[`COVERAGE.md`](COVERAGE.md). This file owns extracted claims, conflicts, and detailed
blind spots.

## Source notes

Add one bounded note per inspected source when the coverage row and evidence locator
are not self-explanatory.

### SRC-001 — `<source title>`

- **Coverage row:** `<CV-...>`
- **Scope actually inspected:** `<thread IDs/date range/path/host/config area>`
- **Inspection method:** `<commands, UI listing, tool query>`
- **Observed at:** `<ISO-8601>`
- **Evidence/output refs:** `<safe locators; no secrets or raw private transcript>`
- **Limitations:** `<none or exact limitation>`

## Candidate claims

All claims begin provisional. Use claim-level provenance and verification; do not
upgrade a whole narrative because one field was checked. Use an MC entry for recalled,
conflicting, interpretive, or transformed claims. Directly observed resource,
environment, tool, or exact-procedure fields may link a named SRC observation
without a redundant MC when no interpretation or normative choice is introduced; the
destination must retain that source as migration provenance.

The destination also retains the dossier path. If more than one migration dossier
exists, every backlink MUST be path-qualified (or use migration-ID-namespaced IDs);
a naked `SRC-001` or `MC-001` is otherwise ambiguous across runs.

### MC-001 — `<exact, atomic claim>`

- **Track:** `<operational | forensic>`
- **Criticality:** `<critical | supporting>`
- **Authority:** `provisional` initially; transition per the rules below before freeze
- **Provenance:** `<live-environment | durable-artifact | incumbent-recall | human-report | inference | unknown>`
- **Verification:** `<verified | unverified | contradicted | stale | inaccessible>`
- **Evidence ref:** `<SRC/file/Git/log/config/live-check locator; CV is denominator state>`
- **Checked at:** `<ISO-8601 or unknown>`
- **Checked by:** `<operator/human/tool identity or unknown>`
- **Scope/limitations:** `<where this claim does and does not apply>`
- **Conflict/unknown:** `<CF/U ID or none; CV rows are denominator state, not evidence>`
- **Destination:** `<STATE | D/R/P ID | audit evidence only | forensic backlog | reject>`
- **Disposition:** `<pending | canonicalized | retained-evidence | rejected | backlog | blocked>`
- **Authority disposition by/at:** `<accepted/rejected + identity/time; or remains provisional + reviewer/time>`

## Conflict log

### CF-001 — `<short conflict>`

- **Claims/evidence in conflict:** `<IDs and exact mismatch>`
- **Operational impact:** `<what becomes unsafe or ambiguous>`
- **Freshest checkable evidence:** `<ref and timestamp>`
- **Accepted intent affected:** `<D ID or none>`
- **Safe interim constraint:** `<constraint or none>`
- **Disposition:** `<unresolved | current observation chosen | human decision required | other>`
- **Resolved by/at:** `<identity/time or pending>`
- **Resulting canonical record:** `<ID or none>`

Current evidence may establish observed reality; it cannot silently supersede an
accepted human decision. When those conflict, keep both and record drift.

### Candidate transition rules

| Candidate condition | Allowed treatment |
| --- | --- |
| `verified` atomic claim | Canonicalize as provisional, or as accepted only with explicit human acceptance. |
| `unverified`/`inaccessible` claim | Keep pending/backlog/blocked unless an authorized human accepts the exact residual risk and a safe constraint. That exception may be canonicalized with the uncertainty intact; it cannot bypass an unsafe critical blocker. |
| `contradicted` claim | Set authority/disposition to rejected, retain it as provenance, and create a separate positive claim for current evidence. |
| `stale` present-tense claim | Set the unsafe assertion to rejected/retained-evidence; split out an exact historical observation and a separate current-unknown claim. |

Authority describes governance of the claim. Disposition describes what migration
did with it; the two are not substitutes. A transformed sentence is a new atomic
claim, not a silent “promotion” of the old one.

## Blind spots

### U-001 — `<inaccessible or unknown surface>`

- **Coverage row:** `<CV-...>`
- **Attempts/evidence:** `<what was tried and what happened>`
- **Why unknown:** `<access denied, deleted, undiscoverable, ambiguous, etc.>`
- **Operational consequence:** `<exact risk, or none with reason>`
- **Classification rationale:** `<why the COVERAGE track/criticality is defensible>`
- **Safe constraint/workaround:** `<how work can proceed safely, or none>`
- **Owner:** `<human/role>`
- **Next action:** `<one action>`
- **Recheck condition:** `<event/time>`

Track, criticality, access, result, and disposition live only in the referenced
`COVERAGE.md` row.

## Required extraction prompts by domain

Use these as audit questions. Results belong in candidate claims and coverage rows,
not duplicate prose under this heading.

### Conversations and native project context

- Which accessible threads may contain decisions, obsolete conclusions, exact
  procedures, open loops, artifact locators, or operational rationale?
- What listing or date scope proves what “accessible” meant?
- Which relevant history is inaccessible or not discoverable?

### Instructions and memory

- Which items are neutral truth, agent mechanics, personal preferences, or stale?
- Which remembered assumptions lack corroboration?
- Which auto-memory/project-memory locations were inspected, and which were not?

### Tools and MCPs

- Identity, required/optional role, dependent functions, capabilities used?
- Configuration locator, authentication/secret class, replacement/recovery path?

### Local repositories and Git

- Repository/worktree roles, branches, relevant commits/tags, dirty state?
- Which material is tracked source, generated output, or ignored local state?

### Remote hosts and topology

- Which host aliases and important directories/resources exist?
- For each: role, assets, inputs/outputs, readers/writers, producer run/revision,
  lifecycle state, access method, secret reference, and last verification?

### Assets and lineage

- Which artifact is raw/source/canonical/derived/cache/scratch/archive/legacy?
- What exact inputs, procedure/job, commit/version/run produced it?

### Services

- What is desired state versus observed state?
- Where are source/config, lifecycle procedures, health check, dependencies, logs,
  persistent state, build/deploy method, and risk?

### Jobs

- Is there a real process/scheduler/service/automation/agent-run ID?
- What host, command/spec, working directory, revision, log/output, owner, next gate,
  check method, observation time, and freshness rule support the status?
- For recurring work, what real scheduler/automation ID, schedule, next-run evidence,
  and disable/recovery procedure exist?
- If the evidence is missing or old, is the defensible state planned, absent, last
  observed, or unknown?

### Environment and operations

- Are environment, dependencies, build, test, deploy, service start, pipeline run,
  reproduction, update, maintenance, and recovery procedures exact and tested?

### Dependencies and secrets

- Which external systems and credential classes are required?
- Where/how does an authorized user obtain or configure each secret, without storing
  its value?

## Normalization ledger

| Candidate | Destination ID | Owning file | Exact claim promoted | Residual limitation | Reviewer |
| --- | --- | --- | --- | --- | --- |
| `<MC-...>` | `<D/R/P-...>` | `<path>` | `<claim fields>` | `<none or limitation>` | `<identity>` |

After cutover, freeze this dossier. Correct it with a dated addendum; update ongoing
truth only in the owning canonical object.
