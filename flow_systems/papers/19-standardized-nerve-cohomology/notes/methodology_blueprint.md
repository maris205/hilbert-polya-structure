# Paper 19 methodology blueprint

Date: **2026-08-24**
Design: **pure theoretical cochain computation with bounded symbolic controls**

## Frozen inputs

- Paper 12's category of common-stabilizer standardized groupoids.
- `H=LZ`, `L>0`, a nonempty bare orbit set `Q`, and the same right `R` action.
- The exact continuous, unnormalized, trivial-real-coefficient nerve complex.
- Paper 12's degree-one computation and continuous functor
  `J:G_std -> G_actual` as prior results.

No alternative normalization or coefficient theory may be selected after the
calculation begins.

## Method

1. Write the degree-two cocycle and boundary equations on a single standard
   orbit in explicit coordinates.
2. Build a cochain comparison with the stabilizer model, proving continuity,
   chain-map identities, and inverse/homotopy identities directly.
3. Derive degree two before attempting a general-degree recursion.
4. Prove the arbitrary-`Q` assembly componentwise, checking whether products
   commute with kernels, images, and the chosen homotopy.
5. Compute `J*` on the exact representatives and test strict-automorphism
   naturality.
6. Compare the package with primary literature on continuous groupoid/group
   cohomology and Morita invariance under exactly matching hypotheses.

## Controls

- singleton `Q`;
- two-orbit and finite-`Q` component tests;
- rescaling `L` while retaining the same typed owner;
- direct verification of `d^2=0` and the first homotopy identities;
- a normalized-complex comparator used only to detect accidental convention
  drift, never as substituted proof;
- actual-owner comparison to prevent the standardized topology from being
  silently replaced by the indiscrete one.

## Failure modes

- a cited Morita theorem uses a different cochain category or topology;
- the proposed homotopy is not continuous;
- a product/image interchange fails for infinite `Q`;
- an origin choice is presented as canonical;
- degree-one prior work is repackaged as the new theorem;
- a routine textbook corollary is overstated as standalone novelty.

## Validation

- two independent derivations of degree two;
- line-by-line verification of the chain maps and homotopy equations;
- finite symbolic controls for signs and face maps;
- nearest-precedent matrix with exact theorem locators;
- independent devil's-advocate review before a proof lock.

## Expected output and effort

The Phase-2 source/routine audit is complete and the standalone composition
effort has stopped.  If separately authorized as a Paper-12 amendment, the
remaining bounded work is the exact author-complex comparison, cup
convention, higher `J*`, and limitations proof; until then the all-degree
formula remains a conditional theorem shape.
