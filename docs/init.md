# INIT protocol

INIT adds Relay to a new project or to an existing project whose material state is
already explicit in the folder and in explicitly supplied resource locators. It is
not a shortcut for latent native-agent context.

## Entry gate

Use INIT only when all are true:

- a fresh agent can inspect the project without relying on prior chat or auto-memory;
- no material decision or exact procedure exists only in conversation;
- important remote hosts, datasets, services, jobs, and tools are either irrelevant
  or already explicitly supplied;
- inaccessible history is not needed to continue safely.

If any answer is “no” or “unknown,” use [MIGRATE](migrate.md). A project may look
self-contained while a deployment, dataset lineage, or running job lives elsewhere;
ask that question explicitly.

## Procedure

### 1. Establish a safe boundary

Inspect the project root, current branch, working tree, and existing native agent
files. Do not overwrite `AGENTS.md`, `CLAUDE.md`, `.gitignore`, or an existing
`.relay/` directory blindly.

If the folder is not a Git repository, initialize it:

```sh
git init
```

Existing uncommitted work belongs to the project. Preserve and describe it in the
initial state when relevant; do not discard or absorb unrelated changes silently.

### 2. Install the neutral workspace

Copy the template's `.relay/` directory into the project root:

```sh
cp -R /path/to/project-relay/template/.relay .
```

Then merge the template's ignore patterns into the project's `.gitignore`. Ignore
rules are defense in depth; canonical files still must not contain secret values.

### 3. Install thin adapters

- If `AGENTS.md` does not exist, copy `template/AGENTS.md`.
- If it exists, preserve its project instructions and add a short first-read rule
  pointing to `.relay/START.md` and `.relay/STATE.md`. Move any duplicated live state
  into `.relay/` and replace it with a link.
- If `CLAUDE.md` does not exist, copy the template's one-line `@AGENTS.md` import.
- If it exists, preserve Claude-specific instructions and add `@AGENTS.md` once.
  Do not copy the AGENTS content into it.

The adapters MAY retain truly agent-specific mechanics. Current frontier, decisions,
resources, procedures, and job status MUST remain neutral and canonical under
`.relay/`.

### 4. Populate the snapshot

Replace every unresolved placeholder in `.relay/STATE.md` with:

- one current frontier;
- concrete active work or `none`;
- one next human gate or `none` with a reason;
- links to the few governing decisions needed at bootstrap;
- current blockers/unknowns;
- explicit background execution (`none` unless job records prove otherwise).

Do not put history, long procedures, inventories, or timeless “running” assertions
in the snapshot.

### 5. Externalize the minimum operational set

Create stable-ID records only for what exists:

- accepted and important provisional decisions in `DECISIONS.md`;
- repositories, critical assets and lineage, remote resources, required tools,
  services, real jobs, secret references, and durable unknowns in `RECORDS.md`;
- exact environment/build/test/deploy/reproduce/maintain/recovery procedures in
  `PROCEDURES.md` when they are necessary for safe continuation.

Use `unknown` rather than prose that exceeds the available evidence. Empty sections
are valid. Do not invent a service or job record merely to fill the template.

### 6. Verify from a fresh-reader perspective

Without using the current conversation, answer from the new files:

1. What is the frontier and active work?
2. Which accepted decisions govern it?
3. What is the next human gate?
4. Where is the exact task-relevant procedure or resource?
5. Is any job currently running, and what independent evidence supports that tense?

If the files cannot answer the first four, fix the owning records. If question 5
cannot be live-verified, record `unknown` or “last observed,” never “running.”

### 7. Checkpoint and commit

Ensure the owning files contain the source state, records, unknowns, and next gate.
That durable write-back is the checkpoint. Review the diff, then create one coherent
commit when authorized:

```sh
git add AGENTS.md CLAUDE.md .relay .gitignore
git diff --cached
git commit -m "chore: initialize Project Relay workspace"
```

Adjust the path list so it does not stage unrelated existing work.

## INIT completion criteria

INIT passes when a fresh Codex and a fresh Claude Code session both discover the
same neutral state, the required operational records have checkable provenance, no
adapter contains a second copy of live truth, and the Git diff is public/private-safe
for the project's intended visibility.
