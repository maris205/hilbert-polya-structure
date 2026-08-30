# P125 — Quadratic-state shear over F2

Status: **ANONYMOUS ROUND-TWO FINAL INTERNAL FREEZE / GO_INTERNAL /
EXTERNAL HOLD**.

Let `(V,Q)` be a nonsingular `2m`-dimensional quadratic space over `F_2` and
iterate

```text
Phi(x,y) = (y, x + Q(x)y)
```

on `V x V`.  The paper determines the complete functional graph for both
Witt signs:

1. the polar bit is invariant, every depth is at most two, and the only
   periods are `1,2,3,4`, with all pointwise shortenings classified;
2. every target has an explicit `0/1/2`-element fibre, and the second image
   is exactly the recurrent set;
3. all three depth layers have closed Witt-sensitive counts;
4. every component has one of six decorated cycle shapes, giving all cycle
   counts and the finite-map zeta function.

The map is not a transvection action and fails both the braid and quantum
Yang--Baxter relations by explicit hyperbolic-plane witnesses.  Static
quadratic counts, transvection theory, Yang--Baxter pair-map theory, and zeta
bookkeeping receive zero contribution credit.  P99, P103, P106, P109, and
P118 are explicitly subtracted as internal package or vocabulary neighbors.

Run the deterministic standard-library audit with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

The canonical result is **27,405,887 exact assertions, PASS**.  Unlike the
earlier proof spike, this paper-local verifier checks literal set equality
`im(Phi^2)=Rec(Phi)` and traverses every connected component through
dimension ten, comparing its rooted-cycle decoration with the six formulas.
Directed cycle decorations are quotiented only by cyclic rotation; an
asymmetric sentinel asserts that reflection is not identified.

The owner search is bounded.  Public posting, submission, novelty, priority,
and external release remain **HOLD**.
