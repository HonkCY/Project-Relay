# Migration cutover — `<migration-id>`

Cutover changes the old native project/chat from incumbent witness to non-canonical
history. Complete this only after normalizing candidate claims into `.relay/`.

## Delta sweep

- **Previous watermark:** `<ISO-8601>`
- **Sweep completed at:** `<ISO-8601>`
- **Operator:** `<identity>`

| Volatile surface | Check performed | Evidence | Change since watermark | Canonical update |
| --- | --- | --- | --- | --- |
| Git branch/commit/dirty state | `<check>` | `<ref>` | `<none/change>` | `<ID/path>` |
| Recent material conversations | `<check>` | `<ref>` | `<none/change>` | `<ID/path>` |
| Active/pending/recurring jobs | `<check>` | `<ref>` | `<none/change>` | `<R ID/path>` |
| Service health/deploy state | `<check>` | `<ref>` | `<none/change>` | `<R ID/path>` |
| Remote outputs/resources | `<check>` | `<ref>` | `<none/change>` | `<R ID/path>` |
| Human decisions | `<check>` | `<ref>` | `<none/change>` | `<D ID/path>` |

Any known material drift that was not reconciled blocks cutover.

## Fresh-agent dry run

- **Agent/product:** `<fresh Codex or Claude Code>`
- **Freshness condition:** `<new session; no bespoke handoff or useful chat context>`
- **Started from:** `<project root and Git state>`
- **Records read:** `<paths/IDs observed, not supplied in prompt>`

| Question/task | Expected canonical source | Fresh-agent result | Evidence | Pass? |
| --- | --- | --- | --- | --- |
| State current frontier and active work | `.relay/STATE.md` | `<answer>` | `<capture/ref>` | `<yes/no>` |
| State accepted governing decisions | linked `D` records | `<answer>` | `<capture/ref>` | `<yes/no>` |
| State next human gate | `.relay/STATE.md` | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Locate one exact critical procedure | linked `P` record | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Locate one critical remote resource and lineage | linked `R` record | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Report job/service state using fresh evidence or unknown tense | linked `R` record + live check | `<answer>` | `<capture/ref>` | `<yes/no>` |
| Perform one safe task-relevant verification | procedure/record | `<result>` | `<capture/ref>` | `<yes/no>` |

Discrepancies: `<IDs, owners, dispositions or none>`

## Operational gate

- [ ] Required domains have explicit scope; no operational-critical row is `not-attempted`.
- [ ] Every operational-critical item has a disposition.
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

- **Residual non-blocking risks:** `<U/CV IDs and concise rationale>`
- **Forensic backlog:** `<CV/U IDs>`
- **Decision:** `<approved | rejected | changes required>`
- **Authorized human:** `<identity>`
- **Decision at:** `<ISO-8601>`
- **Cutover commit:** `<existing commit hash; fill only after it exists>`

After approval, freeze the migration dossier. Future corrections use dated addenda;
future operational changes update their normal canonical owners.

