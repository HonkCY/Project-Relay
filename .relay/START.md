# Relay start

This directory is the canonical project workspace for the Project Relay framework
repository. The root agent files are adapters, not stores of project truth.

## Bootstrap

1. Start with the native adapter, this START file, and [STATE.md](STATE.md); read
   START and STATE completely before other project content.
2. Inspect `git status --short --branch`; uncommitted canonical files may be newer
   than `HEAD`.
3. Follow only the IDs and links relevant to the task:
   - [DECISIONS.md](DECISIONS.md) — governing and superseded choices
   - [RECORDS.md](RECORDS.md) — repositories, assets, tools, services, jobs, unknowns
   - [PROCEDURES.md](PROCEDURES.md) — exact repeatable operations
4. When a remembered claim conflicts with a canonical record or current evidence,
   stop treating the claim as fact. Record the conflict or unknown and verify it.

Build the requested working set from START/STATE first. If STATE suffices, do not
follow deeper owners for reassurance or complete understanding. Follow a D/R/P ID
only for a missing requested fact, execution/modification of that owner, exact
procedure/resource detail, required fresh verification, or unresolved canonical
conflict. A question about where detail lives needs only the ownership pointer.
Locate that exact ID heading in its mapped registry, then read its bounded section
and only required direct dependencies; do not inventory headings or load a registry
merely because it is monolithic. Ordinary Git bootstrap stops at current status.

Using the mandatory reads, check that START supplies its ownership/write-back map
and STATE supplies frontier, active work, gate, governing decisions, urgent unknowns,
and background safety. Require intelligible non-empty content, not exact headings;
explicit none/unknown/initialization placeholders are valid. Complete paginated or
truncated tool output before judging the file. Missing content is not an answer.
Report inaccessible evidence or readable gaps/conflicts accurately; preserve work
and pause dependent actions without inventing or overwriting state.

Require one definition for a task-required ID within this workspace's map. Other
workspaces, examples, and historical evidence are separate scopes. Missing/ambiguous
lookup or a suspected conflict copy exposed by status/a relevant path needs only
scoped resolution using the map and accepted precedence. If still ambiguous,
preserve files and request human disposition before dependent actions. Never elect
by mtime/first hit, automatically delete/hide suspected conflict copies, or perform
a global duplicate scan.

Stop when all requested facts have owners, coordination state suffices, and no
required freshness/conflict/uncertainty remains, unless execution, modification,
audit, or provenance reconstruction is requested. Migration dossiers and historical
evidence are not bootstrap material unless explicitly requested or required by a
task-relevant owner to settle verification/conflict. Plausibility is not freshness.

Because `.relay/` is hidden, search it with an explicit path or with, for example,
`rg --hidden --glob '!.git/**' '<term>' .relay`.

This file is the short executable subset of the
[normative framework protocol](../docs/protocol.md). Project-specific accepted
decisions may specialize it; accidental contradictions must be surfaced, not guessed
away.

## Ownership and precedence

- `STATE.md` owns only the current frontier, active work, next human gate, and
  urgent blockers. Its decision titles are pointers, not duplicate specifications.
- A decision or system record owns its durable details. A procedure owns exact
  steps. Git owns transition history.
- An accepted normative decision remains governing until a later accepted decision
  explicitly supersedes it. Fresh live evidence may reveal drift from that decision;
  report both rather than silently overwriting either.
- For descriptive operational facts, report the freshest checkable evidence and its
  timestamp. If its freshness window has elapsed, say "last observed" or "unknown",
  not "current".

## Write-back

Checkpoint when a material decision, frontier, human gate, canonical artifact,
remote job/service state, or meaningful blocker changes, and before a likely switch
or context-loss boundary when material unrecorded work exists.

Use this order:

1. verify the change where possible;
2. edit the owning decision, system, or procedure record;
3. refresh `STATE.md` only if its small snapshot changed;
4. re-read changed owner sections at their actual paths and changed STATE completely,
   comparing them with the intended values;
5. review the Git diff and commit a coherent state transition when authorized.

Read-back confirms the local saved checkpoint at that observation time, even before
a commit; it does not prove media durability, upload completion, future freshness,
or cross-file atomicity. A failed read-back leaves completion unconfirmed; a mismatch
is a conflict. Preserve recoverable work and report directly if canonical writes are
unsafe. A coherent Git commit is the audit boundary; do not create a parallel handoff
log that can drift from the objects it summarizes.

## Writer and copy boundary

Coordinate one writer per canonical working copy; parallel agents/worktrees require
explicit ownership and serialized integration. Respect known roles/write restrictions
in the map and repository records; a current-looking mirror is not a writer. Resolve
uncertain authority before dependent writes, without default remote/replica inventory.

For cross-host continuation, checkpoint and review a named source commit, transfer
via Git or bundle, and verify receiving commit, dirty state, and required files.
Per-file sync guarantees no coherent Git/tree boundary. Git transport excludes dirty
edits and ignored private evidence; local RECOVER must preserve newer dirty work.
Record off-host recovery coverage or absence/unknown risk in the repository owner
when setting up or changing deployment, not as a new runtime subsystem.

Agent proposals remain `provisional`. They do not overwrite an `accepted` decision
without explicit human acceptance. See [the protocol](../docs/protocol.md) for the
full model.
