# Round 2 proof audit

## Provenance and release posture

**Provenance:** same independent cross-agent reviewer as Round 1.  The
requested GPT-5.4 child remained unavailable because of the structural thread
cap; this report does not claim GPT-5.4 provenance.  External release remains
**HOLD**, and no priority conclusion is made.

## Verdict and score

**Verdict:** **INTERNAL THEOREM PASS WITH TWO MINOR NOTATION EDITS.**

**Score:** **9.0/10** after Round 1 revision.

The revised Section 5 now proves Bowen entropy in Bowen’s variable-length
Carathéodory sense.  The cylinder geometry, type-cover upper bound, Bernoulli
local-entropy lower bound, conditional maximum, and Legendre endpoints form a
complete chain.  Two symbols should be defined more explicitly, but no
formula or theorem needs narrowing.

## Round 1 closure audit

1. **M1 closed.** At scale `2^-M`, the manuscript proves the exact equality
   between an `n`-Bowen ball and the cylinder fixing `[-M,-1]` plus
   `[0,n+M-1]`.  The past and terminal-future factors are independent of `n`.
2. **Carathéodory upper bound closed.** Exact-average sequences are a
   countable union of eventually eta-controlled sets.  Type cylinders at
   arbitrarily large lengths make the variable-length sum vanish above
   `H_(alpha,eta)`; compactness closes `eta -> 0`.
3. **Lower bound closed.** A fixed-past/Bernoulli-future law gives full mass
   to a feasible generic level, and its Bowen-ball local exponent is `H(p)`.
4. **Natural-extension bridge closed.** Finite-dimensional inverse-limit
   distributions give the unique affine lift, and generating partitions give
   entropy equality.
5. **Periodic alignment closed.** The negative coordinate formula fixes the
   cyclic phase and yields the displayed degree product.

## Independent proof trace

### Pressure and rigidity

- The preimage count is exactly `k_(x_-1)`.
- The natural extension records each forgotten symbol and is the full
  two-sided `S`-shift; the lifted potential is one-coordinate.
- Arbitrary invariant measures satisfy entropy rate at most one-symbol
  entropy.  Gibbs equality forces the stated marginal, and entropy-rate
  equality forces Bernoulli independence.
- Conjugacy preserves local degree and fixed points, so the degree-`k`
  fixed-point count `k m_k` recovers multiplicities.
- Equal profiles give the explicit coordinatewise conjugacy.  Equal pressure
  curves give finite exponential sums, whose largest base and coefficient are
  recursively recoverable.

### Multifractal spectrum

- The orbit sum differs from the future digit sum by one uniformly bounded
  term.
- The exact Bowen-cylinder equality is correct under the stated product
  metric: later negative windows see no old coordinate deeper than `-M`, and
  crossed future symbols are already fixed before applying `tau`.
- Type counts provide the stated polynomial prefactor and constrained Shannon
  exponent.
- The Bernoulli local cylinder exponent is `H(p)` even when `p` has zeros,
  because typical words stay in its support.
- Conditional entropy is maximized by uniform mass within each fibre, giving
  `H(r)+alpha`; Gibbs duality gives the pressure Legendre transform, including
  endpoint limits.

## CRITICAL issues

None.

## MAJOR issues

None.

## MINOR issues

### m1. Define the metric value at equality explicitly

After `N(x,x)=infinity`, add the convention `2^(-infinity)=0`; otherwise the
formula for `rho(x,x)` relies on an implicit extended-real convention.

### m2. Name the lower-bound probability

The lower proof writes `Prob(B_n(...))` after describing a
fixed-past/Bernoulli-future law.  Denote this law by `nu_p` and write
`nu_p(B_n(...))`; this removes any ambiguity with the global macro `Prob`.

## Source and ownership recheck

The direct-owner statements were checked against the current primary texts:
Lamei--Mehdipour for the zip map/local-homeomorphism and periodic setting;
Martins--Mattos--Varão Theorems A--B for the Bernoulli metric/folding
entropies; Mehdipour--Jangjooye Shaldehi for uniform full zip shifts; and
Bowen for noncompact-set entropy.  The arXiv version of the direct owner is
now present in the bibliography.  The active-neighbor audit still requires
external release to remain HOLD.

## Control and build audit

- Deterministic pressure/periodic/profile/spectrum controls: PASS.
- Round-1 build: 9 A4 pages.
- Log warnings/undefined references/undefined citations/box warnings: zero.
- The numerical spectrum checks do not substitute for the repaired
  Carathéodory proof; they are correctly labeled regression evidence.

## Release recommendation

**INTERNAL GO AFTER m1--m2 / EXTERNAL HOLD.** Apply the notation edits, rerun
controls and build, freeze Round 2, and retain the specialist-source hold.
