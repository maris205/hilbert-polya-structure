# P25 code status — Rounds 2 through 8 executed

`round2_three_disk_ledger.py` performs four separated operations:

1. exact enumeration of primitive oriented cyclic words through length 12;
2. center-polygon proxy construction, always labeled `MODELING_CHOICE`;
3. actual reflection-orbit solution using variational BFGS plus an independent
   least-squares stationarity solve, visibility and residual checks;
4. paraxial monodromy/half-density calculation and deterministic target-free
   neighboring, shuffle, random, and composite controls.

The monodromy product is evaluated at 80 decimal digits and compared with a
separate binary64 product.  The high-precision rebuild protects the unit
determinant check from cancellation on long unstable words; only the
finite-difference return map counts as an independent stability calculation.

Dependencies recorded by the receipt are Python 3, NumPy 2.4.4, and SciPy
1.16.1.  Commands:

```bash
python3 code/test_round2_three_disk_ledger.py -v
python3 code/round2_three_disk_ledger.py
python3 code/round2_three_disk_ledger.py --verify-existing
```

The second full command regenerates all 2,241 rows and requires an exact
byte-for-byte match.  No prime or zero data are read.

Round 3 adds `round3_return_map_validation.py`.  It does not import or rebuild
the paraxial factor product.  It refines the periodic point against a 100-digit
physical ray-intersection/reflection map and forms direct Jacobians at three
frozen finite-difference scales.  A geometric specular-stationarity fallback is
used when direct fixed-point Newton raises or fails; Round 4 does not identify
a unique failure cause because the frozen implementation catches a broad
exception class.  The reported stability still comes from the direct ray map.

```bash
python3 code/test_round3_return_map_validation.py -v
python3 code/round3_return_map_validation.py
python3 code/round3_return_map_validation.py --verify-existing
```

The Round-3 result is 2,241/2,241 numerically certified direct checks.  This
closes the finite-cutoff numerical validation gap but does not promote the
aggregate half-density beyond `NUMERICAL_OBSERVATION`.

Round 4 adds `round4_conditioning_audit.py`.  It does not solve orbits.  It
freezes the Round-3 ledger by SHA-256, emits length-stratified and fallback-only
tables, checks every frozen numerical acceptance threshold, and uses Python's
AST to audit the target-dependency boundary of ten direct-map/refinement
functions.  Its eight tests and two-build replay run with only the standard
library:

```bash
./experiments/reproduce_round4.sh
```

The static audit establishes an implementation property only.  It is not a
proof of causal conditioning or sampling unbiasedness.

Round 5 adds `round5_universal_half_density.py`.  It proves and replays the
generic `2 x 2` symplectic hyperbolic stability factorization on all 2,241
owners and repetitions `r=1,2,3`, preserving the physical eigenvalue sign.
`test_round5_universal_half_density.py` supplies ten tests for input hashes,
owner/repetition separation, both sign branches, the determinant identity,
monotone repetition correction, deterministic bytes, and Route firewalls.

```bash
./experiments/reproduce_round5.sh
```

Round 6 adds `round6_symbolic_zeta_calibrator.py`.  It compares the frozen
primitive Euler product, adjacency-trace exponential, and reciprocal exact
`3 x 3` determinant through degree 12 for unweighted and collision-parity
conventions, using standard-library integer/rational arithmetic only.

```bash
./experiments/reproduce_round6.sh
```

Ten tests cover hashes, determinants, traces, Möbius counts, oriented owners,
both coefficient identities, typed Route boundaries, source bindings, and byte
determinism.  No physical lengths, stabilities, resonances, primes, or zeros
are consumed.

Round 7 adds `round7_q_symbolic_family.py`.  It proves the closed formulas for
the entire integer family `q>=2` and executes an exact regression grid
`q=2,...,8`, degree at most 12.  Twelve tests independently check direct
integer matrix traces, Möbius counts, Bareiss determinant values, three formal-
series constructions, phase substitution, source bindings, deterministic
rendering, and Route firewalls.

```bash
./experiments/reproduce_round7.sh
```

The default command verifies checked-in canonical bytes.  Use the explicit
`--refresh` argument only when intentionally rebuilding those artifacts.

Round 8 adds `round8_roof_nontransfer.py`.  It source-locks the complete
Round-2 physical ledger, checks the exact symmetric period-two and period-three
length formulas at all three geometries, and emits a 2,241-row scalar-clock
replay.  The theorem is the exact periodic-average argument in the note; the
finite rows are not used to infer cohomology.

```bash
./experiments/reproduce_round8.sh
```

Twelve tests cover freeze/input hashes, exact geometric identities, the
minimax bound, all 2,241 owner rows, the `3/744` per-geometry scalar split,
clock-owner firewalls, source bindings, receipts, and byte determinism.
