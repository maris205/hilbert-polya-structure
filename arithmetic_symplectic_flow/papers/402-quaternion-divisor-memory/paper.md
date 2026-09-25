# An owned quaternion Jacobian clock with a noninteger fixed primitive

Candidate ID: `ANG-20260922-QDM01`. Paper402, version1, 2026-09-22.
Batch `NONLINEAR-RETURN-20260922-K`, round3/5.
Outcome: `OWNED QUATERNION CLOCK; NONINTEGER FIXED PRIMITIVE — STOP / FORK`
Type: arithmetic Borel partial-map groupoid with an all-point inverse-IMAGE clock.
Status: exact owner-level result and decisive negative MAIN packet test.
Classical symplectic suspension: NOT APPLICABLE. T3: NOT AUDITED.
Formal Route coordinates: UNASSIGNED. Route B: NOT INVOKED.

## Abstract

The frozen map couples coordinatewise quaternion digits, left divisibility in the Lipschitz lattice, and a reciprocal transport whose next dividend is the written-back arithmetic memory. Its ordered inverses and four-dimensional Jacobians define an owned all-point clock, including null and boundary states. We prove the full measured inverse identities, actual groupoid and kernels, and complete fixed sets of MAIN and three separately owned controls. MAIN has a fixed packet with entire clock group \(8\log(1+\sqrt2)\mathbb Z\); its positive primitive exponent is \(577+408\sqrt2\), not an ordinary integer prime. This single MAIN packet violates the frozen necessary target. No higher-period census, invariant probability, conservative lift, analytic operator, or external novelty claim is made.

## 1. Contract, lineage, and claim boundary

The owner is exactly the [100-line frozen card](candidate-card.md), including its pre-release CP1 target clarification; no parameters or domains are changed. Write \(\Lambda=\mathbb Z+\mathbb Zi+\mathbb Zj+\mathbb Zk\), \(N(q)=q\bar q=|q|^2\), and \(C=[0,1)^4\). The full carrier and measure are
\[
Y=\Lambda^2\times\mathbb H,\qquad \mu=\#_{\Lambda^2}\otimes\operatorname{Leb}_4.
\]
This is a standard Borel, sigma-finite measured owner, not a finite-dimensional symplectic map or a positive-roof suspension. Countable memory slices and bounded real boxes establish sigma-finiteness. All integer memories and all real quaternion coordinates remain objects. No probability, trace, analytic determinant, or operator is supplied.

On the slice \(A=n-1,B=1,z=d+R\), with positive integers \(n,d\) and arbitrary \(R\in C\setminus\{0\}\), the left quotient is \(n/d\). Permission is exactly \(d\mid n\); proper-divisor inputs have \(1<d<n\). This verifies the divisor-symbolic-to-geometric arrow on every such remainder cell, without restricting the actual carrier to that slice. The geometric digit decides present permission; the quotient written into memory becomes the subsequent reciprocal dividend. The chosen lattice, coordinate floor, and multiplication order remain design choices; strong arithmetic naturalness is OPEN.

The target requires EVERY MAIN positive primitive to be \(\log p\) for an ordinary integer prime, at most one distinct packet per prime, and ultimately a nonempty all-prime ledger. A single wrong MAIN primitive is decisive. Controls cannot convict MAIN, and an empty fixed window would not prove a global coverage failure. We use neither prime tables nor inserted prime clocks.

## 2. Full actual maps, terminals, and ordered inverses

For \(x=(A,B,z)\), set \(D=\lfloor z\rfloor\in\Lambda\) coordinatewise and \(R=z-D\in C\). The common legal domain is
\[
\mathcal D=\{D\ne0, R\ne0, B\ne0, Q=D^{-1}(A+B)\in\Lambda\}.
\]
There are four distinct owners, each with its own copy of \(Y,\mu\):
\[
T(A,B,z)=(B,Q,R^{-1}B),\quad T_H(A,B,z)=(A,B,R^{-1}B),
\]
\[
T_O(A,B,z)=(B,Q,R^{-1}),\qquad T_V(A,B,z)=(B,Q,BR^{-1}).                 \tag{1}
\]
Outside \(\mathcal D\) the state is terminal, not deleted. The identity iterate and every actual incoming remain. In particular \(A=0\) and \(A+B=0\) are not exclusions; a legal step may have \(Q=0\) and end at a terminal. Units, negative coordinates, and every cube face use the same rule. Each next digit is read afresh, not retained as an independent label.

Here are ALL one-step predecessors; \(D\) ranges over \(\Lambda\setminus\{0\}\). For MAIN at \(u=(P,Q,w)\), the common target domain is \(P,w\ne0\), \(Pw^{-1}\in C\setminus\{0\}\), and
\[
I_D(u)=(DQ-P,P,D+Pw^{-1}).                                             \tag{2}
\]
Indeed \(D^{-1}((DQ-P)+P)=Q\), the floor is exactly \(D\), and \((Pw^{-1})^{-1}P=w\). Conversely every predecessor has old \(B=P\), old \(A=DQ-P\), and \(R=Pw^{-1}\). This proves both identities and exhaustion with the stated multiplication order. For fixed \(D\), \((P,Q)\mapsto(DQ-P,P)\) is injective: recover \(P\) from the second memory and then \(Q=D^{-1}(A+P)\). Different digits give distinct predecessors, including when \(Q=0\).

For H, at target \((A,B,w)\), require \(B,w\ne0\), \(Bw^{-1}\in C\setminus\{0\}\). Its inverse is
\[
I_D^H(A,B,w)=(A,B,D+Bw^{-1}),\qquad D^{-1}(A+B)\in\Lambda.               \tag{3}
\]
For O, at target \((P,Q,w)\), require \(P,w\ne0\), \(w^{-1}\in C\setminus\{0\}\); for V require \(P,w\ne0\), \(w^{-1}P\in C\setminus\{0\}\). Their inverses are respectively
\[
I_D^O(u)=(DQ-P,P,D+w^{-1}),\qquad I_D^V(u)=(DQ-P,P,D+w^{-1}P).           \tag{4}
\]
For H the memories are unchanged and the displayed left-divisibility check is essential. O and V have the same injective memory map as (2). Directly, \((w^{-1})^{-1}=w\) and \(P(w^{-1}P)^{-1}=w\), proving their forward identities. Reversing each equality forces precisely (3) or (4), so these lists too are exhaustive. Every inverse uses its own target domain, floor, nonzero checks, and source permission. No norm cutoff is imposed. An object outside an inverse domain is not thereby a forward terminal.

The coordinate floor is Borel and quaternion inversion is continuous off zero. Lattice membership is a countable condition. Thus all domains and maps are Borel, with a countable injective digit atlas. Source digit cells are disjoint, although their forward images can overlap. We do not count alternative inverse words as additional arrows.

## 3. All-point Jacobians and every-Borel IMAGE

For \(w\ne0\), differentiation in the real four-dimensional quaternion space gives
\[
d(w^{-1})[h]=-w^{-1}h w^{-1}.
\]
Multiplication on either side by \(a\ne0\) scales Euclidean norms by \(|a|\), hence has absolute real determinant \(|a|^4=N(a)^2\). Inversion therefore has absolute Jacobian \(N(w)^{-4}\). Applying this separately to (2)--(4) and (3) gives
\[
J^T_D(P,Q,w)=J^V_D(P,Q,w)=\frac{N(P)^2}{N(w)^4},\quad
J^H_D(A,B,w)=\frac{N(B)^2}{N(w)^4},\quad
J^O_D(P,Q,w)=\frac1{N(w)^4}.                                          \tag{5}
\]
Each is finite and strictly positive on its own complete inverse domain. These are the frozen real-analytic extension derivatives, also at actual cube faces. We are not inferring point values from an almost-everywhere Radon--Nikodym class.

For every Borel set \(E\) in any one inverse branch domain,
\[
\mu(I_D^F E)=\int_E J_D^F\,d\mu,\qquad F\in\{T,T_H,T_O,T_V\}.         \tag{6}
\]
Proof: on each target memory slice the real map is a diffeomorphism on the ambient nonzero quaternion domain, so real change of variables applies to arbitrary Borel subsets, including their intersections with half-open cells. The fixed-digit memory map is injective (identity for H). Summing these identities over the countable memory slices proves (6), also for infinite measure. Counting memory contributes factor \(1\), not a lattice index or \(N(D)\). One may sum inverse images across distinct digits because their source cells are disjoint; overlapping forward images must not be summed as if disjoint. This proves the full measured identity, not merely a one-slice identity.

At a legal source put \(\kappa_F(x)=-\log J_D^F(Fx)\). Norm multiplicativity gives \(N(R^{-1}B)=N(BR^{-1})=N(B)/N(R)\), and hence
\[
\kappa_T=\kappa_H=\kappa_V=2\log N(B)-4\log N(R),\qquad
\kappa_O=-4\log N(R).                                                 \tag{7}
\]
Equality of these formulas where stated follows from each owner's own derivative; no clock is transferred. They are real signed clocks, not a claim of positivity at all legal states. There is no one-step clock at a terminal. All point and boundary values used below are fixed by (5), including measure-zero fixed states.

## 4. Full actual groupoids, kernels, isotropy, and phases

The following statements apply separately to each map \(F\) in (1). For every legal length \(m\ge0\), define
\[
K_m(x)=\prod_{j=0}^{m-1}\frac{N(B_j)^2}{N(R_j)^4}\quad(F=T,T_H,T_V),
\qquad K_m^O(x)=\prod_{j=0}^{m-1}N(R_j)^{-4},\quad S_m=\log K_m,          \tag{8}
\]
with empty product \(1\). The actual groupoid consists of triples
\[
G_F=\{(x,m-n,y):F^m x=F^n y,\ m,n\ge0\text{ legal}\},\qquad
c_F(x,m-n,y)=\log\frac{K_m(x)}{K_n(y)}.                                \tag{9}
\]
The source is \(y\), range \(x\), multiplication adds lags, and equal triples are identified. If two witnesses have the same lag, their lengths differ by a common integer; the longer witness appends identical legal factors to both sides of (9). Thus \(c_F\) is independent of witnesses. To compose two arrows, extend the shorter of their histories at the middle object to the longer legal history and use the shared future; the intermediate sums cancel. This proves the cocycle law, with inversion changing its sign. The countable equality loci give a Borel groupoid. On an actual branch-pair chart the ratio of inverse Jacobians is \(e^{-c_F}\); applying (6) and its finite compositions proves its every-Borel IMAGE identity as well.

Here are the COMPLETE kernels, with membership always in the actual \(G_F\):
\[
\ker c_F=\{(x,m-n,y):K_m(x)=K_n(y)\},
\]
\[
\ker\ell=\{(x,0,y):\exists m\ge0, F^m x=F^m y\},\qquad
\ker c_F\cap\ker\ell=\{(x,0,y):F^m x=F^m y, K_m(x)=K_m(y)
\text{ for some legal }m\}.                                          \tag{10}
\]
These conditions are exhaustive and witness-independent, not merely sufficient subgroups. In particular the lag kernel need not be units: distinct allowed first inverse branches of one target have the same one-step \(K\), since (5) is digit-independent, and give arrows in both kernels. There is no additional isotropy from free digit words.

For completeness, let a source \(x\) eventually enter a genuine least-period-\(q\) full-state cycle. Then \(G_{F,x}^x=q\mathbb Z\); otherwise it is \(\{0\}\). Proof: a nonzero isotropy witness repeats one forward state and thus yields an eventual cycle. On an eventual least-\(q\) cycle, exactly the multiples of \(q\) give such repeated states, and every multiple has legal witnesses after the entry time. If \(\lambda=\sum_{j=0}^{q-1}\kappa_F(f_j)\) on that cycle, transient terms cancel and
\[
c_F(kq)=k\lambda,\qquad H_x=c_F(G_{F,x}^x)=\lambda\mathbb Z.            \tag{11}
\]
Off eventual cycles, \(H_x=\{0\}\). This characterizes full isotropy without classifying any higher-period cycles. Finite trajectories ending at a terminal have zero isotropy, even with many incoming branches.

The extension has ALL objects \(Y\times\mathbb R\) and arrows \((y,h)\to(x,h+c_F(g))\). Height translation descends to its orbit SET; no Hausdorff quotient or invariant measure is asserted. Extension isotropy is \(\{kq:k\lambda=0\}\): it is zero if \(\lambda\ne0\), retains \(q\mathbb Z\) if \(\lambda=0\), and is zero off eventual cycles. The stabilizer of height translation over a base orbit is precisely the ENTIRE \(H_x\), so the positive primitive is \(|\lambda|\) when nonzero and there is none when zero. Repetitions use \(k\lambda\), not a rescaled or selected clock.

All incoming are defined recursively by \(P_0(u)=\{u\}\) and \(P_{m+1}(u)=\bigcup_{v\in P_m(u)}\{I_D^F(v):\text{all own inverse checks hold}\}\). The full base orbit of \(u\) is the union of these \(P_m(F^n u)\) over every legal \(n,m\ge0\). This follows in both directions directly from the meeting relation (9); no unchecked digit word is an incoming. To describe ALL extension phases over that orbit, fix \(f\) and choose any arrow \(g_y:y\to f\). Then
\[
[(y,h)]\longmapsto h+c_F(g_y)\pmod{H_f}                               \tag{12}
\]
is well-defined and complete: two choices differ by isotropy at \(f\), and equal classes give an actual lifted arrow. Height translation becomes addition on \(\mathbb R/H_f\). For a cycle with \(f_j=F^j f_0\) and \(F^m y=f_j\), the phase is \(h+S_j(f_0)-S_m(y)\pmod{\lambda\mathbb Z}\). All real phases, not only a chosen section, remain.

## 5. Complete MAIN and order-reversed fixed sets

A MAIN fixed state satisfies \(A=B\ne0\) and \(D^{-1}(2B)=B\). Thus \(2B=DB\), and right multiplication by \(B^{-1}\) forces \(D=2\). Its real equation \(2+R=R^{-1}B\) is equivalent to
\[
B=R(2+R)=R^2+2R,\qquad R\in C\setminus\{0\}.                         \tag{13}
\]
For V the integer equations give the same \(A=B,D=2\), while its OWN real equation gives \(B=(2+R)R=R^2+2R\). The equality here uses the now-forced central digit \(2\), not general commutativity or a full-map conjugacy.

An exhaustive explicit lattice parameterization is as follows. For every \(B=b_0+b_1i+b_2j+b_3k\in\Lambda\setminus\{0\}\), set
\[
s_B=\sqrt{\frac{|B+1|+b_0+1}{2}}.
\]
Keep only \(1\le s_B<2\), define
\[
R_B=(s_B-1)+\frac{\operatorname{Im}B}{2s_B},
\quad\text{and require }0\le\frac{b_j}{2s_B}<1\quad(j=1,2,3).           \tag{14}
\]
Exactly the fixed cores, for EACH of MAIN and V, are
\[
f_B=(B,B,2+R_B)                                                       \tag{15}
\]
for these accepted \(B\). To prove uniqueness and exhaustion, write \(1+R=s+v\) with \(s\ge1\). Equation (13) becomes \((s+v)^2=B+1\), giving \(2sv=\operatorname{Im}B\), \(s^2-|v|^2=b_0+1\), and \(s^2+|v|^2=|B+1|\). These force (14); conversely (14) satisfies those identities and (13). \(B\ne0\) excludes \(R=0\). The exact half-open inequalities retain all valid boundary points; no numerical list or root choice is omitted.

At (15), \(N(B)=N(R_B)N(2+R_B)\). The separately owned clocks therefore give
\[
\lambda_B=2\log\frac{N(2+R_B)}{N(R_B)}>0,                              \tag{16}
\]
because \(N(2+R)-N(R)=4+4\operatorname{Re}R>0\). Each accepted \(B\) supplies one fixed source core, with full source isotropy \(\mathbb Z\) and entire \(H=\lambda_B\mathbb Z\), not a subgroup generated by a chosen inverse branch. Distinct cores cannot merge under (9), since their constant futures could meet only if equal. Equal times do not merge packets.

In particular take \(B=1\), \(r=\sqrt2-1\), and \(\alpha=1+\sqrt2=2+r\). Then \(r\in C\setminus\{0\}\), \(r\alpha=1\), and \(r^2+2r=1\). Hence
\[
f_*=(1,1,\alpha),\quad D=2,\quad Q=1,\quad
H_{f_*}=L_*\mathbb Z,\quad L_*=8\log\alpha>0.                           \tag{17}
\]
This is the actual least positive primitive by (11), not an iterate or selected symbolic period. Exactly
\[
e^{L_*}=(1+\sqrt2)^8=577+408\sqrt2\notin\mathbb Z.                     \tag{18}
\]
Thus MAIN itself violates the ordinary-integer-prime target. Its full incoming and all extension phases, given below, cannot remove or shorten this primitive.

## 6. Independently owned H and O fixed sets

For H, memories are unchanged. Choose any \(D\in\Lambda\setminus\{0\}\), \(K\in\Lambda\), and \(R\in C\setminus\{0\}\). Form
\[
B_R=R(D+R),\quad\text{retain exactly }B_R\in\Lambda\setminus\{0\};
\quad f_{D,K,R}=(DK-B_R,B_R,D+R).                                     \tag{19}
\]
This is its complete fixed set. In fact permission is exactly \(D^{-1}(A+B)=K\), and the real fixed equation is equivalent to \(B=R(D+R)\). Conversely every H fixed state uniquely recovers \(D,R,K\) and hence (19). These are explicit coordinates with an exact integrality predicate, not a missing choice of a fixed solution. For an integer-indexed algebraic alternative, write \(D=d_0+\mathbf d\), \(B=b_0+\mathbf b\ne0\), and choose \(t\in[0,1)\), \(n\in(0,4)\). Set \(a=d_0+2t\), \(U=a^2+|\mathbf d|^2\). When \(U>0\), retain exactly
\[
tU=(b_0+n)a+\mathbf b\cdot\mathbf d,\quad
nU=(b_0+n)^2+|\mathbf b|^2,\quad R=(B+n)(D+2t)^{-1}\in C\setminus\{0\}. \tag{20}
\]
These equations give \(\operatorname{Re}R=t,N(R)=n\), so \(R^2=2tR-n\) proves \(R^2+RD=B\), and conversely every nonsingular solution of (19) satisfies (20). The omitted \(U=0\) case is exactly \(D=-1,t=1/2,B=-m\), \(m\in\{1,2,3\}\), and
\[
R=\tfrac12+\mathbf v,\quad 0\le v_j<1,\quad |\mathbf v|^2=m-\tfrac14.    \tag{21}
\]
Indeed \(R(D+2t)=B+n\) forces \(B=-n\), with \(n\in(0,4)\cap\mathbb Z\); this proves both exhaustion and the stated singular family. Thus (19), or (20)--(21) with \(A=DK-B\), is a complete exact parameterization including continuous fixed sets.

At every H fixed core its OWN clock is
\[
\lambda_H=2\log\frac{N(D+R)}{N(R)}.                                   \tag{22}
\]
The entire group is \(\lambda_H\mathbb Z\); when \(N(D+R)=N(R)\) it is zero and source/extension isotropy \(\mathbb Z\) survives. For instance \(R=(1+i+j+k)/2,D=-1,B=-1\) gives \(N(R)=N(D+R)=1\). All \((A,-1,D+R)\), \(A\in\Lambda\), are legal H fixed cores with zero clock. Conversely (22) is the exact test for ALL zero-clock cores, not just this example. The family \(D=2,R=r,B=1,A=2K-1\), \(K\in\Lambda\), supplies infinitely many distinct H fixed packets with its own clock \(L_*\). These control multiplicities are not transferred to MAIN.

For O, the fixed memory equations force \(A=B\ne0,D=2\). Its OWN real equation is \(2+R=R^{-1}\), or \((R+1)^2=2\). Writing \(R+1=s+v\), \(s\ge1\), forces \(v=0\) from \(2sv=0\), and then \(R=r\). Consequently its complete fixed set is
\[
f_B^O=(B,B,\alpha),\qquad B\in\Lambda\setminus\{0\}.                   \tag{23}
\]
Its own (7) gives \(\lambda_O=-4\log N(r)=L_*\). These are countably infinitely many distinct fixed packets with the same positive primitive, proved for O independently of the MAIN clock. H, O, and V each keep their own measure, inverse atlas, and full groupoid throughout.

## 7. Fixed-core full incoming, entire groups, and multiplicity

For ANY fixed core \(f\) of ANY one of the four maps, the complete base orbit is
\[
\mathcal B_f=\bigcup_{m\ge0}P_m(f)=\{y:F^m y=f\text{ for some legal }m\}.
\]
The equality follows because the future of \(f\) is constant. Every \(y\in\mathcal B_f\), including nonperiodic incoming states, has source isotropy \(\mathbb Z\), entire clock group \(H_y=\kappa_F(f)\mathbb Z\), and extension isotropy zero when this clock is nonzero, \(\mathbb Z\) when it is zero. For any hitting time \(m\), ALL phases are
\[
h-S_m(y)\pmod{\kappa_F(f)\mathbb Z}.                                  \tag{24}
\]
Larger hitting times change this expression only by an integer multiple of the fixed clock. Thus the packet is the full circle \(\mathbb R/(|\kappa_F(f)|\mathbb Z)\) if nonzero, or a nonperiodic height line \(\mathbb R\) if zero. Choosing a representative phase or a root state does not delete the other phases or create additional packets.

For MAIN and V, with \(f_B\) from (15), and for O with \(f_B^O\) from (23), the complete first incoming list is respectively
\[
((D-1)B,B,D+R_B),\qquad ((D-1)B,B,D+r),\qquad D\in\Lambda\setminus\{0\}.
\]
For V the first list follows from its own \(z^{-1}B=R_B\), which is valid at these fixed cores; MAIN uses \(Bz^{-1}=R_B\). Every digit in these lists is legal by its own inverse formula. In particular \(D=1\) gives \(A=0\), a retained legal incoming; as a target it has no earlier MAIN/O/V predecessor because its first memory is zero. Deeper incoming are precisely the recursion preceding (12), with every intermediate inverse domain checked, not arbitrary concatenations of digits.

For an H core \((A,B,D_0+R_0)\), its complete first incoming list is
\[
(A,B,D+R_0),\quad D\ne0,\quad D^{-1}(A+B)\in\Lambda.
\]
All later layers again use only its own recursion and checks. This includes zero-clock cores and every valid boundary state. Distinct fixed cores have disjoint basins and one packet each when their clock is nonzero; incoming multiplicity is not extra packet multiplicity. Equations (14), (19)--(23) therefore specify complete fixed-core packet multiplicities, including retained zero-clock isotropy, without a higher-period claim.

## 8. Gate assessment, limitations, and decision

| Owner-level item | Supported result and boundary |
| --- | --- |
| T0 | Full Borel owner, exact ordered inverses, sigma-finite measure, every-Borel IMAGE, actual groupoid and extension are established. |
| T1 | The divisor slice and arithmetic-memory feedback are exact; the real signed clock is the owner's four-dimensional inverse Jacobian. Strong naturalness remains OPEN. |
| T2 | Complete fixed sets and their full incoming, kernels, isotropy, entire groups, phases, and packet convention are established. MAIN's actual (17)--(18) violates the necessary target: STOP / FORK. |
| T3 / classical / formal / B | NOT AUDITED / NOT APPLICABLE / UNASSIGNED / NOT INVOKED. |

The same-object ledger remains intact: no clock, orbit, inverse, measure, or multiplicity was borrowed from a control. The stop is not inferred from an empty window or from missing all-prime coverage, but from one proved nonprime MAIN primitive. Higher cycles, spectral data, decay, stationarity, invariant probability, and conservative or Hamiltonian realizations were not investigated. A new architecture would require a fresh frozen card and authorization; none is started here.

## Reproducibility, access, and research-integrity disclosure

Inputs: [candidate card](candidate-card.md), SHA256 `84694a5fc334bec368850e6ea542344ba4723a0aaf39c92fb0e37d39247cd921`, read completely through both EOF markers after CP1 release; the repository's paper template and relevant guidance. Outputs: this proof, [claim ledger](claim-ledger.md), and [package README](README.md). All mathematics above is exact quaternion algebra, differentiation, and Borel change of variables; no scientific code, numerical scan, truncation, external source lookup, or prime data was used. File hashes, line counts, and local-link checks are mechanical verification only.

The author's definition scout read the316/317 cards including outcomes and carried shared361/386/392/396 history and informal pre-freeze algebra; this is not a blind prediction or a novelty/nonconjugacy certificate. The same-author helper `/root/bilateral_transport_review/direct_controls` was assigned only the H/O/V control derivations; its task access was the final100-line402 card, not402 evidence, raw proof, or peers. The main author independently rederived and integrated those controls. This helper is NOT the independent reviewer, and its work is not represented as independent validation. The author read no402 evidence/raw/peer proof and wrote only the three authorized author surfaces.

AI agents supplied mathematical derivation, drafting, and internal checks; the separate repository review process is also AI-assisted internal review. No human or external mathematical verification is certified. Internal review is shared-history NOT_CALIBRATED, not blind or external peer review. ARS guidance was used to separate the frozen owner, exact claims, control ownership, and these access/assistance disclosures. No external publication, funding, or human-subject involvement is claimed. The result is a scoped mathematical STOP / FORK record, not accumulated credit toward a Route pass.

EOF — QDM01 author proof; no higher-period census or new candidate.
