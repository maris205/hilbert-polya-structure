# Proof package — binary-projective Steiner triangle collapse

## Equality strata

If `(a,b,c)=(x,x,x)`, idempotence gives a fixed point.  If exactly two
coordinates are equal, a direct three-line calculation with
`x star x=x` and `x star y=x+y` shows that the position of the singleton
rotates and that the third iterate, but neither earlier iterate, is the
starting ordered triple.  There are `3N(N-1)` such states and therefore
`N(N-1)` strict three-cycles.

## Distinct triples

For distinct inputs no idempotent branch is used, so

```text
S(a,b,c)=(b+c,c+a,a+b).
```

The three outputs remain nonzero and distinct, and their sum is zero.  Thus
every distinct input lands in an ordered projective-line block.  If the
input already satisfies `a+b+c=0`, then `b+c=a`, `c+a=b`, and `a+b=c`, so it
is fixed.  Otherwise it has depth exactly one.

Choose the first two entries of an ordered block freely and distinctly; the
third is their nonzero sum.  Hence there are `N(N-1)` ordered blocks.  With
the `N` diagonals this gives `N^2` fixed points.  Subtracting diagonals,
exactly-two-equal triples, and blocks from `N^3` gives
`N(N-1)(N-3)` nonblocks.  At `N=3` this shell is empty; at every larger
binary-projective rank it is nonempty.

## Target-resolved inverse

The equality pattern calculation already gives one predecessor for every
diagonal or exactly-two-equal target and shows that no such source can reach
a distinct target.  A distinct source always maps to a block, so a nonblock
has no predecessor.

Let `(x,y,z)` be a block, so `x+y+z=0`.  Solving

```text
b+c=x,  c+a=y,  a+b=z
```

over `V` leaves one free vector `t=a` and yields

```text
(a,b,c)=(t,t+z,t+y).
```

All three entries are nonzero exactly when `t` avoids `0,z,y`.  For these
allowed values they are automatically distinct: an equality would force
one of `x,y,z` to vanish.  There are `(N+1)-3=N-2` choices.  This direct
parametrization proves the fibre theorem without division by orbit counts.

The complete graph and zeta formula follow.  The combined replacement
verifier checks ranks 2, 3, and 4; its role is bounded counterexample
pressure only.
