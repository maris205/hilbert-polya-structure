# HCS-C236 — sine--Gordon kink and breather coherent families

This source-local Route-A package closes a declared, exact coherent-family
theorem for
\[
 u_{tt}-u_{xx}+\sin u=0\quad (x\in\mathbb R).
\]
It covers the monotone finite-energy travelling heteroclinics (all integer
vacuum layers of the Lorentz kinks/antikinks), exact rest and boosted breathers, the topological charge and
energy--momentum ledger, and the factored rest-kink Hessian.  The scope is
deliberately *not* a classification of every finite-energy solution.

The clock warning is part of the theorem: $2\pi/\Omega$ is the rest-frame
(comoving) breather period.  A boosted breather has no asserted strict period
at a fixed laboratory $x$ when $V\ne0$.  No primitive periodic-orbit owner is
declared, and the literal firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

Reproduce the receipt with:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c236_sine_gordon_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c236_sine_gordon_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c236_sine_gordon_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c236_sine_gordon_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c236_sine_gordon_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c236_release_manifest.py
```

`paper/main.pdf` is the final (round-2) paper; all three round artifacts are
retained for deterministic comparison.
