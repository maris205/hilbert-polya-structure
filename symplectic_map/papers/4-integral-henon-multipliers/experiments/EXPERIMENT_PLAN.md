# Experiment Plan: Exact Hénon Multiplier-Modulus Prime-Support Audit

**Problem:** Audit an all-period good-reduction obstruction for exact rational
moduli of return multipliers of a global polynomial symplectic Hénon map.  
**Method thesis:** A non-archimedean maximum lemma makes algebraic periodic
coordinates integral; determinant-one integral monodromy makes every return
eigenvalue an algebraic unit; a conjugation-stable Galois-closure argument
then constrains exact rational moduli; exact low-period elimination and a
planted denominator control test the implementation and the theorem's
scope.  
**Date:** 2026-08-13  
**Execution state:** source-lock v2 written; no candidate experiment executed.

## Claim Map

| Claim | Why it matters | Minimum convincing evidence | Linked blocks |
|---|---|---|---|
| C1. Every complex periodic coordinate of $H_u$ is algebraic and then an algebraic integer. | This is the good-reduction input and makes the result all-period. | Projective no-points-at-infinity proof plus the complete place-by-place maximum proof; symbolic audit on frozen controls. | B1, B2 |
| C2. Every periodic monodromy is in $\mathrm{SL}_2$ of the algebraic integers, so its eigenvalues are algebraic units. | This converts coordinate integrality into the multiplier obstruction. | Exact derivative/determinant proof and direct monodromy products through periods 1--3. | B1, B3 |
| C3. Any multiplier of $H_u$ with exact rational modulus has modulus $1$, hence no rational-prime modulus occurs; rational $\lambda=\pm1$ is a special case. | This closes the global polynomial symplectic prime-modulus clock without assuming rational eigenvalues. | C1--C2 plus $|\lambda|^2=\lambda\overline\lambda$, conjugation-stability of algebraic units, and $\mathbb Q_{>0}\cap\overline{\mathbb Z}^{\times}=\{1\}$. | B1, B3 |
| C4. For monic area-preserving Hénon compositions over $\mathcal O_{K,S}$, prime factors of any exact rational multiplier modulus lie below $S$. | This is the reusable rational-modulus prime-support certificate. | General cyclic maximum proof, Galois closure with all places above $S_{\mathbb Q}$, valuation proof for rational $S$-units, and planted prime-2 control. | B1, B2 |
| C5. $a=-15/16$ realizes exact fixed multipliers $2,1/2$. | Shows area preservation alone is insufficient and the bad-prime support is sharp. | Direct exact fixed-point, trace, factorization, and bad-prime calculation. | B2 |

### Anti-claims to rule out

- The theorem excludes nonrational unstable multipliers or all large
  spectral radii.
- Complex conjugation must preserve the originally selected places of $S$;
  no Galois-closure enlargement is needed.
- A numerically rational-looking modulus is an exact rational modulus.
- Exact absence through period three proves the all-period result.
- Area preservation alone excludes rational primes.
- The bad set may be enlarged after looking at observed multipliers.
- Prime or Riemann-zero data are needed to define or evaluate the claim.

## Paper Storyline

The main paper should establish:

1. a globally polynomial symplectic Hénon candidate at the inherited $u$;
2. the cyclic non-archimedean maximum lemma;
3. integral special-linear periodic monodromy and algebraic-unit multipliers;
4. the rational-modulus $S$-unit prime-support corollary for finite
   compositions, including the Galois-closure step;
5. exact low-period trace/multiplier-polynomial audits for the candidate;
6. the sharp denominator control with multipliers $2,1/2$;
7. explicit separation of exact rational modulus from irrational/approximate
   modulus, general spectral-radius, singular-value, Lyapunov, prime-orbit,
   and target-zero interpretations.

Appendices may contain complete Groebner bases, resultants, exact factor
records, timings, environment manifests, and hashes.  No high-period floating
orbit ledger is required.

## Frozen Definitions

For an algebraic point $P$ of exact period $n$,

$$
M_{P,n}=D_P(H_u^n),
\qquad \det M_{P,n}=1.
$$

A **cycle multiplier** is an eigenvalue $\lambda$ of $M_{P,n}$.

- **Raw rational-prime modulus:** $|\lambda|=p$ exactly; no rationality
  assumption is imposed on $\lambda$.
- **Rational-modulus $S$-unit:** the numerator and denominator of
  $q=|\lambda|\in\mathbb Q_{>0}$ have support only in the predeclared
  $S_{\mathbb Q}$.
- **Irrational/approximate modulus:** $|\lambda|\notin\mathbb Q$, or only a
  numerical approximation looks rational; outside the support conclusion.

## Experiment Blocks

### B0: Source-lock and static integrity

- Validate `experiments/source_lock.json` as JSON and record SHA-256.
- Record that no candidate exact/numerical run preceded the lock.
- Scan executable candidate code for forbidden prime/zero paths, target
  arrays, nearest-prime routines, tolerances that promote near-rational
  eigenvalues or moduli, and
  imports from sealed prior results.
- **Pass rule:** valid lock; zero target-data access; zero candidate run before
  lock.
- **Failure:** protocol stop before any candidate calculation.

Planning-time validation passed: the v2 lock parses as JSON and has SHA-256
`3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269`.
This validates the theory/source-lock artifact only; it does not execute R001
or any candidate run.

### B1: Independent theorem audit

- Check the polynomial inverse and exact preservation of $dX\wedge dY$.
- Audit projective homogenization of the cyclic recurrence: at $Z=0$ every
  coordinate vanishes, and a positive-dimensional projective component would
  meet the hyperplane $Z=0$.
- Confirm algebraicity before invoking valuations.
- Reproduce the cyclic factor-substep recurrence and maximum argument at an
  arbitrary finite place outside $S$.
- Check that monicity and degree $\ge2$ give strict domination when
  $|z|_v>1$.
- Verify monodromy membership in $\mathrm{SL}_2(\overline{\mathcal O}_{K,S})$.
- Verify that both $\lambda$ and $\lambda^{-1}$ are integral and hence units.
- Put all algebraic data in a finite Galois $M/\mathbb Q$ and enlarge to all
  places of $M$ above the rational primes $S_{\mathbb Q}$; verify that this
  set is stable under complex conjugation without assuming that the original
  $(K,S)$ is stable.
- Verify that $\overline\lambda$ is an $S_{\mathbb Q}$-unit and that
  $|\lambda|=q\in\mathbb Q_{>0}$ forces
  $q^2=\lambda\overline\lambda$ and
  $q\in\mathbb Z[S_{\mathbb Q}^{-1}]^\times$.
- Check explicitly that the proof never identifies
  $\overline\lambda$ with the reciprocal eigenvalue; both are units, but
  they are generally different algebraic numbers.
- **Pass rule:** every assumption used is explicit; exact rational modulus
  is distinguished from irrational and approximate moduli.
- **Failure:** weaken or correct the theorem before candidate execution.

### B2: Controls-first exact algebra

#### B2a: planted bad-prime positive

For $a=-15/16$:

- prove $(5/4,5/4)$ is fixed;
- compute the exact derivative matrix;
- factor $L^2-(5/2)L+1$ as $(L-2)(L-1/2)$;
- derive the bad-prime set $\{2\}$ from coefficients before classifying the
  multipliers;
- require both multipliers and their exact rational moduli to be recognized
  as allowed $S$-units.

#### B2b: integral negative control

For $a=0$ and exact periods $1\le n\le3$, run the same recurrence,
monodromy, trace-elimination, and exact-modulus pipeline.  Every exact
rational multiplier modulus must be $1$; every exact rational multiplier
must be $\pm1$ as a special case.

#### B2c: determinant scope control

For the symbolic family
$J_{a,\delta}(X,Y)=(X^2-a-\delta Y,X)$, verify
$\det DJ=\delta$.  The software must refuse the reciprocal-unit conclusion
unless $\delta$ is explicitly declared an $S$-unit and tracked.

- **Pass rule:** the planted prime modulus is found, correctly supported at
  $2$; the integral control has no exact rational modulus outside $1$ (and
  no rational multiplier outside $\pm1$); the scope control is rejected when
  its assumptions are absent.
- **Failure:** repair the exact/rational classification engine before B3.

### B3: Candidate exact audit through period three

Work in

$$
K=\mathbb Q[u]/(u^3-2u^2+2u-2).
$$

For each $n=1,2,3$:

1. build the cyclic recurrence ideal
   $x_{j+1}+x_{j-1}-x_j^2+u=0$ with indices modulo $n$;
2. exclude exact lower-period solutions by exact gcd, saturation, or explicit
   lower-period factor removal;
3. compute the return monodromy

   $$
   M_n=\prod_{j=n-1}^{0}
   \begin{pmatrix}2x_j&-1\\1&0\end{pmatrix};
   $$

4. verify $\det M_n=1$ before any eigenvalue classification;
5. eliminate orbit coordinates to obtain an exact polynomial for the trace
   $T_n=\operatorname{tr}M_n$;
6. combine it with $L^2-T_nL+1$ to obtain the multiplier polynomial;
7. detect rational roots exactly after reducing all coefficients in the
   basis $1,u,u^2$;
8. for each certified complex embedding, represent complex conjugation
   exactly, form $\mu=\lambda\overline\lambda$, and classify
   $|\lambda|\in\mathbb Q$ only when the minimal polynomial of $\mu$ has
   degree one and its positive square root is rational;
9. require every exact rational modulus to be $1$, every rational eigenvalue
   to be $\pm1$, and every algebraic eigenvalue to have a unit
   norm/constant-term certificate;
10. recompute the trace after a cyclic starting-point shift and require exact
   equality.

Period one should additionally use a separate direct elimination from
$X^2-2X-u=0$ and $L^2-2XL+1=0$.

- **Interpretation:** an audit consistent with the theorem is an
  implementation certificate, not empirical evidence for all periods.
- **Failure:** an exact rational modulus outside $1$ triggers an independent
  theory, conjugation, and algebra reconstruction; it is not immediately
  promoted as a counterexample.  A rational eigenvalue outside $\pm1$ is the
  corresponding special case.

### B4: Scope counterexamples and boundary tests

- Serialize at least one integral determinant-one matrix with an irrational
  algebraic-unit eigenvalue $>1$ to demonstrate that irrational spectral
  radius is not restricted to one; a standard cat-map matrix is sufficient
  as a scope control, not a Hénon novelty claim.
- Verify that substituting a floating approximation for $u$ breaks exact
  integrality metadata and cannot enter the theorem pipeline.
- Feed a complex nonrational eigenvalue with irrational exact modulus into
  the reporting layer and require `IRRATIONAL_MODULUS_OUTSIDE_SUPPORT_CLAIM`.
  Feed a floating modulus close to a rational number and require
  `APPROXIMATE_MODULUS_NOT_EXACT`.
- Verify that bad-prime support is derived only from frozen coefficients and
  Jacobian data.

## Run Order and Milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---:|---|
| M0 | Freeze integrity | R000 lock validation; R001 forbidden-data scan | Any pre-lock candidate run or target access stops execution | <1 min | Protocol contamination |
| M1 | Validate proof and engine | R010 proof audit; R011--R013 controls | All proof items and controls pass | <10 min | Hidden good-reduction assumption |
| M2 | Candidate preflight | R020 parameter/root identity; R021 inverse/symplectic identity | Exact identities pass | <1 min | Sign convention drift |
| M3 | Exact candidate algebra | R031--R033 periods 1--3 | Determinant, trace, exact-modulus classification, and cyclic checks agree | <1 CPU-hour | Elimination expression swell |
| M4 | Scope audit | R040--R043 counterexamples/reporting guards | All overclaims rejected | <5 min | Eigenvalue/modulus conflation |

## Exact Run Registry

| Run ID | Purpose | Input | Output | Initial status |
|---|---|---|---|---|
| R000 | Validate/hash source lock | `experiments/source_lock.json` | lock certificate | SOURCE-LOCK PASS |
| R001 | Static target isolation | candidate executable code | isolation report | TODO |
| R010 | Proof and conjugation dependency audit | `notes/PROOF_PACKAGE.md` | proof checklist | TODO |
| R011 | Planted prime-2 control | $a=-15/16$ | exact fixed-point/multiplier record | TODO |
| R012 | Integral control | $a=0$, $n\le3$ | exact multiplier records | TODO |
| R013 | Determinant scope control | symbolic $\delta$ | refusal/assumption record | TODO |
| R020 | Parameter preflight | $P(U)$ and isolation interval | exact parameter certificate | TODO |
| R021 | Global symplectic preflight | $H_u,H_u^{-1},DH_u$ | identity certificate | TODO |
| R031 | Candidate period one | cyclic recurrence | exact trace/multiplier record | LOCKED |
| R032 | Candidate period two | cyclic recurrence | exact trace/multiplier record | LOCKED |
| R033 | Candidate period three | cyclic recurrence | exact trace/multiplier record | LOCKED |
| R040 | Irrational-unit scope control | cat-map matrix | irrational spectral-radius nonclaim record | TODO |
| R041 | Floating-parameter rejection | decimal $u$ | rejection record | TODO |
| R042 | Irrational/approximate-modulus rejection | complex algebraic eigenvalue and floating display | reporting guard record | TODO |
| R043 | Bad-set provenance | frozen coefficient metadata | support certificate | TODO |

`LOCKED` means R031--R033 become executable only after R000--R021 and all
controls pass.  This plan does not execute them.

## Metrics and Reporting Rules

There are no fitted scores or statistical thresholds.  Required output is
exact and categorical:

- `PASS` / `FAIL` for identities and proof dependencies;
- exact ideals, resultants, trace polynomials, characteristic polynomials,
  and rational candidate lists;
- `RATIONAL_EIGENVALUE_UNIT`, `RATIONAL_MODULUS_UNIT`,
  `RATIONAL_MODULUS_S_UNIT`, `RAW_RATIONAL_PRIME_MODULUS`,
  `ALGEBRAIC_UNIT_IRRATIONAL_MODULUS`, or
  `APPROXIMATE_MODULUS_NOT_EXACT`;
- exact distinction among period dividing $n$, formal period, and exact
  period;
- coefficient-derived bad-prime support frozen before multiplier
  classification;
- wall time and peak memory as engineering diagnostics only.

Primality may be tested only after an exact rational modulus is derived
internally.  No external prime list, nearest-prime computation, or
distance-to-prime metric is allowed.

## Failure Matrix

| Failure | Interpretation | Action |
|---|---|---|
| The control misses modulus $2$ or $1/2$ | Exact-modulus or bad-support engine is invalid | Repair before candidate execution |
| The integral control reports an exact rational modulus outside $1$ | Embedding, conjugation, period separation, or exact algebra is invalid | Stop and reconstruct independently |
| Candidate monodromy determinant differs from one | Derivative order or sign error | Stop interpretation |
| Candidate exact rational modulus lies outside $1$ | Direct conflict with the theorem or implementation | Independent proof, conjugation, and algebra audit; do not inspect targets |
| A near-rational modulus is labeled exact | Protocol violation | Invalidate affected output |
| The reporter conflates rational eigenvalue with rational modulus | Scope/logic violation | Repair reporting layer |
| Bad-prime support changes after candidate multipliers are seen | Post-hoc contamination | Invalidate the run |
| Elimination at period three exceeds budget | Engineering limit only | Report periods 1--2 and retain theorem; do not weaken all-period logic |

## Artifact Plan

Required outputs after execution:

- `results/source_lock_validation.json`
- `results/proof_audit.json`
- `results/control_audit.json`
- `results/candidate_multiplier_audit.json`
- `results/symplectic_identity_audit.json`
- `results/scope_audit.json`
- exact serialized period ideals and multiplier polynomials for $n\le3$
- command/environment manifest and SHA-256 hashes
- a negative-result ledger that preserves all nonclaims

## Final Checklist

- [x] Research question frozen before candidate execution.
- [x] Algebraic periodic-point quantifier stated explicitly.
- [x] Rational eigenvalue, exact rational modulus, and approximate modulus
  separated.
- [x] Conjugation-stable Galois-closure enlargement stated explicitly.
- [x] All-period proof written before finite computation.
- [x] Exact cutoff frozen at $n\le3$.
- [x] Planted prime-2, integral, and determinant-scope controls frozen.
- [x] Bad-prime support derived from coefficients before multiplier access.
- [x] No prime table or Riemann-zero data allowed.
- [x] Source-lock JSON validated and hashed.
- [x] Proof independently audited at source-lock level after the explicit
  Galois-closure repair; executable R010 artifact remains future work.
- [ ] Controls executed before candidate runs.
- [ ] Candidate exact audit independently checked.
- [ ] Final reporting guards verified.
