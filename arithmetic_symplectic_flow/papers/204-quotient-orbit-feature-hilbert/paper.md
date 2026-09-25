# A fixed Hilbert observation space for the whole completed quotient flow

**Paper ID:** 204-quotient-orbit-feature-hilbert  
**Candidate ID:** AQC-20260916-QHK01  
**Research date:** 2026-09-16  
**Status:** ADVANCE — FIXED STATE-SEPARATING HILBERT GROUP ON THE WHOLE COMPLETED QUOTIENT; NONUNITARY AND NONCOMPACT; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The entire completed positive-cone quotient admits a single Hilbert
space of bounded continuous scalar functions, containing constants
and separating every finite and infinite state. Actual time pullback
is a strongly continuous group on that space, with norm at most
exp(abs(h)/2). The construction first obtains global deck-invariant
coordinates from a real-power mass gauge, then combines their full
time trajectories using a fixed exponentially weighted integral.
The coefficient map is not injective; its closed function kernel is
quotiented before any Hilbert norm is assigned to observations.
The resulting kernel is jointly continuous. Its changing diagonal
proves that this frozen norm does not make the flow unitary. Every
time-group operator is noncompact. Thus this is a fixed full-quotient
representation, not an ordinary trace-class realization, self-adjoint
spectral model or natural arithmetic-source theorem.

## 1. One geometric owner and one new analytic contract

The [version-1 card](candidate-card.md) precedes this proof. The
geometric dependency is the full proof of
[194](../194-rapid-decay-cone-completion/paper.md), specifically its
completed space, Hausdorff quotient, continuous complete flow, actual
global section and all-support orbit ledger. No analytic assertion
from 201 is imported.

The all-integer monoid algebra has e_m e_n=e_(mn). The square of
its nonunit ideal I is precisely the span of composite e_n, so the
declared quotient Q=I/I^2 has derived atom classes q_a at primes.
This algebraic source, not a supplied prime table, determines the
indices below. The [prior-work lineage](../../docs/prior_work/README.md)
is proper-factor symbolic admissibility -> indecomposable arithmetic
source -> full positive geometry -> actual-flow observation. There
is no asserted Logistic/Henon conjugacy or chronological sieve.

| Field | Exact owner | Scope |
| --- | --- | --- |
| Completed real space | E with norms sum_a a^k abs(v_a), all integers k>=0 | Every finite and rapidly decreasing infinite support |
| Carrier and topology | P_hat, its entire punctured nonnegative cone; X_hat=P_hat/<D> with original quotient topology | No new topology or support selection |
| Deck and physical time | Dv=(a v_a); phi_t[v]=[exp(t)v] | Real powers of D below are auxiliary coordinates, not replacement time |
| Section and clock | m(u)=1; F(u)=D^(-1)u/c(u), tau=-log c, c=sum_a u_a/a | Actual old return; no roof change |
| New analytic owner | Frozen orbit-feature image with the exact closed-kernel quotient norm | One fixed space, no spectral parameter s |
| Later analytic/geometric claims | No weighted-return determinant, Hamiltonian or quantum owner | No 201 operator or 196 geometry transfer |

The time-integration weight below is a probability measure on R,
not an invariant probability measure on X_hat. Observables will be
actual functions at every state, not equivalence classes modulo
unseen physical states. Arithmetic naturalness remains OPEN.

## 2. A global continuous deck gauge on all supports

Write (D^r v)_a=a^r v_a for real r. For abs(r)<=R,

\[
 \|D^r v\|_k\le \|v\|_{k+\lceil R\rceil}.
 \tag{1}
\]

This proves membership and uniform continuity in v on bounded
r-intervals. For a fixed v, truncate its summable weighted tail;
the finitely many retained coefficients vary continuously in r,
while (1) bounds the omitted difference by twice the corresponding
tail in norm k+ceil(R). Hence (r,v)->D^r v is jointly continuous
in every original norm. The same coordinate formulas give its
real group law and inverse. This is not boundedness in a lone norm.

**Proposition 1 (global gauge and quotient coordinates).** For every
v in P_hat there is a unique real theta(v) such that

\[
 m(D^{-\theta(v)}v)=1,
 \qquad w(v)=D^{-\theta(v)}v\in\widehat S.
 \tag{2}
\]

Both maps are continuous, theta(Dv)=theta(v)+1 and w(Dv)=w(v).
The resulting map from X_hat to S_hat times R/Z is a homeomorphism
of the existing topologies, not a new definition of the carrier.

**Proof.** The continuous function r->m(D^(-r)v) is strictly
decreasing: at least one positive coordinate strictly decreases and
all others weakly decrease. For r>=0 it is at most 2^(-r)m(v),
so tends to zero as r tends to positive infinity. At the other end,
any single positive coordinate tends to infinity. The intermediate
value property gives a unique solution of (2), for infinite as well
as finite support.

At v_0, the masses at theta(v_0)-epsilon and theta(v_0)+epsilon
strictly bracket one. Joint continuity preserves those inequalities
in a neighborhood of v_0. Monotonicity traps theta(v) between them,
proving continuity. Joint continuity of real powers proves continuity
of w. Uniqueness in (2) gives both deck identities.

The maps v->(w(v),theta(v)) and (u,r)->D^r u are continuous
inverses between P_hat and S_hat times R. In these coordinates D
acts as (u,r)->(u,r+1). Quotienting gives the asserted product
homeomorphism: the product of the identity with R->R/Z is an open
quotient map, so the equivariant homeomorphism induces both continuous
directions. QED.

This circle coordinate is a deck coordinate, not a claim that mixed
physical trajectories are circles. For real physical t the new theta
must still solve m(D^(-theta) exp(t)v)=1. On a singleton cq_a it
is log(c)/log(a), so physical time increments theta by t/log(a).
On mixed states the same mass equation remains in force, and the
old nonperiodic orbit ledger is unchanged.

For B={0,*} disjoint union the derived atoms define on X_hat

\[
 g_0=1,\qquad g_*([v])=e^{2\pi i\theta(v)},
 \qquad g_a([v])=w(v)_a .
 \tag{3}
\]

Every g_j is continuous and bounded in modulus by one. They are
genuine scalar functions on the quotient by the deck identities.
If every value agrees for [v] and [z], their w coordinates agree
and their theta coordinates differ by an integer. The inverse map
in Proposition 1 then gives z=D^n v, so the two quotient states
are equal. Thus (3) separates every state; no finite-support step
is used to discard infinite mixtures.

## 3. Hilbertization without false coefficient injection

Fix beta_0=beta_*=1/4, beta_a=2^(-a), and let
nu(dt)=rho(t)dt=(1/2)exp(-abs(t))dt. Then nu(R)=1 and

\[
 B_0:=\sum_{j\in B}\beta_j
 =\tfrac12+\sum_a2^{-a}\le 1.
 \tag{4}
\]

These representation weights are declared design inputs. Their
all-integer formulas use no per-prime choices or zero data. Define
the complex Hilbert space K=direct_sum_j L^2(R,nu), with inner
product linear in its first argument, and

\[
 Jb(x)=\sum_j\sqrt{\beta_j}
             \int b_j(t)g_j(\phi_t x)\,d\nu(t).
 \tag{5}
\]

**Proposition 2 (actual continuous function image).** Equation (5)
is absolutely defined for every b and x and obeys
norm(Jb)_infinity<=sqrt(B_0) norm(b)_K. Its evaluation vector is

\[
 (k_x)_j(t)=\sqrt{\beta_j}\,
                 \overline{g_j(\phi_t x)},
 \qquad Jb(x)=\langle b,k_x\rangle_K.
 \tag{6}
\]

The map x->k_x is norm continuous. In particular Jb belongs to
C_b(X_hat), in the original topology, for every coefficient vector.

**Proof.** Cauchy--Schwarz first in t and then in j gives

\[
 \sum_j\sqrt{\beta_j}\int |b_j(t)g_j(\phi_t x)|\,d\nu(t)
 \le\sum_j\sqrt{\beta_j}\|b_j\|_{L^2(\nu)}
 \le\sqrt{B_0}\|b\|_K .
 \tag{7}
\]

Thus neither exchanging the summation nor evaluation hides a
conditional series. Equation (6) is a vector of norm at most
sqrt(B_0). To check its continuity, first retain finitely many j,
bounding the squared omitted difference by 4 times the omitted
sum of beta_j. Then restrict time to [-T,T]; its omitted squared
contribution is at most 4 B_0 nu(abs(t)>T). For each retained j,
joint continuity of g_j(phi_t x) gives convergence uniformly in
this compact time interval as x tends to x_0, by a finite
neighborhood cover of the interval. The remaining finite integral
therefore tends to zero. These two arbitrary tails prove norm
continuity. Finally
abs(Jb(x)-Jb(y))<=norm(b)_K norm(k_x-k_y)_K. QED.

The map J is not injective: b_0(t)=t and all other components zero
give a nonzero L^2 vector but Jb=0 by oddness of t rho(t). Therefore
one cannot transport the K norm directly to the function image.
Use instead the exact closed subspace

\[
 N=\{b:Jb(x)=0\text{ for every }x\}
   =\bigcap_x \ker\langle\,\cdot\,,k_x\rangle,
 \qquad H=K/N\simeq N^\perp.
 \tag{8}
\]

Every coset has its unique orthogonal minimum-norm representative;
the Hilbert quotient is complete. Identify it with J(K) using this
norm. Two coefficients give the same actual function exactly when
their difference lies in N, so this identification is unambiguous.
Every k_x lies in N-perp. Consequently

\[
 \|f\|_\infty\le\sqrt{B_0}\|f\|_H,
 \quad
 \kappa(x,y)=Jk_y(x)
 =\sum_j\beta_j\int
           g_j(\phi_t x)\overline{g_j(\phi_t y)}\,d\nu(t)
 \tag{9}
\]

is the reproducing kernel; norm(ev_x)^2=kappa(x,x). It is
jointly continuous by (6). Positivity follows by expressing finite
quadratic forms as squared norms of finite sums of evaluation
vectors. The quotient norm does not imply C_b-closedness of H.

**Proposition 3 (constants, separation and infinite dimension).**
The fixed H contains 1, separates all points of X_hat and is
infinite dimensional.

**Proof.** Set b_0(t)=2 and all other components zero. Then Jb=1
and norm_H(1)<=2. For x different from y, choose j with
g_j(x) different from g_j(y). The continuous function
Delta(t)=g_j(phi_t x)-g_j(phi_t y) is nonzero on an interval
about zero. Take b_j(t)=overline(Delta(t)), other components zero.
It belongs to K since Delta is bounded and nu is finite, and

\[
 Jb(x)-Jb(y)=\sqrt{\beta_j}\int |\Delta(t)|^2\,d\nu(t)>0.
 \tag{10}
\]

For each atom a take instead b_a(t)=1/sqrt(beta_a), all other
components zero, and call its image f_a. On every singleton circle
C_b, w(phi_t x)=q_b for every t, so f_a restricted to C_b is
delta_ab. Thus every finite family of the f_a is linearly independent.
The derived atom set is infinite, so H is infinite dimensional. QED.

This proof does not assume that all original g_j belong to H;
the functions f_a are their time averages. Nor does a continuous
point-separating feature map prove that its Hilbert norm recovers
the entire all-weight topology. No such embedding theorem is claimed.

## 4. The actual flow on one fixed Hilbert space

For h in R let R_h f(x)=f(phi_h x). A change of integration
variable in the absolutely convergent (5) gives

\[
 R_h Jb=J U_h b,\qquad
 (U_h b)_j(t)=\frac{\rho(t-h)}{\rho(t)}b_j(t-h).
 \tag{11}
\]

The ratio, not bare translation in weighted L^2, is essential.
For r=t-h,

\[
 \|U_h b\|_K^2
 =\sum_j\int |b_j(r)|^2\frac{\rho(r)^2}{\rho(r+h)}\,dr
 \le e^{|h|}\|b\|_K^2.
 \tag{12}
\]

The inequality follows from abs(r+h)-abs(r)<=abs(h).
The ratios telescope, giving U_h U_l=U_(h+l) and inverse U_(-h).

**Theorem 4 (fixed full-quotient C0 group).** Actual time pullback
preserves H and defines a strongly continuous group with

\[
 \|R_h\|_{H\to H}\le e^{|h|/2},\qquad R_h^{-1}=R_{-h}.
 \tag{13}
\]

**Proof.** If b lies in N, (11) vanishes at every x because Jb
vanishes at every phi_h x. Hence U_h N is contained in N; using
-h gives equality. The coefficient group therefore induces precisely
the claimed actual-function action on K/N, with bound (13) by
taking the infimum over representatives. Its inverse and group law
are induced as well, not imposed on an unrelated representation.

For strong continuity on K, use vectors with finitely many components,
each a continuous compactly supported function of time. They are dense:
truncate component and time tails, then use the ordinary local L^2
approximation, since rho is positive continuous and bounded above
and below on any compact interval. For these vectors U_h b tends
to b as h tends to zero. Indeed the translated functions converge
uniformly on a common compact support and rho(t-h)/rho(t) tends
uniformly to one, bounded between exp(-abs(h)) and exp(abs(h)).
The uniform bound in (12) for abs(h)<=1 extends this convergence
to every b by density. Finally the quotient norm bounds the difference
of its cosets by norm_K(U_h b-b). This proves strong continuity
on H at zero, and the group law gives it at every time. QED.

The physical H and its norm do not depend on s. All scalar
observations descend to the true quotient; both time directions and
every finite/infinite state are retained. In the sup norm, pullback
is an isometry because phi_h is bijective. This does not say that
it is an isometry in the different Hilbert norm.

## 5. Two decisive costs: nonunitarity and no ordinary time trace

The kernel diagonal is

\[
 \kappa(x,x)=\tfrac12+
    \sum_a\beta_a\int w_a(\phi_t x)^2\,d\nu(t).
 \tag{14}
\]

Consider the retained mixed state x=[q_2+q_3]. If
r_h=theta(exp(h)(q_2+q_3)), its equation is
2^(-r_h)+3^(-r_h)=exp(-h). Thus r_h tends to positive infinity
as h tends to positive infinity and to negative infinity at the
other end. The ratio w_3/w_2=(3/2)^(-r_h) proves
w(phi_h x)->q_2 at the positive end and ->q_3 at the negative end.
For every fixed t the same limits hold at h+t. Since the weights
are bounded and nu is a probability measure, a compact-time/tail
argument in (14) gives

\[
 \lim_{h\to+\infty}\kappa(\phi_hx,\phi_hx)=\tfrac34,
 \qquad
 \lim_{h\to-\infty}\kappa(\phi_hx,\phi_hx)=\tfrac58.
 \tag{15}
\]

If every R_h were unitary, the relation ev_(phi_h x)=ev_x R_h
would preserve the norm of evaluation, and (14) would be constant
along this orbit. Equation (15) refutes that assertion. The frozen
representation is therefore genuinely nonunitary, not just missing
a proof of unitarity. This argument does not rule out other classes
of Hilbert representation or claim any quantum interpretation.

Every R_h, including h=0, is invertible on the infinite-dimensional
H. It cannot be compact: otherwise R_(-h)R_h would make the
identity compact, whereas an orthonormal sequence in H has no
convergent subsequence. In particular none of these group operators
is ordinary Hilbert trace class. This is not a statement about every
smoothed operator, resolvent, distributional trace or Fredholm status
of I-R_h. None of those different obligations has been frozen here.

## 6. Controls and arithmetic limits

1. **Cover versus quotient.** Equations (2)--(3) prove full deck
   invariance before feature construction; raw powers of a cover
   coordinate are not substituted for these scalar observables.
2. **Function kernel versus coefficient labels.** The explicit b_0=t
   control makes N nonzero. Equation (8), not an asserted injection,
   gives the correct norm and removes only duplicate descriptions
   of a function, never physical states.
3. **Time weight versus invariant state measure.** nu lives on R.
   No physical state is identified with another almost everywhere;
   (10) separates any two actual states, including mixed ones.
4. **No hidden clock change.** The auxiliary D^r coordinate has
   period one modulo deck translation. It is not physical time;
   on prime axes physical time remains log(a) per circle. Mixed
   periods are still tested by exp(t)v=D^n v and remain absent.
5. **PROVES_TOO_MUCH.** For any jointly continuous flow equipped
   with a countable continuous point-separating family uniformly
   bounded in modulus by one (rescale each bounded feature if needed),
   the summable-feature and exponential-time construction above
   works by the same proof (include 1 to obtain constants). This
   legitimate representation theorem does not select prime arithmetic.
   The special work here supplies that family on the entire frozen
   quotient, rather than assuming it on an external carrier.
6. **Representation choices.** beta and rho are engineered, fixed
   in advance and unrelated to a fitted spectrum. Their success
   does not prove source-clock or observable-norm naturalness.
   Changing their values later would require a newly frozen contract.
7. **Analytic owner separation.** The 201 operator is a weighted
   first-return action on a different family of physical function
   spaces. This paper supplies actual fixed-time pullback on X_hat.
   Their common geometric ancestor does not transfer a determinant
   or prove weighted-return invariance on this H.

Algebra closure, equality with C_b, topology recovery, spectral
classification and any self-adjoint generator are NOT CLAIMED.
There is no numerical cutoff, simulation or prime-data input in
the proof. Finite truncations justify infinite estimates and density;
they are not numerical evidence for global assertions.

## 7. Decision and gate boundaries

| Obligation | Result | Disposition |
| --- | --- | --- |
| Original completed geometry and source lineage | Retained exactly, with new global coordinate proof | Same-object ledger intact; naturalness OPEN |
| Full scalar quotient observation | Continuous point-separating family and legitimate Hilbert image, constants included | ESTABLISHED on all states |
| Fixed physical time action | Actual C0 bounded group on one H, norm bound (13) | ADVANCE this precise representation contract |
| Unitary norm and ordinary time-group trace | Kernel-diagonal mismatch and invertible infinite-dimensional action | FAIL in the specified norm / no ordinary trace class |
| Weighted first-return determinant | Not constructed on this H | NOT EVALUATED; no 201 transfer |
| Classical A0--A2 / formal Route / B | No classical carrier or formal protocol evaluated | NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

Advance the fixed scalar Hilbert representation and stop this card
at that theorem. Its genuine gain is the entire quotient, a single
space, actual continuous-time action, constants and full state
separation together. Its costs are a designed quotient-feature norm,
nonunitarity and noncompact time operators. No natural A0 or formal
Route passage follows. New trace, regularity or spectral proposals
need fresh cards rather than stronger names for this result.

The [claim ledger](claim-ledger.md) and
[evidence index](evidence/README.md) distinguish the proof, source
reading, actual nonblind model review and mechanical verification.
The existence of any of these documents is not itself a proof or
human peer-review certificate.
