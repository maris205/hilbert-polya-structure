# C318 executable lanes

- `c318_ssh_producer.py`: deterministic exact/high-precision evidence.
- `c318_ssh_checker.py`: producer-independent strict parser and theorem
  checker using a site continuant, exact Sturm counts, direct block
  equations, independent Taylor propagation, and semantic/raw-byte locked
  YAML semantics.
- `c318_ssh_sympy_crosscheck.py`: independent symbolic prefactor, edge,
  threshold, face, block-power, Bloch, and quench identities.
- `c318_ssh_replay.py`: two isolated producer executions and byte comparison.
- `c318_ssh_mutation.py`: repaired-hash semantic plus raw JSON/YAML attacks,
  including global OBC scaling and odd-ring sampled-gap regressions.
- `c318_release_manifest.py`: 27-payload/28-physical-file closure,
  deterministic paper rebuilds, warning/font/raster checks, and SHA-256
  ledger.

All lanes refuse `python -O`.  The independent lanes do not import the
producer.  Run with `python -B` to suppress bytecode sidecars.
