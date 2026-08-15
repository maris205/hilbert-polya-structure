# Exact audit implementation

This package separates the permitted pre-execution stages from the registered
candidate run.

- `python -B code/scripts/run_safe_preflight.py` runs P0--P2 only: immutable
  bindings, executable isolation, symbolic proof contracts, finite-field
  checks, exact controls, and the hash-plus-semantic upstream regression.
- `python -B code/scripts/run_registered_audit.py` is fail-closed.  It will not
  evaluate the frozen candidate unless `results/CODE_REVIEW.md` contains one
  canonical independent `DEPLOYMENT_PASS` authority line bound to both the
  v2 source lock and the current reviewed code-tree digest.
- `python -B code/scripts/build_result_manifest.py` is post-run only.

The registered periods are fixed at 2--7 and have no command-line override.
The exact least-period root set uses the frozen radical/set-difference formula;
formal dynatomic polynomials and scheme multiplicities are diagnostics only.
All arithmetic is exact.  The code has no network, floating-orbit, external
target-table, or dynamic-import path.

The reviewed tree is a closed file allowlist and rejects symlinks, special
files, bytecode, and cache artifacts.  Run tests with bytecode disabled, e.g.
`PYTHONDONTWRITEBYTECODE=1 python -m pytest`, before requesting review.
