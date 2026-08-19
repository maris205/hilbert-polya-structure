# C71 theorem package

Let `C=D direct-sum K` be the fixed C69 decomposition and let
`Gamma_f={(f(k),k):k in K}` for `f in Hom(K,D)`.

## Theorem 1: graph intersection distribution

Every complement of `D` is a unique `Gamma_f`.  For any `f,g`,

```text
Gamma_f intersect Gamma_g ~= ker(f-g),
K/ker(f-g) ~= im(f-g).
```

Consequently the spectrum is translation invariant.  Here index means
`[Gamma_f : Gamma_f intersect Gamma_g]=[K:ker(f-g)]`, not the index in `C`.
From every fixed complement, the numbers at indices `1,2,4,8,16,32` are
respectively

```text
1, 28665, 117600270, 70111567864, 1030892519424, 1097901539328.
```

The ten quotient types and exact counts are:

```text
0                         1
Z/2                   28665
Z/4                  245760
(Z/2)^2           117354510
Z/8                  262144
Z/2 + Z/4        1509212160
(Z/2)^3         68602093560
Z/2 + Z/8        1609826304
(Z/2)^2 + Z/4 1029282693120
Z/8 + (Z/2)^2 1097901539328
```

These counts sum to `2^41`.

## Theorem 2: universal core and span

The common intersection and total span of the complement family are

```text
intersection_f Gamma_f = 8C ~= Z/3 + Z/18,  |8C|=54,
generated subgroup of all Gamma_f = C.
```

In fact `1097901539328` differences `f-g` are surjective; each corresponding
pair of complements already generates `C`.

## Proposition: named core geometry

The orders of `8[S_1],...,8[S_16]` are

```text
9,3,3,3,1,1,9,3,2,1,3,3,1,1,9,9.
```

No one or two of these elements generate `8C`.  Exactly 25 triples generate
it, and all contain `S9`.  The canonical evidence records all 25 triples.

No claim is made that the quotient image type determines the full abstract
kernel type in every row of the distribution.
