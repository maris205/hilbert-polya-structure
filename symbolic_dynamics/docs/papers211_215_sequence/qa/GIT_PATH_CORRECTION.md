# Git path correction

2026-09-11. User explicitly requires this stream under `symbolic_dynamics/`.
Earlier root-path synchronization receipts retain historical meaning only.

P211--P215 migration commit: `5b3d97afe873d566a806c286232a83e1164aa532`.
Remote main was queried after push and matched this commit. The seven old
root paths are absent from its tree. The new paths contain 20,486 files:
19,453 byte-identical relocations and 1,033 previously ignored build evidence
files (7,034,438 bytes). Earlier claims that all evidence was tracked were
incomplete: worktree equality alone did not detect ignored files.

The subsequent historical migration moves P187--P210, four batch directories
and `docs/research_state/` by exactly 38,094 R100 prefix renames. No destination
conflicts were present. Shared `docs/agent_workflows/` remains at repository
root because it covers other research streams as well.

No scientific result, frozen evidence, failure or review is rewritten.
Root copies are removed from the latest Git tree only after their destination
copies are checked. Previous commits remain recoverable; no history rewrite.
Workspace data stays at `/root/autodl-tmp/symbolic_dynamics`. Git destinations
now add `symbolic_dynamics/` to workspace-relative research paths. Historical
absolute paths in raw evidence remain archival and are not rewritten.

This receipt is included after the first migration; it does not claim its
own containing commit hash. The batch remains complete and paused with
`HOLD_EXTERNAL` unchanged.
