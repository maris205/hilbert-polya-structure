# Implementation Notes — SD-C28

- `sdc28_pure_power_selector.py` is the inventory-blind candidate core.
- `sdc28_evaluator.py` alone contains prime and control predicates.
- Exhaustive word ledgers use deterministic length-lexicographic order.
- All matrices, ranks, traces, characteristic determinants, sums, and
  products use exact integers, `Fraction`, or SymPy rational arithmetic.
- The aggregate adversary deliberately separates scalar-pencil success from
  necklace-resolved failure. It must remain in every regression run.
- The de Rham fixtures use the inherited contraction
  `q_n=2^{-ell(n)}` and weight `n^{-2}`. Polynomial truncations certify the
  chain identity, every frozen power, and the characteristic quotient.
- The countable theorem is represented by finite exact prefixes plus the
  analytic l1 majorant; finite prefixes are not promoted to a convergence
  proof.
- The canonical runner executes generator, tests, and analyzer twice with
  `PYTHONHASHSEED=0`, removes caches, compares code/results snapshots, writes
  the integrity audit, and finally freezes the SHA ledger.
- The double-run certificate covers code and generated results only. It does
  not claim byte identity for manuscript or documentation files.
- Git is outside the integrator scope. Route metadata therefore retains the
  paired `PENDING_FIRST_ARTIFACT_COMMIT` two-stage placeholders.
