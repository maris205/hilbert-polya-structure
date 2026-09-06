# Supplementary exact verification

2026-09-06. Executed from the repository root:

```text
python henon_dynamics/continuation_c409_c413_round2/nonlinear_geometry/verify_trace_contract.py
```

Result: exit code 0.

```text
PASS symbolic inverse, invariant, three infinite itineraries, signed zero-neighbour obstruction, rational 2-cycle
PASS all 125 states in [-2,2]^3: 49 periodic, 76 exit; forward/backward exit histograms=[{1: 36, 2: 8, 3: 8, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4}, {1: 36, 2: 8, 3: 8, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4}]
PASS full partial-permutation graph [-20,20]^3: cycle counts={1: 2, 3: 1, 4: 20, 6: 20, 12: 20}, 445 periodic points
PASS exact source return formulas for integer levels -10 through 200 and ordinary times 1 through 60
ALL SUPPLEMENTARY CHECKS PASS; global completeness is proved in PROOF_PACKAGE.md, not inferred from these finite tests
```

The symbolic checks use exact polynomials and rational numbers. The finite
graph extraction constructs a partial permutation on all 68,921 states of
the cube; it does not label a long unclosed trajectory as nonperiodic merely
because a guessed time cutoff expires. The graph only classifies cycles
wholly contained in that specified cube.

The 125-state test separately iterates every one of the 76 noncycle states
both forward and backward until it leaves the small cube. The maximum observed
first-exit time is 9 in each direction. The author proof needs only the
independently established finite-set bound 125; it does not rely on the
observed stronger value 9.

The layer return checks use levels -10 through 200 and times 1 through 60.
They do not assert that those finite ranges establish the universally
quantified return law; that law is proved from the orbit classification.

The preceding exploratory `scout_checks.py` run also completely extracted
cycles contained in [-12,12]^3, and all integral cycles for each fixed
integer parameter -12 through 400 in the odd cubic Hénon family. Those are
explicitly finite scouts, not research contracts or a substitute for a full
cubic-family theorem. No sealed checks or unrelated experiments were rerun.
