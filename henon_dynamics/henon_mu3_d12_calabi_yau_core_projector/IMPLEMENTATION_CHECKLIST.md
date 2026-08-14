# HCS-C52 implementation checklist

Status: **PASS; every C52 release item closed**

## B0 source lock

- [x] Verify frozen C47--C51 certificate and payload hashes.
- [x] Reconstruct \(K=\mathbf Q(\rho)\) and
      \(\rho^2+\rho+1=0\).
- [x] Reconstruct the exact cubic, quadric, and chronological closing edge.
- [x] Verify dimension, degree, characteristic-zero smoothness scope, and
      C51 Tate normalization.
- [x] Recompute the inherited middle Hodge dimensions \(1,83,83,1\).
- [x] Fail closed on every inherited-source mismatch.

## B1 group theorem

- [x] Enumerate projective monomial maps without duplicate scalar lifts.
- [x] Prove completeness of the enumeration.
- [x] Build multiplication, inverse, and order tables.
- [x] Exhibit generators and verify the order-24 dihedral presentation.
- [x] Verify the element-order histogram.
- [x] Verify preservation of both equations, including the closing edge.
- [x] State explicitly that the theorem does not classify full
      \(\operatorname{Aut}(X)\).

## B1 Chow projectors

- [x] Recompute \(\int_Xh^5=6\).
- [x] Prove the six ambient Lefschetz projectors are orthogonal idempotents.
- [x] Construct the algebraic middle projector \(\pi_5\).
- [x] Prove every graph fixes \(h\) and commutes with \(\pi_5\).
- [x] Prove \(e_G\), \(\pi_{\mathrm{core}}\), and
      \(\pi_{\mathrm{lev}}\) are self-transpose Chow idempotents.
- [x] Add a negative control rejecting a rank assignment to \(e_G\) before
      applying \(\pi_5\).

## B2 Cayley-ring representation

- [x] Fix the exact bigrading and term order.
- [x] Compute \(R_{1,-3}\) and \(R_{2,-3}\) over
      \(\mathbf Q(\rho)\).
- [x] Verify dimensions \(1\) and \(83\) by an independent relation-matrix
      checker.
- [x] Include the residue-orientation multiplier
      \(\det(M_g)/\det(A_g)\).
- [x] Verify invariance under changing a scalar lift in
      \(\mathrm{PGL}_8\).
- [x] Reconstruct all class traces and character inner products.
- [x] Verify one-dimensional multiplicities \((4,1,3,3)\).
- [x] Verify two-dimensional multiplicities \((7,8,6,8,7)\).
- [x] Verify that \(H^{4,1}\) is trivial under the group action.

## B2 theorem decision

- [x] Prove the core Hodge ledger \((1,4,4,1)\) and rank \(10\).
- [x] Prove the complementary ledger \((0,79,79,0)\) and rank \(158\).
- [x] Prove the augmentation lemma for every element of
      \(\mathbf Q[G]\), not only central elements.
- [x] Prove that no graph-algebra idempotent yields the \(2+166\) split.
- [x] State that correspondences outside the graph algebra remain open.
- [x] Use “Calabi--Yau-type Hodge structure,” not “Calabi--Yau threefold.”

## Reproducibility and hostile checks

- [x] Keep producer and checker algorithms independent.
- [x] Use exact arithmetic only; no floating-point theorem fields.
- [x] Reject missing and unknown schema keys.
- [x] Reject `bool` values smuggled into integer fields.
- [x] Mutation-test the closing edge, one phase, group size, relation rank,
      residue twist, trivial multiplicity, middle projector, and claimed
      coefficient category.
- [x] Require each semantic mutation to produce the intended FAIL gate,
      not ERROR.
- [x] Generate release hashes and a manifest only after docs, code, results,
      paper, and Route records are frozen by their respective lanes.

## Source and novelty audit

- [x] Add exact primary locators for finite-group graph projectors.
- [x] Add exact primary locators for the complete-intersection
      Cayley/Jacobian-ring Hodge representation.
- [x] Audit prior Calabi--Yau-type \((2,3)\) fivefold results.
- [x] Audit explicit group-action/motive decompositions near this example.
- [x] Separate curve/Jacobian decomposition prior art from the fivefold
      statement.
- [x] Make no absolute novelty claim; record the targeted,
      non-exhaustive search boundary in SOURCE_AUDIT.md.

## C52/C53 boundary

- [x] Keep B3 projected Frobenius polynomials out of the C52 schema and
      manuscript.
- [x] Keep B4 incidence correspondences and every rank-two projector claim
      out of C52.
- [x] Hand the rank-10 Chow summand to C53 only after B0--B2 pass.
- [x] Do not turn a finite-prime ledger into the C52 headline.

## Release-integration safeguards

- [x] Code and results were promoted only after the theorem scope stabilized.
- [x] The paper and Route-A records preserve the B0--B2 claim boundary.
- [x] Top-level candidate and obstruction registries use unique C52 entries.
- [x] The user-owned `codex_prompt.md` was not touched or staged.
