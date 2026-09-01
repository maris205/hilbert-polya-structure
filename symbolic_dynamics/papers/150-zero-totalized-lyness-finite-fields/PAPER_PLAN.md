# P150 paper plan

**Working title:** The All-Affine Functional Graph of the Zero-Totalized
Lyness Map over Odd Finite Fields  
**Type:** anonymous rigorous mathematical short note  
**Status:** `ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL`  
**Target length:** 4--6 A4 pages including references and declarations  
**Absolute ceiling:** P150 in
`docs/papers147_151_sequence/phase1/FINAL_THEOREM_CONTRACTS.md`  
**One-sentence contribution:** After assigning inverse zero the value zero,
the Lyness five-cycle has an exactly classifiable functional graph on the
whole affine plane over every odd finite field: one generic period-five
locus, recurrent coordinate axes, three explicit tail layers, and a complete
`0/1/q` inverse atlas.

## Claims--evidence matrix

| Claim | Formal proof object | Paper-local control | Credit boundary |
|---|---|---|---|
| The affine plane is the disjoint union of the generic locus, the coordinate axes, and three displayed exceptional layers. | Pointwise case split in the stratification theorem, followed by a cardinality check. | Exact membership, pairwise disjointness, coverage, and layer sizes in every field box. | Set partition bookkeeping is not itself a contribution; the literal all-affine boundary completion is the residual object. |
| The recurrent set has size `q^2-3q+5`; the temporal polynomial is `(q^2-3q+5)+(q-1)z+(q-2)z^2+(q-2)z^3`, with sharp depth three. | Five rational iterates on the generic locus, explicit axis arrows, and the three exceptional arrow identities. | Every state receives its predicted tail and period; full depth histograms are compared. | Classical Lyness period five on its birational domain receives zero credit. |
| There are `1+r_q` fixed points, two 2-cycles, `(q-3)/2` 4-cycles, and `((q-2)(q-3)-r_q)/5` 5-cycles, yielding the stated zeta product. | Fixed-point equation, inversion-pair classification on the axes, and prime period five on the generic locus. | Exact cycle extraction and point-period counts in all boxes. | Generic finite-map cycle and zeta identities receive zero credit. |
| Every target has fibre size `q`, `0`, or `1` according to the displayed rule; the image has size `q^2-q+1`. | Solve the single inverse equation after the first target coordinate fixes the source's second coordinate. | Literal fibre counters over every target, including the unique maximum fibre. | Generic rational inverse methods receive zero credit. |
| The exceptional component is exactly one leaf and `q-2` length-three chains attached to the two-cycle `(-1,0)<->(0,-1)`. | Combine the layer arrows with the every-target fibre theorem to exclude further predecessors. | Exact predecessor sets, leaves, and chain arrows. | No claim is made about other totalizations or projective compactifications. |

## Paper architecture

1. **Scope and complete statement.** Define `inv0`, the literal map, entry
   time, `r_q`, all five strata, and the complete theorem. State the ownership
   subtraction before the proof.
2. **All-plane stratification and tails.** Prove disjoint coverage point by
   point, establish the five rational iterates on the generic locus, classify
   the axes, and prove every exceptional arrow and the temporal polynomial.
3. **Cycle census and zeta.** Solve the fixed equation, classify inversion
   pairs, show all remaining generic points have exact period five, and derive
   the zeta factorization.
4. **Every-target fibres and the singular component.** Solve every inverse
   equation, count the image, and prove that the displayed exceptional
   in-tree is complete.
5. **Exact controls, limitations, and declarations.** Report deterministic
   finite-field falsification, distinguish it from proof and ownership, and
   include the required anonymous declarations.

## Figure decision

No figure is needed. The five disjoint strata and all arrows fit in four
displayed formulas; a graph drawing would obscure the target-resolved fibre
law and would require field-dependent duplication. A compact control table is
used only for reproducibility bookkeeping.

## Citation plan

Five verified primary or author-hosted sources are cited:

- Lyness (1942) for the original cycle observation;
- Hone--Kouloukas for the type-`A_2` cluster interpretation and classical
  Lyness five-cycle;
- Hone for the rational Lyness/QRT map, projective denominator treatment, and
  arithmetic use;
- Jogia--Roberts--Vivaldi for integrable birational maps over finite fields;
- Kanki for the distinct extended-space/almost-good-reduction treatment of
  finite-field division by zero.

All cited material is explicitly zero-credit background. No citation is used
as evidence of novelty or priority.

## Review and closure checkpoint

The outline was checked against the frozen contract rather than a venue
template. Before drafting, coverage was separated from its cardinality
consequence, polynomial fixed points were placed in the generic locus, the
fibre theorem was used to certify the entire exceptional in-tree, and the
bounded owner-search limitation was stated. Hostile Review A then independently
rederived the theorem and requested only two minor hardenings: expose the
five-orbit integrality argument plus the `q=3`/characteristic-five boundaries,
and make the owner-search ledger replayable while adding Lyness (1942) and
Kanki (2013). Both are implemented in round 1 without changing the contract.

Hostile Review B returned **0 Critical / 0 Major / 1 Minor, REVISE** after
closing both Review-A items and independently accepting every theorem,
source, verifier, build, and visual interface. Its sole finding was stale
round-zero provenance in `FINAL_QA.md`. The current Markdown closure repairs
that Minor and leaves **0 unresolved Critical / 0 unresolved Major / 0
unresolved Minor**. The internal round-2 gate is therefore accepted under the
same narrow claim ceiling and `HOLD_EXTERNAL` boundary.

## Closure conditions

- Every P150 contract item has a symbolic proof in `main.tex`.
- The generic five-cycle identity is cited and reproved only as a direct
  algebraic input; it receives zero contribution credit.
- The full affine complement, not just sample fields, is partitioned.
- The verifier transcript replays byte for byte with exact arithmetic.
- The four-stage LaTeX/BibTeX build has no undefined citation or reference.
- `main_round0_original.pdf` preserves the first settled author build.
- Both hostile reviews are preserved; all requested repairs are closed and no
  Critical, Major, or Minor item remains unresolved.
- Current `main.pdf` is the accepted 5-page, 403,358-byte artifact at SHA-256
  `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca`;
  5/5 references resolve, 2,144,131 assertions pass, two isolated builds are
  byte-identical, and all 5/5 pages are visually accepted.
- Root separately froze `main_round2.pdf` during this closure; a read-only
  comparison confirms that it is byte-identical to current `main.pdf` at the
  accepted 403,358-byte size and SHA-256.
- No novelty, priority, authorship, posting, contact, submission, or release
  claim is made; status remains `HOLD_EXTERNAL`.
