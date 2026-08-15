# Paper 34 preregistration — SD-C36

**Status:** frozen before canonical authority result generation.

**Date:** 2026-08-15 UTC.

## Question

Test the finite exact consequences and sharp boundary of the positive
recognition-to-recurrence quadrilemma. The experiment audits shared recurrent
states, mutual SCC reachability, terminal pruning, finite-code clock
certificates, first-return marker ownership, and signed/matrix countercontrols.
It does not infer an infinite theorem from a cutoff.

## Frozen finite class

- loop-allowed directed graphs with no parallel edges on one through four
  vertices, exhaustively;
- 64 deterministic hash-seeded strongly connected graphs on five through
  eight vertices;
- strictly positive rational scalar edge weights in the primary census;
- primitive closed words modulo cyclic rotation, not reflection;
- exact integer, rational, formal-polynomial, CSV, JSON, and SHA-256 arithmetic;
- no target-zero data, coefficient fitting, network, stochastic sample,
  runtime timestamp, or external database.

## C1 — shared-state mixed-root gate

For every pair of distinct primitive simple cycles sharing a vertex, rotate
both to the same basepoint. The primitive root of their concatenation must be a
legal new closed word and must differ cyclically from both inputs.

**Gate:** zero true failures in the exhaustive census and frozen random
controls.

## C2 — mutual-connector gate and frozen repair policy

The initial proxy asks for lexicographically first shortest mutual connectors
whose interiors avoid both vertex-disjoint cycles. Any failures of this strict
normal form must be retained. They do not by themselves refute the source
theorem.

The repaired theorem-level evaluator asks only whether two vertex-disjoint
cycles lie in one SCC. It may choose arbitrary attachment vertices and mutual
directed paths. Concatenating the first cycle, a path, the second cycle, and a
return path must yield a closed word whose primitive root contains edge support
from both cycles and therefore differs from each.

**Gate:** report all strict-proxy failures; require zero repaired mixed-root
failures. Any repaired failure narrows or rejects the theorem.

## C3 — terminal pruning ownership gate

Attach only acyclic decision tails to a neutral recurrent inventory. Exact
power traces and determinants must remain equal to the unclassified recurrent
core. Deleting rejected recurrent blocks must instead yield a support-selected
product and be recorded as a label-dependent different operator.

**Gate:** terminal equality for every inventory; pruning differs for every
proper nonempty support; non-arithmetic inventories reproduce the architecture.

## C4 — finite-code clock gate

For alphabet sizes `q=2,3,4` and cutoffs `31,127,511,2047`, use canonical
q-ary gamma payloads with a return marker. Verify exact decoding,
prefix-freeness, Kraft sums, roof shares summing to one, and the powered
inequality `n^2<q^ell`.

**Gate:** all finite identities pass. These are witnesses for the proved
infinite argument, not a numerical proof of noncompactness.

## C5 — original-marker firewall

For every neutral cycle of length `ell>1` and orbit weight `w`, compare
`1-w z^ell` with the induced factor `1-w z`.

**Gate:** equality after `z=1`; formal inequality in the free marker whenever
`ell>1`; no induced factor described as the original graph-step determinant.

## C6 — sharp controls

- a one-way connector and a transient branch must not be classified as shared
  recurrence;
- two rotations of one primitive word must not be counted twice;
- signed scalar and matrix toys must demonstrate that literal positivity is
  essential;
- prime, square, Fibonacci, modular, hash-selected, matched hash, all, empty,
  and arbitrary supports must reproduce terminal/pruning and marker behavior.

## Source separation

The neutral source generator may not classify primes, squares, Fibonacci
numbers, modular supports, or hash-selected inventories. An independent
post-source evaluator owns labels and reconstructs all decisive graph and
formal certificates without importing the source implementation.

## Reproducibility

1. Execute source generation, evaluation, tests, and analysis in two fresh
   result directories.
2. Require byte identity for all declared artifacts.
3. Publish only after exact aggregate SHA agreement.
4. Reject caches, symlinks, CRLF, forbidden control bytes, timestamps,
   unexpected files, trailing whitespace, and extra EOF blank lines.
5. Freeze a sorted SHA-256 ledger without self-inclusion and validate a cold
   start plus post-seal provenance form.

## Decisions

```text
GO_RECOGNITION_TO_RECURRENCE_OBSTRUCTION_THEOREM
STOP_SHARED_POSITIVE_SCALAR_RECURRENT_COMPILER
STOP_TERMINAL_ORBITIFICATION_AS_ARITHMETIC_MECHANISM
STOP_PRIVATE_FINITE_CODE_LOG_CLOCK_FREDHOLM_CLAIM
STOP_FIRST_RETURN_AS_SAME_MARKER_DETERMINANT
BOUNDARY_SIGNED_MATRIX_OPEN
ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The canonical counts and hashes remain `PENDING_CANONICAL_EXECUTION` at this
freeze point.
