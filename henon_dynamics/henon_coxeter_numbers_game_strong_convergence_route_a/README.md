# HCS-C286: finite Coxeter numbers-game strong convergence

This package closes one classical finite-type dynamical theorem.  Let
`Phi` be a finite reduced crystallographic root system, let
`x_i=<lambda,alpha_i^vee> >= 0`, and fire node `i` only when `x_i>0` by
replacing `lambda` with `s_i lambda`.  If
`J={i:x_i=0}`, every complete legal play ends at the same anti-dominant
point, uses exactly

```text
|Phi^+| - |Phi_J^+|
```

moves, and accumulates to `w_0 w_J`: the unique shortest representative of
the terminal coset `w_0 W_J`, equivalently the unique maximum among the
minimal right-coset representatives `W^J`.

The theorem covers strict dominance, walls, the zero vector, disconnected
finite systems, and rank one.  Affine and indefinite generalized Cartan
matrices are explicit stopping boundaries, not inferred extensions.

## Reproduce

From this directory:

```bash
python3 -B code/c286_numbers_game_producer.py
python3 -B code/c286_numbers_game_checker.py
python3 -B code/c286_numbers_game_sympy_crosscheck.py
python3 -B code/c286_numbers_game_replay.py
python3 -B code/c286_numbers_game_mutation.py
python3 -B code/c286_release_manifest.py
```

The producer enumerates legal firing paths.  The checker does not replay that
simulation: it reconstructs positive roots, Weyl elements, inversion lengths,
longest elements, parabolic subsystems, the quotient `W^J`, and its weak-order
path ledger.  Thus agreement is producer-independent at the mathematical
mechanism level.

The frozen Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, with overall verdict
`ROUTE_A_REJECTED`; Route B is not authorized.  The scope literal is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
