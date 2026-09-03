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
- **Locator:** repository root (`.`)
- **Role:** source
- **Important contents:** protocol, templates, migration kit, acceptance scenarios,
  and the sanitized Coastwatch fixture
- **Inputs / outputs / dependencies:** authoritative design brief → public-safe
  Markdown design artifacts; no runtime dependency
- **Readers/writers:** humans and agents read; repository maintainers write through
  reviewed Git changes
- **Producer procedure:** implementation and P-001 review at the named Git boundary
- **Access:** local filesystem and Git; no secret required
- **Version/run:** v0.1 design boundary identified by annotated tag `v0.1-design`
- **Status or last observation:** active design repository; human review pending
- **Evidence ref:** `git status --short --branch`; [v0.1 validation](../docs/validation.md)
- **Checked by:** Codex implementation agent
- **Checked at:** 2026-09-03
- **Valid until / recheck rule:** recheck after the release tag, branch, or working tree changes
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

No secret is required. Public examples use reserved, non-resolving locators and
contain no motivating-project data.
