# C382: primary CM Frobenius phases and all-degree native zeta

Status: PROVED_AS_STATED, exact source theorem with independent evidence.

For E:y²=x³−x at every odd prime, rational four-torsion fixes the primary Gaussian trace sign. Ordinary normalized phase is irrational; supersingular phase has exact order four. Every extension count and primitive closed-point degree follows, including the complete classification of Hasse endpoint degrees. The full H0/H1/H2 determinant has its native functional equation and critical circle. Fixed-fibre zero count is linear, producing obstruction HEN-O366 to a Riemann-target divisor.

This is a classical-theorem synthesis and a new complete local package, not a claim of literature priority. The native theorem does not change strict target gates: (A0_STRUCTURAL_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT), overall ROUTE_A_EXPLORATORY.

[Final paper](paper/main.pdf), [full proof](proof/ANALYTIC_PROOF.md), [exact evidence](results/c382_cm_evidence.json), [release manifest](C382_RELEASE_MANIFEST.json).

Reproduce with `python -B code/c382_release_manifest.py`; rebuild with `python -B code/c382_release_manifest.py --write --build-pdfs`.

Finite evidence: all 167 odd primes ≤1000 and degrees 1–24 (4008 cells), plus quadratic-extension recounts for 13 odd primes ≤43. These tests do not replace the proof. Scope: NO_BAD_EULER_OR_ROOT_NUMBER.
