# HCS-C66 results

Status: `PREFREEZE_G3_PASS`.

The exact restricted C64 mark matrix is 16-by-16, rank 16, and has determinant
`226492416 = 2^23 3^3`.  Its complete Smith invariants are

```text
[1, 2,2,2,2,2,2,2,2,2,2, 4,4,4, 24,144]
```

Therefore

```text
coker(mark) ~= (Z/2)^10 + (Z/4)^3 + Z/24 + Z/144.
```

The primary decomposition is `(Z/2)^10 + (Z/4)^3 + Z/8 + Z/16` at 2 and
`Z/3 + Z/9` at 3.  C65 compatibility is confirmed:
`old_snf=(2,8)`, `all_snf=(2,2,8)`, relative quotient `Z/2`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No full Burnside-ring, arithmetic,
local-field, bad-Euler-factor, or root-number claim is made.
