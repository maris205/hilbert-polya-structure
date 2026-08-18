# HCS-C63 results

Status: `PREFREEZE_G3_PASS`.

The exact C61 `W(E_6)` action has order `51840` and 25 conjugacy classes.  On
the 16 ambient-conjugacy subgroup types from the C62 dictionary, the complete
fixed-coset character matrix is `25 x 16`, has rational rank 13, and has
nullity 3.

A basis of the restricted rational kernel is

```text
z1 = S10 - S9
z2 = -S2 - S3 - S5 - S6 + S11 + S12 + S13 + S14
z3 = S16 - S15
```

The headline C63 relation is the exterior-square plus-minus difference

```text
R4 = S2 + S3 + S5 + S6 - S11 - S12 - S13 - S14.
```

Its support-restricted `25 x 8` matrix has rank 7 and one-dimensional kernel.
Because every coefficient of `R4` is nonzero, no proper subset of these eight
types supports a nonzero relation.  The four plus/minus pairs have degrees
`480, 480, 4320, 4320`, total degree `9600` on each side, and distinct
ambient-conjugacy type labels.

The symmetric-square difference equals `R4 + (S15-S16)`.  The `S15-S16`
direction is the original C61 Gassmann relation, and `S10-S9` is retained as
an inherited C60 collision control rather than a C63 novelty claim.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No full-Burnside-kernel, arithmetic
resolvent, local-field, bad-Euler-factor, or root-number claim is made.
