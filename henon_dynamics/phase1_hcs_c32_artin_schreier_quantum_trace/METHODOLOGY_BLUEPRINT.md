# HCS-C32 Methodology Blueprint

## Research Paradigm

**Selected:** Positivist formal-computational mathematics.

**Justification:** The research question has an objective yes/no content:
exact operator identities, an exact cohomological realization, specified
weights and dimensions, and reproducible finite-field checks.  Numerical
patterns cannot substitute for the claimed theorem.

## Method

**Type:** Theoretical research with exact computer-assisted verification.

**Specific method:** Theorem-led algebraic construction, primary-source
hypothesis audit, and independent finite-field trace reconstruction.

**Justification:** The primary question is universal in \((p,n,r)\), so it
must be answered by algebra and cohomology.  Computation is used only to test
interfaces, signs, exceptional low periods, gauge laws, and small local
polynomials.

## Frozen Mathematical Object

For \(p>3\), \(k_r=\mathbb F_{p^r}\), and

\[
\psi_r(x)=
\exp\!\left(\frac{2\pi i}{p}
\operatorname{Tr}_{k_r/\mathbb F_p}(x)\right),
\]

define

\[
(U_r f)(Q)=|k_r|^{-1/2}
\sum_{q\in k_r}\psi_r(S_6(q,Q))f(q),
\qquad
S_6(q,Q)=qQ-q+2q^3.
\]

The chronological phase at time \(n\) is

\[
\Phi_n(\mathbf x)=
\sum_{i\in\mathbb Z/n\mathbb Z}
(x_ix_{i+1}-x_i+2x_i^3).
\]

The primary arithmetic trace array is

\[
E_{p,n}(r)=
\sum_{\mathbf x\in\mathbb F_{p^r}^{,n}}
\psi_r(\Phi_n(\mathbf x)),
\]

with the axes frozen as

\[
n=\text{dynamical time},
\qquad
r=\text{Frobenius extension degree}.
\]

The proposed single cross-time object is the raw sheaf kernel

\[
\mathcal K_p=\mathcal L_{\psi(S_6)}
\in D_c^b(\mathbb A^1\times\mathbb A^1).
\]

No half-Tate normalization is built into \(\mathcal K_p\).  Its function is
the unnormalized phase \(\psi_r(S_6)\); the factor \(p^{-r/2}\) belongs to
the complex unitary \(U_r\).

Fix \(\ell\ne p\) and one nontrivial character
\(\psi_0:\mathbb F_p\to\overline{\mathbb Q}_\ell^\times\).  Every
cohomology statement below concerns the rank-one nontrivial-character sheaf
\(\Phi_n^*\mathcal L_{\psi_0}\).  It does not concern the full cover
\(y^p-y=\Phi_n\), whose cohomology contains all \(p-1\) nontrivial character
sectors and a trivial summand.

## Data Strategy

**Data type:** Both exact secondary dependencies and newly generated exact
finite-field data.

**Local dependency classes:**

- the source-normalized area-preserving Hénon family and its generating
  function;
- HCS-C05's action, Hessian, repetition, and gauge obstruction ledger;
- HCS-C12A's finite-flat rank-\(2^n\) fixed scheme and cyclic Hill identity;
- HCS-C31's scope boundary requiring a canonical arithmetic fibre or twist.

Every imported artifact will be content-addressed before Phase-3
implementation.  C05 numerical action values are not inputs to the finite
field theorem.

**Generated exact data:**

- finite fields represented by frozen monic irreducible polynomials;
- integer histograms of \(\operatorname{Tr}_{k_r/\mathbb F_p}\Phi_n\) in
  \(\mathbb F_p\), which represent exponential sums in
  \(\mathbb Z[\zeta_p]\) without binary floating point;
- low-degree Frobenius characteristic polynomials reconstructed by Newton
  identities;
- direct and independently reconstructed traces, gauge transforms, critical
  ideals, and Hill determinants.

**Confirmatory computational grid:**

- \(n=1\), \(p\in\{5,7,11,13\}\), \(1\leq r\leq2\);
- \(n=2\), \(p\in\{5,7\}\), \(1\leq r\leq4\).

This grid is sized to reconstruct degrees \(2\) and \(4\).  It is an
interface verification sample, not the population supporting the all-\(n\)
claim.  Any larger grid requires a new freeze.

**Time frame:** Phase 2 performs source verification and equivalence audit;
only after user confirmation may Phase 3 implement the frozen grid.

## Analytical Framework

### WP0 -- Primary-source and equivalence gate

Verify, using primary sources:

1. the exact smooth-at-infinity hypotheses for degree-three
   Artin--Schreier sums;
2. cohomological concentration, dimension \((3-1)^n\), purity, and the
   Grothendieck trace convention;
3. prior finite-field quantizations of polynomial/Hénon maps and prior
   exponential-sum formulations;
4. whether the combined critical-scheme/Hill/cohomology bridge is a genuine
   theorem delta;
5. the precise kernel-convolution, diagonal trace, shifts, and Frobenius
   signs needed to package every Hénon time using one sheaf kernel.

**Hard stop:** a source already proves the same kernel, two-axis trace
identity, Hénon critical interpretation, and rank/purity package, with no new
effective or structural delta left.

### WP1 -- Exact operator and chronology theorem

Prove, without numerical inference:

1. \(U_r=\mathcal F_rD_r\), hence \(U_r\) is unitary;
2. the type-I equations
   \[
   p_{\rm old}=-\partial_qS_6,
   \qquad P_{\rm new}=\partial_QS_6
   \]
   recover exactly \(H_6\);
3. matrix multiplication gives
   \[
   \operatorname{Tr}(U_r^n)
   =p^{-rn/2}E_{p,n}(r);
   \]
4. the \(n=1\) collided derivative and the doubled \(n=2\) neighbor
   occurrences agree with the source cyclic recurrence;
5. no chronological transition average appears anywhere.

At the sheaf-function level, define convolution explicitly by

\[
\mathcal K_p^{\star n}
=R(p_{0n})_!
\bigotimes_{i=0}^{n-1}p_{i,i+1}^*\mathcal K_p,
\]

where the intermediate coordinates are ordered by time.  Freeze all shifts
and signs by checking that its trace function is the unnormalized kernel of
the corresponding operator power over every extension field.

The phrase "exact quantization" will be restricted to the specified
generating-function unitary kernel.  No full nonlinear Egorov theorem is
asserted.

### WP2 -- Gauge theorem

For

\[
S'(q,Q)=S(q,Q)+G(Q)-G(q)+C,
\]

prove

\[
U_r'=\psi_r(C)M_GU_rM_G^{-1}
\]

and

\[
\Phi_n'=\Phi_n+nC.
\]

The released invariant is the projective conjugacy/common-rotation class.
The source normalization \(S_6(0,0)=0\) may be used for reproducibility, but
its absolute eigenphases will not be called classical invariants.

### WP3 -- Critical-scheme and Hill bridge

Prove

\[
\frac{\partial\Phi_n}{\partial x_i}
=x_{i-1}+x_{i+1}-1+6x_i^2,
\]

so that

\[
\operatorname{Crit}(\Phi_n)
=\operatorname{Fix}(H_6^n)
\]

scheme-theoretically, using the multiset-neighbor conventions for
\(n=1,2\).  Reuse only after independent interface verification the exact
facts that this scheme is finite flat of rank \(2^n\) for \(p>3\) and that

\[
\det D^2\Phi_n
=(-1)^{n+1}\det(I-DH_6^n)
\]

on the cyclic critical scheme, with the sign frozen from a direct
\(n=1,2\) calculation.

This is the mandatory Hénon-specific bridge.  Equality of two dimensions by
itself is not treated as a canonical basis correspondence.

### WP4 -- Single-kernel categorical trace theorem

With \(X=\mathbb A^1\) and diagonal \(\Delta:X\to X\times X\), prove the
convention-locked isomorphism

\[
\mathcal V_{n,p}
:=R\Gamma_c\!\left(X,\Delta^*\mathcal K_p^{\star n}\right)
\simeq
R\Gamma_c\!\left(
\mathbb A^n,
\mathcal L_{\psi(\Phi_n)}
\right),
\]

including the exceptional variable collisions at \(n=1,2\).  Grothendieck's
trace formula must then recover \(E_{p,n}(r)\) for every \(r\), while the
function-level normalization recovers \(\operatorname{Tr}(U_r^n)\).

This is the only authorized sense in which one object controls all Hénon
times.  The complexes \(\mathcal V_{n,p}\) vary with \(n\); they are not
powers of one fixed finite-dimensional Frobenius matrix.

### WP5 -- Artin--Schreier cohomology theorem

The top homogeneous form is

\[
\Phi_{n,3}=2\sum_i x_i^3.
\]

For \(p>3\), verify directly that its projective gradient has no common zero.
After the Phase-2 theorem audit, derive the correctly conventioned statement

\[
H_c^i(\mathbb A^n_{\overline{\mathbb F}_p},
\mathcal L_{\psi(\Phi_n)})=0
\quad(i\ne n),
\]

\[
\dim H_c^n=2^n,
\]

and purity of weight \(n\).  If the middle-degree Frobenius eigenvalues are
\(\alpha_{p,n,j}\), the target power-sum identity is

\[
E_{p,n}(r)=(-1)^n
\sum_{j=1}^{2^n}\alpha_{p,n,j}^{r},
\]

subject to the frozen arithmetic/geometric Frobenius convention.  Under a
chosen complex embedding,

\[
|\alpha_{p,n,j}|=p^{n/2}.
\]

No literal half-Tate-twisted representation is introduced when \(n\) is odd.
The sign \((-1)^n\) is a supertrace sign.  It must not be absorbed by
declaring a new ordinary operator whose powers would give the same sign for
every \(r\).

The corresponding normalized local series is frozen as

\[
\exp\!\left(
\sum_{r\geq1}p^{-rn/2}E_{p,n}(r)\frac{z^r}{r}
\right)
=
\det\!\left(
I-zp^{-n/2}\operatorname{Fr}_p\mid H_c^n
\right)^{(-1)^{n+1}}.
\]

Thus parity decides determinant versus reciprocal determinant.  No
self-reciprocity is inferred: Poincar\'e duality pairs the \(\psi_0\) sector
with the \(\psi_0^{-1}\) sector, not generally with itself.

### WP6 -- Exact low-degree reconstruction

Use the first \(2^n\) exact power sums on the frozen grid and Newton identities
in a cyclotomic integer representation to reconstruct the degree-\(2^n\)
polynomial.  Verification has two independent paths:

1. direct enumeration of \(\Phi_n\) trace-residue histograms;
2. an independent finite-field/convolution implementation that does not
   import the producer's arithmetic routines.

Complex embeddings are visualization diagnostics only.  Equality and
purity-interface checks use exact algebra or directed enclosures.

### WP7 -- Baselines and mutations

The following controls are frozen before computation:

- **uncoupled cubic:** remove \(x_ix_{i+1}\); this keeps the generic cubic
  smooth-at-infinity rank/purity baseline but loses the Hénon recurrence;
- **linear/metaplectic:** remove \(2x_i^3\); unitarity survives while the
  degree-three cohomology theorem changes;
- **matched cubic coupling:** change the neighbor coefficient while keeping
  degree and field size fixed;
- **constant gauge:** verify the predicted common root-of-unity rotation;
- **endpoint coboundary:** verify exact unitary conjugacy and invariant
  traces;
- **axis swap mutation:** any code path equating \(r\) with \(n\), or
  \(U_{p^r}^n\) with \(U_p^{rn}\), must fail closed;
- **small-period chronology:** deleting the collided \(n=1\) derivative or
  one of the two \(n=2\) neighbor occurrences must fail;
- **bad-characteristic mutation:** attempting to promote \(p=2,3\) to the
  theorem must fail.
- **isotypic mutation:** replacing the single nontrivial character sector by
  the full Artin--Schreier cover while retaining dimension \(2^n\) must fail;
- **parity mutation:** deleting \((-1)^n\), or treating both parities as an
  ordinary determinant, must fail;
- **point-count mutation:** replacing finite-flat length \(2^n\) by the
  rational point count, or inferring an orbit-indexed basis at a degenerate
  fibre, must fail.

The controls explicitly separate three facts:

1. Fourier--chirp unitarity is generic;
2. smooth-cubic purity is generic;
3. the critical/Hill identification is Hénon-specific.

## Decision Rules

### Promotion threshold

Advance to a full C32 theorem project only if all of the following hold:

1. Phase-2 primary-source review finds a defensible theorem delta;
2. WP1--WP5 close for every \(p>3\) and \(n,r\geq1\);
3. a producer and independent checker reconstruct at least the frozen
   degree-2 and degree-4 cells;
4. all gauge, axis, bad-characteristic, and \(n=1,2\) chronology mutations
   are rejected;
5. the released main claim is the two-axis Hénon trace/cohomology bridge, not
   the generic statement that a unitary has unit-circle spectrum;
6. one fixed sheaf kernel, rather than an unrelated cohomology group chosen
   separately at each \(n\), produces every fixed-time trace complex;
7. the Hénon-specific content exceeds the formal Fubini/sheaf--function
   convolution identity and the generic smooth-cubic purity theorem;
8. no Euler product, Riemann divisor, self-adjoint infinite operator, or
   cross-prime compatible system is inferred.

### Stop or pivot threshold

- **STOP-DUPLICATE:** the combined theorem is direct prior art.
- **STOP-BASELINE:** only generic Fourier unitarity and generic Deligne purity
  remain after controls; the Hénon bridge has no independent theorem content.
- **STOP-CONVENTION:** Frobenius, gauge, or \(n/r\) conventions cannot be made
  source-independent and fail-closed.
- **LOCAL-ONLY:** the local theorem passes but no compatible structure across
  primes or times exists.  Publish, if novel, only as a scoped local theorem;
  do not manufacture an Euler product.
- **PIVOT-1:** prove the general \(\mathrm{SL}_2\) derivative-representation
  collapse theorem and close that finite fibre class.
- **PIVOT-2:** certify the real action Livšic quotient as an auxiliary
  geometric result, but do not market it as arithmetic.

## Validity Criteria

| Criterion | Strategy to ensure it |
|---|---|
| Internal mathematical validity | Exact derivations, explicit exceptional \(n=1,2\) cases, primary-source hypothesis checklist, and convention-locked signs. |
| Construct validity | Keep the unitary spectrum, fixed-\((p,n)\) cohomological spectrum, critical scheme, and real Hénon survivor as four distinct objects. |
| Chronology validity | Preserve every ordered neighbor term and reject all \(n/r\) or transition-average mutations. |
| Arithmetic validity | Use exact finite fields, trace-compatible additive characters, cyclotomic integer histograms, and explicit bad-prime flags. |
| Reproducibility | Content-addressed inputs, deterministic irreducible-polynomial ledger, separate producer/checker, mutation tests, and hash manifest. |
| External validity | The theorem is universal for \(p>3\), while computation is labeled only as low-degree interface verification. |
| Claim validity | Route-A and Hilbert--Pólya language remains downstream and scoped; no local Weil theorem is relabeled as RH. |

## Limitations by Design

- The central purity theorem may be a routine specialization of standard
  exponential-sum theory; the novelty gate is therefore mandatory.
- The finite-field realization is not the certified real four-state survivor
  from HCS-C31.
- The additive character and generating-function constant leave a projective
  phase ambiguity.
- Fixed-\((p,n)\) purity does not provide compatibility across \(n\) or \(p\).
- The single-kernel convolution gives a precise relation across \(n\), but
  the resulting cohomology groups change with time and do not form one fixed
  finite-dimensional spectrum.
- The normalized cohomological phases do not equal the complete spectrum of
  \(U_{p^r}\).
- The full Artin--Schreier cover has \((p-1)2^n\) middle-dimensional
  nontrivial-character contribution plus a trivial sector; the rank \(2^n\)
  statement is for one fixed nontrivial character only.
- Purity alone does not imply Frobenius semisimplicity, a canonical inner
  product, self-adjointness, or a self-functional equation.
- No global counting law, functional equation for \(\xi\), or infinite
  self-adjoint operator follows from this design.

## Ethical Considerations

- No human subjects, personal data, or IRB-regulated activity is involved.
- Riemann-zero ordinates, prime-weight fitting, and target-driven parameter
  selection are forbidden.
- AI assistance, source provenance, and computer-assisted proof boundaries
  must be disclosed in any eventual paper.

## IRB Plan

Not applicable: pure mathematical and computational research with no human
participants or identifiable data.

## Reporting Standard

EQUATOR guidelines are not applicable.  Use theorem-proof reporting with a
computer-assisted mathematics reproducibility appendix, exact claim-status
tables, and an artifact manifest.

## Preregistration

**Recommended:** Yes, internally, before any local polynomial reconstruction.

**Platform:** Repository-frozen protocol; an OSF timestamp is optional if the
project advances beyond Phase 2.

**Status:** Planned.  The protocol must freeze the field grid, Frobenius
convention, controls, failure thresholds, and forbidden data.
