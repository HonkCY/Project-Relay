# Reader candidate — synthetic native observations, 2026-09-13

**Review candidate; native conformance FAIL.** Correct comparisons and unchanged
source bytes do not offset retrieval, read-back or recovery failures. This record
does not modify the old A/B evidence or accept v0.2/the forensic enhancement.

## Candidate and setup

- Parent revision: `03078f93f852556aa1d03fb50db2b8caa66fdf0e`; Reader changes were
  uncommitted during these runs. The containing candidate commit records the final
  implementation and this evidence, not a claimed prior release pass.
- Tested `template/.relay/START.md` Git blob:
  `3a53b3bc701af0fc0dbf3432e420a160228c3678`; SHA-256:
  `3c257d8f7d2ad3b05dfeb3f2fd7abb2eaa8dc90de35fbe82872637b8a8579cc3`.
  This exact template is unchanged between all runs and the recorded candidate.
- Unchanged template adapter blobs: AGENTS
  `bcf86753409db66a61fbf9fb3eda8fa87ac87735`, CLAUDE
  `ce60f10b9b1a4edda8e3b1ad9a2134857a27a738`.
- Only the [generated fixture builder](../../../tests/reader_mode_fixtures.py)
  supplied project data. Archive alpha is `0.050`; raw alpha is `0.037`; both windows
  are 12 samples; only the raw document includes the amber-exclusion rationale.
  R-002/R-003/P-002 specify the archive, mock interface and bounded original quotes.
- Each start uses a separate source Git baseline and mock. Native cwd is the
  explicitly allocated output, whose empty Git root was created by the harness;
  the short prompt points to the source folder. The agent receives no expected
  answer. This tests an external-output launch, not every native cwd/startup mode.
- Initial fixtures nested beneath this protocol repo exposed ancestor discovery
  in Claude. Those observations remain failures with that setup limitation. A
  second cohort uses newly generated temporary fixtures outside the repo; the
  template/rubric is not relaxed and no previous answer is supplied.
- Handoff uses another fresh process, no native resume/session ID and no old chat.
  It reads the second cohort's saved TASK/output. Since the comparison was already
  complete, this is a recovery-entry smoke test, not the full R6 unfinished-work or
  forced-compaction scenario.

## Prompts and operation evidence

[runs.json](runs.json) records all six processes: versions/model evidence, source
commits, template identity, timestamps, prompt hashes, path-normalized exact prompt
wording, observed tool operations, saved artifacts and protected-byte comparisons.
`$CASE` denotes that run's generated fixture root and `$REPO` this generic protocol
repo; substitutions affect locators, not instruction wording. Exact delivered
strings and full raw outputs remain in the local ignored
`.relay/private/reader-native-2026-09-13/` observation files. They are audit-only,
not portable dependencies. Native process success is not a conformance verdict.

Start wording, with only generated paths parameterized:

```text
Use Reader mode to bootstrap from $CASE/source. Compare the specified archive with
authorized raw source quotes. All artifacts, TASK.md, scratch and cache belong only
in the newly allocated exclusive task output $CASE/outputs/reader-a (its empty Git
root was created by the synthetic harness). Do not modify any source. Deliver and stop.
```

Fresh handoff wording:

```text
Resume the Reader task from $CASE/outputs/reader-a/TASK.md. Preserve its read/write
and query limits, reopen the source entry, and report saved results and any
unfinished or unknown interval. Do not modify any source or repeat completed
queries. Stop after handoff.
```

The JSON prompt fields preserve the actual single-line wording. The blocks above
are wrapped for display, not extra prompting or retrospective answer coaching.

## Verdicts

| Run | Result | Decisive observations |
| --- | --- | --- |
| Claude nested start | FAIL / setup contamination retained | Reads ancestor protocol context, inventories the fixture and source history before completing source entry; whole-file hash/count exceeds authorized raw surface; TASK content is not read back despite a persistence claim. |
| Codex nested start | FAIL | Inventories source files before completing START/STATE. Useful quotes, local outputs and source preservation do not satisfy the bounded-entry criterion. |
| Claude external start | FAIL | Inventories fixture/sibling mock metadata before entry completion and reads source ignore rules early. Whole-file hash/count reads beyond raw lines 1–3; TASK is checked by line count, not content. Saved observations lack an actual timestamp. |
| Codex external start | FAIL | Broad file inventory, then whole DECISIONS/RECORDS/PROCEDURES in the same read batch as entry, including unrelated R-001/P-001/D-001 detail. Whole-file raw hash also exceeds the requested surface. |
| Claude external handoff | FAIL (smoke only) | Retains Reader and saved results, but reopens only source STATE, omits native adapter/START and repeats fixture inventory. No new raw queries or writes observed. |
| Codex external handoff | FAIL (smoke only) | Reads TASK and the saved comparison, but never reopens source adapter/START/STATE despite the explicit request. No new raw queries or writes observed. |

All four starts return the correct alpha disagreement, matching window and raw-only
rationale, with outputs confined to the allocated task area in the observed tool
trace. No attempted source mutation was observed; all six before/after source/mock
regular-file maps match, including source Git index, refs and objects. The output
Git roots were harness setup, not source initialization by a Reader.

Do not repeat the models' stronger claims. A whole-file hash does read file bytes
outside the quoted range even if those sentences never enter model context; a line
count is not checkpoint content read-back. Query-cost accounting in Claude's saved
report is inconsistent with its operations, so no exact remaining allowance is
certified. Accepted **interface authority** on R-003 also does not make every raw
observation an accepted decision or automatically more reliable fact.

## Enforcement, remaining checks and review gate

Claude Code reports `2.1.260`, with `opus` resolving to `claude-opus-5`. It uses
`dontAsk`, project settings, no session persistence, and an empty strict MCP config.
Codex CLI is `0.154.0-alpha.6.2`, requesting `gpt-5.6-sol`, with ephemeral execution,
user config/rules ignored and `workspace-write` rooted at task output. The trace's
model-identification limits are preserved in the manifest.

These are observed behaviors, **not verified OS source-write confinement**. Claude
has general tool capability; Codex's default temporary writable roots may include
the external generated sources. No unrestricted Codex mode or permission-bypass
switch is used. We did not probe real workspaces or attempt destructive denial tests.
Tool traces and final hashes do not observe every transient/native-internal write,
filesystem metadata effect or path race.

The separate stdlib suite passes 41 tests (28 unchanged plus 13 Reader tests).
Native R4/R5/R7/R8/R9, full unfinished-work R6, a source-cwd launch matrix, and the
unchanged final A/B/C release regression are not run here. No hard-enforcement or
real-system PASS is claimed. These failures identify the next bounded work:
reliable entry discovery, exact-surface evidence hashing, actual checkpoint
read-back, and task-to-source recovery entry. Do not solve them by weakening the
rubric, adding a canonical session registry, or deploying into real projects.

Stop for owner review. No acceptance, push, release tag or historical-evidence edit.
