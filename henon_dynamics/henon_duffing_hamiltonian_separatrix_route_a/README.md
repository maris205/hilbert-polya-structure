# HCS-C232 — Duffing energy topology and homoclinic boundary

This paper closes one complete theorem-scale step for a conservative nonlinear
oscillator:

\[
 \dot x=v,\qquad \dot v=-\delta x-\beta x^3,\qquad \beta>0.
\]

It classifies every regular energy component in the single-well and
double-well regimes, gives the exact turning-root formula, period/action
quadratures, the action derivative, center and quartic scaling limits, and the
explicit homoclinic separatrix.  The lower-dimensional `beta=0` faces are
kept separate.

The result is a source-native Hamiltonian atlas, not a claim about an
arithmetic zeta.  A continuum of real-energy ovals is not an isolated
primitive-orbit owner.  The strict Route-A tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B is false under
the scope firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.

Reproduce from this directory:

```bash
python -B code/c232_duffing_producer.py
python -B code/c232_duffing_checker.py
python -B code/c232_duffing_sympy_crosscheck.py
python -B code/c232_duffing_replay.py
python -B code/c232_duffing_mutation.py
python -B code/c232_release_manifest.py
```

The paper is [paper/main.pdf](paper/main.pdf); canonical evidence is
`results/c232_duffing_evidence.json`, and the release ledger is
`C232_RELEASE_MANIFEST.json`.
