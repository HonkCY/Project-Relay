# Bounded prior art

Reviewed 2026-09-03. This pass intentionally covers only mechanisms that changed the
v0.1 design; it is not a market or literature survey.

## Codex project instructions

[Official OpenAI documentation](https://developers.openai.com/codex/guides/agents-md/)
documents that Codex discovers `AGENTS.md` from the project root down toward the
working directory, with more local guidance later in the chain, and imposes a
default combined size limit. Project Relay borrows the reliably discovered root
entrypoint but keeps it tiny. It does not depend on nested overrides, custom fallback
filenames, or a larger instruction budget.

Material effect: root `AGENTS.md` contains only invariant bootstrap/write-back rules
and points to the neutral workspace. Live state never goes into an agent adapter.

## Claude Code project memory

[Anthropic's Claude Code memory documentation](https://code.claude.com/docs/en/memory)
states that Claude Code reads `CLAUDE.md`, not `AGENTS.md`, and explicitly recommends
a `CLAUDE.md` containing `@AGENTS.md` to share instructions without duplication. It
also notes that imports are expanded at launch, project-root instructions are
re-read after compaction, and auto-memory is machine-local agent-written context.

Material effect: `CLAUDE.md` imports only the tiny adapter, not the full Relay corpus.
The portable Git folder remains authoritative; Claude auto-memory is a useful but
non-canonical migration source. A text import is preferred over a symlink for
cross-platform behavior.

## GitHub Spec Kit

[Spec Kit's official integration reference](https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md)
shows a shared repository workflow adapted to many native coding agents, while its
[init reference](https://github.com/github/spec-kit/blob/main/docs/reference/core.md#initialize-a-project)
shows explicit scaffolding and separation of shared infrastructure from agent
integration files.

Material effect: Relay borrows the adapter/shared-core boundary and the idea that an
existing folder can be initialized. It does not borrow the integration CLI, generated
command trees, per-agent workflow packages, managed manifests, or agent-switch
operation. Relay switching must work by opening either native agent against the same
canonical folder, with no controller or regenerated truth.

## Deliberately deferred

Git-backed agent-memory projects and semantic-memory stores were not adopted because
the required v0.1 scenarios are satisfied by Markdown, stable IDs, links, search, and
Git history. The protocol defines a rebuildable optional-index boundary only after a
real retrieval failure is demonstrated.

