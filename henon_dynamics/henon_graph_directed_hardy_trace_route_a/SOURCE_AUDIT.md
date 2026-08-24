# C124 source audit

## Source boundary

This package is source-defined.  Its only mathematical inputs are the frozen
rational matrix (A), the three rational translations, the directed graph
(B), the edge weights (c), and the radius-three polydisc.  All claims are
derived from those bytes by exact arithmetic.

No paper, web page, numerical database, prime table, zero table, arithmetic
local datum, fitted parameter, or Route-B artifact is used.  Consequently this
package makes no literature-novelty claim and contains no citation whose
existence would need external verification.

## Frozen source

```text
A = [[3/16,-1/32],[1/4,0]]
t = (-2,0,2)
B = [[1,1,0],[1,0,1],[1,0,0]]
c = (1/2,1/3,1/5)
W = B diag(c)
domain = three copies of D_3^2
clock = one admissible graph edge per iterate
determinant = D_H(z)=det(I-z L)
```

The theorem has no orbit cutoff.  Periods (1) through (8) and Taylor degree
(8) are replay prefixes, not completeness limits.

## Integrity boundary

The exact producer is checked by a standard-library implementation that imports
no producer code, a fresh SymPy reconstruction including explicit polynomial
finite sections, byte replay, and hostile mutations.  The paper labels the
translation-blindness result as a negative control: the Fredholm determinant
does not identify affine orbit locations.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
