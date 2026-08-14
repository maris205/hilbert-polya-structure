# Implementation Notes — SD-C31

- Candidate core and independent evaluator are separate Python modules.  The
  evaluator imports neither the core nor the generator and re-derives all
  decisive rational formulas from serialized ledgers.
- Claim-bearing arithmetic uses `fractions.Fraction`.  Oscillation is stored
  as an exact frequency ratio and rational-times-squarefree-radical amplitude;
  no sampled cosine value decides a claim.
- The source-cover predicate derives the active inventory.  Numeric roof marks
  are transported coefficient data and never decide atom membership.
- Finite source recompilation and ambient-compilation/active-cutoff restriction
  are separate.  Direct finite Grams are control fixtures, not claimed to be
  compressions of the infinite divisibility Gram.
- Every CSV is UTF-8/LF.  Canonical runs set `PYTHONHASHSEED=0` and
  `PYTHONDONTWRITEBYTECODE=1`, clear only this paper's `results/`, remove local
  caches, perform two fresh runs, then audit and freeze SHA-256.
- The Route-A YAML begins with paired `PENDING_FIRST_ARTIFACT_COMMIT` values.
  A later metadata-only sealing stage may replace all three with one immutable
  artifact commit; mixed provenance is rejected.
