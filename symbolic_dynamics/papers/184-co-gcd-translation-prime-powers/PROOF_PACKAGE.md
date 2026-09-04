# Proof package — P184

## Status

`PROVABLE AS STATED`

## Assumptions

- `p` is prime, `a>=1`, and `N=p^a`.
- States are the canonical integer representatives `0,...,N-1`.
- `T(x)=x+N/gcd(x,N) mod N`, with `gcd(0,N)=N`.
- `v_p(0)=a`; for nonzero representatives, `v_p` is the ordinary valuation.
- Tail means the least entrance time into a directed cycle.

## Notation

- A nonzero state is written uniquely as `x=p^v u`, with `p` not dividing `u`
  and `1<=u<p^(a-v)`.
- `d=p^floor((a-1)/2)` is the image defect.
- `D` and `Z` are respectively the explicit double- and empty-target sets in
  the manuscript.

## Proof strategy

Compare the valuations `v` and `a-v` of the two summands.  Low strata reduce
to translations of unit coordinates; high strata fall into low strata; the
equality stratum increments units.  Then invert those three restrictions and
count their images.

## Dependency map

1. The valuation comparison proves all pointwise tails and periods.
2. Stratum sizes divided by periods give the cycle census.
3. Counts of high and equality strata give the tail census.
4. Low bijectivity plus high injection gives all double targets.
5. Absence of a middle stratum for odd `a`, or its exact unit-shift image for
   even `a`, gives all empty targets.
6. Explicit set counts give the fibre histogram and image size.

## Proof

### Step 1: low valuation strata

For nonzero `x=p^v u`, the update is

`T(x)=p^v u+p^(a-v) mod p^a`.

When `2v<a`, divide by `p^v`.  On unit coordinates modulo `p^(a-v)`, the map
adds `p^(a-2v)`.  For `v>0` this increment is divisible by `p`, so unit status
is preserved; for `v=0` the increment is zero modulo `p^a`, with the same
conclusion.  Its additive order is

`p^(a-v)/gcd(p^(a-v),p^(a-2v))=p^v`.

Thus every low state is recurrent with exact period `p^v`.

### Step 2: high valuation strata and zero

When `2v>a`, factor the update as

`T(x)=p^(a-v)(1+p^(2v-a)u)`.

The parenthesis is a unit, so the next valuation is `a-v<a/2`.  Step 1 gives
period `p^(a-v)`.  The high initial state cannot recur after entering an
invariant low stratum, hence its tail is one.  Separately, `T(0)=1`, and 1 is
fixed; the same tail/period formula holds with `v_p(0)=a`.

### Step 3: the even-exponent equality conveyor

Let `a=2h` and `x=p^h u`, where `u` is a unit modulo `p^h`.  The unit
coordinate advances by one at each middle-layer step.  Put
`r=p-(u mod p)`.  For `0<=k<r`, `u+k` is a unit, while `u+r` is divisible by
`p`.  Therefore the first `r-1` images stay in the middle layer and the `r`th
image is high (possibly zero).

Let `s=v_p(u+r)`, allowing `s=h` when `u+r=p^h`.  The high landing valuation
is `h+s`.  One more step reaches low valuation `h-s`; for `s=h`, this is the
separate transition `0->1`.  Step 1 gives period `p^(h-s)`.  None of the
preceding middle/high states belongs to the low cycle, so the exact tail is
`r+1`.  When `p=2`, every unit is 1 modulo 2, hence `r=1` and the tail is two.

### Step 4: cycles and recurrent count

The exact-valuation-`v` stratum contains `(p-1)p^(a-v-1)` states.  For
`2v<a`, Step 1 gives common cycle length `p^v`; division yields
`(p-1)p^(a-2v-1)` cycles.  Low states are precisely the residues not divisible
by `p^ceil(a/2)`.  There are `p^a-p^floor(a/2)` of them.

### Step 5: tail populations

If `a=2h+1`, high states are the multiples of `p^(h+1)`, including zero.
There are `p^h`, all at tail one.  If `a=2h`, strict high states are the
`p^(h-1)` multiples of `p^(h+1)`, all at tail one.  In the middle stratum each
nonzero value of `u mod p` occurs `p^(h-1)` times.  As this value runs through
`1,...,p-1`, `r+1` runs through `p,...,2`; each depth `2,...,p` therefore has
`p^(h-1)` states.

### Step 6: low and high inverse images

Step 1 makes each low restriction a bijection, so every low target has one
low predecessor.  A strict high source with complementary low valuation `w`
is uniquely `p^(a-w)u`, where `1<=u<p^w` and `p` does not divide `u`.  Its
target is

`p^w(1+p^(a-2w)u)`.

The valuation recovers `w`, and the displayed quotient recovers `u`, proving
injection.  Together with the special source `0->1`, these images are exactly
the stated set `D`.  Each already has its low predecessor, so precisely these
targets have two predecessors and no target can receive more than two.

### Step 7: empty targets

For odd `a`, no middle layer exists.  Both low and high sources target low
strata, so exactly the high targets are empty fibres.  Their number is
`p^floor(a/2)`.

For `a=2h`, the middle unit coordinate map is `u->u+1 mod p^h`.  A high or zero
coordinate is divisible by `p` and has the unique unit predecessor `u=z-1`.
A middle target coordinate `z` has a middle predecessor iff `z-1` is a unit,
which fails exactly when `z=1 mod p`.  These `p^(h-1)` targets are exactly the
stated set `Z`.

### Step 8: census and image

For either parity, the empty set has size `d=p^floor((a-1)/2)`.  The double
set has size

`1+sum_(1<=w<a/2) (p-1)p^(w-1)=d`.

It lies in low strata, while the empty set lies in high or middle strata, so
the sets are disjoint.  All remaining `p^a-2d` targets have one predecessor.
The image therefore has `p^a-d` elements.

All claims follow. ∎

## Boundary audit

- `a=1`: units are fixed, `0->1`, one empty and one double fibre.
- `p=2`, even `a`: every equality-layer state has tail exactly two.
- `x=0`: handled separately before applying nonzero factorization.
- `u+r=p^h`: the landing state is zero and `s=h`, giving period one.
- Empty sums in the double-target atlas are allowed for `a<=2`.

## Corrections or missing assumptions

None identified.  The canonical-representative convention is necessary
because the integer `N/gcd(x,N)` must be defined from a residue representative;
gcd invariance modulo `N` makes the value well defined.

## Open risks

- Exact-formula external ownership remains incompletely searched.
- Composite moduli are outside scope; no Chinese-remainder factorization is
  asserted for the state-dependent increment.

