# Experiment plan

## Frozen model

Use `M=product_i S^{d_i}` with the unit round metrics, `d_i>=1`, and
`g(0)=direct_sum_i a_i g_i`, `a_i>0`.  The physical clock is the time in
`partial_t g=-2 Ric(g)`.  The constant-volume clock is frozen by

`c(t)=(V(0)/V(t))^(2/n)`, `hat g=cg`, and `d tau/dt=c`.

No alternative clock, curvature convention, or post-hoc normalization is
allowed.

## Analytic obligations

- Derive `a_i(t)=a_i-2(d_i-1)t` from product curvature.
- Treat `d_i=1` as an infinite collapse clock, not by division by zero.
- Let `I` contain every minimizer of the finite factor clocks and retain its
  total dimension `D`.
- Prove the exact scalar, Riemann-norm, volume, and diameter laws and their
  Type-I residues.
- Prove the pointed blowup
  `product_{i in I} S^{d_i}(-2(d_i-1)s) x R^{n-D}`.
- Derive the volume-normalized equation from constant scaling and the time
  change.  Prove the endpoint integral diverges exactly when `D=n`.
- Close one factor, all-flat torus, mixed flat/curved products, unique clocks,
  tied clocks, and common scale/permutation covariance.

## Executable matrix

The deterministic producer covers 14 named families, including two all-flat
families, five full-collapse Einstein families, and seven partial-collapse
families.  It emits:

- 14 exact case classifications;
- 68 unnormalized flow cells;
- 66 constant-volume cells with independently integrated normalized time;
- 12 first-singularity ledgers;
- 36 near-singularity cells;
- 14 permutation/common-scale controls;
- 8 explicit boundary rows.

The independent checker must reconstruct every formula without importing the
producer.  SymPy checks the ODE, logarithmic volume identities, normalized
equation, Einstein face, tied residue, and flat-factor boundary.  Replay must
be byte-identical.  Fifty-one repaired-hash semantic mutations plus one stale
hash control must all fail; fail-closed schema, truncated-vector,
wrong-positive endpoint-tail, required-key-drop, and duplicate/drop-replace
attacks cover every row family.

## Release gates

Three conditional manuscript rounds must be substantively different.  Each
round is built twice in a fresh directory with fixed epoch `1788220800`.
Round 2 is final.  The release gate checks warnings, fonts, extracted text,
visual audit receipt, exact 27-payload/28-physical-file closure, and every
source/evaluator/scope lock.
