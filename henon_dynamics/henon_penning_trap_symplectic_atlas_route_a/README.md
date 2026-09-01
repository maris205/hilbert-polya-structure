# HCS-C274 — Ideal Penning-trap symplectic atlas

This package proves a complete parameter-and-boundary theorem for the ideal,
axially symmetric Penning Hamiltonian.  It gives the exact six-dimensional
canonical flow, the sharp magnetic-confinement threshold, the critical Jordan
face, the unstable splitting, signed stable-mode actions and Krein signs, and
the full active-mode resonance/minimal-period/strobe-fixed-space atlas.

The theorem status is **PROVABLE AS STATED**.  The package is deliberately
candidate-local: it does not extend to imperfect traps, damping, many-body
motion, or experimental accuracy.

## Frozen result

With signed cyclotron frequency `c`, axial frequency `zeta >= 0`, and
`Delta = c^2 - 2 zeta^2`, the radial rotating-frame equation is

```text
w'' + Delta w/4 = 0.
```

Consequently `Delta > 0`, `Delta = 0`, and `Delta < 0` give respectively the
bounded, critical-Jordan, and radially unstable chambers.  All zero-field,
zero-axial, free, and field-sign-reversal boundaries are part of the theorem.

The strict Route-A tuple is

```text
(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
```

and the overall verdict is `ROUTE_A_REJECTED`; Route B is not invoked.  The
scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

Run from the repository root:

```bash
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_producer.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_checker.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_sympy_crosscheck.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_replay.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_penning_mutation.py
python -B henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/code/c274_release_manifest.py
```

The independent checker does not import producer code.  The evidence receipt
contains 48 full `6 x 6` flow matrices, 24 stable-mode/action rows, 13 strobe
rows, 7 minimal-period rows, 9 boundary rows, and 2,743 explicitly recounted
numeric cells.

## Claim boundary

The analytic proof establishes the continuum theorem; the finite receipt is a
deterministic regression witness.  Clean resonant invariant tori are not
renamed isolated primitive orbits.  Natural canonical quantization of the
ideal trap is not promoted to a Hilbert--Polya operator, target divisor, or
target determinant.
