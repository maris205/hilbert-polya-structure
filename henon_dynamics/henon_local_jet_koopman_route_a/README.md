# C114 — finite local Koopman jet for a polynomial Hénon germ

This package freezes the polynomial germ

\[
F(u,v)=\bigl(u^2+\tfrac32u-\tfrac12v,\,u\bigr),\qquad F(0,0)=(0,0),
\]

and constructs its exact Koopman pullback on the finite local algebra
\(A_4=\mathbb Q[u,v]/(u,v)^5\).  The ordered monomial basis has dimension
15.  All entries of the pullback matrix, its five associated-graded blocks,
eight trace powers, characteristic polynomial, and \(\det(I-zK)\) are stored
as exact rational data.

The result is deliberately operator-first but finite and local.  It does not
identify a global function space, a global Koopman spectrum, a nuclear
operator, or a Fredholm determinant.  Its release scope is the literal
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

From this directory run:

```bash
python code/c114_jet_producer.py
python code/c114_jet_checker.py
python code/c114_sympy_crosscheck.py
python code/c114_replay.py
python code/c114_mutation.py
(cd paper && SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
python code/c114_release_manifest.py
```

The independent checker imports no producer code.  The mutation harness
requires every one of thirteen hostile edits to be rejected.

## Route-A status

- A1: `A1_PARTIAL_CERTIFIED`, qualified by one fixed germ and its order-four jet only;
- A2: `A2_CERTIFIED_PREFIX`, qualified by a 15-dimensional finite local quotient only;
- A3: `A3_NOT_ADDRESSED`;
- A4: `A4_FAIL`;
- overall: `ROUTE_A_EXPLORATORY`.

The compiled paper is [paper/main.pdf](paper/main.pdf), the canonical evidence
is [results/c114_jet_evidence.json](results/c114_jet_evidence.json), and the
content ledger is [C114_RELEASE_MANIFEST.json](C114_RELEASE_MANIFEST.json).
