# 456 — frozen card-only independent derivation

Candidate **ANG-20260924-GOF01**; date 2026-09-24; internal **NOT_CALIBRATED**.

## 1. Exact input, release and scope

After root's full CP1 reading and distinct RAW RELEASE, I personally reread the complete original `candidate-card.md`, lines 1–86 through EOF: 86 lines / 5112 bytes, SHA-256 `84ee5f19a6910b63bff4e401f17c03fc9a667bbdc843c52bc951a16352152e46`.
The frozen CP1 report is 65 lines / 7887 bytes, SHA-256 `db845cd7949badf3b4d953543849791660d877fbc25c673ae259a0ea69f57b4d`. Its actual instruction-read and inherited-exposure disclosures remain applicable.
No author manuscript, README, ledger, outcome, peer/helper proof or historical science was read. No auxiliary, network, scientific code/numerics, Git or PDF was used. The derivation below uses this card only, not any earlier candidate's theorem or clock.
This is the inherited model with shared history, not blind, cross-model or error-independent verification. The raw will be frozen after complete self-read; a later discrepancy must be disclosed separately rather than retroactively rewriting this record.

## 2. Actual sources and arithmetic interface

Write Γ(x,y)=Gamma(floor x,floor y), with the card's Gamma(0,0)=1. It is a Borel positive-integer function on the entire real plane. For fixed g≥1 put

\[
A_g=\begin{pmatrix}1&-g\\g&1\end{pmatrix},\quad
(t,s)=A_g(x,y),\quad f(t)=\frac{t}{1+t^2}.
\]

MAIN reads g=Γ(x,y) once and applies (f(t),s) exactly when t²≠1. G uses g=1 with its own guard (x−y)²≠1. L uses (t,s) with the current Γ and is total. All outputs are finite real points; no additional carrier restriction is needed.
MAIN/G's excluded critical sources remain terminal objects with units and incoming. L has no such exclusion. Floor faces, signed axes and null states remain in every full carrier with the original Lebesgue area.
On a positive integer cell [N,N+1)×[D,D+1), the readout is gcd(N,D). For integers 1<D<N it equals D if and only if D divides N. This proves the stated arithmetic interface, but neither makes it a full-source restriction nor turns general nondivisor states into terminals.

## 3. All finite inverse roots, images and actual domains

The equation f(τ)=u is exactly uτ²−τ+u=0. At u=0 its sole finite root is τ=0. At 0<|u|<1/2 there are two real simple roots, with product 1 and the sign of u: one lies in (−1,1), the other in the corresponding outer sheet. At |u|=1/2 the sole root is critical τ=±1 and is forbidden; for |u|>1/2 there is no real root.
The inner-sheet inverse is τ_0(u)=2u/(1+√(1−4u²)) on |u|<1/2, including u=0. The outer inverse (1+√(1−4u²))/(2u) is used only when 0<|u|<1/2, with its sign selecting the outer sheet. There is no root at infinity at u=0.
For each MAIN cell C_ab=[a,a+1)×[b,b+1), g=Gamma(a,b), and each appropriate sheet root, define

\[
\theta_{ab,j}(u,v)=\frac{(\tau_j(u)+gv,\ v-g\tau_j(u))}{1+g^2}.
\]

Its actual domain is precisely the sheet's displayed u-domain together with θ_ab,j(u,v)∈C_ab. The chosen root has τ²≠1 automatically. Substitution gives A_gθ=(τ,v), so the source is legal and its forward image is (u,v). Conversely every legal predecessor has its unique actual cell and one of these roots. Thus these domains include all frozen readout/guard/equality checks without testing outgoing permission at the target.
G uses the same formula with g=1 and no cell restriction. Its full image is (−1/2,1/2)×R. Each u=0 target has exactly one predecessor, each 0<|u|<1/2 target exactly two, and all other targets have none.
L's cell inverse is θ_ab(u,v)=((u+gv),(v−gu))/(1+g²), retained exactly when it lies in C_ab. This is exhaustive by the two linear inverse identities, with no folding sheet or critical restriction.
MAIN and L images are exactly the unions of these actual inverse domains. No unsupported surjectivity claim is made. Sources are deduplicated only as equal real points; uniqueness of the actual Γ and floor labels prevents an alternative label from becoming a different predecessor of the same point.

These descriptions also admit an exact finite target test, although no global label cutoff is used. For a fixed finite (τ,v), let R=√(τ²+v²). If a reconstructed source has actual g≥2, it cannot have both |x|<1 and |y|<1: their floors would belong to {−1,0}, forcing Γ=1. Therefore its norm is at least 1. Since ∥A_gz∥=√(1+g²)∥z∥=R, any such g satisfies g<R.
Consequently one may enumerate g=1 and all integers 2≤g<R, reconstruct the point and check Γ=g; for MAIN do this for every finite root, and for L use τ=u. This is equivalent to the full cell enumeration and proves that every direct predecessor set is finite. The bound varies with the actual target and root; it is not a scientific cutoff or a claim that every enumerated g occurs.
For MAIN/G, |u|≥1/2 targets have no incoming one-step predecessor but remain full objects and may have their own outgoing step. Critical targets likewise are not deleted. In particular (−1/2,−1/2) is a legal MAIN and G source of (0,−1), which is terminal for both. L retains the outgoing step at that same target.

## 4. Every-point germs and every-Borel IMAGE

On each noncritical sheet,

\[
f'(t)=\frac{1-t^2}{(1+t^2)^2},\quad
D\theta=\frac1{1+g^2}\begin{pmatrix}1/f'(\tau)&g\\-g/f'(\tau)&1\end{pmatrix}.
\]

Thus the signed inverse determinant is 1/((1+g²)f'(τ)), and the prescribed area density is

\[
J_{M,G}=\frac{(1+\tau^2)^2}{(1+g^2)|1-\tau^2|}>0,\qquad
J_L=\frac1{1+g^2}>0,
\]

where G uses g=1. All values are finite at every actual target, including assigned integer faces. The derivative at u=0 is supplied by the inner analytic branch, not a singular divided formula.
For fixed g, the oblique linear map is invertible and each one-dimensional noncritical sheet is analytically diffeomorphic onto its stated open image interval. Their product and composition give an ambient two-dimensional diffeomorphism for each inverse branch. Its ordinary change-of-variables law restricts to every Borel E in the actual cell-restricted inverse domain:

\[
\mu(\theta E)=\int_E J_\theta\,d\mu.
\]

L independently has the affine change-of-variables law on each own cell domain. Borel restrictions and their images remain Borel. This covers null cuts, not merely a.e. sources; the germ prescribes their values, while the measure identity alone does not make a null-point version unique. No floor derivative or global continuity across cuts is asserted.
The forward factors and own step clocks are

\[
\rho_{M,G}(z)=(1+g^2)\frac{|1-t^2|}{(1+t^2)^2},\quad
\kappa_{M,G}=\log\rho_{M,G},\qquad
\rho_L=1+g^2,\quad\kappa_L=\log(1+g^2).
\]

These follow from −log J_actual(Tz). MAIN/G have positive, negative and zero clocks; all are retained. For both owners, the actual g=1 points (0,0), (1/√2,0), and (√(√5−2),0) have respective forward factors 2, 4/9, and 1. Their critical sources have no outgoing step clock. L's own legal clocks are strictly positive, without importing a removed critical guard.

## 5. Complete history owner, kernels and conditional whole groups

Each partial map and every legal iterate has Borel domain. Fixed cell/sheet itineraries refine finite histories into countably many injective Borel branches with the inverse formulas above. The actual retained-lag groupoid has countable source/range fibres, units (z,0,z), and arrows (z,m−n,w) exactly when T^mz=T^nw legally.
For composable witnesses T^mz=T^nw and T^rw=T^sv, if r≥n extend the first equality by r−n using the already-legal middle history; if n≥r extend the second by n−r. This gives the summed lag and never pads a terminal beyond its legal history. Inversion reverses endpoints and lag; addition gives associativity.
Let S_m(z)=Σ_{i=0}^{m−1}κ(T^iz), S_0=0, and W_m=exp S_m. Define c=S_m(z)−S_n(w). Two witnesses with equal lag differ by the same increment to m,n; the common already-legal future contributes identical clock terms on both sides, proving full-point descent. The same alignment proves additivity. The forward arrow (Tz,−1,z) has c=−κ(z).
The fixed-itinerary branch from w to z has IMAGE density W_n(w)/W_m(z)=exp(−c). Composition of the analytic/affine branch laws proves the every-Borel identity on its actual domain, including cut intersections. Shared future factors cancel between witnesses at the assigned all-point version.
The complete arrow kernels are

\[
K_{\rm lag}=\{(z,0,w):\exists m,\ T^mz=T^mw\text{ legally}\},\quad
K_c=\{(z,m-n,w)\in G:W_m(z)=W_n(w)\},\quad
K_{\rm joint}=K_{\rm lag}\cap K_c.
\]

These are full-arrow predicates and do not identify clock equality with a unit arrow. Their exact membership is supplied by the unrestricted inverse/history construction below.
For any object, nontrivial source isotropy occurs exactly when its legal forward history is eventually periodic. Indeed an equal-iterate witness with unequal lengths gives an actual cycle, and an eventual cycle supplies every multiple of its least period p. Hence I_z=pZ in that case and I_z={0} otherwise.
For an actual least-p cycle, put C=Σ_cycle κ, with signs retained. Cancelling the transient proves c(z,jp,z)=jC for every ancestor in its full basin. Thus ENTIRE H=CZ, not a subgroup guessed from a selected return. Extension isotropy is all pZ if C=0 and trivial if C≠0. A non-eventually-periodic source has I=H={0} and trivial extension isotropy.
For C≠0 the physical primitive is |C|, with positive integer repeats; C=0 gives no positive primitive while retaining the source/extension isotropy. These general statements classify the groups conditional on actual eventual cycles; they do not assert an unperformed global cycle census.

## 6. Every incoming depth, phase and packet equivalence

Let Pre_T be the complete predecessor set of §3, P_0(a)={a}, and P_(j+1)(a)=⋃_{b∈P_j(a)}Pre_T(b). Induction proves P_j(a)={z:T^jz=a legally}. Each generation is finite, and no depth is omitted. The full incoming arrows to a are exactly

\[
\{(a,r-j,z):r\ge0,\ T^ra\text{ legal},\ j\ge0,\ z\in P_j(T^ra)\}.
\]

This gives the full source orbit, all kernels above and actual basin membership, without restricting to the core's word/cell. For a terminal τ the complete basin is ⋃_jP_j(τ), with unique arrival depth d(z). Its arrows have lag d(z)−d(w), clock S_{d(z)}(z)−S_{d(w)}(w), trivial isotropy and phase h−S_{d(z)}(z)∈R. Distinct terminal basins remain disjoint.
More generally choose a base b in one source orbit and an actual arrow γ_z=(z,k_z,b) for each of its points, only within that orbit. Put A(z)=c(γ_z). Different choices change A(z) by H_b, so the complete extension phase is [h−A(z)]∈R/H_b. Two extension points have this same phase precisely when an actual arrow connects them: their phase difference is a loop clock at b, which supplies the needed correction arrow.
No global Borel selector or nice quotient topology is claimed. Height translation acts by addition on R/H_b. Each source orbit with H_b≠{0} therefore yields one positive translation packet, not one per ancestor, starting point or height representative. Different source orbits cannot merge merely because their generators agree. For H_b=0 phases remain all real and no positive return occurs.

## 7. Complete GLOBAL fixed sets and their full packets

At a fixed point of MAIN or G, equality of second coordinates gives gx=0 and hence x=0. Equality of first coordinates then requires f(−gy)=0, so y=0. For L the same second-coordinate equation gives x=0 and the first gives gy=0. Thus every owner's entire fixed set is exactly o=(0,0).
At o the actual readout is g=Gamma(0,0)=1; t=0 is noncritical. For all three owners the forward determinant is 2, κ(o)=log 2 and the inverse density is 1/2. These statements use the frozen germ at the retained null point, not a measure-based deletion or fitted clock.
Every inverse of o has τ=0 and second mixed coordinate 0 (or both mixed coordinates 0 for L). Invertibility of A_g forces the source o, whose actual g is 1. Hence Pre_T(o)={o} and P_j(o)={o} for all j. The full incoming basin and source orbit of the core are the singleton {o} for each owner separately.
Consequently the complete restricted source owner is ({o}×Z×{o}), c(o,k,o)=klog 2, I_o=Z, H_o=(log 2)Z and extension isotropy trivial. All three restricted kernels consist only of the unit, and the complete phase is h modulo log 2. The entire fixed-core primitive packet has length log 2, with all positive integer repetitions, and is one packet per owner.
This proves uniqueness within the entire fixed family and its full incoming. It does not prove that no different higher-period source orbit has the same or a different positive primitive.

## 8. Exact prescribed two-step gate

For a two-step MAIN/G return write the positive first and second mixing parameters as a,b, put t=x−ay and X=f(t), Y=ax+y. The second-coordinate return gives bX+Y=y, hence x=−(b/a)f(t). Using y=(x−t)/a, the second step's mixed first coordinate is

\[
t_2=X-bY=\frac ba\,t+
\left(1+b^2+\frac{b^2}{a^2}\right)f(t).
\]

For t≠0, both terms have its sign because f(t) has the sign of t. Thus f(t_2) has the sign of t, while the required returning x=−(b/a)f(t) has the opposite sign. No such return exists. For t=0, these equations force x=y=0.
Apply this exact argument to the two stipulated MAIN words (a,b)=(2,1),(1,2), with all real starting points and both actual legality/readout checks. Their only formal return candidate o has actual gcd word (1,1), so neither prescribed word has any legal returning point, fixed or least-two. No cell bound, sign selection or critical-root repair was used.
For G the same proof with (a,b)=(1,1) applies globally. Its entire legal T_G²=z set is {o}, a fixed point; its GLOBAL exact-two set is empty. The argument is a short exact identity, not a higher-period census.
For L and either specified word, multiplication gives

\[
A_1A_2=A_2A_1=\begin{pmatrix}-1&-3\\3&-1\end{pmatrix}.
\]

Its fixed-vector equation subtracts the identity to give a matrix with determinant 13, so the sole formal two-step return is o. Its actual Γ word is again (1,1), not either prescribed word. L's specified exact-two sets are therefore empty on all R². L is total; no folding guard was used in this test.
No cyclic core or extra packet is produced by either ordering of the empty word family. The return sets above exhaust the frozen two-step obligations; other MAIN/L words and periods beyond this gate are not claimed classified here.

## 9. Gate decision and nonclaims

All three full Borel owners, every-Borel IMAGE laws and full-point history clocks are established. The GLOBAL fixed audit retains a genuine MAIN primitive log 2 with a singleton full basin, and the specified MAIN two-step words add no core. The two controls own their corresponding fixed results and tested exclusions independently.
The bounded gate finds no adverse MAIN primitive, multiplicity or ownership failure. It also does not prove the global prime-only or one-packet-per-prime target, because remaining higher returns were not classified. The precommitted decision is therefore **OPEN / FORK**, not global target success, empty-ledger failure or a general no-cycle claim. Nonemptiness itself is positively established by the fixed packet.
Agreement of the controls at the fixed core is not a proof of strong arithmetic naturalness, nor does it transfer their source laws into MAIN. Naturalness, PROVES_TOO_MUCH, novelty/nonconjugacy and untested return structure remain outside the proved result. T3 is NOT AUDITED, classical fields NOT APPLICABLE, formal coordinates UNASSIGNED and Route B NOT INVOKED.
Only `evidence/independent-derivation.md` is written in this stage. After full self-read and a measured hash/EOF receipt I HOLD for root's full raw reading and a distinct PAPER UNLOCK; the raw will not be overwritten after seeing author material.
