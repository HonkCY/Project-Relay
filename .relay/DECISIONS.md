# Decisions

Decision records are durable and Git-auditable. `authority` is governance,
`provenance` names the source class, and `verification` states what checking did.
Changing one never silently changes another.

## D-001 — The folder is authoritative

- **Authority:** accepted
- **Provenance:** human-report
- **Verification:** verified
- **Evidence ref:** authoritative design brief, sections 1–2
- **Checked at:** 2026-09-03
- **Decision:** Tracked canonical workspace files override remembered chat, agent
  memory, and compaction summaries. Those sources may prompt verification but are
  not project authority.

## D-002 — Use three canonical object types

- **Authority:** provisional
- **Provenance:** inference
- **Verification:** unverified
- **Evidence ref:** authoritative brief sections 8–10 and 15; failure-mode challenge
- **Checked at:** 2026-09-03
- **Decision:** v0.1 uses snapshot, record, and procedure objects. CHECKPOINT is a
  write-back lifecycle recorded by their Git diff/commit, not a second history store.
  File layout follows access and write patterns rather than making every domain a type.
- **Why:** This is the smallest set that retains current state, durable facts and
  decisions, exact operations, and transition history without meta-work explosion.

## D-003 — Separate authority, provenance, and verification

- **Authority:** provisional
- **Provenance:** inference
- **Verification:** unverified
- **Evidence ref:** authoritative brief sections 6–7; migration false-memory scenarios
- **Checked at:** 2026-09-03
- **Decision:** Every consequential migrated claim and operational record states
  governance authority, source provenance, and verification status. Verification
  never implies human acceptance, and incumbent-agent recollection implies neither.

## D-004 — Markdown and Git are sufficient for v0.1

- **Authority:** provisional
- **Provenance:** durable-artifact
- **Verification:** unverified
- **Evidence ref:** acceptance-test design and bounded prior-art review
- **Checked at:** 2026-09-03
- **Decision:** v0.1 requires no daemon, database, embeddings, or validator. Its
  acceptance tests use inspectable Markdown and ordinary Git/filesystem commands.
- **Revisit when:** a documented acceptance failure cannot be solved with stable
  IDs, links, filenames, and text search.

## D-005 — Native files remain thin adapters

- **Authority:** provisional
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** [prior art](../docs/prior-art.md)
- **Checked at:** 2026-09-03
- **Decision:** Root `AGENTS.md` points to Relay bootstrap files. Root `CLAUDE.md`
  imports `AGENTS.md`. Neither stores live project state.
