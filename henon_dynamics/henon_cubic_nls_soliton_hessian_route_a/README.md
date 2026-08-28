# HCS-C221 — Focusing cubic NLS soliton Hessian

This package is a self-contained Route-A certificate for the one-dimensional
focusing cubic nonlinear Schrödinger equation

\[
i\psi_t+\psi_{xx}+2|\psi|^2\psi=0,\qquad
\psi(t,x)=e^{i\omega t}Q_\omega(x),\quad
Q_\omega=\sqrt\omega\,\operatorname{sech}(\sqrt\omega x),\quad \omega>0.
\]

The theorem closes one complete local spectral owner: the mass, Hamiltonian,
action and Vakhitov–Kolokolov slope; both real Hessians; the exact discrete and
essential spectra; the Morse index and kernels; and the scaled
Pöschl–Teller factorizations.  The \(\omega\downarrow0\), defocusing,
periodic-domain and higher-dimensional faces are explicit.

The numerical receipt is finite regression evidence (15 profile rows, 3
integral rows, 15 spectral rows and 15 factorization rows).  The checker is
producer-independent, the SymPy script is separate, replay is byte exact, and
the mutation harness repairs hashes before semantic/unknown-key tests.  A
finite box discretization is never used as a proof of the continuum spectrum.

The strict evaluator tuple is
\[
(A0,A1,A2,A3,A4)=\texttt{(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)},
\]
with `ROUTE_A_REJECTED` and Route B disabled.  The last entry is only the
natural Hamiltonian quantization hint; no Hilbert–Pólya operator is claimed.
No prime or zero table, arithmetic local datum, Euler factor, root number,
automorphy statement, target divisor, or dynamical-zeta determinant is used.

## Reproduce

From this directory:

```text
python3 code/c221_nls_producer.py
python3 code/c221_nls_checker.py
python3 code/c221_nls_sympy_crosscheck.py
python3 code/c221_nls_replay.py
python3 code/c221_nls_mutation.py
python3 code/c221_release_manifest.py
```

The content-addressed manifest excludes itself, Python bytecode and LaTeX
sidecars.  The three manuscript revisions are built with LuaLaTeX at the fixed
epoch recorded in `paper/COMPILE_REPORT.md`.
