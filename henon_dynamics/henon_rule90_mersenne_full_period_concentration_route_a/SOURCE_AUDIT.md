# C155 source audit

## Source lock

The object is multiplication by `a=x+x^{-1}` on
`R_L=F_2[x,x^{-1}]/(x^L-1)` for `L=2^r-1`, `r>=2`.  One update is the clock.
Probability is uniform on the periodic image, not on the full state space;
the mean cycle length is total periodic states divided by total primitive
cycles.  The only matched control is the same local rule on `L=2^s`.

## Proof boundary

The identity `a^(L+1)=a` makes the image a permutation module satisfying
`g^L=I`.  For `d=gcd(j,L)`, polynomial Bézout identities prove
`ker(g^j-I)=ker(g^d-I)`; this is an all-`r` theorem, not an inference from the
finite ledger.  The cleared Rule-90 polynomial has degree `2d`, giving the
fixed-dimension bound.  Since odd `L` has no proper divisor larger than
`L/3`, a union bound gives exponential full-period concentration.  Burnside
then gives the cycle count and mean-length limits.

The rows through `r=8`, 494 proper-time cells, and power controls through
`s=8` are replay sentinels only.  The statement does not claim that every
divisor of `L` occurs as a period or that a thermodynamic orbit measure has
been constructed.  No target/arithmetic data, natural operator, or Route-B
input is used.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
