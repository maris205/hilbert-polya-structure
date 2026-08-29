# HCS-C234 — constant-field Landau–Lifshitz–Gilbert sphere flow

This source-local Route-A package closes the exact unit-sphere ODE
\(\dot m=-\omega m\times e_3-\alpha\omega m\times(m\times e_3)\),
\(\alpha,\omega\geq0\).  Stereographic coordinates linearize the flow,
while the north/south pole stability, energy dissipation, latitude-periodic
face, identity face, and sampled-time fixed sets are kept separate.

The arithmetic/target firewall is literal `NO_BAD_EULER_OR_ROOT_NUMBER`.
The continuous latitude circles are not an isolated primitive-orbit owner and
no Hilbert–Pólya or target-divisor statement is made.

Reproduce the receipt with:

```text
python3 -B code/c234_llg_producer.py
python3 -B code/c234_llg_checker.py
python3 -B code/c234_llg_sympy_crosscheck.py
python3 -B code/c234_llg_replay.py
python3 -B code/c234_llg_mutation.py
python3 -B code/c234_release_manifest.py
```

The final paper is `paper/main.pdf`; the three revision artifacts are retained
for deterministic build comparison.
