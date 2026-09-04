# Relay start

This is the sanitized Coastwatch fixture. The normative v0.1 rules are in
[`docs/protocol.md`](../../../docs/protocol.md).

## Bootstrap

1. Start with the native adapter, this START file, and [STATE.md](STATE.md); read
   START and STATE completely.
2. Inspect the Git working tree.
3. Build the working set requested by the prompt from START and STATE, and answer
   from that set before expanding it. Stable-ID links into
   [DECISIONS.md](DECISIONS.md), [RECORDS.md](RECORDS.md), and
   [PROCEDURES.md](PROCEDURES.md) are on-demand pointers, not default reads.
4. Treat the migration dossier, evidence archives, and historical audit/provenance
   records as supporting provenance, not ordinary bootstrap material.
5. Recheck time-sensitive state before using present tense. A stale “running”
   observation means current state is unknown.

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

Do not expand supporting provenance during bootstrap unless the task explicitly
requires audit/history/provenance, or a task-relevant canonical owner needs that
evidence to resolve a conflict or verification question.

Search hidden canonical files explicitly:

```sh
rg --hidden --glob '!.git/**' '<term>' .relay
```

`STATE.md` owns coordination state; D records own decisions; R records own locators,
lineage, and observations; P records own exact actions; Git owns history. Chat and
agent memory are non-canonical.

Write back only material changes: update the owner, then STATE only if its snapshot
changed, inspect the diff, and commit coherently when authorized.
