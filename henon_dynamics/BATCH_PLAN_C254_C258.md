# Route-A batch plan C254--C258

Baseline: b89544f1f7b1043f4158dfdf9db77787b332f146

Evaluator: flow_systems/skills/route-a-evaluator.md v0.2.0, SHA-256
6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c

Common scope: NO_BAD_EULER_OR_ROOT_NUMBER

Fixed build epoch: 1788048000

## Independent theorem contracts

| ID | owner | theorem-scale advance | strict tuple |
|---|---|---|---|
| C254 | Monod single-species chemostat | exact total relaxation; washout/critical/survival global atlas; transcritical spectrum; invariant-leaf implicit law and critical rate | (A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL) |
| C255 | Euler--Poincare--Suslov rigid body | constrained energy reduction; both explicit heteroclinics; clean reconstructed rotations; singular Poisson density; all principal and zero-energy faces | (A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT) |
| C256 | KdV traveling-wave reduction | all bounded three-root cnoidal waves; exact period and first two moments; Galilean covariance; soliton, harmonic, and constant root-collision faces | (A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT) |
| C257 | Newton maps for `z^2-a^2`, `a != 0` | global Cayley conjugacy; both basins and Julia boundary; convergence rate; full periodic/preperiodic atlas; multiplier, invariant measure, entropy, and source zeta | (A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT) |
| C258 | mixed congruential affine map | all-modulus Hull--Dobell criterion; local valuation and CRT proof; parameter count; primitive/fixed/zeta/Koopman closure | (A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION) |

The first four overall verdicts are ROUTE_A_REJECTED.  C258 is
ROUTE_A_EXPLORATORY because finite-ring prime-power structure is intrinsic,
but it still fails every target determinant and analytic-structure gate.
Route B is false for all five.

## Package gates

Each paper must carry:

1. a frozen source object, clock, normalization, determinant convention, and
   forbidden-data boundary;
2. a self-contained theorem and explicit singular or degenerate faces;
3. a deterministic producer and a genuinely independent checker;
4. symbolic or exact-algebra cross-check, byte replay, and at least twenty
   repaired-hash hostile mutations;
5. two substantive manuscript revisions retained as three distinct PDFs;
6. two fresh fixed-epoch builds per revision, embedded fonts, extracted-text
   checks, and visual inspection;
7. a content-addressed 27-payload release ledger plus one self-excluded
   manifest;
8. an evaluator YAML that does not combine coordinates across candidates.

No package may introduce target prime or zero tables, arithmetic local data,
Euler factors, root numbers, automorphy, a target divisor/counting law or
functional equation, a Hilbert--Polya operator, or Route-B input.
