# Conjugation on complete clock packets: pairing, real cycles and half-turns

**Paper ID:** 408-conjugation-packet-involution.  
**Candidate ID:** ANG-AUDIT-20260923-CPI01; batch NONLINEAR-PACKET-20260923-L, round 4/5.  
**Date:** 2026-09-23. Conditional ownership audit, not an admitted arithmetic candidate.  
Outcome: `CONJUGATION PACKET CLASSIFICATION ESTABLISHED; NO CANDIDATE ADMISSION`
**Route:** classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

Exact reflection of assigned rational germs induces a time-preserving conjugation involution on the full actual-history clock extension. Distinct conjugate source cycles remain different physical packets with equal entire return groups. A self-conjugate least cycle is either entirely real or has even length and conjugation acts by its half-cycle shift. In the latter case the physical involution is a half-period translation when the cycle clock is nonzero, not a second packet; for zero clock it is the identity on the free height orbit. Complete inverse IMAGE laws and kernel formulas include every boundary, terminal and legal incoming history. One linear control has a single log-2 packet; a quadratic fixed-point window has two distinct log-3 packets; a second quadratic has two log-4 fixed packets and one conjugation-invariant log-64 two-cycle packet. These distinguish a conditional multiplicity obstruction from a blanket claim about nonreal points.

## 1. Frozen owner, exposure and question

The sole scientific input is the clarified 81-line [candidate card](candidate-card.md), SHA-256 `2a6f1a70c08b1cfc2c434cc002c0693c8fd696ddf24326e71a312f37294dceae`, read through EOF after CP1 release. Its last clarification defines a fixed/cycle basin as the FULL actual common-tail saturation, not an asymptotic attracting basin. That definition is used throughout.

Fix X=C with real Lebesgue area mu, a conjugation-invariant Borel legal domain D, and disjoint countably many Borel injective pieces P_i covering D. On P_i, T has a specified nonconstant complex rational germ f_i and its actual Borel inverse. Every legal point has finite nonzero assigned derivative; legal poles and critical points are excluded. All X minus D remain terminals. The assigned germ at conjugate(z) is the reflected germ at z, not merely an a.e. or point-value match.

| Same-object row | Definition and boundary |
| --- | --- |
| Derivative and point clock | a(z)=f_i'(z) on its assigned piece; kappa(z)=log abs(a(z))² |
| Inverse version | The derivative of the assigned local inverse germ at every actual inverse target |
| Histories | All legal finite iterates and common-tail triples, integer lag retained, equal triples identified |
| Extension | All X times R, real height translation on the orbit SET; no quotient manifold claimed |
| Periodic owner | Least actual source cycle, all incoming and phases, entire H and repetitions |
| Missing arithmetic | No new divisor-symbolic source, geometric permission construction, operator or Route entry |

The question is exactly when conjugation creates a distinct same-time positive packet. The benchmark is nonempty positive primitive data consisting only of log ordinary-prime times, with at most one packet per prime; ultimate all-prime coverage is a different obligation. Each generic control remains external. The card records root's prior reading of 404's card/outcome and informal fixed/two-cycle design algebra. This is disclosed design exposure, not sealed preregistration, independent evidence or an imported theorem; the author did not read that dependency.

## 2. Full Borel IMAGE and all-point derivative ownership

At a legal point the complex inverse-function theorem supplies a biholomorphic germ, whose real Jacobian determinant is |a(z)|² by the Cauchy--Riemann equations. Its inverse has area Jacobian |a(z)|^(-2). These numbers are finite and strictly positive at EVERY legal point. The actual piece need not be open: cover it by countably many such local neighborhoods and disjointize the corresponding Borel subsets. Injectivity on the piece makes their image subsets disjoint. The ordinary local change-of-variables identity then sums to
\[
\mu(I_iE)=\int_E |I_i'(w)|^2\,d\mu(w),\qquad
|I_i'(Tz)|^2=|a(z)|^{-2},
\tag{1}
\]
for every Borel E in the actual image T(P_i). Null boundary points retain the derivative of their assigned germ; no arbitrary a.e. modification is supplied. Equation (1) proves the negative-log inverse-Jacobian identity kappa(z)=log|a(z)|². Positivity here is positivity of the Jacobian; kappa itself may be positive, zero or negative. At a terminal no next-step kappa is defined.

For a legal prefix define
\[
D_m(z)=\prod_{j=0}^{m-1}a(T^jz),\quad D_0=1,\qquad
S_m(z)=\log|D_m(z)|^2.
\tag{2}
\]
The chain rule for the assigned germs gives (2), even when a point lies on a piece boundary. On each actual inverse-history branch the corresponding Borel IMAGE identity follows by the same partition argument or composition of (1). It uses that history's entire actual domain; a global differentiable extension of the piecewise map is not asserted.

Let Jz=conjugate(z). Germ reflection gives T(Jz)=J(Tz), a(Jz)=conjugate(a(z)), and kappa(Jz)=kappa(z) at every legal point. Reflection preserves D, terminals, area and every legal history, including its assigned inverse derivative. Individual piece labels need not be globally permuted: reflection can move between different pieces, while the actual reflected predecessor is retained. The stronger germ condition is what fixes derivative covariance at null periodic points.

## 3. Complete actual groupoid, kernels, isotropy and heights

The frozen groupoid and clock are
\[
G=\{(z,m-n,w):T^mz=T^nw,\ m,n\geq0\text{ legal}\},\qquad
c=S_m(z)-S_n(w)=\log\frac{|D_m(z)|^2}{|D_n(w)|^2}.
\tag{3}
\]
For two witnesses of the same triple, their exponents differ by common padding. The longer witness certifies legal padding of the common endpoint; both sums acquire the same additional term. This proves descent for partial T as well as total T. Aligning the middle exponents proves additivity under composition; reversing an arrow negates c.

The full clock kernel comprises the actual arrows with |D_m(z)|=|D_n(w)|. The lag kernel comprises those with m=n. Their intersection requires both conditions. In a noninjective owner these can contain nonunit arrows; they are not replaced by germ identities or selected return words. Empty prefixes keep every unit, including terminal units, and finite histories ending at a terminal remain.

Let a least-q cycle have C=S_q(p)=log|D_q(p)|². Every point in its complete common-tail saturation is eventually periodic with source isotropy qZ and clock jC on lag jq. Preperiod contributions cancel, and cyclic changes of the starting phase preserve C. Conversely, a nonzero isotropy lag in a deterministic map implies eventual periodicity; other points, including terminating histories, have trivial source isotropy. At EVERY height,
\[
H_x=C\mathbb Z,\qquad
\operatorname{Iso}_{\rm ext}(x,h)=\{jq:jC=0\}
\tag{4}
\]
on a cycle saturation. Outside all eventual cycles, H and extension isotropy are trivial. For C nonzero, the least positive physical time is L=|C| and extension isotropy is trivial. For C=0, source and extension isotropy remain qZ but H={0}; there is NO positive physical period. Negative C is not discarded or replaced by zero.

The extension has every object (x,h) and arrows `(w,h)->(z,h+c)`. A reference source identifies the extension orbit set of its whole source orbit with R/H: connecting arrows fix height offsets and isotropy supplies exactly their ambiguity. Thus all incoming histories and real phases belong to one physical orbit, while different source cycles remain different packets. Nonzero-C repetitions are r|C| within that same packet. No positivity, non-Zeno or classical suspension claim is inferred from this set-level construction.

## 4. The conjugation involution and exact cycle classification

Define J(z,k,w)=(Jz,k,Jw) and the height map J(x,h)=(Jx,h). Reflection of every history and (2) show that J is a groupoid automorphism, preserves c, and induces an involution on the entire extension orbit set commuting with the SAME real height translation. It does not reverse time merely because it reverses complex orientation. It preserves both kernels, their intersection, source/extension isotropy and the whole H.

**Theorem (cycle action).** Write a least-q cycle as p_j=T^jp_0. Its conjugate is a least-q cycle. Either the two cycles are disjoint, or there is a unique s modulo q with Jp_j=p_(j+s) for every j. In the latter case 2s=0 modulo q. Hence exactly the following occur:

1. The conjugate cycles are distinct, with disjoint common-tail saturations and equal C, H and primitive/repetition times.
2. s=0: EVERY point of the cycle is real, and conjugation acts as the identity on its physical packet.
3. q is even, s=q/2: EVERY point is nonreal, and conjugation is the half-cycle shift on the source cycle.

**Proof.** Commutation with T transports the conjugate of one phase through the whole cycle. If two periodic cycles meet, deterministic iteration makes them the same cycle. On a common cycle the commuting permutation is the displayed shift; involutivity gives 2s=0 modulo q. A real phase forces s=0 and all phases real. A nonzero shift has no fixed phase and must be q/2. Distinct cycle saturations cannot meet, since a point cannot have two different eventual periodic cycles. These arguments use least source period, not a repeated word. QED.

Consequently a nonreal odd cycle must have a distinct conjugate packet. A nonreal even cycle need not: case 3 is not a duplicate. To determine its HEIGHT action, put q=2s. Reflection of the two halves yields
\[
D_s(p_s)=\overline{D_s(p_0)},\qquad
D_q(p_0)=|D_s(p_0)|^2>0,\qquad
C=2S_s(p_0).
\tag{5}
\]
The arrow `(p_0,s,p_s)` has clock C/2, so `[p_s,h]=[p_0,h+C/2]`. Thus conjugation acts on the full physical packet by translation C/2 modulo CZ. When C is nonzero this is the nontrivial half-period involution; it produces no second packet. When C=0 it is the identity on the free physical R, although it still exchanges source phases. Reflection of connecting arrows extends the same action to every incoming and every real height.

In case 2 the core is pointwise fixed by J. Reflecting a history to its real core endpoint preserves its clock, so conjugate incoming points represent the same height phase; the entire physical action is the identity. More generally any self-conjugate source orbit with H={0} has an R-equivariant involution of R, necessarily a translation delta with 2delta=0, hence the identity. Distinct conjugate source orbits with H={0} are paired free physical orbits, not positive packets.

**Benchmark consequence.** A DISTINCT conjugate pair with C nonzero always violates the stated benchmark: if |C| is a prime logarithm, there are at least two different packets at that prime; otherwise the prime-only condition already fails. A zero-C pair supplies no positive period and does not alone imply that violation. A self-conjugate nonreal cycle is not a multiplicity obstruction merely by being nonreal; (5) by itself places no integer-prime restriction on its time. No conclusion about every owner or every nonreal point follows.

## 5. R control: the complete linear ledger

R owns total T(z)=sqrt(2)z on all C and its own Lebesgue area. It is globally injective, with forward area Jacobian 2, inverse z/sqrt(2) of Jacobian 1/2, and kappa=log 2 everywhere. Thus mu(I E)=mu(E)/2 for every Borel E, including unbounded sets. The entire groupoid is `(2^(-k/2)w,k,w)`, k in Z, with c=k log 2. Clock kernel, lag kernel and their intersection are units.

The ONLY periodic point is 0, of least period one: `(sqrt(2))^q z=z` for q>0 forces z=0. Its full incoming saturation is {0}. Source isotropy is Z, extension isotropy trivial and H=(log 2)Z. It gives exactly ONE positive primitive log-2 packet, all height phases R/(log 2)Z and repetitions r log 2. Every nonzero point is non-eventually-periodic, with trivial isotropy and H={0}, retaining its full two-sided dilation source orbit and physical R.

Conjugation fixes the real source orbits and the log-2 packet. A nonreal dilation orbit and its conjugate are distinct: a real positive dilation relating w to conjugate(w) must have modulus factor one and hence w real. They are free physical orbits. R meets the two prime-only/uniqueness conditions with a nonempty ledger, but covers only prime 2 and has an explicitly assigned coefficient, not an endogenous prime source. It is an external control demonstrating why the conjugation obstruction is conditional.

## 6. N/E full inverse owners, kernels and retained terminals

For either real c=3/4 or c=1 let T_c(z)=z²+c on D=C minus {0}, with 0 retained as a terminal. Its two fixed injective pieces are H_+={Re z>0} union {Re z=0, Im z>0} and H_-=-H_+. Each maps bijectively onto C minus {c}. The roots of w-c are opposite; exactly one belongs to each piece. At w=c the only polynomial predecessor would be 0, which is illegal, so that target has NO actual predecessor. Nevertheless c remains a legal object with its own outgoing map. The terminal 0 has both nonzero predecessors solving z²=-c; histories landing there are retained and stop.

Each actual inverse sheet, including its assigned cut-boundary germ, has
\[
J I_\pm(w)=\frac1{4|w-c|}>0\quad(w\ne c),\qquad
\mu(I_\pm E)=\int_E\frac{d\mu(w)}{4|w-c|}.
\tag{6}
\]
Indeed T_c'=2z and |z|²=|w-c|; (1) gives the full Borel identity. Summing both disjoint inverse images gives `mu(T_c^(-1)E)=integral_(E minus {c}) 1/(2|w-c|) dmu`, not a selected-sheet law. No inverse derivative is defined at c because no actual inverse exists there. The forward assigned clock is kappa_c(z)=log(4|z|²) on every z nonzero. It is negative for 0<|z|<1/2, zero on |z|=1/2 and positive outside; neither control has an everywhere positive clock.

For every legal prefix,
\[
D_m^c(z)=2^m\prod_{j<m}T_c^jz,\qquad
S_m^c(z)=\log\left(4^m\prod_{j<m}|T_c^jz|^2\right).
\tag{7}
\]
Their COMPLETE actual groupoids consist of all equal-tail triples with these legal prefixes. Clock kernel is equality of the two positive products in (7); lag kernel is equal prefix length; intersection requires both. These are all-point formulas, not restrictions to the tested cycles. For instance `(z,0,-z)` has witnesses (1,1) and zero clock for every nonzero z, so the kernels include nonunit merger arrows. At all other cycles and incoming histories (4) applies with C=log|D_q^c|², including signed and zero values. No higher-cycle census or attracting-basin claim is made.

## 7. N: complete fixed set and both full fixed saturations

The fixed equation z²-z+3/4=0 gives exactly
\[
p_\pm=\frac{1\pm i\sqrt2}{2},\qquad
|p_\pm|^2=\frac34,\qquad |T_N'(p_\pm)|^2=3.
\tag{8}
\]
Both points are legal and nonreal. Let B_+ and B_- be the unions of ALL legal finite inverse histories landing at p_+ and p_- respectively. These are exactly their common-tail saturations; they are disjoint. Every point in either saturation is nonreal: a real point under this real polynomial could not land at a nonreal core. Consequently neither 0 nor the critical target 3/4 appears in these histories. Every node has both legal square-root predecessors, so all 2^m depth-m inverse points are retained. The two saturations are countable, not asymptotic neighborhoods.

At EVERY point of B_+ or B_-, source isotropy is Z, extension isotropy is trivial and the entire H=(log 3)Z. Each saturation gives one primitive packet, all real phases R/(log 3)Z and repetitions r log 3. Conjugation exchanges the two whole saturations and their two DISTINCT packets. Hence N already fails prime uniqueness in its complete fixed window, regardless of any higher cycles. No representative or shared numerical time merges them.

For an explicit full-basin phase and kernel description, take either fixed core p with clock C, choose ANY landing time a for z, and put b_p(z)=S_a(z)-aC. Additional steps at the core add the same multiple of C, so this is independent of the landing time. Every integer lag r between any two points z,w of that saturation occurs by sufficient padding, and c(z,r,w)=b_p(z)-b_p(w)+rC. Thus its clock kernel imposes that displayed expression equal zero; its lag kernel is every pair at r=0; their intersection imposes b_p(z)=b_p(w). The complete height phase is h-b_p(z) modulo C. Reflection preserves this coordinate while exchanging the fixed packets. The same proof applies to E's two fixed saturations below.

## 8. E: complete fixed and exact-two sets, with all incoming

The fixed equation z²-z+1=0 gives exactly
\[
a_\pm=\frac{1\pm i\sqrt3}{2},\qquad |a_\pm|^2=1,
\qquad C_{\rm fixed}=\log4.
\tag{9}
\]
The full polynomial two-return equation factors as
\[
T_E^2z-z=(z^2-z+1)(z^2+z+2).
\]
The factors have no common root: subtraction would force z=-1/2, which solves neither. Thus the complete EXACT period-two set is
\[
b_\pm=\frac{-1\pm i\sqrt7}{2},\qquad
T_E(b_\pm)=-1-b_\pm=b_\mp,\quad b_+b_-=2.
\tag{10}
\]
Both phases are nonzero, so this polynomial two-cycle is an actual legal cycle, not a return through the terminal. Its complex derivative product is 4b_+b_-=8, but the full area multiplier is 64. Therefore its actual primitive cycle clock is log 64, not log 8.

There are three disjoint source saturations in this window: the two full inverse saturations of a_+, a_-, and the full inverse saturation of the SET {b_+,b_-}. Every incoming is nonreal, so neither 0 nor the critical target 1 occurs and both predecessor roots are retained at every depth. Each fixed saturation has source isotropy Z, trivial extension isotropy, H=(log 4)Z and one packet. Conjugation exchanges these two distinct packets. Their nonprime primitive multiplier 4 already violates the benchmark's prime-only condition.

The two-cycle saturation has source isotropy 2Z, trivial extension isotropy and full H=(log 64)Z at every point and height. It gives ONE primitive packet containing both source phases and every incoming, with all real phases R/(log 64)Z and repetitions r log 64. Conjugation exchanges b_+ and b_- within that packet and induces the half-period height translation log 8; it does not produce two log-64 packets. The two fixed packets have repetitions r log 4 independently. All other E cycles retain (7) and (4) but are outside the frozen census window.

Explicitly put d=log 8, p_0=b_+, p_1=b_-. If T^az=p_sigma, define eta(z)=sigma-a modulo 2 and b(z)=S_a(z)-ad. Both are independent of landing time, since each core step has clock d. All arrows in this full saturation are exactly the lags r with r=eta(w)-eta(z) modulo 2, and c(z,r,w)=b(z)-b(w)+rd; sufficient padding proves existence and (3) gives the formula. These give its entire clock kernel by c=0, lag kernel by r=0 (hence equal eta), and their intersection additionally by b(z)=b(w). Its phase coordinate is h-b(z)+eta(z)d modulo 2d, as substitution in an arrow verifies. Reflection fixes b and adds one to eta, proving the same half-period action at every incoming point, not only at the two core phases.

## 9. Gate assessment and decision

| Gate / control | Exact outcome and boundary |
| --- | --- |
| Conditional T0 | All-point assigned inverse IMAGE, complete actual histories, both kernels and every height are owned |
| Conditional T1 | Reflection preserves the exact geometric clock; arithmetic naturalness remains unestablished |
| Conditional T2 | Distinct-pair / real / even half-turn classification, complete H and repetitions established |
| R complete ledger | One positive log-2 packet; benchmark necessary conditions hold, but no prime source or all-prime coverage |
| N fixed window | Two different log-3 packets: uniqueness STOP |
| E fixed/two window | Two log-4 packets plus one log-64 packet: prime-only STOP; nonreal phases need not duplicate a packet |
| Completeness boundary | All-point formulas exact; N/E higher-cycle census and asymptotic basins NOT AUDITED |
| Formal / analytic | Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED |

**Decision:** retain the conditional conjugation gate and STOP the benchmark wherever a distinct conjugate cycle pair has nonzero clock. Do not stop a different owner merely because it has nonreal points or self-conjugate cycles. The three controls remain external, and this audit admits no arithmetic candidate. A lineage application must separately construct a divisor-symbolic permission rule and geometry obeying the frozen germ reflection. No generic Julia, rational-cycle, novelty, RH or broader no-go assertion is made.

## Reproducibility, design and AI disclosure

Inputs and exact methods are fully stated; see [claim-ledger.md](claim-ledger.md) and [README.md](README.md). Methods are local complex/real change of variables, finite-prefix products, elementary cyclic permutations and exact quadratic factorization. No scientific code, high-period census, numerical fitting, prime/zero data, new literature, operator, PDF, Git mutation or publication is used. Hash/line/ID/Outcome/link checks validate files, not mathematical truth.

The author read the clarified card through EOF and retained shared history, but read no review, raw, peer or other new scientific manuscript. Author helper `/root/batch_clock_scope_review/ccg_cotangent_probe` was limited to rederiving N/E fixed/two windows, actual inverse saturations, kernels and phases from the same full card; its reported access was that card only, without other paper reads, tools for scientific computation, network or file writes. This is author assistance, not independent review. The card's root design exposure is explicitly retained and is not represented as a blind test or sealed preregistration.

AI agents supplied mathematical derivation, drafting and author-side checking; the separate internal-review workflow is also AI-assisted. No human or external verification is certified. Shared-history review is NOT_CALIBRATED, not blind, cross-model or external peer review. ARS bounded claim/evidence discipline applies; criteria_binding_unavailable, with no venue-readiness claim. Root owns card integration and CP2/CP3.

Data availability: card and proofs contain all inputs and methods. Ethics: no human/animal subjects or personal data. Contributions: AI-assisted analysis/writing without assigning human authorship. Funding/conflicts: no declarations supplied, not presumed absent. This is round 4/5 of 405–409; no sixth round is authorized here.
