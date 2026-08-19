# C71 pilot report

Status: **PASS**.

The complement family is the affine group

```text
Hom(K,D) ~= (Z/2)^32 + (Z/4)^3 + Z/8,
|Hom(K,D)| = 2^41.
```

Explicit enumeration gives 38 subgroups in `D`.  Strict subgroup-poset
inversion and an independent Birkhoff/epimorphism calculation agree on ten
image types.  Aggregating by image order gives the six intersection indices
`1,2,4,8,16,32`, whose counts sum exactly to `2^41`.

The common kernel of all maps `K -> D` is `8K`; under `C=D direct-sum K` this
is `8C ~= Z/3 + Z/18`, of order 54.  A surjective graph difference exists, so
two complements already generate `C`, and all complements certainly do.

The named-coordinate HNF calculation finds no generating singleton or pair
for `8C`, and exactly 25 generating triples.  All 25 contain `S9`.
