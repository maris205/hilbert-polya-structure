# HCS-C67 theorem package

Let M be the exact 16-by-16 C64 self-mark matrix. For 1 <= j <= 16 define

```text
o_j = min { n > 0 : n e_j is in M Z^16 }.
```

For the transpose define the analogous dual order by replacing M with M^T.
Then the exact profiles, in the fixed S1,...,S16 order, are

```text
o      = [36,12,6,6,2,2,36,6,16,8,6,12,2,2,36,36]
o_dual = [1,4,2,2,2,2,36,6,16,8,2,4,2,2,2,2].
```

The least common multiple of each profile is 144. Equivalently, the
least positive multiplier of a coordinate vector is the least common
multiple of the reduced denominators in the corresponding column of M^-1
(or row of M^-1 for the dual profile). The global denominator of M^-1 is
144 and it has 43 nonzero entries.

This theorem is restricted to the frozen 16-type support. It does not choose
a canonical Smith basis, classify the full table of marks, or make arithmetic
or Euler/root-number claims.
