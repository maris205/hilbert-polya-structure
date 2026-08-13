# Experiment Plan: Exact Prime-Multiplier Obstruction Audit

**Problem:** Audit an all-period arithmetic obstruction for the genuine
nonlinear derivative clock of the frozen PCF quadratic.  
**Method thesis:** Algebraic integrality and derivative content exclude every
raw rational-prime multiplier before any orbit search; exact low-period
multiplier polynomials and controls test the implementation and scope.  
**Date:** 2026-08-13  
**Execution state:** source lock written; no candidate experiment executed.

## Claim Map

| Claim | Why it matters | Minimum convincing evidence | Linked blocks |
|---|---|---|---|
| C1. Every rational period-$n$ multiplier of $g(z)=z^2-u$ lies in $2^n\mathbb Z$. | This is the mechanism-level all-period obstruction. | Complete proof from periodic-point integrality and the chain rule; exact quotient-ring audits for $n\le4$. | B1, B3 |
| C2. The frozen candidate has no raw rational-prime multiplier at any period. | This closes the nonlinear raw-prime clock without target fitting. | C1 plus the exact $n=1$ exclusion of $\lambda=\pm2$; exact low-period audit finds no contradictory candidate. | B1, B3 |
| C3. Odd rational exponent-prime targets are absent, but $p=2$ remains open for $n\ge2$. | Prevents raw-prime and exponent-prime claims from being conflated. | Exact $2$-adic corollary; outputs report the $p=2$ residue as `OPEN`, never `FAIL` or `ABSENT`. | B1, B3, B5 |
| C4. The cotangent construction only transports the multiplier to a reciprocal symplectic pair branchwise. | Establishes relevance to the symplectic-map program without overclaiming. | Symbolic pullback of the canonical one-form and symbolic zero-section return derivative, together with singular/noninvertible caveats. | B4 |

### Anti-claims to rule out

- The result is a numerical absence up to a cutoff.
- A near-integer multiplier is an exact rational multiplier.
- The theorem excludes $|\lambda|=2^n$ at all periods.
- A formal dynatomic root automatically has exact period $n$.
- The cotangent formula is a global compact symplectomorphism.
- Any prime or Riemann-zero table is needed to formulate or test the claim.

## Paper Storyline

The main paper must establish:

1. the all-period divisibility theorem;
2. the exact specialization and period-one residue check;
3. an exact, reproducible multiplier-polynomial audit through $n=4$;
4. sharp controls showing both theorem-compatible prime values and failure
   when algebraic-integrality assumptions are removed;
5. the exact but only branchwise cotangent relation;
6. the unresolved $p=2$ exponent-prime boundary.

Appendix material may include complete exact polynomials, factorization
records, quotient-ring certificates, timings, and the conditional real-orbit
ledger if its certification gate passes.

Experiments intentionally cut:

- external prime tables, prime-label assignments, and prime-density tests;
- Riemann-zero data, spectral unfolding, determinant fitting, or
  quantization;
- floating searches beyond the exact low-period cutoff;
- any high-period real ledger lacking a completeness certificate;
- parameter neighbors selected after inspecting candidate multipliers.

## Frozen Definitions

For a point $z$ of exact period $n$,

$$
\lambda=(g^{\circ n})'(z).
$$

- **Raw rational-prime:** $\lambda\in\mathbb Q$ and $|\lambda|=p$.
- **Rational exponent-prime:** $\lambda\in\mathbb Q$ and
  $|\lambda|=p^n$.
- **Complex modulus-only:** $|\lambda|=p^n$ without
  $\lambda\in\mathbb Q$; outside the theorem and not tested as a prime clock.

No output may change these definitions after execution.

## Experiment Blocks

### B0: Source-lock and static integrity check

- **Claim tested:** independence and absence of target leakage.
- **Why this block exists:** all candidate computation must be downstream of
  a frozen question, theorem, controls, and stop rules.
- **Task:** validate `source_lock.json` as JSON; record its cryptographic hash;
  scan candidate code and configuration for forbidden prime/zero paths and
  post-hoc tolerances.
- **Compared systems:** none.
- **Metrics:** JSON validity; hash present; forbidden-token count in executable
  code; candidate-run count before lock.
- **Success criterion:** valid lock, zero pre-lock candidate runs, zero
  executable access to forbidden data.
- **Failure interpretation:** protocol failure; do not execute the candidate.
- **Target:** reproducibility appendix and experiment passport.
- **Priority:** MUST-RUN, before all blocks below.

### B1: Analytic theorem and boundary audit

- **Claim tested:** C1--C3.
- **Why this block exists:** the scientific conclusion must not depend on a
  finite orbit cutoff.
- **Task:** independently check every proof dependency:
  monicity of $F^{\circ n}-X$, transitivity of integrality, chain-rule
  factorization by $m^n$, rational algebraic integers, specialization
  $g'=2z$, fixed multipliers $\pm2$, and the odd-$p$ valuation argument.
- **Data:** no numerical data.
- **Metrics:** proof checklist with one pass/fail item per implication;
  assumption-to-conclusion trace; edge-case list.
- **Success criterion:** no hidden assumption and no conclusion stronger than
  the proof.  In particular, $p=2$ exponent-prime for $n\ge2$ remains
  explicitly open.
- **Failure interpretation:** correct or weaken the theorem before executing
  candidate algebra.
- **Target:** theorem and proof appendix.
- **Priority:** MUST-RUN.

### B2: Controls-first exact algebra

- **Claim tested:** the implementation detects both permitted and forbidden
  outcomes and respects the theorem's assumptions.
- **Why this block exists:** a code path that always reports “no prime” is not
  a valid audit.
- **Maps and frozen outcomes:**

  1. $z^2$: fixed multipliers $0,2$; every nonzero exact period-$n$ cycle has
     multiplier $2^n$.
  2. $z^2-2$: fixed multipliers $-2,4$; this exercises the period-one
     $p=2$ residue at the Chebyshev boundary.
  3. $z^2-3/4$: fixed multipliers $-1,3$; the odd raw prime $3$ must be found,
     demonstrating why algebraic-integer coefficients matter.

- **Cutoff:** exact periods $1\le n\le4$ for the same dynatomic/resultant
  pipeline used on the candidate.
- **Metrics:** exact polynomial equality, factor degrees, exact rational-root
  list, divisibility classification, internally derived primality label.
- **Success criterion:** all frozen fixed-point outcomes are recovered; the
  $c=0$ exponent clock is recovered; theorem assumption flags differ correctly
  between $c=0,-2$ and $c=-3/4$.
- **Failure interpretation:** repair the implementation; candidate execution
  remains locked.
- **Target:** control table in the main paper or appendix.
- **Priority:** MUST-RUN before B3.

### B3: Candidate exact multiplier-polynomial audit, $n\le4$

- **Claim tested:** exact implementation consistency with C1 and C2.
- **Why this block exists:** provide reproducible algebraic certificates for
  the frozen map while keeping the all-period proof primary.
- **Coefficient field:**

  $$
  K=\mathbb Q[u]/(u^3-2u^2+2u-2).
  $$

- **Primary construction:**

  $$
  \Phi_n(z)=\prod_{d\mid n}(g^{\circ d}(z)-z)^{\mu(n/d)},
  $$

  followed by

  $$
  R_n(L)=\operatorname{Res}_z
  \left(\Phi_n(z),L-(g^{\circ n})'(z)\right).
  $$

- **Exact-period safeguard:** compute gcds with all lower
  $g^{\circ d}(z)-z$; record any formal-period contamination caused by a
  root-of-unity multiplier.  Do not infer exact period from $\Phi_n$ alone.
- **Cycle multiplier polynomial:** only after exact-period handling, verify
  that per-point multiplicity groups into cycles and that the monic resultant
  is the expected $n$th power.  Store both the per-point resultant and monic
  per-cycle polynomial.
- **Rational-root certification:** reduce coefficients in the basis
  $1,u,u^2$ and require all nonrational basis components to vanish exactly.
  Factor or solve the resulting rational gcd exactly.  Floating
  approximations are display-only.
- **Independent check:** in the quotient algebra
  $K[z]/(\Phi_n)$, compute the chain-rule multiplier directly and verify its
  annihilating polynomial against the resultant.  Separately run the
  conjugate coordinate $f_u$ and check exact equality of cycle multiplier
  polynomials after normalization.
- **Frozen period cutoff:** $n=1,2,3,4$.  No post-hoc extension is needed to
  support the theorem.
- **Metrics:** formal degree, exact-period degree, cycle count, resultant
  degree, perfect-power check, rational candidates, $2^n$ divisibility,
  raw-prime flag, exponent-prime flag, conjugacy equality.
- **Success criterion:** every exact rational candidate is in
  $2^n\mathbb Z$; no raw rational-prime occurs; conjugacy and the two exact
  pipelines agree.
- **Failure interpretation:** a violation of $2^n$ divisibility is an
  algebra/code failure, not an empirical refutation of the theorem.  A
  failure of conjugacy equality also stops interpretation.
- **Target:** main exact-audit table plus machine-readable certificates.
- **Priority:** MUST-RUN.

### B4: Exact branchwise symplectic bridge

- **Claim tested:** C4.
- **Why this block exists:** connect the nonlinear derivative clock to the
  symplectic-map scope while preserving its limitations.
- **Task:** symbolically verify on $q\ne0$

  $$
  \widehat g(q,p)=\left(q^2-u,\frac{p}{2q}\right),
  \qquad
  \widehat g^*(P\,dQ)=p\,dq,
  $$

  and, on $p=0$, verify the one-step derivative and the period-$n$ product
  $\operatorname{diag}(\lambda,\lambda^{-1})$.
- **Negative checks:** evaluation at $q=0$ must be rejected; the two real
  branches must be shown to have overlapping images; no compactness or global
  inverse test may pass.
- **Metrics:** exact pullback residual; determinant; return-product equality;
  critical-line rejection; branch-image overlap flag.
- **Success criterion:** zero symbolic residual on each regular branch and all
  negative checks triggered.
- **Failure interpretation:** remove the bridge claim; it does not affect the
  arithmetic theorem.
- **Target:** one proposition and one limitations paragraph.
- **Priority:** MUST-RUN.

### B5: Conditional certified real-orbit ledger through $n=20$

- **Claim tested:** none beyond reproducibility and qualitative exposition.
- **Why this block exists:** a real-orbit ledger could make the low-entropy
  PCF dynamics concrete, but it is unnecessary for the theorem.
- **Current status:** DISABLED.
- **Enablement gate:** before any candidate evaluation, a controls-only
  prototype must produce disjoint rational intervals, prove existence and
  uniqueness in each interval, prove completeness from a frozen
  symbolic/monotonicity count, and do so without requiring Arb.
- **Maximum cutoff if enabled:** $n=20$; never increase after viewing results.
- **Certification options:** exact rational interval Newton/Krawczyk bounds
  with a rational isolating interval for $u$, or an equivalently rigorous
  SymPy-based exact isolation method.  Plain `mpmath`, Newton convergence,
  residual thresholds, or dense gridding do not certify completeness.
- **Success criterion:** every reported orbit has an interval certificate and
  the ledger cardinality equals the independent symbolic count.
- **Failure interpretation:** omit B5.  Do not replace it by uncertified
  floating output and do not weaken C1 or C2.
- **Target:** appendix only.
- **Priority:** NICE-TO-HAVE, gated and nonblocking.

## Run Order and Milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---:|---|
| M0 | Freeze integrity | R000 validate/hash source lock; R001 forbidden-data scan | Any pre-lock candidate result or forbidden access stops the project | <1 min | Protocol contamination |
| M1 | Validate proof and exact engine | R010 proof dependency audit; R011--R013 three control maps | All controls and fixed predictions pass before candidate access | <5 min | Formal/exact-period confusion |
| M2 | Candidate algebra preflight | R020 minimal polynomial/root selection; R021 exact conjugacy; R022 derivative-content identity | Exact identities all pass | <1 min | Wrong algebraic embedding or normalization |
| M3 | Exact candidate audit | R031, R032, R033, R034 for periods 1--4 | Divisibility, resultant, quotient, and conjugacy checks all agree | <1 CPU-hour | Resultant expression swell at $n=4$ |
| M4 | Symplectic bridge | R040 one-form pullback; R041 return spectrum; R042 singular/global negative checks | All caveats are machine-checked and reported | <1 min | Accidental global-language overclaim |
| M5 | Optional real ledger | R050 controls-only certification feasibility; if and only if passed, dated amendment then R051 candidate $n\le20$ | Omit on any completeness or non-Arb failure | unbudgeted until gate | Certification may be more expensive than its evidentiary value |

## Exact Run Registry

| Run ID | Purpose | Input | Output | Priority | Initial status |
|---|---|---|---|---|---|
| R000 | Validate frozen protocol | `source_lock.json` | validation record and SHA-256 | MUST | TODO |
| R001 | Static isolation scan | candidate executable files | forbidden-access report | MUST | TODO |
| R010 | Proof dependency audit | `notes/PROOF_PACKAGE.md` | proof checklist | MUST | TODO |
| R011 | Power-map control | $c=0$, $n\le4$ | exact multiplier certificates | MUST | TODO |
| R012 | Chebyshev control | $c=-2$, $n\le4$ | exact multiplier certificates | MUST | TODO |
| R013 | Nonintegral control | $c=-3/4$, $n\le4$ | exact multiplier certificates | MUST | TODO |
| R020 | Parameter preflight | $P(U)$ and isolation interval | exact root-selection certificate | MUST | TODO |
| R021 | Conjugacy preflight | $f_u,g,\phi$ | exact polynomial identity | MUST | TODO |
| R022 | Theorem preflight | $g'(z)$ | exact factorization $2z$ | MUST | TODO |
| R031 | Candidate period 1 | $g$, $n=1$ | exact dynatomic/multiplier record | MUST | LOCKED |
| R032 | Candidate period 2 | $g$, $n=2$ | exact dynatomic/multiplier record | MUST | LOCKED |
| R033 | Candidate period 3 | $g$, $n=3$ | exact dynatomic/multiplier record | MUST | LOCKED |
| R034 | Candidate period 4 | $g$, $n=4$ | exact dynatomic/multiplier record | MUST | LOCKED |
| R040 | Canonical one-form | $\widehat g$ on $q\ne0$ | symbolic pullback certificate | MUST | TODO |
| R041 | Reciprocal return | zero-section periodic word | symbolic return certificate | MUST | TODO |
| R042 | Negative geometry checks | critical line and both branches | rejection/overlap record | MUST | TODO |
| R050 | Non-Arb feasibility | controls only | certification gate report | NICE | TODO |
| R051 | Real ledger | candidate, $n\le20$ | certified ledger | NICE | DISABLED |

`LOCKED` means the run becomes executable only after R000--R022 pass.  Writing
this plan does not unlock or execute it.

## Metrics and Reporting Rules

There are no fitted scores or statistical thresholds.  Required reporting is
exact and categorical:

- `PASS` / `FAIL` for polynomial identities and proof dependencies;
- exact factorization and exact rational candidate list;
- `RAW_PRIME`, `EXPONENT_PRIME_ODD`, `EXPONENT_PRIME_TWO`, or `NONE`, using
  only exact rational candidates;
- `OPEN` for the all-period $p=2$ exponent-prime residue;
- explicit distinction among exact period, formal period, and period dividing
  $n$;
- wall time and peak memory as engineering diagnostics only.

Primality is evaluated only after an exact candidate has been derived from
the candidate or a frozen control.  No prime list is loaded, and no nearest
prime or distance-to-prime metric is computed.

## Compute and Data Budget

- **CPU:** less than one CPU-hour for all required exact runs.
- **Memory:** less than 4 GiB for the required $n\le4$ audit.
- **GPU:** none.
- **External data:** none.
- **Human labeling:** none.
- **Biggest bottleneck:** exact resultant expression swell at $n=4$.
- **Mitigation:** reduce coefficients modulo the cubic parameter polynomial
  after every operation; use subresultants; cross-check quotient-algebra
  minimal polynomials; stop at the frozen cutoff.
- **Conditional ledger:** receives no compute budget until R050 passes.  Arb,
  Sage, or PARI availability is not assumed or promised.

## Failure Matrix

| Failure | Interpretation | Action |
|---|---|---|
| A control misses $2$, $-2$, or $3$ | Rational-root/primality pipeline is invalid | Repair before candidate execution |
| Candidate rational multiplier not divisible by $2^n$ | Algebraic representation, period handling, or resultant implementation error | Stop; independently reconstruct the certificate |
| Resultant is not grouped by cycle multiplicity | Formal-period contamination or normalization error | Factor exact-period components; do not take a formal $n$th root |
| $f_u$ and $g$ multiplier polynomials disagree | Conjugacy normalization error | Stop interpretation |
| Low-period audit finds no $2^n$ exponent multiplier | No all-period conclusion about $p=2$ | Keep `OPEN` |
| Cotangent formula fails at $q=0$ | Expected critical singularity | Record as limitation, not a failed arithmetic claim |
| Real-ledger feasibility gate fails | High-period certification unavailable | Omit B5 |
| Any prime/zero target file is accessed | Protocol contamination | Invalidate affected run and do not retune |

## Artifact Plan

Required outputs after execution:

- `results/source_lock_validation.json`
- `results/proof_audit.json`
- `results/control_audit.json`
- `results/candidate_multiplier_audit.json`
- `results/conjugacy_audit.json`
- `results/symplectic_bridge_audit.json`
- exact serialized polynomials for every $n\le4$
- command/environment manifest and SHA-256 hashes
- negative-result ledger preserving the open $p=2$ residue

If B5 is enabled, its interval certificates and completeness count must be
separate from the required exact audit.

## Final Checklist

- [x] Research question frozen before candidate execution.
- [x] Raw-prime and exponent-prime targets separated.
- [x] All-period proof written before finite computations.
- [x] Exact cutoff frozen at $n\le4$.
- [x] Controls $c=0,-2,-3/4$ frozen.
- [x] Conjugacy-invariant check frozen.
- [x] No prime table or Riemann-zero data allowed.
- [x] High-period ledger conditional and nonblocking.
- [ ] Source-lock JSON validated and hashed.
- [ ] Controls executed before candidate runs.
- [ ] Candidate exact audit executed and independently checked.
- [ ] Symplectic bridge and negative geometry checks executed.
- [ ] Results reported without closing the open $p=2$ exponent-prime case.

