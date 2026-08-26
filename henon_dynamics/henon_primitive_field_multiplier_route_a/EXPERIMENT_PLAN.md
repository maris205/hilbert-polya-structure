# C172 exact-validation plan

This package validates an all-prime-power theorem; it does not fit data.

## Gates

1. Freeze \(Q\), primitive \(a\), multiplication clock, fixed-point
   convention and Koopman convention.
2. Generate exact ledgers for 18 representative prime powers, including
   non-prime fields, and fixed counts through \(n=24\).
3. Independently reconstruct prime-power provenance, abstract exponent-cycle
   dynamics, fixed counts, determinants, controls and the \(Q\leq3\)
   self-adjoint boundary.
4. Use SymPy permutation matrices to verify determinant, unitarity,
   self-adjointness and 24 traces for every sentinel \(Q\).
5. Require byte-identical replay and rejection of repaired/stale-hash attacks.
6. Compile three materially different paper rounds, then compile final source
   twice in empty directories at a fixed epoch; require byte identity, embedded
   fonts and zero layout/reference/glyph warnings.
7. Close the self-excluded 27/27 release manifest.

## Commands

```bash
python code/c172_field_multiplier_producer.py
python code/c172_field_multiplier_checker.py
python code/c172_sympy_crosscheck.py
python code/c172_replay.py
python code/c172_mutation.py
python code/c172_release_manifest.py
```

The finite ledger is a regression sentinel.  Cyclicity of
\(\mathbb F_Q^\times\) and the proof in `THEOREM_PACKAGE.md` carry the
all-parameter result.
