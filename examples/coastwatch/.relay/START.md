# Relay start

This is the sanitized Coastwatch fixture. The normative v0.1 rules are in
[`docs/protocol.md`](../../../docs/protocol.md).

## Bootstrap

1. Read [STATE.md](STATE.md) completely.
2. Inspect the Git working tree.
3. Follow task-relevant stable IDs into [DECISIONS.md](DECISIONS.md),
   [RECORDS.md](RECORDS.md), or [PROCEDURES.md](PROCEDURES.md).
4. Treat the migration dossier as frozen supporting provenance, not ongoing truth.
5. Recheck time-sensitive state before using present tense. A stale “running”
   observation means current state is unknown.

Search hidden canonical files explicitly:

```sh
rg --hidden --glob '!.git/**' '<term>' .relay
```

`STATE.md` owns coordination state; D records own decisions; R records own locators,
lineage, and observations; P records own exact actions; Git owns history. Chat and
agent memory are non-canonical.

Write back only material changes: update the owner, then STATE only if its snapshot
changed, inspect the diff, and commit coherently when authorized.

