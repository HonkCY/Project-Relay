# Acceptance tests

These scenarios test the protocol rather than prose quality. Run agent tests in a
disposable clone or worktree. A run records: date, agent/product/version, starting
commit and dirty state, exact prompt, files/IDs read, answer or diff, external checks,
and pass/fail. Do not give the agent project facts in the prompt; discovery is what
the test measures.

The Coastwatch fixture is synthetic. Tests that claim native-agent compatibility
still require real clean Codex and Claude Code sessions before a production release.

## A — Fresh bootstrap

**Given:** A clean session with no useful chat history starts in
`examples/coastwatch/` at a recorded commit.

**When:** The only prompt is: “Bootstrap from this folder. Report the current
frontier, active work, accepted governing decisions, next human gate, urgent
unknowns, and where exact procedures and resources live.”

**Then:** Without hints, the agent discovers the native adapter, reads START and
STATE, and follows the linked IDs. It reports:

- S-14 disposition as the frontier and manual R-005 review as active work;
- D-001 and D-004 as accepted, while D-003 remains provisional;
- Dr. Rivera's D-003 decision as the next gate;
- D/R/P files as owners of deeper detail;
- R-011 as forensic rather than an operational blocker.

**Evidence:** Record the files/IDs the agent says it read and map every answer to one
owner. Fail if it needs chat context, misses an owner, promotes D-003, or imports the
whole corpus without task need.

## B — Claude → Codex → Claude switch

**Given:** A disposable template instance contains an accepted decision with the
non-default sentinel `alpha = 0.037`, a procedure whose exact order is “filter,
normalize, aggregate,” an active task that uses both, and no facts in the prompts.

**When:**

1. A fresh Claude Code session performs a meaningful fixture task, writes its output
   record and material state, reviews the Git diff, and exits.
2. A fresh Codex session receives only “Continue the active work from this folder,”
   verifies Claude's result, records a second material transition, and exits.
3. A second fresh Claude Code session receives the same generic continuation prompt.

**Then:** Each session discovers the exact sentinel and procedure order, continues
from the latest owning files, preserves authority/provenance/verification, and
produces a coherent diff/commit. No bespoke handoff prompt or agent-specific copy of
state appears.

**Evidence:** Save the three exact prompts, adapter/context discovery evidence,
before/after Git diffs, commits if created, and each agent's stated values. Fail on
`0.05`, reordered steps, duplicated live state, or reliance on previous chat.

## C — Compaction or session loss

**Given:** In a disposable workspace, persist one material change to its owning Relay
record but leave it uncommitted. Discuss a second, different change only in chat.
Terminate the session or compact away useful context.

**When:** A fresh session receives only “Recover the project from this folder and
state any uncertainty.”

**Then:** It inspects the dirty working tree, recovers the persisted canonical change,
does not discard it because it is uncommitted, and does not invent the chat-only
change. It marks the unrepresented interval uncertain if relevant.

**Evidence:** Record pre-loss diff, chat-only sentinel, recovery answer, and files
read. Fail if Git `HEAD` is treated as newer than a dirty canonical file or chat-only
work becomes fact.

## D — Migration with latent conversation context

**Given:** An incumbent native project has one operationally critical procedure only
in an accessible prior conversation. No provider export is supplied.

**When:** The incumbent follows MIGRATE, inventories that thread, and extracts the
procedure as an atomic candidate claim.

**Then:** The claim initially has `authority: provisional`, conversation/incumbent
provenance, a source locator/scope, and an honest verification result. It becomes a
canonical P record only after live/durable corroboration or explicit human acceptance
of the residual risk. Coverage remains partial or blocked while a required procedure
is unsafe to use.

**Evidence:** Capture the coverage row, MC record before/after, verification or human
acceptance, normalization ledger, and resulting P record. Fail if recollection is
immediately accepted or the conversation stays the only operational store.

## E — Migration with remote operational state

**Given:** The source project uses at least one remote host, a declared multi-terabyte
raw dataset, a derived artifact, one service, and one job or explicit absence of jobs.

**When:** MIGRATE audits the host and resource topology.

**Then:** Fresh bootstrap can identify each resource's role, safe locator, important
assets, inputs/outputs, readers/writers, producer job/procedure plus revision/run,
access/secret reference, observed state, and last verification. The Git repository
does not contain the bulk dataset or secret values.

**Evidence:** Compare remote inventory output to R records and measure repository
object size before/after migration. Fail if lineage is ambiguous, a private value is
copied, or “portability” means copying bulk data.

## F — False incumbent memory

**Given:** Incumbent memory says the current output is `/derived/v2/`, while current
config/filesystem evidence says `/derived/v3/`. Coastwatch MC-001/CF-001 is the
reference fixture.

**When:** MIGRATE corroborates the remembered path and a fresh agent bootstraps.

**Then:** The current observed record points to v3; v2 remains explicit
superseded/legacy or contradicted history; the conflict and evidence remain auditable.
The agent does not use v2 for current work. If an accepted intention had disagreed,
the result would be visible drift requiring human disposition rather than automatic
supersession.

**Evidence:** Capture MC/CF entries, config/live check, resulting D/R records, and
fresh-agent answer. Fail if the stale claim silently wins or silently disappears.

## G — Inaccessible source or unknown

**Given:** One historical conversation or remote host cannot be inspected. Coastwatch
CV-002/U-001 is the non-blocking forensic reference; create a separate operational-
critical variant.

**When:** Coverage and cutover are evaluated.

**Then:** The inaccessible row states attempts, impact, safe constraint, owner, next
action, and disposition. The forensic variant may cut over with human-approved
residual risk. The operational-critical variant fails until resolved, safely
constrained, or explicitly reclassified with rationale. Neither claims complete
history or a made-up percentage.

**Evidence:** Coverage rows, blind-spot record, gate result, and human disposition.
Fail if inaccessible becomes `pass`, is omitted, or is filled with confident prose.

## H — Background-job truth

**Given:** A prior conversation says “the agent is working; wait,” but no process,
scheduler entry, service, automation, or agent-run ID exists. Also include Coastwatch
R-007 (planned) and R-008 (expired running observation).

**When:** A fresh agent is asked, “What work is running, and will anything wake up
later?”

**Then:** It says the chat claim is not evidence, R-007 is not running, and R-008 is
currently unknown until P-004 rechecks the real ID. It promises no wake-up. A
`running` answer is allowed only after a fresh check records mechanism, host, ID,
log/output, observation time, freshness, owner, and next gate.

**Evidence:** Record the query/check result and answer. Fail on timeless `running`,
scheduled-without-scheduler, success inferred from queue absence, or autonomous
follow-up without a real mechanism.

## I — Public safety

**Given:** A fresh clone including all reachable Git history.

**When:** Review tracked files and history for credentials, private-key headers,
authorization headers, private host/data identifiers, raw motivating-project
transcripts, and non-sanitized example values. Confirm ignored files are not relied on
as portable canonical state. Useful baseline commands include:

```sh
git status --short --ignored
git grep -nEI 'BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|Authorization:[[:space:]]*Bearer' -- .
git log --all --stat --oneline
git log --all -p -- . ':(exclude)docs/acceptance-tests.md'
```

An established secret scanner MAY supplement these commands but is not required by
the protocol.

**Then:** No secret value, private locator, sensitive conversation excerpt, or
motivating-project datum exists in tracked content or reachable history. Examples use
reserved/synthetic locators. Secret records contain class and acquisition/config
references only.

**Evidence:** Save tool versions, commands, reviewed matches, and disposition. Fail
on any real secret/private datum; `.gitignore` alone is not a pass.

## Release interpretation

A–I are independent. One failure is not averaged away. A protocol release may label
real native-switch tests pending, but it must not claim those tests passed. Production
migration cutover additionally requires the project-specific operational gate in
`migration-kit/CUTOVER.md`.

