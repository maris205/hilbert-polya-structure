# Deterministic controls

`packet_trace_controls.py` is the standard-library-only regression layer for
Paper 7. It generates nine finite, target-free controls and a hash manifest.
The tests exercise the same pure functions and verify byte-for-byte repeatability.

Run from this directory:

```bash
python3 -m unittest -v test_packet_trace_controls.py
python3 packet_trace_controls.py --output-dir ../results --max-prime 5000
python3 packet_trace_controls.py --output-dir ../results --verify-only
```

The Fourier convention is
`fhat(xi) = integral f(t) exp(-i t xi) dt`. The Gaussian calculation is a
Schwartz-class normalization control. It does not numerically prove the
compactly supported theorem target.

The finite positive-real determinant convention is explicit throughout the
public interface and generated tables:

```text
tau_Log_D = sum_j m_j log(1-exp(-sigma*L_j)) < 0
log_Z     = -tau_Log_D > 0
D         = exp(tau_Log_D)
Z         = exp(log_Z) = D**(-1)
```

Canonical functions are `tau_log_d_exact`, `log_z_exact`,
`compiled_d_product`, and `compiled_z_product`. The legacy
`trace_log_*`/`compiled_inverse_product` names remain compatibility wrappers
only; their docstrings identify their outputs as `log_Z`/`Z`. Finite
sign/product agreement checks an identity inside the selected proxy; it does
not establish that the source flow owns the algebra, trace, mass
normalization, projection, or determinant.

`--verify-only` checks every generated table and requires the manifest's
`implementation_files` keys to equal the frozen reproduction-file set. It
then hashes the current files relative to the Paper 7 root. The manifest is
deliberately excluded from that set, avoiding self-reference.

No network, random generator, Riemann-zero data, fitting, or external package
is used.
