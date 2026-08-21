# HCS-C91 first-passage race atlas

C91 extends the frozen C88 first-passage receipt to every unordered pair of
targets incomparable in the subgroup poset.  There are 108 such pairs.  For
each pair the evidence gives exact `16!`-permutation counts for left-first,
tie, and right-first outcomes, together with rank-resolved boundary-edge
counts.  Ninety-nine pairs have a nonzero tie class.

Evidence SHA-256: `36b0fffda585ea483ba5603101c83c361b85ca4ba9a49c878f1e366d3c13ff0f`.

The independent checker, SymPy cross-check, clean replay, and 16/16 hostile
mutations pass.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This is an exact finite probability certificate.  It makes no arithmetic or
local-data, Euler-factor, root-number, automorphy, full Burnside/table-of-
marks, or Hilbert--Polya operator claim.
