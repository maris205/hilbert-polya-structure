# C72 theorem package

## Theorem 1: exact named coordinate model

The C71 core has the presentation

```text
8C = <8[S1],8[S3],8[S9]> ~= Z/9 + Z/3 + Z/2.
```

All sixteen named coordinates are recorded in the canonical evidence.  Five
of them, `S5,S6,S10,S13,S14`, vanish after multiplication by eight.

## Theorem 2: complete named-support atlas

The `2^16=65536` named supports generate exactly 20 distinct subgroups, and
these are every subgroup of `8C`.  Their abstract type inventory is

```text
1: 1                 Z/2: 1
Z/3: 4               Z/6: 4
(Z/3)^2: 1           Z/9: 3
Z/18: 3              Z/3 + Z/6: 1
Z/3 + Z/9: 1         Z/3 + Z/18: 1
```

The evidence records the exact ten-type distribution for every support size
from 0 through 16; every row sums to `binomial(16,r)`.

## Theorem 3: generation complex

The full-core generating polynomial is

```text
25 t^3 + 224 t^4 + 940 t^5 + 2461 t^6 + 4504 t^7
+ 6095 t^8 + 6269 t^9 + 4950 t^10 + 2992 t^11
+ 1364 t^12 + 455 t^13 + 105 t^14 + 15 t^15 + t^16.
```

There are exactly 25 inclusion-minimal generating supports.  They are the C71
triples, and all contain `S9`.

The minimum `3` concerns subsets of the sixteen named classes.  The abstract
group `Z/3 + Z/18` has generator rank `2`.
