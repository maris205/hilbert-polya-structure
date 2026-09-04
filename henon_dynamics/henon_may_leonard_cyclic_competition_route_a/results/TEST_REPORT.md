# Test report: HCS-C358

## Exact lanes

- Canonical producer: pass; payload
  `d3cddd47d856d592d385ff11f641e500e57714fcd01630a3453102dea26d864a`.
- Producer-independent checker: pass, 465 exact assertions.
- Independent SymPy derivation: pass, 19 exact identities.
- Isolated byte replay: pass, two independent temporary directories.
- Optimized-mode refusal: required for every executable under both `-O` and
  `-OO` and enforced again by the release gate.

## Serialization and claim gates

The checker rejects duplicate or non-string YAML keys, anchors, aliases,
merge keys, implicit timestamps, duplicate JSON keys, nonfinite JSON values,
unknown fields, stale section hashes, altered evaluator digests, altered
scope, and a changed Route-A decision.  The finite-evidence flag is false.

## Analytic boundary

The global trichotomy rests on the proof in `THEOREM_PACKAGE.md` and
`paper/main.tex`.  No finite row is treated as evidence for a universal
LaSalle, stable-manifold, periodic-leaf, or omega-limit assertion.
