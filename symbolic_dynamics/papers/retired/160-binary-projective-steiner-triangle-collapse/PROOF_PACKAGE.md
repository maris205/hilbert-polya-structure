# Proof package — P160

## Four-way partition

- `(x,x,x)` is fixed by idempotence.
- For `x!=y`,
  `(x,x,y)->(x+y,x+y,x)->(y,y,x+y)->(x,x,y)`; no earlier return is possible.
- For distinct inputs, the update is `(b+c,c+a,a+b)`.  The outputs are
  nonzero, distinct, and sum to zero.  A source block is fixed; a nonblock has
  depth one.

Counts follow without orbit extrapolation: `N` diagonals, `N(N-1)` ordered
blocks, `3N(N-1)` two-equal states, and the remaining
`N(N-1)(N-3)` nonblocks.  This yields `N^2` fixed points and `N(N-1)` strict
three-cycles.

## Inverse calculation

For a block `(x,y,z)`, solve `b+c=x`, `c+a=y`, `a+b=z`.  Consistency is
exactly `x+y+z=0`; setting `a=t` gives `(t,t+z,t+y)`.  Nonzero entries require
`t` to avoid `0,z,y`.  Any equality among the resulting entries would force
one of `x,y,z` to be zero.  Hence all `N-2` allowed parameters are valid and
distinct.

The equality-stratum cycles provide singleton fibres.  Distinct sources
always map to blocks, so nonblocks have zero fibres.  Of a block's `N-2`
sources, one is the block and all others are source-free nonblocks; therefore
the same fibre statement holds for every positive iterate.

## Corollaries

The image is the recurrent core.  Fixed points of `S^k` are the `N^2` fixed
states, plus all `3N(N-1)` three-cycle states exactly when `3|k`.  The zeta
product follows from the fixed and primitive-three-cycle counts.
