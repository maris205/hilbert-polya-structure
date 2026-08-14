# Implementation Notes — SD-C25

The implementation uses two explicit layers:

- `code/sdc25_unary_fiber.py` contains the source graph, ordered word,
  fixed finite-state/fixed-dimensional fibers, exact rational matrices, and
  same-object block operator. Its constructor has no target predicate.
- `code/sdc25_evaluator.py` contains post-freeze prime and matched-support
  controls. Every such result records `candidate_used_target_predicate=False`.

Large computations remain sparse or exact:

- unary behavior is reduced to functional-orbit tail/period certificates;
- matrix responses use `fractions.Fraction` and Cayley–Hamilton;
- block determinants use Newton trace coefficients and an independent exact
  Gaussian determinant;
- trace-class prefixes use 60-digit `Decimal` directed rounding;
- the factorial ledger stores bit length and byte-level SHA rather than huge
  decimal expansions.

The primitive finite-block factor is always treated as
`det(I-w_k*B*A^(k-1))`. The trace-zero (2\times2) control prevents a first
trace coefficient from being misread as deletion of the complete local
factor or of repeated traversals.

The countable statements are limited to the imported Paper19 transient and
Paper20 recurrent architectures. No universal countable-system no-go is
encoded. The canonical runner disables bytecode and pytest caches, performs
two complete generator/test/analysis runs, compares every non-self-referential
code/result byte, and only then writes integrity and SHA artifacts.

