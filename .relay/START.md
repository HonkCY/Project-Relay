# Relay start

This directory is the canonical project workspace for the Project Relay framework
repository. The root agent files are adapters, not stores of project truth.

## Bootstrap

1. Read [STATE.md](STATE.md) completely.
2. Inspect `git status --short --branch`; uncommitted canonical files may be newer
   than `HEAD`.
3. Follow only the IDs and links relevant to the task:
   - [DECISIONS.md](DECISIONS.md) — governing and superseded choices
   - [RECORDS.md](RECORDS.md) — repositories, assets, tools, services, jobs, unknowns
   - [PROCEDURES.md](PROCEDURES.md) — exact repeatable operations
4. When a remembered claim conflicts with a canonical record or current evidence,
   stop treating the claim as fact. Record the conflict or unknown and verify it.

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
4. review the Git diff and commit a coherent state transition when authorized.

Saving the owning canonical files is the durable checkpoint. A coherent Git commit
is its audit boundary; do not create a parallel handoff log that can drift from the
objects it summarizes.

Agent proposals remain `provisional`. They do not overwrite an `accepted` decision
without explicit human acceptance. See [the protocol](../docs/protocol.md) for the
full model.
