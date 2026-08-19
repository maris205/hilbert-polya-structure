# C69 theorem package

Let `C=Z^16/MZ^16`, let `U=[u1 u2 u3]`, and identify the C68 subgroup `D`
with `A=Z/8 + Z/2 + Z/2` through `a |-> [Ua]`.

## Theorem 1: actual extension splits

The formula

```text
rho([x])=(x10 mod 8, x3 mod 2, x1+x15 mod 2)
```

defines a homomorphism `rho:C->A` and `rho([Ua])=a`.  Thus the fixed inclusion
`D subset C` splits.

Certificate: its row matrix `R` satisfies `RM=0 mod (8,2,2)` and
`RU=I mod (8,2,2)`.

## Theorem 2: explicit complement

Let

```text
L={x : x10=0 mod 8, x3=0 mod 2, x1+x15=0 mod 2}.
```

Then `MZ^16 subset L`, `[Z^16:L]=32`, and `K=L/MZ^16=ker(rho)`.  With the
explicit column basis `B` in the evidence, `N=B^{-1}M` is integral and

```text
SNF(N)=[1,1,1,1,2,2,2,2,2,2,2,2,4,4,12,144].
```

Therefore `C=D direct-sum K`, with

```text
K ~= (Z/2)^8 + (Z/4)^2 + Z/12 + Z/144.
```

## Theorem 3: all complements

The set of retractions of the fixed inclusion is a torsor under
`Hom(C/D,D)`.  Its three target-coordinate exponents are `(17,12,12)`, so
the row counts are `(2^17,2^12,2^12)` and the total number of retractions is

```text
2^41 = 2199023255552.
```

Kernel gives a bijection from these retractions to complements of `D` in `C`.
Consequently the displayed complement is explicit but not canonical.
