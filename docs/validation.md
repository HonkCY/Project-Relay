# v0.1 validation record

This record describes the repository-level checks performed for the immutable
`v0.1-design` checkpoint and, in separately labeled addenda, later native A/B
evidence and the final v0.1 seal. Project Relay v0.1 is accepted and sealed; this is
not a claim that it is production-certified or that every acceptance scenario has
run against real external systems.

## Boundary and environment

- **Validation date:** 2026-09-03
- **Intended boundary:** annotated Git tag `v0.1-design`
- **Host tools:** Git 2.49.0, ripgrep 15.1.0, Ruby 2.6.10, Bash 3.2.57
- **Runtime dependencies:** none; validation used ordinary filesystem, Git, Ruby,
  ripgrep, and Bash checks

The repository-check pass table below applies only to the tree at `v0.1-design`.
Inspect that immutable version with `git show v0.1-design:docs/validation.md`; later
main-branch addenda do not retroactively change the tag or its 37-file count.

## Repository checks

| Check | Result | Evidence and scope |
| --- | --- | --- |
| Markdown links and anchors | pass | Every local link in 37 Markdown files resolves to an existing file and heading. |
| Stable IDs and schemas | pass | Fixture IDs are unique and linked; all D/R/P entries contain their common evidence envelope and kind-specific required fields. |
| Migration coverage model | pass | Coastwatch has 13 coverage rows, 8 operational-critical rows, zero unresolved operational-critical rows, and no operational backlog disposition; every row obeys both state matrices. |
| Shell examples | pass | All 12 fenced `sh`/`bash` blocks parse with Bash 3.2 `bash -n`; commands remain synthetic where marked. |
| Template smoke test | pass | A temporary template copy initializes under Git, exposes both adapters, discovers hidden `.relay` files, and ignores `.relay/private/`. |
| Nested private-path defense | pass | Root ignore rules protect `.relay/private/` at the root and in nested fixture/workspace paths. |
| Public-content scan | pass | Tracked content and reachable history contain no private-key header, bearer token, secret assignment, motivating-project locator, local user path, or non-reserved example domain. |
| Git integrity | pass | The checkpoint has a clean worktree, an annotated tag, and passes `git diff --check` and `git fsck --full`. |
| Independent adversarial reading | pass | Separate clean-reader, migration, and whole-repository reviews found no unresolved internal design defect after corrections. |

The checks above validate this repository's internal structure and stated boundary.
The Coastwatch evidence is deliberately inspectable fiction; it proves that the
schema can represent the scenario, not that any `.example` host or service exists.

## Acceptance-scenario status

| Scenario | v0.1 evidence status |
| --- | --- |
| A — fresh bootstrap | Structural clean-context reader check passed on Coastwatch. Real clean native Codex and Claude Code runs remain pending. |
| B — Claude → Codex → Claude | Pending: requires three real native sessions in a disposable template instance. |
| C — compaction/session loss | Ownership, dirty-tree, and RECOVER semantics passed adversarial inspection; a native forced-compaction run remains pending. |
| D — latent conversation migration | Candidate, coverage, human-risk, and promotion paths passed fixture/schema inspection; no provider conversation was migrated. |
| E — remote operational state | Multi-terabyte data, host topology, lineage, service, job, and secret-reference records passed fixture inspection; no external host was contacted. |
| F — false incumbent memory | Coastwatch MC-001/MC-006/CF-001 preserves and rejects stale v2 recall while canonicalizing verified v3 evidence. |
| G — inaccessible source | Coverage matrices preserve inaccessible evidence as unknown and distinguish constrained operational risk from forensic backlog. |
| H — background-job truth | R-007 remains planned, R-008 remains currently unknown, and queue absence is never treated as success. |
| I — public safety | Repository and reachable-history scans passed at the tagged boundary. |

Scenarios are independent. “Fixture/schema inspection” is not reported as a real
native or external-system execution. At the tagged boundary, A/B compatibility still
required clean product sessions before any production-release claim.

## Post-tag native A/B addendum — 2026-09-04

Real, clean-session native runs were completed after `v0.1-design`. The full
public-safe record is
[R-002 native A/B evidence](../.relay/evidence/native-ab-2026-09-04/README.md).
This addendum does not rewrite the tagged status table above.

| Scenario | Post-tag result | Disposition |
| --- | --- | --- |
| A — fresh bootstrap | **fail** | Claude Code Opus and Codex both recovered the correct frontier, decisions, gate, owners, and unknowns, but both exceeded the explicit task-relevant retrieval boundary. Tighten bounded retrieval and rerun A without enriching the prompt. |
| B — Claude → Codex → Claude | **pass** | Three fresh native sessions preserved `alpha = 0.037`, filter → normalize → aggregate, epistemic fields, exact output, and a clean linear three-commit transition using the same generic prompt. |

Because A and B are independent, B's pass does not offset A's failure. The current
frontier and human gate are owned by [canonical STATE](../.relay/STATE.md).

## Post-tag bounded-retrieval remediation addendum — 2026-09-04

The original A failure above remains unchanged. At the tested remediation candidate,
the smallest bounded-retrieval correction was applied without changing the Scenario
A prompt or substantive pass/fail criteria, the D/R/P object model, or registry
structure. The final public-safe run record is
[R-003 bounded-retrieval remediation evidence](../.relay/evidence/native-ab-remediation-2026-09-04/README.md).

| Scenario | Final candidate result | Disposition |
| --- | --- | --- |
| A — fresh bootstrap | **pass** | Fresh Claude Code Opus and Codex sessions recovered every required semantic result from their native adapter plus START/STATE, then stopped without opening a D/R/P registry, README, migration material, or evidence archive. |
| B — Claude → Codex → Claude | **pass** | After A passed, three new native sessions reran the sentinel transition from the final candidate's template boundary and preserved `alpha = 0.037`, filter → normalize → aggregate, exact bytes, epistemic authority, and a clean linear transition. |

Both results apply to remediation candidate `b7097c4`; the evidence record identifies
the exact tree/blob boundary and reconstructable B commits. The passing A result shows
that the monolithic registry structure is not a systematic over-read constraint for
this prompt, so no stable-ID sharding was implemented.

This addendum advances the candidate to human review only. D-002–D-004 remain
provisional, and `v0.1-design` remains the unchanged historical design checkpoint.

## Final v0.1 seal — 2026-09-04

The project owner accepted the final Scenario A pass, the final post-remediation
Scenario B regression pass, and D-002–D-004. Before sealing, Scenario A prose was
clarified to treat linked stable IDs as authoritative on-demand pointers and to
follow only task-required owners. The exact prompt, semantic expectations,
substantive bounded-retrieval failure condition, and recorded R-002/R-003 runs did
not change. No native A/B rerun was required for this wording-only reconciliation.

Final deterministic checks cover Markdown links and anchors, stable-ID/schema
structure, migration matrices, shell examples, template bootstrap and ignore rules,
public-content safety, Git diff integrity, and `git fsck --full`. All passed at the
final seal boundary. The annotated `v0.1` tag identifies that boundary;
`v0.1-design` remains the immutable historical checkpoint at
`18c6c216b8f574e5c436968e4e5032797983dee0`.

## Reproduction notes

The validation used read-only checks equivalent to:

```text
git diff --check
git fsck --full
git status --short --branch
git check-ignore -v examples/coastwatch/.relay/private/probe
rg --hidden --glob '!.git/**' '<pattern>' .
bash -n <each extracted sh/bash fence>
```

The temporary template smoke-test directory was outside the repository and is not
part of the checkpoint. Reviewers should execute the complete Given/When/Then
procedures in [acceptance tests](acceptance-tests.md), recording product versions,
exact prompts, source boundary, and outputs.
