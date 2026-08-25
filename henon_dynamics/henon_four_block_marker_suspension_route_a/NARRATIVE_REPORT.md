# C139 narrative report

## Outcome

C139 makes a narrow but explicit Route-A advance over edge clocks.  A single
four-block marker `0011`, weighted by `sqrt(5)`, distinguishes two primitive
period-six words that remain identical under every one-, two-, and three-block
population.  The associated higher-block matrix retains an exact finite
determinant and an all-period primitive product.

## What is genuinely new

The progress is not merely another longer word enumeration.  The theorem
quantifies a minimal forward-memory step under the frozen coding: any memory-
at-most-three roof has periodic sums determined by the common block-count
vectors and therefore cannot separate the witness.  The four-block term does.
The five radical coefficients are rationally independent, so clock equality
is equivalent to equality of the frozen feature vector.

## What fails next

The feature vector still aggregates distinct primitive necklaces.  The
period-seven pair `0101111`, `0110111` has the same edge and marker counts.
Thus C139 improves resolution without promoting it to orbit injectivity.
Minimal memory is also coding-relative, not a cohomology invariant.

## Evidence and boundary

The replay contains 8,190 rooted words, 747 primitive cycles, 258 rooted
feature cells, and 229 primitive feature cells through period twelve.  These
numbers test the implementation; the infinite determinant/product claims are
proved separately.  The candidate remains source-side and exploratory:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.  No target, arithmetic/local, natural-
operator, Hilbert--Polya, or Route-B claim is made.
