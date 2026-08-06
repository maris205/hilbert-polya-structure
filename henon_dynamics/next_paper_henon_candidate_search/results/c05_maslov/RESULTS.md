# HCS-C05 Maslov/action/instability pilot

## Frozen object

- Map: `H_6(q,p) = (1 - 6 q^2 - p, q)` on the certified local four-state survivor.
- Input: `henon_instability_roof_zeta/results/catalog_robustness.json` (`sha256=37fefa481f1b5d26acfe87f4b5a33dafe75f24b56d625bbda102f12fffc4d08e`).
- Primitive catalogue: 2170 cycles, complete only for that local survivor through period 20.
- Cutoffs: [8, 12, 16, 20]; `s=[0.0, 0.5]`, `theta=[0.0, 1.0]`.
- Fixed control seeds: [20260805, 20260806, 20260807].
- No arithmetic target tables were read.

## Phase convention and its hard boundary

The Morse/Maslov candidate is the negative inertia of the cyclic Hessian of

`sum_i [q_i q_(i+1) - q_i + 2 q_i^3]`.

The Fourier branch is frozen as `sqrt(i)=exp(i*pi/4)`, hence the stationary-phase character is `(-i)^mu`. This ledger is reproducible under the frozen convention. It is **not** an absolute phase selected by classical Hénon dynamics: `S -> S+C` leaves the map unchanged but sends `A_p -> A_p+n_p C`, equivalently `z -> z exp(i theta C)`. A global quantum-kernel phase has the same effect. Fixed-`z` root angles therefore fail the intrinsicness gate.

The explicit coefficient-rotation audit for `C=0.37`, `theta=1` agrees to 2.089e-17. A closed coboundary `f(Q)-f(q)` cancels on every periodic orbit, but the additive constant does not.

## Exact-structure audit

- Reversal partners found: 2170/2170; self-reversing: 464.
- Reversal failures: 0.
- Nontrivial repeated-orbit Hessians rebuilt directly: 70.
- `mu(p^r)=r mu(p)` failures through total period 20: 0 (this equality was tested, never assumed).
- `mu(gamma)=#{i:q_i<0}` failures: 0.
- Certified-coordinate bound failures for `|q_i|>=1/3`: 0; observed minimum `|q_i|=0.37087`.
- Minimum strict sign-diagonal-dominance margin: 2.45044.
- Maslov/orientation parity failures: 0.
- Hill determinant-sign mismatches: 0.
- Near-singular Hessians: 0; minimum absolute Hessian eigenvalue: 3.47214.
- Maximum Hill log-determinant error, including dedicated `n=1,2` formulas: 1.421e-14.
- Maximum action repetition error: 2.665e-15.
- Maximum direct/Chebyshev monodromy trace relative error: 1.650e-15.

Here the repetition statement is stronger than a numerical pattern. On the certified survivor, `|q_i|>=1/3`. For `n>=3` the Hessian has diagonal `12q_i` and two unit off-diagonal entries; for `n=2` the single off-diagonal entry is `2`. Hence every row is strictly sign-diagonally dominant. Scaling the off-diagonal part continuously to zero never crosses a singular matrix, so Sylvester inertia is exactly the number of negative `q_i` symbols. The `n=1` Hessian `2+12q_0` is checked separately and has the same sign conclusion. Therefore

`mu(gamma) = #{i:q_i<0}` and `mu(gamma^r)=r mu(gamma)`

are **proved on this survivor**, and the Maslov character is merely the one-symbol locally constant weight `(-i)^(# negative symbols)`. The direct Hessian ledger independently verifies the proof on every available repetition.

The inherited exact audit also supplies one period-four orbit with coordinates `(-1/sqrt(6),-1/sqrt(6),1/sqrt(6),1/sqrt(6))` and exact action zero. Its stored/direct checks pass, so action cannot serve as a positive roof.

## Finite determinant controls

These are finite formal sections only. Coefficient-prefix agreement is algebraic engineering consistency, and evaluation drift does not establish an infinite Fredholm determinant, A2, continuation, or A3.

| Variant | coefficient-prefix drift | max prescribed-point cutoff drift | median drift | min-root-modulus range at cutoff 20 |
|---|---:|---:|---:|---:|
| constant_roof | 0.000e+00 | 7.389e-11 | 0.000e+00 | [1.50196, 2.66781] |
| maslov_action | 0.000e+00 | 7.389e-11 | 0.000e+00 | [1.50196, 3.73565] |
| orientation_fallback | 0.000e+00 | 2.245e-11 | 0.000e+00 | [1.86873, 4.655] |
| random_phase | 0.000e+00 | 6.518e-06 | 6.167e-11 | [1.71419, 4.09088] |
| shuffled_action | 0.000e+00 | 2.303e-06 | 4.021e-14 | [1.61811, 4.02316] |

On the prespecified `s=0.5, theta=1` slice, maximum evaluation drifts are `constant_roof=7.897e-13`, `maslov_action=4.459e-14`, `orientation_fallback=9.943e-15`, `random_phase=1.999e-09`, `shuffled_action=1.085e-09`. The Maslov/action section beats random-phase and shuffled-action controls, so the geometric cancellation is real at finite order; however, the simpler branch-independent orientation fallback is at least as stable, and the constant-roof control is also highly stable. This does not isolate a C05-specific mechanism.

## Decision

**Hard kill for promotion as an intrinsic absolute-phase RH candidate.** The additive-constant/global-kernel phase is not fixed by the classical map. More strongly, strict sign-diagonal dominance proves that the Maslov character is only a one-symbol locally constant weight and that every repetition phase is the corresponding primitive power. Reversal supplies equality/degeneracy, not a new conjugation or functional-equation mechanism. Although the target-free finite section is substantially more stable than random/shuffled controls, the simpler orientation fallback matches or improves that stability. Thus the result is genuine dynamical cancellation but not a distinct C05 phase mechanism.

Retain the exact local Maslov collapse as `PROVED` and the finite determinant sections as a reusable `NUMERICAL_OBSERVATION`/bookkeeping baseline. The Hessian ledger, Hill identity, reversal pairing, and branch-independent orientation character are valid inputs for a later localized trace theorem. Formal status remains `A1_WEAK`; there is no A2/A3 promotion.

## Controls not run

- No neighboring-parameter catalogue was used: the inherited neighboring catalogues are numerical continuations, not certified complete survivor catalogues.
- No independent arbitrary-precision Hessian implementation was rerun; this pilot inherits the 80-digit coordinates and audits the Hessian identities in float64.
- No direct coefficient-by-coefficient comparison against every inherited scalar determinant artifact was added; `orientation_fallback` is the cheapest parent control used here.

These omissions limit any positive stability claim. They do not weaken the negative C05 decision, which follows exactly from the additive-constant gauge and the local-symbol Maslov collapse.
