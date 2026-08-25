# C157 code

- `c157_abel_trace_producer.py`: exact primitive/repetition shell evidence and
  high-precision primal/accelerated-dual sentinels.
- `c157_abel_trace_checker.py`: independent shell solver and larger-cutoff
  deterministic numerical checker with analytic truncation envelopes and a
  `1e-34` comparison margin; `--quick` is for hostile tests only.
- `c157_sympy_crosscheck.py`: Fourier constant, branch scaling, boundary-pole
  residue, and third shell path.
- `c157_replay.py`: fresh-path byte replay.
- `c157_mutation.py`: repaired-hash semantic attacks and stale-hash control.
- `c157_release_manifest.py`: self-excluded release ledger.

Claim-bearing shell arithmetic is exact; every numerical comparison carries
an explicit deterministic tail bound.
