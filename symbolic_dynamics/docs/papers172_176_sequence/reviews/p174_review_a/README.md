# P174 hostile Review A control

This directory contains an independent bit-mask implementation of the
minimum-pivot Möbius dynamics.  It imports no author or scouting code and is
review evidence only.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a.py
sha256sum -c MANIFEST.sha256
```

Expected terminus: `ASSERTIONS 161536`, `RESULT PASS`.  Finite verification
is not an all-parameter proof or a novelty certificate.  Lifecycle:
`HOLD_EXTERNAL`.
