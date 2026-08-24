# C128 — Finite metaplectic quantization of a toral Hénon map

C128 constructs a natural, exact quantum lift of

\[
A=\begin{pmatrix}3&-1\\1&0\end{pmatrix},\qquad
H(x,y)=(3x-y,x)\pmod 1,
\]

at the frozen odd level `N=7`.  On `C^7`, an explicit chirp--Fourier unitary
obeys all 49 Weyl Egorov identities, preserves the discrete clock, and has an
exact antiunitary reversor.  This is the first package in the local series to
meet the narrowly defined `A4_NATURAL_QUANTIZATION` gate.

An exact convention control also proves that the literal `q*p/2` Weyl phase
cannot be copied unchanged to even modulus because two has no inverse there.
This does not exclude separately defined doubled-phase even-level conventions.

The same exact construction exposes a negative result: `U^8=I`, so the
finite-level traces are 8-periodic and cannot reproduce the exponential
growth of the real-torus fixed-point counts.  The paper therefore does not
claim a Hilbert--Pólya operator or authorize Route B.

## Reproduce

```bash
python3 code/c128_metaplectic_producer.py
python3 code/c128_metaplectic_checker.py
python3 code/c128_sympy_crosscheck.py
python3 code/c128_replay.py
python3 code/c128_mutation.py
```

Strict tuple:
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`.
Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`; `route_b_invocation_allowed: false`.
