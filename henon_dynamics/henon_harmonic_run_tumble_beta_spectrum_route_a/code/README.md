# HCS-C328 executable lanes

- `c328_run_tumble_producer.py` writes the canonical finite receipt.
- `c328_run_tumble_checker.py` independently recomputes beta moments, the full two-by-two stationary correlation matrix, and exact rational generator ranks; it does not import producer code.
- `c328_run_tumble_sympy_crosscheck.py` checks the stationary forward equations, beta integrals, the Jordan correlation limit, characteristic polynomials, and resonance nullities symbolically.
- `c328_run_tumble_replay.py` performs two isolated byte-for-byte evidence reproductions.
- `c328_run_tumble_mutation.py` attacks nested coordinates, canonical encodings, odd/even resonance classes, parsers, and the raw/semantic YAML lock, repairing the payload digest where appropriate.
- `c328_release_manifest.py` is the fail-closed release gate and manifest writer.

Every executable refuses optimized Python.  The finite degree-eight grid is a regression receipt, not the proof of the all-degree theorem.
