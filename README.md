# Project Relay

Project Relay is a folder-first, agent-neutral workspace protocol for long-running
research and engineering projects. It lets a fresh Codex or Claude Code session
recover the project's operational state from the repository instead of trusting
chat history, compaction summaries, or model memory.

> **Invariant:** agent, session, and model memory is disposable. Project state is
> not.

This repository is the v0.1 protocol, a copyable workspace template, a migration
kit, and a sanitized research-project example. It is deliberately Markdown-first:
native coding agents remain the execution harness, while Git and the project
folder are the durable system of record.

## Start here

- To understand the design, read [the protocol](docs/protocol.md).
- To inspect the object-model tradeoffs and failure-mode challenge, read
  [design decisions](docs/design-decisions.md).
- To add Relay to a new or already self-contained project, follow
  [INIT](docs/init.md).
- To externalize a project whose important state is still in native-agent chats,
  memories, remote hosts, or running systems, follow [MIGRATE](docs/migrate.md).
- To review the design, run the scenarios in
  [acceptance tests](docs/acceptance-tests.md).
- To inspect what was and was not exercised at the checkpoint, read the
  [v0.1 validation record](docs/validation.md).
- To see a filled workspace, open the
  [Coastwatch example](examples/coastwatch/README.md).

Do not substitute INIT for MIGRATE. If material context or external operational
state is latent, unexternalized, or uncertain, migration is a provenance
reconstruction, not a file-copy task. Explicitly supplied, already verifiable remote
records may still use INIT.

## Normal workspace experience

```text
cd project
codex                 # or: claude
```

The native agent reads a tiny root adapter, then always reads:

1. `.relay/START.md` — stable bootstrap rules and index
2. `.relay/STATE.md` — small current snapshot

It follows stable IDs and links into decisions, systems, or procedures only when
the task needs them. After a material change, it updates the owning canonical
record, refreshes the snapshot only if needed, and creates a coherent Git diff.

## The minimal model

| Object | Purpose | Typical write pattern |
| --- | --- | --- |
| Snapshot | Current frontier, active work, next human gate, urgent unknowns | Edit in place |
| Record | Decisions and operational entities, with authority, provenance, and verification | Edit in place; preserve supersession links |
| Procedure | Exact repeatable work, verification, and recovery | Edit in place |

CHECKPOINT is a lifecycle, not a fourth truth object: write the owning objects
promptly, inspect the diff, and commit a coherent transition when authorized. Git
already supplies the append-only history.

The default template maps these objects to five canonical Markdown files under
`.relay/`. Resources, environments, tools, services, jobs, and assets share one
record model rather than creating a taxonomy of databases. Large workspaces may
shard a file without changing the object model.

## Repository map

```text
AGENTS.md               Codex-compatible thin adapter
CLAUDE.md               Claude adapter importing AGENTS.md
.relay/                 Canonical state for this repository itself
docs/                   Normative protocol and lifecycle documents
template/               Minimal files copied during INIT
migration-kit/          Temporary audit and cutover worksheets for MIGRATE
examples/coastwatch/    Sanitized, remote-aware research example
```

## What Relay is not

Relay is not an API orchestrator, hosted memory service, chat UI, scheduler, or
vector database. It never claims background execution without a real process,
scheduler, service, or agent run that can be independently checked.

## Status

The [canonical repository state](.relay/STATE.md) owns the live checkpoint, review
gate, and known risks. This README's static version label is the v0.1 protocol design;
the [tagged validation record](docs/validation.md) preserves the pre-run v0.1 boundary,
while [R-002](.relay/RECORDS.md#r-002--native-a-b-acceptance-evidence) owns the latest
post-tag native A/B results.
