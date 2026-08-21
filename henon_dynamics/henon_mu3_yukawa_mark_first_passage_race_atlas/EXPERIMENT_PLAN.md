# C91 finite experiment plan

1. Rebind the C75, C83, C85, and C88 receipts by exact SHA-256 digest.
2. Decode all twenty C88 hit bitsets on all 65,536 support masks.
3. Enumerate the 108 unordered incomparable target pairs from the frozen
   inclusion matrix.
4. For every pair, enumerate all first-hit boundary edges.  A rank-`k` edge
   contributes `(k-1)!(16-k)!` permutations.  Separate left-only, simultaneous,
   and right-only boundary events.
5. Emit canonical JSON with pair totals, probabilities, rank-resolved counts,
   edge counts, and partition identities.
6. Rebuild the receipt independently, check exact rational generating
   functions with SymPy, replay in a clean process, and reject hostile field
   mutations.
7. Compile the finite theorem note twice in isolated directories and verify
   the resulting PDF and fonts.

No simulation, fitted parameter, arithmetic/local-data assertion, Euler
factor, root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Polya
operator claim is part of C91.
