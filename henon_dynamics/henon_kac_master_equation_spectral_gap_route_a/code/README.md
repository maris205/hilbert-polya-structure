# Code lanes

- `c322_kac_producer.py` constructs exact sphere moments, conditional polynomials, gap receipts, and polynomial Gram/`Q` forms.
- `c322_kac_checker.py` imports no producer code and reconstructs all receipts with separately organized expansions.
- `c322_kac_sympy_crosscheck.py` checks a disjoint symbolic basis.
- `c322_kac_replay.py` requires byte-identical regeneration.
- `c322_kac_mutation.py` applies repaired-hash theorem, normalization, parser, matrix, and provenance attacks.
- `c322_release_manifest.py` reruns every lane, rebuilds every PDF twice, and verifies the exact 27-file payload ledger.

All executable lanes fail closed under optimized Python.
