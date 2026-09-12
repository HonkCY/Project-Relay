# Current state

- **Frontier:** Project Relay v0.1 remains sealed. The approved v0.2 implementation
  scope adds conservative workspace-integrity rules without changing canonical
  objects or native adapters.
- **Active work:** implement and validate bounded usability/owner-conflict checks,
  checkpoint read-back, and writer/copy boundaries; run new fault fixtures and
  fresh native A/B/C regression at a recorded candidate.
- **Next human gate:** review the v0.2 candidate and its separate validation. The
  earlier post-v0.1 forensic-capture enhancement also remains pending explicit
  owner acceptance; implementation authorization does not accept either release.

## Accepted governing decisions

- [D-001](DECISIONS.md#d-001--the-folder-is-authoritative) — the folder is authoritative.
- [D-002](DECISIONS.md#d-002--use-three-canonical-object-types) — use three canonical object types.
- [D-003](DECISIONS.md#d-003--separate-authority-provenance-and-verification) — authority, provenance, and verification are independent.
- [D-004](DECISIONS.md#d-004--markdown-and-git-are-sufficient-for-v01) — keep v0.1 Markdown/Git-only.
- [D-005](DECISIONS.md#d-005--native-files-remain-thin-adapters) — native files remain thin adapters.

## Immediate risks and unknowns

None within the sealed v0.1 scope. New workspace-integrity behavior has not yet
completed native regression; no v0.2 PASS or release is claimed. Read-back cannot
prove storage durability, remote sync completion, or cross-file atomicity. The
post-v0.1 helper remains optional: `.relay/private/` is non-canonical, non-portable,
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
- [Upgrade guidance](../docs/upgrade-v0.2.md) and
  [disposable fault fixtures](../tests/README-workspace-integrity.md) define the
  scoped implementation and new validation without rewriting historical evidence.

## Background execution

No background job, service, scheduler, automation, or delegated agent is claimed by
this canonical workspace.
