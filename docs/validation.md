# v0.1 validation record

This record describes the repository-level checks performed for the
`v0.1-design` checkpoint. The outcome is **ready for human design review**, not a
claim that Project Relay is production-certified or that every acceptance scenario
has run against real external systems.

## Boundary and environment

- **Validation date:** 2026-09-03
- **Intended boundary:** annotated Git tag `v0.1-design`
- **Host tools:** Git 2.49.0, ripgrep 15.1.0, Ruby 2.6.10, Bash 3.2.57
- **Runtime dependencies:** none; validation used ordinary filesystem, Git, Ruby,
  ripgrep, and Bash checks

The pass table is valid only when `v0.1-design` resolves to the commit containing
this record and the checkout is clean. Before that tag exists, treat this file as an
in-progress release checklist rather than evidence of a completed checkpoint.

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
native or external-system execution. In particular, A/B compatibility must be
demonstrated in clean product sessions before any production-release claim.

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
