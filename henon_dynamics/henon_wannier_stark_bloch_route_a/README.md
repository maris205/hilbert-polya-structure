# HCS-C267 — Wannier–Stark Bloch oscillations

This source-local Route-A certificate closes the one-dimensional uniform-field tight-binding Hamiltonian
`(Hψ)_n=Fnψ_n-J(ψ_{n+1}+ψ_{n-1})` on `ell^2(Z)`, for every real `J` and every real `F != 0`.
It proves the Fourier gauge conjugacy, simple ladder spectrum, Bessel eigenbasis, exact propagator and least
full-space return, delta-source shell law, and the sharp compactness/Schatten boundaries.  The finite receipt
is a regression oracle only; all infinite-dimensional conclusions have analytic proofs.

Run, from this directory:

```bash
python3 -B code/c267_wannier_producer.py
python3 -B code/c267_wannier_checker.py
python3 -B code/c267_wannier_sympy_crosscheck.py
python3 -B code/c267_wannier_replay.py
python3 -B code/c267_wannier_mutation.py
python3 -B code/c267_release_manifest.py
```

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Verdict: `ROUTE_A_REJECTED`; Route B is disabled.
