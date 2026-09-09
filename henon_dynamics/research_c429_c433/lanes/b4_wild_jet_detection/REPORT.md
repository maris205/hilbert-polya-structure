# B4: scale-free periodic jets and the exact local-model failure boundary

2026-09-09. Lane-owned scout; no manuscript admission, formal evaluation,
mathematical execution, build, Git write, or external-model upload.

## Frozen question

Let $E/\mathbb Q_p$ be any finite extension, $m>r\ge1$,
$d=p^m$, $k=p^r$, $a\in E^\times$, $c\in E$, and

$$
F(x,y)=(y,y^d+cy^k-ax).
$$

The phase space is $\mathbb A^2(\overline E)$ and the clock is one
application of $F$. Points, not nonreduced scheme lengths, define cycles.
For a point $P$ of least period $n$, let
$g_P(z)=F^n(P+z)-P$. For $N\ge1$ let $j_Ng_P$ be its Taylor jet,
with coefficients normalized as coefficients of monomials (Hasse/Taylor
coefficients), not unnormalized iterated derivatives.

The question frozen here is whether **scale-free integral higher-jet data,
even with compatible one-step charts around each entire native cycle,
characterizes potential all-affine regular good reduction**, and, if not,
what its complete parameter failure boundary is. Its precise scalar
observable is

$$
\mathcal J_N(P)=\inf_{L,A}\max\{1,
 \|j_N(A^{-1}g_PA)\|_{\mathrm{coeff}},
 \|j_N(A^{-1}g_P^{-1}A)\|_{\mathrm{coeff}}\},                 \tag{1}
$$

where $L/E$ ranges over finite extensions containing $P$ and
$A\in\mathrm{GL}_2(L)$. The coefficient norm uses the maximum absolute
value, $|p|=p^{-1}$. Thus the normalization is an explicit optimization
over all tangent lattices, **including their scale**; it does not secretly
fix the displayed Hénon coordinates or a volume form. The definition is
invariant under every affine conjugacy over a finite extension.

The strengthened compatibility test asks for one finite extension and
affine charts centered at the points of each individual cycle such that
all its one-step transitions and inverse transitions have integral
coefficients, simultaneously in every order. Different cycles may have
different charts and scales. This quantifier is deliberate; it is not one
global affine good model. The success claim would be equality with the
potential-good-reduction locus. A decisive refutation is a complete
larger parameter locus satisfying all these local tests, not a low-period
example or a claim that an arbitrarily chosen jet norm is intrinsic.

## Outcome and exact boundary

**PROVABLE AS STATED: the frozen test has a complete failure boundary.**
The proof is in [PROOF_SUPPLEMENT.md](PROOF_SUPPLEMENT.md), not an
experimental inference. For any polynomial automorphism germ in any
dimension over a finite extension of $\mathbb Q_p$, and every $N\ge1$,

$$
\mathcal J_N(P)=\max_i\{1,|\lambda_i(D F^n_P)|,
                              |\lambda_i(D F^n_P)|^{-1}\}. \tag{2}
$$

The infimum is attained. For polynomial germs the same chart can attain
(2) for the entire forward and inverse polynomial, hence every jet order
at once. More strongly, an entire native cycle has the compatible
one-step integral charts defined above if and only if its return
multipliers are all units. One can arrange every nonlinear transition
coefficient to lie in the maximal ideal. Thus the reduced local charts
can all be linear even when global regular good reduction is impossible.

Consequently, importing rather than reproving WM6, every finite $N$, the
entire jet tower, and the cycle-compatible version pass for all periodic
points exactly when

$$
|a|=1,\qquad |c|\le C_*:=|p|^{-r(d-k)/(d-1)}.              \tag{3}
$$

Potential all-affine regular good reduction holds exactly when
$|a|=1$ and $|c|\le1$. The complete false-positive region of this
strengthened local integral-jet test is therefore

$$
|a|=1,\qquad 1<|c|\le C_* .                              \tag{4}
$$

The endpoints, $p=2$, $a=-1$, $c=0$, nonunit $a$, arbitrary finite base
extensions, all least periods, repeated multipliers, and nonsemisimple
return matrices are included. This is not uniformity of one radius or
one field extension across infinitely many cycles: those are not in the
frozen observable.

## Two further exact interfaces, not extra paper candidates

1. Pullback on the finite local algebra
   $\mathfrak m_P/\mathfrak m_P^{N+1}$ has eigenvalues
   $\lambda_1^i\lambda_2^j$, $1\le i+j\le N$. Hence taking the spectra of
   higher jets, even at every order, cannot improve the original unit-norm
   test. The joint forward/inverse spectral radius to the power $1/N$
   equals the right side of (2).
2. Any continuous conjugacy-invariant function on the full space of
   invertible $N$-jets, taking values in a Hausdorff space, factors through
   the linear part: scalar conjugacy contracts every term of order at
   least two to zero. Every globally regular algebraic class function of
   an invertible plane $N$-jet is accordingly a regular function of trace
   and determinant, with determinant inverted. These are **extension-to-
   the-linear-locus** results, not a theorem that raw formal conjugacy
   classes or rational invariants contain no nonlinear information.

The second interface does not say exact derivatives have the same values
throughout (4): WM6 proves only an equality of multiplier *norms*. Exact
trace-spectrum reconstruction remains a different, source-owned problem.

## What is not proved or claimed

There is no universal impossibility theorem for every conceivable
finite-jet observable. In particular, this result does not exclude:

- a singular/rational invariant defined only away from the linear locus;
- a chosen volume form, a common scale across all cycles, or a lattice
  calibrated by the global leading homogeneous terms;
- correlated jet data using the relative positions of distinct periodic
  points in a common ambient chart;
- exact multiplier/trace reconstruction, or nonlinear conjugacy strata.

Such additions must be specified and justified separately. Calibrating by
the degree-$d$ forward and inverse leading tensors recovers the scale
which the present minimization discards; but a degree-$d$ fixed-point jet
already contains the entire degree-$d$ polynomial map. Reading its
coefficient $c$ is not a new inverse-spectral mechanism. No such
reconstruction is relabeled as this lane's contribution.

## Source subtraction and actual access

Local sources were read first:

- WM6's [contract](../../../research_c424_c428/continuation_round6/arithmetic_spectral/FROZEN_CONTRACT.md),
  [proof](../../../research_c424_c428/continuation_round6/arithmetic_spectral/PROOF_PACKAGE.md),
  and [source/disposition record](../../../research_c424_c428/continuation_round6/arithmetic_spectral/SOURCE_AND_DISPOSITION.md).
  All WM6 phase formulas are imported outputs, not a new B4 calculation.
- GR5/C426's [proof, local Sections 1–2](../../../research_c424_c428/continuation_round5/arithmetic/PROOF_PACKAGE.md).
  Its all-affine leading-term separation and unique common-disk scale
  explain exactly why tiny independent local models do not supply a
  global regular good model. The global ideal-class obstruction is not
  used or reproved.

Primary-source browsing accessed:

- [Robert L. Benedetto, *Determining Potential Good Reduction in Arithmetic
  Dynamics*, original 2015 slides](https://math.colorado.edu/arithmetic2015/slides/Benedetto.pdf),
  title/date and PDF pages 2–9 via extracted text, especially page 8.
  The one-dimensional wild no-repelling/non-potential-good phenomenon is
  expressly source-owned. This is an original lecture source, not a
  claimed journal proof of the present jet statement.
- [Cantat–Dujardin, *Multiplier rigidity for complex Hénon maps*,
  arXiv:2603.09445v1](https://arxiv.org/html/2603.09445v1), introduction
  Sections 1.2–1.5 and Theorems A–B as retrieved. Finite ambiguity from
  exact trace spectra and bounded-period finite determination are not
  claimed here as new results. This access was not a full review of their
  Lyapunov or rigidity proofs.
- Targeted searches for jet-conjugation invariants and local integral
  germs also found formal-normal-form and differential-invariant work,
  but no retrieved primary theorem was used to replace the elementary
  proofs below. Failure to locate an identical statement is not a
  worldwide novelty certificate.

Search query groups used the phrases “non archimedean polynomial
automorphism higher jets good reduction multipliers”, “non archimedean
analytic germ integral linearization invariant lattice unit eigenvalues”,
“Benedetto determining potential good reduction no repelling periodic
points wild”, “invariants conjugation jets diffeomorphisms invariant ring
linear part scalar dilation”, “jet group conjugation polynomial invariants
characteristic polynomial derivative”, and “formal diffeomorphism
conjugacy invariant regular functions jets linear part”. No private
manuscript was transmitted. Web snippets from mirrors, encyclopedias,
automated summaries, and third-party commercial archives were not treated
as theorem evidence.

## Transfer and disposition

For B3: integral analytic neighborhoods around every periodic cycle,
even with simultaneous inverse integrality and all jet orders, do not
imply the single regular affine good model whose classification B3 uses.
The missing condition is global calibration/compatibility, not a higher
Taylor order. Use the cycle-chart lemma in the supplement directly.

For A4: the filtered-jet spectral lemma works in every characteristic.
If a proposed refinement only takes characteristic polynomials of the
local jet action, it sees symmetric powers of the derivative, not the
off-diagonal extension data. This does not invalidate integral/Witt
structures that retain actual multiplication or nontrivial extension
classes. No wild local length is reconstructed here.

A4 subsequently read the complete proof of supplement Section 4 and
confirmed its hypotheses in its one-dimensional unit-multiplier local
counterfamily: every ambient depth-$N$ action there has characteristic
polynomial $(T-1)^N$, while the dynamical fixed-algebra length varies.
That recipient-side application belongs to A4's report; it is not a B4
proof of A4's ramification construction or A3's missing Artin–Schreier
nonvanishing lemma.

The current X2 lane supplies a complementary
[raw fixed-depth counterexample](../x2_obstruction_transfer/PERIODIC_JET_COUNTEREXAMPLE.md),
read in full here: for each prescribed $N$, a map over $\mathbb Q_p$
already has all centered native return $N$-jets integral in the common
translated ambient basis, but has no potential affine good model. Its
degree grows with $N$. B4 instead handles every order of a fixed map
simultaneously, while permitting independent lattice scales. Neither
scope should be silently promoted to fixed-degree, globally calibrated
jet reconstruction, and the two statements are not separate paper
admissions. The X2 proof's binomial estimate and GR5 interface were
checked in this focused reading; that is not the coordinator's formal
independent review or a new result claimed by B4.

Recommended disposition: **complete auxiliary no-go/interface package;
not self-admitted as one of the five papers**. The stronger compatible
whole-germ statement is useful, but its proof is elementary local lattice
theory plus contraction; the general mechanism and WM6 phase formulas
must be subtracted before judging independent paper substance.

The batch/proof-writer skills enforced one exact question, full quantifier
and normalization disclosure, no arbitrary pilot, and this explicit
limitation. The research-lit/idea-creator defaults were used only for
local-first source subtraction and pruning under the current team/no-
external-upload contract, not an old-model/GPU pipeline. The ARS router
was inspected; no full ARS workflow or external verification was run.

`NO_BAD_EULER_OR_ROOT_NUMBER`: these are source-local germs and matrices,
not target Euler factors, root numbers, automorphy, zero correspondence,
or a Hilbert–Pólya realization.
