# An owned simplex clock with an empty positive-period ledger

Candidate ID: `ANG-20260924-RDSS01`.
Outcome: `OWNED SIMPLEX CLOCK; EMPTY POSITIVE LEDGER — GLOBAL STOP / FORK`

Paper: `451-reciprocal-divisor-simplex-swap`; batch `TRANSPORT-PACKET-20260924-U`, round 2/5.
Date: 2026-09-24. Status: exact, global, same-owner negative result.
Classical symplectic/suspension fields: NOT APPLICABLE. T3 NOT AUDITED; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.
Internal AI-assisted work: shared history, same model, NOT_CALIBRATED; no human, external, or cross-model verification is certified.

## Abstract

The frozen source is the entire open positive simplex with its original area measure. Two reciprocal integer readings govern a partial rational swap; its two controls remove either divisibility permission or the projective denominator. We prove all actual inverse domains and the prescribed every-point, every-Borel IMAGE identities, including assigned reciprocal cuts. The resulting clock is an endpoint potential difference on every actual history, so its entire isotropy image is zero for all three owners. Separately, a global coordinate-sum argument excludes every source cycle for MAIN and the permission-OFF control, including the latter's zero-quotient branches. The denominator-OFF control retains a continuum of fixed points and two-cycles, all with zero clock, as well as one-step terminal pairs and isolated terminal objects. Complete inverse recursion retains every incoming depth and phase. The required nonempty positive packet ledger fails globally; this is not a general obstruction to arithmetic groupoids or a classification of nonperiodic asymptotics.

## 1. Frozen objects, arithmetic interface, and scope

For each owner separately let
\[
X=\{(x,y)\in\mathbb R^2:x>0,\ y>0,\ x+y<1\},\qquad
\mu=\operatorname{Leb}_2|_X,\quad n=\lfloor1/x\rfloor,\quad d=\lfloor1/y\rfloor.
\]
The usual Borel structure and unnormalized area are fixed. Axes and the line \(x+y=1\) are outside \(X\) from definition, not discarded after testing. Every point of \(X\), including every internal reciprocal cut, remains an object. In particular \(n,d\) are positive integers.
Put \(A=\{z\in X:d\mid n\}\), \(R(x,y)=(y,x)\), and
\[
F_q(x,y)=\left(\frac{y}{1+qx},\frac{x}{1+qx}\right).
\]
The three partial maps are
\[
T_M=F_{n/d}\text{ on }A,\qquad
T_G=F_{\lfloor n/d\rfloor}\text{ on }X,\qquad
T_Q=R\text{ on }A.
\]
The frozen additional source requirements are a positive own denominator where present and an image in \(X\); Proposition 1 proves them without changing admission. Failed sources have units and actual incoming arrows, but no outgoing step and no step clock. There is no terminal reset or absorbing identity step. \(T^0\) is the identity for every object; higher iterates require every intermediate step to be legal.

For integers \(1<D<N\), \(N\ge3\), the point \(z_{N,D}=(1/N,1/D)\) lies in \(X\), since its coordinate sum is at most \(1/3+1/2<1\). Its actual readings are \(n=N,d=D\), and MAIN admission is exactly \(D\mid N\). Thus the lineage is proper-divisor symbolic permission \(\to\) two current reciprocal readings \(\to\) an actual rational geometric update \(\to\) new readings of the successor. This family is not a source restriction. No prime list, selected prime fiber, manually assigned roof, or logarithmic prime datum is an input.

The question is whether this same measured source supplies a nonempty positive primitive ledger with every primitive equal to an ordinary-prime logarithm and at most one packet per prime. Coverage is an additional target, not a substitute for nonemptiness. The frozen global tests are the coordinate sum for \(M,G\) and actual two-step legality for \(Q\); no longer-cycle census is used.

## 2. Type, all inverse branches, and all-point IMAGE

**Proposition 1 (type).** The actual domains are precisely \(A,X,A\) for \(M,G,Q\).

**Proof.** On MAIN, \(q=n/d\ge1\); on \(G\), \(q=\lfloor n/d\rfloor\ge0\), including zero. Thus \(D_q=1+qx>0\). Both output coordinates are positive and their sum is \((x+y)/D_q\le x+y<1\). The swap \(R\) preserves positivity and the sum. This proves every additional geometric guard. It does not imply that an admitted MAIN or \(Q\) source has an admitted successor. \(\square\)

For all positive integers \(n,d\), retain the disjoint Borel cells
\[
I_{nd}=X\cap\left(\frac1{n+1},\frac1n\right]\times
\left(\frac1{d+1},\frac1d\right].
\]
These partition \(X\); some are empty. At a target \(w=(u,v)\in X\), put
\[
\Delta_q(w)=1-qv,\qquad
\theta_q(w)=\left(\frac{v}{\Delta_q(w)},\frac{u}{\Delta_q(w)}\right).
\]
For \(O=M\), enumerate all \(d\mid n\) with \(q=n/d\); for \(O=G\), enumerate all \(n,d\) with \(q=\lfloor n/d\rfloor\). In either case the exact domain is
\[
\Omega^O_{nd}=\{w\in X:\Delta_q(w)>0,\ \theta_q(w)\in I_{nd}\}. \tag{1}
\]
The source-cell condition includes the source simplex inequality, equivalently \(u+(q+1)v<1\). Each enumerated label enforces its own arithmetic rule. Thus (1) includes every frozen source check; it does not impose permission at the target. For \(Q\), enumerate \(d\mid n\) and use
\[
\theta^Q_{nd}(w)=R(w),\qquad
\Omega^Q_{nd}=\{w\in X:R(w)\in I_{nd}\}. \tag{2}
\]
There is no inherited \(\Delta_q\) restriction in (2).

**Proposition 2 (complete inverse and IMAGE).** Equations (1)–(2) are exactly the actual inverse branches. On every point of their domains the prescribed inverse-germ densities are
\[
J^M_{nd}(u,v)=J^G_{nd}(u,v)=\Delta_q(u,v)^{-3},\qquad J^Q_{nd}=1. \tag{3}
\]
For every Borel \(E\) in an actual branch domain,
\[
\mu(\theta^O_{nd}E)=\int_E J^O_{nd}\,d\mu. \tag{4}
\]
All densities in (3) are finite and strictly positive, including at assigned cell endpoints.

**Proof.** If \(w=F_q(x,y)\), then \(1-qv=(1+qx)^{-1}>0\), so \(\theta_q(w)=(x,y)\). Conversely, if (1) holds, \(1+q\,v/\Delta_q=1/\Delta_q\), and substitution gives \(F_q\theta_q(w)=w\). The reconstructed cell selects precisely the required actual \(q\). Every true preimage has its unique actual pair of floor labels, hence occurs in this list; reconstructed sources, not quotient labels alone, are the deduplication rule. The two identities for (2) follow from \(R^2=\mathrm{id}\), subject to its reconstructed source admission.

All branch domains are Borel. For \(q>0\), \(F_q\) is a smooth diffeomorphism from the positive quadrant onto \(\{(u,v):u>0,\ 0<v<1/q\}\); the displayed inverse proves the statement directly. For \(q=0\) it is the positive-quadrant swap. On these open domains,
\[
DF_q=
\begin{pmatrix}-qy/D_q^2&1/D_q\\1/D_q^2&0\end{pmatrix},
\qquad
D\theta_q=
\begin{pmatrix}0&1/\Delta_q^2\\1/\Delta_q&qu/\Delta_q^2\end{pmatrix}.
\]
Consequently \(\det DF_q=-D_q^{-3}\) and \(\det D\theta_q=-\Delta_q^{-3}\); \(R\) has determinant \(-1\). The ordinary change-of-variables identity on these open diffeomorphisms applies to every Borel subset of the actual restricted domains, proving (4). In particular it applies to sets on cell cuts, and to null sets; no ratio of set masses is used. Borel images are Borel because the ambient branch is a homeomorphism. The assigned germ fixes the value at every cut, without claiming that the full piecewise map is continuous across a cut. Positivity and finiteness follow from \(\Delta_q>0\). \(\square\)

The signed step clocks, in the frozen IMAGE orientation, are therefore
\[
\kappa_M(z)=-3\log(1+(n/d)x),\qquad
\kappa_G(z)=-3\log(1+\lfloor n/d\rfloor x),\qquad
\kappa_Q(z)=0, \tag{5}
\]
on their own legal sources only. These are derived from \(-\log J_{\mathrm{actual}}(Tz)\), not from a chosen roof. MAIN clocks are strictly negative; \(G\) retains its zero clocks when \(q=0\). A negative step is not by itself an absence-of-packets argument, because the groupoid also contains inverses.

## 3. Whole histories, exact kernels, incoming, and phases

All notation in this section is independently instantiated for each \(T_O\). Its actual Borel groupoid is
\[
\mathcal G_O=\{(z,r-s,w):r,s\ge0,\ T_O^rz=T_O^sw\text{ legally}\},
\quad s(z,k,w)=w,\quad r(z,k,w)=z. \tag{6}
\]
Equal triples, not merely common endpoints or clocks, are identified. Units are \((z,0,z)\), inversion changes \((z,k,w)\) to \((w,-k,z)\), and multiplication adds lags.
To verify closure without padding a terminal, compose witnesses \(T^rz=T^sw\), \(T^pw=T^qv\). If \(p\ge s\), continue the first equality for the already legal \(p-s\) steps along \(w\), obtaining \(T^{r+p-s}z=T^qv\). If \(p<s\), continue the second equality for the already legal \(s-p\) steps, obtaining \(T^rz=T^{q+s-p}v\). Both give lag \(r-s+p-q\). Existence domains of finite iterates are Borel by induction; (6) is a countable union of Borel equality sets in \(X\times\mathbb Z\times X\).

Let \(\sigma(z)=x+y\), \(V(z)=3\log\sigma(z)\), and let \(S_r(z)\) sum the \(r\) legal step clocks, with \(S_0=0\). For \(M,G\), \(\sigma(Tz)=\sigma(z)/(1+qx)\); for \(Q\), \(\sigma(Tz)=\sigma(z)\). Equation (5) gives, separately for all three owners,
\[
\kappa(z)=V(Tz)-V(z),\quad
S_r(z)=V(T^rz)-V(z),\quad
c(z,r-s,w)=S_r(z)-S_s(w)=V(w)-V(z). \tag{7}
\]
Thus the prescribed clock descends to every actual triple and is additive. In particular the actual forward arrow \((Tz,-1,z)\) has clock \(V(z)-V(Tz)=-\kappa(z)\), as required. There is no limiting sum or terminal clock.

The same version is compatible with complete finite-history IMAGE. Fix actual label itineraries witnessing a branch from \(w\) to \(z\), \(T^rz=T^sw\). On its exact Borel domain this branch is the own inverse of \(T^r\) composed with the own forward \(T^s\). Successive applications of (4), or the determinant chain rule on these fixed-label germs, give its forward IMAGE density \(\exp(-S_r(z)+S_s(w))=\exp(-c(z,r-s,w))\). This proves the every-Borel identity on every such restricted branch, including cuts. Equation (7) makes its all-point density independent of alternative witnesses for the same actual triple.

Here is an unrestricted, exact incoming algorithm. Let \(P^O_0(t)=\{t\}\) and
\[
P^O_{j+1}(t)=
\bigcup_{v\in P^O_j(t)}
\{\theta^O_{nd}(v):v\in\Omega^O_{nd},\ (n,d)\text{ an allowed own label}\}. \tag{8}
\]
All labels and all finite depths are included, with source-based deduplication. Propositions 1–2 and induction prove \(P^O_j(t)=\{z:T_O^jz=t\text{ legally}\}\). Hence the entire set of arrows incoming to the object \(t\) is
\[
\{(t,r-j,z):r\ge0,\ T_O^rt\text{ legal},\ j\ge0,\ z\in P^O_j(T_O^rt)\}. \tag{9}
\]
Taking inverses gives every outgoing arrow. This includes every terminal's incoming histories by taking \(r=0\), and every basin at every depth. No bound on labels or depth, removal of null sources, or addition of infinite-limit endpoints occurs.

The lag, clock, and joint kernels have the following complete descriptions:
\[
\begin{aligned}
K_{\mathrm{lag}}^O
 &=\bigcup_{j\ge0,\ t\in X}\{(z,0,w):z,w\in P^O_j(t)\},\\
K_c^O&=\{(z,k,w)\in\mathcal G_O:\sigma(z)=\sigma(w)\},\\
K_{\mathrm{joint}}^O
 &=\bigcup_{j\ge0,\ t\in X}
 \{(z,0,w):z,w\in P^O_j(t),\ \sigma(z)=\sigma(w)\}. \tag{10}
\end{aligned}
\]
For \(M,G\), equations (1) and (8) specify these sets without a finite census or any unsolved branch choice. For \(Q\), the more explicit simplification \(K_{\mathrm{lag}}^Q=K_{\mathrm{joint}}^Q=X\) (units) and \(K_c^Q=\mathcal G_Q\) follows below. Vanishing isotropy clock does not assert that \(K_c^M\) or \(K_c^G\) is the entire groupoid.

Write \(I_O(z)=\{k:(z,k,z)\in\mathcal G_O\}\). Equation (7) proves for every object, independently of its source-period classification,
\[
H_O(z)=c(\mathcal G_{O,z}^{z})=\{0\}. \tag{11}
\]
The extension has objects \(X\times\mathbb R\) and arrows \((w,h)\to(z,h+c(z,k,w))\). At every \((z,h)\) its isotropy consists of all \((z,k,z)\) with \(k\in I_O(z)\): none is removed by a nonzero clock, since (11) holds. The source isotropy itself is determined in §§4–5.

To retain all phases explicitly, let \(\mathcal O\) be any full source orbit, as enumerated by (9). For every \(\eta\in\mathbb R\), precisely one extension orbit over \(\mathcal O\) is
\[
\mathcal L_{\mathcal O,\eta}=\{(z,\eta-V(z)):z\in\mathcal O\}. \tag{12}
\]
Equation (7) proves both containment and connectivity, and every extension point is in exactly such a set. Height translation sends \(\eta\) to \(\eta+t\), so its stabilizer is exactly \(\{0\}\). This is an assertion about orbit sets, not a Hausdorff quotient, a selected representative, or a topological flow model. For \(Q\), ordinary height \(h\) itself is constant along each extension orbit, since every own clock is zero.

Only an entire image group \(H=L\mathbb Z\), \(L>0\), would supply a positive primitive period \(L\), with positive integer repeats. Equation (11) excludes such a period for every source orbit and every phase, for all three owners. The source and extension isotropy retained below is not deleted or counted as a positive-time packet.

## 4. MAIN and permission-OFF: global source-return exclusion

**Proposition 3.** Neither \(M\) nor \(G\) has any legal source periodic point or eventually periodic source point. For every object their source isotropy and extension isotropy are trivial.

**Proof for MAIN.** On each legal step \(q=n/d\ge1\) and \(x>0\), so \(\sigma(T_Mz)<\sigma(z)\). A finite legal cycle would give a strict chain back to the same sum, which is impossible. An eventual cycle would be a cycle at its entry point and is also impossible. If \(T^rz=T^sz\) with \(r>s\), the point \(T^sz\) would lie on such a legal cycle of length \(r-s\). Thus \(I_M(z)=\{0\}\), including terminals. The extension statement follows from §3. \(\square\)

**Proof for \(G\).** The sum never increases. Equality at a step is equivalent to \(q_G=0\), because \(x>0\); this is exactly \(n<d\). Such a step is the actual swap \(R\), so its successor has actual readings \((d,n)\), including on the assigned reciprocal endpoints. Its next quotient is \(\lfloor d/n\rfloor\ge1\). That step is legal by Proposition 1 and strictly decreases the sum. Therefore no two consecutive steps have equality. Any legal cycle would force equality at all its steps (otherwise a nonincreasing sum could not return); periodic repetition would then contradict the preceding two-step observation. This includes a putative one-step cycle. Eventual periodicity and nontrivial isotropy are excluded by the same argument used for MAIN. \(\square\)

The \(G\) proof uses the actual successor readings, not an independently repeated zero-quotient label. These arguments do not claim finite termination for MAIN, convergence of either owner, or a classification of infinite nonperiodic itineraries. All such sources and their incoming in (8)–(9) remain present.

## 5. Denominator-OFF: every actual return and terminal orbit

**Proposition 4.** For \(Q\), the full two-step-legal set is
\[
E=\{z\in X:n=d\}.
\]
Its fixed set is \(\{(t,t):0<t<1/2\}\). Its exact period-two set is \(E\setminus\{x=y\}\). Outside \(E\), every nontrivial source orbit is a single legal edge from an admitted source to a terminal target; all remaining source orbits are isolated terminals.

**Proof.** A first legal step requires \(d\mid n\), and the swap exchanges the actual readings. The second step is legal precisely when \(n\mid d\) also holds. Positivity of \(n,d\) makes the conjunction equivalent to \(n=d\). The swap has square the identity on this entire set; it fixes exactly \(x=y\), where membership in \(X\) is \(0<x<1/2\), and every other point of \(E\) has least period two.

For an arbitrary target with readings \((n,d)\), its only possible predecessor is \(Rz\). Its source readings are \((d,n)\), so this predecessor is actual exactly when \(n\mid d\). If \(d\mid n\) and \(n>d\), \(z\) is admitted, has no predecessor, and maps to the terminal \(Rz\). If \(n\mid d\) and \(d>n\), \(z\) is that terminal, with the unique admitted predecessor \(Rz\). If neither integer divides the other, \(z\) has neither outgoing step nor predecessor and is an isolated terminal. The equality case has no additional predecessor outside its one- or two-point orbit, because \(R\) is injective. These cases exhaust \(X\). \(\square\)

This also makes every depth of (8) explicit for \(Q\). On \(E\), \(P_j^Q(z)=\{R^jz\}\) for all \(j\). At an unequal-divisibility terminal, \(P_1^Q(z)=\{Rz\}\) and \(P_j^Q(z)=\varnothing\) for \(j\ge2\). At an admitted unequal-divisibility source or an isolated terminal, \(P_j^Q(z)=\varnothing\) for every \(j\ge1\). In every case \(P_0^Q(z)=\{z\}\).

All legal iterates of \(Q\) are injective on their actual domains. Thus \(T_Q^jz=T_Q^jw\) forces \(z=w\), proving that its lag kernel is just the unit space. All its arrows preserve \(\sigma\), so its clock kernel is the entire groupoid and the joint kernel is the unit space. More explicitly,
\[
I_Q(z)=
\begin{cases}
\mathbb Z,&z=(t,t),\quad0<t<1/2,\\
2\mathbb Z,&z\in E,\quad x\ne y,\\
\{0\},&z\notin E.
\end{cases} \tag{13}
\]
At a fixed point the lag group is all integers. On a two-cycle, if its points are written \(z_a\), \(a\in\mathbb Z/2\mathbb Z\), with \(Rz_a=z_{a+1}\), the arrows \((z_a,k,z_b)\) have precisely \(k\equiv b-a\pmod2\). This labels the full orbit; it does not select one state and discard the other. For a finite terminal pair \(a\to b=Ra\), the nonunit arrows are \((b,-1,a)\) and its inverse \((a,1,b)\), with no nonunit isotropy. An isolated terminal has only its unit.

Equations (11)–(13) retain all ineffective source isotropy in the extension at every real height. The least source lags one and two have all their integer repeats, but their clock images are zero and do not supply a positive primitive time. Distinct source cycles, terminal pairs, isolated objects, and all their real phases are retained; none are merged by their common zero clock.

## 6. Global decision and owner boundaries

| Owner | Actual source behavior | Source isotropy | Entire clock image | Positive primitive packets |
| --- | --- | --- | --- | --- |
| MAIN \(M\) | No cycle or eventual cycle; all legal histories and terminals retained | \(\{0\}\) everywhere | \(\{0\}\) everywhere | Empty |
| Permission-OFF \(G\) | No cycle or eventual cycle; \(q=0\) cannot persist for two steps | \(\{0\}\) everywhere | \(\{0\}\) everywhere | Empty |
| Denominator-OFF \(Q\) | All fixed/two-cycles in \(E\), finite terminal pairs and isolated terminals | (13) | \(\{0\}\) everywhere | Empty |

T0's frozen Borel carrier, full inverse architecture, original-area all-point IMAGE, and actual extension are established. The proper-divisor interface and derived clock are owned by that same source. Nevertheless arithmetic T1 is NOT PASSED: the necessary nonempty positive ledger fails globally. T2's actual source/packet/repetition accounting is settled, but it does not meet the requested prime-packet target. “Every positive primitive is a prime logarithm” and uniqueness would be vacuous on an empty ledger, not positive evidence. Prime coverage fails as well.

The main decision is **STOP / FORK**. This is a global result from the frozen discriminators, not an extrapolation of a finite window. Q's source returns do not repair MAIN, and the endpoint-potential identity is not permission to replace the measure, clock, or carrier. Strong naturalness and PROVES_TOO_MUCH remain OPEN design assessments, not assumed mathematical inputs. No symplectic/conservative physical realization, operator, trace, zeta, or formal Route coordinate is constructed. T3 is NOT AUDITED; classical A0–A2 fields are NOT APPLICABLE; formal Route coordinates remain UNASSIGNED and Route B NOT INVOKED. No new candidate or further round is created here.

## 7. Provenance, verification, and limitations

The sole new scientific input was the [candidate card](candidate-card.md), personally read at original lines 1–93 through its provided and measured EOF (93 lines). Its original-prefix SHA-256 is `065e2b6753f85f74904348af8edfd75bfdae6ad7860463d0bb59739dd4bf3f4d`. Root supplied the formula and an informal global-feasibility thought before freeze; this author supplied inverse-domain and discriminator design. This was not blind discovery or sealed preregistration.

During design, the only two old-card definition reads were [398](../398-projective-plane-admission/candidate-card.md), lines 1–30 (not EOF; measured total 88), prefix SHA-256 `9f7ace5d578d5dcdd9792bf55ed33eb391ebe2b81862777ba8d1890c8a8b5e12`, and [395](../395-simultaneous-content-return/candidate-card.md), lines 1–39 (not EOF; measured total 109), prefix SHA-256 `3621519d2234bbdf4739d5cbbcc7ddd7fef8089e8277fd9e479a5b1e1ecbd0c2`. Heading-only search exposed their Outcome titles at 398:74 and 395:95, not outcome status/body in that read. These prefixes supplied definitions and proposed obligations, not imported proofs.

398 supplies a full-projective-plane, round-measure conditional projective class; 395 instead uses \(\lfloor1/x\rfloor,\lfloor y/x\rfloor\) and gcd-normalized remainder transport. The present displayed owner has a different carrier/measure and exact arithmetic law, but no global novelty or nonconjugacy is claimed. This author previously authored 395; shared historical outcomes were already exposed. No old proof was reread or transferred.

A bounded same-model author aid, `rdss_q_author_aid`, received only the original 451 card, lines 1–93, and returned a Q-only derivation of its source/incoming/isotropy and IMAGE bookkeeping. This was author assistance, not an independent reviewer seat. No reviewer scope, raw proof, answer, or other current manuscript was read by this author. The author refreshed the ARS router and academic-paper workflow, using their scoped writing, evidence, and disclosure discipline rather than expanding to literature or publication.

All scientific work here is exact symbolic derivation written in this paper. No numerical orbit search, scientific program, web/API query, external upload, Git operation, PDF, or operator computation was used. Read receipts used `nl -ba ... | sed -n '1,93p'`, `head -n 93 ... | sha256sum` and `wc -l`; final author checks use full EOF reads, SHA-256, and text/link validation only. Source asymptotics outside the proved return statements and topological properties of the orbit-set quotient are not claimed.

Evidence index: [frozen card](candidate-card.md), [claim ledger](claim-ledger.md), [package overview](README.md). Root separately owns card outcome append, internal review integration, and batch records; these are not author self-certification.

### Research declarations

Data availability: no empirical dataset was used; the frozen definitions, exact proofs, and local provenance are supplied in this package. Ethics: no human participants, personal data, or animal subjects were involved. Contributions: AI agents supplied candidate-design assistance, mathematical derivation, drafting, and bounded author checking; root coordinates separate internal review and integration. AI assistance is explicit, and no human/external verification is certified. Internal same-model shared-history work remains NOT_CALIBRATED. Funding and conflicts of interest: no author funding or conflict declarations were supplied; none is inferred. No external venue, submission, or publication is claimed.
