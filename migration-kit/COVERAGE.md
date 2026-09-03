# Migration coverage — `<migration-id>`

This file is the sole inventory and denominator for migration coverage. Do not
replace it with a single percentage. Add one row per actual source, repository,
host, resource group, service, job group, or procedure surface; the starter rows are
scope prompts and MUST be expanded or given a justified `n/a` result.

## Result vocabulary

- **Track:** `operational` or `forensic`
- **Criticality:** `critical` or `supporting`
- **Access:** `accessible`, `inaccessible`, or `not-attempted`
- **Result:** `pass`, `partial`, `unknown`, or `n/a`
- **Disposition:** `pending`, `canonicalized`, `constrained`, `backlog`, `blocked`,
  or `not-applicable`

Access says whether inspection was possible; result says what the inspection covered;
disposition says what the migration did about the result. `inaccessible` includes a
source that was attempted but denied, deleted, or undiscoverable within the stated
scope. `not-attempted` means no inspection attempt and is never equivalent.

Valid combinations:

| Access | Allowed result | Rule |
| --- | --- | --- |
| `accessible` | `pass`, `partial`, `unknown`, `n/a` | Inspection ran; `unknown` still requires a blind spot. |
| `inaccessible` | `unknown` | An attempted but denied/deleted/undiscoverable surface cannot pass. |
| `not-attempted` | `unknown` | No attempt can establish pass, partial, or non-applicability. |

And for result/disposition:

| Result | Allowed disposition | Rule |
| --- | --- | --- |
| `pass` | `canonicalized`, `backlog` | Material findings are normalized, or a forensic result is intentionally retained. |
| `partial` | `pending`, `constrained`, `backlog`, `blocked` | State the inspected subset and residual gap; an operational residual needs a constraint or remains pending/blocked. |
| `unknown` | `pending`, `constrained`, `backlog`, `blocked` | Link a blind spot; never call it canonicalized. |
| `n/a` | `not-applicable` | State evidence that the domain truly has no project function. |

`constrained` requires a documented safe constraint and explicit human acceptance in
`CUTOVER.md`. It cannot make an unsafe condition safe by wording alone. `pending`
means no final treatment yet. `blocked` always blocks cutover; an unsafe unresolved
operational/critical row must use it. `backlog` is forensic-only: an operational row
must be canonicalized, constrained, pending, blocked, or explicitly reclassified to
forensic with rationale before it can enter backlog.

## Surface inventory

| ID | Domain/source | Locator or scope basis | Track | Criticality | Access | Result | Inspected by/at | Evidence/output refs | Gap/unknown | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CV-001 | conversations/threads | `<listing method and bounded set>` | operational | critical | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-002 | native instructions/memory | `<locations/scopes>` | operational | critical | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-003 | MCPs/tools/connectors | `<config and inventory scope>` | operational | supporting | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-004 | local repos/worktrees/Git | `<repo set>` | operational | critical | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-005 | remote hosts/topology | `<host/resource set>` | operational | critical | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-006 | assets/lineage | `<asset families>` | operational | critical | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-007 | services | `<service inventory source>` | operational | supporting | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-008 | jobs | `<scheduler/process/automation scope>` | operational | critical | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-009 | environment/build/deploy/reproduce/maintain | `<procedure set>` | operational | critical | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-010 | dependencies/secret refs | `<dependency/config scope>` | operational | critical | not-attempted | unknown | unknown | none | `<U ID>` | pending |
| CV-011 | historical/other unknowns | `<known blind-spot set>` | forensic | supporting | not-attempted | unknown | unknown | none | `<U ID>` | backlog |

Domain rows do not prove domain coverage if several material sources exist. Expand,
for example, accessible conversations into one row per thread or bounded thread set,
and remote infrastructure into rows with defensible scope.

## Defensible roll-up

- **Operational critical rows (total):** `<count and IDs>`
- **Unresolved operational critical rows:** `<count and IDs; must be zero for cutover>`
- **Operational supporting partial/unknown rows:** `<count and IDs>`
- **Forensic open rows:** `<count and IDs>`
- **Operational `not-attempted` rows:** `<count and IDs>`
- **Scope limitations:** `<plain-language denominator limits>`

## Coverage assertions

- [ ] Every required domain has at least one scope row or justified `n/a`.
- [ ] Every known operational source has its own row or belongs to a named bounded set.
- [ ] Every inaccessible/unknown result links a detailed blind spot in `AUDIT.md`.
- [ ] Every `partial` result states the inspected subset and residual gap.
- [ ] Every row uses a valid result/disposition combination.
- [ ] Every row uses a valid access/result combination; inaccessible/not-attempted
  never becomes `pass` or `n/a`.
- [ ] No operational row uses the forensic-only `backlog` disposition.
- [ ] Every `constrained` row has a safe constraint and human-acceptance row in `CUTOVER.md`.
- [ ] No bare completeness percentage appears in migration claims.
- [ ] Operational and forensic tracks are not conflated.
