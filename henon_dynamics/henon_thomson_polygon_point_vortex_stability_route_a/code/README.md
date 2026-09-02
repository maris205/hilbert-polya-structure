# C284 executable map

- `c284_point_vortex_producer.py` emits canonical sorted JSON from the proved
  integer mode formula and appends a self-excluding payload SHA-256.
- `c284_point_vortex_checker.py` is producer-independent.  It constructs the
  logarithmic pair Hessian in raw Cartesian coordinates for every `N=3..64`,
  checks the rotating equilibrium, rotates all `2 by 2` blocks to local
  frames, proves block circulancy numerically, performs the DFT, and applies
  the raw Hessian/linearization to explicit symmetry-slice vectors.  Its JSON
  loader rejects duplicate and nonstandard input, and its exact schemas reject
  unknown, missing, wrongly typed, reordered, or semantically duplicated rows.
- `c284_point_vortex_sympy_crosscheck.py` differentiates and transforms exact
  raw Hessians for `N=3,4,6`, verifies exact slice actions, and reconstructs
  all root-sum cells by coefficient counting independently.
- `c284_point_vortex_replay.py` writes the evidence on two unrelated fresh
  paths and requires byte equality with the archive.
- `c284_point_vortex_mutation.py` repairs payload hashes after semantic,
  schema, type, order, and duplicate/drop-replace mutations.  Raw duplicate-key,
  nonstandard-constant, and stale-hash controls must also fail.
- `c284_release_manifest.py` reruns every gate, performs two fresh LuaLaTeX
  builds per manuscript round, checks fonts/text/logs/pages/hashes, and closes
  exactly 27 payload files plus its own manifest.

No checker imports producer code.  Set `PYTHONDONTWRITEBYTECODE=1` or use
`python -B`; bytecode and LaTeX sidecars are not release payloads.
