# Planned code package

No implementation is claimed complete. Code will be added only after R001 is
frozen.

Planned modules:

- `henon_action.py`: exact map, generating function, action gauge, monodromy,
  cyclic Hessian (with dedicated \(n=1,2\) cases), action, and Maslov data.
- `local_survivor.py`: read and independently validate the R058/R059 state
  graph and orbit coordinates.
- `quantum_kernel.py`: high-order quadrature for the exact Hénon kernel and
  chronological direct-sum localization.
- `periodic_trace.py`: fixed-point stationary-phase trace and repeated-orbit
  amplitudes.
- `weyl_obstruction.py`: analytic constants and numerical quartic counting
  sanity checks.
- `run_experiment.py`: immutable-config run entry point.
- `run_controls.py`: cutoff, quadrature, adjacency, action, amplitude, and
  boundary controls.
- `check_manifest.py`: source/input hashes, no-target dependency scan, and gate
  validation.

Implementation rules:

- no imports of Riemann-zero or prime tables;
- no fitted global phase or energy-unwrapping index;
- no periodic FFT box in the main computation;
- no silent use of the full two-shift;
- source-row/target-column orientation must pass a non-palindromic word test;
- branch \(\sqrt i=e^{i\pi/4}\), global phase, subprincipal convention,
  cutoff type, and trace-class theorem version must be stored in every config;
- all complex traces computed independently from quantum matrices and orbit
  data;
- all configs and results machine-readable and content-addressed.
