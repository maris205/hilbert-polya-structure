# Cross-audit methodology

The active package `/tmp/p49_tree_stage2` was treated as immutable.  The
cross-audit wrote only below `/tmp/p49_tree_cross_audit` and did not import or
execute any active-package Python module.

The audit used four independent gates:

1. reconstruct C0--C7 from the frozen definitions, with special attention to
   cylinder endpoints, finite-union quantifiers, convolution invertibility,
   finite-level denominators, and excluded graph mutations;
2. verify the active self-excluding manifest, file-set coverage, modes,
   evidence hashes, count ledger, and implementation import separation;
3. independently implement prime-exponent rational log forms, exact integer
   ordering, complete-block recursion, weak compositions, one- and
   multi-level optimizers, `p=2` formulas, and all six negative controls;
4. repeat the primary-source owner audit and take a full active snapshot both
   before and after all reads.

The exact comparer clears rational denominators in a difference of logarithmic
forms and compares the resulting positive integers.  No floating tolerance is
used.  Finite sweeps support the audit but do not replace the universal proof.

`audit_replay.py --capture-before`, `--replay`, and `--verify-after` are the
only replay entry points.  They write only canonical JSON in this audit root.
The cross-audit manifest excludes itself and is checked for exact file-set
coverage, hashes, modes, normalized paths, caches, links, and nonregular
entries.
