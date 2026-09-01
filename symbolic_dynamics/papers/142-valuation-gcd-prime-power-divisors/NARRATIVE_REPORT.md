# P142 narrative report

Status: `ANONYMOUS ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL`.

## Core story

Fix an odd prime `p` and an exponent `e>=2`.  On the divisors of `p^e`,
iterate the literal arithmetic map

```text
F(d) = gcd(p^e, d^2 + p^e/d).
```

Writing `d=p^a` converts this map exactly into

```text
T_e(a) = min(2a,e-a).
```

The conversion is not merely notation: when the two summands have equal
valuation, their unit sum is `2`, so oddness of `p` is essential.  Once the
literal identity is established, the finite dynamics has two inverse
branches and a rigid doubling/reflection geometry.  The paper determines the
whole recurrent set, every fixed-iterate count, every pointwise entry time,
the unique deepest divisor, the complete temporal polynomial, the image, and
the fibre over every target.

## Proof spine

1. **Literal valuation.**  Factor
   `p^(2a)+p^(e-a)` by the smaller power.  Unequal valuations leave a unit
   `1+p^k`; equal valuations leave the unit `2` because `p` is odd.  This
   proves the exact gcd identity.  For `p=2` and `e=3a`, the valuation rises
   from `2a` to `2a+1`, with `(e,a)=(3,1)` the smallest failure.
2. **Invariant band.**  Put `L=ceil(e/3)` and `U=floor(2e/3)`.  Below `L`,
   the map doubles.  On `[L,U]`, it complements `a` to `e-a`, and above `U`
   it reflects in one step to `[0,L-1]`.  Hence the recurrent set is exactly
   `{0} union [L,U]`; its nonfixed recurrent states form complement pairs.
3. **Pointwise clock.**  A lower state enters the band when its first doubled
   value reaches `L`.  An upper state first reflects to the lower state
   `e-a`.  This gives the four-case entry-time law.  The upper state `e-1`
   is the unique state with the maximal doubling distance when `e>=4`; the
   small cases `e=2,3` have unique deepest state `e`.
4. **Temporal census.**  Lower states of depth `j` are the integers in one
   exact dyadic interval, counted by a difference of two ceilings.  Each has
   one reflected partner of depth `j+1`, while `e` supplies the remaining
   depth-one state.  This yields the entire temporal polynomial.
5. **Every-target inverse.**  Solving `2a=b` and `e-a=b`, with the correct
   branch inequalities, gives the image `[0,U]` and the complete fibre set.
   The two solutions coincide exactly when `3b=2e`.

## Credit boundary

General valuation algebra, functional-graph and zeta bookkeeping, ceiling-log
identities, piecewise-monotone interval dynamics, and discretized tent maps
are established background and receive zero contribution credit.  In
particular, the real piecewise-linear map `x -> min(2x,1-x)` already displays
the same silhouette.  The narrow admissible residual is only the conjunction
of the literal odd-prime divisor map with its full arithmetic temporal and
inverse atlas.

The bounded owner search recorded in the algebraic scout did not locate the
literal gcd map or this theorem package.  That non-hit is not evidence of
novelty, priority, ownership, or freedom to operate.  If specialist review
finds that the divisor presentation is only a cosmetic encoding of the
piecewise-linear map, the residual must be killed rather than enlarged.

## Exact evidence and limitation

`verify_p142.py` uses exact Python integers, literal gcd computations, and no
sampling or floating point.  For each `p in {3,5,7,11}` and every
`2<=e<=128`, it constructs the complete functional graph and checks all
frozen formulas state by state.  It also checks every binary exponent
`2<=e<=48`, including all sixteen equal-valuation failures.  The frozen run
contains 319,074 assertions and ends with `STATUS=PASS`.

Finite enumeration is counterexample pressure only.  It cannot prove an
all-parameter theorem, establish source ownership, or authorize external
release.  External status remains `HOLD_EXTERNAL`.
