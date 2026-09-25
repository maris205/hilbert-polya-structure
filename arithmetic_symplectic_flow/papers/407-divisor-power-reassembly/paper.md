# Divisor-power reassembly owns its clock but retains composite fixed primitives

Candidate ID: `ANG-20260923-DPR01`. Paper407, version1, 2026-09-23.
Batch `NONLINEAR-PACKET-20260923-L`, round3/5.
Outcome: `OWNED REASSEMBLY CLOCK; COMPOSITE FIXED PRIMITIVES — STOP / FORK`
Type: Borel partial arithmetic map, counting–Lebesgue IMAGE, actual lag groupoid.
Status: exact owner and complete fixed-window result; necessary MAIN target fails.
Strong naturalness / arbitrary-encoding risk: OPEN. T3: NOT AUDITED.
Classical fields: NOT APPLICABLE. Formal Route: UNASSIGNED. Route B: NOT INVOKED.

## Abstract

The frozen reassembly map lets a real digit select an actual divisor of a retained integer; the quotient determines a power map and a second digit grid, whose digit writes back the next integer. We establish the full ordered inverse atlas, every-Borel IMAGE with a prescribed all-point derivative version, the actual groupoid, its kernels, whole clock groups, and all incoming phases. MAIN has fixed packets of primitive length \(2\log q\) for every integer \(q\ge2\), as well as a continuum of fixed packets of length \(\log(1+\sqrt{17})\). In particular the retained boundary point \((2,1/4,0)\) has entire clock group \(\log4\,\mathbb Z\), so the ordinary-prime target fails on MAIN itself. Three controls are proved with their own inverses, clocks, and complete fixed sets. A general cycle identity is derived, not a census of higher periods.

## 1. Frozen owner, lineage, and scope

The input is the [105-line frozen card](candidate-card.md), unchanged by this author. The full standard Borel carrier and sigma-finite measure are
\[
X=\mathbb N_0\times[0,1]^2,\qquad
\mu=\#_{\mathbb N_0}\otimes\operatorname{Leb}_2.
\]
Each memory slice has mass \(1\); no probability or invariant-measure claim is made. States with \(n=0\), \(x=1\), or \(y=1\) are terminal. Else \(n\ge1\), and set
\[
d=1+\lfloor nx\rfloor,\quad r=nx-(d-1).
\]
MAIN additionally requires \(r>0\) and \(d\mid n\). Then put
\[
q=n/d,\quad e=1+\lfloor qy\rfloor,\quad s=qy-(e-1),\qquad
T(n,x,y)=\left(d+e,r^q,\frac{d-1+s}{d}\right).                         \tag{1}
\]
Thus \(1\le d\le n\), \(0<r<1\), \(1\le e\le q\), and \(0\le s<1\) on each legal branch. All other points remain terminals, with the identity iterate and every actual incoming, not absorbing loops. This includes units, zero memory, square faces, and all digit cuts; \(r=0\) is terminal whereas \(s=0\) is legal. For example MAIN sends \((1,1/2,0)\) to the terminal cut point \((2,1/2,0)\), so terminal does not mean no incoming.

For a fixed integer \(n\) and \(1<d<n\), the whole open digit strip \((d-1)/n<x<d/n,\ 0\le y<1\) is legal exactly when \(d\mid n\). This is the exact proper-divisor interface, not a gcd relaxation or a prime label. Unit strips remain. The quotient changes the real power and the second digit grid; that current geometric digit changes the next integer. This realizes divisor-symbolic admissibility \(\to\) actual two-coordinate feedback, not a conservative/symplectic realization.

The three distinct controls retain their OWN full \(X,\mu\). L has MAIN's domain and update but replaces \(r^q\) by \(r\). H has MAIN's domain and geometry but replaces the output integer \(d+e\) by \(n\). G deletes \(d\mid n\), sets \(q=\lfloor n/d\rfloor\), and otherwise uses (1). We write \(F\) for whichever owner is under discussion; no clock or packet conclusion is transferred.

The frozen target requires every MAIN positive primitive to equal \(\log p\) for an ordinary integer prime, at most one packet per prime, and a nonempty positive ledger; ultimately every prime must occur. A wrong MAIN primitive suffices to stop. An empty bounded window would not prove a global failure. Only ownership and COMPLETE fixed sets are enumerated here; no higher-period search or parameter tuning is performed.

## 2. Complete inverses and their measured identities

For T, L, H, source branches are indexed by \(d,q\ge1,\ 1\le e\le q\), with \(n=dq\). For G they are indexed by \(n\ge1,\ 1\le d\le n,\ q=\lfloor n/d\rfloor,\ 1\le e\le q\). In each case the source cell is
\[
B_\alpha=\{n\}\times\left(\frac{d-1}{n},\frac d n\right)
                     \times\left[\frac{e-1}{q},\frac e q\right).       \tag{2}
\]
These Borel cells partition the legal domain, including the assigned horizontal cuts. The target memory is \(m=d+e\), except H where \(m=n\). Its complete branch image is
\[
E_\alpha=\{m\}\times(0,1)\times[1-1/d,1).
\]
At \((m,u,v)\in E_\alpha\), define \(s=dv-(d-1)\) and
\[
I_\alpha(m,u,v)=
\left(n,\frac{d-1+r}{n},\frac{e-1+s}{q}\right),\qquad
r=u^{1/q}\ (T,H,G),\quad r=u\ (L).                                  \tag{3}
\]
All indices are enumerated, without truncation. H has no branch at \(m=0\); G does not impose \(n=dq\). The inequalities in \(E_\alpha\) ensure \(0<r<1,\ 0\le s<1\), hence the source floors recover exactly \(d,e\), and the stated permission holds by the indexing rule. Substitution gives \(F I_\alpha=\mathrm{id}\). Conversely a legal source determines its unique \(n,d,e,q\); solving its real equations gives (3), proving \(I_\alpha F=\mathrm{id}\) on (2) and exhaustion. Different source cells give distinct actual predecessors. No extra inverse-word arrows are created.

All maps and domains are Borel. With indices fixed, (3) extends real-analytically to \(u>0,\ v\in\mathbb R\), providing the prescribed derivative version even at an actual lower \(v\)-face. Direct differentiation gives the diagonal real inverse derivatives
\[
\frac{\partial x}{\partial u}=\frac{1}{nq}u^{1/q-1},\qquad
\frac{\partial y}{\partial v}=\frac d q\quad(T,H,G);
\qquad \frac{\partial x}{\partial u}=\frac1n\quad(L).
\]
Therefore the OWN inverse Jacobians are
\[
J_T=J_H=q^{-3}u^{1/q-1},\quad J_L=q^{-2},\quad
J_G=\frac{d}{nq^2}u^{1/q-1}.                                        \tag{4}
\]
They are positive and finite at EVERY actual inverse point. No value at a null cut is chosen from an unspecified almost-everywhere class. The unique source cell selects \(\alpha(\xi)\); define \(\kappa_F(\xi)=-\log J_{\alpha(\xi)}(F\xi)\) on legal steps.

For every Borel \(A\subset E_\alpha\), real change of variables on the analytic inverse, restricted to the half-open rectangle, proves
\[
\mu(I_\alpha A)=\int_A J_\alpha\,d\mu.                                \tag{5}
\]
On the memory coordinate, a fixed branch sends its single source register to its single target register, a bijection of two singleton counting sets with mass \(1\); it has no additional continuous or lattice-index determinant. Countable unions of slices are handled by their countable branch partition, not by declaring overlapping target images disjoint.

Explicitly, for arbitrary Borel \(A\) in the legal domain, let
\[
N_A(z)=\sum_\alpha {\bf1}_{E_\alpha}(z)
                       {\bf1}_{A}(I_\alpha z).
\]
Each summand is zero off its branch domain. Then \(F(A)=\{z:N_A(z)>0\}\), so \(\mu(F(A))=\int{\bf1}_{N_A>0}\,d\mu\). By (5), its inverse change of variables, and nonnegative summation,
\[
\int N_A\,d\mu=\sum_\alpha\mu(F(A\cap B_\alpha))
              =\int_A e^{\kappa_F}\,d\mu.                            \tag{6}
\]
This counts multiplicity only where intended; the first formula counts the full image union once. All identities allow infinite measure.

At a legal source, using its OWN branch in (4),
\[
\begin{aligned}
\kappa_T=\kappa_H&=3\log q+(q-1)\log r,\\
\kappa_L&=2\log q,\\
\kappa_G&=\log(nq^2/d)+(q-1)\log r.
\end{aligned}                                                       \tag{7}
\]
These are real clocks, not asserted positive stepwise. There is no step clock at a terminal. In particular zero-clock steps must not be confused with zero cycle clock or absent source isotropy.

Precisely, T/H have \(\kappa=0\) at every legal \(q=1\) step and, for \(q>1\), exactly at \(r=q^{-3/(q-1)}\). L has zero clock exactly when \(q=1\). G has zero clock for \(q=1\) exactly when \(n=d\), and for \(q>1\) exactly at \(r=(d/(nq^2))^{1/(q-1)}\). These follow directly from (7), within the respective legal domains; all such point values are retained.

## 3. Actual groupoid, complete kernels, and full extension

Put \(A_F=e^{\kappa_F}\) using (7), and, for every legal length \(a\ge0\),
\[
K_a(\xi)=\prod_{j<a}A_F(F^j\xi),\quad S_a=\log K_a,\quad K_0=1.
\]
Length zero is valid at every object. A positive length requires only its constituent steps to exist; the endpoint may be terminal. For each owner the actual groupoid and proposed clock are
\[
\mathcal G_F=\{(\xi,a-b,\eta):F^a\xi=F^b\eta,\ a,b\ge0\text{ legal}\},
\qquad c_F=\log\frac{K_a(\xi)}{K_b(\eta)}.                            \tag{8}
\]
Source is \(\eta\), range \(\xi\), lag is retained, and equal triples are identified. Two witnesses for the same triple differ by a common increment of their lengths; their added factors follow the same common future and cancel. Thus \(c_F\) descends. For composition, extend the shorter history at the common middle object to the longer legal history; the common intermediate sums cancel. This proves additivity and the inverse sign rule. Countable Borel equality loci define the groupoid; the inverse atlas gives countable source fibres. On finite history charts, the chain rule and (5) give inverse IMAGE \(e^{-S_a}\); on actual branch-pair charts the range/source IMAGE is \(e^{-c_F}\). These retain the prescribed point versions.

The following are the FULL kernels; the indicated witnesses must always be legal and belong to (8):
\[
\ker c_F=\{(\xi,a-b,\eta):K_a(\xi)=K_b(\eta)\},
\]
\[
\ker\ell=\{(\xi,0,\eta):F^a\xi=F^a\eta\text{ for some }a\},\qquad
\ker c_F\cap\ker\ell
=\{(\xi,0,\eta):F^a\xi=F^a\eta,\ K_a(\xi)=K_a(\eta)\text{ for some }a\}.
                                                                        \tag{9}
\]
These are exhaustive, witness-independent criteria, not a selected subgroup. The lag kernel is not assumed to consist only of units: for example distinct H inverse branches with the same \(d,q\) and different \(e\) have the same target and Jacobian, giving arrows in both kernels.

A source has nonzero isotropy exactly when its full forward state eventually enters a cycle. If that cycle has least source period \(k_0\), then
\[
\mathcal G_{F,\xi}^{\xi}=k_0\mathbb Z,\qquad
c_F(jk_0)=j\Lambda,\qquad H_\xi=\Lambda\mathbb Z,\quad
\Lambda=\sum_{i=0}^{k_0-1}\kappa_F(f_i).                              \tag{10}
\]
Indeed a nonzero isotropy witness repeats a forward state. Least period then forces and supplies precisely these lags, while transient sums cancel. Otherwise source isotropy and \(H_\xi\) are zero, including finite terminal-ending histories. No higher cycles are being enumerated in this structural statement.

All \(X\times\mathbb R_h\) remain extension objects, with \((\eta,h)\to(\xi,h+c_F)\). Extension isotropy is \(\{jk_0:j\Lambda=0\}\), hence zero for \(\Lambda\ne0\), the full \(k_0\mathbb Z\) for \(\Lambda=0\), and zero off eventual cycles. Height translation acts on the orbit SET, with stabilizer exactly the ENTIRE \(H_\xi\). Thus the positive primitive is \(|\Lambda|\) when nonzero; \(H=0\) has no positive primitive but does not erase ineffective source isotropy. No positive roof, smooth quotient, or invariant flow measure is asserted.

## 4. General remainder ledger, without a higher-period census

For the power owners T, H, G, write \(x_j\) for the first real coordinate. Along a legal step, \(x_{j+1}=r_j^{q_j}\) and \(n_jx_j=d_j-1+r_j\). Hence
\[
e^{\kappa_F(F^j\xi)}
=B_j\,\frac{x_{j+1}}{x_j},\qquad
B_j=\frac{q_j^2(d_j-1+r_j)}{d_jr_j}
   =\frac{q_j^2}{d_j}\left(1+\frac{d_j-1}{r_j}\right).                \tag{11}
\]
All these \(x_j\) are positive. For a nonempty legal history the coordinate ratio telescopes; for a cycle it cancels completely:
\[
\Lambda=\sum_{j<k_0}\log B_j\quad(T,H,G),\qquad
\Lambda=2\sum_{j<k_0}\log q_j\quad(L).                               \tag{12}
\]
Because \(0<r_j<1\), \(B_j\ge1\), with equality exactly when \(d_j=q_j=1\). In T/G this would force \(n_j=1\) at every cycle step, but the next integer is \(2\); therefore every actual T/G cycle has positive clock. In H, an all-unit cycle is exactly a point of the identity sheet \(n=1,\ 0<x<1,\ 0\le y<1\). For L a zero cycle would require every \(q_j=1\), giving \(n_{j+1}=n_j+1\), impossible on a cycle. Thus all actual L cycles also have positive clock, and H's zero-cycle case is precisely that sheet. These are consequences conditional on the existence of an actual cycle, plus the explicit H sheet; they assert neither existence nor classification of higher periods.

## 5. Complete MAIN, L, and G fixed sets

For MAIN or L a fixed integer obeys \(dq=d+e\), so \(e=d(q-1)\) with \(1\le e\le q\). This forces either \(d=1,\ q\ge2,\ e=q-1,\ n=q\), or \(d=q=e=2,\ n=4\). No \(q=1\) case survives.

For MAIN's \(d=1\) case the real fixed equation gives \(r^q=r/q\), hence the unique \(r=q^{-1/(q-1)}\). The second equation gives \(y=s=(q-2)/(q-1)\). For its \(d=q=e=2\) case, \(r^2=(1+r)/4\) has the unique root
\[
\rho=\frac{1+\sqrt{17}}8\in(0,1),
\]
and the second real coordinate is unchanged throughout \(1/2\le y<1\). Consequently the COMPLETE MAIN fixed set is
\[
a_q=\left(q,q^{-q/(q-1)},\frac{q-2}{q-1}\right)\quad(q\ge2),
\qquad b_t=(4,\rho^2,t)\quad(1/2\le t<1).                            \tag{13}
\]
The two parts are disjoint digit cells. Substitution verifies all floor, divisibility, and endpoint conditions. Their OWN cycle clocks, from (7), are
\[
\kappa_T(a_q)=2\log q,\qquad
\kappa_T(b_t)=\log(1+\sqrt{17}).                                     \tag{14}
\]
Each fixed core has full source isotropy \(\mathbb Z\), so (10) makes these the actual least positive primitive times, not selected repetitions. In particular
\[
f_*=(2,1/4,0)=a_2,\qquad H_{f_*}=\log4\,\mathbb Z.                    \tag{15}
\]
The lower-face value \(y=0\) is an actual legal point and uses (4)'s prescribed derivative. Since \(4\) is not an ordinary prime, MAIN fails the necessary target. More generally every \(a_q\) has composite multiplier \(q^2\); the continuum \(b_t\) has the noninteger multiplier \(1+\sqrt{17}\). No deletion, rescaling, or equal-time merger is allowed.

For L, the SAME integer classification must be combined with its OWN real equation \(r=(d-1+r)/(dq)\). The \(d=1\) case forces \(r=0\), excluded by its frozen domain. The remaining case gives \(r=1/3\). Thus
\[
\operatorname{Fix}(T_L)=\{(4,1/3,t):1/2\le t<1\},\qquad
\kappa_L=\log4.                                                     \tag{16}
\]
Its continuum of packets follows from its own inverse and clock, not MAIN's power equation.

For G a fixed integer satisfies \(n=d+e,\ q=\lfloor(d+e)/d\rfloor,\ 1\le e\le q\), without assuming \(n=dq\). If \(d=1\), then \(q=e+1=n\). If \(d\ge2,e<d\), then \(q=e=1,n=d+1\). If \(d\ge2,e\ge d\), the inequalities \(d(q-1)\le e\le q\) force \(d=q=e=2,n=4\). The middle case has \(s=y\) and fixed equation \(y=(d-1+y)/d\), forcing the forbidden boundary \(y=1\). The other two cases are precisely (13), including their full \(t\)-interval. At those cores, G's OWN formula (7) gives exactly (14). Therefore
\[
\operatorname{Fix}(T_G)=\{a_q:q\ge2\}\cup\{b_t:1/2\le t<1\}.           \tag{17}
\]
This equality of fixed sets does not identify the full maps or remove G's nondivisible branches.

## 6. Complete H fixed set, including all zero-clock cores

H holds \(n=dq\) fixed. Its real fixed equations are
\[
dq\,r^q=d-1+r,\qquad (q-d)y=e-d,\qquad
y\in[1-1/d,1),\quad 1\le e\le q.                                   \tag{18}
\]
The interval is exactly \(0\le s=dy-d+1<1\); with (18), it also recovers the required second source digit. If \(q=1\), the first equation is \((d-1)(r-1)=0\). Only \(d=1\) survives, and gives the entire fixed identity sheet
\[
U=\{(1,x,y):0<x<1,\ 0\le y<1\},\qquad \kappa_H=0.                    \tag{19}
\]
If \(q\ge2\), there is exactly one root \(\rho_{d,q}\in(0,1)\) of the first equation: after division by \(r\), the left side \(dq\,r^{q-1}\) is strictly increasing and the right side \(1+(d-1)/r\) is nonincreasing; their endpoint inequalities are opposite. This also covers \(d=1\), where \(\rho_{1,q}=q^{-1/(q-1)}\).

For \(q<d\), the second equation at \(y<1\) would give \(e=q+(d-q)(1-y)>q\), impossible. For \(q=d\), it forces \(e=d\) and allows the whole interval. For \(q>d\), set \(e=q-j\). Then
\[
y=1-\frac{j}{q-d},\qquad s=1-\frac{dj}{q-d},\qquad
1\le j\le\lfloor q/d\rfloor-1.                                     \tag{20}
\]
The interval is nonempty precisely for \(q\ge2d\). Thus, besides \(U\), the COMPLETE H fixed set consists of
\[
(d^2,\rho_{d,d}^{\,d},t),\quad d\ge2,\quad 1-1/d\le t<1,
\]
\[
\left(dq,\rho_{d,q}^{\,q},1-\frac{j}{q-d}\right),\quad
d\ge1,\ q\ge2d,\quad 1\le j\le\lfloor q/d\rfloor-1.                  \tag{21}
\]
Every stated lower endpoint \(s=0\) is included. The derivation is exhaustive, and substitution into (18) proves the converse. Each such nonunit core has its OWN strictly positive clock
\[
\lambda_{d,q}=\log\!\left(q^3\rho_{d,q}^{\,q-1}\right)
=\log\!\left(\frac{q^2(d-1+\rho_{d,q})}{d\rho_{d,q}}\right)
\ge2\log q>0.                                                      \tag{22}
\]
The sheet \(U\) is the complete zero-clock fixed set, and by (12) the only zero-cycle core. It retains source and extension isotropy \(\mathbb Z\) and \(H=0\), not a positive primitive. All other fixed cores in (21) have entire \(H=\lambda_{d,q}\mathbb Z\) and trivial extension isotropy. Continuum or equal-time fixed cores are not merged.

## 7. Every incoming layer, phases, and packet multiplicity

Equations (2)--(3) give every one-step predecessor at ANY target, including terminal targets. An explicit untruncated first-layer form for T/L at a fixed core \(f=(m,u,v)\) is: choose every \(1\le a\le m-1\) with \(v\ge1-1/a\), set \(e=m-a\), choose every \(b\ge e\), and take
\[
\left(ab,\frac{a-1+R}{ab},\frac{e-1+av-a+1}{b}\right),
\qquad R=u^{1/b}\ (T),\quad R=u\ (L).                               \tag{23}
\]
For G use the same \(a,e,b,R=u^{1/b}\) and ALL \(j=0,\ldots,a-1\), replace the first coordinate by \(n=ab+j\), and divide the second numerator by \(n\), not \(ab\). This enumerates exactly \(\lfloor n/a\rfloor=b\), preserving every nondivisible predecessor. For H choose every divisor \(a\mid m\) with \(v\ge1-1/a\), put \(b=m/a\), choose EVERY \(e=1,\ldots,b\), and use (23)'s real coordinates with memory \(m\). Equality in each strip test is retained.

In particular all first MAIN incoming to (15) are
\[
\left(b,\frac{4^{-1/b}}{b},0\right),\qquad b\ge1.                     \tag{24}
\]
This includes the unit-memory predecessor \(b=1\), which itself has no MAIN predecessor; no incoming can shorten (15)'s entire group. For H each point of \(U\) has only itself as predecessor, by its \(m=1\) inverse list.

For any owner define \(P_0(z)=\{z\}\) and \(P_{a+1}(z)=\bigcup_{w\in P_a(z)}\{I_\alpha w:w\in E_\alpha\}\). Every level performs ALL its own intermediate domain checks; no arbitrary branch word is admitted. The full base orbit of \(z\) is \(\bigcup_{b\ge0:\,F^bz\text{ defined}}\bigcup_{a\ge0}P_a(F^bz)\), directly by (8), including terminal endpoints. For a fixed core \(f\) this is its full basin \(\mathcal B_f=\bigcup_a P_a(f)\). All its points have source isotropy \(\mathbb Z\) and ENTIRE \(H=\kappa_F(f)\mathbb Z\), by transient cancellation in (10). Different fixed cores have disjoint basins: their constant futures could meet only if the cores were equal.

For any base orbit choose a reference \(f\) and an arrow \(g_z:z\to f\). Then ALL extension phases are \(h+c_F(g_z)\pmod{H_f}\). Choices differ exactly by reference isotropy, and equality of phase classes supplies a lifted arrow, proving completeness. Over a fixed basin this becomes
\[
h-S_a(z)\pmod{\kappa_F(f)\mathbb Z}\qquad(F^az=f).                    \tag{25}
\]
Different hitting times differ by an integer fixed clock. For an eventual cycle \(f_j=F^jf_0\), the corresponding formula is \(h+S_j(f_0)-S_a(z)\pmod{\Lambda\mathbb Z}\) when \(F^az=f_j\). Height translation is ordinary addition on \(\mathbb R/H_f\), including the full line when \(H_f=0\). Thus each positive-clock fixed core supplies one physical circle packet with all phases; incoming branches are not extra packets. Zero-clock cores retain all phases and isotropy but no positive packet. The parameterizations (13), (16), (17), (19), (21) consequently give the complete fixed-window multiplicities.

## 8. Gate assessment and decision

| Item | Result for this frozen owner |
| --- | --- |
| T0 | Full Borel source, sigma-finite measure, exact inverse atlas, all-point every-Borel IMAGE, groupoid and extension established. |
| T1 | Genuine divisor permission and geometric-to-integer feedback; clock owned by the actual inverse. Strong naturalness and arbitrary-encoding risks remain OPEN. |
| T2 | Complete fixed sets and full incoming/isotropy/phase ownership established; MAIN's primitive \(\log4\) violates the necessary ordinary-prime target. STOP / FORK. |
| T3 / classical / formal / B | NOT AUDITED / NOT APPLICABLE / UNASSIGNED / NOT INVOKED. |

The same-object ledger is intact. The failure is neither missing nonemptiness nor a control's adverse result: MAIN has its own wrong positive primitive. No higher-period classification, global prime-coverage theorem, invariant probability, convergence, spectrum, zeta, or operator is inferred. A new architecture requires a new card and authorization; none is started here.

## Reproducibility, access, and AI assistance

The frozen105-line input SHA256 is `52ad8cc8d271c49317cf7245aed09ef3d421d2245b3b091c0f6c5054c96b25a1`. The author read it completely after release, along with the paper template and relevant repository/ARS guidance. Outputs are this proof, [README](README.md), and [claim ledger](claim-ledger.md). All scientific work is exact algebra, monotonicity, differentiation, and Borel change of variables; no scientific code, numerical scan, truncation, external search, or prime/zero data is used. Hash, local-link, identity, and formatting checks are mechanical only.

The definition scout read AGENTS/plan/400 summary, prior guide1–180, and only collision cards365 and397 in full including outcomes; shared prior authorship includes396 and402. The scout disclosed brief, unverified mental algebra on a local derivative and fixed-memory relation before freeze, not used for tuning. This is not zero-exposure or blind preregistration. The frozen object was rederived after CP1 release; no novelty or nonconjugacy certification is made.

The same-author helper `/root/bilateral_transport_review/direct_controls` first saw only the draft sent in a message for definition-completeness checking. After release it read only the frozen105-line407 card for a bounded H/G owner and fixed-set derivation; the main author independently derived and integrated these results. This helper is NOT the independent reviewer. The author read no407 review, raw, or peer proof and wrote only the three authorized author surfaces, not the root-owned card or evidence.

AI agents supplied mathematical derivation, drafting, and internal checks; the separate repository review process is likewise AI-assisted. No human or external mathematical verification is certified. Shared-history same-model internal review is NOT_CALIBRATED, not blind or external peer review. ARS guidance informed the frozen-owner boundaries, separate control proofs, and access/assistance disclosures. No external publication or funding is claimed; no human-subject study is involved.

EOF — DPR01 author proof; complete fixed gate, no higher-period census.
