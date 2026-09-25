# Cross-sector source feedback: a complete flow and a mixed bound packet

**Paper ID:** `236-cross-sector-frontier`  
**Scope ID:** `ASFS-SCOUT-20260918-CSF01`  
**Audited candidate:** `ANG-20260918-SDT01`  
**Date / evidence:** 2026-09-18; exact construction and scoped negative theorem.  
**Status:** `T0 ESTABLISHED; MIXED-PRIME PERIODIC PACKET — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

The frozen self-catalytic divisor-transfer flow replaces the two-occupied-factor
source of the preceding multiplicative models by a quartic coupling that lets
one occupied composite mode excite its proper divisors. We prove a complete
two-sided mild action on the entire unit sphere of complex ell squared, with
no finite-energy restriction or phase quotient. The state e6 immediately
excites modes 2 and 3, so the old powers-of-6 sector is genuinely broken.
Nevertheless, the entire divisor-closed subspace spanned by e2, e3 and e6 is
invariant under the full equation. A compact constrained-energy maximum there
produces an actual mixed-prime primitive point orbit with a proved least
physical period. Thus sector leakage is established but prime-exclusive
returns fail. Naturalness and the remaining periodic ledger stay OPEN; no
trace, determinant, classical symplectic suspension or quantum owner is added.

## 1. Question, provenance and same-object contract

The [scope and exact SDT01 short card](candidate-card.md) were frozen before
this mathematical audit. The question is whether a source can break the
mixed-prime power sectors of [233](../233-multiplicative-resonant-flow/README.md)
and [234](../234-multiplicative-sector-obstruction/README.md), without merely
changing coefficients or diagonal dispersion, and avoid mixed closed packets.
The [235 dispersion fork](../235-quadratic-dispersion-flow/README.md) is a
separate stopped owner, not a source of inherited theorems.

The [prime-symbolic lineage](../../docs/prior_work/README.md) is the explicit
replacement of the proper-divisor incidence a|n by coherent transfer from
occupied n to a and its Hamiltonian back reaction. No conjugacy with a sieve,
Logistic map or Henon map is asserted. Coefficients (ab)^(-2), unit charge and
dispersion log n are declared all-integer designs. No prime list, prime-specific
parameter, von Mangoldt weight, fitted zero data or suspension roof is supplied.

| Owner row | Exact SDT01 object | Evidence boundary |
| --- | --- | --- |
| Carrier | Entire M={z in ell squared(n>=2;C):Q(z)=1}, Q=sum abs(z_n)^2 | Norm topology; no states discarded |
| Action | Mild equation (1), with the frozen diagonal L and quartic V | Full two-sided action proved below |
| Arithmetic source | Every ordered pair (a,b), a,b>=2, with product ab | Proper-divisor transfer; naturalness OPEN |
| Clock and packets | Actual parameter t; nonconstant point orbits modulo time translation only | Least return T and traversals rT |
| Classical base / roof | NOT APPLICABLE | No finite-dimensional symplectic map or mapping torus |
| Analytic / later owner | NOT SUPPLIED | No zeta, determinant, trace or quantum realization |

The ambient form i sum dz_n wedge d(bar z_n) is not declared symplectic after
restriction to M. The formal Hamiltonian has quadratic part finite only on
{sum log n |z_n| squared<infinity}; this domain does not replace M. The scoped
T0 result below concerns the actual mild action, not a globally finite-valued
Hamiltonian or a strong solution at every state.

The different linear proposal [UDC01](../237-unary-divisor-coherence/candidate-card.md)
has a separate card and owner. This proof neither uses nor establishes its
results. Nearest structural controls are the real fragmentation cotangent
lane in [192](../192-six-architecture-source-frontier/README.md), the diagonal
character action in [186](../186-multiplicative-bar-clock/README.md), and the
prior quotient in [193](../193-indecomposable-radial-quotient/README.md).
None is identified with SDT01. No general novelty claim is made.

## 2. The full quartic gradient

Write E=ell squared({n>=2};C), with inner product
<u,v>=sum bar u_n v_n. Let Lz=(log n)z_n on
D(L)={sum (log n)^2 |z_n|^2<infinity}; S_tz=n^(-it)z_n. The action is

\[
 z(t)=S_tz_0-i\int_0^tS_{t-s}G(z(s))\,ds,
 \qquad G=\partial_{\bar z}V,
 \quad V(z)=\operatorname{Re}\sum_{a,b\ge2}
 \frac{\bar z_a z_{ab}|z_{ab}|^2}{(ab)^2}.
 \tag{1}
\]

The derivative convention is dV(z)[h]=2 Re<h,G(z)>; derivatives here are
real Frechet derivatives. Put C=sum_(a,b>=2)(ab)^(-2)<infinity. Its finiteness
follows, for example, from sum_(n>=2)n^(-2)<=integral_1^infinity x^(-2)dx.
On ||z||<=R, each summand of V is bounded by (ab)^(-2)R^4. Its first and
second derivatives have operator norms at most 4(ab)^(-2)R^3 and
12(ab)^(-2)R^2: differentiate the four coordinate or conjugate-coordinate
factors, each of norm at most one as a real-linear functional.

The sums and derivatives therefore converge uniformly on every bounded ball.
In particular V is real C2, its gradient is C1, and

\[
 |V(z)|\le C\|z\|^4,\qquad
 \|G(z)\|\le2C\|z\|^3,\qquad
 \|G(z)-G(w)\|\le6CR^2\|z-w\|
 \quad(\|z\|,\|w\|\le R).
 \tag{2}
\]

For c=ab, one summand is
(2c^2)^(-1)(bar z_a z_c^2 bar z_c+z_a bar z_c^2 z_c).
Since a<c, differentiation in the factor coordinate and in the product
coordinate are distinct contributions. Summing them gives the full formula

\[
 G_n(z)=\frac12\sum_{b\ge2}\frac{z_{nb}|z_{nb}|^2}{(nb)^2}
 +\frac1{2n^2}\sum_{\substack{a,b\ge2\\ab=n}}
       \bigl(\bar z_a z_n^2+2z_a|z_n|^2\bigr).
 \tag{3}
\]

The sum in (1) is ordered, including a=b once. Formula (3) uses that same
convention, with no extra factor for a=b. The first sum converges absolutely;
it is also the coordinate of the Hilbert gradient justified by (2).

The quartic is invariant under uniform phase rotation and homogeneous of
real degree four. Differentiating these two identities gives

\[
 G(e^{i\theta}z)=e^{i\theta}G(z),\qquad
 \operatorname{Im}\langle z,G(z)\rangle=0,\qquad
 \langle z,G(z)\rangle=2V(z).
 \tag{4}
\]

The last equality combines the real Euler identity with the preceding zero
imaginary part. No phase rotation has been quotiented out of the carrier.

## 3. T0: complete action on the entire norm shell

**Theorem 1.** Equation (1) has a unique global mild solution for every z0 in
E, conserves Q, and defines a jointly continuous two-sided action on E and
on M. No finite-energy hypothesis is required.

**Proof.** The operators S_t are unitary, form a group, and are strongly
continuous. Strong continuity follows by dominated convergence in the series
sum |n^(-it)-1|^2|z_n|^2. Set w(t)=S_(-t)z(t). Equation (1) is equivalent to

\[
 w'(t)=-iS_{-t}G(S_tw(t)),\qquad w(0)=z_0.
 \tag{5}
\]

The vector field is jointly continuous in (t,w), locally Lipschitz in w
uniformly in t on bounded balls, and bounded there, by strong continuity and
(2). Picard iteration on continuous E-valued curves thus gives a unique local
C1 solution w. For example on a fixed radius-R ball the Lipschitz bound is
6CR^2 and the size bound is 2CR^3, so the usual integral map is a contraction
on a sufficiently short interval depending only on R and the initial radius.
This argument works forward or backward from any initial time.

Since w is C1, charge may be differentiated in (5) without differentiating
Lz for a general mild datum:

\[
 \frac d{dt}\|w(t)\|^2
 =2\operatorname{Re}\langle w,-iS_{-t}G(S_tw)\rangle
 =2\operatorname{Im}\langle S_tw,G(S_tw)\rangle=0.
 \tag{6}
\]

Unitarity gives Q(z(t))=Q(w(t))=Q(z0). Thus w stays on a bounded ball, where
the local existence interval is uniform in its start time. A finite endpoint
cannot obstruct extension in either direction, giving the global solution.
The contraction estimate, or its integral Gronwall inequality, gives continuous
dependence uniformly on compact time intervals. Together with strong
continuity of S_t this proves joint continuity of z(t,z0).

The original mild equation is autonomous: its integral identity, split at any
time s and combined with S_(t+s)=S_t S_s, shows that a shifted solution is the
solution starting from z(s). Uniqueness gives Phi_(t+s)=Phi_t Phi_s and
Phi_0=id; in particular Phi_(-t) is the inverse of Phi_t. This proves the
claimed action. The transformation groupoid has objects M and arrows (z,t)
from z to Phi_t(z), all owned by this action. QED.

Only w in (5) has been claimed C1 for every initial datum. In particular this
proof does not assert z(t) is a strong solution on all E, does not invoke a
finite Hamiltonian at every z, and does not require a Galerkin limit. The
finite-dimensional invariant states used next are strong solutions of the
original equation and lie in D(L).

## 4. Genuine leakage and the surviving complete probe

At the unit coordinate vector e6, (3) gives

\[
 G_2(e_6)=G_3(e_6)=\frac1{72},\qquad
 G_n(e_6)=0\quad(n\notin\{2,3\}).
 \tag{7}
\]

The mild solution has derivative at t=0 because e6 is in D(L): divide (1)
minus z0 by t and use strong continuity and continuity of G. Hence
dot z2(0)=dot z3(0)=-i/72. In particular the complete powers-of-6 subspace
{z:z_n=0 unless n=6^k,k>=1} is not invariant. This is actual source feedback,
not a relabeling of modes or a diagonal change.

Now let D=span_C{e2,e3,e6}. For z in D, the first term of G_n can be nonzero
only when nb=6, yielding n=2 or 3. The second term contains z_n or |z_n|^2
and vanishes outside D. Thus G(D) is contained in D; S_t also preserves D.
Picard iteration inside D and uniqueness from Theorem 1 show that its solution
is exactly the full E solution for every datum in D. Therefore the entire D
is invariant for all real time. This is not a projected ODE substituted for
the original system. The restriction is finite dimensional and hence gives
global strong solutions; every point of D remains in the main carrier when
its charge is one.

On D the actual Hamiltonian and quartic reduce exactly to

\[
 A(z)=(\log2)|z_2|^2+(\log3)|z_3|^2+(\log6)|z_6|^2,
 \quad H_D(z)=A(z)+V_D(z),
\]
\[
 V_D(z)=\frac1{36}\operatorname{Re}
       \bigl((\bar z_2+\bar z_3)z_6|z_6|^2\bigr).
 \tag{8}
\]

There are just two surviving ordered factor pairs, (2,3) and (3,2).

## 5. T2 stop: an intrinsic mixed-prime primitive

**Theorem 2.** The full SDT01 flow on M has a nonconstant primitive point
orbit with nonzero 6-coordinate. If v maximizes H_D on D intersect M, and
m=H_D(v), then

\[
 \Phi_t(v)=e^{-i\lambda t}v,\qquad
 \lambda=2m-A(v)\ge\log6>0,\qquad
 T=\frac{2\pi}{\lambda},\quad T_r=rT.
 \tag{9}
\]

**Proof.** The unit sphere of D is compact and H_D is continuous, so a
maximizer v exists. Since H_D(e6)=log6, m>=log6. If v6=0, (8) would give
V_D(v)=0 and H_D(v)<=log3, a contradiction. Thus v6 is nonzero.

The real Lagrange-multiplier rule on this sphere gives a real lambda with
Lv+G(v)=lambda v: dH_D[h]=2 Re<h,Lv+G(v)> and dQ[h]=2 Re<h,v>.
There are no missing normal coordinates, because Lv and G(v) belong to D.
The restricted gradient equation is therefore the full coordinate equation
in E. Pairing it with v and using (4) yields

\[
 \lambda=A(v)+2V_D(v)=2m-A(v).
 \tag{10}
\]

On the unit sphere A(v)<=log6, so lambda>=log6>0. By the phase equivariance
in (4), z(t)=e^(-i lambda t)v satisfies i dot z=Lz+G(z) in every coordinate
and hence is the full mild solution by uniqueness. It is nonconstant. A
return to v occurs exactly when e^(-i lambda t)=1, as v6 is nonzero; the
least positive physical return is therefore 2pi/lambda, and traversing the
same point orbit r times has time rT. QED.

The precommitted arithmetic interpretation requires each prime packet's
support to lie in {p^k:k>=1} for a single prime p. A nonzero 6-coordinate
violates it regardless of the other two coordinates, because 6 has the
distinct prime factors 2 and 3. Theorem 2 is therefore a same-object
mixed-prime periodic packet, not a repetition manufactured from labels.
No uniqueness or count of maximizing orbits is asserted, and all such
states are retained rather than choosing one as a representative quotient.

## 6. Controls, limitations and decision

The zero-interaction control, a different flow, has every integer pure mode
rotating with least period 2pi/log n. In SDT01 itself, a pure-prime state
c e_p with |c|=1 has G(c e_p)=0 by (3), so its actual period remains
2pi/log p. Here log p is a frequency, not a derived period log p. This
separate clock observation supplies no rescue or transferred result.

The e6 test establishes the intended positive source change. The invariant
divisor probe and Theorem 2 are its adverse control: breaking an infinite
power sector is not sufficient to exclude mixed bound packets. The latter
failure is not inferred from a numerical cutoff; the probe is proved
invariant in the complete owner. No coefficient tuning, extra phase quotient,
composite-mode deletion or change of physical time is made.

| Gate | Exact SDT01 evidence | Status / boundary |
| --- | --- | --- |
| T0 | Theorem 1, full norm shell and transformation groupoid | ESTABLISHED at action level; not classical symplectic suspension |
| T1 | Explicit proper-divisor transfer and physical time | Source leakage established; source/scale naturalness OPEN |
| T2 | Theorem 2 with least period and repetitions | Prime-exclusive target scoped FAIL; complete periodic classification OPEN |
| T3 | None supplied | NOT SUPPLIED / NOT EVALUATED |
| Classical A0 / A1 / A2 | No classical base or suspension claimed | NOT APPLICABLE |
| Formal Route / B | No formal evaluation | UNASSIGNED / NOT INVOKED |

**Portfolio decision: stop / fork.** The decisive reason is an intrinsic
mixed-prime primitive in the unchanged full action. The useful new layer is
the whole-space conservative nonlinear source and its actual sector leakage;
the remaining obstruction lives in a different invariant support. A future
fork needs its own card and a mechanism addressing mixed-source closed
packets, not merely the previous power-sector invariance. This paper does
not rule out all nonlinear arithmetic dynamics and does not promote negative
records into accumulated Route credit.

## 7. Separate linear lane and portfolio boundary

The independently frozen [UDC01 candidate in 237](../237-unary-divisor-coherence/paper.md)
uses a bounded symmetric linear divisor-incidence matrix on the full ordinary
norm shell. Its own proof establishes global action and actual leakage from
the powers-of-6 support, but an attained lowest-energy state is positive at
every integer coordinate. That state yields a nonconstant periodic orbit
in its unchanged physical flow. Its conclusion is also STOP / FORK; it is
not a theorem about SDT01 and is not an ingredient in the proofs above.

The two lanes expose different replacement obstructions. SDT01 retains a
finite divisor-closed invariant probe; UDC01 has a full-support standing wave
despite its connected transfer graph. Thus an eventual new card must address
the mechanism producing mixed-source bound packets, not just demonstrate
escape from the old power sector. Neither deleting unwanted modes nor taking
a global-phase quotient is a same-candidate repair. No general impossibility
theorem or pooled Route credit is inferred from these two scoped stops.

## Reproducibility and research-integrity record

The [candidate card](candidate-card.md), [claim ledger](claim-ledger.md) and
[evidence index](evidence/README.md) identify every input, proof dependency
and boundary. All substantive results are proved above. There is no numerical
run, cutoff, precision parameter, downloaded dataset or external citation
needed for these self-contained derivations. The selected local comparisons
are architectural context, not theorem dependencies or a systematic novelty
search.

This is an AI-assisted internal mathematical research record, not external
peer review or a submission-readiness claim. ARS is used to keep definitions,
proof dependencies and adverse evidence separate; no venue-specific criteria
binding is supplied (`criteria_binding_unavailable`). Root retains portfolio
integration; the bounded author derives and drafts the SDT01 proof. Independent
review is recorded only after its actual execution, never inferred from this
paper's existence. Data availability: all mathematical inputs and derivations
are in this package. Ethics: no human-subject data or external disclosure is
involved. Human authorship, conflicts and funding were not supplied; none are
invented or certified absent.
