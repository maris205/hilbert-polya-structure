# C64 source and novelty audit

## Authority

The producer binds the exact byte hashes of the released C61 group evidence,
the C62 complete atlas and fixed-field dictionary, and the C63 kernel evidence.
It reconstructs all 51840 group elements and every stabilizer from the source
arrays.  Neither the C63 character matrix nor the C64 pilot output is used as
authority for the mark counts.

## Prior art and bounded contribution

Table-of-marks theory, Burnside's mark homomorphism, Gassmann relations, and
the injectivity of the full mark map are classical.  The bounded contribution
is the exact instance-specific 16-type mark matrix attached to the frozen
C62 (W(E_6)) subgroup dictionary, its determinant, and the explicit
nonzero mark image of the C63 four-versus-four relation.

No absolute priority or literature-completeness claim is made.  The result is
not a new general theorem about table-of-marks algorithms.

## Scope firewall

`NO_BAD_EULER_OR_ROOT_NUMBER` is mandatory.  Arithmetic fields, local
decomposition, bad Euler factors, root numbers, automorphy, and Hilbert--Polya
operators are excluded.  The full 350-class Burnside ring is explicitly not
claimed.
