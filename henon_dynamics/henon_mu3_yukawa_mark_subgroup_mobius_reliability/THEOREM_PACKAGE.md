# C77 theorem package

## Theorem 1 (cumulative closure probability)

Let `C_i` be the cyclic closure of named label `S_i`, and let `H` be one of
the twenty subgroups in the C76 ordered lattice.  If every label is deleted
independently with probability `q`, then

\[
 P_{\le H}(q)=\Pr[\Phi(A)\le H]=q^{16-n_H},
 \qquad n_H=|\{i:C_i\le H\}|.
\]

Indeed, labels with `C_i\not\le H` must all be deleted, while labels with
`C_i\le H` are unrestricted.

## Theorem 2 (Möbius inversion)

For every subgroup `H`,

\[
 P_{=H}(q)=\Pr[\Phi(A)=H]
 =\sum_{K\le H}\mu(K,H)q^{16-n_K},
\]

where `mu` is the integer Möbius function of the actual twenty-node subgroup
poset.  The direct support polynomial

\[
 \sum_{A:\Phi(A)=H}(1-q)^{|A|}q^{16-|A|}
\]

has the same integer coefficient vector for every `H`.

## Exact C77 data

In subgroup-index order `0,...,19`, the subgroup orders and `n_H` values are

```text
orders: 1,2,3,3,3,3,6,6,6,6,9,9,9,9,18,18,18,18,27,54
n_H:    5,6,7,6,7,6,8,7,8,7,11,7,7,8,12,8,8,9,15,16
```

The exact inverted coefficient vectors (key = exponent of `q`) are

```text
0: {11: 1}
1: {10: 1, 11: -1}
2: {9: 1, 11: -1}
3: {10: 1, 11: -1}
4: {9: 1, 11: -1}
5: {10: 1, 11: -1}
6: {8: 1, 9: -1, 10: -1, 11: 1}
7: {9: 1, 10: -2, 11: 1}
8: {8: 1, 9: -1, 10: -1, 11: 1}
9: {9: 1, 10: -2, 11: 1}
10:{5: 1, 9: -2, 10: -2, 11: 3}
11:{9: 1, 10: -1}
12:{9: 1, 10: -1}
13:{8: 1, 10: -1}
14:{4: 1, 5: -1, 8: -2, 10: 5, 11: -3}
15:{8: 1, 9: -2, 10: 1}
16:{8: 1, 9: -2, 10: 1}
17:{7: 1, 8: -1, 9: -1, 10: 1}
18:{1: 1, 5: -1, 8: -1, 9: -2, 10: 3}
19:{0: 1, 1: -1, 4: -1, 5: 1, 7: -1, 8: -1, 9: 5, 10: -3}
```

The top row is therefore

\[
P_{=Q}(q)=1-q-q^4+q^5-q^7-q^8+5q^9-3q^{10}
=(1-q)(1-q^4-q^7-2q^8+3q^9).
\]

## Corollaries and boundaries

The twenty exact rows form a probability partition (`sum_H P_{=H}=1`), and
the top row agrees with the independently derived C73 reliability law.  This
is a finite named-coordinate theorem.  No arithmetic/local, Euler-factor,
root-number, automorphy, full Burnside-ring, or Hilbert--Polya statement is
made.
