# Source provenance

## Pinned source

| Field | Value |
|---|---|
| Source repository | `git@github.com:maris205/prime_dynamics_theory.git` |
| Source local clone | `/root/autodl-tmp/prime_dynamics_theory` |
| Source commit | `02d51d372e9c95ffc2ed36727829363a32cec030` |
| Import date | 2026-09-13 |
| Target location | `zeta_mvp0/{papers,PRIME_DYNAMICS_RH_*.md,rh_import_metadata,readme.md}` |
| Copy mode | source-tracked-file whitelist; no source files were modified |

The source and target worktrees were clean at the time the selection was
locked.  The source commit, rather than a mutable working-tree timestamp, is
the authoritative identity of this import.

## Root-document selection

| Imported target file | Source | Selection | SHA-256 of selected bytes |
|---|---|---|---|
| `PRIME_DYNAMICS_RH_HANDOFF.md` | `RH_HANDOFF.md` | complete file | `83eb6c07e1523946b30531884f147d5a71b08ad47271f5fb8aa4071515eed90a` |
| `PRIME_DYNAMICS_RH_README_SECTION.md` | `README.md` | lines 1--9 | `1da280fee32eddb5a1e79eccdbbb5de5c1944b6321e1e42666ca5db58fa2f7fc` |
| `PRIME_DYNAMICS_RH_WORKFLOW.md` | `AGENTS.md` | lines 55--174 | `c9d8795376f7dc4a3977f17347ff4854e335b7e5a553f43f66aa3c1564954b79` |

The source-root `AUTO_REVIEW.md`, `DERIVATION_PACKAGE.md`, `IDEA_REPORT.md`,
`PROOF_PACKAGE.md`, `TPC_COMPASS.md`, `TPC_HANDOFF.md`, and `codex_prompt.md`
are excluded because they are TPC-specific or environment/workflow material,
not RH corpus documents.  The source `AGENTS.md` is not installed under its
active filename: only its RH workflow segment is retained as a historical
reference, and the target repository's own `AGENTS.md` remains authoritative.

## Historical-path caveat

Some imported records retain historical absolute paths, including references
to `/root/math/prime_dynamics_theory`.  They are evidence-path strings from
the source snapshot, not instructions to rewrite history or claims that the
old path exists here.  Use
[PRIME_DYNAMICS_RH_REPRODUCE.md](PRIME_DYNAMICS_RH_REPRODUCE.md) for the current
comparison location.
