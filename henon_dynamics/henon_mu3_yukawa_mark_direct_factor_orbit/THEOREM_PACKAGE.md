# C70 theorem package

Let `C=D direct-sum K` be the C69 decomposition.

## Theorem 1: homogeneous spaces

`Aut(C)` acts transitively on all `D`-type direct factors and on all ordered
`(D,K)` decompositions.  The corresponding stabilizers are

```text
Stab(D) = Hom(K,D) semidirect (Aut(D) x Aut(K)),
Stab(D,K) = Aut(D) x Aut(K).
```

## Theorem 2: exact masses

The orbit sizes are

```text
N_D   = 5846893330432 = 2^25 * 7 * 11 * 31 * 73,
N_dec = 12857454406351852314558464
      = 2^66 * 7 * 11 * 31 * 73.
```

Every `D`-type direct factor has `|Hom(K,D)|=2^41` complements, and

```text
N_dec = N_D * 2^41,
|Aut(C)| = N_D * |Stab(D)|,
|Aut(C)| = N_dec * |Stab(D,K)|.
```

Split embeddings form one orbit of size
`N_D*|Aut(D)|=2245207038885888`; their stabilizer is
`Hom(K,D) semidirect Aut(K)`.

## Proposition: boundary counterexample

In the diagonal 2-primary model, let `g4` generate the `Z/16` factor and let
`f1,f2` be two `Z/2` generators.  Then

```text
H=<2*g4,f1,f2> ~= D,
C2/H has type (3,2,2,2,1^9), not K2=(4,2,2,2,1^8).
```

Thus `H` is not a direct factor.  No transitivity claim is made for all
subgroups abstractly isomorphic to `D`.

The Birkhoff subgroup formula gives `8794482475008` total `D`-type subgroups,
including `2947589144576` non-direct subgroups.  Consequently there are
`3377081270403072` monomorphisms from an abstract `D`, but only
`2245207038885888` split embeddings.
