# P162 Hostile Review B owner and collision audit

**Status:** `PASS_OWNER_THIN / HOLD_EXTERNAL`  
**Audit date:** 2026-09-03  
**Scope:** bounded primary-source and P1--P165 mechanism audit; no novelty,
priority, or freedom-to-publish conclusion.

## Direct background owners

### Translation erosion and composition

Heijmans and Ronse, *The Algebraic Basis of Mathematical Morphology I:
Dilations and Erosions*, *Computer Vision, Graphics, and Image Processing* 50
(1990), 245--295,
<https://doi.org/10.1016/0734-189X(90)90148-O>, develops the complete-lattice
and abelian-group framework for translation-invariant dilations and erosions.
The official abstract explicitly places erosions in an abelian group of
automorphisms.  P162 therefore receives no contribution credit for recognizing

$$
\mathcal E_H(A)=\bigcap_{h\in H}(A+h)
$$

as an erosion or for the generic composition algebra.

Heijmans and Serra, *Convergence, Continuity, and Iteration in Mathematical
Morphology*, *Journal of Visual Communication and Image Representation* 3
(1992), 84--102,
<https://doi.org/10.1016/1047-3203(92)90032-O>, is a direct iteration source.
The manuscript cites and subtracts it accurately.

### Stochastic morphology

Sivakumar and Goutsias, *Binary Random Fields, Random Closed Sets, and
Morphological Sampling*, *IEEE Transactions on Image Processing* 5 (1996),
899--912, <https://doi.org/10.1109/83.503907>, is direct background for random
closed sets and morphological sampling.  The inspected abstract concerns
continuous and discretized binary random fields rather than P162's finite
translation-span inverse polynomial.  The general stochastic-morphology lane
nevertheless receives zero credit.

### Finite-field random rank

Balakin, *The Distribution of the Rank of Random Matrices over a Finite
Field*, *Theory of Probability and Its Applications* 13 (1968), 594--605,
<https://epubs.siam.org/doi/10.1137/1113076>, directly owns finite-field random
matrix rank distributions.  The Gaussian-binomial rank law, full-rank product,
and geometric rank-acquisition mean are treated as classical inputs, not as an
independent contribution.

## Focused direct-owner search

Searches combined the literal update and its less obvious terminology:

- `A intersect (A+v)` with random translations over finite vector spaces;
- iterated erosion by random two-point structuring elements;
- intersection of translates plus the generated history span;
- target translation stabilizer and erosion fibres;
- source-size polynomial, proper subsets of affine cosets, and ordered
  histories.

The bounded search returned the morphology and random-rank owner lanes above,
but no primary source stating the conjunction

```text
sharp witness V\{0}
+ arbitrary-target stabilizer filter
+ source-size/history polynomial
+ one-step stabilizer recovery.
```

This is a bounded non-hit only.

## Internal P1--P165 subtraction

| comparator | occupied mechanism | separation from P162 |
|---|---|---|
| P109 | deterministic image dynamics on a subspace lattice; Gaussian fibres and nilpotent clock | P162's state is an arbitrary subset, while randomness builds a translation span; the proper-subset coset fibre does not transfer. |
| P115 | a fixed finite-linear Cartier operator with uniform affine-kernel fibres | P162 has history-dependent spans and nonuniform target stabilizers. |
| P128 | deterministic polynomial-factor translation/GCD erosion | generic erosion is zero credit, but P128 has no random rank clock or target-stabilizer source/history polynomial. |
| P158 | random cut intersections encoded by complementary vertex-history words | both use random intersections, but P158's target structure is a bicluster graph and its fibres use component word assignments, not affine cosets or translation stabilizers. |
| P163 | deterministic complemented-shadow dynamics on set families | different carrier, recurrent rank-support mechanism, and fibre proof. |
| P164 | q-ary cyclic equality feedback with a Rule-102 tail | different literal map and affine-code target spectra. |
| P165 | low-weight support shortening on subspaces | deterministic shortening and extremal preimage bounds, not stochastic subset erosion or complete fibres. |

The active same-batch kill ledgers also treat direct sliding-AND erosion,
random-rank shadows, and generic random intersections as occupied or killed.
P162's paper-level residual must therefore remain exactly the target-resolved
conjunction above; it may not promote the erosion or rank marginal to novelty.

## Citation QA

- All four BibTeX keys resolve in both cold builds.
- Author names, titles, journals, volumes, issues, pages, years, and DOI fields
  agree with the inspected publisher or authoritative index records.
- BibTeX reports zero warnings.
- The source-subtraction prose is appropriately qualified: it states that the
  source search was bounded and disclaims novelty, priority, and
  freedom-to-publish.

## Verdict

**PASS_OWNER_THIN.**  No direct owner or P1--P165 proof transfer was found for
the residual conjunction.  Mathematical morphology, stochastic morphology,
finite-field ranks, Gaussian coefficients, and generic stabilizer facts remain
zero-credit background.  Maintain `HOLD_EXTERNAL`.
