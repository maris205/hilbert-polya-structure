# C223 -- exact excitation blocks for Jaynes--Cummings dynamics

This package proves the conserved-excitation decomposition of the rotating-
wave Jaynes--Cummings Hamiltonian, including the separate vacuum, every
two-dimensional dressed block, its spectrum and unitary propagator, bare-state
transition probability, finite-support revival conditions and all singular
parameter/cutoff boundaries.

From this directory run:

```text
python3 -B code/c223_jaynes_cummings_producer.py
python3 -B code/c223_jaynes_cummings_checker.py
python3 -B code/c223_jaynes_cummings_sympy_crosscheck.py
python3 -B code/c223_jaynes_cummings_replay.py
python3 -B code/c223_jaynes_cummings_mutation.py
python3 -B code/c223_release_manifest.py
```

The full Fock-space unitary is explicitly distinguished from its finite
blocks: it is noncompact and not Schatten, and no ordinary trace or Fredholm
determinant is claimed.  The strict verdict is `ROUTE_A_REJECTED`; natural
quantization of the source model is not a Hilbert--Polya bridge.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
