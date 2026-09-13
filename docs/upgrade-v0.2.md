# Upgrade a v0.1 workspace to the v0.2 integrity rules

This is a surgical merge of protocol behavior into an existing workspace. Keep
the same STATE / DECISIONS / RECORDS / PROCEDURES owners, stable IDs, thin native
adapters, and private-evidence boundary. No new database, daemon, registry, lock
service, mandatory field schema, or transcript ingestion is required. The changes
are a review candidate until the project's authorized owner accepts them.

Only a Maintainer explicitly authorized to upgrade this workspace may perform the
merge. A Reader handoff, missing entry file, or access to a read-only snapshot is
not upgrade authorization. Readers can report gaps in their independent outputs;
they do not install files, initialize Git, inventory native history, or repair the
source. This guide does not authorize batch upgrades of other workspaces.

## 1. Inspect the active workspace

Read its native adapter, START, and STATE; inspect `git status --short --branch`.
Preserve uncommitted work, including canonical edits newer than `HEAD`. Establish
which working copy is canonical and which copies are mirrors or backups from the
existing map and task-relevant repository records. Do not scan every registry or
every folder for matching IDs. An ID in another independent workspace is not a
duplicate owner here.

Use existing repository record fields for locator, role, readers/writers, observed
revision, recheck condition, and limitations. A mirror can be `derived`, a backup
`archive`; neither is authorized to write merely because it is synchronized.
Coordinate one writer to this canonical working copy and define an integration
order for parallel worktrees. Where a known sync mechanism or visible conflict
raises a task-relevant inconsistency, resolve it before affected writes.

## 2. Merge the rules into START

Compare the current START with [template START](../template/.relay/START.md), then
merge only the relevant instructions. Preserve project-specific paths, accepted
decisions, and bounded lookup guidance; never replace the whole `.relay/` tree.
Native adapters continue to route to START and STATE.

- [Session access contract](protocol.md#session-access-contract): add Reader and
  Maintainer lifecycle routing, with session-local source/output/query boundaries.
  Do not put a mutable global mode flag in shared STATE. Existing explicitly
  authorized maintenance remains valid when mode is omitted; a generic continue,
  checkpoint instruction, or writable tool is not a grant. Task metadata records
  an authorization basis but cannot promote its author.
- [BOOTSTRAP](protocol.md#bootstrap): check required snapshot meaning using the
  already required reads. Explicit `none` and `unknown` are valid; missing content
  is not an implicit answer. Complete paginated output before diagnosing a damaged
  file. Resolve only task-required owner ambiguity and stop when the working set is
  sufficient; stable-ID pointers remain on-demand.
- [CHECKPOINT / WRITE-BACK](protocol.md#checkpoint--write-back): save owners first,
  then changed STATE, then reopen the affected sections at the intended paths and
  compare expected values before reporting completion. A write success message
  alone is insufficient. Read-back confirms local content at a time; it does not
  prove physical persistence, sync completion, or a later state.
- [SWITCH](protocol.md#switch) and [Git semantics](protocol.md#git-semantics): local
  saved edits remain recoverable without a commit. An authorized cross-host writer
  transfer names a coherent commit, transfers it through Git or a bundle, and checks the
  receiving commit and required canonical files. Preserve and inspect receiving
  dirty work; neither a commit match nor a sync icon proves the working tree is
  identical or semantically correct.
  Reader handoff instead retains the task output/checkpoint and authorized read
  basis, including a permitted non-Git snapshot; it does not transfer writer rights.

Maintainer checkpoints use the existing owner/evidence/unknown fields for material
mismatches. Route Reader CHECKPOINT, VERIFY, RECOVER, and SWITCH to its separate
task output, preserving mode and query limits across recovery. The optional
[Reader task template](../reader-kit/TASK.md) stores task boundaries, read basis,
saved work and handoff proposals, not a second project STATE or editable owner
replica. Existing adapters that already delegate checkpoint behavior to START need
no expanded role rules; merge away any adapter-specific unconditional source-write
instruction while preserving unrelated project constraints.

If an expected value is absent or wrong, or its source is inaccessible, report that
specific limitation and apply existing verification
and conflict rules. Suspend only the operation that depends on the unresolved fact.

## 3. Update setup and migration procedures

Merge the relevant [INIT](init.md) and [MIGRATE](migrate.md) changes into any local
procedure that specializes them. Keep storage/copy roles in repository R records
and migration observations in the existing run boundary, SRC notes, and delta rows.
An off-host backup SHOULD exist where practical; record absent or unverified backup
as a recovery limitation. Merely configuring a remote does not demonstrate a backup.

MIGRATE still enumerates surfaces, extracts claims, records provenance, normalizes
owners, and requires human cutover. Apply bounded read-back to the Phase-6 changed
owners and final cutover transition. Preserve native-session snapshots as optional
private forensic evidence; fresh-agent continuation must work without
`.relay/private/`. Do not alter frozen dossiers or historical validation evidence
to make them appear to have tested the new rules.

## 4. Verify and checkpoint the merge

Check Reader source/output isolation, task-scoped version or dirty-content basis,
bounded R/P query authorization, and recovery without promotion. Require current
owner comparison and serialized selective integration of Reader deliveries; an
older delivery cannot overwrite newer source state or supply human acceptance.
Use synthetic fixtures only unless real-project testing is separately authorized.

Review the diff against the specific rules above. Confirm that task-relevant IDs
still point to their intended owners, adapters remain thin, and the snapshot can
answer the normal bootstrap questions with no new default registry reads. Exercise
the applicable [acceptance scenarios](acceptance-tests.md), including malformed
snapshot/read-back and copy-boundary cases, using new fixtures or evidence.

Apply the updated checkpoint rule to this merge. Keep existing decision authority
unchanged unless the authorized owner explicitly changes it; implementing proposed
rules does not grant acceptance. Retain the historical `v0.1` and `v0.1-design` tag
targets, original Scenario A/B results, and frozen Coastwatch dossier. Record the
new candidate boundary and its own validation before the next human gate.
