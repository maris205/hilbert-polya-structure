# Code contract

No formal C22 implementation exists at Stage 1.  This directory is reserved
for the post-confirmation producer/checker package.

The first implementation milestone must contain:

- an exact-rational common-cover and contraction producer;
- a nonimporting independent checker for every rational margin;
- joint parameter--state necklace enumeration with cyclic and reversal
  metadata;
- interval Newton/Krawczyk orbit and monodromy certification;
- complete state-orbit aggregation above each tested parameter necklace;
- exact finite-field controls;
- tests that deliberately reverse chronological multiplication and separately
  canonicalize the two necklaces, both of which must be detected as errors.

No code may call a frequency-averaged Hénon map or transition matrix.  A
finite operator section may be used for diagnostics only after its exact
relationship to the frozen determinant is stated.
