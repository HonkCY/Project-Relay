# Current state

- **Frontier:** bounded-retrieval remediation is complete; real fresh native A and
  the required post-remediation B regression both pass at candidate `b7097c4`.
- **Active work:** human review of the remediation diff and
  [R-003 acceptance evidence](RECORDS.md#r-003--bounded-retrieval-remediation-evidence).
- **Next human gate:** the repository maintainer accepts or revises the remediation
  candidate. This gate does not itself accept D-002–D-004 or authorize a release tag.

## Accepted governing decisions

- [D-001](DECISIONS.md#d-001--the-folder-is-authoritative) — the folder is authoritative.
- [D-005](DECISIONS.md#d-005--native-files-remain-thin-adapters) — native files remain thin adapters.

## Provisional design choices under review

- [D-002](DECISIONS.md#d-002--use-three-canonical-object-types) — use three canonical object types.
- [D-003](DECISIONS.md#d-003--separate-authority-provenance-and-verification) — authority, provenance, and verification are independent.
- [D-004](DECISIONS.md#d-004--markdown-and-git-are-sufficient-for-v01) — keep v0.1 Markdown/Git-only.

## Immediate risks and unknowns

- Human acceptance of the proposed v0.1 design is pending.
- [R-002](RECORDS.md#r-002--native-a-b-acceptance-evidence) preserves the original
  Scenario A bounded-retrieval failure and the pre-remediation B pass.
- [R-003](RECORDS.md#r-003--bounded-retrieval-remediation-evidence) records the final
  A pass and the required B rerun pass at the same remediation candidate. Other
  native-agent platforms remain outside v0.1 scope.

## Background execution

No background job, service, scheduler, automation, or delegated agent is claimed by
this canonical workspace.
