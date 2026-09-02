# Odd-subtree contraction: theorem pass, portfolio kill

**Final decision:** `KILL_INTERNAL_P148_SILHOUETTE`  
**External state:** `HOLD_EXTERNAL`  
**Paper action:** none

## Literal system

A state is a finite plane rooted tree.  At every synchronous step, delete
each nonroot vertex whose current rooted fringe subtree has odd order and
promote its surviving descendants to the nearest retained ancestor in their
inherited plane order.  The outer root is always retained.

This rule is mathematically productive.  If a source of order `n` maps to a
target of order `m`, every retained nonroot vertex injects into a distinct
deleted odd child, so `n >= 2m-1`.  Iteration gives

```text
|source| >= 1 + 2^t (|target|-1).
```

Equality is constructible for every target and every time.  Hence, on trees
of order at most `N`, a target `U` lies in the time-`t` image exactly when
`1+2^t(|U|-1) <= N`.  The singleton is the unique recurrent state, and the
sharp cap height is `ceil(log2 N)`, witnessed by paths.

## Target-resolved extremal fibre

Let

```text
c_t = product_{j=1}^t (2^j-1)^(2^(t-j)),    c_0=1.
```

For a target `U` of order `m`, the number of time-`t` sources at the minimum
possible order `1+2^t(m-1)` is

```text
E_t(U) = c_t^(m-1)
         product_{v != root} binom(deg_U(v)+2^(t+1)-2, 2^(t+1)-2).
```

The local recurrence is `F_t=F_(t-1) F'_(t-1)`, with
`F_t(z)=c_t(1-z)^(-(2^(t+1)-1))`.  Lagrange extraction gives the aggregate

```text
sum_{|U|=m} E_t(U)
 = c_t^(m-1)/(m-1) * binom(2^(t+1)(m-1),m-2)
```

for `m>=2`, and value one for `m=1`.  The smallest order attaining depth
`h>=1` is `1+2^(h-1)`, with exactly `c_(h-1)` trees there.

## Exact pressure and the failed first run

The root verifier independently enumerates all 82,500 plane trees through
order twelve, checks every cap-time image through cap eleven, the local
closed form through time seven and degree fourteen, literal extremal fibres
through the stated boxes, sharp minimal-depth layers, and all declared
boundaries: 413,496 assertions in total.  Two fresh replays were
byte-identical at canonical SHA-256
`3a57d198bb751b715583b8aeb855375a6878d517abd5586ffa08460cda9e34fa`;
the verifier SHA-256 is
`e64284d4c8a72ad5b05b229d170bdb849a4f6e25e0acfd6f2a6c348cddb0f9f3`.

The first run failed because its audit compared the full image of an
extremal source layer with only the target-order slice: sources minimal for
an `m`-vertex target can also collapse below order `m`.  The verifier was
repaired to filter the rank-`m` slice in both support and aggregate checks;
the theorem and literal map were unchanged.  This negative event is retained
as part of the falsification record.

## Why it is killed

An independent gate reproduced the mathematics but found a decisive
portfolio collision with P148.  Both systems use the same plane-tree
carrier, synchronous vertex contraction with ordered child promotion, a
singleton recurrent core, a sharp logarithmic size clock, and a
target-outdegree product followed by Lagrange extraction.  The selector is
genuinely different---current fringe-subtree parity here versus generation
parity in P148---but the scored proof silhouette is not sufficiently
separated under the P1--P165 firewall.

The formulas remain a valid negative-control result.  They are not promoted,
do not fill P166, and provide no novelty or priority claim.
