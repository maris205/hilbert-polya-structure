# Coordinator kill gate — common-factor-cancellation divisor tent

**Date:** 2026-09-03 UTC  
**Decision:** `KILL_INTERNAL_COLLISION_P142`  
**External state:** `HOLD_EXTERNAL`.

## Literal system and exact signal

For `d|N`, cancel the common factor from the complementary pair
`(d,N/d)` and multiply what remains:

```text
C_N(d) = N / gcd(d,N/d)^2.
```

Writing `N=prod p^e` and `d=prod p^a` turns the update into the independent
integer maps

```text
a -> |e-2a|,       0 <= a <= e.
```

This signal is mathematically clean.  If `e=2^s m` with `m` odd, the
recurrent exponents are exactly those with `v_2(a)=s`, the sharp scalar tail
is `s+1`, and the recurrent quotient is doubling on `Z/mZ` modulo sign.  In
particular

```text
#Fix(C_e^t) = (gcd(m,2^t-1)+gcd(m,2^t+1))/2.
```

For a general `N`, fixed-iterate counts multiply and the sharp tail is
`1+max_(p^e || N) v_2(e)`.  Every positive-time target fibre is also exact:
for one exponent it is the set of `0<=a<=e` satisfying

```text
2^t a = e-b or e+b  (mod 2e),
```

and therefore is a union of at most two explicit arithmetic progressions.
The multivariate source-divisor enumerator factors over the primes of `N`.

The verifier checks the triangle-wave iterate identity, pointwise and sharp
tails, recurrent set, fixed iterates, and all target fibres for every
`1<=e<=160`, plus eleven multi-prime boxes and literal big-integer gcds.

## Why the candidate is killed

P142 already occupies an arithmetic prime-power divisor map whose exact
valuation reduction is a finite two-branch tent map, together with complete
recurrent, fixed-iterate, pointwise-time, image, and every-target fibre
atlases.  The present map has a different scalar formula and adds a
multi-prime product, but its carrier, decisive valuation reduction, temporal
machinery, and inverse-branch engine transfer directly.  Those are the
coordinates that matter under the portfolio firewall.

Consequently the attractive modular-doubling classification does not rescue
this as a new paper system.  It is retained only as an exact negative and is
not eligible for P172--P176.  This internal collision decision makes no
novelty or ownership claim.
