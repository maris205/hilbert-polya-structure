# Final Proposal: Four-Step Escape from Finite-Rank Tori for Monomial Hénon Maps

## Lifecycle

**SOURCE_DESIGN_DRAFT / PENDING_INDEPENDENT_REVIEW / NO_CODE / NO_RESULTS / NO_MANUSCRIPT**

## One-sentence thesis

For every monomial Hénon automorphism

\[
H(x,y)=(b x^d+a y+c,x)
\]

over a characteristic-zero field and every finite-rank multiplicative group,
four forward steps inside the corresponding torus admit a coefficient-uniform
explicit bound, whereas three steps can contain an infinite rank-one family.

## Exact setup

Let:

- \(K\) be any field of characteristic zero;
- \(d\ge2\);
- \(a,b,c\in K^\ast\);
- \(\Gamma\le K^\ast\) have finite rank \(r\).

No coefficient is required to lie in \(\Gamma\). Define

\[
T_m(H,\Gamma)
=
\{P\in\Gamma^2:H^j(P)\in\Gamma^2
  \text{ for all }0\le j\le m\}.
\]

## Main theorem

\[
\boxed{
\#T_4(H,\Gamma)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
}
\]

This is the headline theorem. It is stronger than the historical
periodic-point formulation because no periodicity assumption is used.

## Sharp threshold theorem

For every \(d\ge2\), choose

\[
b=1,\qquad a=-1,\qquad c^{d-1}=-1,
\qquad K=\mathbb Q(c),
\qquad \Gamma=\langle2,c,-1\rangle.
\]

Then \(\operatorname{rank}\Gamma=1\), and for every \(t=2^n\),

\[
P_t=(t,t^d)
\]

has

\[
P_t,\ H(P_t),\ H^2(P_t),\ H^3(P_t)\in\Gamma^2.
\]

Thus

\[
\#T_3(H,\Gamma)=\infty.
\]

The four-step window is therefore universally minimal.

## Weighted periodic corollary

Let \(C_n^\Gamma(H)\) count exact-period-\(n\) orbits
\(\mathcal O\subseteq\Gamma^2\). Then

\[
\boxed{
\sum_{n\ge1}n\,C_n^\Gamma(H)
\le
4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.
}
\]

The whole-orbit containment is part of the notation and may not be weakened
to one representative in \(\Gamma^2\).

## Proof architecture

### 1. Fixed-coefficient ESS

At each recurrence index,

\[
\frac1c x_{i+1}
-\frac bc x_i^d
-\frac ac x_{i-1}=1.
\]

The variables lie in \(\Gamma^3\), whose rank is \(3r\), while the displayed
scalars are arbitrary fixed nonzero coefficients. ESS yields at most

\[
\exp\!\bigl(18^9(3r+1)\bigr)
\]

nondegenerate triples. Each fixes \(x_i^d\), hence has at most \(d\) local
states. Four local indices give the first summand.

### 2. Degeneracy automaton

Use the locked labels

\[
\begin{aligned}
A_i&:a x_{i-1}+c=0,\\
B_i&:b x_i^d+c=0,\\
C_i&:b x_i^d+a x_{i-1}=0.
\end{aligned}
\]

The complete nine-transition table has only two free adjacent words:

\[
BA,\qquad CB.
\]

Every \(BA\) branch closes at the third letter. Every \(CB\) branch closes at
the third letter except

\[
CBA,\qquad a=-1,\qquad bc^{d-1}=-1,
\]

and this branch closes at the fourth letter. Therefore every word in
\(\{A,B,C\}^4\) has at most \(d^2\) initial states, giving \(81d^2\).

### 3. Overlap and boundary cases

Pairwise simultaneous degeneracies give permutations of
\((-1,1,1)\) among the normalized summands. Triple degeneracy is impossible
in characteristic zero. Choosing any valid label covers every point; overlap
only increases a union upper bound.

Periods \(1,2,3,4\) are included because the proof does not require distinct
states.

## Contribution hierarchy

1. **Primary:** coefficient-uniform \(T_4\) bound over arbitrary
   characteristic-zero fields and finite-rank groups.
2. **Co-primary:** rank-one infinite \(T_3\) construction proving window
   sharpness.
3. **Technical core:** full \(b\)-version degeneracy automaton with fixed
   \(A/B/C\) indexing.
4. **Corollary:** weighted bound for periodic orbits wholly contained in
   \(\Gamma^2\).

## Literature boundary

The ESS paper is the only imported theorem. One-dimensional \(S\)-unit
dynamics, univariate orbit dependence modulo finitely generated groups,
general hitting-time structure, Hénon common-zero results, integral-orbit
non-density, cyclotomic Hénon non-density, and 2026 higher-dimensional
semigroup dependence are adjacent but do not provide the combined theorem.

Bell--Chen--Hossain Theorem 1.1 treats a fixed orbit through one rational
observable, while Bell--Ghioca Theorem 1.1 treats return times of one fixed
orbit of a rational self-map of a semiabelian variety to a finitely generated
subgroup. Both are qualitative return-time structure results; neither bounds
all initial states surviving a prescribed four-transition Hénon window, and
neither yields a rank-only cardinality bound.

The closest current Hénon boundaries are:

- Ji--Xie--Zhang Theorem 1.8 and Corollary 1.9: cyclotomic-extension Hénon
  periodic points are not Zariski dense, which is not a finiteness theorem;
- Kim--Krieger--Postolache--Szeto Theorem A: for every odd \(d>2\), a
  rational polynomial \(s_d\) of degree at most \(d\) gives the
  general-polynomial Hénon map \((y,-x+s_d(y))\) at least \((d-4)^2\)
  rational periodic points; Theorem B, for \(d\equiv1\pmod6\), gives an
  integer cycle of length \((8d+10)/3\). This is lower-bound context outside
  the monomial-plus-constant family;
- Noytaptim--Zhong Theorem 1.2: non-density of a common-iterate locus for
  compositionally independent Hénon-type maps and a third morphism, with no
  multiplicative-subgroup window conclusion;
- Mello--Yasufuku Theorems 1.1--1.2 and Corollary 1.3: projective
  endomorphism semigroups over number fields and finitely generated groups,
  conditional on \(\mathrm{Hyp}_\epsilon\) for
  \(\epsilon\ge(1+c)/2\). Their Theorem 4.2, under additional divisor
  hypotheses and Vojta's Main Conjecture, supplies only sufficiently small
  \(\epsilon\), so it does not verify the general main hypothesis.

These results require explicit discussion to prevent false generalization.
The remaining novelty lies in all initial states, a fixed four-transition
window, an explicit rank-and-degree-only cardinality, finite-rank rather than
finitely generated groups, and the exact \(T_4/T_3\) threshold.

## Scores preserved

### Independent assessment A

- novelty: \(7.0/10\);
- standalone size: \(6.0\)--\(6.5/10\);
- proof confidence: \(9.5/10\);
- recommendation: GO after formal repair.

### Independent assessment B

- novelty: \(7.0/10\);
- standalone size: \(6.0\)--\(6.3/10\);
- proof confidence: \(9.7/10\);
- recommendation: GO with source-package corrections.

The scores are separate advisory records, not theorem evidence and not
cross-model certification.

## Optional extensions not promoted

A later source package may investigate a complete coefficient-stratified
\(T_2/T_3\) theorem. The present package proves only the explicit rank-one
\(T_3\) family and must not imply a classification.

No optimization of the ESS or degeneracy constants is proposed.

## Complete nonclaims

The proposal does not claim:

- bounds for all rational or integral periodic points;
- bounds for periodic points with only one torus-valued representative;
- coefficient membership in \(\Gamma\);
- positive-characteristic or \(d=1\) results;
- zero-coefficient cases;
- arbitrary-polynomial Hénon results;
- optimal constants;
- effective enumeration or height bounds;
- complete \(T_2/T_3\) strata;
- that every degeneracy word occurs;
- periodicity of the \(T_3\) example;
- computational confirmation;
- numerical, prime, modulus, or parameter scans;
- absolute priority;
- any result from the quartic candidate reserved for Paper 15.

## Paper 15 reserve

The quartic sharp-cutoff candidate is held for Paper 15. Paper 14 neither
depends on nor competes internally with an unreviewed quartic theorem. Any
future comparison must wait until both packages have independent reviews.

## Required next gate

A fresh independent reviewer must replay the fixed-coefficient ESS step,
derive the nine-transition table and both free chains, verify simultaneous
degeneracy and short orbits, check the sharp family, and reopen all primary
citations. Until then the lifecycle remains unchanged.
