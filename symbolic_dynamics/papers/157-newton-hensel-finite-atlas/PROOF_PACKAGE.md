# Proof package — P157

## Claim

For every `n>=1`, the map

~~~text
F_n(x)=3x^2-2x^3 mod 2^n
~~~

has the exact temporal census, image criterion, every-target fibres, and image
size stated in Theorem 1 of `main.tex`.

## Status

**PROVABLE AS STATED.**  The claim survives unchanged, including the separate
quotient boundaries `N=1,2`.

## Assumptions and notation

- States are residue classes modulo `2^n`, with `n>=1`.
- `v_2(0 mod 2^n)=n` is the truncated valuation.
- `e(x)=x` for even `x` and `e(x)=1-x` for odd `x`.
- A nonzero even source is `x=2^v w`, `w` odd.
- In a nonzero output stratum, `N=n-2v` and
  `h_v(w)=w^2(3-2^(v+1)w)`.

## Dependency map

1. The temporal theorem uses only the two exact endpoint-error
   factorizations and divisibility counting.
2. The inverse theorem uses valuation separation plus the normalized-unit
   lemma.
3. The lemma uses odd-square congruences and an exact cubic Taylor difference.
4. Full fibres restore a `2^v` reduction multiplicity; endpoint fibres use a
   direct divisibility count; the odd side follows by reflection.

## Proof

### 1. Temporal law

Direct expansion gives

~~~text
F(x)=x^2(3-2x),
1-F(x)=(1-x)^2(1+2x),
F(1-x)=1-F(x).
~~~

The cofactor is odd in the selected parity basin, so the selected error
valuation satisfies

~~~text
v_2(e(F(x)))=min(n,2v_2(e(x))).
~~~

Induction gives the formula at time `t`; parity preservation identifies the
endpoint.  Entry by time `t` is equivalent to divisibility of the initial
selected error by `2^ceil(n/2^t)`.  Each parity basin contributes
`2^(n-ceil(n/2^t))` states, giving the CDF.  Consecutive differences give all
shells.  Initial errors of valuation one attain the sharp maximum
`ceil(log_2 n)`.  Finite absorption leaves only the fixed endpoints recurrent.
For `n=1`, all states are already endpoints and the same formula gives height
zero.

### 2. Normalized-unit lemma

For an odd `w`, `w^2=1 mod 8`.  Hence `h_1(w)=7 mod 8`, while
`h_v(w)=3 mod 8` for `v>=2`.  Reduction gives the asserted `N=1,2` image
classes; their domains contain one and two odd residues, respectively, and
all map to the sole admissible target.

For `N>=3`, write `w=r+4z`, where `r` is `1` or `3`, and set

~~~text
Phi_{v,r}(z)=[h_v(r+4z)-h_v(r)]/8.
~~~

This is integral because all odd inputs have the same image modulo eight.
The derivatives are

~~~text
h'_v(w)=6w(1-2^v w),
h''_v(w)=6-6*2^(v+1)w,
h'''_v(w)=-6*2^(v+1).
~~~

On odd inputs their valuations are exactly `1`, exactly `1`, and at least
`3`.  With `delta=4*2^j`, the exact cubic identity divided by eight reads

~~~text
[h_v(w+delta)-h_v(w)]/8
 = delta h'_v(w)/8
 + delta^2 h''_v(w)/16
 + delta^3 h'''_v(w)/48.
~~~

The first term is `2^j` times an odd integer; the next terms have valuations
at least `2j+1` and `3j+5`.  Thus

~~~text
Phi(z+2^j)-Phi(z)=2^j mod 2^(j+1).
~~~

Induction from the unique class modulo one proves that each branch is a
permutation at every truncated quotient level.  For modulus `2^N`, the
output beyond the fixed low three bits depends on `Phi mod 2^(N-3)`, while
`z` ranges modulo `2^(N-2)`.  Each branch gives two preimages and the two
branches give four.

### 3. Full fibres and image

The factorization

~~~text
F_n(2^v w)=2^(2v)h_v(w)
~~~

shows that nonzero even image valuations are exactly even values `2v<n`.
For `N=n-2v`, the source unit lives modulo `2^(n-v)` but the target condition
only sees it modulo `2^N`; reduction has `2^v` lifts.  Multiplication by the
reduced `1`, `2`, or `4` solutions gives

~~~text
2^[v+min(N-1,2)].
~~~

The zero predecessors are exactly the multiples of `2^ceil(n/2)`, numbering
`2^floor(n/2)`.  Reflection gives the odd basin and the fibre over one.
There are `2^max(0,N-3)` normalized image units in each nonzero stratum.
Summing the strata, doubling, and adding `0,1` proves the image-size formula.

## Corrections or missing assumptions

None.  The small cases `N=1,2` must remain visible in every compressed form.

## Open risks

- The Taylor formula is an exact polynomial identity, not an approximation.
- The cubic and quadratic lifting mechanism remain zero-credit prior
  background; Burban–Drozd is a direct record, not an origination claim.
- An earlier source for the residual one-step inverse atlas would reopen
  subtraction.
