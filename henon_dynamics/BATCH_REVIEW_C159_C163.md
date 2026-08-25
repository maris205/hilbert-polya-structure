# Batch review: HCS-C159--HCS-C163

Date: 2026-08-25

System family: five separate Route-A dynamical advances under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five papers as explicit theorem progress,
continue Route A, and keep Route B unauthorized**.

## Completed paper outputs

1. **C159** replaces the rejected clock-decorated Sturmian vacuum by a
   recurrent Thue--Morse S-gap renewal shift.  The allowed zero gaps are
   `S={s>=0:t_s=1}`, so the code lengths include two and three.  Boundary
   completion proves topological mixing; boundary-aligned repetitions give
   dense periodic points, and a nested repeated-block construction gives a
   recurrent dense orbit.  Unique circular parsing yields

   ```text
   F(z)=z*T(z),
   P(z)=product_(j>=0)(1-z^(2^j))=1/(1-z)-2*T(z),
   zeta_X(z)=1/((1-z)(1-F(z)))
            =2/(2-3z+z(1-z)P(z)).
   ```

   The entropy root has the certified rational bracket
   `0.67633710444063914<R<0.67633710444063915`.  Radial zeros at the dense
   dyadic roots and exact recovery of `P` from the zeta prove that the source
   meromorphic continuation has the unit circle as a natural boundary.
2. **C160** upgrades the C155 all-proper-clock union bound to an exact
   maximal-subgroup sieve on every Mersenne circumference `L=2^r-1`.  If
   `P(L)` is the set of distinct prime divisors of the finite source clock,
   then

   ```text
   {v:per(v)<L}=union_(p in P(L)) Fix(g^(L/p)),
   intersection_(p in Q) Fix(g^(L/p))=Fix(g^(L/product_(p in Q)p)).
   ```

   Polynomial-gcd fixed dimensions therefore give exact inclusion--exclusion
   and Bonferroni bounds for every `L`.  When `L>3` is prime, the period
   support is exactly `{1,L}`, zero is the unique fixed state, there are
   `2^(L-1)-1` exact-period states and `(2^(L-1)-1)/L` primitive cycles, and
   the short-period probability is exactly `2^(-(L-1))`.  No infinitude of
   Mersenne primes is assumed or claimed.
3. **C161** records and rejects the proposed Heisenberg all-iterate local
   product because its quotient coordinates, translation removal, and
   degenerate `2`- and `5`-primary equivalences were not proved.  The
   replacement system is the odd cyclic rotation `R_q(x)=x+1` with quadratic
   observable `a*x^2+b*x`.  Its `n`-step phase is

   ```text
   A_n=a*n,
   B_n=a*n*(n-1)+b*n,
   C_n=a*n*(n-1)*(2*n-1)/6+b*n*(n-1)/2.
   ```

   With `d=gcd(A_n,q)` and `Q=q/d`, the complete amplitude vanishes exactly
   when `d` does not divide `B_n`; otherwise it has the exact Jacobi sign,
   `epsilon_Q`, magnitude `d*sqrt(Q)`, and completed-square phase, including
   the separate constant `Q=1` branch.  For every odd prime and nondegenerate
   quadratic branch, the zero level has `1+(Delta/p)` points.  In the pure
   quadratic case `p>=5`, `Delta=n^2(1-n^2)/3`, with the branches
   `n congruent to 0,+/-1 modulo p` stated explicitly.  On `ell^2(Z/qZ)`,
   the same-clock owner is `Tr(U_phi^n K^(-n))`; the involutive antiunitary
   `Theta=D_((a-b)x^2) P J` sends `U_phi` to `U_phi^(-1)`.
4. **C162** extracts a canonical coefficient from the complete Dirichlet
   square-billiard Abel half-wave trace, rather than from an isolated formal
   branch.  For every `N>=1`, with `t_N=2*sqrt(N)`, it proves

   ```text
   lim_(epsilon->0+) epsilon^(3/2) W_D(epsilon-i*t_N)
     =exp(i*pi/4)*r_2^src(N)/(8*pi*N^(1/4)),
   ```

   and obtains the complex conjugate at negative time.  A finite nonmatching
   shell split and uniform two-dimensional `|m|^(-3)` domination justify the
   full infinite trace limit.  If `N` is a square, the coincident boundary
   subtraction is only a simple pole, hence becomes `O(epsilon^(1/2))` after
   normalization and vanishes.  The coefficient counts the complete source
   shell, including signs, axes, collisions, and repetitions.
5. **C163** resolves the phase question left open by C158.  For the two
   normalized surviving one-site phases and their ratio `r`, it proves

   ```text
   r+r^(-1)=(sqrt(3)-sqrt(111))/6,
   3*x^4-19*x^2+27=0.
   ```

   The primitive irreducible integer polynomial is distinguished from the
   monic rational minimal polynomial
   `x^4-(19/3)x^2+9`; its nonintegral coefficient proves that `r` is not a
   root of unity.  The multiplicity-weighted full-cycle phase measure obeys

   ```text
   mu_hat_k(m)=u_-^(m*k)*((1+r^m)/2)^k,
   ```

   so every fixed nonzero Fourier mode decays exponentially and the measures
   converge to Haar measure.  Jointly, the centered square-root-`k`
   log-modulus fluctuation and phase converge to a Gaussian--Haar product.
   The moved-hole order-four branch remains an exact torsion control.

## Uniform release audit

All five deterministic producers, producer-independent checkers, separate
SymPy reconstructions, canonical byte replays, and hostile mutation suites
pass on the released bytes:

- C159: 742 checker assertions, 118 symbolic checks, and 46/46 hostile
  rejections;
- C160: 186 checker assertions, 100 symbolic checks, and 47/47 hostile
  rejections;
- C161: 483,310 checker assertions, 15,834 symbolic checks, and 30/30 hostile
  rejections;
- C162: 1,988 checker assertions, 9 symbolic checks, and 24/24 hostile
  rejections;
- C163: 646 checker assertions, 170 symbolic checks, and 95/95 hostile
  rejections.

The batch totals are **486,872 checker assertions, 16,231 symbolic checks,
and 242/242 rejected hostile cases**.  The hostile split is 237 repaired-hash
semantic/schema mutations plus five stale-hash controls.  An additional
read-only internal C161 audit checked 166,649 composite odd-modulus Gauss
cases, 33,866 finite matrix/antiunitary identities, and 3,188 prime
pure-quadratic root-count cases.  This was internal adversarial validation,
not external peer review or a claim of an independent error process.

Every release manifest has an exact 27/27 payload ledger with no missing,
extra, or hash-mismatched file.  Each package therefore has 28 physical
release files including its self-excluded manifest, for 140 physical files in
the batch.  All five Route-A YAML records parse, contain the required
evaluator inputs, use only allowed evidence labels, and retain
`route_b_invocation_allowed=false`.  No Python cache, bytecode, LaTeX
auxiliary, log, recorder, intermediate snapshot build, or build-cache artifact
remains.

Fresh isolated fixed-epoch double builds reproduce all five checked-in PDFs
byte for byte.  The ten rendered A4 pages use embedded fonts and show no
clipping, collision, truncation, malformed formula, missing glyph, blank
page, or unreadably small text.  Final fresh-build logs contain no warning,
overfull/underfull box, missing-glyph, undefined-reference/citation, or
multiply-defined-label message.  Every paper contains independently phrased
English and Chinese abstracts, six or seven keywords in each language, and
data, ethics, contribution, conflict, funding, and AI-use declarations.  The
round-zero, round-one, and round-two PDFs are content-distinct in every
package, and each `main.pdf` is byte-identical to its round-two snapshot.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C159 | `aa9884a34e283c347481f40c66c67042295ecc8345306588ad6eb72c9b92a62a` | `1eb08405e11870017c9ef448fa2c14cb5b93a53916b09421d5e46c0741c6ab5c` | `f5da54dabe93dc62b33c0affdbdf8b4702a9caead17a6948cf041ce8d4650150` |
| C160 | `a9232e4d8b795aa211a11dfb39dd862ee9345262aed457bbf6719ab96f468a72` | `cd4df138379fd4b689ac749337abebf785f1a42a32164842dbc84a9d2c29d7c5` | `f2e7200ec159f3fd9caa0fb5ac7ca77e83b7315db97a32faef854307bfc57a69` |
| C161 | `83aa29f3cfb2e148f7382407bf6718da3cad85e3bf9327309f4ddaafba06f236` | `7a99b240ff6e2446a5fd97f42300314c6e9607d10add5ea76a1cab03cd0446b5` | `5e79fcc5ae69720e008e3e336650dfb17f86baf8d9e8dfa2a0dd6c162f943e23` |
| C162 | `1a2cf270689cd73d6c77643c76e0e781ede9c401189a8be9f3bcbf2741653161` | `1bbae9d35ac4d54f97f76a020ef1ed85ae1f87d9df9d41cb2faf27394ada19e6` | `b5fab9857f6d5927e4ce2dcf9e67c162ae65b613a66fe760632406ae35300b2c` |
| C163 | `b32bec233e3865aa73fecfb2119902fe8111370c58aea96666ba497fee4a0f19` | `51ee28b93e7d7f88cc6e287398f065f8a1d9829d9c92fa1254786658d9e534b8` | `7d7dd26c1b1059270e91dd164137947ba997054bce366afe12e4faefbb15afd6` |

## Internal cross-review and repair ledger

The reviews below were evidence-anchored internal theorem, scope, and release
audits.  They were not external peer review and do not claim reviewer or
error-process independence.

- C159 rejected the initial periodic-vacuum-adjacent candidate, supplied the
  boundary-completion proof of mixing and the all-zero-cylinder periodic
  witness, made the circular parse behind `-log(1-F)` explicit, and exposed
  the exact recovery of `P` used in the natural-boundary transfer.
- C160 added the bridge from a full-ring fixed vector to the periodic image,
  proved the fixed-space intersections at gcd clocks, isolated the `L=3`
  identity exception, and replaced ambiguous multiplier language by the
  direct kernel equation.  A separate read-only hostile audit found no proof
  gap.
- C161 stopped the unsupported Heisenberg extension, hardened every nested
  claim-bearing evidence field, added the `Q=1` branch and `p>=5` restriction,
  corrected all special cases to congruences modulo `p`, and added the
  explicit antiunitary reversal.  Early identical snapshot PDFs were rejected;
  the released three stages contain genuine mathematical and scope changes.
- C162 promoted a single matching summand calculation to a full-trace theorem
  by adding uniform tail domination, negative-time conjugation, and the exact
  coincident-simple-pole expansion.  The shell ledger was kept as a sentinel,
  and the two-page proof was rebalanced with the missing proof receipts.  A
  separate read-only hostile audit found no proof gap.
- C163 corrected an early terminology conflation: `3x^4-19x^2+27` is the
  primitive irreducible integer polynomial, whereas
  `x^4-(19/3)x^2+9` is the monic rational minimal polynomial.  The checker and
  mutation suite were expanded over the algebraic-integrality and moved-hole
  controls before final deterministic rebuild and debris removal.

## ARS Stage 2.5 failure-mode audit

This is the pre-manuscript integrity checkpoint applied after theorem and
evidence construction.

1. **Implementation bug passing self-review: CLEAR.**  Producer-independent
   exact reconstruction, SymPy, replay, mutation, and separate hostile proof
   audits exposed the fixed-kernel receipt, C161 antiunitary/schema gaps, and
   C163 polynomial terminology before release.
2. **Hallucinated citation: CLEAR.**  No external citation, bibliography, or
   literature-derived numerical claim enters the five theorem paths; imported
   source conventions are stated directly.
3. **Hallucinated result: CLEAR.**  Every finite ledger is canonically
   generated and separately reconstructed.  Every all-parameter conclusion is
   supported by a proof rather than extrapolated from the ledger.
4. **Shortcut reliance: CLEAR.**  Period-18, finite-ring, shell-800, and
   finite-`k` calculations are explicitly regression sentinels, not theorem
   cutoffs.
5. **Bug reframed as insight: CLEAR.**  The two rejected candidates, C160
   proof wording, C161 special-case/A4 additions, snapshot defect, and C163
   polynomial correction are recorded as repairs or pivots.
6. **Methodology fabrication: CLEAR.**  Review is reported only as internal
   artifact-level review; no unavailable external reviewer, acceptance score,
   cross-model independence, or unperformed experiment is claimed.
7. **Early frame-lock: CLEAR.**  Failure of an initial model triggered an
   explicit dynamics pivot in C159 and C161.  The other three systems retain
   their negative controls, and no theorem is forced into a target-facing
   promotion.

## ARS Stage 4.5 failure-mode audit

This is the final artifact and manuscript checkpoint, separate from Stage
2.5.

1. **Implementation bug passing self-review: CLEAR.**  Final released bytes
   pass 486,872 checker assertions, 16,231 symbolic checks, 242 hostile cases,
   five byte replays, and the additional C161 internal hostile sweeps.
2. **Hallucinated citation: CLEAR.**  Final PDFs contain no bibliography or
   unsupported attribution; source ownership and imported conventions remain
   explicit.
3. **Hallucinated result: CLEAR.**  Displayed finite values agree with the
   content-addressed evidence, while evidence, PDF, and manifest hashes were
   independently recomputed in the batch audit.
4. **Shortcut reliance: CLEAR.**  Manuscripts visibly separate theorem ranges
   from finite sentinels, floating error indicators, and matched controls.
5. **Bug reframed as insight: CLEAR.**  All release-relevant corrections are
   preserved in the two-round improvement logs and the cross-review ledger.
6. **Methodology fabrication: CLEAR.**  Commands, source locks, tests,
   manifests, declarations, deterministic builds, and AI-use disclosures are
   present; internal review is not represented as external peer review.
7. **Early frame-lock: CLEAR.**  Final tuples remain conservative, every
   package retains its obstruction, the five coordinates remain separate, and
   Route B remains disabled.

## Route-A assessment

The strict tuples are:

```text
C159 (A1_WEAK,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)
C160 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C161 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C162 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C163 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

All five are `ROUTE_A_EXPLORATORY`.  C161's finite weighted-Koopman
quantization, C162's Dirichlet half-wave operator, and C163's finite
subunitary scattering gate belong to distinct source systems and are not
combined.  C159's partial analytic structure is a source natural-boundary
theorem, not a target continuation claim.  No package freezes or compares a
target zero census, target divisor, target functional equation, target
counting law, arithmetic local datum, Euler factor, root number, automorphy
object, or Hilbert--Polya operator.  Every package has
`route_b_invocation_allowed=false`.

## Next gate

The next five-paper round, if explicitly confirmed, should again require one
new all-parameter theorem per paper and preserve subtype diversity.  Promising
directions include an operator owner for a recurrent symbolic natural-boundary
system, a composite-clock Rule-90 exact-period distribution beyond the
prime-circumference law, a genuinely different affine or higher-dimensional
finite rotation model, a billiard geometry whose clean-shell coefficient
changes under a controlled deformation, and an open quantum-map phase law
beyond the frozen two-phase binomial reduction.  Any candidate that cannot
close its proof gate should change dynamical model and record the pivot.
Target-facing comparison remains a separately frozen protocol requiring
explicit authorization.
