# Records registry

This file owns operational entities for the Project Relay framework repository.
The common record and type-specific fields are defined by the
[protocol](../docs/protocol.md#record-requirements).

## R-001 — Framework Git repository

- **Kind:** repository
- **Authority:** provisional
- **Provenance:** live-environment
- **Verification:** verified
- **Purpose/claim:** version the v0.1 protocol, template, migration kit, and example
- **Locator:** repository root (`.`); `origin` is
  [HonkCY/Project-Relay](https://github.com/HonkCY/Project-Relay.git), the public
  publication destination supplied by the repository maintainer
- **Role:** source
- **Important contents:** protocol, templates, migration kit, acceptance scenarios,
  and the sanitized Coastwatch fixture
- **Inputs / outputs / dependencies:** authoritative design brief → public-safe
  Markdown design artifacts; no runtime dependency
- **Readers/writers:** humans and agents read; repository maintainers write through
  reviewed Git changes
- **Producer procedure:** implementation and P-001 review at the named Git boundary
- **Access:** local filesystem and Git; public HTTPS reads require no secret.
  Publishing uses the maintainer's externally managed GitHub authentication;
  credential values are not stored in Relay
- **Version/run:** final v0.1 seal boundary identified by annotated tag `v0.1`;
  annotated tag `v0.1-design` remains the fixed historical design boundary
- **Status or last observation:** final human review passed and v0.1 is sealed at the
  final annotated tag. The initial atomic publication created `main` and annotated
  tag `v0.1-design`. At that historical observation, remote `main` and the peeled tag
  both resolved to
  `18c6c216b8f574e5c436968e4e5032797983dee0`, before the later
  publication-metadata and acceptance checkpoints. The design tag remains fixed
  while `main` may advance
- **Evidence ref:** successful
  `git push --atomic --set-upstream origin main refs/tags/v0.1-design`;
  `git ls-remote origin refs/heads/main refs/tags/v0.1-design 'refs/tags/v0.1-design^{}'`;
  final owner decision on 2026-09-04;
  [R-003 final native acceptance evidence](RECORDS.md#r-003--bounded-retrieval-remediation-evidence);
  [v0.1 validation](../docs/validation.md)
- **Checked by:** Codex release seal agent
- **Checked at:** 2026-09-04T06:52:48Z
- **Valid until / recheck rule:** the final `v0.1` and historical `v0.1-design` tags
  are immutable boundaries; verify remote refs after publication
- **Owner:** repository maintainer
- **Risks/limitations:** other native-agent platforms remain outside v0.1 scope; no
  unresolved v0.1 design-review blocker remains

## R-002 — Native A-B acceptance evidence

- **Kind:** asset
- **Authority:** provisional
- **Provenance:** live-environment + durable-artifact
- **Verification:** verified
- **Purpose/claim:** records real clean-session Scenario A results and a real
  Claude Code Opus → Codex → Claude Code Opus Scenario B transition
- **Locator:**
  [`.relay/evidence/native-ab-2026-09-04/README.md`](evidence/native-ab-2026-09-04/README.md)
  with reconstructable B format patches below that directory
- **Role:** archive
- **Important contents:** exact prompts, versions/models, starting boundaries,
  observed file/ID reads, semantic answer mapping, transition commits, hashes,
  diffs, and unambiguous external verdicts
- **Inputs / outputs / dependencies:** P-001 and `docs/acceptance-tests.md`; updates
  the STATE review gate but does not change D-001–D-005 authority
- **Readers/writers:** repository reviewers read; acceptance harness writes a new
  dated evidence record for a later run rather than rewriting this observation
- **Producer procedure:** P-001 native A/B subset, run `2026-09-04-native-ab`
- **Access:** tracked public-safe Markdown and text patches; no secret required
- **Version/run:** `2026-09-04-native-ab`; first checkpoint containing this R record
  owns the Git boundary without a self-referential hash
- **Status or last observation:** Scenario A failed because both agents exceeded the
  task-relevant retrieval boundary despite correct semantic recovery; Scenario B
  passed all listed switch criteria
- **Evidence ref:** the locator above; B chain `f69e2dc` → `de48084` → `e64691e` →
  `8cbf40c`; external clean-tree, hash, and immutable-input checks
- **Checked by:** Codex acceptance harness with real native Claude Code and Codex CLIs
- **Checked at:** 2026-09-04T05:01:16Z
- **Valid until / recheck rule:** immutable observation; create a new dated record
  after adapter/protocol changes or any A/B rerun
- **Owner:** repository maintainer
- **Risks/limitations:** raw CLI event streams remain in the invoking task rather than
  Git; the checked-in summary preserves the review facts and B patches. A Claude
  compound `git status` check was denied by the read-only harness, but external
  before/after checks proved the clone clean; that harness issue is distinct from A's
  independently observed retrieval failure

## R-003 — Bounded-retrieval remediation evidence

- **Kind:** asset
- **Authority:** accepted
- **Provenance:** live-environment + durable-artifact
- **Verification:** verified
- **Accepted by/at:** project owner through final human review / 2026-09-04
- **Purpose/claim:** records the bounded-retrieval remediation iterations, final
  native Scenario A pass, and required final Scenario B regression pass at one
  candidate boundary
- **Locator:**
  [`.relay/evidence/native-ab-remediation-2026-09-04/README.md`](evidence/native-ab-remediation-2026-09-04/README.md)
  with reconstructable final B format patches below that directory
- **Role:** archive
- **Important contents:** unchanged prompts and rubric boundary, product/model
  versions, native START/STATE discovery, exact files/IDs/sections read, semantic
  answers, failed and passing remediation candidates, final transition commits,
  hashes, unrelated-read checks, and external verdicts
- **Inputs / outputs / dependencies:** P-001, `docs/acceptance-tests.md`, and R-002's
  immutable prior failure; updates the STATE review gate but does not change
  D-001–D-005 authority
- **Readers/writers:** repository reviewers read; a later acceptance run creates a
  new dated evidence record rather than rewriting this observation
- **Producer procedure:** P-001 native A/B subset, run
  `2026-09-04-native-ab-remediation`
- **Access:** tracked public-safe Markdown and text patches; no secret required
- **Version/run:** final remediation candidate
  `b7097c4741f5f9084f053d7a096415048f51f29c`; first checkpoint containing this
  R record owns the publication boundary without a self-referential hash
- **Status or last observation:** Scenario A passed in fresh Claude Code Opus and
  Codex sessions without any unrelated registry, migration, or evidence reads;
  Scenario B passed a fresh Claude Code Opus → Codex → Claude Code Opus regression
  at the same candidate boundary
- **Evidence ref:** the locator above; final B chain `a9ecf1e` → `4108b17` →
  `a16dbe4` → `b02bcbe`; external clean-tree, hash, immutable-input, canonical
  verification-consistency, and unchanged
  acceptance-specification checks
- **Checked by:** Codex acceptance harness with real native Claude Code and Codex CLIs
- **Checked at:** 2026-09-04T06:27:57Z
- **Valid until / recheck rule:** immutable observation; rerun A and then B after a
  later change to bootstrap/retrieval semantics
- **Owner:** repository maintainer
- **Risks/limitations:** raw CLI event streams remain in the invoking task rather
  than Git; the checked-in summary preserves review facts and reconstructable B
  transitions. This result advances a human gate only and does not accept provisional
  design decisions

## Tools

No MCP server, connector, or optional external tool is required to read or use the
v0.1 Markdown protocol. Native agent support for the two adapter files is described
in [prior art](../docs/prior-art.md).

## Services

No service is operated by this repository.

## Jobs

There are no canonical job records. Therefore the repository claims no scheduled,
queued, running, or autonomous background work.

## Secrets

No secret is required to read or use the protocol. Publishing the framework
repository uses externally managed GitHub authentication as described in R-001;
no credential value belongs in tracked files. Public examples use reserved,
non-resolving locators and contain no motivating-project data.
