# HCS-C140: mod-three sofic suspension

C140 freezes the strictly sofic binary shift in which every finite zero gap
between consecutive ones is divisible by three, including the all-zero point.
Its three-state residue presentation has cover determinant `1-u-v^3`, but the
cover overcounts the all-zero label point.  The exact intrinsic correction is

```text
Z_140(u,v)=(1+v+v^2)/(1-u-v^3),
D_140=Z_140^(-1)=(1-u-v^3)/(1+v+v^2).
```

The package proves strict soficity, minimality of the three-state
right-resolving cover, uniqueness of lifts off the all-zero point, the
all-period weighted fixed-point correction, and the intrinsic primitive
product.  Independent checking keeps cover paths and label points separate.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  The conservative verdict is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`; Route B is
not authorized.
