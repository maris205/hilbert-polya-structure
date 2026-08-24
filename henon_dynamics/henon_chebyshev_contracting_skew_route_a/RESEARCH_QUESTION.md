# Research question — HCS-C126

## Primary question

Can one frozen, nontrivially recurrent Hénon-type skew dynamics support an
all-period theorem simultaneously covering complete real periodic-point
enumeration, unique fiber closure, primitive orbit counts, an orbit-owned
zeta, and exact stability/orientation/repetition laws?

## Falsifiable theorem obligations

1. Prove \(f^n=T_{3^n}\) for the base map \(f=T_3\), without inferring the
   statement from a finite composition prefix.
2. Prove that \(T_{3^n}(x)-x\) has exactly \(3^n\) *distinct real* roots.
3. Prove that every base fixed point has exactly one fiber coordinate fixed by
   \(F^n\), and that least periods are preserved.
4. Derive the exact-period and primitive-orbit formulas by Möbius inversion and
   derive the Artin–Mazur zeta from the resulting fixed counts.
5. Classify every fixed-point multiplier, orientation, and stability
   determinant and prove the primitive repetition law.
6. Show that changing the fiber multiplier to one or changing the base cubic
   to \(4x^3-2x\) destroys named parts of the theorem.

## Advancement criterion

This paper counts as progress only if the headline claims hold for every
period.  A table through a larger cutoff, one more low-period cycle, or the
formal degree of an iterate would not meet the criterion.

## Route boundary

Even a positive answer is assigned

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
route_b_invocation_allowed = false
```

because the all-period source atlas has no prime-like target semantics, the
Artin–Mazur zeta is not a weighted target-facing Fredholm determinant, and no
analytic completion or natural lift is supplied.
