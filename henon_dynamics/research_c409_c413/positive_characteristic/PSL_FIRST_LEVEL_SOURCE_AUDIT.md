# First-level ownership: Serre's exact projective cover

2026-09-06. Primary-source normalization check, restricted to the first
level. The independent all-iterate collision audit is owned by the
nonlinear-geometry lane. This file makes no admission decision.

## Verified owner and actual read scope

S. S. Abhyankar, *Galois theory on the line in nonzero characteristic*,
Bulletin of the American Mathematical Society (N.S.) **27** (1) (1992),
68–133, DOI [10.1090/S0273-0979-1992-00270-7](https://doi.org/10.1090/S0273-0979-1992-00270-7),
with an **Appendix by J.-P. Serre**, a letter dated 15 November 1990.

The [author-deposited arXiv PDF](https://arxiv.org/pdf/math/9207210)
was accessible. I read the complete appendix: PDF pages 64–66, corresponding
to journal pages 131–133. The publisher PDF timed out. I did not read or
claim to have read the entire 66-page article for this check. The opening
bibliographic page and the historical discussion in §11 were also inspected.

The appendix proves the exact first-level equation

$$Y^{q+1}-XY+1=0$$

has geometric monodromy $\operatorname{PSL}_2(\mathbb F_q)$, with $q$ a
power of the characteristic. It constructs the cover using Dickson
invariants for $\operatorname{PGL}_2$, removes the tame branch by a cyclic
base change, and explicitly recovers the displayed degree-$q+1$ equation.
Serre starts with algebraically closed constants. The construction is
first-level, not a theorem about repeated rational composition.

## Exact normalization in the scout proof

The equation in the source is literally the first inverse equation of

$$f(X)=X^p+X^{-1},$$

after renaming its source and target variables and setting $q=p$. No
parameter specialization, analogy, or heuristic identification is needed.

The model reconstructed in [WILD_PSL_RATIONAL_PROOF.md](WILD_PSL_RATIONAL_PROOF.md)
is

$$w^p-w=v^{-(p+1)/2},\qquad
t=v^{p(p-1)/2}+v^{-(p-1)/2}.$$

It is an explicit Artin–Schreier presentation of this classical splitting
cover. Its first group, projective permutation action, one-point branching,
and first-level genus are **not claimed as new**. The matrix transformations
and root-recovery formulas in the scout proof make the normalization
self-contained and justify its stated arbitrary-constant-field scope.
That reconstruction is still not counted as an independent contribution.

## What this check does and does not resolve

The first-level ownership collision is resolved affirmatively: classical.
The proposed increment is the actual all-height tower for this *fixed*
rational map, including global independence and full local ramification.
Whether an existing general composition theorem already owns that
increment is a separate question; see the independently prepared
[all-level source audit](../nonlinear_geometry/PSL2_TOWER_SOURCE_AUDIT.md)
when available. Absence of an iterate theorem in the three-page appendix
does not establish novelty of the tower.

The source check suggested two particularly relevant classical leads to
that independent audit: Abhyankar's *Wreath products and enlargements of
groups* (1993) and *Linear disjointness of polynomials* (1992). Their full
texts were not read in this first-level check. Their titles alone are not
evidence either for or against ownership of the proposed theorem.
