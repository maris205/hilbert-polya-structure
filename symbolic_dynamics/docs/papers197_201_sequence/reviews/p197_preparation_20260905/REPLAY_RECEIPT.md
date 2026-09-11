# Preparation probe replay

2026-09-05 UTC. Two fresh Python processes ran
`python3 docs/papers197_201_sequence/reviews/p197_preparation_20260905/probe_preparation.py`
from the workspace root. Both exited zero; their entire stdout was
byte-identical, and that stdout is saved in `CANONICAL.txt`.

- Assertions per run: 24,676.
- Probe SHA-256: `43194e42dcecc19bdc9037ecd5a344ee3839f0ea0929df261099fa0d478c4d14`.
- Stdout SHA-256: `61f430b16c3d24330ab74b35634563173a50d855a67ec8a1614188c65e1bdf15`.

This probe has no author imports and does not depend on mutable draft
bytes. It is pre-Round-0 preparation and counts as zero paper reviews.
The full future Review A plan in `ATTACK_PLAN.md` has not yet been run.
