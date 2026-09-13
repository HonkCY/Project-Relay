# Current state

- **Frontier:** Project Relay v0.1 remains sealed. The approved v0.2 implementation
  scope adds conservative workspace-integrity rules without changing canonical
  objects or native adapters; the Reader lifecycle addition is a review candidate.
- **Active work:** Reader source/output/query boundaries, task-local checkpoint and
  recovery, and selective Maintainer integration are implemented. Review the
  separate synthetic validation: 41 mechanical tests pass, but fresh native Reader
  conformance still fails; do not infer release readiness from useful deliverables.
- **Next human gate:** review the Reader changes, native failures and remaining
  regression work before any acceptance or real-workspace rollout. The
  earlier post-v0.1 forensic-capture enhancement also remains pending explicit
  owner acceptance; implementation authorization does not accept either release.

## Accepted governing decisions

- [D-001](DECISIONS.md#d-001--the-folder-is-authoritative) — the folder is authoritative.
- [D-002](DECISIONS.md#d-002--use-three-canonical-object-types) — use three canonical object types.
- [D-003](DECISIONS.md#d-003--separate-authority-provenance-and-verification) — authority, provenance, and verification are independent.
- [D-004](DECISIONS.md#d-004--markdown-and-git-are-sufficient-for-v01) — keep v0.1 Markdown/Git-only.
- [D-005](DECISIONS.md#d-005--native-files-remain-thin-adapters) — native files remain thin adapters.

## Immediate risks and unknowns

None within the sealed v0.1 scope. The first v0.2 native candidate passed A and C but
failed new fault conformance through excess retrieval and a missed background-safety
gap. Targeted reminder remediation and an equal-authority duplicate fixture correction
are awaiting fresh regression; no v0.2 PASS or release is claimed. Read-back cannot
prove storage durability, remote sync completion, or cross-file atomicity. The
post-v0.1 helper remains optional: `.relay/private/` is non-canonical, non-portable,
and unnecessary for fresh-agent continuation.

The Reader tests expose native over-retrieval, incomplete checkpoint read-back and
recovery-entry omissions. No hard source-write denial was independently established;
unchanged synthetic source/Git bytes are only an observation. Existing v0.2 failures
and the final native compatibility/release gate remain open; this addition does not
repair them by assertion or lower their criteria.

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
- [Reader validation](../docs/validation.md#reader-lifecycle-addendum--2026-09-13)
  and its [separate evidence](evidence/reader-mode-2026-09-13/README.md) distinguish
  mechanical checks, actual native behavior, and unverified enforcement. Only
  newly generated fixtures were used; no real workspace or remote source was read.

## Background execution

No background job, service, scheduler, automation, or delegated agent is claimed by
this canonical workspace.
