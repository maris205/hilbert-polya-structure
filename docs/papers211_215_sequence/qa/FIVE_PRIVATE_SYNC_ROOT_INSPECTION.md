# Root acceptance - completed P211-P215 private synchronization

2026-09-11 UTC. Status:
`ROOT_ACCEPTED_EXACT_FIVE_COMPLETE_AND_SCOPED_PRIVATE_SYNC`.
The separate [scientific acceptance](../FINAL_QA_REPORT.md) remains unchanged:
exactly P211--P215 are complete, with zero current open findings. No new batch,
theorem, review, scientific run, build, or page view was started for this sync.

## Actual commit and selected scope

The first normal private push produced commit
`06c2c90ba119fb657762e56b43368ba7d578d014`, sole parent
`9812a4a3718354507b78c5d5b8baefe2ecdfbb87`, and tree
`b3bd0ddd0c051e2c204abc54f0f1098272aab610`. The pushed commit contains only
these seven approved path groups:

- `SYMBOLIC_DYNAMICS_STATE.md`
- `docs/papers211_215_sequence/`
- `papers/211-kernel-image-projection-feedback/`
- `papers/212-closed-pointer-orbits/`
- `papers/213-receiver-limited-cyclic-transfer/`
- `papers/214-nilpotent-bilinear-clock/`
- `papers/215-prefix-drawdown-clock/`

The cached-path guard found zero paths outside that scope. The commit changes
18,627 files: 18,625 additions, two modifications, and zero deletions, with
9,586,026 inserted lines and 13 deleted lines. The largest changed file is
33,482,356 bytes, below GitHub's 100,000,000-byte single-file limit. The large
scope is intentional: it retains frozen rounds, complete run evidence, and all
failed/HOLD/rejected evidence rather than pruning history.

## Remote and source checks

The isolated synchronization repository was created from remote `main` at
`9812a4a3718354507b78c5d5b8baefe2ecdfbb87`. Remote advancement after the old
`7d43cb32` checkpoint affected `henon_dynamics/` only and did not overlap this
selection. Before commit, checksum-based `rsync -rcn --delete` comparisons
reported no difference for the copied batch and five paper directories.

Immediately before push, `git fetch origin main` still returned `9812a4a3`;
that ref was an ancestor of the new commit and the normal push was a
fast-forward. A fresh read-only `git ls-remote` after push returned exactly
`06c2c90ba119fb657762e56b43368ba7d578d014`, and local versus `origin/main`
ahead/behind was 0/0. No force push, history rewrite, broad worktree copy, or
out-of-scope staging occurred.

The historical accepted local bare repository remains at `7d43cb32` and was
not relabelled as current or modified during this sync. The authoritative
verified destination for this milestone is the configured private GitHub
`origin/main` above.

## Receipt boundary and pause

This receipt and the final lifecycle index refresh are deliberately outside
the commit they describe. They are synchronized by one subsequent scoped
commit; this file does not make a circular claim about that commit's hash.
The pre-refresh central bytes remain pinned by SHA-256 and Git blob identity in
[the preservation note](control_before_private_sync_complete01/README.md).

All five papers remain `OWNER_AMBER / HOLD_EXTERNAL`. No public release,
external manuscript upload, submission, publication, or specialist contact
occurred. The requested batch is closed and the stream pauses here; no next
round has been opened.
