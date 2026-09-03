# Records registry

This file owns operational entities for the Project Relay framework repository.
The common record and type-specific fields are defined by the
[protocol](../docs/protocol.md#record-requirements).

## R-001 — Framework Git repository

- **Kind:** repository
- **Authority:** provisional
- **Provenance:** live-environment
- **Verification:** verified
- **Purpose:** version the v0.1 protocol, template, migration kit, and example
- **Locator:** repository root (`.`)
- **Role:** canonical source
- **Inputs:** authoritative design brief
- **Outputs:** public-safe Markdown design artifacts
- **Version/run:** current Git `HEAD` plus any visible working-tree changes
- **Status:** active
- **Evidence ref:** `git status --short --branch`
- **Checked at:** 2026-09-03
- **Risks:** the repository has not yet passed human review

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
