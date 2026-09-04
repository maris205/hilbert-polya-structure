# HCS-C367 — two-state reflected Markov fluid

This self-contained package proves a sharp recurrence trichotomy and reconstructs the complete stable stationary law of a two-state reflected Markov fluid.  It includes an exact zero-rate boundary atlas and deterministic release evidence.

Its nearest workspace neighbors are C351 (discrete Jackson networks), C346 (a deterministic two-dimensional oblique Skorokhod map), and C332 (deterministic scalar play hysteresis).  None is a Markov-additive reflected fluid; the exact boundary is recorded in `SOURCE_AUDIT.md` and locked by repaired-hash mutations.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c367_release_manifest.py
```

To regenerate all evidence and PDFs:

```bash
SOURCE_DATE_EPOCH=1788480000 PYTHONDONTWRITEBYTECODE=1 \
  python3 -B code/c367_release_manifest.py --write --build-pdfs
```

The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  Route A is rejected at all five gates, and Route B is not invoked.
