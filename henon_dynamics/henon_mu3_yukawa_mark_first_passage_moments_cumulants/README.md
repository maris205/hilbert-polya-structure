# HCS-C89 first-passage moments and cumulants

C89 lifts the frozen C88 first-passage atlas from distributions to exact
moment data.  For each of the twenty actual subgroup targets it records the
raw moments, falling-factorial moments, central moments, and cumulants through
order six.  The same rows are rebuilt from the 65536-bit C88 hit indicators,
and every raw and factorial moment is independently recovered from survival
tails.

Evidence SHA-256: `86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9`.

The producer, independent checker, SymPy cross-check, clean replay, and
13/13 hostile mutations pass.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.

This is an exact finite probability certificate.  It makes no arithmetic or
local-data, Euler-factor, root-number, automorphy, full Burnside/table-of-
marks, or Hilbert--Polya operator claim.
