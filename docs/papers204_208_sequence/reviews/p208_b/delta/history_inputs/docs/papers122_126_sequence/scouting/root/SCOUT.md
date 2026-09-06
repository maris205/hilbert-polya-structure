# Root/cross-family breadth scout for P122--P126

> **Post-scout decision:** X01 was killed by the independent value/collision
> gate because it resurrects the P102-round balanced-divisor tent and remains
> a mechanical sign-quotient doubling realization.  The correct formulas are
> archived, but X01 cannot receive a paper number.

**Status:** sixteen literal systems screened; one conditional proof-spike
leader, two narrow reserves, thirteen kills.  No paper number is frozen.  
**Date:** 2026-08-30.  
**External status:** `HOLD_EXTERNAL`.

This lane deliberately searched outside the three specialist lanes.  It
tested arithmetic divisor lattices, histogram descents, comparator systems,
and quotient encodings.  A search non-hit is bounded evidence only and is not
a novelty or priority statement.

## Sixteen-system ledger

| ID | literal update | early signal | intake decision |
|---|---|---|---|
| X01 | on `d|N`, send `d` to `lcm(d,N/d)/gcd(d,N/d)` | every prime exponent follows an integral tent map; exact pointwise tails/periods, fixed counts and all depth layers | **CONDITIONAL PROOF SPIKE** |
| X02 | on `d|N`, send `d` to `d/gcd(d,N/d)` | clipped doubling has a closed absorption clock | reserve behind X01; same carrier and weaker recurrence |
| X03 | on `d|N`, send `d` to `lcm(d,N/d)/d` | reflected clipped doubling, with only one fixed point plus a two-cycle locally | reserve behind X01; same carrier |
| X04 | replace an integer partition by its sorted positive multiplicities | depth thresholds `2,3,4,7,14,42,...` | kill: multiplicity/inventory dynamics has direct owners |
| X05 | replace a set partition by the multiplicities of its block sizes | weighted frequency fibres | kill: X04 engine with Stirling decoration |
| X06 | replace a graph by the canonical partition of its degree multiplicities | collapses graph structure in one round | kill: frequency-partition statistic, not graph dynamics |
| X07 | replace a functional digraph by the multiplicities of its indegrees | inventory cycles after one projection | kill: direct inventory engine |
| X08 | replace a hypergraph by the multiplicities of its edge sizes | one-step loss of incidence data | kill: theorem-thin histogram |
| X09 | on a divisor pair, apply `(gcd,lcm)` | idempotent sorting | kill: lattice comparator background |
| X10 | apply odd/even parallel gcd--lcm comparators to a divisor word | finite sorting-network clock | kill: comparator-network mechanism, no new residual |
| X11 | cyclically apply all overlapping gcd--lcm comparators | small periods depend on the update convention | kill: fragile scheduling variant |
| X12 | send `d|N` to `gcd(d,N/d)` | one-step projection below every half exponent | kill: idempotent after one further round |
| X13 | send `d|N` to `N/gcd(d,N/d)` | one-step projection to a unitary-side interval | kill: endpoint-only lattice formula |
| X14 | rotate and renormalize Euclidean remainder vectors | Euclidean quotients are the complete clock | kill: direct Euclidean-algorithm owner |
| X15 | iterate the multiplicity sequence of cyclic gap lengths | inventory dynamics after forgetting positions | kill: X04 plus a cosmetic cyclic encoding |
| X16 | iterate numerical-semigroup blowup multiplicities | the classical multiplicity sequence is the orbit | kill: named numerical-semigroup owner |

## X01 exact signal

Write

```text
N = product p_i^a_i,    d = product p_i^e_i.
```

Then X01 is coordinatewise

```text
f_a(e) = |2e-a|.
```

Under `y=a-e`, this becomes `y -> 2 min(y,a-y)`, the quotient of doubling
on `Z/(2a)` by sign.  For `y>0`, set

```text
M = 2a/gcd(y,2a) = 2^alpha m,   m odd.
```

The bounded evidence supports the exact contract:

1. the preperiod is `alpha`;
2. the eventual period is the least positive `k` with
   `2^k = +1 or -1 (mod m)`;
3. `Fix(f_a^n) = (gcd(2^n-1,2a)+gcd(2^n+1,2a))/2`;
4. if `R=v_2(2a)`, the number of states of preperiod at most `t<R` is
   `floor(a/2^(R-t))+1`, and all `a+1` states have preperiod at most `R`;
5. on the full divisor lattice, preperiods take coordinatewise maxima,
   eventual periods take least common multiples, and fixed counts and
   cumulative depth counts multiply.
6. every iterated local fibre is given explicitly by the dyadic kernel size,
   with separate zero and order-two quotient classes; product fibres
   multiply.

The period-two orbit for `(a,e)=(5,1)` kills the naive claim that all proper
divisors absorb.  Its period is two although `ord_5(2)=4`, so it also forces
the sign quotient rather than an unsigned multiplicative-order formula.

The canonical pilot exhausts literal integer arithmetic, all local states
through `a=128`, 238 exponent profiles, 15,659 product states, fixed iterates,
depth layers, every iterated local fibre, and Möbius exact-period
reconstruction.  It passes **348,392
exact assertions**; the stored stdout is byte-stable.

## Owner and collision subtraction

The arithmetic expression itself is already public: OEIS A332618 records the
aggregate `sum_(d|N) lcm(d,N/d)/gcd(d,N/d)`, including its prime-power and
Dirichlet-series formulas.  The expression, its multiplicativity, and those
aggregate formulas receive zero candidate credit.  The full-height tent map
and its symbolic/radix dynamics are classical and
receive zero candidate credit.  In particular, Scheicher--Sirvent--Surer,
*Dynamical properties of the tent map*, JLMS 93 (2016),
DOI `10.1112/jlms/jdv071`, is an explicit modern owner for the tent-map
side.  Unitary divisors, gcd/lcm as the divisor lattice meet/join,
multiplicative orders, Möbius recovery of exact periods, and product-map
bookkeeping also receive zero credit.

A bounded literal search for iteration of the arithmetic update and its
complete divisor-lattice functional graph found no direct match beyond that
static OEIS aggregate.  The only potentially defensible residual is therefore
the exact conjunction of the natural complementary-divisor update with:

- the sign-quotient pointwise orbit formula;
- all product-lattice transient layers;
- fixed and exact-period counts for every iterate; and
- explicit separation from P100 digit erasure and P107 ideal dynamics.

This residual may still be judged mechanical because the exponent map is a
classical tent map.  X01 must therefore pass a hostile owner/value gate before
it can receive a paper number.

## Recommendation

Advance only X01 to an all-parameter proof spike.  X02 and X03 remain controls
for the same carrier and cannot occupy separate papers.  The remaining
systems are permanently killed in their literal forms.
