# P24 pipeline state

Date: **2026-08-27**

| Item | Status |
|---|---|
| ARS Stage 1 | **IN PROGRESS** |
| Continuous-time object | **FROZEN** — unit-speed geodesic flow on torsion-free level-`(3)` Bianchi manifold |
| Level-`(3)` neatness / torsion-freeness | **PROVED** — self-contained congruence-trace lemma in Stage-1 brief |
| Arithmetic source | **FROZEN** — Gaussian principal congruence group |
| Primary target | **MODELING_CHOICE / FROZEN** — `zeta_{Q(i)}` prime-ideal calibration; no Riemann-`zeta` A0 credit |
| Secondary target | **`[PROVED]` OWNER RULES / `[OPEN]` MAP** — rational primes with split/inert/ramified cases |
| Clock / primitive / repetition | **FROZEN** — arclength / primitive loxodromic class / powers |
| Bold hypothesis | **HEURISTIC** — Hecke/holonomy prime-ideal factorization |
| Finite word-ball ledger | **NUMERICALLY_CERTIFIED** — 22,409 reduced words, 11,481 exact matrices, cutoff `<=5` |
| Exact group checks | **NUMERICALLY_CERTIFIED** — determinant one and `A=I mod 3` for every row |
| Primitive/repetition scope | **`[NUMERICALLY_CERTIFIED]` WITH BOUNDARY** — 10,944 primitive-within-ball candidates and 32 observed exact repetitions; full-group primitivity `[OPEN]` |
| Holonomy shuffle | **`[NUMERICAL_OBSERVATION]`** — 10,944 target-free rows executed; verdict `[OPEN]` |
| Round-3 Schottky ping-pong certificate | **`[PROVED]`** — 8 closed disks, 28 exact separation checks, 8 exact conjugacy identities |
| Round-3 Schottky marked-word ledger | **`[NUMERICALLY_CERTIFIED]`** — 22,409 distinct projective word matrices; 4,148 oriented cyclic classes at cutoff `<=5` |
| Round-3 primitive / repetition split | **`[PROVED]` symbolically / `[NUMERICALLY_CERTIFIED]` artifact** — 4,092 / 56 in the frozen free-group marking |
| Matched-control boundary | **FROZEN** — rank 4, alphabet 8, cutoff 5 only; finite volume, cusps, covolume, lengths, and full-group orbit counts not matched |
| Control arithmetic scope | **NO OWNER** — infinite-volume non-lattice; possible larger arithmetic ambient containment `[OPEN]` |
| Round-3 intrinsic holonomy diagnostic | **`[NUMERICAL_OBSERVATION]`** — score 0.0258111348; shuffled score 0.0234922291; arithmetic verdict `[OPEN]` |
| Round-4 control object | **`[PROVED BY SOURCE CHAIN]`** — `5_2=m015`, orientable finite-volume hyperbolic 3-manifold, one complete torus cusp, non-arithmetic |
| Round-4 source ownership | **VERIFIED** — HIKMOT Theorem 5.1 + rigorous SnapPy positive isometry + Reid arithmetic-knot classification |
| Round-4 geometry match | **IMPROVED** — dimension 3, manifold/torsion-free, finite volume, cusp presence, geodesic flow, arclength clock, complex-length primitive type |
| Round-4 primitive length ledger | **`[NUMERICAL_OBSERVATION]`** — 18 complex-length groups / 31 primitive classes by multiplicity at real length `<3.05` |
| Round-4 independent prefix crosscheck | **`[NUMERICAL_OBSERVATION]`** — 9 classes / 6 groups; multiplicities agree; max residual `2.2944e-31` |
| Round-4 interval status | **NOT RUN** — SageMath unavailable; decimals are not promoted to interval certificates |
| Round-5 pre-result freeze | **PINNED** — common marked-word/canonicalization/root/multiplicity/cutoff/phase contract; SHA-256 `210cff78...a85b7`; no target data |
| Round-5 exact symbolic census | **`[PROVED]` / EXECUTED** — candidate 19,624 raw words -> 2,074 owners; control 372 -> 51; primitive/repetition 2,046/28 and 41/10 |
| Round-5 matrix evidence | **SPLIT** — candidate determinant and level-`(3)` exact; control holonomy numerical at 212 bits with max determinant residual `1.5618e-62` |
| Round-5 phase comparison | **`[NUMERICAL_OBSERVATION]`** — 1,932 versus 39 primitive loxodromic rows; z values `-1.74684` / `-0.811352`; absolute contrast `0.935490` |
| Round-5 same-enumeration status | **ALGORITHM MATCH COMPLETE / PRESENTATION MATCH OPEN** — the word-ball-versus-metric-cutoff type mismatch is closed, but marked positive-generator count 4/alphabet 8 versus 2/alphabet 4 remains |
| Remaining control mismatch | **OPEN** — marked generator count/presentation, exact Bianchi cusp count, covolume, length distribution, and full primitive spectra |
| Full `Gamma((3))` / conjugacy completeness | **OPEN** — elementary generated subgroup word ball only |
| Orbit-to-prime-ideal map | **OPEN** — no arithmetic labels attached |
| Proposal stage | Stage 1 / Route A A0--A1 |
| Formal Route-A tuple | UNASSIGNED |
| Route A A2--A4 | NOT EVALUATED |
| Route-B evaluation | NOT RUN |
| Route-B invocation allowed | `false` |
| Manuscript | NOT STARTED |

Next gate: preregister and execute a same-marked-generator-count Nielsen sensitivity
panel.  Round 5 has removed the direct Bianchi-word-ball versus control-metric-
prefix comparison error, but the current 4-generator and 2-generator
presentations produce sharply different census sizes.  The existing contrast
may not be promoted to an arithmetic kill verdict.  No orbit-to-Gaussian-
prime-ideal claim or A0/A1 verdict is permitted before the marking,
owner/completeness, and robustness obligations close.  A later rational-prime
push-forward must separately preserve the frozen split/inert/ramified rules.
