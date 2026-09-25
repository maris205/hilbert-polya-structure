# Evidence — ASFS-20260915-CWT01

**Status:** STOP — AREA KOOPMAN NONCOMPACT; LOCAL INDEX ZERO; GAUSSIAN DIAGONAL DIVERGENT.

## Inputs and method

The [version-1 card](../candidate-card.md) was frozen by the integrating
agent before this analytic audit. The exact map, full area measure, unit
roof, operator and local alternatives are reproduced in the
[paper](../paper.md). All arithmetic is the displayed all-integer
divisibility formula, not an imported prime list.

No numerical run or finite-period scan was performed. Reproduction means
checking the explicit inverse and cycle sum, the L2 change of variables
and orthonormal sequence, the fixed-period compact-boundary degree
homotopy, and the two-variable Gaussian substitution in Propositions 1--5.
No cutoff is used for the global orbit statement; the compact cutoff
in the local integral is part of its exact test-function definition.

## Controls and limits

The Gaussian has covariance epsilon^2 I and normalization
(2 pi epsilon^2)^(-1). Its local cutoff is fixed independently of
epsilon, nonnegative, smooth, compactly supported and equal to one near
(1,1). Those choices determine the proved epsilon^(-1/2) rate.
No finite-part subtraction or other regularization is assessed.

The degree proof uses a separate sufficiently small positive auxiliary
parameter for each fixed return period. It requires no parameter uniform
in the period and does not alter the frozen candidate.

The proposed full-area determinant is stopped at the operator-ideal
check; formal Route coordinates remain UNASSIGNED and Route B NOT INVOKED.

## Review and verification

The [bounded model review](review.md) manually rechecked the full paper,
including the operator, index, Gaussian and counting arguments, and found
no mathematical correction necessary. It used a separate task context
in the same model family, with the proposed arguments supplied in advance;
it was not blind, human peer review, cross-model verification, numerical
cross-checking or formal proof certification.

Verification used a Node filesystem walk of this package's Markdown,
resolved local Markdown link targets, checked the candidate ID in each
file, and checked trailing whitespace. Before the review was added,
5 files and 18 local links passed. After linking the completed review,
the final check passed on 6 Markdown files and 24 local links, with zero
missing targets, missing candidate IDs or trailing-whitespace errors.
Git diff --check was also
run for the exact package path; the filesystem check additionally covers
the package's untracked Markdown.

Navigation: [summary](../README.md), [paper](../paper.md),
[claim ledger](../claim-ledger.md).
