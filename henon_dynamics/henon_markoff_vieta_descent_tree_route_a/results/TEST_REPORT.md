# C193 test report

## Exact executable checks

- Producer: PASS — 513 rows through depth ten, 512 retained frontier
  children, 1,539 Vieta-invariance tests, 15 bounded solutions, and 19
  complete descent traces containing 107 steps.
- Independent checker: PASS — 8,417 assertions; no producer import.
- Alternate-variable bounded oracle: PASS — exactly the same 15 normalized
  solutions with largest coordinate at most 2,000.
- SymPy reconstruction: PASS — 8,418 checks.
- Canonical replay: PASS — 402,099 bytes and exact SHA-256 match.
- Mutation suite: PASS — 156 repaired-hash plus one stale-hash rejection.

All four read-only release checks were rerun with bytecode generation disabled
after the evidence and PDF were frozen.

## Independence and coverage

The producer solves the Markoff quadratic for the largest coordinate at fixed
first and second coordinates.  The checker instead solves the quadratic in
the middle coordinate at fixed first and largest coordinates, uses an
independent loop order, reconstructs the quotient tree from the root, and
recomputes parents, children, local branch words, levels, heights, coordinate
sums, invariance, bounded closure, and every stored descent trace.

The separate SymPy path reconstructs polynomial invariance, involutivity,
Vieta root sum and product, the tied-maximum obstruction, the between-roots
sentinel, and both nonparent-edge ascent identities.  It then checks every
stored row, child, in-table reverse edge, bounded solution, and trace.  The
two ascent decompositions are substantive polynomial identities; they are not
tautological restatements of the inequalities under test.

The bounded scan does not prove global generation, termination, or tree
completeness.  Those claims use the exact descent argument and the
source-attributed Vieta-orbit theorem.  Depth-ten rows deliberately retain
their one-step depth-eleven children, so the evidence is not presented as a
closed finite tree.
