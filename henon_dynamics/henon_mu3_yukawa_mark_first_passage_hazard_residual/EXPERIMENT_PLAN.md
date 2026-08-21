# Experiment plan

1. Rebind the C88 receipt and manifest by exact SHA-256 and scope checks.
2. Reconstruct each of the twenty first-passage distributions from C88 hit
   bitsets and derive `A_k`, hazards, and survival counts.
3. Emit all `20 x 17` hazard rows and all `20 x 17 x 17` residual grids using
   canonical JSON and reduced rational numbers.
4. Run the independent checker, SymPy cross-check, deterministic replay, and
   hostile mutation suite.
5. Compile the short theorem paper twice in isolated temporary directories and
   freeze a manifest over the non-generated package files.
