# C308 code lanes

- `c308_hatano_nelson_producer.py` deterministically emits the canonical exact evidence and its semantic self-hash.
- `c308_hatano_nelson_checker.py` independently recomputes every cell, rejects duplicate/nonfinite/noncanonical/type-confused JSON, strictly parses and pins the Route-A YAML, and refuses `python -O`.
- `c308_hatano_nelson_sympy_crosscheck.py` independently checks continuants, Chebyshev identities, diagonal similarity, biorthogonality, cyclic normality, and Jordan ranks.
- `c308_hatano_nelson_replay.py` regenerates the evidence twice in isolated temporary paths and requires byte identity with the release evidence.
- `c308_hatano_nelson_mutation.py` runs repaired-hash semantic attacks, raw parser attacks, and stale-hash controls.
- `c308_release_manifest.py` is the final closed-world 28-file/27-payload release gate.

Run all commands from the package root with Python 3. The checker and symbolic/mutation lanes intentionally fail under optimization because their assertions are part of the executable contract.
