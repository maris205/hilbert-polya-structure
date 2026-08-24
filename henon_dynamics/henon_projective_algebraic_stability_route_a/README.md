# C121 — projective algebraic stability of a quadratic Hénon map

This package freezes

\[
H(x,y)=(x^2-4-y,x),\qquad H^{-1}(x,y)=(y,y^2-4-x),
\]

and studies its exact extension to the projective plane.  The forward and
inverse indeterminacy points are separated, the unique exceptional line maps
to a forward-fixed point, and a direct nonexpanded recurrence proves
\(\deg H^n=2^n\) for every \(n\geq1\).  The associated algebraic dynamical
degree is exactly two.  This last quantity is used only as an algebraic
degree-growth invariant; no entropy equality is claimed.

The orbit layer certifies the two fixed points
\((1\pm\sqrt5,1\pm\sqrt5)\) and the primitive real two-cycle
\((0,-2)\leftrightarrow(-2,0)\), including its exact tangent monodromy.
Controls at parameters \(c=-3\) and \(c=-5\) fail the frozen cycle equations.

## Reproduce

From this directory run:

```bash
python code/c121_projective_producer.py
python code/c121_projective_checker.py
python code/c121_sympy_crosscheck.py
python code/c121_replay.py
python code/c121_mutation.py
(cd paper && SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
python code/c121_release_manifest.py
```

The checker imports no producer code.  The evidence represents iterates by an
exact recurrence DAG, sparse leading data, and exact probes, so replay through
degree 256 does not require a huge expanded polynomial.

## Route-A status

- A1: `A1_WEAK`.  The all-order degree law, two fixed points, and one
  primitive two-cycle are exact structural evidence, but there is no complete
  orbit atlas or prime-like target correspondence;
- A2: `A2_FAIL`, because there is no weighted dynamical zeta, transfer owner,
  target divisor, or zero-matching test;
- A3: `A3_FAIL`, because no functional equation, Gamma factor, counting law,
  controlled continuation, or analytic bridge is constructed;
- A4: `A4_FAIL`;
- overall: `ROUTE_A_EXPLORATORY`.

The canonical route tuple, using exactly the labels in
`henon_dynamics/skills/route-a-evaluator.md`, is

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

The compiled paper is [paper/main.pdf](paper/main.pdf), the canonical evidence
is [results/c121_projective_evidence.json](results/c121_projective_evidence.json),
and the content ledger is [C121_RELEASE_MANIFEST.json](C121_RELEASE_MANIFEST.json).
The literal release scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
