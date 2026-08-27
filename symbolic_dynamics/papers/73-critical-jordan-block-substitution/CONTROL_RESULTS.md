# Deterministic control results

Command: `python3 code/verify_critical_jordan.py`.

The exact control checks the characteristic/Jordan/Perron identities and
supertile sums through level 32, plus the pointwise periodic-envelope identity
through level 8.  Starting only from the three substitution images, it builds
the legal `2 x 2` patch closure with exact sizes `3 -> 13 -> 20 -> 20` and
then constructs all 63 legal `3 x 3` patches.  Their four phase classes have
sizes 18, 20, 15, and 10 and are pairwise disjoint.  Status: **PASS**.
