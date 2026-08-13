# Exact gate protocol

## Frozen input

The source H6 paper, the prior-work and related-program registries, and the
Route-A evaluator are locked by SHA-256 inside the certificate. The
mathematical object is

\[
\mathcal U_H=\mathcal F_{\mathbb A}\mathcal M_{2q^3-q}
\]

and the fixed-domain range pair is

\[
R_0=\overline{E\mathcal F(\mathcal S_0)},\qquad
R_H=\overline{E\mathcal F(\mathcal M_{P_6}\mathcal S_0)}.
\]

## Ten checker gates

1. G0_SCHEMA_HASH: exact schema, canonical payload hash, exact payload key
   set, and type-strict structure.
2. G1_HENON_OBJECT: source hashes and the H6 symplectic/unitary object.
3. G2_GLOBAL_ADDITIVE_CHARACTER: exact replay of every rational phase and
   local fractional part on the frozen grid.
4. G3_CONSTANT_GAUGE: exact global product-formula cancellation.
5. G4_SPHERICAL_VACUUM: finite-prime registry and the all-prime
   integral-polynomial theorem.
6. G5_THETA_AND_RANGE: theta stabilizer and adapted mother-range identity.
7. G6_RAW_PRODUCT_NO_GO: local degree and interior-zero-accumulation
   obstruction.
8. G7_LOCAL_DILATION_NONCOMPACTNESS: exact cubic sum, Haar normalization,
   matrix coefficient, norm-defect ledgers, and direct cyclotomic controls.
9. G8_STATIC_RANGE_AND_SCALING_COVARIANCE: both boundary functionals, common
   subspace, static quotient/projection bounds, dilation law, infinite
   pre-Poisson boundary orbit, and the exact fixed-scale Poisson defect mode.
10. G9_ROUTE_AND_SCOPE: conservative Route-A tuple, stop/go decisions, and
    non-claim firewall.

All schema comparisons are recursive and type-strict. A semantic rejection
is FAIL; an unexpected checker exception is ERROR, and both exit nonzero.

## Mathematical and computational boundary

The rational grid is a replay of the product formula, not a finite proof of
the all-rational theorem. The local rows replay consequences of the exact
recurrence; they do not infer it numerically. The static range theorem is
linear algebra on boundary functionals. The Poisson-defect gate is an exact
identity, but it does not assert collapse of the infinite coefficient orbit.
No scattering matrix or determinant value is hard-coded.
