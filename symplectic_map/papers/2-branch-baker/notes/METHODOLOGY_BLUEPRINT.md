# Methodology Blueprint

## Research paradigm

**Selected:** exact mathematical construction with confirmatory computational
verification.

The question concerns existence, equivalence, periodic-orbit accounting, and
an arithmetic obstruction.  Exact algebra and symbolic dynamics therefore
carry the claims; floating-point experiments are implementation audits rather
than substitutes for proof.

## Method

**Type:** theoretical/computational mixed method.

**Specific method:**

1. derive the PCF Markov graph from the exact post-critical orbit;
2. construct the Parry-affine labeled Markov--baker map from Perron--Frobenius
   left and right eigenvectors;
3. prove branchwise exact symplecticity, almost-everywhere inverse coding, and
   the boundary quotient;
4. enumerate primitive cycles by graph necklaces and M\"obius inversion;
5. derive the unsigned and factor-orientation-weighted determinants without
   combining their conventions;
6. prove the finite-edge locally constant clock obstruction;
7. verify the implementation with exact arithmetic, an independent 100-digit
   parent-factor audit, and sealed floating-point stress splits;
8. run matched controls before assigning any effect to symplecticity.

## Data strategy

**Data type:** candidate-generated mathematical and numerical artifacts only.

No prime list or zero list is an input.  The only inherited scalar parameter
is the exact algebraic \(u_c\), selected by its post-critical orbit before this
candidate was defined.  All random seeds are derived mechanically from a
frozen namespace.  The test split remains inaccessible until the code,
analysis script, thresholds, and validation record are hashed.

### Frozen verification scale

- Candidate ledger: primitive periods 1--20, with the exact predicted count
  vector recorded before implementation.
- Dyadic-baker positive control: primitive periods 1--12.
- Independent parent-factor audit: 100 decimal digits.
- Floating stress test: \(2^{16}\) area-distributed points per split and 256
  one-step forward/inverse checks per point.
- Splits: development, validation, sealed test, with SHA-256-derived 64-bit
  seeds recorded in `experiments/source_lock.json`.

## Analytical framework

### Exact geometry

Let

\[
A=\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix},
\qquad \lambda=\sqrt2,
\qquad r=\ell=\left(\tfrac12,\tfrac12,\tfrac1{\sqrt2}\right).
\]

The labeled rectangles have width \(r_i\), height \(\ell_i\), and area
\(\ell_i r_i\).  An allowed edge \(i\to j\) maps a vertical strip in
\(R_i\) to a horizontal strip in \(R_j\) with frozen derivative

\[
DB_{ij}=\operatorname{diag}
\left(\sigma_{ij}\lambda,\sigma_{ij}/\lambda\right).
\]

Every identity involving the PCF polynomial, eigenvectors, strip tiling,
Jacobian, inverse, graph determinant, and cycle count is checked in exact
arithmetic.

### Orbit and determinant separation

The unsigned topological object is

\[
\zeta_A(z)=\det(I-zA)^{-1}.
\]

The inherited factor-orientation object uses the separately frozen signed
matrix \(W\) and is reported as

\[
D_{\mathrm{or}}(z)=\det(I-zW).
\]

These are not interchangeable.  Absolute values may not be introduced after
the signed result is known.  The parent-core Artin--Mazur zeta is audited as a
boundary quotient rather than silently identified with \(\zeta_A\).
The resulting factor-orientation-weighted parent object is also kept distinct
from the Lefschetz zeta: in the frozen convention they are respectively
\(1-z\) and \(1/(1-z)\).  The latter follows from the fixed-point index on the
contractible interval and is not computed from \(W\).
Likewise, the signs in \(W\) are inherited one-dimensional branch
orientations, not symplectic orientations or Maslov phases.

### Arithmetic gate

For a finite set of locally constant edge lengths \(L=\{\ell_e\}\), every
periodic length belongs to the finite-dimensional rational span of \(L\).
The family \(\{\log p:p\text{ rational prime}\}\) is rationally linearly
independent by unique factorization.  Consequently a finite-edge locally
constant clock cannot contain all prime logarithms exactly.  The specialized
candidate gives the stronger prediction

\[
|\Lambda_u(\gamma)|=2^k
\quad\text{for every primitive period }2k\text{ orbit}.
\]

This multiplier statement and its Euler product apply to the frozen
constant-slope, unquotiented SFT/baker.  They are not claims about the
nonlinear parent's derivative cocycle.

This is an analytic A0 test, not a fit.

## Controls

1. **Dyadic baker positive control:** validates exact cycle generation,
   canonical rotation, inverse mapping, and multiplier calculations.
2. **Folded-tent positive control:** validates simultaneous reversal of stable
   and unstable coordinates on a decreasing factor branch.
3. **Matched dissipative control:** replaces the stable factor by
   \(\rho\sigma_{ij}/\lambda\) at \(\rho=1/2\), preserving future code but
   giving determinant \(\rho\) and a non-surjective image.
4. **Label-erasure control:** projects to the one-sided parent and demonstrates
   the loss of past-branch reconstruction.
5. **Anti-symplectic implementation control:** flips only one coordinate on a
   decreasing branch and must be rejected because its determinant is \(-1\).
6. **All-positive-sign phase null:** preserves \(A\), areas, unsigned cycle
   counts, and symplecticity while removing the parent-orientation weights.

## Validity criteria

| Criterion | Required strategy |
|---|---|
| Construct validity | Keep branch-code preservation, raw-coordinate factorization, symplecticity, and arithmetic relevance as four distinct claims. |
| Internal validity | Derive all thresholds and expected counts before validation; treat discrepancies in exact identities as implementation errors, not adverse data. |
| Reproducibility | Store source lock, manifests, exact JSON artifacts, independent audit outputs, environment record, hashes, and non-overwriting CLI behavior. |
| Numerical reliability | Use exact algebra where possible; label the 100-digit audit as consistency evidence rather than interval certification. |
| Specificity | Require matched dissipative and sign-null controls before attributing any observable to symplecticity or inherited orientation. |
| Scope fidelity | A static isolation test forbids imports, paths, seeds, and sealed results from `1-symp-vs-diss`. |

## Stopping rules

- Failure of an exact PCF, tiling, inverse, or symplectic identity stops
  interpretation until the implementation is repaired.
- More than the single pre-declared periodic boundary collapse invalidates the
  parent-factor claim; the partition may not be retuned.
- Any need for smoothing, variable edge slopes, a non-locally-constant roof,
  a countable tower, or higher dimension terminates this candidate and requires
  a new source lock.
- The parent derivative cocycle may not replace the branch-baker monodromy.
- Signed cancellation may not be undone with absolute values or selective
  orbit deletion.
- A code-only effect reproduced at \(\rho=1/2\) is classified
  `PROVES_TOO_MUCH / SYMBOLIC_ONLY`.
- Even a perfect structural verification does not open prime tables, Riemann
  zeros, Route-A A2, quantization, or Route B.

## Limitations by design

- The candidate is compact and piecewise symplectic but not a globally smooth
  symplectomorphism.
- The Parry-affine realization preserves the finite branch language, not the
  raw metric derivative of the quadratic parent.
- The rectangle order and affine translations introduce gauge choices; no
  arithmetic action or unique quantum boundary phase is claimed.
- The finite SFT/baker realizes a branch coding.  It is not asserted to be the
  full topological inverse-limit continuum of the quadratic parent.
- The finite-state construction is expected to be arithmetically sterile.  Its
  value is an exact separation of the carrier and clock obstructions.
- The \(RLR^\infty\) parent determinant and boundary-period mechanism have
  direct prior art and are reproduction baselines, not original claims.

## Ethical and reporting considerations

No IRB review is applicable.  Reporting follows reproducible computational
mathematics practice rather than an EQUATOR human-study guideline.  The final
paper must disclose AI-assisted coding/review, distinguish proof from
high-precision audit, and describe the classical status of generalized baker
maps and natural extensions.

## Source locking

**Recommended:** yes; implemented locally before candidate code or validation
artifacts are created.

**Registry:** repository-local hash-bound source lock.  It is described as
`source-locked` or `pre-test-declared`, not as a public preregistration.

## Design-freeze decision

**Decision:** sound, with a deliberately negative expected A0 outcome.

**Drivers:**

1. every geometric and orbit claim is exactly falsifiable;
2. the arithmetic gate follows from the frozen finite-edge clock rather than
   target data;
3. the matched controls isolate branch coding, parent orientation, and
   symplecticity.

No cross-model design check was requested or run.
