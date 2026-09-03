# Relay start

This project uses Project Relay protocol v0.1. The root native-agent files are thin
adapters; tracked files in `.relay/` are the portable canonical workspace.

## Bootstrap

1. Read [STATE.md](STATE.md) completely.
2. Inspect `git status --short --branch`; a dirty canonical file may be newer than
   `HEAD` and must not be discarded automatically.
3. Follow only task-relevant stable IDs:
   - [DECISIONS.md](DECISIONS.md) — accepted, provisional, superseded, rejected choices
   - [RECORDS.md](RECORDS.md) — repositories, assets, hosts, tools, services, jobs, unknowns
   - [PROCEDURES.md](PROCEDURES.md) — exact repeatable operations
4. Recheck time-sensitive facts. After evidence expires, say “last observed” or
   `unknown`, never timeless `running`.
5. If memory conflicts with canonical state or evidence, record and verify the
   conflict; do not choose silently.

Because this is a hidden directory, search with an explicit path or, for example:

```sh
rg --hidden --glob '!.git/**' '<term>' .relay
```

## Field ownership

- `STATE.md` alone owns frontier, active work, next human gate, and urgent blockers.
- A decision record owns decision text, authority, rationale, and supersession.
- An operational record owns locators, lineage, dependencies, observed state, and
  verification freshness.
- A procedure owns exact commands/steps, verification, and recovery.
- Git owns transition history. Do not create a second full-state handoff log.

Other files may show an ID, title, and link, but MUST NOT maintain another copy of a
field's value.

## Epistemic fields

Consequential records separate:

- **Authority:** `accepted`, `provisional`, `superseded`, `rejected`, `unresolved`
- **Provenance:** `live-environment`, `durable-artifact`, `incumbent-recall`,
  `human-report`, `inference`, `unknown`
- **Verification:** `verified`, `unverified`, `contradicted`, `stale`, `inaccessible`

Include an evidence reference and checked-at time. `accepted` does not mean verified;
`verified` does not mean human-accepted. An agent may propose but must not replace an
accepted choice without explicit human acceptance.

## Job truth

`queued` or `running` requires a real mechanism, host, process/job/run ID, command or
spec reference, log/output locator, submit/start time, current check evidence and
time/freshness, owner, and next human gate. A conversation, plan, or word “wait” is
not execution evidence. A scheduler claim requires a real scheduler entry and ID.

## Checkpoint / write-back

Write back promptly when a material decision, frontier/gate, canonical artifact,
remote job/service state, exact recovery-critical procedure, blocker, or unknown
changes, and before a likely switch/context-loss boundary.

1. Verify where possible.
2. Edit the one owning record/procedure.
3. Refresh `STATE.md` only if its snapshot fields changed.
4. Review the Git diff; commit one coherent transition when authorized.

Saving the canonical files is the crash-resistant checkpoint. Do not checkpoint
ordinary commentary, unchanged polls, or every turn.

