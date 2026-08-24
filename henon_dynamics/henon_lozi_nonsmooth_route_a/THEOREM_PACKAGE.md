# Theorem package — C116

**Finite sign-atlas proposition.**  For the frozen Lozi map, solving all 510
binary affine returns of lengths one through eight and then applying strict
branch tests gives rooted admissible counts

```text
(2, 4, 2, 8, 22, 40, 58, 128).
```

No candidate return is singular and no candidate hits `x=0` in this prefix;
all rejected words fail a declared sign inequality.  Quotienting the strict
primitive words by cyclic rotation gives

```text
(2, 1, 0, 1, 4, 6, 8, 15),
```

or 37 primitive necklaces.

**Finite cycle-atlas identity.**  Give a phase with symbol `s` the diagnostic
edge weight `rho_s`, where `rho_0=1/2` and `rho_1=2/3`, and take the direct sum
of one weighted cyclic block for every certified primitive necklace.  The
resulting sparse operator has 37 blocks, 240 states, and 240 edges.  For
`1 <= k <= 8`, its unweighted trace is exactly the rooted admissible count and
its weighted trace is

```text
7/6, 49/36, 91/216, 1393/1296,
13027/7776, 82873/46656, 430171/279936, 3258913/1679616.
```

Its determinant is recorded only as the exact finite block factor ledger
`product_c (1-rho(c) z^|c|)`.  These claims neither supply a global symbolic
coding nor upgrade the finite matrix to an analytic determinant.
