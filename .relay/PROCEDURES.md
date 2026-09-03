# Procedures

## P-001 — Review the v0.1 design checkpoint

- **Authority:** provisional
- **Provenance:** durable-artifact
- **Verification:** unverified
- **Owner:** repository maintainer
- **Last tested:** not yet

### Preconditions

- All files are visible in the working tree.
- The reviewer has read the authoritative design brief or its required outcomes.

### Steps

1. Read `README.md`, `docs/protocol.md`, `docs/init.md`, and `docs/migrate.md`.
2. Inspect `template/` as a fresh workspace and `examples/coastwatch/` as a filled
   remote-aware workspace.
3. Execute every Given/When/Then scenario in `docs/acceptance-tests.md`.
4. Check the repository for private locators, credentials, secret-like assignments,
   or motivating-project excerpts.
5. Record failures against stable IDs; do not hide unknown or inaccessible surfaces.
6. If acceptable, explicitly accept or revise provisional decisions D-002–D-005.

### Verification

- Each acceptance scenario has inspectable evidence and an unambiguous pass/fail.
- `git diff` is understandable and contains no duplicated live state in adapters.

### Recovery

If a scenario fails, leave the design provisional, record the failing evidence and
impact in `STATE.md`, then fix the owning record and commit a coherent correction.
