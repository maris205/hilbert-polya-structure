# First-round experiment results and second-round theorem bridge

Date: 2026-08-05  
Generation: `HCS-2026-08-05`  
Status: **first round and C02C complete; no candidate reached BF3 or formal
Route-A promotion**

## 1. Executive decision

The first-round tournament produced one reusable positive analytic structure
and two target-independent obstructions:

1. **C02/C02B positive, narrowly scoped.**  The true derivative projective
   cocycle contracts explicit separated complex fibre disks over the real
   survivor.  A second-round theorem also proves that the R059 signed-root
   orbit solver is a strict holomorphic contraction on explicit complex
   sequence polydiscs.  Finite-dimensional holomorphic Markov branches,
   nuclearity, and a Fredholm determinant remain open.
2. **C03 stopped.**  Exact finite-field local zeta factors exist, but the
   striking cycle statistics are explained by the correct reversible null.
   The naive global Euler-product route has no canonical local-to-global
   mechanism.
3. **C05 stopped as an intrinsic absolute-phase candidate.**  The generating
   function has an additive-constant gauge which rotates the determinant
   variable.  More strongly, strict diagonal dominance proves that its
   Maslov character is only a one-symbol locally constant weight on this
   survivor.

No Riemann zeros, target prime weights, fitted spectral scale, or post-hoc
unfolding were used.  Route B remains closed.

## 2. Raw comparison table

| Candidate | Frozen independent variable | Primary raw result | Control / delta | Decision |
|---|---|---|---|---|
| C02 | memory $m=1,\ldots,8$ | $q$-diameter bound falls from $0.141479$ to $8.93987\times10^{-4}$; fibre derivative bound $0.0839725$; child-disk gap $0.187107$ | memory-8 bound is $99.368\%$ below memory 1; 17/17 primitive cycles through period 8 pass projective/monodromy checks | exact real-base/complex-fibre lemma; no A2 |
| C02B | cyclic words through length 12 | uniform complex self-map margin $9.43718\times10^{-3}$; contraction $2/\sqrt{17}=0.485071$ | producer 14/14 and independent checker 18/18; all cyclic chronology checks pass | proved signed-root complex-polydisc bridge only |
| C03 | all primes $p\le251$ | 54 exact local ledgers; 52 good-prime aggregates; 995,777 phase points | no matched-reversible metric reaches the frozen candidate threshold | reject naive global Euler product; retain local ledger |
| C05 | cutoffs $8,12,16,20$ | 2,170 primitive cycles; 2,240 primitive/repeat phase rows; 0 Hill, reversal, parity, or symbol-count defects | at $s=0.5,\vartheta=1$, Maslov drift is $4.459\times10^{-14}$, but orientation fallback is $9.943\times10^{-15}$; exact gauge and local-symbol collapse dominate the decision | reject intrinsic fixed-$z$ absolute phase; retain phase ledger |

### C03 matched-reversible raw diagnostics

The table reports the Hénon mean, the mean of the 16-control ensemble at each
prime averaged over 52 good primes, the raw relative delta, and the frozen
standardized summaries.

| Diagnostic | Hénon | Matched control | Relative delta | mean $z$ | mean $\lvert z\rvert$ | outside empirical interval |
|---|---:|---:|---:|---:|---:|---:|
| cycle count | 118.577 | 120.512 | -1.606% | -0.768 | 1.073 | 13.5% |
| fixed points | 0.904 | 1.978 | -54.31% | -0.683 | 0.737 | 9.6% |
| largest-cycle fraction | 0.07502 | 0.07955 | -5.686% | -0.089 | 1.078 | 23.1% |
| short-point-mass fraction | 0.28244 | 0.28049 | +0.697% | -0.127 | 0.940 | 19.2% |
| symmetric-cycle count | 116.846 | 116.846 | 0 | 0 | 0 | 0 |
| symmetric-degree fraction | 0.99591 | 0.99122 | +0.473% | +0.212 | 0.915 | 15.4% |

The large raw fixed-point difference is not a new anomaly: Hénon fixed points
are forced by the quadratic discriminant

\[
 \#\operatorname{Fix}(H_6/\mathbb F_p)
 =1+\left(\frac{28}{p}\right)
 =1+\left(\frac7p\right),\qquad p\ne2,3.
\]

At the first prime coefficient this has the sign of
\(\zeta(s)L(s,\chi_{28})\), not \(\zeta/L\); it does not determine higher
local coefficients.  The 16 controls per prime give a frozen screening rule,
not a calibrated hypothesis test.

Against the inappropriate uniform-permutation null, mean standardized effects
were $+38.802$ for cycle count, $-2.884$ for largest-cycle fraction, and
$+44.624$ for short-point mass.  Their collapse under the matched
involution-product null shows why reversibility must be controlled explicitly.

### C05 finite-section control slice

| Variant | maximum prescribed-point drift at $s=0.5,\vartheta=1$ | ratio to Maslov/action |
|---|---:|---:|
| orientation fallback | $9.943\times10^{-15}$ | 0.223 |
| Maslov/action | $4.459\times10^{-14}$ | 1 |
| constant roof | $7.897\times10^{-13}$ | 17.7 |
| shuffled action | $1.085\times10^{-9}$ | $2.43\times10^4$ |
| random phase | $1.999\times10^{-9}$ | $4.48\times10^4$ |

These numbers establish finite-order cancellation only.  Coefficient-prefix
agreement is algebraic for a degree-truncated formal determinant, and the
simpler orientation character is at least as stable as the proposed Maslov
phase.

## 3. Findings

### Finding 1 — an explicit holomorphic sequence-domain theorem survives

**Observation.**  For

\[
 c=\frac{23}{48},\quad \rho=\frac7{48},\quad
 K_\varepsilon=\prod_i\overline D(\varepsilon_i c,\rho),
\]

the two allowed radicand disks are
\(\overline D(1/6,7/144)\) and
\(\overline D(47/144,7/144)\).  They lie in the right half-plane.  The
principal signed-square-root map strictly self-maps $K_\varepsilon$ with
margin at least $9.43718\times10^{-3}$ and contracts by at most
\(2/\sqrt{17}\).

**Interpretation.**  The real symbolic coding has a source-locked complex
sequence-polydisc extension.  This is stronger than a plot or a fitted
Möbius approximation.

**Implication.**  The former “missing complex domain” blocker is narrowed,
but not removed at the operator level.  A sequence-space fixed-point solver
is not yet a finite-dimensional graph-directed holomorphic branch system.

**Next test.**  First compare the proposed endpoint/pinning statements line by
line with Rugh and Baladi--Pujals--Sambarino.  Only if a quantitative \(H_6\)
delta survives should the project formalize a finite-window endpoint solver with
uniform boundary domains, exponential boundary-influence bounds, consistency
under extension and chronological two-coordinate gluing, and equivalence with
the already-proved cyclic solution.  The decisive paper gate is then an exact
finite-dimensional crossed/pinning-map composition theorem with a frozen
flat-trace weight.  Only afterward should graph-directed cylinder convergence
or nuclearity be tested.

### Finding 2 — finite-field reversibility is a false-positive mechanism

**Observation.**  For odd primes, with $R(q,r)=(r,q)$ and $I=H_6R$,

\[
 s_p=\frac{\#\operatorname{Fix}R+\#\operatorname{Fix}I}{2}=p,
 \qquad Z_p=Z_{p,\mathrm{sym}}Z_{p,\mathrm{pair}}^2.
\]

The same identities hold in the matched random-involution ensemble.

**Interpretation.**  Symmetric-cycle dominance and the excess of cycles over
an unrestricted random permutation are generic consequences of representing
the map as a product of two involutions.

**Implication.**  Raw local permutation factors do not supply a distinguished
arithmetic normalization.  Setting $u=p^{-s}$ also collapses two conceptually
different axes—dynamical iteration and Euler exponent—without a trace or
cohomological theorem.

**Next test.**  C03 remains stopped.  A legitimate revival must retain

\[
 N_p(r,n)=\#\operatorname{Fix}
 (H_6^n:\mathbb F_{p^r}^2\to\mathbb F_{p^r}^2)
\]

as a two-variable object and explain the Frobenius-extension index $r$ and
dynamical iterate $n$ before forming a global product.  Merely increasing
the prime cutoff is not informative.

### Finding 3 — the Maslov candidate collapses exactly

**Observation.**  On the certified survivor, $|q_i|\ge1/3$.  For
$n\ge2$, the cyclic action Hessian has diagonal $12q_i$ and off-diagonal
row radius at most 2.  The homotopy from the Hessian to its diagonal never
crosses zero.  The $n=1$ case is direct.  Therefore

\[
 \mu(\gamma)=\#\{i:q_i<0\},\qquad
 \mu(\gamma^r)=r\mu(\gamma).
\]

**Interpretation.**  The character
\((-i)^{\mu(\gamma)}\) is only a one-symbol locally constant potential, not a
new long-range periodic-orbit invariant.

**Implication.**  C05 fails BF1 distinctness as a new phase mechanism.  In
addition,

\[
 S\mapsto S+C
 \quad\Longrightarrow\quad
 D_C(z,s,\vartheta)
 =D_0(ze^{i\vartheta C},s,\vartheta),
\]

so a fixed-$z$ absolute root angle is not selected by the classical map.

**Next test.**  Do not spend more control budget on this fixed-$z$ candidate.
A gauge-covariant $z$-family or a quantum normalization principle would be
a new candidate requiring a new source lock.

## 4. Route-A screening

These are conservative **screening ceilings**, not schema-complete formal
evaluations.  The frozen experiment plan permits a Route-A YAML only after
BF3; no pilot reached BF3.  C02/C02B lacks a frozen operator input.  C02C
freezes unit time and a signed finite flat-trace denominator, but still lacks
an infinite operator, function space and normalization.  Consequently it is
formally `NOT_TESTABLE` at Route-A input validation; the tuple below is only an
informal layer ceiling.  Its `A4_FORMAL_HINT` derives from the inherited exact
symplectic Hénon structure and known quantization context, not from a
clock-preserving lift constructed by C02C.

| Candidate | Screening tuple | Overall | Reason |
|---|---|---|---|
| C02/C02B | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_EXPLORATORY` | exact orbit/projective/complex-domain infrastructure, but no prime-like mechanism or determinant |
| C02C | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_EXPLORATORY` | exact finite-window trace residue and chronology, but no infinite operator, normalization or arithmetic mechanism |
| C03 | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `ROUTE_A_REJECTED` | local exactness only; global mechanism absent and reversible null explains bulk signal |
| C05 | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` for the intrinsic fixed-$z$ phase claim | exact gauge obstruction and proved one-symbol Maslov collapse |

`route_b_invocation_allowed` is `false` for all candidates.

## 5. Reproducibility

Independent checks were run without target data:

- C02: clean temporary-directory regeneration; deterministic CSVs agree;
  all summary checks and independent checks pass.
- C02B: producer 14/14 and checker 18/18; clean temporary-directory rerun
  passes after making the checker path-portable.
- C02C: producer and independent Newton checker pass all frozen assertions;
  complete-ID, three tamper/truncation, scalar-average and reversed-order
  controls pass; the two worst binary64-conditioned cases pass 90-digit
  Newton rechecks.
- C03: 10/10 tests; independent tuple-state enumeration passes 54/54 local
  ledgers; an independent full run reproduced all deterministic data.
- C05: self-check passes; clean rerun is byte-identical; an independent
  Toeplitz-matrix exponential reproduced degree-20 determinant coefficients
  to $6.21\times10^{-17}$.

Canonical commands are listed in `code/README.md`.  This workspace has no Git
metadata; provenance uses frozen protocols, source hashes, deterministic
seeds, artifact hashes, and independent reruns.

## 6. Paper-selection ruling

No RH/HP paper is frozen.  WP0 and C02C are complete: the endpoint,
chronological gluing, matching/Hill and complex-projective statements are
proved as an effective complex \(H_6\) specialization.  The conjugate real
SFT/uniqueness and the qualitative complex pinning/absolute-Fredholm
mechanisms are prior art.  The decision is
`RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
NOVELTY_DELTA_UNCONFIRMED`.

The next gate is C02D's trace-compatible cylinder/operator approximation
theorem.  If that theorem is merely a routine specialization or cannot be
proved in a natural frozen norm, the lane returns to breadth-first generation
rather than polishing a duplicate.

## 7. C02C finite-window addendum

The frozen run audited 432 complete open center-endpoint cases, 120 complex
boundary probes and 120 complete cyclic words through length eight.  The
center and cyclic rows are persisted individually; the boundary count and
extrema are persisted in the certificate.  The run verified the exact theorem
package in `../DERIVATION_PACKAGE.md` and recorded the following worst metrics:

| Quantity | Maximum / minimum |
|---|---:|
| open recurrence residual | \(1.8274\times10^{-13}\) |
| high-precision crossed residual | \(5.2856\times10^{-80}\) |
| boundary derivative-bound ratio | \(0.541329\) |
| boundary disk margin | \(0.0102588\) |
| high-precision matching error | \(1.0763\times10^{-96}\) |
| high-precision Hill error | \(3.0949\times10^{-90}\) |
| direct/glued discrepancy | \(9.3980\times10^{-15}\) |
| scalar-average expected-fail residual | \(1.41130\) |
| reversed-monodromy expected-fail discrepancy | \(5631.07\) |

The raw binary64 forward crossed discrepancy
\(6.4354\times10^{-8}\) and Hill subtraction error
\(5.6445\times10^{-5}\) are retained as conditioning diagnostics.  Separate
90-digit Newton solves reduce the corresponding residual/identity errors to
\(1.85\times10^{-85}\) and \(7.85\times10^{-81}\), respectively.  This is a
precision correction for the same frozen objects and cases, not a change of
the protocol or theorem.
