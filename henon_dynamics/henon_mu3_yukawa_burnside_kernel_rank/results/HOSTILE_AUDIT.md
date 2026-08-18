# C63 hostile audit

## Passed boundaries

- The 16 columns are ambient-conjugacy subgroup types, not hashes or subgroup
  orders used as field names.
- Rank 13 and nullity 3 are recomputed from the full integer matrix.
- The `R4` support submatrix has rank 7, proving a one-dimensional restricted
  kernel rather than merely exhibiting one vanishing vector.
- `S15-S16` is identified with the original C61 relation.
- `S10-S9` is labeled an inherited C60 collision and excluded from the C63
  novelty statement.
- Exterior and symmetric relations are kept distinct: the latter is the
  exterior relation plus the diagonal C61 relation.

## Refused claims

C63 does not classify the kernel of the full Burnside ring of `W(E_6)`.  It
does not compute arithmetic field resolvents, maximal orders, discriminants,
local fields, bad Euler factors, or root numbers.  The literal firewall is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
