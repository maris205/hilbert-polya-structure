# P174 hostile Review B control

This directory contains a second independent exact control for minimum-pivot
Möbius feedback.  It represents each projectivity as a fully materialized
point permutation, each state as a `frozenset`, reconstructs fibres from the
reverse edge relation, and recovers cycles and weak components by generic
orbit tracing and union--find.  It imports no author, scout, or Review-A
code.

Reproduce from this directory with

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 verify_review_b.py
sha256sum -c MANIFEST.sha256
```

Expected terminus: `ASSERTIONS 4755152` followed by
`VERDICT EXECUTABLE_CLAIMS_PASS`.  The run exhausts 51 complete parameter
boxes through `p=17` (282,889 states) and separately checks the no-wrap and
count identities for every prime through 101.  Finite execution is not an
all-parameter proof or owner/novelty evidence.  Lifecycle:
`PROVISIONAL_AMBER / HOLD_EXTERNAL`.
