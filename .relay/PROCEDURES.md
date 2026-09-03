# Procedures

## P-001 — Review the v0.1 design checkpoint

- **Authority:** provisional
- **Provenance:** durable-artifact
- **Verification:** unverified
- **Evidence ref:** `docs/acceptance-tests.md`; [v0.1 internal validation](../docs/validation.md)
- **Checked by/at:** Codex implementation agent / 2026-09-03
- **Owner:** repository maintainer
- **Last tested:** internal repository subset on 2026-09-03; full native A/B runs pending
- **Applies to:** D-002 through D-005 and all v0.1 acceptance scenarios

### Preconditions and inputs

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
6. If acceptable, explicitly accept or revise provisional decisions D-002–D-004 and
   verify conformance with accepted D-005.

### Outputs

A review verdict, evidence for each acceptance scenario, and any resulting updates to
the owning D/R/P records and STATE snapshot.

### Verification

- Each acceptance scenario has inspectable evidence and an unambiguous pass/fail.
- `git diff` is understandable and contains no duplicated live state in adapters.

### Recovery

If a scenario fails, leave the design provisional, store the detailed evidence in its
owning record or test artifact, surface only a linked urgent blocker in `STATE.md`,
then fix the owner and commit a coherent correction.
