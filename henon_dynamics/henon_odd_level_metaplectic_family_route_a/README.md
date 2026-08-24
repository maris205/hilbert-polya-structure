# C131 — Odd-level metaplectic family for the toral Hénon map

C131 lifts the level-seven construction to every odd integer `N>=3` for

\[
A=\begin{pmatrix}3&-1\\1&0\end{pmatrix}.
\]

With one frozen half-phase, Fourier, and chirp convention, the package proves
unitarity, all `N^2` Weyl Egorov identities, exact clock preservation, and one
uniform antiunitary reversor at every odd level.  Nine exact certificate levels
include odd composite moduli and cover 25,313 Weyl observables.

The family also has a growing no-action-alias window.  If
`N > ||A^n-I||_max`, then the modular classical action is not the identity and
`U_N^n` cannot be scalar.  This is an adjoint-action result, not a trace or
semiclassical match.

The literal `q*p/2` convention has no direct even-level extension because two
is not invertible modulo an even integer.  Other even-level Weil/metaplectic
conventions are not excluded.

## Reproduce

```bash
python3 code/c131_odd_metaplectic_producer.py
python3 code/c131_odd_metaplectic_checker.py
python3 code/c131_sympy_crosscheck.py
python3 code/c131_replay.py
python3 code/c131_mutation.py
```

Strict tuple:
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`.
Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`; `route_b_invocation_allowed: false`.
