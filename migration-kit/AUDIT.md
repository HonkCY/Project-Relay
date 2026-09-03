# Migration audit — `<migration-id>`

Copy this file to `.relay/migration/AUDIT.md`. Replace angle-bracket placeholders;
when a value cannot be known, write `unknown` and create a blind-spot entry. This is
a candidate-claim dossier, not a destination-state database.

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
upgrade a whole narrative because one field was checked.

### MC-001 — `<exact, atomic claim>`

- **Track:** `<operational | forensic>`
- **Impact:** `<blocker | supporting>`
- **Authority:** `provisional`
- **Provenance:** `<live-environment | durable-artifact | incumbent-recall | human-report | inference | unknown>`
- **Verification:** `<verified | unverified | contradicted | stale | inaccessible>`
- **Evidence ref:** `<SRC/CV/file/Git/log/config/live-check locator>`
- **Checked at:** `<ISO-8601 or unknown>`
- **Scope/limitations:** `<where this claim does and does not apply>`
- **Conflict/unknown:** `<CF/U ID or none>`
- **Destination:** `<STATE | D/R/P ID | forensic backlog | reject>`
- **Disposition:** `<pending | canonicalized | rejected | backlog | blocked>`
- **Accepted by/at:** `<only if an authorized human explicitly accepts>`

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

## Blind spots

### U-001 — `<inaccessible or unknown surface>`

- **Coverage row:** `<CV-...>`
- **Attempts/evidence:** `<what was tried and what happened>`
- **Why unknown:** `<access denied, deleted, undiscoverable, ambiguous, etc.>`
- **Track/impact:** `<operational|forensic> / <blocker|supporting>`
- **Operational consequence:** `<exact risk, or none with reason>`
- **Safe constraint/workaround:** `<how work can proceed safely, or none>`
- **Owner:** `<human/role>`
- **Next action:** `<one action>`
- **Recheck condition:** `<event/time>`
- **Disposition:** `<blocked | constrained | reclassified | forensic backlog>`

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

| Candidate | Destination ID | Owning file | Fields promoted | Residual limitation | Reviewer |
| --- | --- | --- | --- | --- | --- |
| `<MC-...>` | `<D/R/P-...>` | `<path>` | `<claim fields>` | `<none or limitation>` | `<identity>` |

After cutover, freeze this dossier. Correct it with a dated addendum; update ongoing
truth only in the owning canonical object.

