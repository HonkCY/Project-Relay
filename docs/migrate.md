# MIGRATE protocol

MIGRATE externalizes an incumbent Codex or Claude Code project whose operational
truth is partly latent in native conversations, agent memory, tools, repositories,
remote systems, services, or jobs. It does not use provider export as a dependency.
The incumbent agent is a migration operator and witness, never automatic authority.

During migration, the three `migration-kit/` files form the canonical audit dossier.
After cutover they become read-only supporting provenance; ongoing truth moves to the
normal decision, record, procedure, and state owners.

## Tracks and success

Every audit surface belongs to one track:

- **Operational:** needed for a fresh agent to continue active work safely. This is
  the cutover gate.
- **Forensic:** deeper historical rationale, abandoned work, old experiments, and
  low-priority conversations. It may continue after cutover unless evidence shows
  that an item is operationally critical.

Migration never claims “100%” without a real, enumerated denominator. Coverage is a
table of surfaces and dispositions, summarized as total and unresolved operational
critical rows, supporting partials, and open forensic items.

## Phase 0 — Prepare the target, open the run, and set a watermark

MIGRATE must first create a usable destination; it does not assume Relay already
exists. The target may be the incumbent repository or a new folder.

1. Inspect the target's branch, working tree, existing adapters, ignore rules, and
   any `.relay/` directory. Preserve unrelated or uncommitted work.
2. Initialize Git if absent.
3. Copy `template/.relay/` only when no Relay workspace exists. Merge the thin
   `AGENTS.md`, `CLAUDE.md`, and ignore patterns using INIT steps 1–3; never overwrite
   existing instructions blindly.
4. Choose an empty active-dossier path. Use `.relay/migration/` for a first run. If
   that path already exists, inspect its migration ID. Resume a same-ID in-progress
   dossier in place without recopying; never resume or edit a frozen dossier. For a
   different or completed run, choose a new empty ID-scoped path such as
   `.relay/migrations/<migration-id>/`. Copy `migration-kit/AUDIT.md`, `COVERAGE.md`,
   and `CUTOVER.md` only into the newly chosen empty path, then replace run-boundary
   placeholders before linking it from canonical state.
5. As the final Phase-0 write, set target `STATE.md` to “migration in progress,”
   background execution `unknown`, and next human gate “operational cutover.” Its
   active-work entry MUST link the actual `AUDIT.md`, `COVERAGE.md`, and `CUTOVER.md`
   paths selected in step 4, making the in-progress dossier recoverable after a
   switch or compaction. It must not claim incumbent state yet.

These are shared scaffolding mechanics, not INIT eligibility or completion. The
incumbent project/environment remains the live operational workspace until cutover;
the incumbent agent remains only operator and witness, never authority.

At cutover, activate the already-tested candidate projection, remove STATE's
in-progress dossier links, and keep its normalized D/R/P links and frontier. The
frozen dossier remains reachable through migration-provenance links from those
records; it never becomes an unindexed second source of live truth.

Record migration ID, incumbent project and agent, operator, start time, audit horizon,
source branch/commit/dirty state, and intended target workspace. The watermark says
what moment the first inventory describes; a delta sweep will update it before
cutover.

In that existing run boundary and related repository `SRC` observations, identify
the incumbent live workspace, candidate target, known mirrors/backups, and who may
write each. Coordinate one writer per canonical working copy; parallel worktrees
need an explicit integration order. A received mirror does not gain write authority.
When file synchronization is known to apply, check task-relevant incomplete delivery,
conflict copies, and competing writes before affected operations; record limitations
using the existing unknown/conflict mechanism. No automatic sync discovery or new
coordination service is required.

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

For the incumbent session itself, inventory the native filesystem surface before
interpreting transcript content. Claude Code uses the literal
`CLAUDE_CODE_SESSION_ID`; Codex uses a non-empty `CODEX_THREAD_ID`, falling back to
`CODEX_SESSION_ID` only when the thread variable is absent. Record the identity
source, exact ID, configured native search boundary, and the related conversation or
session coverage row. Never infer the incumbent from modification time, “latest”
JSONL, or another session. A missing, unreadable, or ambiguous exact match is an
explicit limitation, not permission to substitute a conversation.

For every surface, record track, criticality, access result, inspection evidence,
gap, and disposition. `not-attempted` is distinct from `inaccessible`.

## Phase 2 — Inspect each domain

### Conversations and native context

Extract decisions, superseded/rejected choices, current versus obsolete conclusions,
conversation-only exact procedures, unresolved loops, referenced artifacts, and
operationally important rationale. Record a stable source locator when the product
exposes one; otherwise describe the bounded source and limitation. Do not paste
sensitive transcripts into a public workspace.

Before substantial extraction, attempt one lossless private snapshot of the exact
incumbent native session when its filesystem storage is accessible:

- Claude Code searches only
  `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/projects/**/<CLAUDE_CODE_SESSION_ID>.jsonl`.
  Alongside the exact primary JSONL, it may copy regular files below only the exact
  adjacent `<session-id>/` directory, such as `tool-results/` and `subagents/`.
- Codex searches only `${CODEX_HOME:-$HOME/.codex}/sessions/**/` for the current
  native basename form `rollout-YYYY-MM-DDTHH-MM-SS-<id>.jsonl`, then compares the
  parsed terminal `<id>` with the selected thread/session identity above. An
  unrecognized future filename format is `unavailable`; it does not relax into a
  suffix or recency guess.

Require one exact regular-file match. Do not follow nested symlinks, copy special
files, recurse into siblings, or inspect transcript content merely to identify the
session. Preserve bytes without semantic rewriting. Write only below
`.relay/private/migrations/<migration-id>/native-sessions/<harness>/<native-id>/`
at restrictive local permissions, after verifying the destination is ignored and no
`.relay/private/` path is tracked. A deterministic rerun replaces that one ID-scoped
snapshot instead of appending timestamped copies; an unavailable refresh preserves
the last successful snapshot.

The optional standard-library helper in
[`migration-kit/capture-native-session.py`](../migration-kit/capture-native-session.py)
implements these bounds. Invoke it from a Project Relay checkout, naming the target
workspace explicitly when it is a different folder:

```sh
python3 migration-kit/capture-native-session.py \
  --harness claude-code \
  --migration-id 2026-09-05-project \
  --repo-root /path/to/target-workspace
```

Use `--harness codex` for Codex. The helper returns metadata only and does not parse
or print transcript content. Handled outcomes are `captured`, `partial`,
`unavailable`, and `inaccessible`; missing or ambiguous identity matches are handled
outcomes rather than newest-file fallbacks. An equivalent native copy operation may
be used when Python is unavailable, but it MUST enforce the same identity, path,
symlink, byte-preservation, privacy, digest, and refresh rules.

Attach the result to the existing conversation/session `SRC` note and coverage row.
Record the harness, identity source and ID, safe original locator, private snapshot
locator, captured-through watermark, bounded surface/file count, bytes, primary
SHA-256, private-manifest SHA-256, result, and limitations. Keep absolute local paths,
companion per-file names, and raw bytes in the private manifest. A snapshot proves
only which bytes were copied; it does not verify the transcript's claims, replace
conversation enumeration or extraction, or change authority. Because the incumbent
session is still live, always say “native session snapshot captured through
`<timestamp>`,” not “final” or “complete.” A platform SessionEnd hook may be
considered later, but is not a migration dependency.

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

Reuse repository record locator, role, readers/writers, evidence, recheck, and
risks/limitations fields to distinguish the live canonical workspace from derived
mirrors and archive backups. An off-host backup SHOULD exist where practical;
record the recovery limitation if absent or unverified. A configured remote is
not proof of a received backup. If cutover or continuation crosses hosts, identify
the Git transport or bundle and the named commit the receiver must check, along
with required canonical files and any receiving dirty-state overlay.

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
or specification reference, working directory and revision, inputs, outputs/logs,
submit/start times, observed state and timestamp, check command/result/evidence,
output validation, owner, next human gate, and recovery. Recurring work also records
the scheduler/automation entry, schedule, next-run evidence, and disable procedure.
If an identifier or live check is missing, record a verified absence, `planned`, or
“current state unknown; last observed …” as evidence permits.

### Procedures, dependencies, and secrets

Reconstruct exact environment/build/test/deploy/reproduce/maintain/recovery steps.
Test operationally critical procedures where safe. Record secret class, configuration
location, and authorized acquisition process; never copy values into canonical files.

## Phase 3 — Extract candidate claims

Each consequential interpretive, recalled, conflicting, or otherwise transformed
claim normalized through `AUDIT.md` contains:

- claim ID and exact statement;
- criticality and operational/forensic track;
- authority (`provisional` initially);
- provenance basis at claim level;
- verification result at claim level;
- evidence locator and observation time;
- limitations or scope;
- intended canonical destination;
- conflict/unknown link and disposition.

Mixed-source records keep claim-level evidence. One live check must not upgrade an
entire remembered narrative. A directly observed resource, environment, tool, or
exact-procedure field MAY normalize from a named `SRC` observation without a
redundant `MC` entry when no interpretation, normative choice, or transformation
occurs; its destination record still links that source as migration provenance.

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

- current frontier and next gate to a candidate projection in `STATE.md`;
- normative choices to `DECISIONS.md`;
- resources/tools/services/jobs, unknowns, and lineage to `RECORDS.md`;
- exact operations to `PROCEDURES.md`.

Until cutover, that snapshot MUST say `migration candidate — not cut over`, identify
the incumbent project/environment as the live operational workspace, state that the
incumbent agent remains only operator/witness, name `operational cutover` as the
current migration gate, and retain links to the active dossier. In a separately
labelled candidate projection it exposes the proposed post-cutover frontier, active
work, and next operational human gate for testing without prematurely declaring the
destination authoritative.

Link every normalized destination back to its migration `MC`, `CF`, `U`, or direct
`SRC` evidence ID. When more than one dossier exists, use a path-qualified Markdown
backlink (or migration-ID-namespaced identifier) so a bare `SRC-001` cannot refer to
two runs. Recollection-only claims remain provisional unless an authorized human
explicitly accepts the residual risk. Avoid copying the audit narrative into
canonical files; each fact has one ongoing owner.

## Phase 6 — Delta sweep

Immediately before validation, recheck surfaces likely to have changed during the
migration: branch and dirty state, recent material conversations, active jobs,
service health, remote outputs, and human decisions. Update the watermark, coverage,
and canonical records. A migration that ignores known drift cannot pass cutover.

Rerun the exact-ID native-session capture into the same deterministic private
destination. Record the Phase-6 attempt, refreshed captured-through watermark,
bounded surface, bytes and digests in the same `SRC` provenance entry and in the
`CUTOVER.md` delta row. If the exact source has become unavailable or inaccessible,
record that result and limitation without replacing a prior successful snapshot or
guessing another session. This refresh narrows the live-session tail; it does not
claim to include writes made after its watermark.

Apply [CHECKPOINT / WRITE-BACK](protocol.md#checkpoint--write-back)
to the changed owners, candidate STATE, and affected dossier sections: reopen their
bounded sections at the intended paths and compare the expected changes. Use the
existing delta rows and source observations for the check and any discrepancy;
do not create a parallel checkpoint log. Complete paginated/truncated reads before
classifying a missing value. A successful write response alone does not complete the
checkpoint, and read-back proves only locally observed content at that time, not
physical persistence or delivery to another host.

Inspect the resulting diff and commit a clean candidate boundary. This commit
contains the normalized D/R/P owners and the explicitly non-cutover candidate STATE;
it is the exact boundary tested in Phase 7.

For a receiving host, verify the named candidate commit, required canonical files,
and relevant dirty-state/conflict observations there before declaring the handoff
ready for Phase 7. Sequential file synchronization does not by itself establish
that commit boundary; uncommitted source edits are not transported by Git or a bundle.

## Phase 7 — Fresh-agent dry run

Start a genuinely fresh native-agent session from the clean candidate commit, with no
bespoke handoff explanation. It must recover the candidate frontier, active work,
governing accepted decisions, proposed post-cutover next human gate, critical
resources/procedures, and truthful current or unknown job/service state. It must also
report that cutover has not occurred, `operational cutover` is the current migration
gate, the incumbent project/environment remains live, and the incumbent agent is only
operator/witness.

Test one safe task-relevant operation or verification. Record the exact candidate
commit, agent, start condition, questions asked, records read, answers, discrepancies,
and pass/fail in `CUTOVER.md`. If the run exposes a material defect, correct its owner,
repeat the delta sweep, commit a new candidate, and rerun Phase 7.

Apply the normal bounded bootstrap integrity checks: required snapshot meaning must
be present, and any task-required stable ID must resolve to one owner in this
workspace. Explicit `none`/`unknown` differs from an empty or missing safety field;
heading variants are valid. A tool's truncated output requires completing the read,
not immediately diagnosing damaged storage. Resolve task-relevant owner ambiguity
or inconsistent candidate files through existing conflict/unknown rules.

The dry run MUST succeed when `.relay/private/` is absent. It MUST NOT ingest or
require a native transcript snapshot; only tracked canonical owners and their safe
supporting provenance are portable.

## Phase 8 — Operational cutover

After a fresh-agent run passes, commit its dossier evidence as an immutable
pre-cutover review boundary. This evidence commit MUST NOT change material
operational truth from the candidate that was tested; if it does, return to Phase 6
and rerun. Obtain the resulting commit hash; the human reviews exactly that boundary.

Cutover passes only when:

- every required domain has an inventory scope and no operational/critical surface
  remains `not-attempted`;
- every coverage row obeys the access/result/disposition state matrix; inaccessible
  evidence never becomes `pass` or `n/a`;
- no operational coverage row remains `pending` or `backlog`, and no coverage row
  remains `blocked`;
- no forensic coverage row remains `pending`; each open forensic row is a named
  backlog entry with owner, value, next action, and recheck condition;
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

If the human rejects the boundary or requires changes, record that disposition but
keep the dossier active and do not cut over, freeze, or tag. Correct the owning
records, return to Phase 6, create a new candidate, and rerun Phase 7. Only an
approved boundary proceeds below.

On acceptance, change STATE from candidate to active canonical state and remove its
live active-dossier links; provenance backlinks keep the frozen dossier reachable.
Record approver, time, the reviewed pre-cutover commit, and the intended cutover-tag
name in `CUTOVER.md`. Read back the changed STATE and CUTOVER sections using the same
checkpoint rule. Commit only that cutover transition, then create the named
annotated tag at the decision commit. The tag identifies the transition without a
self-referential hash in the commit. From cutover onward, the old native-agent project
context, chat, and memory are non-canonical witnesses; the underlying target
repository and external systems retain exactly the authority recorded in D/R owners.

## Phase 9 — Forensic continuation

Continue the already-disposed forensic backlog without mutating the frozen migration
dossier. Record later evidence in normal canonical owners or a dated migration
addendum. If later evidence makes an item operational, reclassify it and surface it in
`STATE.md`; never leave a newly critical gap hidden behind the prior cutover.
