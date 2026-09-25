# Round-volume clocks on four complete projective three-space owners

**Paper ID:** 393-projective-dimension-control.  
**Candidate:** ANG-CONTROL-20260922-PDC01; batch NONUNIT-RETURN-20260922-I, round 4/5.  
**Date:** 2026-09-22. Classification: EXTERNAL CONTROL, not a lineage-admitted main candidate.  
Outcome: `EXTERNAL DIMENSION CONTROL ESTABLISHED; MAIN-CANDIDATE ADMISSION STOP`
**Route:** classical A0/A1/A2 NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED; T3 NOT AUDITED.

## Abstract

The round-volume Jacobian of a projective map induced by an invertible real four-by-four matrix is derived on the entire real projective three-space, including every Borel transport set. Four separately frozen matrices give complete retained-lag clock owners. The MAIN matrix has two irrational eigenlines with least positive physical time log 2, but also a complementary projective line of distinct packets with that time and a continuum of two-cycle packets with least time log 4. Its remaining points are nonperiodic. The three controls expose scalar cancellation, continuous complementary packets and the distinction between finite projective map order and unreduced lag isotropy. Rational positive multipliers here do not contradict a one-dimensional rational-projective restriction. Assigned coefficients and absent prime-symbolic feedback keep every result external; no minimum-dimension or main-candidate claim follows.

## 1. Exact owners, source exposure and scope

The sole scientific input is the full 74-line [candidate card](candidate-card.md), SHA-256 `42b57df25ae79aa9deb72de31997f96497361b0db4a24e43c733485f97cf9ecc`, read before root's CP1 release. No other new paper, raw derivation or reviewer evidence is used. The projective carrier and volume below are independently constructed for EACH row, not transported between controls.

| Owner | Frozen matrix on R4 | Carrier and metric |
| --- | --- | --- |
| MAIN | A=diag(B,I2), B=((0,2),(1,0)) | Full RP3, standard round metric and volume m |
| S | A=2I4 | Its own full RP3 and round m |
| D | A=diag(2,1,1,1) | Its own full RP3 and round m |
| B-control | A=diag(B2,B2), B2=((0,2),(1,0)) | Its own full RP3 and round m |

For every row, F_A([v])=[Av] and the actual forward return named in the card is T=F_A^(-1). The frozen arrow convention is nevertheless `(F_A^k(w),k,w)` for every integer k. All powers, inverse powers and integer labels remain, even when projective maps agree. A physical multiplier means exp(L), where L is the least positive generator of the ENTIRE physical stabilizer. Signed one-step logarithmic clocks are not called positive primitive times; the volume Jacobians themselves are positive.

The coefficient 2 is assigned. No symbolic coding, admission feedback, endogenous prime mechanism, symplectic form, positive roof, quotient manifold, invariant suspension measure, operator or analytic trace owner is supplied. The question is only whether the dimensional boundary of a one-dimensional argument needs to remain explicit.

## 2. Entire round-volume IMAGE law from polar volume

Let A be any invertible real four-by-four matrix and define f_A(u)=Au/||Au|| on S3. This is a smooth antipodal-equivariant diffeomorphism. Write sigma for round sphere volume. For every nonnegative Borel function h on S3, Euclidean change of variables y=Ax gives
\[
\int_{\mathbb R^4}h(Ax/\|Ax\|)1_{\{0<\|Ax\|\leq1\}}\,dx
=\frac1{4|\det A|}\int_{S^3}h(\theta)\,d\sigma(\theta).
\]
Polar coordinates x=ru give the same left side as
\[
\frac14\int_{S^3}h(f_Au)\|Au\|^{-4}\,d\sigma(u).
\]
Taking h to be the indicator of f_A(E), for any Borel E on S3, therefore proves
\[
\sigma(f_AE)=\int_E\frac{|\det A|}{\|Au\|^4}\,d\sigma(u).
\tag{1}
\]
There is no selected hemisphere in this identity. The quotient q:S3->RP3 is a two-sheeted local isometry, and its round volume is m(E)=sigma(q^(-1)E)/2. The integrand in (1) is antipodal-invariant. Consequently, for EVERY Borel E in RP3,
\[
m(F_AE)=\int_EJ_A\,dm,\qquad
J_A([v])=|\det A|\frac{\|v\|^4}{\|Av\|^4}.
\tag{2}
\]
This is the full IMAGE law, not merely a cylinder or selected-chart test. It applies in every Borel transport chart, including sets meeting coordinate hyperplanes; F_A is globally one-to-one. Its smooth density is the everywhere pointwise Riemannian volume Jacobian: the usual smooth change-of-variables density agrees almost everywhere by (2), and continuity plus full support of round volume upgrades equality to every point.

Multiplying v by any nonzero scalar leaves (2) unchanged. Replacing A by tA also leaves it unchanged, since |det(tA)|=|t|^4|det A|. For arbitrary invertible A,C, cancellation of the intermediate norm gives
\[
J_{AC}([v])=J_A([Cv])J_C([v]).
\tag{3}
\]
Thus the formula is intrinsic to the projective map and composes exactly, independent of its matrix scalar representative. It applies to every integer power, including negative ones.

## 3. Full groupoid, clock kernels and all height phases

For each owner separately set delta=|det A|. The clock of its full action groupoid is
\[
c_A(F_A^kw,k,w)=4\log\frac{\|A^kv\|}{\|v\|}-k\log\delta,
\qquad w=[v],\quad k\in\mathbb Z.
\tag{4}
\]
Equation (3) proves cocycle additivity under arrow composition and sign reversal under inversion. The extension has every object (w,h) in RP3 times R and arrows `(w,h)->(F_A^kw,h+c_A(k,w))`. Translation by any real number commutes with every arrow; no positive-step or quotient-regularity hypothesis is needed.

The lag kernel is ONLY the unit arrows k=0, even if F_A has finite order. The clock kernel is exactly
\[
\ker c_A=\{(F_A^kw,k,w):\|A^kv\|^2=\delta^{k/2}\|v\|^2\}.
\tag{5}
\]
Their intersection is the unit groupoid. The formulas for each matrix below explicitly describe all of (5), not just its isotropy restriction.

If w has least source period d, then its source isotropy is dZ. Put ell=c_A(d,w). By the cocycle law all its isotropy clocks are n ell; hence
\[
H_w=\ell\mathbb Z,\qquad
\operatorname{Iso}_{\rm ext}(w,h)=\{nd:n\ell=0\}.
\tag{6}
\]
At a nonperiodic point both isotropy groups are trivial and H={0}. These conclusions are independent of h. Because the base is invertible, every legal incoming point already belongs to that same two-sided source orbit: no additional transient histories can be appended to a periodic orbit.

For a complete source orbit, fix one reference point. Connecting arrows identify every other base point's heights with reference heights modulo exactly H, so its extension orbit set is R/H, with real translation. Thus it gives ONE physical orbit, not one per source phase. If ell is nonzero, its least positive time is L=|ell| and its positive repetitions are rL. If ell=0, H={0}, the physical orbit is R and has no positive period, even when extension isotropy is infinite. Distinct source orbits remain distinct packets even when their times coincide.

Traversing the actual T return reverses the lag: at a d-periodic point c_A(-d,w)=-ell, with the same H and least positive L. None of the following positive physical periods asserts that the T one-step clock is a positive roof on the whole carrier.

## 4. MAIN: all periodic and nonperiodic projective points

Write v=(u,w) with u=(x1,x2), w=(x3,x4), and U={w=0}, W={u=0}. Here delta=2 and A^2=diag(2I2,I2). On P(W), F_A is the identity. On P(U), its square is the identity, and its only fixed points are
\[
e_+=[\sqrt2:1:0:0],\qquad e_-=[-\sqrt2:1:0:0].
\tag{7}
\]
They are irrational projective lines, since their first/second coordinate ratios are not rational. Every other point of P(U) has least period 2.

There are NO periodic points with both u and w nonzero. Indeed, if F_A^k[v]=[v] for nonzero k, squaring the equation gives a scalar equality `(2^k u,w)=r(u,w)`. The nonzero w forces r=1, while nonzero u forces 2^k=1, impossible. This also excludes all unlisted higher periods. The entire periodic set is precisely P(U) disjoint union P(W), with every mixed point nonperiodic.

At e_+ and e_-, the norm ratio for A^k is 2^(k/2). Equation (4) gives c_A(k)=k log 2. Hence each has source isotropy Z, trivial extension isotropy, H=(log 2)Z and positive primitive multiplier 2. There are TWO such source packets, not one eigenvalue-selected packet.

At EVERY point of P(W), the norm ratio is 1, so c_A(k)=-k log 2. Source isotropy is Z, extension isotropy is trivial and H=(log 2)Z again. Each point of this entire RP1 is a separate packet of least positive time log 2; reversing the clock orientation does not remove it. Thus the total log-2 packet set is `{e_+,e_-}` disjoint union P(W), a continuum, not two packets.

For x in P(U) other than e_+,e_-, source isotropy is 2Z. At lag 2n, A^(2n)v=2^n v, so c_A(2n)=2n log 2. Extension isotropy is trivial and H=(2 log 2)Z. Its positive primitive time is log 4 and multiplier 4. Each two-point source orbit contributes one packet containing both phases. The quotient `(P(U) minus {e_+,e_-})/<F_A>` is a continuum of such distinct packets. Repeating one packet r times gives r log 4, not a merger with another packet.

Every mixed point has trivial source and extension isotropy, H={0} and a nonperiodic physical R orbit. All its positive and negative iterates remain. There are continuum many such source orbits: each is countable, the carrier has continuum cardinality, and already the invariant direction [w] ranges over a continuum. These are not positive primitive packets.

For the COMPLETE clock kernel, put a=x1^2, b=x2^2 and t=x3^2+x4^2. For k=2n with n nonzero, (5) is exactly
\[
t=2^n(a+b).
\tag{8}
\]
For every odd k=2n+1, with n any integer, it is exactly
\[
(2^{2n}-2^{n+1/2})a
+(2^{2n+2}-2^{n+1/2})b
+(1-2^{n+1/2})t=0.
\tag{9}
\]
These follow from the actual norm squares of A^(2n)v and A^(2n+1)v. Together with all unit arrows, they describe every kernel arrow. In particular nonzero-lag zero-clock arrows can join nonperiodic points; they are not isotropy merely because their clock vanishes. The lag kernel and its intersection with (8)--(9) remain just units.

## 5. S control: scalar projective identity with retained integer lags

For S, delta=16 and A^k=2^k I4. Formula (2) gives J_(A^k)=1 EVERYWHERE for every k, and c_S=0. Every projective point is fixed; the source orbits are the individual points of RP3, a continuum. The source isotropy is Z at each point, not a trivial group obtained by identifying equal maps. Extension isotropy is also Z at every height.

The clock kernel is the entire retained-lag groupoid; the lag kernel and their intersection are units. Every H is {0}. Each point contributes a physical R, so there are no positive primitive times, multipliers or repetitions of a positive-time packet. This owner tests why a nonunit matrix scalar cannot itself supply physical time.

## 6. D control: full complementary projective plane retained

For D write a=x1^2 and b=x2^2+x3^2+x4^2. Now delta=2 and ||A^kv||^2=4^k a+b. The entire fixed set consists of the axis point e=[1:0:0:0] and its complementary RP2={x1=0}. Every point with a,b positive is nonperiodic: F_A^k[v]=[v] would require both scalar factors 2^k and 1 to agree. No other finite periods occur.

At e, c_D(k)=3k log 2, so source isotropy is Z, extension isotropy is trivial and H=(3 log 2)Z. It gives ONE packet with least positive time log 8 and multiplier 8. At every point of the whole complementary RP2, c_D(k)=-k log 2, so the same isotropy conclusions hold but H=(log 2)Z. This is a continuum of separate log-2 packets. All real phases and positive repetitions r log 8 or r log 2 are retained for their respective packets.

All remaining points have trivial source/extension isotropy and H={0}, with physical R orbits. There are continuum many source orbits, for instance because the complementary direction [x2:x3:x4] is invariant and arbitrary. The complete clock is
\[
c_D(k,[v])=2\log\frac{4^ka+b}{a+b}-k\log2.
\]
For k nonzero put s=2^(k/2)>0. Equation (5) factors as `(s-1)(s(s^2+s+1)a-b)=0`. Thus its full clock kernel comprises all units and exactly the arrows with
\[
b=s(s^2+s+1)a,\qquad k\ne0.
\tag{10}
\]
All these nonunit kernel sources are nonperiodic. Lag kernel and kernel intersection are units. No complementary plane or nonperiodic point was discarded to isolate the axis packet.

## 7. B control: finite projective order without collapsing the lag groupoid

For this separate matrix delta=4, A^2=2I4 and F_A^2 is globally the identity. Its eigenspaces are
\[
E_+=\{(\sqrt2 y_1,y_1,\sqrt2 y_2,y_2)\},\quad
E_-=\{(-\sqrt2 y_1,y_1,-\sqrt2 y_2,y_2)\}.
\]
The fixed set is exactly P(E_+) disjoint union P(E_-), two complete RP1s. Every other projective point has least period 2. There is no nonperiodic complement. Each fixed point is its own source orbit; each remaining two-cycle is one orbit with both phases. Both collections have continuum cardinality.

Put a=x1^2+x3^2 and b=x2^2+x4^2. Directly from this owner's (2)--(4),
\[
J_A=\frac{4(a+b)^2}{(a+4b)^2},\qquad
c_B(2n,[v])=0,\qquad
c_B(2n+1,[v])=2\log\frac{a+4b}{2(a+b)}.
\tag{11}
\]
These identities hold for all integers n. In particular finite projective order does NOT make every individual step round-volume-preserving. The clock kernel is all even-lag arrows, plus odd-lag arrows exactly on the complete quadric a=2b. This quadric contains, but is larger than, the fixed set: for example [sqrt(2):1:sqrt(2):-1] belongs to it but neither eigenspace. Lag kernel and its intersection with the clock kernel remain units.

At every fixed point, a=2b and ALL isotropy clocks vanish. Source and extension isotropy are both Z. At every nonfixed point, the source isotropy is 2Z and (11) makes extension isotropy also 2Z. Every point has H={0}; no positive physical period exists. Each full source orbit gives an R of height phases, even when a one-step phase change has nonzero clock. Distinct two-cycles and fixed-point packets are not identified, and no positive-time repetitions can be assigned to these zero-return owners.

## 8. Why the dimension comparison is valid and limited

For comparison only, the same polar argument in R2 gives the standard-round RP1 Jacobian `J_M([v])=|det M| ||v||^2/||Mv||^2`. At a real eigenline with eigenvalue lambda, this is |det M|/lambda^2. Here is the needed rational-matrix restriction, proved without importing another paper.

Let M be a nonscalar invertible rational two-by-two matrix fixing an irrational real projective line. Its eigenvalue lambda cannot be rational: the kernel of M-lambda I would otherwise be a one-dimensional rational subspace. Thus lambda has irreducible quadratic minimal polynomial, with conjugate eigenvalue mu. If the return Jacobian were positive rational, then lambda^2 would be rational. Conjugation gives mu^2=lambda^2; the distinct roots force mu=-lambda, whence |det M|=lambda^2 and J_M=1. If M is scalar, J_M=1 directly.

The same reasoning applies to any rational return power M^d. Therefore an irrational periodic RP1 point cannot have a rational multiplier exp(|ell|)>1 for this round-volume clock: rationality of that multiplier makes either J_(M^d) or its reciprocal rational, forcing ell=0. This is the precise one-dimensional restriction used here, not a claim about arbitrary metrics, nonlinear maps or other dimensions.

In MAIN, the full RP3 return at either irrational eigenline instead has lambda^4=4 and |det A|=2. Thus J_A=1/2 and the physical multiplier is 2. The fourth-power norm and the full four-dimensional determinant are exactly the dimensional difference. Restricting to the invariant projective line P(U) would use its OWN one-dimensional volume: B gives |det B|/lambda^2=1 there. That restricted metric clock is not the full RP3 clock, despite identical point dynamics on the line.

This supplies a counterexample only to an unwarranted dimension-free extension of the stated RP1 restriction. It proves no minimum dimension, universal higher-dimensional existence, novelty or prime-symbolic realization. The assigned coefficient and continuous packet multiplicities make target credit especially inappropriate.

## 9. Gates, controls and decision

| Gate or control | Exact disposition |
| --- | --- |
| External T0 ownership | Four separately specified complete RP3 owners; all-point round IMAGE laws established |
| External T1 clock bookkeeping | Exact owned matrix-Jacobian cocycles established; arithmetic naturalness NOT ESTABLISHED |
| External T2 ledger | All source periods, kernels, source/extension isotropy, H, multiplicities and repetitions classified |
| S / D / B controls | Scalar cancellation; full complementary-plane multiplicity; finite-map-order versus retained-lag distinction |
| Robustness / completeness | All-point analytic identities, every integer lag and Borel set; no cutoff or precision limit |
| PROVES_TOO_MUCH risk | An assigned coefficient and one selected eigenline do not establish a prime source; continuum equal-time packets remain |
| Classical / analytic / formal | A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED |

**Decision: STOP main-candidate admission; retain the exact external dimension control.** The full owner ledger is intact, including adverse multiplicities and zero-clock kernels. No symbolic labels may be attached afterwards to promote this frozen object. Any future lineage-admitted construction requires its own frozen source and ownership chain; these results supply only a dimensional screening boundary.

## Reproducibility and disclosure

Methods are Euclidean polar integration, exact change of variables, cocycle algebra and complete linear-period classifications. There are no scientific numerical runs, cutoffs, fitted roofs, prime/zero tables, external references, PDFs, uploads or Git writes. Mechanical line/hash, identity/Outcome and relative-link checks are separate from the proofs. See the [claim ledger](claim-ledger.md) and [overview](README.md).

The author read the frozen card through EOF and retained shared research context, but read no other new main/raw/peer material. A same-card author-side helper checked S/D/B; it is not the separate reviewer. Internal model-assisted work is NOT_CALIBRATED. ARS bounded writing/claim discipline is used; criteria_binding_unavailable, with no venue or submission-readiness assertion. CP2/CP3 remain root-owned.

Data availability: every input and exact method is in the card and paper. Ethics: no human/animal subjects or personal data. Contributions: AI-assisted formal analysis and writing, without assigning human authorship. Funding and conflicts: no declarations supplied; absence is not presumed. This is round 4/5, and neither this paper nor its external outcome authorizes work beyond the existing batch.
