# MIGRATE protocol

MIGRATE externalizes an incumbent Codex or Claude Code project whose operational
truth is partly latent in native conversations, agent memory, tools, repositories,
remote systems, services, or jobs. It does not use provider export as a dependency.
The incumbent agent is a migration operator and witness, never automatic authority.

Copy the three files from `migration-kit/` into `.relay/migration/`. During migration
they form the canonical audit dossier. After cutover they become read-only supporting
provenance; ongoing truth moves to the normal decision, system, procedure, and state
owners.

## Tracks and success

Every audit surface belongs to one track:

- **Operational:** needed for a fresh agent to continue active work safely. This is
  the cutover gate.
- **Forensic:** deeper historical rationale, abandoned work, old experiments, and
  low-priority conversations. It may continue after cutover unless evidence shows
  that an item is operationally critical.

Migration never claims “100%” without a real, enumerated denominator. Coverage is a
table of surfaces and dispositions, summarized as counts of operational blockers,
supporting partials, and open forensic items.

## Phase 0 — Open the run and set a watermark

Record migration ID, incumbent project and agent, operator, start time, audit horizon,
source branch/commit/dirty state, and intended target workspace. The watermark says
what moment the first inventory describes; a delta sweep will update it before
cutover.

All extracted candidate claims start `provisional`. Do not edit accepted destination
decisions merely because the incumbent remembers something different.

## Phase 1 — Inventory surfaces before interpreting them

Create the coverage denominator first. Add one row for each known source or bounded
surface in these required domains:

1. accessible project conversations, threads, and sessions;
2. native project instructions, project/auto-memory, and model-specific conventions;
3. MCP servers, tools, and connectors;
4. local repositories, worktrees, branches, commits, tags, and dirty state;
5. remote hosts and important directory/resource topology;
6. assets and lineage;
7. services;
8. active, recurring, pending, failed, and relevant legacy jobs;
9. environment, build, test, deploy, start, reproduce, update, maintenance, and recovery;
10. external dependencies and secret references;
11. unknown or inaccessible sources.

“Every accessible conversation” means enumerate using the incumbent product's
available listing/navigation, then record the scope used. It does not mean claiming
inaccessible or undiscoverable history was read. Add those as blind spots.

For every surface, record track, criticality, access result, inspection evidence,
gap, and disposition. `not-attempted` is distinct from `inaccessible`.

## Phase 2 — Inspect each domain

### Conversations and native context

Extract decisions, superseded/rejected choices, current versus obsolete conclusions,
conversation-only exact procedures, unresolved loops, referenced artifacts, and
operationally important rationale. Record a stable source locator when the product
exposes one; otherwise describe the bounded source and limitation. Do not paste
sensitive transcripts into a public workspace.

### Instructions and memory

Classify every material item as neutral project truth, agent-specific behavior,
stale assumption, personal preference, or irrelevant. Neutral truth becomes a
candidate record. Agent-specific behavior may remain in an adapter only when needed.
Stale assumptions are rejected/superseded explicitly; auto-memory never migrates as
authority merely because it was loaded.

### Tools and MCPs

Capture identity, purpose, required/optional status, dependent project functions,
capabilities actually used, configuration locator, secret/auth class without values,
and replacement/recovery notes. Verify configuration where accessible.

### Local Git topology

Record each repository/worktree role, branch, relevant commits/tags, dirty files,
generated versus tracked material, and relationships among repositories. Do not
clean or commit incumbent work merely to make migration look tidy.

### Remote hosts, resources, and lineage

Inspect important host aliases and directories. For every material resource capture
role, purpose/key assets, inputs, outputs, readers/writers, producer job/procedure and
commit/version/run, lifecycle state, access method, safe secret reference, and last
verification. Prefer locators and provenance over copying large data.

### Services

Separate desired state from observed state. Capture host/runtime/endpoint, source and
config, lifecycle procedure IDs, health check plus result/time/evidence, dependencies,
build/deploy/update, logs, persistent state, and risk. “Should be running” does not
make observed state `running`.

### Jobs

Capture execution mechanism, host/scheduler, real process/job/run ID, exact command
or specification, working directory and revision, inputs, outputs/logs, submit/start
times, observed state and timestamp, check command/result/evidence, output validation,
owner, next human gate, and recovery. If an identifier or live check is missing,
record `planned`, `absent`, `last observed`, or `unknown` as evidence permits.

### Procedures, dependencies, and secrets

Reconstruct exact environment/build/test/deploy/reproduce/maintain/recovery steps.
Test operationally critical procedures where safe. Record secret class, configuration
location, and authorized acquisition process; never copy values into canonical files.

## Phase 3 — Extract candidate claims

Each consequential claim in `AUDIT.md` contains:

- claim ID and exact statement;
- impact and operational/forensic track;
- authority (`provisional` initially);
- provenance basis at claim level;
- verification result at claim level;
- evidence locator and observation time;
- limitations or scope;
- intended canonical destination;
- conflict/unknown link and disposition.

Mixed-source records keep claim-level evidence. One live check must not upgrade an
entire remembered narrative.

## Phase 4 — Corroborate and resolve conflicts

Verify high-impact recollection against the live filesystem/server/process/scheduler,
Git, configuration, logs, and current artifacts where practical. Keep the incumbent
claim and contradicting evidence in the conflict log until disposition.

If memory says `/srv/v1` and live configuration shows `/srv/v2`, `/srv/v2` is the
current observed locator; `/srv/v1` remains a superseded or contradicted historical
claim. Live evidence does not independently supersede an accepted human intention;
that mismatch is operational drift requiring human disposition.

## Phase 5 — Normalize into canonical Relay objects

Promote only disposed claims:

- current frontier and next gate to `STATE.md`;
- normative choices to `DECISIONS.md`;
- resources/tools/services/jobs, unknowns, and lineage to `RECORDS.md`;
- exact operations to `PROCEDURES.md`.

Link promoted records back to migration claim/evidence IDs. Recollection-only claims
remain provisional unless an authorized human explicitly accepts the residual risk.
Avoid copying the audit narrative into canonical files; each fact has one ongoing
owner.

## Phase 6 — Delta sweep

Immediately before validation, recheck surfaces likely to have changed during the
migration: branch and dirty state, recent material conversations, active jobs,
service health, remote outputs, and human decisions. Update the watermark, coverage,
and canonical records. A migration that ignores known drift cannot pass cutover.

## Phase 7 — Fresh-agent dry run

Start a genuinely fresh native-agent session with no bespoke handoff explanation.
It must recover frontier, active work, governing accepted decisions, next human gate,
critical resources/procedures, and truthful current or unknown job/service state.

Test one safe task-relevant operation or verification. Record agent, start condition,
questions asked, records read, answers, discrepancies, and pass/fail in `CUTOVER.md`.

## Phase 8 — Operational cutover

Cutover passes only when:

- every required domain has an inventory scope and no operational-critical surface
  remains `not-attempted`;
- every operational-critical item has a disposition;
- no unresolved critical unknown or conflict permits unsafe continuation;
- frontier, active work, decisions, next gate, and required procedures are canonical;
- critical remote resources are locatable with enough lineage and access references;
- job/service reports use checkable, time-stamped observed state;
- false-memory conflicts have explicit disposition;
- the fresh-agent dry run passes;
- an authorized human accepts residual non-blocking risks and the cutover boundary.

Human risk acceptance is not a magic bypass for an unsafe operational blocker. The
operator must resolve it, impose a safe constraint/workaround, or have the human
explicitly reclassify its impact with rationale.

Record approver, time, and cutover commit after that commit exists. Do not place a
future self-referential hash inside the commit. From cutover onward, the old project,
chat, and memory are non-canonical witnesses.

## Phase 9 — Forensic continuation

Move open non-blocking history to the forensic backlog with owner, value, and recheck
condition. If later evidence makes an item operational, reclassify it and surface it
in `STATE.md`; never leave a newly critical gap hidden behind the prior cutover.
