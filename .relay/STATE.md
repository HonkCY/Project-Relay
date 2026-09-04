# Current state

- **Frontier:** Project Relay v0.1 remains sealed; a conservative post-v0.1
  MIGRATE native-session forensic snapshot enhancement is implemented and validated
  on `main` as a review candidate.
- **Active work:** project-owner review of the bounded forensic-capture enhancement.
- **Next human gate:** accept or revise this post-v0.1 enhancement; the sealed v0.1
  design and native A/B boundary is unchanged.

## Accepted governing decisions

- [D-001](DECISIONS.md#d-001--the-folder-is-authoritative) — the folder is authoritative.
- [D-002](DECISIONS.md#d-002--use-three-canonical-object-types) — use three canonical object types.
- [D-003](DECISIONS.md#d-003--separate-authority-provenance-and-verification) — authority, provenance, and verification are independent.
- [D-004](DECISIONS.md#d-004--markdown-and-git-are-sufficient-for-v01) — keep v0.1 Markdown/Git-only.
- [D-005](DECISIONS.md#d-005--native-files-remain-thin-adapters) — native files remain thin adapters.

## Immediate risks and unknowns

None within the sealed v0.1 scope. The post-v0.1 helper is optional tooling for
private migration evidence; `.relay/private/` remains non-canonical, non-portable,
and unnecessary for fresh-agent continuation.

## Retained evidence and scope

- [R-002](RECORDS.md#r-002--native-a-b-acceptance-evidence) preserves the original
  Scenario A bounded-retrieval failure and the pre-remediation B pass.
- [R-003](RECORDS.md#r-003--bounded-retrieval-remediation-evidence) is the accepted
  final A pass and required B rerun evidence at the same remediation candidate.
- The post-v0.1 MIGRATE enhancement has a separately labelled
  [validation addendum](../docs/validation.md#post-v01-migrate-native-session-snapshot-addendum--2026-09-05);
  it does not rewrite R-002/R-003, the A/B rubric, or the frozen Coastwatch dossier.
- Other native-agent platforms remain outside v0.1 scope.

## Background execution

No background job, service, scheduler, automation, or delegated agent is claimed by
this canonical workspace.
