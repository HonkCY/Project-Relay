# Migration cutover — `<migration-id>`

Cutover changes the old native-agent project context, chat, and memory from incumbent
witnesses to non-canonical history. It does not demote an underlying target repository
or external system whose authority is recorded in D/R owners. Complete this only
after normalizing candidate claims into `.relay/`.

- **Fresh-agent candidate commit:** `<clean candidate commit tested in Phase 7>`
- **Coverage/records reviewed at:** `<later pre-cutover commit containing that run's evidence>`
- **Cutover tag to create after decision commit:** `relay-cutover-<migration-id>`

This file's gate checklist is a derived verdict from that named coverage/record
boundary; `COVERAGE.md` remains the owner of per-surface state.

## Delta sweep

- **Previous watermark:** `<ISO-8601>`
- **Sweep completed at:** `<ISO-8601>`
- **Operator:** `<identity>`

| Volatile surface | Check performed | Checked by/at | Evidence | Change since watermark | Canonical update |
| --- | --- | --- | --- | --- | --- |
| Git branch/commit/dirty state | `<check>` | `<identity/time>` | `<ref>` | `<none/change>` | `<ID/path>` |
| Recent material conversations | `<check>` | `<identity/time>` | `<ref>` | `<none/change>` | `<ID/path>` |
| Active/pending/recurring jobs | `<check>` | `<identity/time>` | `<ref>` | `<none/change>` | `<R ID/path>` |
| Service health/deploy state | `<check>` | `<identity/time>` | `<ref>` | `<none/change>` | `<R ID/path>` |
| Remote outputs/resources | `<check>` | `<identity/time>` | `<ref>` | `<none/change>` | `<R ID/path>` |
| Human decisions | `<check>` | `<identity/time>` | `<ref>` | `<none/change>` | `<D ID/path>` |

Any known material drift that was not reconciled blocks cutover.

## Fresh-agent dry run

- **Agent/product:** `<fresh Codex or Claude Code>`
- **Freshness condition:** `<new session; no bespoke handoff or useful chat context>`
- **Started from:** `<project root at the exact fresh-agent candidate commit above>`
- **Records read:** `<paths/IDs observed, not supplied in prompt>`

| Question/task | Expected canonical source | Fresh-agent result | Evidence | Pass? |
| --- | --- | --- | --- | --- |
| State candidate frontier and active work | `.relay/STATE.md` | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Report cutover status, current migration gate, and incumbent boundary | `.relay/STATE.md` | `<candidate/not cut over; operational cutover; live incumbent workspace; agent only operator/witness>` | `<capture/ref>` | `<yes/no>` |
| State accepted governing decisions | linked `D` records | `<answer>` | `<capture/ref>` | `<yes/no>` |
| State proposed post-cutover next human gate | `.relay/STATE.md` | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Locate one exact critical procedure | linked `P` record | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Locate one critical remote resource and lineage | linked `R` record | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Report job/service state using fresh evidence or unknown tense | linked `R` record + live check | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Perform one safe task-relevant verification | procedure/record | `<executed result, not procedure selection>` | `<capture/ref>` | `<yes/no>` |

Discrepancies: `<IDs, owners, dispositions or none>`

## Operational gate

- [ ] Required domains have explicit scope; no operational/critical row is `not-attempted`.
- [ ] Every coverage row obeys the access/result/disposition state matrix.
- [ ] No operational coverage row remains `pending` or `backlog`, and no row remains `blocked`.
- [ ] No forensic coverage row remains `pending`; each open forensic row is in the backlog
  table with owner, value, next action, and recheck condition.
- [ ] No unresolved critical unknown/conflict permits unsafe continuation.
- [ ] Frontier, active work, accepted decisions, and next gate are canonical.
- [ ] Required runbooks are exact and verified or their limitation blocks unsafe use.
- [ ] Critical remote resources are locatable with inputs/outputs/readers/writers and lineage.
- [ ] Job/service reports have real identifiers and time-stamped evidence, or say unknown/absent.
- [ ] False incumbent-memory conflicts have explicit dispositions.
- [ ] Delta sweep reconciled all material drift.
- [ ] Fresh-agent dry run passed.
- [ ] Public/private safety check passed for the destination's intended visibility.

## Human cutover authority

### Residual non-blocking risks

| Coverage/unknown IDs | Safe constraint | Residual rationale | Accepted by/at |
| --- | --- | --- | --- |
| `<CV/U IDs>` | `<constraint>` | `<why continuation is safe>` | `<identity/time>` |

### Forensic backlog

| Coverage/unknown IDs | Value/reason | Owner | Next action | Recheck condition |
| --- | --- | --- | --- | --- |
| `<CV/U IDs>` | `<why retain>` | `<identity>` | `<action>` | `<event/time>` |

### Decision

- **Decision:** `<approved | rejected | changes required>`
- **Authorized human:** `<identity>`
- **Decision at:** `<ISO-8601>`
- **Reviewed state:** `<same existing boundary named above>`
- **Cutover tag:** `relay-cutover-<migration-id>` (create after committing this decision)

If the decision is `rejected` or `changes required`, record it but keep this dossier
active: do not cut over, freeze, or tag. Fix the owning records, return to MIGRATE
Phase 6, create a new candidate, and rerun Phase 7.

Only after approval, commit this decision, create the named annotated tag at that
commit, and freeze the migration dossier. The tag, rather than a self-referential
hash inside the commit, identifies cutover. Future corrections use dated addenda;
future operational changes update their normal canonical owners.
