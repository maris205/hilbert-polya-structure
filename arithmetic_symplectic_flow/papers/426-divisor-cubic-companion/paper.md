# Divisor cubic companion: an owned prime-five fixed packet

Candidate ID: `ANG-20260923-DCC01`. Paper426; 2026-09-23.
Batch `SYMMETRY-FEEDBACK-20260923-P`, round2/5.
Outcome: `OWNED CUBIC IMAGE CLOCK; PRIME-5 FIXED PACKET — BOUNDED OPEN / FORK`.

Contract: [frozen card](candidate-card.md), original99 lines fully read.
Scope: three complete inverse/IMAGE/history owners; ALL fixed states in
the CLOSED cube \([-2,2]^3\), with unrestricted complete incoming.
No period-two or higher search; no claim of global prime purity or coverage.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal Route UNASSIGNED; Route B NOT INVOKED.
AI-assisted derivation/drafting; shared-history NOT_CALIBRATED.

## Abstract

The current divisor and product digits of a real three-register state
determine a cubic companion transport. Its actual inverse-root atlas owns
a finite positive analytic IMAGE version at every legal point, including
assigned arithmetic cuts. In the frozen cube MAIN has exactly one fixed
state, the diagonal \(-\sqrt2\). Its complete unrestricted source packet
contains only that state and has entire return group \((\log5)\mathbb Z\).
The permission-off control additionally has a prime-seven fixed packet;
the cubic-off control has a continuous zero-clock fixed family, including
one nontrivial incoming endpoint. All branches, critical terminals,
ineffective isotropy and height phases remain. One positive packet
establishes nonemptiness, not the required global prime ledger. The
precommitted bounded decision is therefore OPEN / FORK.

## 1. Entire source, controls and divisor-symbolic interface

Each owner separately has \(X=\mathbb R^3\), its usual Borel structure,
and \(\mu=\mathrm{Leb}_3\). At \(z=(a,b,c)\), put
\[
 m=\lfloor a\rfloor,\qquad n=\lfloor bc\rfloor,\qquad
 P_q(r)=r^3+qr,\qquad \Delta_q(r)=3r^2+q .
 \tag{1}
\]
MAIN requires \(m\ne0,m\mid n\), takes \(q=n/m\), and is legal
exactly when also \(\Delta_q(a)\ne0\). Its action is
\[
 T(a,b,c)=(b,c,P_q(a)).
 \tag{2}
\]
G replaces its arithmetic rule by
\(q_G=\lfloor n/m\rfloor\) for \(m\ne0\), and \(q_G=0\) for \(m=0\).
Its only domain condition is \(\Delta_{q_G}(a)\ne0\), with the same
cubic formula. L retains MAIN's arithmetic rule but uses
\[
 T_L(a,b,c)=(b,c,qa),\qquad q\ne0.
 \tag{3}
\]
The cubic \(\Delta\) condition is NOT imposed on L.

All signs, units, zero digits, axes, floor faces and critical points remain
objects. Illegal sources have no next step; they are neither deleted nor
assigned absorbing loops. They retain their identities and every actual
incoming arrow. A terminal next-step clock is NOT DEFINED, not zero.
Critical termination, Lebesgue measure and the polynomial are frozen
designs, not consequences of an already established naturalness theorem.

The [prior-work](../../docs/prior_work/README.md) interface is the integer
proper-divisor seed \((N,d)\mapsto(d,N,1)\), for integers \(N\ge2\),
\(1<d<N\). Its digits are \(m=d,n=N\), so arithmetic permission
is exactly \(d\mid N\). When permitted,
\(\Delta=3d^2+N/d>0\) and \(T(d,N,1)=(N,1,d^3+N)\).
Thus geometric regularity does not discard a permitted integer seed.
This verifies a deformation of divisor admissibility into actual nonlinear
transport and subsequent current-state feedback. It proves no conjugacy,
symplectic lift, prime acceptance rule or natural prime-period theorem.

## 2. Full inverse branches, domains and IMAGE

The connected monotonic intervals of \(P_q\), ordered from left to right,
and their full images are as follows. Endpoints in this table are excluded.

| Parameter | Intervals \(I_{q,j}\) | Corresponding images \(P_q(I_{q,j})\) |
| --- | --- | --- |
| \(q>0\) | \(\mathbb R\) | \(\mathbb R\) |
| \(q=0\) | \((-\infty,0),(0,\infty)\) | \((-\infty,0),(0,\infty)\) |
| \(q<0,\ h=\sqrt{-q/3}\) | \((-\infty,-h),(-h,h),(h,\infty)\) | \((-\infty,2h^3),(-2h^3,2h^3),(-2h^3,\infty)\) |

Indeed \(P'_q=\Delta_q\) has a constant nonzero sign on each interval;
the endpoint values for \(q<0\) are \(P_q(-h)=2h^3\),
\(P_q(h)=-2h^3\), and the outer limits are infinite.
Hence the branch inverse \(\rho_{q,j}\) is analytic on the stated image.
Critical VALUES are not globally excluded targets: another regular branch
may reach one. All regular roots must pass their own source tests.

For target \(y=(u,v,w)\), MAIN enumerates ALL integers
\(m\ne0,n\) with \(m\mid n\), \(q=n/m\), and every such \(j\).
Its exact branch is
\[
 \theta_{m,n,j}(y)=(r,u,v),\quad r=\rho_{q,j}(w),\qquad
 E_{m,n,j}=\{w\in P_q(I_{q,j}),\ \lfloor r\rfloor=m,\
                                      \lfloor uv\rfloor=n\}.
 \tag{4}
\]
G enumerates ALL \(m,n\in\mathbb Z\), using its OWN \(q_G(m,n)\)
and the identical floor tests (4). No divisibility condition is added to G.
L enumerates all MAIN arithmetic labels with \(q=n/m\ne0\), and has
\[
 \theta^L_{m,n}(y)=(w/q,u,v),\qquad
 E^L_{m,n}=\{\lfloor w/q\rfloor=m,\ \lfloor uv\rfloor=n\}.
 \tag{5}
\]
These formulas include the frozen regularity, own-source and forward-image
checks: (4) reconstructs a point in its regular root interval and its actual
digits, and substitution into its own polynomial gives \(w\); (5) does the
same with nonzero \(q\). Targets need not have a next step.

Conversely, any predecessor has last two coordinates \((u,v)\), its actual
digits fix \(m,n,q\), and its regular first coordinate belongs to exactly
one interval \(I_{q,j}\), or solves the L equation as \(w/q\).
It therefore appears in (4) or (5). Each branch is injective because its
own forward map recovers the target. An actual source fixes its floors and
regular interval uniquely, so no artificial label copies remain.
All domains are Borel, all inverse sets countable, and no root/index cutoff
or selected branch enters this complete enumeration.

Differentiate the inverse identity \(P_q(\rho(w))=w\) on its regular
interval. The inverse coordinate derivative is
\(\rho'(w)=1/\Delta_q(r)\). The other two output coordinates are \(u,v\),
so their permutation contributes no change to the absolute determinant:
\[
 J_\theta(y)=\frac1{|\Delta_q(r)|}\quad\text{for MAIN/G},\qquad
 J^L_\theta(y)=\frac1{|q|}.
 \tag{6}
\]
These values are finite and positive at EVERY actual inverse point.
Before digit restriction, \((a,b,c)\mapsto(b,c,P_q(a))\) is a
diffeomorphism \(I_{q,j}\times\mathbb R^2\to
\mathbb R^2\times P_q(I_{q,j})\); the L linear map is a diffeomorphism
for \(q\ne0\). Change of variables on these geometric open sets, restricted
to each Borel actual domain, proves
\[
 \mu(\theta E)=\int_EJ_\theta\,d\mu
 \quad\text{for EVERY Borel }E\subseteq E_\theta .
 \tag{7}
\]
Null sets and arithmetic faces are included. The prescribed analytic germ
supplies the point value on each assigned face; measure alone does not
uniquely determine values there. No version is repaired after observing a
periodic point. A critical source is retained as a terminal, not treated as
an inverse point with an infinite or invented density.

Consequently the actual branch forward densities and signed clocks are
\[
 \lambda_T(z)=|\Delta_q(a)|,\quad
 \lambda_G(z)=|\Delta_{q_G}(a)|,\quad
 \lambda_L(z)=|q|,\qquad \kappa_O=\log\lambda_O .
 \tag{8}
\]
Each is \(J_{\theta_z}(T_Oz)^{-1}\) from its own inverse. The cubic clocks
can be signed or zero; no positive roof or Hamiltonian time is substituted.

## 3. Full histories, kernels, return groups and phases

For each owner, let \(P(y)\) consist of ALL passing inverse points from its
own atlas, and define
\[
 P^0(y)=\{y\},\qquad
 P^{j+1}(y)=\bigcup_{x\in P^j(y)}P(x).
 \tag{9}
\]
The two inverse identities prove inductively that this is exactly every
legal predecessor at each depth. The depth-zero identity remains even
when \(P(y)\) is empty. This construction never restricts sources to the cube.

For legal histories put
\[
 M_r(z)=\prod_{i=0}^{r-1}\lambda(T^iz),\quad
 S_r(z)=\log M_r(z),\qquad M_0=1,\ S_0=0.
 \tag{10}
\]
Fixing an owner, its countable Borel groupoid and cocycle are
\[
 G=\{(z,r-s,w):T^rz=T^sw,\ r,s\ge0\text{ legal}\},\qquad
 c(z,r-s,w)=\log\frac{M_r(z)}{M_s(w)}.
 \tag{11}
\]
Source is \(w\), range is \(z\), and equal actual triples are identified.
The countable inverse atlas and the Borel finite iterates make this a
countable Borel relation with retained integer lag.
Two presentations of one triple differ by extending both ends equally;
the added products on their common tail cancel. To compose arrows, align
the middle exponents using the longer already legal middle history.
The resulting lag is the sum and the middle products cancel. Thus the
groupoid operations and cocycle are well-defined even at finite-terminal
histories, with \(c(g^{-1})=-c(g)\). No unavailable future step is inserted.
The forward arrow \((Tz,-1,z)\) has \(c=-\kappa(z)\).
On every history bisection, repeated (7) gives actual IMAGE density
\(M_s(w)/M_r(z)=e^{-c}\) for the arrow \(w\mapsto z\).

With \(\ell(z,k,w)=k\), the FULL kernels are the explicit product tests
\[
 \begin{aligned}
 \ker\ell&=\{(z,0,w):T^rz=T^rw\text{ for some legal }r\},\\
 \ker c&=\{(z,r-s,w)\in G:M_r(z)=M_s(w)\},\\
 \ker\ell\cap\ker c
 &=\{(z,0,w):T^rz=T^rw,\ M_r(z)=M_r(w)
                  \text{ for some legal }r\}.
 \end{aligned} \tag{12}
\]
All products use (8); these are not assertions that equal-level incoming
sources are identical, or that zero-step clocks exhaust the clock kernel.

Nonzero source isotropy is equivalent to eventual periodicity of the legal
future: a nonzero-lag self-arrow is precisely an actual repeated future
state. If the eventual core has least source period \(p\), and \(F\)
is any of its points, then
\[
 C=\sum_{i=0}^{p-1}\kappa(T^iF),\quad
 G_z^z=p\mathbb Z,\quad c(z,kp,z)=kC,\quad H_z=C\mathbb Z .
 \tag{13}
\]
Every eventual repetition lag is a multiple of \(p\), and every such
multiple is realized; the entrance products cancel. These are therefore
ENTIRE groups, not subgroups generated by a selected witness. A
non-eventually-periodic or finite-terminal future has source isotropy zero
and \(H_z=\{0\}\). Formula (13) is the general ledger, not a census of
periodic cores outside the authorized fixed-state window.

The extension retains all \((z,h)\in X\times\mathbb R\), with arrows
\((w,h)\mapsto(z,h+c)\). On its orbit SET,
\(\rho^t[z,h]=[z,h+t]\) is well-defined for all real \(t\), since it
commutes with every extension arrow. Its stabilizer is exactly \(H_z\).
The extension groupoid isotropy on an eventual period-\(p\) packet is
\(\{kp:kC=0\}\). If \(C\ne0\), the primitive is \(|C|\), repetitions
are its positive integer multiples, and extension isotropy is trivial.
If \(C=0\), source \(p\mathbb Z\) remains in extension isotropy with
NO positive return time. Non-eventually-periodic/terminal packets also have no positive
stabilizer, but may have actual incoming and nonzero individual arrow clocks.

For any source packet choose a base \(b\) and an actual arrow \(g_z:z\to b\).
The phase is \(h+c(g_z)\) modulo \(H_b\); different such arrows differ by
a loop in \(H_b\). If \(T^az=T^ib\), this is
\(h+S_i(b)-S_a(z)\); for a fixed base it is \(h-S_a(z)\).
All phases \(\mathbb R/H_b\) remain. A periodic core's complete source
packet is exactly the union of (9) over its core points and all depths,
because tail equivalence to that core means eventual arrival.
Different fixed cores cannot share a packet: their constant forward tails
are unequal. No phase selection, packet merging or manifold quotient is used.

## 4. ALL fixed states in the closed cube

The companion shift forces every fixed point to be \((t,t,t)\), with
\(-2\le t\le2\). Write \(m=\lfloor t\rfloor,n=\lfloor t^2\rfloor\).

For MAIN, \(t=0\) and all \(m=0\) states are illegal. A legal fixed
state satisfies \(t^2=1-q\). This is an integer, so \(n=t^2=1-q\).
Together with \(n=qm\), it gives \(q(m+1)=1\). The integer possibilities
are \(q=1,m=0\), which is forbidden, and \(q=-1,m=-2\).
The latter yields \(t=-\sqrt2,n=2,\Delta=5\ne0\).
Thus, writing \(F_k=(-\sqrt{k},-\sqrt{k},-\sqrt{k})\),
\[
 \operatorname{Fix}(T)\cap[-2,2]^3=\{F_2\}.
 \tag{14}
\]
This argument includes the outer cube faces and assigned floor endpoints;
it is used here only for the frozen fixed-state question.

For G, \(t=0\) has its assigned \(q=0,\Delta=0\), hence is terminal.
For \(t\ne0\), fixedness again implies \(t^2=k=1-q\), now with
\(k\in\{1,2,3,4\}\). Checking all signs gives the complete finite table:

| \(k\) | Actual \(q_G\) at \(+\sqrt{k}\) | Actual \(q_G\) at \(-\sqrt{k}\) | Required \(1-k\) |
| --- | --- | --- | --- |
| 1 | 1 | -1 | 0 |
| 2 | 2 | -1 | -1 |
| 3 | 3 | -2 | -2 |
| 4 | 2 | -2 | -3 |

Only \(F_2,F_3\) survive. Their own \(\Delta=2k+1\) is \(5,7\),
so both are legal, including their exact product-floor faces \(bc=2,3\).
Thus \(\operatorname{Fix}(G)\cap[-2,2]^3=\{F_2,F_3\}\).

For L, \(t=0\) fails permission; otherwise fixedness requires \(q=1\).
Thus \(n=m\ne0\), and \(n=\lfloor t^2\rfloor\ge0\) forces \(m>0\).
In the cube, \(m=1\) gives \(1\le t<\sqrt2\); the only \(m=2\)
point \(t=2\) has \(n=4\ne2\). Therefore
\[
 \operatorname{Fix}(L)\cap[-2,2]^3
 =\{U_t=(t,t,t):1\le t<\sqrt2\}.
 \tag{15}
\]
The lower endpoint is included and the upper one excluded by its actual
new product digit, not by deleting a boundary. L's own \(q\ne0\)
regularity is satisfied, with no irrelevant cubic test.

## 5. Complete unrestricted incoming and boxed packet ledgers

Every MAIN predecessor of \(F_2\) must be \((a,-\sqrt2,-\sqrt2)\);
its product digit is exactly \(n=2\). Its complete list of possible
divisor digits is \(m=1,2,-1,-2\).
For \(m=1,2\), the cubic output is positive. For \(m=-1,q=-2\),
\(a\in[-1,0)\) gives \(a(a^2-2)>0\).
For \(m=-2,q=-1\), \(a\in[-2,-1)\); \(a^3-a\) is strictly
increasing there and has the solution \(a=-\sqrt2\).
Thus \(P_T(F_2)=\{F_2\}\); induction in (9) leaves no incoming tail
at ANY depth, including sources outside the cube.

For either G core \(F_k\), \(k=2,3\), a predecessor has form
\((a,-\sqrt{k},-\sqrt{k})\) and must solve
\(a^3+q_G(a)a=-\sqrt{k}\), with \(n=k\).
If \(a\ge0\), its quotient and cubic output are nonnegative.
If \(a<0\), put \(m=-j\), \(j\ge1\). For \(j=1\),
\(q=-k\) and \(a(a^2-k)>0\). For \(j=2\),
\(q=1-k\), and the cubic is strictly increasing on \([-2,-1)\);
its unique solution is \(a=-\sqrt{k}\). For EVERY \(j\ge3\),
\(q=-1,a<-2\) and \(a^3-a<-6<-\sqrt{k}\).
This exhausts all integer labels without a cutoff, so each G core also
has only itself as a predecessor and no incoming tail at any depth.

For an L core \(U_t\), \(1\le t<\sqrt2\), every predecessor is
\((a,t,t)\), with \(n=1\). Divisibility forces \(m=\pm1\).
The \(m=1,q=1\) inverse gives \(a=t\), always valid.
The \(m=-1,q=-1\) inverse gives \(a=-t\), valid only at \(t=1\);
for \(t>1\), its actual floor is \(-2\), not \(-1\).
At \(t=1\), let \(A=(-1,1,1)\). An incoming point to A would be
\((a,-1,1)\), with \(n=-1,m=\pm1,q=-1/m\). Its required output
gives \(a=-m\), contradicting \(\lfloor a\rfloor=m\) in both cases.
Therefore A has no predecessor, while retaining its identity and its
actual arrow to \(U_1\), of clock \(\log|-1|=0\).

The ENTIRE source packets of the found cores are consequently
\[
 \mathcal B_T(F_2)=\{F_2\},\quad
 \mathcal B_G(F_k)=\{F_k\}\ (k=2,3),\quad
 \mathcal B_L(U_t)=
 \begin{cases}\{U_1,A\},&t=1,\\\{U_t\},&1<t<\sqrt2.\end{cases}
 \tag{16}
\]
The found cores have least source period one. A is not periodic: it enters
\(U_1\) after one step, with eventual period one. Applying (8), (13) and
the exact incoming classification gives the full positive/zero ledger:

| Owner/core | Source isotropy | Entire \(H\) | Extension isotropy | All phases / primitive |
| --- | --- | --- | --- | --- |
| MAIN \(F_2\) | \(\mathbb Z\) | \((\log5)\mathbb Z\) | \(0\) | \(\mathbb R/(\log5)\mathbb Z\); \(\log5\) |
| G \(F_2\) | \(\mathbb Z\) | \((\log5)\mathbb Z\) | \(0\) | same form, OWN packet |
| G \(F_3\) | \(\mathbb Z\) | \((\log7)\mathbb Z\) | \(0\) | \(\mathbb R/(\log7)\mathbb Z\); \(\log7\) |
| L every \(U_t\), also A in its packet | \(\mathbb Z\) | \(\{0\}\) | \(\mathbb Z\) | full \(\mathbb R\); no positive primitive |

For each positive singleton-source packet, its arrows are exactly integer
loops; lag, clock and joint kernels on that packet are units. No smaller
positive stabilizer than \(\log5\) or \(\log7\) exists. All height phases
form that packet's whole translation circle, not selected centres or new
packets for each phase. Repeated traversals give integer multiples.

For each L singleton-source packet the clock kernel is the entire integer
loop group, while lag and joint kernels are units. On the two-point L
packet \(\{U_1,A\}\), all triples with either endpoint and any integer lag
are realized by their common fixed future. All have clock zero; its lag
and joint kernels are ALL four zero-lag endpoint pairs, not only identities.
Both endpoints have source and extension isotropy \(\mathbb Z\).
The phase offset from A to \(U_1\) is zero; all real phases remain.
The continuum of distinct L zero-clock packets is not discarded.

## 6. Decision, limits and evidence

The source interface, full carrier/inverses and prescribed all-point
geometric clock ownership are established. MAIN has a genuine fixed
packet with primitive \(\log5\), so its positive ledger is nonempty.
Its source lies outside the positive integer test interface; the exact
lineage does not by itself explain global prime purity. The G control
retains that packet and adds a prime-seven fixed packet; it supplies no
MAIN credit. L demonstrates that removing the nonlinear term leaves the
entire zero-clock fixed family and its boundary incoming.

There is no wrong-prime or duplicate-prime MAIN packet in the frozen fixed
window, but nothing here excludes one elsewhere or at higher source period.
Global prime purity, uniqueness and all-prime coverage remain OPEN.
Strong naturalness, including the critical terminal design and pointwise
analytic versions at null product cuts, remains OPEN; arithmetic T1 is
NOT PASSED. The precommitted decision is bounded OPEN / FORK.
No period-two work or enlargement of the cube is made.
T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

Inputs and methods: the original99-line card; exact real-root branch
analysis, substitution, differentiation, Borel change of variables,
history cancellation, integer-floor enumeration and all-depth induction.
There is no scientific code, orbit table, numerical tolerance, external
data/literature, operator, PDF, publication or Git work.
[Claim ledger](claim-ledger.md) and [overview](README.md) are the author surfaces.

Definition-stage old reads were only
[343 card](../343-gcd-square-register-flow/candidate-card.md) lines1--56 and
[396 card](../396-geometric-divisor-henon/candidate-card.md) lines1--53,
non-EOF; their exact prefix hashes are recorded in the frozen card.
Heading navigation exposed outcome/clarification titles, not bodies.
The frozen426 card itself supplied a one-sentence425 family comparison;
no425 scientific file was read by this author.
Informal fixed-state tractability expectations influenced design; this
was not blind preregistration or a novelty search.
Shared prior author/scouting history is disclosed, with no old theorem
or clock imported. Card-only author helper `dss_g_fixed_author` supplied
the G/L fixed and incoming algebra, personally checked and integrated.
This was author-side assistance, not independent mathematical review.
No reviewer/raw/evidence/peer science was read during author production.

AI agents supplied design, mathematical derivation, drafting and author
checks; the workflow separately includes AI internal review.
All such roles are NOT_CALIBRATED; no human or external verification is
certified. Human contributions, funding and conflicts were not supplied
and are not invented. No human participants or personal data are involved.
Data availability: the full inputs, formulas and exact proof are contained
in this Markdown package; no hidden empirical dataset supports the claims.
