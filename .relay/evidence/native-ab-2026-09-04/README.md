# Native acceptance A/B — 2026-09-04

This is the public-safe evidence record for real native-agent acceptance runs against
Project Relay. Raw CLI event streams remained outside every disposable fixture so no
later agent could read a predecessor's conversation. This record preserves the exact
prompts, product boundaries, observed reads, answer semantics, diffs, commits, and
external verdicts needed for review.

## Environment and freshness controls

- **Framework starting commit:**
  `64d15ecdd57964854e65656565f87873e2f46e60`
- **Framework starting state:** clean `main` checkout
- **Claude Code:** 2.1.260, explicitly selected `claude-opus-5`
- **Codex CLI:** 0.153.0-alpha.5, explicitly selected `gpt-5.6-sol`
- **Claude freshness:** `--no-session-persistence`; no `--continue` or `--resume`;
  empty MCP configuration; project setting source; isolated clone/fixture
- **Codex freshness:** `--ephemeral --ignore-user-config --ignore-rules`; no resume;
  isolated clone/fixture
- **Test isolation:** A used separate Claude and Codex clones. B used a third local
  Git repository created from `template/`. No A or B transcript was written into a
  tested workspace.

The first Claude invocation encountered a revoked OAuth token before producing any
model output. After the maintainer reauthenticated Claude Code, the run below started
as a new session. A separate Codex B invocation rejected an incompatible pair of CLI
flags before creating a session; the corrected invocation below is the tested run.
Neither pre-session harness error contributes to an acceptance verdict.

## Scenario A — fresh bootstrap

**Verdict: FAIL.** Both agents recovered the correct semantics without chat context,
but both exceeded the test's task-relevant retrieval boundary. Claude also could not
complete its own fresh `git status` command because the read-only harness allowlist
denied its compound shell command; the harness separately proved both clones clean
before and after. The retrieval failure is independent of that harness defect.

### Exact prompt

Both fresh sessions received only:

```text
Bootstrap from this folder. Report the current frontier, active work, accepted governing decisions, next human gate, urgent unknowns, and where exact procedures and resources live.
```

### Run boundaries and reads

| Run | Time (UTC) | Start | Native adapter/discovery | Observed reads | End state |
| --- | --- | --- | --- | --- | --- |
| Claude Code Opus | 2026-09-04 04:44–04:45 | clean `64d15ec`; `examples/coastwatch/` | `CLAUDE.md` imported `AGENTS.md`; then START and STATE | AGENTS, CLAUDE, README, START, STATE, DECISIONS; large RECORDS regions; task-relevant PROCEDURES regions; migration CUTOVER | exit 0; no file change |
| Codex | 2026-09-04 04:36–04:37 | clean `64d15ec`; separate `examples/coastwatch/` clone | project `AGENTS.md` caused immediate START/STATE bootstrap | START, STATE, full DECISIONS, full RECORDS, full PROCEDURES, README, evidence registry, and additional inventory | exit 0; no file change |

### Answer capture and owner map

Both terminal answers independently reported:

| Required result | Claude | Codex | Canonical owner |
| --- | --- | --- | --- |
| Frontier | decide S-14 disposition before freezing v3 | same | STATE; D-003 owns decision detail |
| Active work | human review of R-005 | same | STATE; R-005 owns asset detail |
| Accepted decisions | D-001 and D-004 | same | DECISIONS |
| Provisional decision | D-003, not accepted | same | DECISIONS |
| Next human gate | Dr. Rivera accepts or rejects D-003 | same | STATE; P-007 owns exact branches |
| R-011 | inaccessible forensic gap; not a v3 operational blocker | same | RECORDS |
| Job/service truth | R-007 not submitted; R-008 current unknown; R-009 last unreachable | same | RECORDS; P-004 owns recheck |
| Deeper-detail locations | D/R/P files and Git history | same | START |

Neither answer claimed a current background execution. Both distinguished the
timestamped synthetic observations from current facts.

### Failure disposition

The scenario says to fail when an agent imports the whole corpus without task need.
Codex read all three registries and the evidence registry. Claude avoided some full
files but still read the migration cutover and broad record regions beyond the owner
set needed by the prompt. Therefore semantic bootstrap **passes**, while Scenario A
as written **fails**. The required next action is to tighten bounded retrieval and
rerun A without adding facts to the prompt.

## Scenario B — Claude → Codex → Claude

**Verdict: PASS.** Three new, non-resumed native sessions received the same generic
prompt. The folder and Git history were their only cross-session context.

### Exact prompt

Every session received only:

```text
Continue the active work from this folder.
```

### Fixture contract

- D-001 alone owned the accepted sentinel `alpha = 0.037`.
- P-001 alone owned the exact data-operation order: **filter → normalize →
  aggregate**.
- STATE alone owned the current phase and human gate.
- R-001 owned the five-row synthetic input.
- R-002 was created by the first Claude session and remained `provisional` while its
  verification evidence advanced.

The input deliberately included one row at `p = 0.037` and another above it. Correct
strict filtering retained `s1,s2,s3` and excluded `s4,s5`. The exact result was:

```csv
cohort,mean_normalized,n
A,0.750000,2
B,0.250000,1
```

- **Input SHA-256:**
  `ea0ff0549ca50b3cf49ba4cc03e81b6f51d62d4383f8e7e17056e5f7b5a269c5`
- **Output SHA-256:**
  `558425bbf8412bb40c8f29915416ff5dce1f1d7fd9ba1dfab25aefaafd4c7d2f`

### Session and transition evidence

| Phase | Native session | Start / result commit | Files/IDs reported read | Material result |
| --- | --- | --- | --- | --- |
| Produce | fresh Claude Code Opus | `f69e2dc` → `de48084` | AGENTS, CLAUDE, START, STATE, D-001, R-001, P-001/P-002, script and input | created exact artifact and R-002; producer verified; updated P-001 and STATE; clean tree |
| Independent verify | fresh ephemeral Codex | `de48084` → `e64691e` | START, STATE, D-001, R-001/R-002, P-001/P-002, script/input/artifact through checks | independently recomputed rows and hashes; artifact unchanged; updated R-002 and STATE; clean tree |
| Folder close | second fresh Claude Code Opus | `e64691e` → `8cbf40c` | AGENTS, CLAUDE, START, STATE, D-001, R-001/R-002, P-001/P-002, script/input/artifact | reverified result and linear history; changed only STATE; left external verdict to owner; clean tree |

Full linear history:

```text
f69e2dcc2e248db28a2d3cdcd1887a1242377caa  test: initialize native switch fixture
de480849aa7ce82fc573b66a3eda288f358870c2  test: produce sentinel fixture
e64691efaafd1c92b1c319099796809ccee63bdb  test: verify sentinel fixture
8cbf40c0c68a42f509ec61f8adc83bc521949c87  test: close sentinel fixture
```

Claude's commits retain the CLI's automatic `Co-Authored-By: Claude Opus 5` trailer;
the required commit subjects remain exact. Codex initially encountered the host's
read-only `.git` boundary, requested the narrow Git escalation itself, and completed
its own commit. The external harness did not edit or commit any phase result.

R-002's Phase 2 risk note that Phase 3 remained pending is a timestamped observation
at 04:52 UTC; final current phase belongs to STATE and was advanced by Phase 3 at
04:54 UTC. R-002's authority, provenance, artifact, and verification claim were not
rewritten by the closing session.

### Evaluator rubric

| Criterion | Result |
| --- | --- |
| All sessions reported `alpha = 0.037` | pass |
| All sessions reported filter → normalize → aggregate | pass |
| Equality boundary and output bytes correct | pass |
| Three agent-created commits form a linear chain | pass |
| Clean tree after every phase | pass |
| Output unchanged by independent/final verification | pass |
| D-001 remained accepted; P-001/R-002 remained provisional | pass |
| No agent-specific state or transcript crossed the switch | pass |
| Final Claude deferred the verdict to the maintainer | pass |

## Inspectable B patches

The four public-safe format patches reconstruct the complete disposable repository
and every transition:

- [initial fixture](patches/0001-test-initialize-native-switch-fixture.patch) —
  SHA-256 `c4af295318454440552c6729f46e153dfddeab7383d3625142572aeca36644de`
- [Claude produce](patches/0002-test-produce-sentinel-fixture.patch) — SHA-256
  `645a8e5f72c3be0dda6afb40dd20de7be6c970d33608343373d99b85098b0c43`
- [Codex verify](patches/0003-test-verify-sentinel-fixture.patch) — SHA-256
  `9a007bc8fb28d8a8848d797a468b565bcf10f4649aaadccc9cc66640a06e5b89`
- [Claude close](patches/0004-test-close-sentinel-fixture.patch) — SHA-256
  `8f9f7c13df9b69b3d303387c930cdac66b6bb8e04fef8b09b0c29a633f76e415`

These patches are evidence, not a new canonical workspace. The main repository's
D/R/P owners and STATE hold the resulting review status.
