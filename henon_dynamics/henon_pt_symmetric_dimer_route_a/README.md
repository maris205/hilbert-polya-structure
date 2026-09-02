# HCS-C297 — PT-symmetric dimer phase atlas

Frozen obstruction identifier: `HEN-O281`.

This package closes one autonomous balanced-gain/loss two-mode system rather
than extracting an installment from another paper.  For

```text
H_(gamma,kappa) = [[i gamma,kappa],[kappa,-i gamma]],  kappa>0,
i d_t psi = H psi,
```

it proves the exact propagator, the unbroken / exceptional / broken
classification, generic vector and projective periods, the exceptional-point
Jordan law, projective fixed rays, and the complete positive/indefinite metric
boundary.  The integer grid is a regression receipt only; the theorem is for
all real `gamma` and all `kappa>0`.

## Reproduce

From this directory run:

```bash
python -B code/c297_pt_dimer_producer.py
python -B code/c297_pt_dimer_checker.py
python -B code/c297_pt_dimer_sympy_crosscheck.py
python -B code/c297_pt_dimer_replay.py
python -B code/c297_pt_dimer_mutation.py
python -B code/c297_release_manifest.py
```

The release contains 168 exact parameter cells, eight boundary cells, 6,475
independent checker assertions, 516 symbolic checks, and 52 hostile
rejections.  The final paper is [paper/main.pdf](paper/main.pdf).

Scope is literally `NO_BAD_EULER_OR_ROOT_NUMBER`.  Nothing here supplies
arithmetic local data, an Euler factor, a root number, automorphy, a target
zero correspondence, a Hilbert--Pólya operator, or Route-B authorization.
