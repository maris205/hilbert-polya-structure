# An interior-cycle admission gate for rational projective-plane clocks

**Paper ID:** 398-projective-plane-admission.  
**Candidate:** ANG-AUDIT-20260922-PPA01; batch GEOMETRIC-FEEDBACK-20260922-J, round 4/5.  
**Date:** 2026-09-22. Conditional class audit, not a new arithmetic candidate.  
Outcome: `CONDITIONAL CONTINUUM GATE ESTABLISHED; NO CANDIDATE ADMISSION`
**Route:** classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

For one fixed countably-piecewise rational projective map on the entire real projective plane, with its specified round-volume inverse clock, an irrational interior periodic point with nonzero cycle clock and rational physical multiplier cannot provide an isolated primitive packet. Every sufficiently small neighborhood meets continuum-many distinct primitive packets with the same entire physical stabilizer and least time. The proof separates rational eigenvalues from irrational vectors, then separates word-fixed points from least-period source cycles and full extension packets. The exact IMAGE law, retained-lag cocycle and both kernels include all legal histories, boundaries and terminals. Three independent full-carrier controls expose scalar cancellation, a complementary line of equal-time packets and a cubic finite-order zero-return case. No boundary-cycle, other-clock, other-dimension, novelty or arithmetic-admission conclusion follows.

## 1. Frozen identity and same-object ledger

The sole scientific input is the full 72-line [candidate card](candidate-card.md), SHA-256 `91999304e936a18fcaac26324828d0635014dabb78fc553ea9c54ed5fd24cbb6`, read through EOF before proof. Root released mathematics after CP1. No other new main, raw proof or reviewer evidence is used, and no theorem is imported from the linked dimension comparators.

Fix X=RP2 and its standard round volume density m. Fix a Borel domain D and disjoint countably many Borel cells P_i partitioning D, with all boundaries assigned. On P_i the deterministic return is T=F_(A_i)^(-1), where A_i is a fixed element of GL3(Q) and F_A[v]=[Av]. The actual inverse is I_i=F_(A_i) restricted to T(P_i). Every projective point remains; X minus D consists of forward terminals. A terminal has no next-step kappa, while the empty iterate has clock zero.

| Ledger row | Owner / boundary |
| --- | --- |
| Carrier and density | Full RP2, round Riemannian density; no globally oriented volume form asserted |
| Branches and point clock | Frozen matrices and Borel cells; specified smooth extensions assign EVERY actual boundary value |
| Groupoid | All legal common-tail triples, integer lag retained, equal triples identified |
| Extension and packets | All real heights; physical translation on the orbit SET, complete H and repetitions |
| Arithmetic and geometry | No new prime-symbolic source, symplectic map, positive suspension roof or operator |
| Controls | Three separate full-RP2 owners, each D=X with its own one-branch matrix and round clock |

The motivation is the admissibility-to-return-geometry interface. This class audit supplies a restriction on an owned clock, not a missing arithmetic mechanism or a lineage-admitted candidate.

## 2. Full IMAGE law and the assigned point clock

For any invertible real three-by-three A put f_A(u)=Au/||Au|| on S2, with round area sigma. Euclidean polar integration and y=Ax give, for every nonnegative Borel h,
\[
\frac13\int_{S^2}h(f_Au)\|Au\|^{-3}\,d\sigma(u)
=\int_{\mathbb R^3}h(Ax/\|Ax\|)1_{\{0<\|Ax\|\leq1\}}\,dx
=\frac1{3|\det A|}\int_{S^2}h\,d\sigma.
\]
Taking h=1_(f_A(E)) yields the IMAGE formula on every sphere Borel E. Dividing by the two-sheeted antipodal cover, a local isometry, yields on the full RP2
\[
m(F_AE)=\int_EJ_A\,dm,\qquad
J_A([v])=|\det A|\frac{\|v\|^3}{\|Av\|^3}.
\tag{1}
\]
The map is a smooth global diffeomorphism. Its usual differential Jacobian agrees almost everywhere with (1); continuity and full support of m upgrade equality to every point. The expression is unchanged by a nonzero scalar multiple of v or A and obeys J_(AB)(x)=J_A(F_Bx)J_B(x), by direct norm cancellation. No content reduction of the frozen matrix word is needed.

Every T(P_i) is Borel because it is the image of P_i under an ambient homeomorphism. Restricting (1) therefore proves `m(I_i E)=integral_E J_(A_i) dm` for EVERY Borel E contained in T(P_i), including boundary subsets. Its smooth extension also supplies the stipulated pointwise values on null sets; an a.e. density alone would not fix those values. The unique cell assignment makes
\[
\kappa(x)=-\log J_{A_i}(Tx)=\log J(T|_{P_i})_{\rm extension}(x)
\tag{2}
\]
single-valued and finite at each actual step. Equation (2) does not assert intrinsic differentiation of a thin cell or create a clock at a terminal.

## 3. All common-tail arrows, both kernels and complete H

Let S_k(x) be the sum of kappa along k legal steps, with S_0=0. Define
\[
G=\{(z,k-l,w):T^kz=T^lw,\ k,l\geq0\},\qquad
c(z,k-l,w)=S_k(z)-S_l(w).
\tag{3}
\]
If two witnesses have the same lag, their exponents differ by a common integer. Padding the shorter witness adds the identical sum along the common tail, so c is independent of witnesses. The longer witness certifies that this padding is legal even for partial T. Aligning the middle exponents similarly proves additivity under composition; reversing endpoints negates c. All finite histories ending at a terminal remain valid.

For an actual inverse word u=(i_0,...,i_(k-1)), put M_u=A_(i_0)...A_(i_(k-1)) in this exact order, and M_empty=I. On its actual Borel domain I_u=F_(M_u). If z=I_u(t), w=I_v(t) are ANY two legal incoming histories to the same t, then
\[
c(z,|u|-|v|,w)=\log\frac{J_{M_v}(t)}{J_{M_u}(t)}.
\tag{4}
\]
This follows by composing (1) along each actual history. It describes the full kernels: ker c consists exactly of the represented arrows with J_(M_u)(t)=J_(M_v)(t); ker lag consists of those with |u|=|v|; their intersection satisfies BOTH conditions. These are representation-independent by (3). In the general noninjective class ker lag need not be units: distinct points can have equal-length common tails. Countable inverse branches retain all such histories; none is selected away.

The extension has all (x,h) in X times R, with arrows `(w,h)->(z,h+c)`. The sign convention matters: the arrow x->Tx has lag -1 and clock -kappa(x), whereas `(x,1,Tx)` has clock kappa(x). These are consequences of (3), not a change to the frozen clock. Real height translation commutes with every arrow.

For an eventually periodic source point whose least eventual period is q, source isotropy is exactly qZ. If C is the clock sum over its cycle, c on lag nq is nC: preperiod sums cancel and a cyclic change of phase leaves C unchanged. If the point is not eventually periodic, including a terminating history, source isotropy is trivial. Hence at EVERY height,
\[
H_x=c(G_x^x)=C\mathbb Z,\qquad
\operatorname{Iso}_{\rm ext}(x,h)=\{nq:nC=0\}
\tag{5}
\]
in the eventual-periodic case; both are trivial otherwise. Formula (5) is the ENTIRE return group, not a chosen subgroup. If C is nonzero, extension isotropy is trivial and the least positive physical time is |C|; if C=0 then H={0}, not R, and there is no positive physical period.

Fixing one source reference point identifies its entire extension orbit set with R/H: connecting arrows supply height offsets, and two reference heights agree exactly modulo isotropy clocks. All incoming histories and all real phases therefore belong to the same one physical orbit. Distinct source orbits remain distinct packets, even at equal times. Positive repetitions of a nonzero-C packet are r|C|; no positive-roof suspension or regular quotient manifold is inferred.

## 4. Interior-cycle theorem and exact algebraic obstruction

**Theorem.** Let x be an irrational projective periodic point with least source period q. Suppose a full two-dimensional open neighborhood has the same legal first-q itinerary. Let C=S_q(x) be nonzero and exp(|C|) rational. Then every sufficiently small neighborhood of x meets continuum-many DISTINCT primitive physical packets, each with the SAME complete H=CZ and least positive time |C|.

**Proof, algebraic part.** Fix that itinerary and its exact inverse matrix M=A_(i_0)...A_(i_(q-1)) in GL3(Q). Locally T^q=F_M^(-1). Choose a real nonzero representative v of x; periodicity gives Mv=lambda v for a nonzero real lambda. Equation (1) and cycle telescoping give
\[
C=3\log|\lambda|-\log|\det M|,\qquad
e^C=\frac{|\lambda|^3}{|\det M|}.
\tag{6}
\]
Since exp(|C|) is rational, exp(C) is rational as well, so lambda^3 is a nonzero rational number a (with its actual sign). If lambda were irrational, the cubic t^3-a would be irreducible over Q. Indeed a reducible rational cubic has a rational root, whereas t^3-a has exactly one real root, lambda. Its degree-three minimal polynomial would then equal the characteristic polynomial of M, forcing det M=a=lambda^3. Equation (6) would give C=0, a contradiction. Thus lambda is rational.

The eigenspace E=ker(M-lambda I) has a rational basis. If its dimension were one, its sole projective line would be rational, contradicting x not in RP2(Q). Thus dim E is at least two. Dimension three would make M=lambda I and again C=0; therefore dim E=2. Irrationality of x is used here as a statement about its line, not about an arbitrary representative. All points of P(E) are fixed by F_M and have the same ambient round Jacobian |det M|/|lambda|^3.

**Proof, least period and packet multiplicity.** The interior-itinerary hypothesis makes each T^j, 0<=j<=q, a fixed smooth projective expression on a neighborhood U of x. Since x has least period q, its q phase points are distinct. Choose disjoint small neighborhoods of those points and shrink U to a neighborhood V of x such that V and T^j(V) are disjoint for 1<=j<q. When q=1 this separation requirement is empty.

For every y in V intersect P(E), the frozen itinerary is legal and T^q y=y. Returning to y repeats the same deterministic itinerary forever. The phase separation rules out every smaller period, so y has least period q. The same inverse matrix and eigenvalue give S_q(y)=C by (6). Any neighborhood of x contained in V meets a projective-line arc in P(E), containing continuum-many points; explicitly nearby lines [v+t u] with u in E independent of v provide such an arc.

No two distinct such y in V lie in the same source orbit. Two periodic points with a common forward tail lie on the same q-cycle; their phase difference would be some j<q, excluded by V intersect T^j(V) being empty unless they coincide. Adding ALL other incoming histories cannot merge different periodic cycles in a deterministic map. Thus the continuum of points gives a continuum of different source orbits, not repeated descriptions of one orbit. Equation (5) assigns each the full H=CZ, trivial extension isotropy and precisely the primitive time |C|. The same statements hold at every incoming state and every height; each packet has repetitions r|C|. QED.

The theorem stops an isolated-packet inference under exactly these assumptions. It gives no conclusion about boundary-only itineraries, rational periodic points, C=0, irrational exp(|C|), nonprojective maps, different clocks/densities or other dimensions. Those points are not removed from the owner. In particular the audit does not classify all periodic points of an unspecified partitioned map.

## 5. Independent full-carrier controls and their complete clocks

For each control D=X and one matrix A defines T=F_A^(-1). A common-tail triple has z=F_A^n(w), n=k-l, and (3) becomes
\[
c_A(n,[v])=3\log\frac{\|A^nv\|}{\|v\|}-n\log|\det A|.
\tag{7}
\]
This follows directly from S_k=log J_(T^k), not from a borrowed control. Formula (1) independently supplies every owner's all-point and full Borel IMAGE law. Every inverse and incoming is in its full two-sided orbit. In each of these globally invertible controls the lag kernel IS units, as is its intersection with the clock kernel.

**S: A=2I3.** Its determinant modulus is 8 and A^n=2^n I3, so J_(A^n)=1 and c_S=0 for every integer n and point. Every point is fixed, with source and extension isotropy Z, H={0}, and the entire groupoid as clock kernel. There is no nonperiodic complement. The continuum of singleton source orbits each gives a physical R, with no positive primitive time or positive-time repetitions. Equal projective maps do not remove integer isotropy labels.

**D: A=diag(2,1,1).** Write a=x1^2, b=x2^2+x3^2 for v nonzero. The complete clock is
\[
c_D(n,[v])=\frac32\log\frac{4^na+b}{a+b}-n\log2.
\tag{8}
\]
The entire periodic set is the axis e=[1:0:0] and the complementary projective line P={x1=0}; all these points are fixed. If a,b are both positive, `[2^n x1:x2:x3]=[x1:x2:x3]` for nonzero n is impossible, so every remaining point is nonperiodic and no unlisted higher periods exist.

At e, c_D(n)=2n log 2: source isotropy Z, extension isotropy trivial, H=(log 4)Z, and ONE primitive log-4 packet. At EVERY point of P, c_D(n)=-n log 2: source isotropy Z, extension isotropy trivial and H=(log 2)Z, giving a continuum of different primitive log-2 packets. This includes irrational points in a rational two-dimensional eigenspace, consistent with the theorem; the isolated axis point is rational. All mixed points have trivial source/extension isotropy and H={0}, hence physical R orbits. Their source-orbit collection is a continuum, since the direction [x2:x3] is arbitrary and invariant and each orbit is countable.

For the full clock kernel, let n be nonzero and s=2^(2n/3). Equation (8) vanishes exactly when `(s^3-s)a+(1-s)b=0`, equivalently
\[
b=s(s+1)a.
\tag{9}
\]
Together with units these are ALL kernel arrows, and all their nonunit sources are nonperiodic. They are not isotropy. Each positive packet retains all height phases and repetitions r log 4 or r log 2; a repetition of a line packet at log 4 is not the axis primitive packet.

**C: A=((0,0,2),(1,0,0),(0,1,0)).** Here A^3=2I3 and |det A|=2. Its characteristic polynomial is t^3-2, with unique real root rho=cuberoot(2). The only projective fixed point is e_C=[rho^2:rho:1]. Every other point has least source period 3, since the projective map has order 3; there is no nonperiodic complement. This irrational fixed point has ZERO return clock, so the theorem's nonzero hypothesis is essential.

For a=x1^2, b=x2^2, d=x3^2 and N=a+b+d, the complete clock for EVERY integer j is
\[
c_C(3j,[v])=0,\quad
c_C(3j+1,[v])=\frac32\log\frac{a+b+4d}{N}-\log2,\quad
c_C(3j+2,[v])=\frac32\log\frac{a+4b+4d}{N}-\log4.
\tag{10}
\]
This follows from A v=(2x3,x1,x2), A^2v=(2x2,2x3,x1) and scalar invariance of (1), including negative powers. Its full clock kernel has all 3Z-lag arrows, plus residue-1 arrows exactly where `(4-rho^2)d=(rho^2-1)(a+b)`, and residue-2 arrows exactly where `(4-rho^4)(b+d)=(rho^4-1)a`. These conditions concern the whole carrier, not just e_C; each quadric also has nonfixed points.

At e_C, A acts by rho and J_A=2/rho^3=1. Source and extension isotropy are both Z. At every other point, source and extension isotropy are both 3Z because all three-step return clocks vanish. H={0} EVERYWHERE. There is one singleton source orbit and continuum-many three-cycle source orbits, each giving a physical R with no positive primitive time. The three phase sheets are joined by the partial clocks (10), whose full-cycle sum is zero. A nonzero partial displacement is not a physical period. Neither equal maps nor threefold returns collapse the retained lag or identify different source cycles.

## 6. Gate assessment, adverse findings and decision

| Gate / control | Exact disposition and limit |
| --- | --- |
| Conditional T0 | Fixed full carrier, assigned branches, all-point clock and legal-history ownership verified under the frozen inputs |
| Conditional T1 | Owned round-volume clock identities established; no arithmetic source or strong naturalness established |
| Conditional T2 | Interior irrational nonzero rational-multiplier cycle forces continuum distinct equal-time primitive packets |
| S / D / C controls | Scalar cancellation; full-line multiplicity; cubic irrational fixed point with zero full return |
| Completeness / robustness | Exact all-point Borel laws and all integer lags; general admission theorem restricted to its interior hypothesis |
| PROVES_TOO_MUCH boundary | Assigned coefficients, isolated selections or post hoc symbolic labels provide no candidate admission |
| Formal / analytic | Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED |

**Decision:** retain the conditional continuum gate and STOP an isolated primitive-packet claim for the tested class of irrational interior cycles. No concrete arithmetic candidate is admitted or globally rejected by this class audit. A future changed branch rule, clock or geometry requires its own frozen owner; the excluded cases do not inherit either a positive result or this obstruction. No minimal-dimension, novelty, RH or Route conclusion is asserted.

## Reproducibility, exposure and disclosure

All inputs and proofs are in the card and this paper; see [claim-ledger.md](claim-ledger.md) and [README.md](README.md). Methods are polar integration, exact matrix algebra, minimal polynomials, local phase separation and complete control ledgers. No numerical census, cutoff, target fitting, prime/zero data, external references, operator construction, PDF, Git write or external publication is used. File hashes, line counts, ID/Outcome and link checks verify documents, not mathematical truth.

The author read the full card and retained shared context, without reading other new papers or raw/peer evidence. A same-card author-side helper checked the three controls and signs; it is not independent review. Internal work is shared-history NOT_CALIBRATED. ARS bounded writing and claim discipline is used; criteria_binding_unavailable and no venue-readiness assertion. CP2/CP3 and card integration remain root-owned.

Data availability: exact inputs and methods are fully stated. Ethics: no human/animal subjects or personal data. Contributions: AI-assisted formal analysis and writing; no human authorship assigned. Funding/conflicts: no declarations supplied, and absence is not presumed. This is round 4/5 of the existing batch, not authorization for another batch.
