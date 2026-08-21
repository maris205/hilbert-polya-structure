# C83 experiment plan

1. Bind C76/C78 (and the frozen C81 receipt) by raw-byte SHA-256.
2. Reconstruct the C75 point-set closure for all 65536 subsets.
3. For every full-core subset count pivotal labels, then convert the counts
   to exact uniform-permutation stopping counts using factorial weights.
4. Verify the complete distribution, survival counts, reduced probabilities,
   and exact expectation with an independent checker and SymPy polynomial.
5. Run replay and hostile mutations, compile twice, inspect the PDF, and freeze
   a manifest.

Only finite named-support combinatorics are in scope.
