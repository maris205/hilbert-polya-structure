# C164: induced Fredholm owner for the Thue--Morse renewal shift

This package closes the operator-owner question left by C159.  A
branch-resolved rank-one first-return family is trace-norm holomorphic for
`|z|<1` and satisfies

```text
Tr(K_z^m)=F(z)^m,
det_F(I-([z] direct_sum K_z))=(1-z)(1-F(z))=zeta_X(z)^(-1).
```

In contrast, every bounded realization of the uninduced adjacency on a
diagonally weighted `l2(N0,w)` is noncompact and lies in no Schatten class.
The owner cannot extend as a trace-class meromorphic family through a unit-
circle arc.

Run:

```text
python code/c164_owner_producer.py
python code/c164_owner_checker.py
python code/c164_sympy_crosscheck.py
python code/c164_replay.py
python code/c164_mutation.py
```

Finite tables are sentinels; the operator and obstruction statements are
proved for all parameters in their stated domains.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B remains disabled.
