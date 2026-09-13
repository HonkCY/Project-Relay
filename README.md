# Project Relay

Project Relay is a folder-first, agent-neutral workspace protocol for long-running
research and engineering projects. It lets a fresh Codex or Claude Code session
recover the project's operational state from the repository instead of trusting
chat history, compaction summaries, or model memory.

> **Invariant:** agent, session, and model memory is disposable. Project state is
> not.

This repository contains the protocol, a copyable workspace template, a migration
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
- To merge the proposed v0.2 integrity rules into an existing workspace, follow the
  [upgrade guide](docs/upgrade-v0.2.md).
- To review the design, run the scenarios in
  [acceptance tests](docs/acceptance-tests.md).
- To exercise v0.2 read/write and copy-boundary faults, use the
  [disposable integrity fixtures](tests/README-workspace-integrity.md).
- To inspect what was and was not exercised at the checkpoint, read the
  [validation record](docs/validation.md).
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
the task needs them. After a material change, an authorized Maintainer updates the
owning canonical record, refreshes the snapshot only if needed, reads back the
affected sections, and creates a coherent Git diff. A Reader instead saves and
reads back its work in its own authorized output area; the source stays read-only.

## Reader: investigate and deliver without updating the source

Reader is a session/task contract, not a shared-folder switch. It can retrieve
original material through authorized R/P interfaces, compare evidence, and deliver
analysis or proposed changes. Context access alone grants neither external query
authority nor source write authority. Its output, scratch, and cache belong to one
exclusive task outside the source workspace. See the
[access contract](docs/protocol.md#session-access-contract) and optional
[task checkpoint template](reader-kit/TASK.md); do not create another editable
`.relay/` as project truth.

These examples use synthetic paths, not existing project authorization:

```text
Start: Use Reader mode from /tmp/relay-demo/source. Compare the designated archived
evidence with original text through its authorized R/P source interface, within
the recorded query budget. Save material and task checkpoints only under the new,
exclusive /tmp/relay-demo/task-a (including scratch/cache). Do not modify any source
or source Git state. Deliver the comparison with source locators, then stop.

Resume: Resume /tmp/relay-demo/task-a/TASK.md as Reader. Preserve its source/output
and query limits, reopen the source entry, and continue only the saved unfinished
comparison. Do not update the source; report any uncertain unsaved interval.

Integrate: As the authorized Maintainer for this synthetic source, review task-a's
delivery against current source owners. Selectively integrate applicable findings,
preserve newer work, read back changes and review the diff. Do not treat the Reader's
assessment as human acceptance or apply its delivery wholesale.
```

If mode is omitted, existing explicitly authorized maintenance may continue within
its scope; tool availability or a checkpoint instruction does not grant authority.
Missing permissions constrain the affected operation, not all safe reading and
reporting. Reader restrictions survive compaction and a generic `continue`; mutable
task metadata cannot grant its author new permissions. The protocol states the
contract; actual file/tool permissions must enforce it when hard isolation is needed.

## The minimal model

| Object | Purpose | Typical write pattern |
| --- | --- | --- |
| Snapshot | Current frontier, active work, next human gate, urgent unknowns | Edit in place |
| Record | Decisions and operational entities, with authority, provenance, and verification | Edit in place; preserve supersession links |
| Procedure | Exact repeatable work, verification, and recovery | Edit in place |

CHECKPOINT is a lifecycle, not a fourth truth object: authorized maintenance writes
the owning objects, confirms expected local content by bounded read-back, inspects
the diff, and commits a coherent transition when authorized. Reader checkpoints
save task progress and evidence outside those owners. Git already supplies the
project's append-only history.

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
reader-kit/             Optional task-local Reader boundary/checkpoint template
examples/coastwatch/    Sanitized, remote-aware research example
```

## What Relay is not

Relay is not an API orchestrator, hosted memory service, chat UI, scheduler, or
vector database. It never claims background execution without a real process,
scheduler, service, or agent run that can be independently checked.

## Status

Project Relay v0.1 is accepted and sealed at the annotated `v0.1` tag. The
[canonical repository state](.relay/STATE.md) owns the closed checkpoint and scope.
The historical `v0.1-design` tag remains fixed; [R-002](.relay/RECORDS.md#r-002--native-a-b-acceptance-evidence)
preserves the initial native A failure, and accepted
[R-003](.relay/RECORDS.md#r-003--bounded-retrieval-remediation-evidence) owns the final
post-remediation A/B results.

The current development target is a v0.2 review candidate for bounded workspace
integrity checks, checkpoint read-back, coordinated writes, explicit copy and
handoff boundaries, and Reader task isolation. It retains the canonical object model
and the private forensic snapshot boundary. New mechanical and native conformance results are recorded
separately in [validation](docs/validation.md); the historical v0.1 pass does not
establish a v0.2 pass or authorize a new release.
