# C166 two-round internal improvement log

## Round 0 baseline

- Preserved as `paper/main_round0_original.pdf`.
- Introduced the high-dimensional tower and the Pascal iterate formula.
- Stated the candidate clock and period ledger, with the valuation necessity
  proof and operator reversal left for review.

## Round 1

- Preserved as `paper/main_round1.pdf`.
- Replaced finite-prefix language by the all-parameter fixed-point iff.
- Added the sufficiency bound
  `v_2(binomial(n,k))>=v_2(n)-v_2(k)`.
- Added the explicit necessity witness `k=2^(b+1)` and explained why its
  auxiliary binomial factor is odd.
- Derived primitive cycles and the exact Artin--Mazur zeta, while leaving the
  antiunitary implementation for the final round.

## Round 2

- Preserved as `paper/main_round2.pdf`, byte-identical to `paper/main.pdf`.
- Added the unit argument showing that the fixed-point condition is
  independent of the state.
- Added the complete truncated-ring proof that
  `sigma(t)=-t/(1+t)` is involutive and reverses multiplication by `1+t`.
- Added the same-clock Koopman determinant and antiunitary identity.
- Recorded the two-dimensional-shear pivot and explicitly removed any
  complexity, target, arithmetic, or Route-B promotion.
- Expanded independent recurrence, SymPy, replay, mutation, deterministic
  build, font, and rendered-page receipts.

Both rounds were internal artifact review, not external peer review.

## Post-round hostile audit repair

- Restricted the displayed binomial-valuation inequality to
  `1<=k<=n` and stated separately that `k>n` coefficients vanish.  This
  removes an implicit `v_2(0)` convention without changing the theorem or its
  witnesses.
