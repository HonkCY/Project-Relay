# Native A remediation and final A/B regression — 2026-09-04

This is the public-safe evidence record for the bounded-retrieval remediation that
followed [R-002](../native-ab-2026-09-04/README.md). R-002's original Scenario A
failure remains an immutable observation. This record does not weaken that prompt or
its semantic/retrieval rubric; it records two failed remediation candidates, the
passing candidate, and the required Scenario B rerun at the same semantic boundary.

Raw CLI event streams remained outside the tested clones and fixture. This record
preserves the exact prompts, product boundaries, observed reads, semantic results,
transition commits, hashes, and external verdicts needed for review.

## Candidate and unchanged acceptance boundary

- **Final remediation candidate:**
  `b7097c4741f5f9084f053d7a096415048f51f29c`
- **Candidate state:** detached clean checkouts for A; a fresh disposable repository
  initialized from the candidate's `template/` tree for B
- **Acceptance specification:** `docs/acceptance-tests.md` was not edited by any
  remediation commit. Its SHA-256 before and after remediation is
  `1a7087456183ca60eee44ff9a935d9359d80cf4d1f35557019b718ccd19a0cc2`.
- **Candidate tree anchors:** `template/` tree
  `aa41eda7cf3990414f4edbcfc44616a660417786`; `docs/protocol.md` blob
  `a32f3cd7aaecb59ea0f17bef8defc2e396a1e849`; template START blob
  `a2830b6f56c63f1cc655c0faf3a4e5efbc50391d`; Coastwatch START blob
  `a4a6b914adeb98aa02cfd0d755376a81d932eac4`; template adapter blob
  `bcf86753409db66a61fbf9fb3eda8fa87ac87735`; Coastwatch adapter blob
  `6fc502f066011d2ecae41fcac04ecffacb0da3c4`; template CLAUDE blob
  `ce60f10b9b1a4edda8e3b1ad9a2134857a27a738`; template ignore-file blob
  `602b8bb42ade15a4e244eed6cfde562aa2a14920`.
- **Historical tag:** `v0.1-design` still resolves to
  `18c6c216b8f574e5c436968e4e5032797983dee0`; it was neither moved nor recreated.

The bounded-retrieval change is deliberately limited to the normative protocol,
template START, Coastwatch START, and the two project adapters needed to make the
native bootstrap order effective. It does not change the D/R/P object model and does
not shard a registry.

## Products and freshness controls

- **Claude Code:** 2.1.260, explicitly selected `claude-opus-5`, high effort,
  `--no-session-persistence`, project settings only, empty strict MCP configuration,
  Chrome and slash commands disabled, and no resume/continue
- **Codex CLI:** 0.153.0-alpha.5, explicitly selected `gpt-5.6-sol`,
  `--ephemeral --ignore-user-config --ignore-rules`, and no resume
- **Isolation:** every final A product used its own fresh clone at the exact candidate
  commit. B used another fresh disposable Git repository. No transcript or native
  session state was placed in a tested workspace.
- **Claude B clock boundary:** `TZ=UTC` and
  `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` were set for both Claude B phases.

Scenario A's final Claude command intentionally omitted `--restricted`: that mode
suppressed the native project adapter and therefore did not test folder bootstrap.
The passing run instead exposed only read-only tools and used `dontAsk` permissions.
The final Codex A run used its read-only sandbox. Scenario B enabled the file-edit
tools required by the scenario.

Immediately before the final B chain, one Claude command returned “not logged in”
before any model output or file access. The host OAuth login was refreshed and the
final Phase 1 then began as a new session from the unchanged clean initialization
commit. The pre-session authentication failure is not a test result.

## Scenario A — fresh bootstrap

**Final verdict: PASS.** Both final sessions recovered the required semantics from
START and STATE and stopped. Neither followed a deeper D/R/P ID, inventoried a
registry, opened migration/provenance material, or read unrelated project content.

### Exact prompt

Both fresh sessions received only:

```text
Bootstrap from this folder. Report the current frontier, active work, accepted governing decisions, next human gate, urgent unknowns, and where exact procedures and resources live.
```

The prompt and semantic expectations are identical to R-002.

### Remediation iterations

| Candidate | Claude result | Codex result | Disposition |
| --- | --- | --- | --- |
| `d892066` | fail: semantic answer correct, but README and broad directory content were inventoried | fail: semantic answer correct, but every heading in the monolithic D/R/P registries was enumerated | Tighten lookup scope; keep rubric unchanged. |
| `f524e8b` | fail: README, directory inventory, and Git history preceded START because the harness suppressed native adapter loading | pass | Correct the harness/adapter bootstrap boundary; do not accept a partial product result. |
| `b7097c4` | pass | pass | Final A candidate; no registry sharding required. |

The first two rows are retained as failed observations. They are not counted as final
acceptance evidence.

### Final START/STATE discovery and exact reads

| Product/model | Native discovery | Exact project reads in order | Unrelated reads |
| --- | --- | --- | --- |
| Claude Code 2.1.260 / `claude-opus-5` | Native `CLAUDE.md` import supplied the applicable `AGENTS.md`; the adapter directed immediate START/STATE bootstrap | complete `examples/coastwatch/.relay/START.md` lines 1–60; complete `.relay/STATE.md` lines 1–35; `git rev-parse --abbrev-ref HEAD` and `git status --short --branch` | D/R/P registries: none; README: none; migration: none; evidence/provenance archive: none; other files: none |
| Codex CLI 0.153.0-alpha.5 / `gpt-5.6-sol` | Native applicable `AGENTS.md` context directed immediate START/STATE bootstrap | one read of complete `.relay/START.md` and `.relay/STATE.md`; `git branch --show-current` and `git status --short --branch` | D/R/P registries: none; README: none; migration: none; evidence/provenance archive: none; other files: none |

Both clones were clean before and after the run. The stable-ID links visible in START
and STATE were treated as pointers, not default read obligations.

### Semantic answer and authoritative owners

Both final answers independently reported the same task-relevant state:

| Requested result | Reported semantic answer | Authoritative owner available at stop |
| --- | --- | --- |
| Frontier | decide the S-14 disposition before freezing v3 | STATE; D-003 is the linked decision-detail owner |
| Active work | human review of R-005 | STATE; R-005 is the linked asset-detail owner |
| Accepted decisions | D-001 and D-004 | STATE links the decision owners |
| Provisional decision | D-003 remains provisional, not accepted | STATE links D-003 |
| Next human gate | Dr. Rivera accepts or rejects D-003 | STATE; P-007 owns exact branches if later required |
| Urgent unknowns | R-011 is an inaccessible forensic gap, not a v3 operational blocker; R-008/R-012 are not usable proof of current execution | STATE links the record owners |
| Exact-detail locations | decisions in DECISIONS, resources in RECORDS, procedures in PROCEDURES, historical transitions in Git | START index |

Neither answer claimed a current background execution. All prompt items had an
authoritative owner and a sufficient current coordination answer in START/STATE;
there was no freshness conflict, execution request, audit request, or provenance
reconstruction requirement. Stopping at that point therefore satisfied both the
semantic and bounded-retrieval criteria.

Because both native agents passed without opening a monolithic registry, the A
failure was not a systematic registry-structure constraint. Stable-ID sharding is
not proposed or implemented in this candidate.

## Scenario B — final Claude → Codex → Claude regression

**Verdict: PASS.** After A passed, three new non-resumed native sessions ran B from a
fresh template-derived repository at the same final remediation boundary. The folder
and Git history were the only cross-session context.

The fixture's START, AGENTS, CLAUDE, and ignore-file blobs exactly match the final
candidate template blobs named above. The sentinel D/R/P records and strengthened
Phase 2/3 consistency wording are fixture-only test inputs, not a protocol/object-model
change.

### Exact prompt

Every phase received only:

```text
Continue the active work from this folder.
```

### Fixture contract

- D-001 alone owned the accepted sentinel `alpha = 0.037`.
- P-001 alone owned the exact operation order: **filter → normalize → aggregate**.
- STATE alone owned the current phase and human gate.
- R-001 owned the five-row synthetic input.
- The producing session created R-002; it remained `provisional` while its
  verification evidence advanced.

Strict filtering retained `s1,s2,s3` and excluded the equality-boundary row `s4`
and above-threshold row `s5`. The exact output remained:

```csv
cohort,mean_normalized,n
A,0.750000,2
B,0.250000,1
```

- **Input SHA-256:**
  `ea0ff0549ca50b3cf49ba4cc03e81b6f51d62d4383f8e7e17056e5f7b5a269c5`
- **Output SHA-256:**
  `558425bbf8412bb40c8f29915416ff5dce1f1d7fd9ba1dfab25aefaafd4c7d2f`

### Exact phase reads and transitions

| Phase | Fresh native session | Exact files/IDs/sections read | Result commit and material result |
| --- | --- | --- | --- |
| Produce | Claude Code 2.1.260 / `claude-opus-5` | native CLAUDE/AGENTS context; complete START and STATE; D/R/P heading search; P-002 lines 72–141; P-001 lines 1–71; R-001 lines 1–32; complete one-record DECISIONS file containing D-001; R-001/R-002 boundary lines 26–50; input, transform verification branch, artifact, ignore file, and Git preconditions | `a9ecf1e` → `4108b17`; observed sentinel/order, created exact artifact and R-002, updated P-001/STATE, committed `test: produce sentinel fixture`; clean tree |
| Independent verify | Codex CLI 0.153.0-alpha.5 / `gpt-5.6-sol` | complete START and STATE; Git status; exact heading searches for P-002/R-002 then P-001/D-001/R-001; R-002 lines 28–90; P-002 lines 76–150; D-001 section lines 3–75; R-001 lines 3–27; P-001 lines 3–75; complete transform script, input/artifact through checks, and the required Git history/diff | `4108b17` → `a16dbe4`; independently recomputed rows/hashes, left artifact unchanged, updated P-001/R-002/STATE so no current field still said independent verification was pending, committed `test: verify sentinel fixture`; clean tree |
| Folder close | Claude Code 2.1.260 / `claude-opus-5` | native CLAUDE/AGENTS context; complete START and STATE; exact heading searches for P-002, P-001, R-002, D-001; P-002 from line 77 with a 70-line bound; P-001 lines 3–76; R-002 lines 28–67; D-001 lines 3–32; script/input/artifact and required Git transition history | `a16dbe4` → `b02bcbe`; reverified exact result/history and canonical verification consistency, changed only STATE, preserved artifact and authorities, committed `test: close sentinel fixture`; clean tree |

Full linear history:

```text
a9ecf1e065893e9ba7fa8a61641f40edc74b4033  test: initialize native switch fixture
4108b1715d5b4360693ae96dd180962c6fc77ab3  test: produce sentinel fixture
a16dbe4b630d51ddd04617b92fc91682c329753d  test: verify sentinel fixture
b02bcbe55c64a1125f3b5e0d3845f029b4a0d59b  test: close sentinel fixture
```

The B repository's START/adapters and immutable input, script, and D-001 were
unchanged across the three agent transitions. D-001 remained accepted; P-001 and
R-002 remained provisional. Phase 2 recorded independent verification in both P-001
and R-002 and reconciled STATE; Phase 3 confirmed that no current canonical field
still claimed independent verification was pending. The final STATE reported no
active execution and left the evidence verdict to the maintainer.

Two earlier post-remediation B attempts were discarded before acceptance. In the
first, Claude labeled a Taipei local clock value with `Z`. In the second, R-002 was
independently verified but P-001 and STATE retained stale “independent verification
pending” language. The harness detected both provenance/consistency defects, counted
neither chain, clarified the disposable fixture's existing Phase 2/3 consistency
contract without weakening the external Scenario B rubric, and reran all three phases
in a new repository with a UTC clock boundary. Only the chain above is final
candidate evidence; no agent output was manually repaired.

### Final evaluator rubric

| Criterion | Result |
| --- | --- |
| All sessions recovered `alpha = 0.037` | pass |
| All sessions recovered filter → normalize → aggregate | pass |
| Equality boundary and output bytes correct | pass |
| Three agent-created commits form a linear chain | pass |
| Clean tree after every phase | pass |
| Output unchanged by independent/final verification | pass |
| D-001 stayed accepted; P-001/R-002 stayed provisional | pass |
| P-001, R-002, and STATE agree on independent-verification state | pass |
| No transcript or native session state crossed the switch | pass |
| Final Claude stopped at the maintainer evidence gate | pass |

## Inspectable final B patches

The four public-safe format patches reconstruct the complete accepted disposable
repository and every transition. Patch author email fields use reserved `.invalid`
addresses; they are evidence, not canonical workspace objects. Replaying them
reconstructs each original tree and the linear content transitions; the anonymized
author metadata intentionally produces different replayed commit object IDs.

- [initial fixture](patches/0001-test-initialize-native-switch-fixture.patch) —
  SHA-256 `928d6061334ee022cdaa03308b4739aa4fba279871ff0ab64a4ed0714647310f`
- [Claude produce](patches/0002-test-produce-sentinel-fixture.patch) — SHA-256
  `0c383d7fbb129791b37e583285f54dab0fb1865993bac76fdc9b1010c2f52dfd`
- [Codex verify](patches/0003-test-verify-sentinel-fixture.patch) — SHA-256
  `e843f9b79ca1b367fe4fd073dccb6b8bca52c5f08dddd949bf53f18fc6b9cf70`
- [Claude close](patches/0004-test-close-sentinel-fixture.patch) — SHA-256
  `791da8e9cf6f3c92161be2cf9e4c4ef351ef9bec5acfbe78b4e0778f929834f4`

These patches preserve content transitions; raw native event streams remain outside
the fixture. The main repository's D/R/P owners and STATE own the review status.

## Gate disposition

Scenario A and the post-remediation Scenario B regression both pass at the same
final candidate boundary. This advances the repository only to human review. It does
not accept D-002–D-004, does not create a final v0.1 release tag, and does not move
the historical `v0.1-design` tag.
