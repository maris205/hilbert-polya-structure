# C113 — Third-order memory Hénon map

C113 tests a genuinely higher-dimensional Hénon subtype,

\[
 G(x,y,z)=(x^2-55/16-y-z/2,x,y).
\]

The map has two exact algebraic fixed points
(x=y=z=5/4\pm\sqrt5) and one exact primitive period-two cycle

\[
(-7/4,1/4,-7/4)\longleftrightarrow(1/4,-7/4,1/4).
\]

The Jacobian determinant is constantly (-1/2).  The period-two monodromy has
determinant (1/4), trace (-15/4), and characteristic polynomial
((4\lambda^3+15\lambda^2-2\lambda-1)/4).  Forward polynomial degrees begin
(2,4,8), so a finite low-degree polynomial space is not automatically an
operator owner.

The conservative verdict is `A1_WEAK`, `A2_CERTIFIED_PREFIX`,
`A3_NOT_ADDRESSED`, `A4_FAIL`.  This is an exact low-period witness, not a
complete three-dimensional orbit atlas or an analytic Fredholm theorem.

## Reproduce

```bash
python3 code/c113_memory_producer.py
python3 code/c113_memory_checker.py
python3 code/c113_sympy_crosscheck.py
python3 code/c113_replay.py
python3 code/c113_mutation.py
python3 code/c113_release_manifest.py
```

The paper is [paper/main.pdf](paper/main.pdf).
