# C69 pilot report

Status: **PASS**.

The sparse row matrix representing

```text
(x10 mod 8, x3 mod 2, x1+x15 mod 2)
```

satisfies `RM=0 mod (8,2,2)` and `RU=I mod (8,2,2)`.  Hence it descends to a
retraction of the actual C68 embedding.

The zero-congruence lattice has the column basis obtained from `I_16` by
replacing

```text
b1=e1-e15, b3=2e3, b10=8e10, b15=2e15.
```

Its determinant is 32.  The integral matrix `B^{-1}M` has Smith invariants
`(1^4,2^8,4^2,12,144)` and order 7077888.  The retractions form a torsor of
size `|Hom(C/D,D)|=2^41`.

The candidate therefore survives as a splitting-and-classification paper.
