# HCS-C24 source-lock roadmap: Rauzy--Veech chronology with a metaplectic fibre

**Date:** 2026-08-09

**Status:** `COMPLETED_SCOPED_OBSTRUCTION; CANONICAL_ANALYTIC_APPLICATION_OPEN`

**Reason for switch:** C22G closes with open nuclear/all-word gates and C23
closes at a fixed-word cyclic-resultant baseline. No larger Hénon ledger is
authorized.

## Completed outcome

The round is released in
[`../rauzy_metaplectic_obstruction/`](../rauzy_metaplectic_obstruction/).
The literal permutation passed source lock: the fixed-label Rauzy class has
seven states and fourteen edges, its crossing form has rank four and
determinant one, and the stratum is \(\mathcal H(2)\).  Exact enumeration
through elementary length 12 gives 828 primitive fixed-label cycle codes, of
which 146 are eventually positive in every cyclic phase.  Twenty-one selected
codes lie on \(\det(I-M)=0\), so the regular point formula for the Weil
distribution character cannot define a finite weight on the full selected
labeled-cycle set.  The 146 selected codes realize 41 reciprocal
characteristic polynomials, but cycles are not quotiented by this spectral
coincidence.

The operator gate closed two broad realization classes.  A nonzero
exact/modulo-compact branch compression has positive essential norm, and an
absolutely norm-summable discrete metaplectic atomic sum on Hilbert base
spaces is noncompact whenever one central-sign-aware aggregate is nonzero.
No particular canonical analytic Zorich space has yet been shown to satisfy
either application hypothesis.  Thus the unrestricted operator proposal is
not declared globally dead; the formal result is

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

The text below is retained as the original pre-registered roadmap.

## Big-door question

Replace the switched Hénon map by a countable-return model for a genus-two
Teichmüller flow. The base carries a chronological integral homology cocycle,
and the cocycle has a natural infinite-dimensional metaplectic lift. The
single question is:

> Can the chronology-preserving metaplectic extension of a standard
> Rauzy--Veech--Zorich transfer operator possess an ordinary nuclear Fredholm
> determinant, or does its unsmoothed unitary fibre force noncompactness?

This is deliberately one large operator gate. A negative theorem closes each
realization class only after its stated application hypotheses are verified;
finite oscillator truncations are not a fallback.

## Proposed frozen object

Start from the four-letter reversal permutation

\[
\pi_0=
\begin{pmatrix}
1&2&3&4\\
4&3&2&1
\end{pmatrix}.
\]

The source-lock gate S0 must reconstruct its Rauzy class, singularity data,
genus, and absolute-homology intersection form directly from the
combinatorics. The intended component is the genus-two hyperelliptic
component customarily denoted \(\mathcal H(2)\). If the literal permutation
does not produce that object under the implemented convention, C24 stops;
the permutation may not be silently replaced after data are inspected.

Take a fixed Zorich acceleration and a fixed first-return section to the
declared base state. Each return branch \(h\) has a roof \(r_h>0\) and an
integer Rauzy--Veech matrix. Edge matrices transport the intersection forms
between Rauzy states; a closed return word induces an absolute-homology
matrix

\[
\overline B_w\in\operatorname{Sp}(4,\mathbb Z).
\]

For a chronological word \(w=e_1\cdots e_n\), later edges act on the left:

\[
B_w=B_{e_n}\cdots B_{e_1}.
\]

No averaged cocycle is permitted.

The primitive objects are primitive directed closed return words, quotiented
only by cyclic phase. Direction, the metaplectic central sign, and all
proper-power metadata are retained. For a positive pseudo-Anosov loop, the
intrinsic period candidate is

\[
\ell(w)=\log\lambda_{\rm PF}(B_w),
\qquad
\ell(w^r)=r\ell(w).
\]

No prime table, Riemann-zero table, affine time fit, or post hoc unfolding is
allowed.

## Natural quantum fibre

Lift the closed-loop absolute-homology cocycle chronologically to the
metaplectic double cover. The lift must be fixed edge by edge from a declared
path convention, so the central sign cannot be discarded. Its oscillator
representation acts unitarily on \(L^2(\mathbb R^2)\):

\[
U_h=\mu(\widetilde B_h).
\]

The proposed branch-resolved transfer operator is

\[
\mathcal L_s^{\rm Mp}
=\sum_h e^{-s r_h}K_h\otimes U_h,
\]

where \(K_h\) is the standard inverse-branch operator on the frozen Zorich
base space. No heat factor, oscillator cutoff, or finite-dimensional
replacement is part of the candidate.

The Weil/metaplectic character is a distribution character. Any familiar
expression involving a phase and \(|\det(I-\overline B_w)|^{-1/2}\) must be
reconstructed with its hypotheses, Haar normalization, lift, and Maslov/Weil
index convention. It must not be called the ordinary Hilbert-space trace of
the single unitary \(U_w\).

## The first kill theorem

### Elementary tensor obstruction

Let \(K\ne0\) be compact on a Hilbert or Banach space and let \(U\) be a
unitary operator on an infinite-dimensional Hilbert space. Then

\[
K\otimes U
\]

is not compact. Choose \(x\) with \(Kx\ne0\) and an orthonormal sequence
\((e_j)\). The bounded sequence \(x\otimes e_j\) is sent to
\(Kx\otimes Ue_j\), whose pairwise distances are constant and nonzero, so
its image has no convergent subsequence.

The nontrivial application gate is therefore exact branch isolation. On the
declared graph-directed space, prove or refute the existence of bounded
input/output cylinder projections satisfying

\[
P_h^{\rm out}\mathcal L_s^{\rm Mp}P_h^{\rm in}
=e^{-sr_h}K_h\otimes U_h
\]

for one nonzero branch. If such a compression exists, compactness and
nuclearity of the full operator are impossible. If analytic continuation
spaces do not admit these projections, a different proof is required; one
may not infer noncompactness of a sum solely from noncompactness of its
formal summands.

## One-round work packages

### S0 -- primary-source and convention lock

- derive the Rauzy graph, genus, stratum, intersection forms, edge transport,
  Zorich acceleration, and roof convention;
- distinguish relative from absolute homology and edge transport from
  closed-loop symplecticity;
- freeze the metaplectic path lift and central sign;
- reconstruct the distribution-character formula from a primary source.

### S1 -- exact chronological ledger

Enumerate primitive positive loops through combinatorial length 12. Emit the
literal word, cyclic representative, orientation, proper-power audit,
chronological matrix, reciprocal characteristic polynomial, symplectic-form
check, exact \(\det(I-B_w^r)\) for \(r\le6\), and a certified isolating
interval for \(\lambda_{\rm PF}\). A second implementation must rebuild the
Rauzy graph and matrices without importing the producer.

This ledger validates the object; it is not evidence for Riemann zeros.

### S2 -- ordinary Fredholm obstruction

Freeze the actual graph-directed base space and prove the branch-compression
lemma or a direct essential-norm lower bound. Combine it with the tensor
obstruction to decide compactness of \(\mathcal L_s^{\rm Mp}\) on a nonempty
domain.

### S3 -- diagnostic only

Oscillator cutoffs may visualize the repeated singular values of
\(K_h\otimes U_h^{(N)}\) as \(N\) grows. The plot must be labelled as a
finite-dimensional illustration of S2, never as a proof or a convergent
Fredholm approximation.

## Mandatory mutation tests

The release must reject:

- averaged Rauzy matrices or reversed chronological multiplication;
- proper powers reported as primitive;
- loss of orientation or cyclic multiplicity;
- treating relative-homology edge matrices as one fixed symplectic action
  without transport;
- deletion of the metaplectic central sign;
- a distribution character labelled as an ordinary operator trace;
- a heat factor or oscillator cutoff inserted to manufacture trace class;
- finite-cutoff spectral stability promoted to an infinite determinant.

## Pass, kill, and Route-A boundary

**Kill:** prove that the unsmoothed chronological operator is not compact
under explicit realization hypotheses, or fail to define one canonical
branch-resolved operator and lift. Record a `PROVED_SCOPED_OBSTRUCTION` and
close only the realization class covered by the proof.

**Pass:** only a trace-class compression, semifinite determinant, or other
trace object forced uniquely by Rauzy/KZ geometry can survive. It must be
cutoff independent, retain chronology and the central sign, and obey exact
repetition. An arbitrary \(e^{-\beta N}\) regularizer does not pass.

Before S0, the candidate is not formally Route-A testable. Even after S0,
the expected first verdict is A1 weak, A2 fail unless an ordinary or
canonically generalized determinant survives, A3 fail, and A4 at most a
natural-quantization hint. No Route-B invocation is authorized.

## Prior-art boundary

The Rauzy--Veech/Kontsevich--Zorich cocycle, hyperelliptic Rauzy--Veech
groups, and Weil/metaplectic character are classical inputs, not proposed
discoveries. Initial primary controls are:

- A. Avila and M. Viana, *Simplicity of Lyapunov spectra: a sufficient
  criterion*, [arXiv:math/0607757](https://arxiv.org/abs/math/0607757);
- A. Avila, C. Matheus, and J.-C. Yoccoz, *Zorich conjecture for
  hyperelliptic Rauzy--Veech groups*,
  [arXiv:1606.01227](https://arxiv.org/abs/1606.01227);
- T. Thomas, *The Character of the Weil Representation*,
  [arXiv:math/0610644](https://arxiv.org/abs/math/0610644).

The only possible C24 contribution is the precise compatibility or
obstruction theorem for the source-locked chronological Fredholm object.

## Why this outranks another C23 scan

C23 can currently add only finite ramification rows to a fixed-word object
already controlled by cyclic-resultant theory. C24 directly joins a natural
primitive flow, a chronological integral symplectic cocycle, and a natural
infinite-dimensional quantum representation, then subjects the missing
Fredholm bridge to an all-period operator theorem. Either outcome is a large
structural result.
