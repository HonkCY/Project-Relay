# Project Relay protocol v0.1

This document is normative for v0.1. “MUST”, “SHOULD”, and “MAY” express requirement
strength. Project-specific canonical truth lives under `.relay/`, not here.

## Design boundary

Relay makes a Git folder the durable project brain while Codex, Claude Code, or a
future native coding agent remains the harness. Relay does not launch agents, call
model APIs, provide a UI, run a scheduler, or promise future autonomous execution.

The normal switch is deliberately boring: checkpoint material work, exit one agent,
open another agent in the same folder, and let it bootstrap from tracked state.

## Default workspace layout

```text
AGENTS.md               thin shared native adapter
CLAUDE.md               Claude import of AGENTS.md
.relay/
  START.md              stable bootstrap rules and index; always read
  STATE.md              small current snapshot; always read
  DECISIONS.md          durable normative records
  RECORDS.md            resources, assets, environments, tools, services, jobs, unknowns
  PROCEDURES.md         exact operational procedures and contracts
```

`START.md` and `STATE.md` are the only mandatory Relay reads at bootstrap. The
adapter MUST point to them. `START.md` indexes deeper files, and `STATE.md` MUST use
stable record IDs or links for important details instead of copying specifications.

All five `.relay/` files are canonical. Their ownership is disjoint:

- `STATE.md` owns current coordination state.
- `DECISIONS.md` owns normative decisions and their supersession.
- `RECORDS.md` owns current operational entity records, lineage, and durable unknowns.
- `PROCEDURES.md` owns exact repeatable operations.
- `START.md` owns the local map and write-back rules, not project facts.

Small evidence safe for Git MAY live under `.relay/evidence/`; it is supporting,
not canonical by itself. Large or sensitive evidence stays external and is named by
a safe locator. `.relay/private/` is ignored by the default template and MUST NOT be
treated as portable canonical state.

## Canonical object model

Relay uses three objects. The distinction is semantic, not one-file-per-type.

### 1. Snapshot

A single edited-in-place view containing:

- current frontier;
- active work;
- next human gate;
- links to governing decisions;
- urgent blockers, conflicts, and unknowns;
- an explicit background-execution summary.

It SHOULD fit on one screen or a few hundred lines at most. Historical narrative
belongs in records or Git history.

### 2. Record

A stable-ID entry for a decision or operational entity. Resources, datasets,
artifacts, environments, repositories, remote hosts, tools, MCPs, services, and jobs
are record kinds, not separate databases. Unknown is a valid field value and may
also be a record when the blind spot itself must be tracked.

Decision records live separately from system records because they have different
review and retrieval patterns, not because they use a different epistemology.

### 3. Procedure

A stable-ID runbook or contract containing prerequisites, exact steps, outputs,
verification, and recovery. A prose claim that work is reproducible is not a
procedure.

## Authority, provenance, and verification

Relay separates governance, evidence source, and the result of checking that source.

### Authority

Every consequential record uses one value:

- `accepted` — explicitly accepted by an authorized human, or directly imposed by
  an authoritative human-supplied project brief;
- `provisional` — usable working state not yet accepted for a consequential choice;
- `superseded` — formerly applicable, now replaced by a named record;
- `rejected` — considered and explicitly not adopted;
- `unresolved` — no safe disposition yet.

Agents MAY create or update provisional records. They MUST NOT promote a
consequential choice to accepted, or replace an accepted decision, without explicit
human acceptance. Superseded and rejected records remain discoverable with reason
and links.

### Provenance

Each consequential claim uses one or more basis labels:

- `live-environment` — current filesystem, host, process, scheduler, or service;
- `durable-artifact` — file, Git object, log, artifact, or tool configuration;
- `incumbent-recall` — reconstructed from native conversation context or agent memory;
- `human-report` — stated by a human but not necessarily independently checked;
- `inference` — reasoned from named evidence rather than directly observed;
- `unknown` — source is unavailable or the claim cannot presently be checked.

### Verification

Each consequential claim also has one check result:

- `verified` — the named evidence was checked and supports the scoped claim;
- `unverified` — it has not been checked sufficiently;
- `contradicted` — named evidence conflicts with it;
- `stale` — a formerly relevant observation is outside its freshness condition;
- `inaccessible` — the source could not be inspected.

Records MUST include `evidence ref` and `checked at`; use `none` or `unknown` rather
than inventing them. Time-sensitive facts SHOULD include `valid until` or a stated
recheck condition. A mixed-source record MUST put provenance and verification at the
claim or field level when one envelope would falsely upgrade the whole record.

`accepted` does not mean empirically verified, and `verified` does not mean policy
approved. If live evidence contradicts an accepted intended state, record operational
drift and preserve the decision until a human changes it. `incumbent-recall` alone
MUST NOT become accepted during migration.

### Conflict rule

For normative choices, the newest explicitly accepted, non-superseded decision
governs. For descriptive facts, the freshest relevant checkable evidence governs
the report. A conflict between the two is visible drift, not permission to rewrite
history. If evidence cannot settle a consequential conflict, status is `unresolved`
or provenance is `unknown` and the next human gate MUST expose it.

## Record requirements

Every record has:

- stable ID and concise title;
- kind;
- authority;
- provenance;
- verification;
- purpose or claim;
- safe evidence reference;
- checked-at timestamp or date;
- status and risk/unknown when relevant;
- relationships to inputs, outputs, dependencies, successor, or superseded record.

Type-specific minimums follow.

### Resources, assets, repositories, and environments

Record locator and role (`source`, `canonical`, `derived`, `cache`, `scratch`,
`archive`, or `legacy`), important contents, inputs, outputs, readers/writers,
producer procedure plus version/run/commit, access method, last verification, and
active/legacy state. A remote topology record describes important directories by
these same fields. It SHOULD point to large data rather than copy it.

### Tools and MCPs

Record identity, purpose, required/optional status, dependent project functions,
important capabilities used, configuration locator, authentication or secret class
without values, and replacement/recovery notes.

### Services

Record purpose, host/location, endpoint or port when safe, source/config locator,
start/stop/restart procedure IDs, health check, dependencies, build/deploy/update
procedure, logs, persistent state, operational risks, and last verified state.

### Jobs and truthful background state

A job uses one of `planned`, `queued`, `running`, `blocked`, `succeeded`, `failed`,
`cancelled`, or `unknown`. `planned` is never running.

`queued` or `running` requires all of:

- a real execution mechanism (process, scheduler, service, automation, or agent run);
- host and command/specification reference;
- runtime process/job/run identifier;
- output or log locator;
- start/submission time;
- current-status evidence with `checked at` and `valid until` or recheck rule;
- owner and next human gate.

After evidence expires, an agent says “last observed running at …; current state
unknown” until it rechecks. A chat statement, plan, checkpoint, or word “wait” is not
execution evidence. Scheduled work also requires a real scheduler/automation ID and
next-run evidence. Relay never implies a conversational agent will wake itself.

## BOOTSTRAP

A fresh agent MUST:

1. read its native adapter;
2. read `.relay/START.md` and `.relay/STATE.md` completely;
3. inspect the Git branch and working tree;
4. follow only task-relevant IDs into deeper canonical files;
5. verify time-sensitive external state before presenting it as current;
6. state unknown or last-observed conditions without filling gaps from memory.

The result is a compact working set: frontier, active work, governing choices, next
human gate, and pointers to exact detail. Re-bootstrap after compaction using the
same sequence. A compaction summary MAY help locate a record but never overrides it.

## CHECKPOINT / WRITE-BACK

A checkpoint write-back is required promptly when any of these materially changes:

- an accepted or proposed consequential decision;
- project frontier, active work, or next human gate;
- canonical artifact identity, lineage, or version;
- real job, service, remote-resource, or deployment state;
- an exact procedure needed for continuation or recovery;
- a meaningful blocker, conflict, or unknown;
- work that would otherwise be lost at a switch, compaction, crash, or session exit.

Do not checkpoint commentary, exploration with no durable consequence, unchanged
polls, or every turn. For long-running actions, record the real job immediately
after submission and write back again only on a material status transition.

Write owning records first, then the snapshot only if it changed. Once saved, those
canonical files are the durable checkpoint even before a commit, which makes abrupt
session loss recoverable. Review the diff and commit coherent accepted or operational
transitions when authorized. Git is the transition history; never add a parallel
state-dump log or write a future commit hash into the commit it purports to name.

## SWITCH

Before a planned switch, the current agent applies the materiality test and writes
back any unrecorded material state. The user exits and opens the other native agent
in the same folder. The new agent bootstraps normally; no handoff prompt is needed.

If the previous agent vanished, the new one uses the last durable canonical state,
inspects the working tree and external evidence, and marks work not represented in
canonical files as uncertain. It does not reconstruct the missing interval as fact.

## VERIFY

Verification is a record update, not merely a conversational assurance:

1. identify the exact claim and its authority/provenance;
2. inspect the named current environment or durable evidence;
3. record observation, locator, checker, and time;
4. capture conflicts and freshness limits;
5. change authority only if the human-governance rule permits it.

## INIT and MIGRATE

INIT creates Relay for a new or already self-contained project. MIGRATE reconstructs
an operational project from an incumbent native-agent context and external systems.
They have separate protocols: [INIT](init.md) and [MIGRATE](migrate.md). Any material
latent chat/memory, inaccessible history, remote state, service, or job moves the
task to MIGRATE.

## Git semantics

- Canonical current values are edited in place; Git retains their history.
- Superseded/rejected decisions remain in place with explicit links.
- Commits group coherent state transitions, not arbitrary agent turns.
- Generated bulk data, secrets, volatile logs, and caches stay out of Git; records
  carry safe locators and lineage.
- Dirty state may contain the newest durable canonical state and is not an error
  to discard automatically.

## Scaling and retrieval

Use filenames, headings, stable IDs, links, and ordinary text search first. Because
`.relay/` is hidden, commands that rely on default ignore behavior MUST name it
explicitly or use `rg --hidden --glob '!.git/**'`. If a
canonical file becomes costly to scan (a practical default is about 400 lines or
frequent merge conflicts), shard it by stable domain under `.relay/records/` or
`.relay/procedures/` and update `START.md`. Do not change IDs or retain a duplicated
aggregate copy.

Semantic retrieval is a future optional index. Any index MUST be rebuildable from
canonical Markdown, non-authoritative, and unnecessary for bootstrap or recovery.

## Security and public safety

Store secret class and acquisition/configuration references, never values. Do not
commit private hostnames, raw conversation excerpts, tokens, SSH material, private
dataset identifiers, or sensitive logs to a public workspace. Sanitized examples
use reserved domains. `.gitignore` is defense in depth, not proof of safety; public
release still requires the public-safety acceptance test.
