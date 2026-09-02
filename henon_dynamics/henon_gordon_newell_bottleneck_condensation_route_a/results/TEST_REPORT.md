# Test report — HCS-C285

All commands were run with `PYTHONDONTWRITEBYTECODE=1` from the package root.

## Deterministic producer

Command:

```bash
python -B code/c285_gordon_newell_producer.py
```

Result: `C285_PRODUCER_PASS`; 158,346 bytes; payload SHA-256
`1a301c0b96ff32590088ea1a46f62d52fb90dd3aeee447050e6315e5c5511bb0`.

## Producer-independent checker

Command:

```bash
python -B code/c285_gordon_newell_checker.py
```

Result: `C285 independent checker: PASS (11628 assertions)`. Before any
scientific comparison, the checker enforces every exact object key set and
JSON-decoded scalar/container type, rejects Boolean-as-integer substitutions,
and requires every rational to be a canonical reduced string. It then
independently solves each Fraction traffic system, builds every row-generator,
computes the full RREF nullspace of its transpose, proves nullity one,
normalizes and matches every state probability, reconstructs three routes to
`Z_N`, and checks all moments, flows, reversals, condensation rows, and
boundaries. It imports no producer code.

## Symbolic reconstruction

Command:

```bash
python -B code/c285_gordon_newell_sympy_crosscheck.py
```

Result: `C285_SYMPY_PASS (28 symbolic identities)`. Covered generating
coefficients, Newton recurrences, Euler/covariance identities, a symbolic
two-station global-balance system, a nonreversible reversal/involution case,
and uniform-composition counts.

## Two fresh-path byte replays

Command:

```bash
python -B code/c285_gordon_newell_replay.py
```

Result: `C285 double fresh-path byte replay: PASS`; both 158,346-byte receipts
equal the archived bytes and file SHA-256
`981db83511e8bcccd0f8296ca98ae7a7035a475cba0661b3361836488c062106`.
Each fresh path also passed the independent checker.

## Hostile mutations

Command:

```bash
python -B code/c285_gordon_newell_mutation.py
```

Result: `PASS 64/64`. The suite includes 60 repaired-hash
schema/semantic/type attacks, including the reproduced Route-B Boolean as
integer, scope-flag Boolean as integer, rational string as integer, and state
integer as Boolean escapes. It also probes canonical-rational syntax,
top-level and nested type confusion, row duplication and row-count-preserving
drop/replace, truncated or empty vectors and matrices, altered
routing/boundary/reversal/condensation semantics, an additional condensation
drop/replace, a stale hash, and raw top-level plus nested duplicate JSON keys.

## Route carrier and release

The unique YAML carrier rejects unknown, duplicate, merge and alias keys and
tuple/axis/overall/Route-B mismatches. The package freezes evaluator version
`0.2.0` and semantic token
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
release does not depend on mutable external registry bytes.

The final release command is:

```bash
python -B code/c285_release_manifest.py
```

It reruns every gate, performs six fresh PDF builds (two per revision), and
closes 27 payload files plus the self-excluded manifest as 28 physical files.
