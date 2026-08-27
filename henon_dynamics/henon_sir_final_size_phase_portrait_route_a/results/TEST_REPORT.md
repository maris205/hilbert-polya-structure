# C198 test report

## Executable gates

- Producer: high-precision lower and upper Lambert branches generated.
- Independent checker: both intersections recovered by Lambert-free Decimal
  bisection and all exact physical scalings checked.
- SymPy: nondimensionalization, invariant, phase curve, peak, equilibrium
  spectrum, sensitivity and all numeric branch equations checked.
- Replay: canonical evidence reproduced byte for byte.
- Mutation: every repaired-hash semantic mutation and the stale-hash mutation
  was rejected.

Exact counts and hashes are refreshed before manifest closure and recorded in
`C198_RELEASE_MANIFEST.json`.

## Paper gates

Release additionally requires three content-distinct revisions, final/fresh
byte identity under a fixed epoch, embedded fonts, clean logs, extractable
scope text, and visual inspection of every page.

## Boundary check

The positive-infection grid does not cover `I0=0`; that branch is proved and
stated separately.  No finite regression is promoted to an all-parameter proof.
