# HCS-C03 frozen pilot protocol

Freeze time: 2026-08-05 UTC

Post-run mathematical erratum: the frozen text originally described the
first-coefficient character as a `zeta/L` head.  Since
\(1+\chi_{28}(p)\) is the first logarithmic coefficient of
\(\zeta(s)L(s,\chi_{28})\), the sign is corrected below.  This correction
changes no object, control, threshold, random seed, or pilot decision.

This file was written before the full (p\leq 251) census.  It fixes the
object, controls, diagnostics, and decision language so that none can be
chosen after seeing the prime-by-prime output.

## Object and exact conventions

- Integral map: (H_6(q,r)=(1-6q^2-r,q)).
- Local phase space: all of (mathbb F_p^2), with no orbit selection.
- Prime range: every prime (p\leq251).
- Bad reduction: (p=2,3), because the quadratic coefficient vanishes.
  Their exact factors remain in the ledger but are excluded from every
  cross-prime aggregate.  The good prime (p=7) is separately flagged
  because the fixed-point discriminant (28) vanishes.
- Primitive object: one cycle of the finite permutation (H_6/\mathbb F_p).
- Repetition law:
  \[
  \#\operatorname{Fix}(H_6^n)=\sum_{\ell\mid n}\ell c_{\ell,p}.
  \]
- Local zeta convention:
  \[
  Z_p(u)=\exp\!\left(\sum_{n\geq1}
      \frac{\#\operatorname{Fix}(H_6^n)}n u^n\right)
      =\prod_{\ell\geq1}(1-u^\ell)^{-c_{\ell,p}}.
  \]
- Stored fixed-point window: (1\leq n\leq64).  The complete sparse cycle
  ledger reconstructs every later fixed count exactly.
- Direct, cycle-independent fixed-point check: (1\leq n\leq12).
- No Riemann-zero data, target prime weights, fitted unfolding, or target
  comparison is permitted.

The inverse used for an exhaustive bijection check is

\[
H_6^{-1}(Q,P)=(P,1-6P^2-Q).
\]

## Intrinsic reversibility factorization

The fixed integral reversor is (R(q,r)=(r,q)).  With (I=H_6R), both
(R) and (I) are involutions and (H_6=IR).  Hence non-(R)-invariant
cycles occur in pairs.  Before seeing the data we declare the exact split

\[
Z_p(u)=Z_{p,\mathrm{sym}}(u)Z_{p,\mathrm{pair}}(u)^2.
\]

This is a factorization, not permission to discard the paired factor.  The
code verifies for every length that
(c_{\ell,p}=s_{\ell,p}+2t_{\ell,p}), and verifies the fixed-locus pattern
of every symmetric cycle.  It is the only candidate normalization admitted
in this pilot.  Dividing by a fitted average, by a random factor, or by a
factor selected after looking across primes is forbidden.

## Controls

Master seed: `20260805`.  Replicates: `16` per prime and per ensemble.  A
documented SplitMix64 generator and unbiased Fisher--Yates shuffle make the
controls independent of NumPy and its version.

1. `uniform_permutation`: a uniform random permutation of (p^2) labels.
2. `matched_reversible`: keep the coordinate-swap (R), sample uniformly an
   involution (I_*\) with the same fixed-point cardinality as (H_6R), and
   use (I_*R).  This removes the leading effect of being a product of two
   involutions.  It does not match polynomial degree or algebraic geometry.

The second ensemble is essential: deviation from an unrestricted random
permutation alone is not evidence for arithmetic structure.

Roberts--Vivaldi's random-involution model is a hard literature boundary for
interpretation (arXiv:0905.4135).  In particular, normalized cycle laws,
predominantly symmetric cycles in the relevant asymptotic regime, and
Poisson-type repeated-cycle statistics are null predictions for compositions
of involutions.  None is an anomaly here.  Only a cross-prime structure that
survives the matched fixed-point involution-product control can pass the
empirical gate.

## Predeclared bulk diagnostics

At each prime, with (N=p^2) and short-cycle threshold (L=p), record:

1. total cycle count (K), including its exact uniform-permutation harmonic
   mean/variance z-score;
2. fixed-point count;
3. largest-cycle fraction;
4. fraction of points in cycles of length at most (p);
5. number of (R)-symmetric cycles;
6. fraction of points in the symmetric zeta sector;
7. paired-sector base degree and the identity
   (\deg Z_{\rm sym}+2\deg Z_{\rm pair}=p^2);
8. the exact fixed-point prediction from (6q^2+2q-1=0), including the
   Legendre symbol of (28) at good primes.

The eighth item is a forced arithmetic head term, not a discovered anomaly.
For every good (p\ne7),

\[
\#\operatorname{Fix}(H_6/\mathbb F_p)
 =1+\left(\frac{28}{p}\right)
 =1+\left(\frac{7}{p}\right),
\]

and (p=7) gives the double-root case.  Thus any later global proposal must
state in advance whether it retains or removes the corresponding formal
\(\zeta(s)L(s,\chi_{28})\)-type \(n=1\) head.  Observing this character in the census
cannot promote the candidate.

For each numerical diagnostic, the map is compared with the prespecified
control mean, standard deviation, empirical 2.5/50/97.5 percentiles, and
range.  Good-prime aggregate summaries report mean standardized effect,
median and mean absolute effect, sign consistency, and the fraction outside
the empirical control interval.  No subset of residue classes may be chosen
after the run.

## Frozen kill and promotion language

- `RUN_INVALID`: any failure of bijectivity, the inverse formula,
  reversibility, point totals, fixed-count identities, cyclotomic degree, or
  the symmetric/paired factorization.
- `UNRESTRICTED_RANDOM_REJECTED_ONLY`: deviations from the uniform control
  disappear under the matched-reversible control.  This is a reversibility
  effect, not an arithmetic promotion.
- `NO_BULK_ANOMALY`: for every matched-control primary diagnostic, the
  good-prime mean absolute standardized effect is below 1 and no more than
  20% of primes lie outside its empirical 95% interval.
- `CANDIDATE_NONRANDOM_SIGNAL`: at least one matched-control primary
  diagnostic has absolute mean standardized effect at least 2, a common sign
  on at least 75% of valid good primes, and an outside-interval rate at least
  50%.  This is only a signal to explain; it is not a local-to-global theorem.
- `LOCAL_FACTORS_ONLY`: exact local factors exist, but no canonical global
  Euler product, common convergence theorem, continuation, or divisor has
  been established.  This is the default Route-A ceiling of the pilot.

No bulk threshold alone promotes C03.  Promotion requires an exact,
prime-stable relation not exhausted by (i) the fixed-point discriminant,
(ii) reversibility, or (iii) generic finite-permutation identities, plus a
separately justified global construction.  Otherwise the correct output is a
negative obstruction or a reusable local arithmetic ledger.

There is also a frozen conceptual gap: substituting (u=p^{-s}) in (Z_p(u))
identifies the dynamical iterate (n) with the Euler exponent (p^{-ns}).
No natural cohomological, sheaf-theoretic, or trace-formula explanation for
that diagonal binding is presently known.  A numerically convergent truncated
product would not close this gap.
