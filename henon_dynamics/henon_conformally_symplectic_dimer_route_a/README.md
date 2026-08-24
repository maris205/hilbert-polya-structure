# C118 — Conformally symplectic damped Hénon dimer

C118 freezes the two-site variational map

\[
F(q,p)=(\nabla U(q)-\gamma p,q),\qquad
\gamma=1/2,quad \kappa=1/4,quad a=13/2,
\]

with

\[
U(q)=\sum_{i=1}^2\left(\frac{13}{4}q_i^2-\frac13q_i^3\right)
-\frac18(q_1-q_2)^2.
\]

Its Jacobian satisfies `J^T Omega J = gamma Omega` and has determinant
`gamma^2=1/4`.  The package verifies two synchronous fixed points and the
primitive synchronous period-two orbit

```text
((2,2),(6,6)) <-> ((6,6),(2,2)).
```

The two-step monodromy splits into longitudinal and transverse modes, with
traces `-59/4` and `-13`.  This is exact low-period tangent evidence, not a
transfer/Fredholm owner or complete orbit atlas.  No arithmetic, Euler-factor,
root-number, automorphy, Hilbert–Pólya, or Route-B claim is made; the literal
firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python3 code/c118_damped_dimer_producer.py
python3 code/c118_damped_dimer_checker.py
python3 code/c118_sympy_crosscheck.py
python3 code/c118_replay.py
python3 code/c118_mutation.py
python3 code/c118_release_manifest.py
```

The paper is [paper/main.pdf](paper/main.pdf).
