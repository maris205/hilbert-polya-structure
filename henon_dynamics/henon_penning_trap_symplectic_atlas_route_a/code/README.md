# HCS-C274 executable audit

Run from the repository root with Python bytecode disabled:

```bash
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_producer.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_checker.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_sympy_crosscheck.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_replay.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_mutation.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_release_manifest.py
```

The checker imports no producer code.  It reconstructs the canonical
Hamiltonian generator and uses an independent matrix exponential.  The replay
runs the producer in a fresh process and temporary directory.  Every hostile
mutation repairs the payload hash before the independent checker is invoked.
The release command additionally rebuilds every archived revision twice in
fresh directories at `SOURCE_DATE_EPOCH=1788220800`, checks warning-free logs
and embedded subset fonts, and closes the self-excluded 27-file ledger.
