# Deterministic isotropy-trace controls

`isotropy_trace_controls.py` is the standard-library-only regression layer for
Paper 8. It generates nine target-free CSV controls and a hash manifest. The
tests exercise the same pure functions, validate the final active tuple and
implementation hashes, and compare two fresh generations byte for byte.

Run from this directory:

```bash
python3 -m unittest -v test_isotropy_trace_controls.py
python3 isotropy_trace_controls.py --output-dir ../results
python3 isotropy_trace_controls.py --output-dir ../results --verify-only
```

The active conventions are

```text
fhat(xi) = integral_R f(t) exp(-i t xi) dt
chi_theta(rL) = exp(+i r theta)
xi(u+rL) = exp(-i r theta) xi(u)
frequency_n = (2 pi n - theta)/L
T_theta(f) = L sum_r f(rL) exp(+i r theta).
```

The non-even shifted Gaussian has an analytic Fourier transform and detects
the simultaneous sign. It is explicitly a Schwartz convention control, not a
numerical proof for the compactly supported theorem target. Compact
`C^infinity` bumps handle zero-time, positive-time, and domain controls.

The rank-one-corner tables are finite witnesses only. They record shrinking
continuous peaks in `p A_L p ~= C(T)` and two representatives of the zero
class in `L^infinity(T)` that differ at one point. They do not prove the fixed
regular completion, identify the image of `p`, construct a singular state, or
transport a local obstruction to a packet.

`--verify-only` checks every CSV, the exact active protocol/candidate/amendment
hashes, and the frozen implementation-file set. The manifest is excluded from
its own implementation ledger to avoid self-reference.

No network, random generator, Riemann-zero data, target Euler product, fitting,
external package, packet measure, determinant, or Route evaluation is used.
