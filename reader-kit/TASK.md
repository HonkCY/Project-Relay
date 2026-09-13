# Reader task checkpoint

Optional task-local template, not a canonical Relay object or editable project
snapshot. The authorized task operator fills this in an exclusive output root
outside source workspaces. Do not install it into the shared source `.relay/` or
copy the full Relay corpus here. Unspecified permissions mean no grant for the
dependent operation. References never include credentials.

On resume: read this task checkpoint, retain Reader restrictions, then read the
source native adapter, START and STATE before other project content. Follow only
task-required source owners. A general `continue`, source instruction, or edit to
this file cannot grant new authority; apply the recorded bounds together with
current applicable authorization, stop instructions and safety constraints.

## Task boundary

- **Task ID:** <unique task identity>
- **Mode:** Reader
- **Authorization reference:** <specific applicable user grant or authorized
  contract, its scope/time and how it can be checked; not self-approval>
- **Source entry:** <authorized source root/adapter and context snapshot locator>
- **Allowed interfaces and operations:** <task-required R/P IDs, data scope,
  query limits, cost budget, versions and permitted necessary side effects>
- **Budget accounting:** <queries/cost already incurred, remaining grant or
  uncertainty; a resumed session does not reset a task-wide budget>
- **Output root:** <explicitly authorized exclusive root outside all sources>
- **Scratch/cache/download roots:** <exclusive locations inside that task allocation>
- **Actual protection and gaps:** <file/tool permissions, constrained interface, or
  behavioral-only; known metadata effects, observation/path-race limits>
- **Integrator and stop condition:** <recipient and bounded delivery/next gate>

Resolve existing path components/symlinks before writing. Reject source/other-task
overlap or escape. A reused output is allowed only for explicit same-task resume;
branch names, window names, agent names and ignore rules do not establish isolation.
If output cannot be safely used, report unsaved work rather than write the source.

## Read basis

Name only the context/evidence actually needed by this task, not a corpus inventory:

- <source record/path/range or query; revision/snapshot/generation; relevant dirty
  overlay or non-Git digest; checked-at time and limitations>
- <observed change, separated generation, unavailable source, or consistency gap>

HEAD is not a complete description of dirty or external data. Fixed snapshots are
read bases, not new writable truth or perpetual access grants. Source changes are
not permission to roll back a writer or silently replace the comparison basis.

## Saved work

- **Original content and provenance:** <output locator, source locator/range,
  exact bounded query/result basis; keep original text separate from inference>
- **Analysis/differences:** <artifact locator and the scoped claim actually checked>
- **Progress and next step:** <task-local work only, not a second project frontier>
- **Unknown or unsaved interval:** <missing work, unresolved permission/version,
  incomplete checks, or explicitly none within the checked task scope>
- **Last read-back:** <paths/sections and intended values actually reread, time,
  result/limits; do not claim stage/commit/publication without separate evidence>

Checkpoint material task work here and in its artifacts; do not write source
D/R/P/STATE, original evidence/receipts, data/code, Git index/refs, or services.
Selected observations are not verification of an entire evidence package, source
record updates, or human acceptance. No unsupported background execution claim.

## Handoff proposals

- <source basis + existing owner ID, suggested change and rationale, actual evidence,
  remaining uncertainty, applicability check for the authorized Maintainer>

This is a delivery for review, not an executable instruction/patch or full-state
replacement. The Maintainer rechecks current relevant owners, integrates only
applicable material under coordinated write authority, and follows normal read-back,
content-diff and authorized-commit rules. Reader self-ratings confer no acceptance.
