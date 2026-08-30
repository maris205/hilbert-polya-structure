# Hostile audit

The 40 mutations in `code/c251_majority_mutation.py` all terminate in checker
failure.  They include:

- altered schema, candidate, date, source commit, evaluator, or fixed epoch;
- repaired-hash changes to the frozen rule, clock, wall convention, matrices,
  Lucas/cosine rows, parity traces, state histograms, trajectories, and truth
  table;
- changed theorem and identity prose, route tuple/verdict, Route-B flag, and
  scope flag;
- altered citation DOI/URL, nonclaim, unknown key, missing row, and stale
  payload hash.

No mutation is silently accepted.  This is an internal integrity audit, not an
external peer review.
