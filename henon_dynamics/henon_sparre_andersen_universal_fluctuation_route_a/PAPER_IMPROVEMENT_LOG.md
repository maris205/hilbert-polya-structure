# Paper improvement log

## Round 0 — core theorem

The first build states the frozen continuous symmetric model, derives the
unique-maximum convolution, and obtains the square-root survival law and first
strict descent.  It deliberately stops before asserting the second arcsine
statistic.

## Round 1 — occupation statistic and scaling

The second build adds the permutation-cycle identity for the number of positive
partial sums, extracts its bivariate coefficients, and proves the common
`Beta(1/2,1/2)` scaling limit with an explicit endpoint bound.  This is a
substantive theorem extension, not a prose-only revision.

## Round 2 — convention failure and release audit

The final build adds the minimal atomic counterexample, explains exactly why
strict/nonnegative and maximum-time conventions diverge, and integrates the
independent checker, SymPy, byte replay, hostile mutation, scope, and Route-A
receipts.  All three round PDFs have distinct hashes; `main.pdf` is byte-equal
to `main_round2.pdf`.
