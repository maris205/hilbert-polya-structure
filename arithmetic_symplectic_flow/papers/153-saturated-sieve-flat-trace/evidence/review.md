# Bounded mathematical review — ASFS-20260915-SFT01

**Date:** 2026-09-15.  
**Candidate status:** ADVANCE — FULL-MAP FLAT TRACES AND GRADED ZETA IDENTITY; FREDHOLM AND TARGET CLOCK OPEN.  
**Review result:** no mathematical defect found in the stated full-kernel
flat-trace construction, convergence domains or graded identity; one
control-definition clarification recommended.

The reviewer first read the [frozen card](../candidate-card.md) and the
separate [147 proof](../../147-saturated-drift-cotangent-sieve/paper.md),
then derived the requested kernel, weights and convergence tests before
reading the completed [153 paper](../paper.md). The assignment itself
included formulas to test: this was not a result-blind review. No other
153 reviewer report was supplied. A separate invocation and bounded
derivation do not establish independent error processes, human peer
review, calibrated review or formal verification. The manuscript was
not uploaded to an external model.

## 1. Full noncompact operator and diagonal restriction

The frozen domains are compactly supported smooth sections of the degree
j exterior cotangent bundles over the full all-integer surface. Since
F and F inverse are continuous, preimages of compact sets under F are
compact; smooth pullback is continuous on these test-section spaces.
No boundedness on a default Hilbert completion is needed for this
statement.

With x the output variable of the operator and y the input variable, the
kernel is
\[
K_{j,m}(x,y)=\Lambda^j(DF_x^m)^T\delta(y-F^m x).
\]
The direction of this kernel agrees with U_j=F^*, not with the inverse
pullback. At a fixed point, the matrix acts on the same exterior fibre
and has a well-defined ordinary finite-dimensional trace.

The global periodic proof has the necessary scope. Summing the actual
configuration increments over m=rK_n excludes every composite cycle.
In prime fibres, the monotone sign drift forces q=0 and the contracting
momentum equation forces p=0. This leaves all K_p phase points, not one
chosen representative, for every prime with K_p dividing m.

For each such point,
\[
DF_x^m=\operatorname{diag}(\lambda^m,\lambda^{-m}),\qquad\lambda=3/2.
\]
Neither multiplier is one. The graph and diagonal are therefore
transverse at every intersection, and the local delta change of
variables has denominator
\[
|\det(I-DF_x^m)|=\lambda^m+\lambda^{-m}-2=B_m>0.
\]
The absolute value is essential: the signed determinant is negative.

The noncompactness issue is resolved at the level actually claimed.
Any fixed point satisfies K_n<=m and hence n<=2^{m+1}, while its two
real coordinates are zero. Thus the complete fixed set is finite.
At every other finite point a neighbourhood of the diagonal misses the
graph, so the restricted distribution vanishes there. The resulting
global diagonal restriction is a finite sum of point masses and has
compact support. Pairing it with one is well-defined through any
compactly supported test function equal to one near that full support.
This is not a change of the original operator domain or a selection of
prime representatives.

No uniform transversality constant at spatial infinity is required for
this local restriction followed by compactly supported integration.
Conversely, this argument must not be silently promoted to a global
heat-kernel or smoothing-regularization trace limit: controlling any
mass escaping to infinity would be a separate obligation. The paper
does not claim such a limit.

The reviewer checked the author-hosted
[Dyatlov--Zworski source, Section 2.4](https://math.berkeley.edu/~zworski/zeta.pdf)
for the definition of a flat trace by diagonal kernel restriction.
Its compact-manifold setup and continuation results are not transferred.
The support and transversality arguments above are candidate-specific.

## 2. Trace weights, sign and phase multiplicity

The exterior-power traces at a fixed point are, respectively,
1, lambda^m+lambda^{-m}, and 1. Counting the full fixed set gives
\[
N_m=\sum_{p:K_p\mid m}K_p,\qquad
T_0(m)=T_2(m)=N_m/B_m,
\]
\[
T_1(m)=N_m+2N_m/B_m,\qquad
T_0(m)-T_1(m)+T_2(m)=-N_m.
\]
These agree with the actual manuscript. The K_p factor counts all
section points; with m=rK_p, division by m supplies 1/r and does not
erase primitive multiplicity.

An exact low-iterate illustration checks both the empty n=2 block and
the sign. At m=1 the only contributing primes are 2 and 3, so
\[
N_1=2,\quad B_1=1/6,\quad
T_0(1)=T_2(1)=12,\quad T_1(1)=26.
\]
The graded trace is therefore -2. This is direct rational substitution,
not a numerical run or a finite-sample basis for any global claim.

For the frozen exponential convention, the negative graded trace gives
\[
\log(D_0D_2/D_1)
=\sum_{m\geq1}e^{-sm}N_m/m=\log Z(s)
\]
on the common convergence domain. Thus the quotient is Z, not its
reciprocal; no sign or normalization constant is missing.

## 3. Convergence and product expansion

The proof of the ordinary logarithmic series has exact absolute
abscissa log 2. Its upper bound sums over all integers in dyadic blocks.
Its lower bound uses the first repetitions and
2^{-K_p}>=1/p, together with the elementary reciprocal-prime
divergence argument displayed in the paper. No prime number theorem is
needed.

For every positive m,
\[
\frac1{B_m}
=\frac{\lambda^{-m}}{(1-\lambda^{-m})^2},\qquad
\lambda^{-m}\leq B_m^{-1}\leq9\lambda^{-m}.
\]
The absolute logarithmic series of D_0 and D_2 is therefore comparable
term by term to the ordinary logarithmic series shifted by log lambda.
This proves the exact absolute abscissa log(4/3), including divergence
at that boundary. Since T_1=N_m+2T_0(m) has nonnegative coefficients,
its exact absolute abscissa is log 2.

Normal convergence on strict half-planes follows by using a compact
set's minimum real part in these positive majorants. The exponential
functions are holomorphic and nonzero on the stated domains.

Finally,
\[
B_m^{-1}=\sum_{\ell\geq1}\ell\lambda^{-\ell m}
\]
and absolute summability justify the order of summation in the paper.
They give precisely
\[
D_0(s)=\prod_p\prod_{\ell\geq1}
(1-e^{-(s+\ell\log\lambda)K_p})^\ell,
\qquad \Re s>\log(4/3).
\]
The integer exponent ell is derived from the geometric series for the
actual stability denominator. It was not inserted as a prime weight.
The quotient identity uses the smaller common domain Re(s)>log 2.
An exact absolute abscissa is not an analytic-continuation obstruction,
natural-boundary theorem or spectral divisor identification.

## 4. Operator and claim-strength boundaries

The scalar pullback is unitary on the full symplectic-area L2 space.
An infinite orthonormal sequence stays norm-separated under any
nonzero scalar multiple, so that operator is not compact or trace
class. Consequently the scalar trace exponential is not justified as
the usual trace-class Fredholm determinant on that Hilbert space.

This does not say that I-e^{-s}U_0 is a non-Fredholm operator. For
Re(s)>0 it is in fact invertible by the Neumann series. The paper
correctly distinguishes a missing trace-class determinant from this
different Fredholm-operator question.

For one-forms, the full derivative has a momentum-dependent coefficient
-p f''(q)/(f'(q))^2. Boundedness on a default Euclidean L2 form norm
must not be inferred from the scalar unitary statement; the manuscript
does not make that inference.

The positive result is an actual distributional flat trace of specified
full operators and its convergent analytic identity. It is not merely
an orbit product relabelled as an operator trace, because the full
graph kernel, permitted diagonal pullback and compact restricted support
have been supplied. It also is not a trace-class Fredholm realization.
The rounded binary clock, generic constraint-engineering limitation,
absent Riemann target divisor and absence of formal Route evaluation
remain separate. Route B is NOT INVOKED.

## 5. One small control-definition recommendation

The initially reviewed Section 6 row says that deleting or shifting
witness tests changes the support to all integers or to n+1 prime,
respectively. The deletion rule b=0 is clear and follows directly
from the current proof. The word shifting, without the complete
modified rule or an exact external-control link, is not enough to
identify the second comparator.

The minimum remedy is to retain just the b=0 comparator in that row.
Alternatively, specify the complete all-formulas shift and its
separate owner, with no credit transferred to this card. This is a
control-definition precision issue, not a defect in Propositions 1--5
or a request to change the frozen object. Root authorship owns any
manuscript correction.

**Adjudication, 2026-09-15: ADDRESSED.** The reviewer checked the revised
Section 6 row: it now specifies only deletion of witness tests, b=0,
whose return support is all integers, explicitly as a different comparator.
The undefined shifted-test half was removed. This is a control-description
clarification; the frozen candidate, formulas and mathematical results did
not change, so no mathematical rerun was needed. The original finding is
retained above as the review history.

## Handoff

Advance the bounded full-map flat-trace and graded-zeta result with its
explicit analytic domains. The same-object ledger remains intact.
The comparator clarification is complete, as recorded in the ADDRESSED
adjudication above. Retain the no-Fredholm, no-continuation and rounded-clock
boundaries. No additional computation,
global theorem import or Route coordinate is warranted by this review.
