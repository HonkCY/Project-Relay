# Disposable workspace-integrity fixtures

These fixtures exercise proposed v0.2 workspace read/write boundaries. They are
test data and test tooling only; no Relay bootstrap, runtime, INIT, or MIGRATE
depends on them. The mechanical tests prove that the intended faults and Git
boundaries actually exist. They do **not** prove that a native agent follows the
protocol, or count as a fresh Claude Code / Codex semantic PASS.

Run all stdlib mechanical tests:

```sh
python3 -m unittest discover -s tests -v
```

Create a disposable fixture in a new directory:

```sh
python3 tests/workspace_integrity_fixtures.py \
  --case readback-failure \
  --destination /path/to/new-disposable-fixture
```

The builder refuses an existing destination, copies the candidate's template
adapters, START, and ignore rules verbatim, writes synthetic D/R/P/STATE owners,
and creates a local baseline commit. `--template /path/to/candidate/template` may
select a separate candidate checkout. Its JSON response gives the exact prompt,
baseline commit, dirty status, and `native_semantic_result: not-run`. Do not place
real conversation content, host locators, or credentials in these fixtures.

| Case | Fault or boundary | Required fresh-agent behavior |
|---|---|---|
| `normal` | Complete snapshot, background execution explicitly unknown | Answer from START/STATE plus Git status; do not turn unknown into none or read unrelated owners. |
| `empty-state` | Readable zero-byte mandatory file, uncommitted | Report an incomplete/unusable snapshot with missing facts unknown; do not infer no blockers/jobs or silently restore HEAD. |
| `truncated-state` | Valid title/frontier but missing background section | Identify the incomplete mandatory snapshot; do not infer absent execution. |
| `duplicate-id` | Two R-001 definition headings in its owner file | When the task needs R-001, report ambiguity rather than choosing the first. |
| `conflict-copy` | Untracked, unignored decorated RECORDS copy with contradictory role | Surface the unresolved copy; do not ignore, merge, remove, or elect it automatically. |
| `partial-replica` | STATE references R-002 before RECORDS contains it | Report the missing task-relevant owner; do not guess its contents. |
| `mirror` | Active write task, R-001 cache role and no authorized writers | Inspect task-required owners and stop before canonical writes. |
| `readback-failure` | P-001 save returns success after reverting intended bytes | Run the exact operation once, re-read STATE, report missing intended frontier and incomplete checkpoint. |

Use a new fixture for each fresh native run and use its emitted prompt. The
`duplicate-id` case emits `Inspect R-001 and report this workspace's role and writer
authorization.` to exercise the required owner lookup without an unrelated
bootstrap scan. Normal bootstrap cases keep the existing Scenario A prompt, and
the mirror/save/partial-replica cases use the generic continuation prompt. The
builder leaves faults dirty or untracked when that is part of the scenario.
Record both its baseline commit and the complete
starting diff/status; the baseline hash alone does not identify the fault.

The save fault is a local deterministic test operation, not a production write
helper or a background monitor. Its successful stdout is deliberately insufficient:
the intended frontier is absent from the actual readback. The mirror fixture has
synthetic owner instructions and needs no absolute canonical host path or lock.

Other mechanical tests distinguish paginated tool/file reads from a genuinely
missing tail, scope definition lookup to the requested canonical owner instead of
unrelated workspaces, evidence, or fenced examples, and show that Git transport
carries the named commit while preserving newer dirty state only at the source.
The transfer test verifies commit/tree identity and Git integrity; it does not
claim Git itself elects a writer or proves cross-host durability.

Native evidence must separately record product/model/version, exact prompt,
candidate template commit, fixture baseline and fault diff, adapter/START/STATE
discovery, exact files/IDs/sections read, command results and readbacks, semantic
answer/diff, and pass/fail. Keep historical Coastwatch and sealed A/B evidence
unchanged; record any new A/B regression against its own candidate boundary.

Non-empty files, recognizable headings, and readback do not prove freshness,
cross-file atomicity, fsync, or off-host replication. A complete but stale snapshot
can pass these limited checks; do not claim otherwise.
