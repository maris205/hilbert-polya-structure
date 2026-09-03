# Exact evidence plan

## Objective

Build a finite, exact receipt that exercises every algebraic branch of the
analytic theorem without presenting sampling as a proof of the continuum
claim.

## Lanes

1. Generate rational parameter cases using `ell2=(L/pi)^2`, so every sampled
   Neumann value `mu_n=n^2/ell2` is rational.
2. Record the exact equilibrium, Jacobian invariants, `B`, `Q`, modal traces
   and determinants, all unstable indices, every neutral index, and the
   independently evaluated strict floor/ceiling count.
3. Recompute all rows in a producer-independent checker.
4. Use SymPy to verify the equilibrium, Jacobian, determinant polynomial,
   equal-diffusion identity, and designed neutral/double-wall cases.
5. Replay the producer in two isolated temporary directories and compare
   bytes.
6. Repair the payload hash after hostile mutations and require rejection of
   theorem, mode, evaluator, YAML, serialization, and scope attacks.

## Frozen cases

The grid contains kinetic instability, kinetic neutrality, equal diffusion,
continuous-window/no-discrete-mode, one-mode, two-mode, separate lower- and
upper-endpoint-neutral witnesses, and a double-wall case.  No finite grid is
used to infer arbitrary-parameter existence.
