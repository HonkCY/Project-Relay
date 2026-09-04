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
- **Version/run:** v0.1 design boundary identified by annotated tag `v0.1-design`
- **Status or last observation:** active design repository; v0.1 design checkpoint
  published to `origin`; human review pending. The initial atomic push created
  `main` and annotated tag `v0.1-design`. At the observation below, remote `main`
  and the peeled tag both resolved to
  `18c6c216b8f574e5c436968e4e5032797983dee0`, before this publication-metadata
  checkpoint. The design tag remains fixed while `main` may advance
- **Evidence ref:** successful
  `git push --atomic --set-upstream origin main refs/tags/v0.1-design`;
  `git ls-remote origin refs/heads/main refs/tags/v0.1-design 'refs/tags/v0.1-design^{}'`;
  [v0.1 validation](../docs/validation.md)
- **Checked by:** Codex publication agent
- **Checked at:** 2026-09-04T04:22:11Z
- **Valid until / recheck rule:** this is a historical publication observation;
  verify the remote URL, branch, and release tag before the next publication or handoff
- **Owner:** repository maintainer
- **Risks/limitations:** the repository has not yet passed human review

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
