# C109 — Dissipative Hénon low-period transfer witness

This package freezes the genuinely dissipative polynomial Hénon map

\[
F(x,y)=\bigl(x^2-91/16-y,\;x/2\bigr),
\qquad \det DF=1/2.
\]

The fixed points \((13/4,13/8)\) and \((-7/4,-7/8)\), and the primitive
period-two orbit
\[
(5/4,-11/8)\longleftrightarrow(-11/4,5/8),
\]
are all rational and are checked by exact elimination.  Their Jacobian
denominators give a four-state weighted transition witness.  The resulting
finite determinant is an exact **discrete prefix**, not a Fredholm determinant
of the full map.

The honest Route-A verdict is `A1_PARTIAL_CERTIFIED` and
`A2_CERTIFIED_PREFIX`.  No global real coding, complete primitive-orbit atlas,
analytic operator owner, arithmetic/local data, Euler factors, root numbers,
automorphy, Hilbert–Pólya operator, or Route-B claim is made.

## Reproduce

```bash
cd henon_dynamics/henon_dissipative_route_a
python3 code/c109_dissipative_producer.py
python3 code/c109_dissipative_checker.py
python3 code/c109_sympy_crosscheck.py
python3 code/c109_replay.py
python3 code/c109_mutation.py
python3 code/c109_release_manifest.py
```

The manuscript is `paper/main.tex` and `paper/main.pdf`.  `C109_RELEASE_MANIFEST.json`
is the content-addressed ledger for all source, evidence, tests, and paper
artifacts.
