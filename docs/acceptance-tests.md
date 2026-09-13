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
STATE, uses linked stable IDs as authoritative on-demand pointers, and follows only
those required by the task. It reports:

- S-14 disposition as the frontier and manual R-005 review as active work;
- D-001 and D-004 as accepted, while D-003 remains provisional;
- Dr. Rivera's D-003 decision as the next gate;
- D/R/P files as owners of deeper detail;
- R-011 as forensic rather than an operational blocker.

**Evidence:** Record the files/IDs the agent says it read and map every answer to one
owner. Fail if it needs chat context, misses an owner, promotes D-003, follows a
linked ID without task need, or imports the whole corpus or broadly inventories a
registry without task need.

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

## Post-v0.1 MIGRATE enhancement — native-session forensic snapshot

This bounded conformance check is additive. It does not modify the sealed A–I rubric
or historical native A/B evidence.

**Given:** A temporary target Git workspace ignores `.relay/private/`. Synthetic
Claude Code and Codex native-storage roots contain an exact incumbent transcript,
newer and similarly named decoys, and, for Claude Code, an exact adjacent session
directory with bounded artifacts. Additional cases omit the exact transcript, make
it ambiguous, use a custom `CODEX_HOME`, and expose a symlinked artifact.

**When:** Run `migration-kit/capture-native-session.py` once in the early migration
phase and again as a Phase-6 refresh, using only `CLAUDE_CODE_SESSION_ID` or the Codex
`CODEX_THREAD_ID`-then-`CODEX_SESSION_ID` precedence.

**Then:** The helper copies the exact primary bytes and only bounded regular
associated artifacts, never selects by recency, never follows a symlink, hashes the
snapshot bytes, records a live-session watermark and limitation, and refreshes one
stable ID-scoped private destination. A zero or ambiguous match records
`unavailable`; an unsafe/unreadable match records `inaccessible`; neither substitutes
another session. A failed refresh preserves the last successful snapshot.

The private path is ignored and untracked, source content and modification time are
unchanged, and deleting `.relay/private/` leaves START/STATE bootstrap intact.
Tracked dossier fields contain metadata only; raw transcript content and detailed
private file paths remain private. Fresh-agent continuation never depends on the
snapshot.

**Evidence:** Run:

```sh
python3 -m unittest discover -s tests -v
git check-ignore -v .relay/private/migrations/probe/native-sessions/codex/probe
git ls-files -- .relay/private
```

Fail on a wrong-session selection, transcript rewriting, unbounded companion copy,
symlink traversal, digest mismatch, timestamped duplicate accumulation, loss of a
prior good snapshot after a failed refresh, tracked private output, or any bootstrap
dependency on `.relay/private/`.

## v0.2 workspace-integrity conformance

These checks are additive. The A–I prompts and pass/fail criteria, the forensic
snapshot rubric above, and all sealed evidence remain unchanged. Use new disposable
fixtures and a recorded v0.2 candidate boundary. The
[fixture instructions](../tests/README-workspace-integrity.md) describe mechanical
setup and native evidence; the [upgrade guide](upgrade-v0.2.md) describes the scoped
merge into an existing workspace.

**Given:** Synthetic workspaces use the candidate's thin adapters and START rules.
They separately expose the faults and valid alternatives below. Record the template
candidate commit, fixture baseline commit, and full starting dirty/untracked state;
a baseline commit alone does not identify an uncommitted fault.

**When:** A genuinely fresh native agent receives the recorded bootstrap,
continuation, recovery, or task-required owner prompt. Do not give it the answer,
required file list, or bespoke recovery explanation. For write cases, request the
bounded fixture operation and observe actual writes and subsequent reads.

**Then:**

| Boundary | Required result |
| --- | --- |
| Mandatory snapshot content | Native adapter, START, and STATE are read; the existing snapshot supplies frontier, active work, gate, urgent unknowns, and background safety meaning. Empty/missing content is not inferred as `none`. Explicit `unknown` is valid and remains unknown. |
| Valid headings and tool pagination | Semantically complete heading variants pass. Truncated or paginated tool output is completed with a bounded follow-up before diagnosing a file defect. A readable zero-byte or incomplete snapshot is incomplete, not `inaccessible`; inability to inspect a source is reported separately. |
| Required-ID resolution | Only task-required owners are followed. A missing owner or duplicate definition in the current canonical owner is surfaced, not guessed. The same ID in another workspace, fenced example, historical evidence, or frozen dossier is not automatically a collision. |
| Visible conflict copy | A task-relevant contradictory copy exposed by status or the workspace map is treated as uncertainty until its authority is resolved. Filename resemblance or recency cannot elect an owner. No global duplicate-ID scan is required. |
| Failed save/read-back | A fixture operation reports write success but the expected new value is absent on bounded read-back. The agent identifies the intended path/value mismatch and does not claim checkpoint completion. Successful cases reopen the changed owner/STATE sections and confirm their expected values. |
| Mirror write request | A copy whose relevant repository owner grants no canonical write authority cannot become a writer merely because it received files or a task asks for a change. The agent exposes the boundary and stops affected canonical writes until an authorized workspace or integration path is established. |
| Partial replica | A task requires a stable ID referenced by STATE but absent from its designated owner. The agent reports the missing dependency and constrains affected work; it does not reconstruct the record from chat, a different workspace, or a guessed newest file. |
| Named commit and dirty recovery | Cross-host handoff names a coherent commit and checks that the receiver has that commit, the required canonical files, and no unresolved relevant dirty overlay. Source edits not committed are not claimed to be transferred. Local recovery still uses newer uncommitted canonical edits and preserves unrelated dirty work. |
| Backup limitation | A configured remote alone cannot establish a received off-host backup. The repository record distinguishes a checked backup from an absent or unverified one and records its recovery limitation using existing fields. Absence of a backup alone does not create a mandatory runtime dependency or block otherwise safe local work. |

Across these cases, follow the original answer-first stopping rule. Do not expand
unrelated registries, migration dossiers, or evidence merely to build confidence.
Use the existing authority, verification, conflict, and unknown semantics; checks
do not grant decision acceptance. Read-back establishes content observed at a local
path and time, not fsync, cross-file atomicity, future persistence, or completed
replication. A structurally complete but stale snapshot remains a limitation.

**Evidence:** Mechanical tests must establish the synthetic fault or Git boundary
they claim to test; they cannot claim a native semantic pass. Native runs separately
record exact prompts, product/model/version, adapter/START/STATE discovery, exact
files/IDs/sections read, operation and read-back results, semantic answers/diffs,
pass/fail, and any unrelated registry/migration/evidence reads. Run the existing
native-session capture tests as regression. Keep raw native transcripts private and
publish only sanitized evidence appropriate to the repository.

Fail on an unsupported `none`/`inaccessible` conclusion, heading-only rejection,
guessed owner, unauthorized mirror write, discarded dirty recovery state, checkpoint
success without expected read-back, unverified handoff/backup success claim, or
task-unnecessary corpus expansion. A passing fixture setup test cannot compensate
for a native behavioral failure.

Before a v0.2 release gate, rerun native Scenario A for fresh Claude Code and Codex,
Scenario B's complete Claude → Codex → Claude chain, and Scenario C recovery. A and
the final B chain must pass at the same final candidate boundary after remediation
stabilizes. Preserve the original prompts and semantic expectations, record new
evidence separately, and return to human review; historical v0.1 A/B results do not
prove this changed bootstrap/checkpoint boundary.

## Reader-mode conformance — review candidate

R1–R10 are additive. All A–I prompts/criteria, the private forensic snapshot rubric,
the v0.2 integrity rubric, native regression gates, and historical evidence above
remain unchanged. Use only newly generated synthetic sources, evidence, data and
local mock interfaces. Do not inspect a real workspace, private connector, actual
native history, or remote host for these cases without separate authorization.

**Given:** A disposable fixture identifies the candidate adapters/START, synthetic
source boundary and relevant dirty/non-Git bytes, external task authorization,
exclusive output/scratch/cache roots, and bounded mock R/P access. Source context
contains no Reader-global flag. A non-Git read-only snapshot has its own declared
identity and limitations; it must not acquire Git as a bootstrap repair.

**When:** Fresh agents receive short task prompts that specify Reader, the source,
the bounded investigation, the exclusive output, and the stop condition, but no
fixture answers. Recovery receives the saved task entry rather than prior chat.
Integration is a separate explicitly authorized Maintainer operation.

**Then:**

| Case | Required result |
| --- | --- |
| R1 — Useful Reader delivery | Discover adapter/START/STATE and only task-required owners/evidence. Retrieve authorized original text and deliver a located comparison in the separate output. Preserve source Relay, code/data/evidence and protected Git branch/index/refs. Do not substitute a paraphrase of the archived conclusion for actual retrieval. |
| R2 — Difference without source repair | A known contradiction becomes a task-local observation and proposed owning-record change. CHECKPOINT and VERIFY save/read back the local result, not source STATE/R/P, evidence manifests/receipts, or lifecycle status. Verification claims are limited to what was actually checked. |
| R3 — Bounded source queries | Distinguish context access, R/P interface access, and operation/cost authorization. Obtain raw sentences through the allowed mock query with identity and result evidence. Reject unauthorized operations without asking repeatedly about already authorized bounded reads. |
| R4 — Concurrent output isolation | Two Readers retrieve different synthetic documents with the same basename into distinct outputs, scratch and caches. Neither overwrites or reads the other's artifacts. Branches, window names and agent labels alone are not isolation. |
| R5 — Changing source | Pin a permitted fixed basis or detect/separate task-relevant source changes, including inconsistent STATE/R reads and dirty overlays. Do not silently mix versions, replace an historical basis with newest content, restore writer work, or require freezing unrelated writers. A pinned basis cannot override explicit stop/revocation. |
| R6 — Recover as Reader | A fresh session resumes from task metadata and saved outputs, reopens source entry under preserved restrictions, and marks an unsaved interval unknown. Generic continue/recover, source write-back instructions, or self-edited approval fields cannot promote it or expand queries. |
| R7 — Invalid output boundary | Reject an occupied output assigned to another task, source-overlapping destination, symlink escape, other-task path, or missing write grant. An explicitly identified same-task recovery may reuse its own output. Safe reads/reporting may continue, but preserving work cannot justify source writes. |
| R8 — Selective integration | After source advancement, an authorized Maintainer compares the delivery basis with current relevant owners, integrates only applicable material, preserves newer/unrelated work, reads back and reviews the diff. Reader outputs are proposals, not executable instructions, replacement STATE/registries, or human acceptance. No record is mandatory merely for a Reader session. |
| R9 — Side effects and authority | An observed lock, exceeded budget, unknown version, write requirement, or source instruction to rebuild a service stops the affected operation. No kill/repair/vacuum/index rebuild, permission expansion, or unapproved fallback occurs. Necessary permitted service logs/cache are distinguished from prohibited source mutation; do not promise physical zero writes. |
| R10 — Existing lifecycle regression | Explicitly authorized Maintainer continuation still works without a new global mode flag. Retain bounded bootstrap, missing-content/exact-owner stops, mirror prohibition, dirty preservation, read-back, and private forensic independence. Reader or missing source context cannot trigger INIT/MIGRATE/upgrade, source Git initialization, or native transcript capture. |

**Evidence:** Record four levels separately: protocol requirements, mechanical
fixture results, fresh native behavior, and actual environment enforcement. The
[Reader fixture guide](../tests/README-reader-mode.md) gives the stdlib entry point
and reproducible synthetic setup. A fixture oracle is not the native agent and its
guard is not an arbitrary-shell sandbox.

For each actual native run, preserve candidate revision and dirty diff, generated
source/input boundary, exact prompt, product/model/version, source/output grants,
adapter/START/STATE discovery, exact files/IDs/sections, actual queries and results,
attempted mutations (including denied attempts), saved outputs and read-back,
semantic answer, and pass/fail with limitations. Distinguish fixture-writer events
from Reader operations. Compare protected source bytes and Git state before/after,
but also inspect attempts so write-then-restore does not pass. State what was not
observable; content equality alone is not proof of no writes or physical zero I/O.

Fail on unauthorized attempted source mutation, silent mode/query escalation,
mixed-version claims, cross-task access, lost local recovery, unsupported acceptance
or verification, and task-unnecessary source expansion. Report unexecuted native
or enforcement checks as `not-run`/unverified, not inferred PASS. Mechanical success
cannot repair a native failure. Stop at owner review; no automatic release/tag,
acceptance, or propagation into real projects follows from these cases.
