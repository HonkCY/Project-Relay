# Current state

- **Frontier:** real native acceptance gate A/B has run against the v0.1 design:
  B passed; A recovered the correct state but failed its bounded-retrieval criterion.
- **Active work:** inspect [R-002 native A/B evidence](RECORDS.md#r-002--native-a-b-acceptance-evidence)
  and decide the smallest retrieval correction before rerunning A.
- **Next human gate:** review the A failure disposition and B pass, then authorize or
  revise the A remediation/retest boundary.

## Accepted governing decisions

- [D-001](DECISIONS.md#d-001--the-folder-is-authoritative) — the folder is authoritative.
- [D-005](DECISIONS.md#d-005--native-files-remain-thin-adapters) — native files remain thin adapters.

## Provisional design choices under review

- [D-002](DECISIONS.md#d-002--use-three-canonical-object-types) — use three canonical object types.
- [D-003](DECISIONS.md#d-003--separate-authority-provenance-and-verification) — authority, provenance, and verification are independent.
- [D-004](DECISIONS.md#d-004--markdown-and-git-are-sufficient-for-v01) — keep v0.1 Markdown/Git-only.

## Immediate risks and unknowns

- Human acceptance of the proposed v0.1 design is pending.
- Scenario A does not pass yet: both native agents read beyond the task-relevant owner
  set even though their reported frontier, decisions, gate, and unknowns were correct.
- Scenario B passed a real Claude Code Opus → Codex → Claude Code Opus transition.
  See [R-002](RECORDS.md#r-002--native-a-b-acceptance-evidence) for the exact evidence
  boundary. Other native-agent platforms remain outside v0.1 scope.

## Background execution

No background job, service, scheduler, automation, or delegated agent is claimed by
this canonical workspace.
