# Experiment plan

## Claims under exact finite audit

1. Every transition uses the frozen denominator `2(n-1)` and starts from the one-edge tree.
2. Aggregated degree-vector dynamic programming agrees with an independent weighted parent-history enumeration.
3. Fixed-vertex rising moments through order eight agree with the gamma-product recurrence at every valid birth/time pair through `n=9`.
4. Every degree-count first and second moment is reconstructed exactly, while the conditional drift agrees state by state.
5. Vertex count and total-degree conservation hold exactly.
6. The displayed limiting masses satisfy their recurrence and truncated telescoping identities.

## Frozen grid

- Every time `n=2,...,9`.
- Every labeled vertex born by time `n`.
- Rising-factorial orders `r=1,...,8`.
- Every degree class `k=1,...,n-1`.
- A full independent enumeration of all `8! = 40,320` weighted parent histories at terminal time nine.

## Acceptance gates

The producer must replay byte for byte.  The checker does not import producer code and rebuilds the tree law from parent histories.  A separate SymPy lane checks the gamma recurrence, limit constants, Carleman growth, and degree-profile algebra.  JSON/YAML parsers reject duplicates, nonfinite constants, anchors, aliases, and semantic changes.  Repaired-hash mutations and `python -O` must fail.  Three substantively different manuscript rounds must each build twice identically under LuaLaTeX with no settled warning, overfull box, undefined reference, or missing glyph; every font must be embedded and subset.
