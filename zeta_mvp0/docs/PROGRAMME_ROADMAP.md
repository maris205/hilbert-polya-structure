# Programme roadmap

| Stage | Working paper | Objective | Promotion gate |
|---:|---|---|---|
| 01 | Clock-preserving Hénon operators | construct a fixed self-adjoint family with exact counting clock and nontrivial operator structure | Q/W/\(S_{\rm op}\) |
| 02 | Certified local relative wave trace | make a nonzero-time orbit term rigorous and quantitative on an explicit energy band | complete local complement, phase and global covers |
| 03 | Endogenous prime trace | obtain rational-prime periods \(r\log p\) and correct signed weights without importing prime data | \(P_0\) |
| 04 | Explicit-formula bridge | connect an already certified prime carrier to a signed explicit-formula object | Paper 03 must pass |
| 05 | Hilbert--Pólya synthesis | test whether one fixed self-adjoint operator closes Q--Z coherently | all preceding gates |

The roadmap is conditional, not a promise that every route survives.  A dead
candidate is a useful result when the violated gate is explicit.

## Immediate Paper 02 promotion path

The next local-complement theorem is deliberately split into two stages.
`R401-VAL-L2-S0` is a six-tree representative implementation smoke on slabs
S000, S025, and S050 at 128 and 256 bits.  It is now accepted as
`PASS_IMPLEMENTATION_SMOKE`: all 3,016 evaluated nodes and 1,532 leaves are
accounted for, and 89,962 independent checks pass with zero failures.  The
prospective all-slab stage
requires 102 canonical trees, transactional crash-safe evidence, exact
per-tree budgets, deterministic fair scheduling, and an independent checker
that reconstructs the archive from the frozen plan.  Its design is not yet
frozen and therefore cannot authorize production on the held-out slabs.

Even a complete all-slab local complement would leave the phase/flow-box
cover, the global return cover, and an independently event-projected
determinant/Taylor-width gate open before any quantitative promotion of
\(\delta_{\rm tr}\).
