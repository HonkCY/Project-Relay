# Records registry

Use stable IDs (`R-001`, `R-002`, …). Put durable unknowns here as `kind: unknown`.
Leave absent categories empty; do not invent entities to fill the template.

## Common record shape

```markdown
## R-001 — Concise title

- **Kind:** repository | host | resource | asset | environment | tool | service | job | secret-ref | unknown
- **Authority:** accepted | provisional | superseded | rejected | unresolved
- **Provenance:** live-environment | durable-artifact | incumbent-recall | human-report | inference | unknown
- **Verification:** verified | unverified | contradicted | stale | inaccessible
- **Purpose/claim:** exact scope
- **Status or last observation:** value plus time when time-sensitive
- **Evidence ref:** safe locator or check result
- **Checked at:** ISO-8601 timestamp/date or unknown
- **Checked by:** human/agent/tool identity or unknown
- **Valid until / recheck rule:** time/event or not-applicable
- **Accepted by/at:** identity/time when authority is accepted
- **Owner:** human/role or unknown
- **Inputs / outputs / dependencies:** stable IDs or none
- **Risks/limitations:** none or explicit unknown
```

If fields inside one record have different sources or check results, annotate them
at field/claim level instead of falsely upgrading the whole record.

## Resources, assets, repositories, hosts, environments

Additionally record safe locator/access method, role (`source`, `canonical`,
`derived`, `cache`, `scratch`, `archive`, `legacy`), important contents, readers and
writers, producer procedure/job plus commit/version/run, lifecycle state, and secret
reference without values. Remote data normally remains remote.

No records yet.

## Tools and MCPs

Additionally record identity, required/optional status, dependent functions,
capabilities used, config locator, auth/secret class, and replacement/recovery notes.

No records yet.

## Services

Additionally record desired state separately from observed state, host/runtime/safe
endpoint, source/config, lifecycle and deploy procedure IDs, health check result/time,
dependencies, logs, persistent state, and risk.

No records yet.

## Jobs

Allowed observed states: `planned`, `queued`, `running`, `blocked`, `succeeded`,
`failed`, `cancelled`, `absent`, `unknown`. `queued`/`running` requires mechanism,
host, real process/job/run ID, command/spec and working-directory/revision reference,
inputs, outputs/logs, submit/start time, check method/result/time/freshness, owner,
next human gate, and recovery procedure. Store exact commands in a procedure and link
them here. Recurring/scheduled work also requires scheduler/automation entry ID,
schedule, next-run evidence, and a disable procedure.

No records yet; therefore no background work is claimed.

## Unknowns and blind spots

Additionally record impact, safe constraint/workaround, owner, next action, and
recheck condition.

No records yet.

## Secrets

Store only secret class plus safe configuration/acquisition reference, never a value.

No records yet.
