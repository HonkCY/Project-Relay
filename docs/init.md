# INIT protocol

INIT adds Relay to a new project or to an existing project whose material state is
already explicit in the folder and in explicitly supplied resource locators. It is
not a shortcut for latent native-agent context.

## Entry gate

INIT is a source-mutating lifecycle for an explicitly authorized Maintainer. A
Reader request, a missing Relay file, or a source snapshot without Git is not INIT
authorization. Report the gap and continue only safe permitted work; save Reader
findings in its separate output, not by initializing Git or installing source
files. The [session access contract](protocol.md#session-access-contract) also
applies to the steps below.

Use INIT only when all are true:

- a fresh agent can inspect the project without relying on prior chat or auto-memory;
- no material decision or exact procedure exists only in conversation;
- important remote hosts, datasets, services, jobs, and tools are either irrelevant
  or already explicitly supplied;
- inaccessible history is not needed to continue safely.

If any answer is “no” or “unknown,” the authorized setup workflow requires
[MIGRATE](migrate.md) rather than INIT; obtain its scoped authorization before
inventory or capture. A project may look self-contained while a deployment, dataset
lineage, or running job lives elsewhere;
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

Identify the intended canonical workspace and any known mirrors or backups before
writing. Use existing repository record fields in step 5: safe locator, role,
readers/writers, observed revision, recheck rule, and risks/limitations. A mirror
may use role `derived` and a backup `archive`; neither becomes an authorized writer
merely by receiving files. Coordinate one writer for this canonical working copy;
parallel worktrees require an explicit integration order before canonical writes.

If the workspace is known to use file synchronization, inspect only task-relevant
signs of incomplete delivery, conflicts, or competing writes. Resolve those before
affected writes; do not infer safety from a sync icon or launch an automatic
sync-detection service. Record what is known and any unresolved boundary limitation.

### 2. Install the neutral workspace

If `.relay/` is absent, copy the template directory with an explicit no-clobber
guard:

```sh
test ! -e .relay || { printf '%s\n' '.relay already exists; stop for reviewed merge' >&2; exit 1; }
cp -R /path/to/project-relay/template/.relay .
```

If `.relay/` already exists, do not run the copy command. Treat this as an upgrade:
compare protocol versions and merge individual missing/schema changes only after
reviewing the existing canonical owners and dirty Git state. See the
[v0.2 upgrade guide](upgrade-v0.2.md) for the bounded integrity changes.

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

Record the workspace/copy roles established in step 1 in the relevant repository
record, including who may write and how a receiving copy is checked. An off-host
backup SHOULD exist where practical; when absent or unverified, state the resulting
recovery limitation. A configured remote alone is not evidence that a backup was
received. Keep backup or mirror observations in the same evidence envelope as other
repository facts; no additional registry is needed.

### 6. Verify from a fresh-session perspective

Without using the current conversation, answer from the new files:

1. What is the frontier and active work?
2. Which accepted decisions govern it?
3. What is the next human gate?
4. Where is the exact task-relevant procedure or resource?
5. Is any job queued/running or any service running/healthy, and what independent,
   fresh evidence supports each tense?

If the files cannot answer the first four, fix the owning records. If question 5
cannot be live-verified, record `unknown` or “last observed” with freshness, never a
timeless `running`/`healthy` claim.

Confirm the necessary snapshot meaning, not exact heading text. An explicit `none`
or `unknown` is meaningful; an empty file, missing background safety statement, or
unresolved placeholder is not an equivalent answer. If the read tool paginates or
truncates output, finish that bounded read before judging the file incomplete.
Check only owners needed for these questions. A missing or ambiguous stable-ID
owner must be resolved using the current workspace map and authority rules before
the affected operation; copies in other workspaces do not create duplicate owners.

### 7. Checkpoint and commit

Apply [CHECKPOINT / WRITE-BACK](protocol.md#checkpoint--write-back): save the owning
records first and the snapshot if changed, then reopen only the changed sections
and confirm their expected values at the intended canonical paths. Do not declare
the checkpoint complete when the write reports success but read-back is missing,
different, or inaccessible. Read-back confirms locally observed content at that
time; it is not a guarantee of physical persistence or completed synchronization.
Review the diff, then create one coherent commit when authorized:

```sh
git add AGENTS.md CLAUDE.md .relay .gitignore
git diff --cached
git commit -m "chore: initialize Project Relay workspace"
```

Adjust the path list so it does not stage unrelated existing work.

For cross-host handoff, transfer the named coherent commit through Git transport
or a bundle and check that the receiver has that commit and the required canonical
files before reporting handoff complete. Inspect receiving dirty state too; preserve
it and resolve any relevant overlay or conflict. Uncommitted source changes are not
included by that transfer, although they remain valid input to local RECOVER.

## INIT completion criteria

INIT passes when a fresh Codex and a fresh Claude Code session both discover the
same neutral state, the required operational records have checkable provenance, no
adapter contains a second copy of live truth, and the Git diff is public/private-safe
for the project's intended visibility.
