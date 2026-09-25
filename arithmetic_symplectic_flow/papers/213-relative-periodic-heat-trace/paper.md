# A relative heat trace that recovers the periodic-channel orbit distribution

**Paper ID:** 213-relative-periodic-heat-trace  
**Candidate ID:** AQC-20260916-RHT01  
**Research date:** 2026-09-16  
**Status:** CONTROL ADVANCE — RELATIVE PERIODIC-CHANNEL TRACE RECOVERS THE POSITIVE-TIME ORBIT COMB; FULL-STATE TRACE NOT SUPPLIED; NATURALNESS OPEN.  
**Type:** EXTERNAL REPRESENTATION CONTROL, NOT A NEW FULL-STATE CANDIDATE.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

For the actual singleton circles of the completed arithmetic cone flow,
we subtract a windowed covering-line heat trace from the corresponding
circle heat trace. Both terms are genuine trace-class operator traces
before removing the finite atom cutoff. Their difference cancels the
zero-winding term and leaves the Gaussian peaks at every nonzero repeat
time. Exact all-integer tail bounds give a locally uniform infinite-atom
sum for each positive heat parameter. Its vanishing-heat limit on open
positive time is the primitive-period-weighted closed-orbit distribution.
Neither infinite sector separately has an ordinary trace, and the chosen
invariant-measure representation already ignores mixed-state observations.
Thus this is a constructive relative-trace control with exact arithmetic
periods, not an intrinsic full-state trace, natural-source theorem, Euler
determinant or formal Route result.

## 1. Frozen owner and the observation-channel boundary

The [version-1 card](candidate-card.md) precedes this proof. Retain the
entire geometric owner of [194](../194-rapid-decay-cone-completion/paper.md):

\[
 E=\{v:\sum_a a^k|v_a|<\infty\ \text{for all integers }k\ge0\},
 \quad \widehat P=E_+\setminus\{0\},\quad
 (Dv)_a=a v_a,\quad \widehat X=\widehat P/\langle D\rangle,
 \quad \phi_t[v]=[e^t v].                                  \tag{1}
\]

Here the indices are the derived nonzero classes q_a of the nonunit
ideal modulo its square in the all-positive-integer monoid algebra.
The source is not a supplied prime table. The prior proof gives exactly
one singleton circle C_a with least positive physical time L_a=log a,
every positive repeat, and no mixed-support periodic state. All finite
and infinite supports remain in (1), with the original all-norm topology.
The section, return and roof are unchanged. Real coordinate r on C_a
means the actual state [exp(r)q_a], with r modulo L_a.

| Item | Exact owner | Limitation |
| --- | --- | --- |
| Arithmetic and full geometry | All-integer indecomposable source and completed quotient (1) | Declared design; naturalness OPEN |
| Circles, clock and repetition | Existing actual C_a, L_a and phi_t | No new roof or per-prime period choice |
| Periodic observation Hilbert space | H_per=L2(X_hat,mu), mu=sum_a w_a lambda_a, w_a=2^(-a)/sum_b2^(-b) | 205's invariant-measure representation; not faithful to mixed observations |
| Circle heat and actual translation | Gaussian periodization in the actual time coordinate | Operator of this circle channel, not exact 204 H |
| Relative comparator | The same time circle's universal covering line; one fundamental-length window | Explicit auxiliary covering owner, not an unrelated determinant |
| Infinite trace prescription | Paired finite-atom trace differences, then cutoff removal, then heat limit | Not an ordinary trace of an infinite graded direct sum |
| Classical symplectic/contact/quantum fields | NOT APPLICABLE / NOT SUPPLIED | No Route-B or spectral-identification claim |

The [prior-work arrow](../../docs/prior_work/README.md) is proper-factor
symbolic admissibility -> indecomposable arithmetic source -> positive
geometry -> actual periodic-channel analysis. No Logistic/Henon
conjugacy or naturalness of this algebraic replacement is asserted.

[205](../205-invariant-measure-support/paper.md) proves that the measure
class used here ignores a nonzero bounded continuous mixed-state
observable. This defect is an input boundary, not something cured by
the trace calculation. The fixed full-state representation of 204 and
the faithful covariance of 209 are not being used or replaced.
The whole geometric carrier has not lost its mixed states, but the
chosen analytic channel does not distinguish all of them.

## 2. Actual heat and translation operators, with normalization explicit

For epsilon>0 define on the covering physical-time line

\[
 G_\epsilon(u)=(4\pi\epsilon)^{-1/2}e^{-u^2/(4\epsilon)},
 \qquad H_\epsilon^{\mathbb R}f=G_\epsilon*f,
 \qquad V_t^{\mathbb R}f(r)=f(r+t).                         \tag{2}
\]

The Gaussian integral gives total mass one. Completing the square
in a real convolution gives G_alpha*G_beta=G_(alpha+beta).
Young's inequality, or Cauchy--Schwarz against this probability density
followed by integration, proves that H_epsilon is a contraction on
L2(R,dr). Translations are unitary and commute with it.

For a circle of length L define

\[
 K_{\epsilon,L}(r)=\sum_{m\in\mathbb Z}G_\epsilon(r-mL),
 \qquad
 H_\epsilon^L f(r)=\int_0^L K_{\epsilon,L}(r-s)f(s)\,ds,
 \quad V_t^L f(r)=f(r+t).                                  \tag{3}
\]

The series is uniformly absolutely convergent on a period by its
Gaussian tails. It is periodic, even, and integrates to one over
a period. Unfolding the integral using nonnegative terms and the
line convolution identity proves

\[
 \int_0^L K_{\alpha,L}(r-u)K_{\beta,L}(u-s)\,du
       =K_{\alpha+\beta,L}(r-s).                            \tag{4}
\]

Thus (3) is the heat family derived from the actual circle and its
cover. No list of repeat-time delta masses was installed as an operator.

Calculations below use L2([0,L],dr) with periodic identification.
The normalized circle measure dr/L, or w_a dr/L in H_per, differs
by a positive constant. Multiplication by sqrt(w_a/L) is a unitary
identification with L2(dr) and intertwines the same function actions.
Therefore these constants do not multiply the operator trace. If
one writes the kernel relative to ds/L instead of ds, it is
L K_(epsilon,L)(r-s). Omitting this L would give a wrong period weight.

For completeness, on e_k(r)=L^(-1/2) exp(2 pi i k r/L), actual
translation has multiplier exp(2 pi i k t/L) and (3) has multiplier
exp(-epsilon(2 pi k/L)^2). To verify the latter without a Poisson
formula, unfold the Gaussian integral. Its Fourier transform F(omega)
satisfies F(0)=1 and F'(omega)=-2 epsilon omega F(omega), by
integration by parts using uG_epsilon(u)=-2 epsilon G'_epsilon(u).
Hence F(omega)=exp(-epsilon omega^2). The trace proof below uses
Hilbert--Schmidt kernels directly, not a conjectured spectral sum.

## 3. Two genuine trace-class blocks and their exact difference

We use the elementary kernel identity for two Hilbert--Schmidt operators
A,B: their product is trace class, and
Tr(AB)=integral A(r,u)B(u,r) du dr when the product is absolutely
integrable. Cauchy--Schwarz in (r,u) gives that integrability here;
expanding in an orthonormal basis and taking the Hilbert--Schmidt
limits gives the identity. This is not a formal diagonal rule for
an arbitrary bounded operator.

**Proposition 1 (circle block).** For every real t and epsilon>0,
H_epsilon^L V_t^L is trace class and

\[
 \operatorname{Tr}(H_\epsilon^L V_t^L)
    =L K_{\epsilon,L}(t)
    =L\sum_{m\in\mathbb Z}G_\epsilon(t-mL).                 \tag{5}
\]

**Proof.** On the finite circle the bounded kernel K_(epsilon/2,L)
is square integrable. Factor the operator as A B with
A=H_(epsilon/2)^L and B=V_t^L H_(epsilon/2)^L. Both are
Hilbert--Schmidt. Their trace is the double integral of
K_(epsilon/2,L)(r-u)K_(epsilon/2,L)(u+t-r). Equation (4) makes
the inner integral K_(epsilon,L)(t), independent of r. Integrating
one full time circle supplies exactly L. QED.

Let chi_L be multiplication by the indicator of [0,L] on the line.
The endpoints have zero Lebesgue measure and do not affect this operator.

**Proposition 2 (windowed covering-line block).** The operator
chi_L H_epsilon^R V_t^R chi_L is trace class and

\[
 \operatorname{Tr}(\chi_L H_\epsilon^{\mathbb R}
                     V_t^{\mathbb R}\chi_L)=L G_\epsilon(t).
                                                               \tag{6}
\]

**Proof.** Set A=chi_L H_(epsilon/2)^R and
B=V_t^R H_(epsilon/2)^R chi_L. Their product is the proposed
operator, since heat and translation commute. Direct kernel integration
gives

\[
 \|A\|_{\rm HS}^2=\|B\|_{\rm HS}^2
    =L\int_{\mathbb R}G_{\epsilon/2}(u)^2du
    =L G_\epsilon(0)<\infty.                              \tag{7}
\]

The product-trace integral is
integral_(r in [0,L]) integral_R G_(epsilon/2)(r-u)
G_(epsilon/2)(u+t-r) du dr. Gaussian convolution makes its inner
integral G_epsilon(t). This proves (6), with the actual forward
translation convention and no unjustified diagonal evaluation. QED.

For the derived atom cutoff N>=2, the frozen paired difference is
therefore exactly

\[
 R_{\epsilon,N}(t)
  =\sum_{a\le N}\left[
       \operatorname{Tr}(H_\epsilon^{L_a}V_t^{L_a})
       -\operatorname{Tr}(\chi_{L_a}H_\epsilon^{\mathbb R}
                                V_t^{\mathbb R}\chi_{L_a})\right]
  =\sum_{a\le N}L_a\sum_{m\ne0}G_\epsilon(t-mL_a).         \tag{8}
\]

The integer m labels covering translations, or windings. The term
m=0 in (5) is not the Fourier mode k=0: the former is L G_epsilon(t),
whereas the latter contributes the constant 1 to the spectral trace.
This relative subtraction does not contradict the failure of deleting
circle constants in the different SC22-PF filter test.

## 4. Exact infinite-atom convergence

**Lemma 3 (Gaussian tail bound).** For abs(t)<=T and
L>=max(2T+1,1),

\[
 L\sum_{m\ne0}G_\epsilon(t-mL)
 \le {L\over\sqrt{\pi\epsilon}}
       {e^{-L^2/(16\epsilon)}\over1-e^{-L^2/(16\epsilon)}}.
                                                               \tag{9}
\]

For fixed epsilon this is at most C_epsilon L exp(-L^2/(16epsilon)).
For 0<epsilon<=1 it is at most C L exp(-L^2/32), with one
constant independent of t, L and epsilon in this range.

**Proof.** For m nonzero, abs(t-mL)>=abs(m)L/2. Bound the
two Gaussian tails by twice the sum over m>=1 of
exp(-m^2 L^2/(16epsilon)), then use m^2>=m to sum a geometric
series. The denominator in (9) is at least
1-exp(-1/(16epsilon)); if epsilon<=1 it is at least
1-exp(-1/16). Also, for L>=1 and epsilon<=1,

\[
 \epsilon^{-1/2}e^{-L^2/(16\epsilon)}
 \le 4e^{-L^2/32}.                                        \tag{10}
\]

Indeed split the exponent in half and use
sup_(x>=1) sqrt(x) exp(-x/32)<4 with x=1/epsilon.
Equations (9)--(10) give the assertions. QED.

The all-integer comparison

\[
 \sum_a L_a e^{-c L_a^2}
 \le\sum_{n\ge2}(\log n)e^{-c(\log n)^2}<\infty
 \qquad(c>0)                                              \tag{11}
\]

requires no prime-distribution theorem. Once log n>=3/c the summand
is at most (log n)/n^3; the finite initial part is harmless.

**Theorem 4 (fixed-heat relative trace).** For every epsilon>0,
the paired cutoff traces converge locally uniformly in real t to

\[
 R_\epsilon(t)=\sum_a L_a\sum_{m\ne0}G_\epsilon(t-mL_a).
                                                               \tag{12}
\]

This is a finite continuous nonnegative function, defined by the
prescribed relative trace procedure, not by separately summing two
infinite ordinary traces.

**Proof.** On each compact time interval, all sufficiently large atoms
satisfy Lemma 3; equation (11) then gives a summable uniform bound.
There are only finitely many remaining atoms, and their winding sums
converge uniformly on the interval by ordinary Gaussian tails. Each
summand is continuous and nonnegative. Uniform convergence proves the
claim. It also makes the sum independent of the order of paired atom
blocks; it does not permit unpaired subtraction of divergent sectors.
QED.

## 5. The positive-time distribution limit

**Theorem 5 (relative periodic-channel localization).** With the
cutoff removed first as in Theorem 4,

\[
 R_\epsilon\ \longrightarrow
 \mathcal O=\sum_a\sum_{m\ge1}L_a\delta_{mL_a}
 \quad\hbox{in }\mathcal D'(0,\infty)\quad(\epsilon\downarrow0).
                                                               \tag{13}
\]

Equivalently, for every h in C_c^infinity(0,infinity),

\[
 \lim_{\epsilon\downarrow0}\lim_{N\to\infty}
       \int h(t)R_{\epsilon,N}(t)dt
       =\sum_a\sum_{m\ge1}L_a h(mL_a).                    \tag{14}
\]

**Proof.** Extend h by zero to the real line and choose T with its
support contained in (0,T]. For a fixed circle, the Gaussian approximate
identity gives integral h(t)G_epsilon(t-mL)dt -> h(mL) for each
m. This follows directly from uniform continuity of h, mass one,
and Gaussian mass tending to zero outside any fixed interval about
the center. Only finitely many m have abs(m)L<=2T+1. For all other
m, the same estimate leading to (10), now retaining m^2 L^2,
bounds their tested tails by a summable Gaussian sequence uniformly
for epsilon<=1. Consequently the limit can pass through that circle's
entire winding sum. Terms with m<0 do not meet the positive support.

For the atom sum, split off the finite set with L_a<2T+1.
On the rest, Lemma 3 bounds the absolute tested contribution by
C norm(h)_1 L_a exp(-L_a^2/32), summable by (11) and independent
of epsilon<=1. For every one of these large atoms, no nonzero
winding center lies in the support, so its tested contribution tends
to zero by the fixed-circle argument. Dominated convergence handles
the atom tail. The finite remaining set gives precisely (14).

The right-hand side is locally finite: a contributing center below
T requires a<=exp(T) and m<=T/log 2. Thus it defines the stated
distribution rather than only a formal sum. QED.

The coefficient L_a in (13) came from integration over a whole
actual time circle in (5). The repetitions came from the covering
kernel identity, not a manually supplied prime-power trace weight.
At the same time, the circles themselves and their arithmetic periods
were already known geometric inputs. This calculation does not create
a new arithmetic source or prove its naturalness. The claims are only
on open positive time and in the stated order of limits; no t=0
extension or arbitrary joint-cutoff theorem is asserted here.

## 6. Decisive controls and the full-state stop

**Separate sectors diverge.** For every fixed epsilon>0 and real t,
G_epsilon(t)>0. Equations (5)--(6) show that each of the two
unpaired sums is bounded below by, or equals,
G_epsilon(t) sum_a L_a=+infinity. The sum diverges because there
are infinitely many derived atoms and L_a>=log 2. No ordinary
trace of the infinite graded block operator is justified by (12).
Indeed the circle direct sum is already noncompact: the constant
unit vector on each different circle is fixed by every heat-translation
block, giving infinitely many orthonormal images of norm one.
The line direct sum also cannot be trace class, since the sum of
the absolute block traces is infinite. The subtraction must take
place in paired finite cutoffs before passage to the scalar limit.

**Window and measure controls.** Replacing [0,L_a] by any interval
[b,b+L_a] leaves the covering trace unchanged: the trace integral
is translation invariant and depends only on interval length.
Changing the positive circle-mixture weights changes the measure
representation but is unitarily equivalent blockwise for these
operators, so it does not alter (5). No prime-power reweighting has
been used. These controls distinguish the result from 209's sampling-
dependent covariance trace; they do not establish a canonical trace
for all observations on X_hat.

**Generic-circle control.** The proof works for other period sequences
bounded below by a positive number and satisfying
sum_j L_j exp(-c L_j^2)<infinity for every c>0. In particular,
L_j=log(j+1), j>=1, gives the same construction for circles at
all integer logarithms, including composite labels. Merely assuming
L_j->infinity would not justify the needed summability. The localizing
mechanism is universal circle-cover heat geometry, not a new prime
selector. Its arithmetic output here comes from the specific retained
flow's previously proved prime-only periodic ledger.

**Full-state observation is still missing.** H_per is the exact
measure-based channel of 205, where a nonzero continuous observation
of mixed states is zero almost everywhere. Recovering (13) does not
make that map injective. Nothing in the proof constructs heat on the
mixed directions, a full-state Schwartz kernel, a trace on exact
204 H, or an intertwining that transports this result to that H.
Adding identical full-state summands with opposite signs would cancel
them algebraically; such padding would not prove localization on
those summands. We do not make that additional construction.

This is therefore CONTROL ADVANCE for an exact relative periodic
trace, and STOP as a claimed full-state trace realization. The
observation limitation is explicit from the frozen card and is not
hidden by the successful distribution identity. No determinant from
201, no quantum interpretation, and no formal Route coordinate follow.

## 7. Context, gate assessment and handoff

The general microlocal dynamical-trace literature concerns additional
geometric and analytic hypotheses. As a scope reference only, Semyon
Dyatlov and Maciej Zworski's *Dynamical zeta functions for Anosov flows
via microlocal analysis* concerns smooth Anosov flows and their Ruelle
zeta continuation; its [official arXiv record](https://arxiv.org/abs/1306.4203)
and [arXiv DOI](https://doi.org/10.48550/arXiv.1306.4203) were checked
at metadata/abstract level. No theorem, hypothesis verification or
full-paper read from it is claimed here. In particular, its framework
is not simply inherited by the completed cone. The proof above uses
elementary Gaussian kernels and exact local dependencies, and makes
no novelty or literature-completeness claim.

| Obligation | Evidence | Disposition |
| --- | --- | --- |
| Retained source and actual period ledger | Existing 194 owner, unchanged clock and repeats | Dependency, not new A0 credit; naturalness OPEN |
| Finite circle and covering-line operator traces | Propositions 1--2 with explicit Hilbert--Schmidt factors | ESTABLISHED on their specified owners |
| Infinite paired relative trace and positive-time localization | Lemma 3 and Theorems 4--5, all-integer tail bounds | CONTROL ADVANCE |
| Ordinary infinite-sector or full-state trace | Separate divergences and inherited mixed-observation loss | NOT SUPPLIED; STOP any promotion to that claim |
| Continuation, determinant, target divisor, spectral identification | Not constructed or imported | NOT EVALUATED / NOT CLAIMED |
| Classical A0--A2 / formal Route / B | No classical or formal evaluation | NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

The exact gain is an operator-derived relative distribution with the
correct geometric repeat coefficients, achieved without a fitted trace
weight. The decisive cost is that its analytic channel already sees
only circles. Keep it as a positive localization benchmark. A further
construction must address the mixed directions or explicitly fork to
a different carrier; it cannot rename this control as a full-state
success or continue by adjusting heat parameters in this card.

The [frozen card](candidate-card.md), [claim ledger](claim-ledger.md)
and [evidence index](evidence/README.md) record the definitions, scope,
actual review and mechanical checks. No numerical experiment or finite
prime table supports any infinite claim. Model review is nonblind and
not human peer review or a mathematical certificate.
