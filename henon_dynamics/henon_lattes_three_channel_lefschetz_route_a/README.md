# HCS-C180 — Lattès three-channel Lefschetz theorem

This package resolves, in one all-parameter theorem, the quotient dynamics induced by multiplication on every complex elliptic curve.  For every complex elliptic curve (E_\tau), every integer (m\ge2), and every iterate (n\ge1), it classifies every fixed class of the induced Lattès map into the (+m^n), (-m^n), and branch-(m^{2n}) multiplier channels.  It then proves the exact holomorphic Lefschetz sum, Artin--Mazur zeta, primitive-period formula, and Wold model of the natural Haar Koopman isometry.

The mathematical advance over a fixed-count calculation is the simultaneous three-channel multiplier census over the full elliptic moduli family, including the parity-dependent branch overlap.  The result is also a sharp Route-A stop: the counts are independent of \(\tau\), the zeta is elementary, and the natural Koopman operator is a proper noncompact isometry.

Run from the repository root:

```bash
python3 henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/code/c180_lattes_producer.py
python3 henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/code/c180_lattes_checker.py
python3 henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/code/c180_sympy_crosscheck.py
python3 henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/code/c180_replay.py
python3 henon_dynamics/henon_lattes_three_channel_lefschetz_route_a/code/c180_mutation.py
```

The frozen scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. Route B is false. No arithmetic local factor, Euler factor, root number, automorphy, or Hilbert--Pólya claim is made.
