# Relay start

This project uses Project Relay protocol v0.1. The root native-agent files are thin
adapters; tracked files in `.relay/` are the portable canonical workspace.

## Bootstrap

1. Start with the native adapter, this START file, and [STATE.md](STATE.md); read
   START and STATE completely.
2. Inspect `git status --short --branch`; a dirty canonical file may be newer than
   `HEAD` and must not be discarded automatically.
3. Build the working set requested by the prompt from START and STATE, and answer
   from that set before expanding it. Stable-ID links are on-demand pointers, not
   default read obligations:
   - [DECISIONS.md](DECISIONS.md) — accepted, provisional, superseded, rejected choices
   - [RECORDS.md](RECORDS.md) — repositories, assets, hosts, tools, services, jobs, unknowns
   - [PROCEDURES.md](PROCEDURES.md) — exact repeatable operations
4. Recheck time-sensitive facts. After evidence expires, say “last observed” or
   `unknown`, never timeless `running`.
5. If memory conflicts with canonical state or evidence, record and verify the
   conflict; do not choose silently.

If STATE already answers a requested fact, do not follow its deeper owner merely to
reconfirm it, increase confidence, or understand the whole project. Follow a D/R/P
ID only when the requested fact is absent from STATE, the task executes or modifies
that owner, exact procedure/resource detail is required, a time-sensitive fact needs
fresh verification, or a conflict/uncertainty cannot be resolved from the snapshot.
A request for where exact detail lives is answered by the ownership map and pointer;
it does not by itself request that detail.

When following an ID, read only that stable-ID record or section and the direct
dependencies it references that are required for the task; do not follow a
transitive chain by default. Its presence in a monolithic registry does not make the
full registry part of the working set. Locate the exact ID heading first, then use a
bounded line range or the equivalent offset/limit operation in the native tool.

Stop bootstrap retrieval once every requested item has an authoritative owner, the
current coordination state is sufficient to answer, no required freshness/conflict/
uncertainty remains, and the task has not requested execution, modification, audit,
or provenance reconstruction. Do not continue for “complete understanding.”

Migration dossiers, evidence archives, and historical audit/provenance records are
supporting provenance, not ordinary bootstrap material. Do not expand them unless
the task explicitly requires audit/history/provenance, or a task-relevant canonical
owner needs that evidence to resolve a conflict or verification question.

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
