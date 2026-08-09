# Programme roadmap

| Stage | Working paper | Objective | Promotion gate |
|---:|---|---|---|
| 01 | Clock-preserving Hénon operators | construct a fixed self-adjoint family with exact counting clock and nontrivial operator structure | Q/W/\(S_{\rm op}\) |
| 02 | Certified local relative wave trace | make a nonzero-time orbit term rigorous and quantitative on an explicit energy band | local complement complete; phase and global covers remain |
| 03 | Endogenous prime trace | obtain rational-prime periods \(r\log p\) and correct signed weights without importing prime data | \(P_0\) |
| 04 | Explicit-formula bridge | connect an already certified prime carrier to a signed explicit-formula object | Paper 03 must pass |
| 05 | Hilbert--Pólya synthesis | test whether one fixed self-adjoint operator closes Q--Z coherently | all preceding gates |

The roadmap is conditional, not a promise that every route survives.  A dead
candidate is a useful result when the violated gate is explicit.

## Immediate Paper 02 promotion path

The local-complement programme has completed both prospective stages.
`R401-VAL-L2-S0` first accepted the six-tree implementation smoke on S000,
S025, and S050.  `R401-VAL-L2-A1` then closed all 102 canonical trees on the
51 slabs at 128 and 256 bits: 52,790 nodes were archived, 158,782 independent
checks passed with zero failures, and the 19-role release was sealed under
`PASS_LOCAL_COMPLEMENT_ALL_SLABS`.

`R401-VAL-L3-S0-COMPOSITE-DRAFT` now records representative implementation
feasibility for the next phase-tube bridge.  The exact
`S000/S025/S050 x 128/256` matrix passes both independently checked
components and the separate six-cell composite under
`DRAFT_NON_LICENSING / PASS_IMPLEMENTATION_SMOKE`.  This is not an A4.16
theorem and does not cover the other 48 slabs.

The immediate Paper 02 path is now: independent pre-freeze review,
prospectively frozen 51-slab by two-precision A4.16 production, and then the
separate global tube-routing complement.  The independently event-projected
determinant/Taylor-width gate remains open after those steps.  Neither A4.15
nor the representative A4.16 smoke quantitatively promotes
\(\delta_{\rm tr}\), and neither crosses the arithmetic-prime gate.
