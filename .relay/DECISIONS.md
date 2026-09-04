# Decisions

Decision records are durable and Git-auditable. `authority` is governance,
`provenance` names the source class, and `verification` states what checking did.
Changing one never silently changes another.

## D-001 — The folder is authoritative

- **Kind:** decision
- **Authority:** accepted
- **Provenance:** human-report
- **Verification:** verified
- **Evidence ref:** authoritative design brief, sections 1–2
- **Checked by:** Codex implementation agent
- **Checked at:** 2026-09-03
- **Accepted by/at:** project owner through the authoritative brief / 2026-09-03
- **Supersedes / superseded by:** none
- **Decision:** Tracked canonical workspace files override remembered chat, agent
  memory, and compaction summaries. Those sources may prompt verification but are
  not project authority.

## D-002 — Use three canonical object types

- **Kind:** decision
- **Authority:** accepted
- **Provenance:** inference
- **Verification:** verified
- **Evidence ref:** authoritative brief sections 8–10 and 15; failure-mode challenge;
  [v0.1 validation](../docs/validation.md)
- **Checked by:** Codex implementation agent
- **Checked at:** 2026-09-03
- **Accepted by/at:** project owner through final human review / 2026-09-04
- **Supersedes / superseded by:** none
- **Decision:** v0.1 uses snapshot, record, and procedure objects. CHECKPOINT is a
  write-back lifecycle recorded by their Git diff/commit, not a second history store.
  File layout follows access and write patterns rather than making every domain a type.
- **Why:** This is the smallest set that retains current state, durable facts and
  decisions, exact operations, and transition history without meta-work explosion.

## D-003 — Separate authority, provenance, and verification

- **Kind:** decision
- **Authority:** accepted
- **Provenance:** inference
- **Verification:** verified
- **Evidence ref:** authoritative brief sections 6–7; migration false-memory scenarios;
  [v0.1 validation](../docs/validation.md)
- **Checked by:** Codex implementation agent
- **Checked at:** 2026-09-03
- **Accepted by/at:** project owner through final human review / 2026-09-04
- **Supersedes / superseded by:** none
- **Decision:** Every consequential migrated claim and operational record states
  governance authority, source provenance, and verification status. Verification
  never implies human acceptance, and incumbent-agent recollection implies neither.

## D-004 — Markdown and Git are sufficient for v0.1

- **Kind:** decision
- **Authority:** accepted
- **Provenance:** durable-artifact
- **Verification:** verified
- **Evidence ref:** acceptance-test design, bounded prior-art review, and
  [v0.1 validation](../docs/validation.md); the successful bounded-retrieval
  remediation in [R-003](RECORDS.md#r-003--bounded-retrieval-remediation-evidence)
- **Checked by:** Codex implementation agent
- **Checked at:** 2026-09-03
- **Accepted by/at:** project owner through final human review / 2026-09-04
- **Supersedes / superseded by:** none
- **Decision:** v0.1 requires no daemon, database, embeddings, or validator. Its
  acceptance tests use inspectable Markdown and ordinary Git/filesystem commands.
- **Revisit when:** a documented acceptance failure cannot be solved with stable
  IDs, links, filenames, and text search.

## D-005 — Native files remain thin adapters

- **Kind:** decision
- **Authority:** accepted
- **Provenance:** human-report + durable-artifact
- **Verification:** verified
- **Evidence ref:** authoritative brief section 2.3 and [prior art](../docs/prior-art.md)
- **Checked by:** Codex implementation agent
- **Checked at:** 2026-09-03
- **Accepted by/at:** project owner through the authoritative brief / 2026-09-03
- **Supersedes / superseded by:** none
- **Decision:** Root `AGENTS.md` points to Relay bootstrap files. Root `CLAUDE.md`
  imports `AGENTS.md`. Neither stores live project state.
