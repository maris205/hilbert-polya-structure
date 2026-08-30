# HCS-C250 — Ermakov–Pinney isotonic action atlas (Route A)

This package freezes the positive-component Hamiltonian

\[
  \dot x=v,\qquad \dot v=-\omega^2x+\kappa x^{-3},
  \qquad x>0,\;\omega>0,\;\kappa\ge0.
\]

The theorem-scale step is an explicit nonlinear superposition formula.  If
\(u=\cos(\omega t)\), \(z=\sin(\omega t)/\omega\), then every receipt has
\(x^2=a u^2+2buz+cz^2\) with \(ac-b^2=\kappa\).  Consequently the radial
variable has exact turning radii, primitive period \(\pi/\omega\), and
isotonic action \(J=E/(2\omega)-\sqrt\kappa/2\).  The equilibrium,
\(\kappa=0\), zero-frequency, and negative-\(\kappa\) faces are recorded
separately.

The evidence is source-local mechanics.  It contains no target arithmetic,
Euler factor, root number, automorphy statement, target divisor, or
Hilbert–Pólya operator; accordingly Route B is disabled.

Reproduce from this directory with:

```text
python3 -B code/c250_ep_producer.py
python3 -B code/c250_ep_checker.py
python3 -B code/c250_ep_sympy_crosscheck.py
python3 -B code/c250_ep_replay.py
python3 -B code/c250_ep_mutation.py
python3 -B code/c250_release_manifest.py
```

The final manuscript is [paper/main.pdf](paper/main.pdf).
