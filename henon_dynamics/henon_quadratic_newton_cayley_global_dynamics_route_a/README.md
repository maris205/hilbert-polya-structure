# HCS-C257 — quadratic Newton--Cayley global dynamics

C257 freezes Newton iteration for $p_a(z)=z^2-a^2$, $a\ne0$, on the
Riemann sphere.  The Cayley coordinate $w=(z-a)/(z+a)$ converts the full
map to $w\mapsto w^2$.  One theorem therefore closes both root basins, the
Julia line, exact double-exponential root errors, every periodic and
preperiodic point (including the $2$-adic tail), all cycle multipliers, the
Artin--Mazur zeta, and the invariant Cauchy law on the basin boundary.

## Reproduce

```bash
python3 -B code/c257_newton_producer.py
python3 -B code/c257_newton_checker.py
python3 -B code/c257_newton_sympy_crosscheck.py
python3 -B code/c257_newton_replay.py
python3 -B code/c257_newton_mutation.py
python3 -B code/c257_release_manifest.py
```

The final paper is `paper/main.pdf`; the three revision snapshots are
retained.  The release manifest is self-excluded and hashes exactly 27
payload files.

## Strict boundary

The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  The evaluator tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, the overall verdict is
`ROUTE_A_REJECTED`, and Route B is false.  This exact degree-two dynamical
zeta is not an arithmetic Euler product.  No arithmetic local data, target
divisor, functional equation, target determinant, automorphy, root number,
or Hilbert--Pólya operator is claimed.
