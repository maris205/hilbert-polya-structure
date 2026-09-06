# Independent arithmetic proof and substance decision

Date: 2026-09-07. Reviewer: the coordinating agent, not the author of this
lane. This is substantive internal model review, not human peer review or
external publication approval. The full author proof, scout report and source
audit were read; the proof was checked at its quantified all-SL2 scope.

**Decision: no blocking mathematical defect found; retain as an unadmitted
companion result.** The five-paper substance/source gate is not satisfied by
this proof alone. No C-number, formal evaluation or manuscript is authorized
by this review.

## Mathematical checks

1. The Smith reconstruction includes infinite valuations for null factors.
   Eventual differences distinguish ranks 0, 1 and 2. The case split for the
   signed trace handles both scalars and both parabolic signs; using only
   determinant magnitudes without that split would have been insufficient.
2. Cayley--Hamilton gives `A^2-I=A(2A-tI)` with the stated sign. Entry content
   is unchanged by the left unimodular factor, so row two really recovers h.
   Odd t makes h=g. At even t, primitive centered content leaves only g=r or
   2r, and the second possibility forces D=1 modulo 4.
3. In the exceptional case, `v2(T-epsilon)=2s-1` and s>=2 follow from the
   two consecutive even neighbors of odd T. The coefficient of `2^s` is
   invertible modulo 2 in both classes. No elliptic or parabolic case falls
   into this residual branch. Primitive trace-zero reduction at an odd prime
   is nonscalar, including when D is divisible by that prime; the cyclic
   basis argument does not require distinct eigenvalues.
4. The dyadic lemma's odd-power and squaring arguments give pointwise, not
   merely matrix-order, displacement valuations. In the minus case, the
   exceptional depth m=1 really has period one. Parent-child incidence is
   `2^d L/L'`, and the explicit cycle matching respects reduction because
   chosen child representatives project to already matched parent bases.
   This supplies one inverse-limit conjugacy rather than unrelated
   permutation conjugacies at separate resolutions.
5. Coset preservation implies Haar preservation. Pullback has the stated
   intertwining orientation; restriction to every finite projection recovers
   the trace count in the reverse implication. The character decomposition,
   Mobius projections and self-adjoint direct-sum domains in section 8 are
   valid. None implies a target determinant.
6. The odd/even representatives have the required determinant, content and
   mgcd, also at D=0 and D=-1. The derivative obstruction follows from norm
   preservation along each sequence `2^k x`: a derivative would be integral
   invertible and hence an excluded linear local conjugacy.

The coordinator also ran the author's new `orbit_tree_check.py` once with
`python -B` from the repository root: exit 0, fifteen paired finite towers
and three stated hostile controls. This reproduces a finite diagnostic; it
is not an independent all-height proof or an additional novelty certificate.
The independent reasoning above, not the finite receipt, addresses the
universal claims. No old sealed test was rerun.

## Primary-source ownership actually checked by this reviewer

The reviewer opened the published [Baake--Roberts--Weiss author PDF](https://web.maths.unsw.edu.au/~jagr/BRW08.pdf),
read the introduction and sections 4.2--4.3 through Corollary 4, and verified
that the linear local classification and its compatible profinite form are
explicitly classical. Corollary 3 is a forward statistics implication; it
does not itself state the proposed nonlinear inverse quotient.

The reviewer read the opening and exact orbit-tree criterion in section 1.1
of [Ivanov's original preprint](https://arxiv.org/pdf/0806.4024), including
the explicit Gawron--Nekrashevych--Sushchansky attribution. The original GNS
article's complete proof was not retrieved by this reviewer. Its general
criterion is credited, not claimed as a new lifting theorem here.

The introduction and references of the [2003 Rodrigues--Sousa Ramos preprint](https://arxiv.org/pdf/math/0303185)
positively attribute the older two-dimensional recurrences to the 1996 and
1999 works. The unavailable older theorem texts remain a real access limit;
this review does not erase that limit by using a different observation name.
The new compatible result is distinguished from abstract BF groups and from
BF modules, but no worldwide priority judgment is made.

## Why this is not a new substantial-paper admission

The result answers a coherent complete inverse question. Nevertheless, the
current batch's standard is not simply that a correct answer exists. After
deducting the old census quotient, BRW linear classification, the general
orbit-tree criterion and elementary matrix order lifting, the fresh step is
the homogeneous dyadic incidence calculation in section 5. The profinite
product, filtered Koopman equivalence, radial-operator observation and
derivative contradiction are direct consequences of that same construction.
They do not close independent additional research questions or constitute
separate papers. The old source-access limitation could further reduce the
unclaimed inherited portion.

Accordingly the coordinator preserves the complete proof as a useful source
information-loss companion but does not spend a paper slot on it. This is a
bounded editorial/substance decision, not a claim that the result is known
verbatim or cannot be publishable in any venue. Reconsideration would need
an independently significant added theorem or materially clarifying primary
ownership, not extra pages, another small matrix family, or target labels.

All target-arithmetic constructions remain absent. No Route A tuple, A2
success, Euler/root-number claim or Route B entry is inferred from this
mathematical review.
