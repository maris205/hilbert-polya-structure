# P182 proof package

This document expands the proof dependencies behind `main.tex`.  It contains
no computational assumptions.

## Definitions

Let `L` be a lattice and

```text
T(a,b,c) = (c, a∧b, a∨b).
```

For the enumerative specialization, let `V=F_q^d`, let `L_d(q)` be its
subspace lattice, and write `[n choose r]_q` for the Gaussian coefficient and
`g_n(q)=sum_r [n choose r]_q`.

## Lemma 1 — universal square and collapse

Put `m=a∧b` and `j=a∨b`.  Direct substitution gives

```text
T^2(a,b,c) = (j, c∧m, c∨m).
```

Writing `u=c∧m` and `v=c∨m`, we have `u<=m<=j` and `u<=v`.  Hence

```text
T^3(a,b,c) = (v,u,j),
T^4(a,b,c) = (j,u,v) = T^2(a,b,c).
```

Only associativity and absorption are used.

## Lemma 2 — image, recurrence, and depth

Every output is `(C,M,J)` with `M<=J`.  Conversely, if `M<=J`, then
`T(M,J,C)=(C,M,J)`, so this describes the image exactly.

Since `T^4=T^2`, a recurrent point must equal its square.  The equations

```text
a=a∨b,  b=c∧a∧b,  c=c∨(a∧b)
```

are equivalent to `b<=a` and `b<=c`.  On these states
`T(a,b,c)=(c,b,a)`, so fixed points add `a=c` and every remaining recurrent
state lies in a strict 2-cycle.

For any source, its first image `(c,a∧b,a∨b)` is recurrent exactly when
`a∧b<=c`; the other recurrent inequality is automatic.  Therefore the depth
predicate is:

```text
depth 0: b<=a,c;
depth 1: not depth 0 and a∩b<=c;
depth 2: a∩b not contained in c.
```

For `d>=1`, taking `a=b` a line and `c=0` proves sharp height two.

## Lemma 3 — disjoint ordered pairs

In an `n`-space, the number of ordered pairs `(X,Y)` with `X∩Y=0` is

```text
Q_n(q) = sum_{a=0}^n sum_{s=0}^{n-a}
         [n choose a]_q [n-a choose s]_q q^(as).
```

For fixed `X` of dimension `a` and fixed `s`, choose the image of `Y` as an
`s`-subspace of `V/X`; then `Y` is the graph of one of `q^(as)` maps from
that subspace to `X`.

## Lemma 4 — fixed, recurrent, image, and depth populations

Choose the middle subspace `B` first.  There are `g_(d-b)` superspaces of a
fixed `b`-space.  Consequently

```text
alpha_d = sum_b [d choose b]_q g_(d-b),
rho_d   = sum_b [d choose b]_q g_(d-b)^2
```

count fixed and recurrent states.  Thus strict 2-cycles number
`(rho_d-alpha_d)/2`.  The image has arbitrary first coordinate and an
interval in the last two coordinates, hence size `g_d alpha_d`.

To count sources satisfying `A∩B<=C`, fix `M=A∩B` of dimension `m`.  Quotient
by `M`; Lemma 3 chooses the disjoint images of `A,B`, and `g_(d-m)` chooses
`C/M`.  Thus

```text
eta_d = sum_m [d choose m]_q Q_(d-m)(q) g_(d-m)(q).
```

The depth populations are `rho_d`, `eta_d-rho_d`, and `g_d^3-eta_d`.

## Lemma 5 — every target fibre

A predecessor of `(C,M,J)` is an ordered pair `(A,B)` with
`A∩B=M` and `A+B=J`; the source's third coordinate is forced to equal `C`.
No pair exists unless `M<=J`.  When it does, quotient by `M`.  If
`k=dim(J/M)`, then `A/M` and `B/M` are ordered complementary subspaces.
Choosing the first to have dimension `a` and then choosing its complement
gives

```text
kappa_k(q) = sum_a [k choose a]_q q^(a(k-a)).
```

This proves the targetwise formula.  Targets whose interval has quotient
dimension `k` number

```text
g_d sum_{m=0}^{d-k} [d choose m]_q [d-m choose k]_q.
```

All other `g_d^3-g_d alpha_d` targets have empty fibre.

## Lemma 6 — sharp maximum fibre

Embed a `k`-space `H` as a hyperplane of `H direct-sum ell`.  The injection

```text
(X,Y) -> (X,Y direct-sum ell)
```

sends ordered decompositions of `H` to ordered decompositions of the larger
space.  It misses `(ell,H)`, so `kappa_k<kappa_(k+1)`.  Hence the maximum is
`kappa_d`, which requires `M=0,J=V`; the arbitrary first coordinate produces
exactly `g_d` maximizing targets.  Since `kappa_0=1`, the `g_d^2` targets
`(C,M,M)` are precisely the minimum-positive-fibre targets.

## Dependency closure

Lemmas 1–2 prove the universal theorem.  Lemmas 3–4 prove every functional-
graph population.  Lemmas 5–6 prove every local fibre, its histogram, and its
extrema.  The `d=0` boundary reduces to the unique fixed state; sharp height
and strict fibre growth begin at `d>=1`.

