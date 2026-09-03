# Exact evidence plan

## Claims under audit

The computational lane checks the finite algebraic shadows of matrix-tree
normalization, all transfer-current principal minors, root invariance, labelled
parallel-edge exclusion, local stack confluence, and Wilson/cycle-popping
agreement.  Almost-sure termination and the infinite-stack theorem remain
analytic claims proved in `THEOREM_PACKAGE.md` and `paper/main.tex`.

## Frozen grids

1. Enumerate every connected labelled simple graph on \(1\le n\le5\): 772
   graph rows and 8,136 graph-tree pairs.
2. For each graph, store the full spanning-tree bitmask ledger, reduced
   Laplacian determinant, rational transfer-current matrix, and exact numerator
   of every one of its edge-subset inclusion events.  This gives 55,895 event
   checks, not a single-edge sample.
3. Generate 24 deterministic positive-integer conductance multigraph cases;
   every case contains a distinctly labelled parallel edge.  Store all 846
   weighted trees and all 7,032 subset-event numerators.
4. At stack depth two, enumerate all 12,754 stack tables for every root of every
   connected labelled simple graph through four vertices.  Explore all legal
   pop choices and compare the unique terminal state with the canonical Wilson
   state whenever the finite table suffices.

## Independent lanes

- The producer uses rational Gaussian elimination and recursive state search.
- The checker imports no producer code, reconstructs every graph and case,
  solves linear systems column by column, enumerates all trees and all
  principal determinants, and uses a separate frontier exploration for stacks.
- SymPy proves a fully symbolic weighted triangle, a fully symbolic
  three-parallel-edge boundary, and every edge subset of a weighted \(K_4\).
- Replay regenerates the 1.8 MB evidence twice in an isolated directory and
  compares bytes.
- Mutation repairs outer payload hashes while attacking model, theorem,
  nested graph/case/stack rows, Route-A semantics, raw/semantic YAML bindings,
  duplicate/nonfinite JSON, YAML anchors/aliases/merges/non-string keys,
  implicit timestamps, unknown fields, and scalar types.

All scripts explicitly refuse optimized Python.  The release gate also checks
the exact 27-file payload ledger, deterministic fresh LuaLaTeX builds, revision
tokens, extracted text, page rasters, embedded/subset fonts, and the absence of
warnings and sidecars.
