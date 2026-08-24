# C132 — Order-sensitive Möbius dynamics on Bergman space

C132 freezes the nonlinear two-branch system

\[
\phi_a(z)=\frac1{a+z},\qquad a\in\{3,6\},
\]

on the unit disk and the composition sum
`L f=f(phi_3)+f(phi_6)` on normalized Bergman space.  Both branch images are
strictly inside the disk and are separated by the exact gap `1/20`.  A basis
nuclear decomposition proves that `L` is trace class with the explicit coarse
bound `||L||_1<=89/16`.

For every finite word, its integer Möbius matrix gives the unique fixed point,
quadratic discriminant, multiplier, and composition trace.  These all-word
identities yield `Tr(L^n)` and a primitive Fredholm product with raw absolute
convergence for `|z|<1/2`; the trace-class determinant itself is entire.

The same-count words `33366` and `33636` are not cyclic rotations.  Their
matrices have traces `1344` and `1317`, so their multipliers and composition
traces differ.  This is intrinsic nonlinear order sensitivity, not an added
phase label.

## Reproduce

```bash
python3 code/c132_mobius_bergman_producer.py
python3 code/c132_mobius_bergman_checker.py
python3 code/c132_sympy_crosscheck.py
python3 code/c132_replay.py
python3 code/c132_mutation.py
```

Strict tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`.
Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`; `route_b_invocation_allowed: false`.
