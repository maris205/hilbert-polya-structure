# C171 exact-validation plan

This is a theorem-validation workflow, not a parameter-fitting experiment.

## Gates

1. Freeze \(P_d\), one-flip clock, uniform measure and determinant convention.
2. Generate exact rational ledgers for every \(1\leq d\leq18\) and
   \(0\leq n\leq24\).
3. Independently reconstruct eigenvalues, multiplicities, traces, returns,
   detailed balance and the Krawtchouk recurrence.
4. Brute-enumerate closed walks for \(d\leq7,n\leq8\).
5. Use SymPy to reconstruct the lumped characteristic polynomial and every
   Krawtchouk eigenvector for \(d\leq12\).
6. Require byte-identical producer replay and rejection of repaired-hash plus
   stale-hash mutations.
7. Compile three materially different manuscript rounds and require the final
   PDF to be deterministic in two empty build directories, with embedded
   fonts and no layout, reference or glyph warnings.
8. Close a self-excluded 27/27 content manifest.

## Commands

```bash
python code/c171_ehrenfest_producer.py
python code/c171_ehrenfest_checker.py
python code/c171_sympy_crosscheck.py
python code/c171_replay.py
python code/c171_mutation.py
python code/c171_release_manifest.py
```

Finite checks are regression sentinels.  The proof in `THEOREM_PACKAGE.md`
carries the all-\(d\) claim.
