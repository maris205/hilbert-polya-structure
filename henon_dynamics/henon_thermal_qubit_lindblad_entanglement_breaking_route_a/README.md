# HCS-C303 — thermal qubit Lindblad semigroup

This package closes one all-parameter theorem for a phase-covariant qubit
GKSL semigroup with relaxation, thermal excitation, pure dephasing, and a
Hamiltonian phase.  The advance is not a fragment of a larger calculation:
it gives the exact channel, Liouvillian spectrum, sharp trace-distance
contraction coefficient, normalized Choi state, necessary-and-sufficient
entanglement-breaking condition, unique finite threshold in the faithful
thermal regime, and every degenerate boundary.

The pure-dephasing convention is frozen:

\[
 \frac{\gamma_\phi}{2}(\sigma_z\rho\sigma_z-\rho)
\]

contributes exactly `gamma_phi` to the decay rate of `rho_01`.  Consequently
`Gamma2=Gamma1/2+gamma_phi`.

The mathematical theorem is **PROVABLE AS STATED**.  The Route-A result is
negative and equally definite:

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and
`ROUTE_A_REJECTED`, with Route B locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

From this directory run:

```bash
python -B code/c303_thermal_qubit_producer.py
python -B code/c303_thermal_qubit_checker.py
python -B code/c303_thermal_qubit_sympy_crosscheck.py
python -B code/c303_thermal_qubit_replay.py
python -B code/c303_thermal_qubit_mutation.py
python -B code/c303_release_manifest.py
```

The release contains exactly 27 manifest payloads and 28 physical files after
including `C303_RELEASE_MANIFEST.json`.

## Scope

No target arithmetic local datum, Euler factor, root number, automorphy,
target divisor/counting law, functional equation, target zero match, or
Hilbert–Pólya operator is asserted.  Finite Choi and Liouvillian determinants
remain finite-dimensional source data.
