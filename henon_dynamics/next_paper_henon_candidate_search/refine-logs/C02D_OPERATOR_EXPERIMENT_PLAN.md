# C02D pre-registration: trace-compatible pinning operator

Date: 2026-08-06  
Status: **closed NO_GO on 2026-08-06; no spectrum run authorized**

Closure record: `../../henon_pinning_trace_obstruction/README.md`.
The exact-rational producer and independent checker both pass, certifying the
kill conditions rather than promoting the candidate.

## 1. Decision question

Can the explicit C02C endpoint and projective constants be used to construct a
natural graph-directed holomorphic operator for the certified local
\(H_6\) survivor, together with a quantitative cylinder-truncation theorem
whose flat traces converge to

\[
\sum_{x\in\operatorname{Fix}(H_6^n)\cap\Lambda_*}
\frac{1}{\det(I-DH_6^n(x))}
\]

under the signed holomorphic convention?

This is the remaining manuscript gate.  It is not a search for numerical
agreement with Riemann zeros.

## 2. Source lock and inheritance

- Map: \(H_6(q,p)=(1-6q^2-p,q)\).
- Clock: one chronological Hénon iterate.
- Base: the certified local survivor and its exact admissibility graph.
- Prior-art boundary: after \((x,y)=(-6q,6p)\),
  Sterling--Dullin--Meiss Theorem 3 already covers the real
  forbidden-neighbor SFT and real signed-root uniqueness at \(b=1,k=6\).
- Weight for the first theorem: \(g\equiv1\).
- Trace denominator: signed \(\det(I-DH_6^n)\), not its absolute value.
- Project-specific domains, constants and finite-dimensional residue
  identities: C02C.  The qualitative pinning/Cauchy/Fredholm mechanism is
  prior art and must be reconstructed from the primary sources.  BPS's
  orientation convention gives the absolute determinant denominator; C02D's
  signed convention is a distinct object that must be proved, not assumed.
- No averaged transition matrix, fitted Möbius generator, target zero data,
  prime weight or post-hoc normalization is permitted.

The operator kernel must be derived from the pinning/Cauchy formula used in
the primary analytic-hyperbolic literature.  A direct-sum Hardy or Bergman
composition operator is not assumed in advance.

The inherited projective constant is

\[
\delta=\left(\frac{224}{773}\right)^2
=\frac{50176}{597529},
\qquad
12\delta=\frac{602112}{597529}>1.
\]

## 3. Specific mathematical target

The approximation index is frozen semantically before any formula is chosen:

- \(\mathcal L\) is the exact **one-step-clock** operator, if a natural one
  can be defined;
- \(\mathcal L^{[N]}\) must be a **one-step finite-memory approximation** on
  the same space (or through explicitly frozen intertwining
  embeddings/projections), obtained by replacing infinite-memory pinning
  coordinates or kernel coefficients with their length-\(N\) endpoint
  approximants;
- \(\mathcal L^{[N]}\) is neither the time iterate \(\mathcal L^N\) nor an
  exact \(N\)-block recoding of \(\mathcal L\).  The former changes dynamical
  time and the latter is an intertwining identity rather than a convergent
  approximation.

If the primary-source kernel does not admit the second interpretation
naturally, the norm-convergence experiment is `NO_GO` and must be reformulated
before computation.

If the frozen common operator space is a Hardy/Bergman-type Hilbert space, the
preferred theorem target is a trace-class bound of the form

\[
\|\mathcal L-\mathcal L^{[N]}\|_{\mathfrak S_1}
\le C\tau_{\mathrm{eff}}^N,
\qquad 0<\tau_{\mathrm{eff}}<1.
\]

If the natural common space is instead a holomorphic Banach space, replace
\(\mathfrak S_1\) by a precisely specified nuclear ideal/norm or an
approximation-number bound that implies

\[
\left|
\operatorname{tr}(\mathcal L^n)
-\operatorname{tr}((\mathcal L^{[N]})^n)
\right|
\le C_n\tau_{\mathrm{eff}}^N
\]

for every fixed \(n\).  The constants must be explicit functions of the C02C
disk margins, \(\kappa\), \(\beta\), \(\delta\), graph degree and Cauchy
contour separation.  A per-cylinder estimate is insufficient: after summing
over all admissible length-\(N\) cylinders, the certified effective rate must
still satisfy

\[
\tau_{\mathrm{eff}}<1.
\]

The finite-cylinder index \(N\) and dynamical time \(n\) remain distinct.

## 4. Mandatory derivation packages before implementation

### WP5A — exact kernel reconstruction

1. Transcribe the pinning variables and the Cauchy kernel from the primary
   source, including the endpoint derivative numerator and direction signs.
2. Specialize it to the C02C crossed map without dropping orientation signs.
3. Derive the fixed-point residue and verify that it gives exactly the signed
   C02C matching identity for \(n=1,2\) before general \(n\).
4. State whether the natural space uses interior, exterior or mixed
   holomorphic variables.  Freeze all contours and norms.

### WP5B — quantitative compactness

1. Use the strict endpoint-disk and projective child-disk margins to construct
   nested source/target domains.
2. Derive approximation-number or nuclear-norm bounds analytically.
3. Track base and fibre sensitivities separately; the inequality
   \(12\delta>1\) forbids claiming joint contraction in the unscaled product
   norm.
4. Determine whether a weighted anisotropic norm repairs the estimate
   naturally.  Any weight must be frozen from the derivative inequalities,
   not fitted to finite sections.

### WP5C — trace-compatible cylinder error

1. Define \(\mathcal L^{[N]}\) as a fixed-one-step-clock finite-memory kernel
   assembled from chronological length-\(N\) pinning windows, not as
   \(\mathcal L^N\), an exact block recoding, or an average of transitions.
   Freeze the outer endpoint rule and the kernel replacement for every
   cylinder.
2. Put every \(\mathcal L^{[N]}\) on one common operator space, or freeze
   explicit embeddings and projections that make the comparison meaningful.
3. State whether traces count geometric fixed points or symbolic periodic
   words, prove the coding multiplicity, and handle any Markov-boundary double
   coding explicitly.  Periods one and two retain chronological multiplicity.
4. State the lower range \(N\ge N_0\) and include the growth in the number of
   admissible cylinders in the aggregate \(\tau_{\mathrm{eff}}\) bound.
5. Bound the omitted-cylinder or domain-extension error uniformly.
6. Only after the proof is written, implement numerical singular-value and
   trace regressions as adversarial checks.

## 5. Frozen adversarial controls for a later protocol

Any implementable C02D protocol must include:

- reversed chronological products;
- scalar-averaged or statewise-constant surrogate branches as
  `EXPECTED_FAIL` controls;
- period-one and period-two doubled-incidence checks;
- signed versus absolute determinant traces reported as distinct objects;
- two independent implementations of periodic flat traces;
- complete cylinder-ID checks and deliberate truncation/tamper rejection;
- neighboring contour radii chosen before the run;
- binary64 conditioning diagnostics plus high-precision rechecks, without
  changing the object or threshold after inspection.

## 6. Promotion criteria and mechanical outcomes

C02D may freeze the manuscript only if all of the following hold:

1. the function space, kernel, orientation, potential, clock and norm are
   mathematically natural and fully specified;
2. the exact fixed-point trace agrees with the C02C signed residue;
3. a quantitative approximation theorem is proved, not inferred from stable
   finite spectra;
4. the aggregate error/trace theorem requires a genuinely new
   \(H_6\)-specific estimate or proof step; merely substituting explicit
   constants into a cited general theorem is `NO_GO`;
5. an independent checker rejects reversed, averaged, truncated and tampered
   controls;
6. a direct Rugh 1992 full-text check, dedicated Hill-identity source audit
   and journal-level novelty review find no subsuming theorem.

Apply the outcomes in this order so they are mutually exclusive: any kill
condition gives `NO_GO`; among survivors, test `GO_OPERATOR`; if it fails,
test `GO_LIMITED_TRACE`; if that also fails, return `NO_GO`.

Classify the outcome at exactly one of three levels:

- `NO_GO` **(kill conditions tested first):** the evidence is only stable
  finite spectra, single-branch decay, a routine specialization of known
  nuclearity, failure in the frozen natural norm, or an \(N\)-indexed object
  that is only \(\mathcal L^N\)/exact block recoding rather than a one-step
  finite-memory approximation.  Return to breadth-first candidate generation.
- `GO_OPERATOR`: a natural common operator is frozen, its exact periodic trace
  is proved, and an aggregate operator-ideal/approximation bound
  \(C\tau_{\mathrm{eff}}^N\) with \(\tau_{\mathrm{eff}}<1\) is proved after
  cylinder growth is included.  Determinant convergence remains a separate
  claim unless the bound controls the full trace series.
- `GO_LIMITED_TRACE`: only a fixed-\(n\) estimate
  \(|\operatorname{tr}\mathcal L^n-
  \operatorname{tr}(\mathcal L^{[N]})^n|\le
  C_n\tau_{\mathrm{eff}}^N\) is proved, with no
  sufficient growth control on \(C_n\).  This authorizes only a limited
  coding/trace theorem and explicitly forbids Fredholm-determinant convergence
  claims.

Do not extend the lane merely by increasing matrix size.

## 6A. Final mechanical outcome (2026-08-06)

The first applicable outcome is **NO_GO**, for two independent reasons.

1. In the standard BPS/Rugh pinning construction, the elementary mixed
   Cauchy kernel is already an exact one-step object. On the common endpoint
   domain, the C02C functions \(Q_1,Q_N\) are the iterated pinning data of
   chronological word summands of \(\mathcal L^N\). The usual window
   interpretations are therefore a time iterate or an exact higher-block
   recoding, both explicitly excluded as \(\mathcal L^{[N]}\) above. This
   conclusion is scoped to the frozen standard-kernel semantics; it does not
   forbid designing a new history-space object.
2. With the frozen BPS contour/residual convention, deleting the orientation
   factor gives
   \(\operatorname{tr}K_{\rm raw}^n=-\sum_x\det(I-DF^n(x))^{-1}\).
   No ordinary multiplicative scalar edge cocycle can provide the missing
   orbitwise constant \(-1\) on both a primitive orbit and its double
   repetition. This does not exclude accidental equality of aggregate trace
   sums through cancellations among different orbits.
   Odd supertrace/reciprocal determinant alternatives are algebraically
   valid but classical and do not rescue the pre-registered ordinary
   determinant claim.

A separate positive lemma constructs strict mixed disks
\(Y_t\times X_r\), with \(X_s\Subset Y_s\) margin \(1/128\), square-root
image clearance \(1/360\), and derivative bound \(2/\sqrt{66}\). These are
local analytic constants, not an aggregate nuclear-norm convergence rate.

The complete frozen derivation, source audit, Route-A record, producer,
checker, and artifacts are under `henon_pinning_trace_obstruction/`.

## 7. Route-A and RH firewall

Before the operator and its normalization were frozen, C02D was
`NOT_TESTABLE` under Route-A input validation. The closure audit froze the
standard BPS raw-kernel/scalar-repair candidate and its determinant
convention, so it now has the formal tuple
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` and overall
`ROUTE_A_REJECTED`. Route B, zero fitting and prime fitting remain closed.
