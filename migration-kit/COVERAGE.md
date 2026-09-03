# Migration coverage — `<migration-id>`

This file is the sole inventory and denominator for migration coverage. Do not
replace it with a single percentage. Add one row per actual source, repository,
host, resource group, service, job group, or procedure surface; the starter rows are
scope prompts and MUST be expanded or given a justified `n/a` disposition.

## Result vocabulary

- **Track:** `operational` or `forensic`
- **Criticality:** `blocker` or `supporting`
- **Access:** `accessible`, `inaccessible`, or `not-attempted`
- **Result:** `pass`, `partial`, `unknown`, or `n/a`
- **Disposition:** `canonicalized`, `backlog`, `risk-accepted`, or `blocked`

`risk-accepted` requires an authorized human and cannot make unsafe continuation
safe by itself. `not-attempted` is never the same as `inaccessible`.

## Surface inventory

| ID | Domain/source | Locator or scope basis | Track | Criticality | Access | Result | Inspected at | Evidence/output refs | Gap/unknown | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CV-001 | conversations/threads | `<listing method and bounded set>` | operational | blocker | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-002 | native instructions/memory | `<locations/scopes>` | operational | blocker | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-003 | MCPs/tools/connectors | `<config and inventory scope>` | operational | supporting | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-004 | local repos/worktrees/Git | `<repo set>` | operational | blocker | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-005 | remote hosts/topology | `<host/resource set>` | operational | blocker | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-006 | assets/lineage | `<asset families>` | operational | blocker | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-007 | services | `<service inventory source>` | operational | supporting | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-008 | jobs | `<scheduler/process/automation scope>` | operational | blocker | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-009 | environment/build/deploy/reproduce/maintain | `<procedure set>` | operational | blocker | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-010 | dependencies/secret refs | `<dependency/config scope>` | operational | blocker | not-attempted | unknown | unknown | none | `<U ID>` | blocked |
| CV-011 | historical/other unknowns | `<known blind-spot set>` | forensic | supporting | not-attempted | unknown | unknown | none | `<U ID>` | backlog |

Domain rows do not prove domain coverage if several material sources exist. Expand,
for example, accessible conversations into one row per thread or bounded thread set,
and remote infrastructure into rows with defensible scope.

## Defensible roll-up

- **Operational blocker rows:** `<count and IDs>`
- **Operational supporting partial/unknown rows:** `<count and IDs>`
- **Forensic open rows:** `<count and IDs>`
- **Operational `not-attempted` rows:** `<count and IDs>`
- **Scope limitations:** `<plain-language denominator limits>`

## Coverage assertions

- [ ] Every required domain has at least one scope row or justified `n/a`.
- [ ] Every known operational source has its own row or belongs to a named bounded set.
- [ ] Every inaccessible/unknown result links a detailed blind spot in `AUDIT.md`.
- [ ] Every `partial` result states the inspected subset and residual gap.
- [ ] No bare completeness percentage appears in migration claims.
- [ ] Operational and forensic tracks are not conflated.

