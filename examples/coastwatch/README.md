# Coastwatch fixture

Coastwatch is a high-fidelity synthetic research workspace used to review Project
Relay v0.1. It represents a post-migration sensor-normalization project with remote
data, lineage, a service, stale job evidence, an inaccessible historical chat, and a
human cutover decision.

Everything here is fictional. Domains under `.example` are reserved and do not
resolve; IDs, people, commits, paths, logs, and timestamps are invented. The commands
show what exact project procedures look like but are not executable in this
repository. No motivating-project information is present.

To exercise bootstrap, start a fresh native-agent session in this directory without
explaining the project. The agent should read `AGENTS.md` or `CLAUDE.md`, then recover
the state from `.relay/` and refuse to call either job R-007 or R-008 “running.”

