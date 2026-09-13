# Design decisions and failure-mode challenge

The canonical decision status for this repository lives in
[`/.relay/DECISIONS.md`](../.relay/DECISIONS.md). This document explains rejected
alternatives and tests the design against the brief's named failure modes.

## Why five default files but three objects

The model has three semantic objects: snapshot, record, and procedure. CHECKPOINT is
a lifecycle: promptly write the owning object, review the diff, and commit a coherent
transition when authorized. The default layout uses five files because access/write
patterns differ:

- the stable start map and volatile current snapshot should not churn together;
- decisions need review and supersession, while operational records need frequent
  evidence refresh;
- exact procedures are retrieved differently from entity inventories;
- Git history is already append-only while current truth is edited in place.

Unknowns and blind spots are states/records, not a sixth database. Migration audit
files are a lifecycle dossier, not an everyday canonical object family.

## Rejected alternatives

### One giant agent instruction file

Rejected because it eagerly loads stale detail, duplicates native-agent copies, and
makes current state hard to diff. Adapters point to two small bootstrap files.

### One file per conceptual noun

Rejected because separate host, asset, service, job, MCP, unknown, and handoff stores
create cross-file transaction overhead. Typed records share a registry and scale out
only when size or merge conflict is observed.

### Checkpoint log or full state dump

Rejected because it creates competing truth and duplicates Git history. The saved
owning files are the crash-resistant checkpoint; a coherent commit is the reviewable
transition boundary.

### Conversation export or transcript archive

Rejected as a migration dependency. Exports may be incomplete, unavailable, too
large, sensitive, or semantically ambiguous. The incumbent performs a bounded audit;
material claims are extracted and verified with explicit blind spots.

This does not prohibit an ignored, exact-session local byte snapshot as forensic
insurance when native storage is accessible. Such a snapshot remains optional,
non-canonical, non-portable, and unnecessary for migration or fresh-agent recovery.

### Automatic “latest evidence wins”

Rejected because observed reality and accepted intent are different axes. Fresh
evidence controls descriptive reporting but cannot silently rewrite human decisions.

### Background agent or daemon

Rejected because Relay is a protocol, not an execution harness. Real jobs are tracked
only after some external mechanism supplies a checkable execution ID.

### Required vector or graph store

Rejected until a concrete acceptance failure survives file sharding, stable IDs,
links, and text search. Any future index remains disposable and rebuildable.

## Failure-mode control matrix

| Failure mode | v0.1 control | Review evidence |
| --- | --- | --- |
| Giant instruction file | two short adapter/bootstrap reads; progressive links | adapter line count and bootstrap test |
| Duplicate agent truth | `CLAUDE.md` imports `AGENTS.md`; field ownership rules | adapter diff and conflict test |
| Chat as database | canonical `.relay/` owners; conversation is migration evidence | recovery and migration tests |
| Memory overwrite | authority/provenance axes; accepted supersession rule | conflicting-memory test |
| Imaginary background work | job ID, mechanism, log, time, and live-evidence rule | background-job truth test |
| Migration by hallucination | provisional candidate claims and corroboration | latent-context and false-memory tests |
| Local-folder tunnel vision | required remote/resource/service/job domains | remote operational-state test |
| Copy-everything migration | safe locators plus lineage, no bulk-copy rule | remote dataset fixture |
| Fake 100% completeness | enumerated coverage rows and blind spots, no bare score | inaccessible-source test |
| Meta-work explosion | three objects, materiality trigger, file sharding only on pain | ordinary-work walkthrough |
| External orchestrator creep | explicit boundary; no runtime component | repository inventory |
| Vector-DB reflex | filesystem retrieval first; optional rebuildable index | bootstrap retrieval evidence |

## Reader lifecycle completion — review candidate

The Reader addition addresses a write-back mismatch, not a missing memory layer:
the same source can serve authorized maintenance and several useful read-only
investigations. Reader CHECKPOINT/VERIFY saves observations, original excerpts,
analysis, and recovery progress in a task-exclusive output; the source's D/R/P/STATE
remain the only operational owners. The optional task template is not a copied
project snapshot, shared role board, new record class, or source of authorization.
These are proposed protocol semantics, not newly accepted canonical decisions.

Mode belongs to the session/task. Existing explicitly authorized maintenance is
backwards compatible when mode is omitted, but writable tools cannot elect a
Maintainer. A Reader stays Reader through ordinary continuation, recovery, and
source instructions to write back. An authorization locator records a grant;
editing one's own metadata does not create one. Insufficient permission stops only
dependent operations while safe reading and reporting can continue.

Source access, external query authority, and permitted side effects are separate.
Existing R/P owners carry source/query capabilities and limits; no provider-specific
query subsystem is needed. Reader access can include original remote material, but
does not imply unlimited scans, safe arbitrary database copies, zero locks/logs,
or permission to repair services. A task-scoped read basis includes relevant dirty
or non-Git content where needed; it neither freezes the whole project nor overrides
later stop/revocation instructions.

An exclusive out-of-source output with its own scratch/cache is the supported
default. Branch names and ignore rules alone do not isolate tasks. Reader deliveries
identify their basis and proposed owners; the current authorized Maintainer checks
them against newer canonical work and integrates selectively under existing
materiality, read-back, and acceptance rules. No R record is required merely for
starting or finishing a Reader task.

The boundary is deliberately a protocol, not a sandbox. Mechanical fixture checks,
observed native-agent conformance, and enforceable environment restrictions are
different claims. The [Reader tests](acceptance-tests.md#reader-mode-conformance--review-candidate)
require them to be reported separately; no change here resolves historical native
failures or grants a release pass.
