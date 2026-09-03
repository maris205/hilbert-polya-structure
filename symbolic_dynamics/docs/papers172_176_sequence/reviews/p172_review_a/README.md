# P172 hostile Review A control

This directory contains an independently implemented exact verifier for the
literal update `A <- A intersection f(A)`.  It uses `frozenset` carriers,
direct enumeration of restrictions, inclusion--exclusion onto counts, sparse
trajectory propagation, coefficientwise mark histories, and fraction-free
rank calculations.  It imports no author, scouting, manuscript, or earlier
paper code.

Reproduce from this directory with

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 verify_review_a.py
sha256sum -c MANIFEST.sha256
```

The expected terminus is `ASSERTIONS 86630` followed by
`VERDICT EXECUTABLE_CLAIMS_PASS`.  Exact finite checks are falsifiers, not
all-parameter proofs, novelty evidence, or an external-release clearance.
Lifecycle: `HOLD_EXTERNAL`.
