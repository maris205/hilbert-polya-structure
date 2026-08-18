# C62 arithmetic and local-evidence boundary

## Supported

C62 supports exact finite-group statements for the released `W(E_6)` action:
the two lambda-square character identities, complete orbit/stabilizer/core/
normalizer data, fixed-field degrees `51840/|S|`, ambient-conjugacy type
labels, and factorized marker carriers evaluated at the split-prime witness
`p=692717`.

## Explicitly unsupported

The marker carriers are products in formal orbit variables. They are not
expanded arithmetic resolvents over `Q`, and the split-prime noncollision
check does not compute discriminants, differents, maximal orders, residue
degrees, inertia, ramification, Euler factors, or root numbers. No local-field
classification or bad-prime list is asserted.

The literal scope control is retained in every evidence object:
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Release consequence

The C62 paper may state the finite-etale/fixed-field shadow and its exact
separation data, but must not promote the marker construction to an arithmetic
field-resolvent theorem. Any future arithmetic extension requires a separate
source-bound computation and a new release gate.
