# Divisor-gated kick cylinder: an owned clock with four prime-2 fixed packets

Candidate ID: `ANG-20260923-DKC01`.
Outcome: `OWNED CYLINDER CLOCK; FOUR PRIME-2 FIXED PACKETS — STOP / FORK`.
Date: 2026-09-23. Frozen scientific contract: [candidate card](candidate-card.md), original 94 lines, SHA256 `ee718599f0ca4697601e212684056e47be13023dd21c9cf4d97423f8d0e5d925`.
Type: arithmetic partial Borel groupoid with a real cocycle extension; classical suspension NOT APPLICABLE.
T0 and the prescribed T1 clock ownership are established below; the bounded T2 uniqueness test fails. Strong naturalness remains OPEN.
T3 NOT AUDITED; formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## 1. Result, scope, and frozen owners

MAIN has exactly four fixed states. Each owns the entire height stabilizer \((\log 2)\mathbb Z\), hence the primitive time \(\log 2\). They belong to four different full source orbits even after every incoming state is included. This violates the frozen requirement of at most one packet per prime. It does not show that MAIN has a nonprime primitive time, nor classify higher periods or all-prime coverage.
The same full carrier and measure are separately owned by MAIN and each control:
\[
 X=\mathbb N_0\times\mathbb T\times\mathbb R,\qquad
 \mathbb T=\mathbb R/\mathbb Z,\qquad \mu=\#\times m_{\mathbb T}\times dp.
\]
This is a sigma-finite measure, not an asserted invariant probability. For \(n\ge1\), let \(a=\operatorname{rep}\theta\in[0,1)\), \(d=1+\lfloor na\rfloor\). A step exists exactly when \(d\mid n\); put \(q=n/d\).
MAIN, K, V, and H respectively have
\[
\begin{array}{c|c|c}
 O&v&F_O(n,\theta,p)\\ \hline
 M&p/d+\sin(2\pi q\theta)&(d+q,\theta+v,v)\\
 K&p/d&(d+q,\theta+v,v)\\
 V&p+\sin(2\pi q\theta)&(d+q,\theta+v,v)\\
 H&p/d+\sin(2\pi q\theta)&(n,\theta+v,v).
\end{array}                                                    \tag{1}
\]
Angles in outputs are modulo one. All real momenta and all angle points remain. States with \(n=0\) or failed divisibility are terminals: there is no outgoing step or step clock, but their identity and every actual incoming arrow remain.
For every proper \(d\), the whole strip \([(d-1)/n,d/n)\), with every \(p\), has permission precisely when \(d\mid n\). The quotient \(q\) drives the sine; the resulting angle and register drive the next permission. This is the specific divisor-symbolic-to-geometric feedback lineage. No prime table, selected centre, sign choice, or inserted roof is used.

## 2. Entire inverse atlas and pointwise IMAGE law

For positive integers \(d,q\), set
\[
 A_{dq}=[(d-1)/(dq),\,d/(dq)),\qquad
 B_{dq}=\{dq\}\times\{\theta:\operatorname{rep}\theta\in A_{dq}\}\times\mathbb R.
\]
The \(B_{dq}\) are disjoint Borel cells partitioning the legal source. Write \(m_O=d+q\) for \(O=M,K,V\), and \(m_H=dq\).
The entire target domain of that branch is
\[
 E^O_{dq}=\{(m_O,\beta,v):\operatorname{rep}(\beta-v)\in A_{dq}\}.
                                                               \tag{2}
\]
For \(\theta=\beta-v\) in \(\mathbb T\), the actual inverses are
\[
\begin{split}
 I^M_{dq}=I^H_{dq}&=(dq,\theta,d[v-\sin(2\pi q\theta)]),\\
 I^K_{dq}&=(dq,\theta,dv),\\
 I^V_{dq}&=(dq,\theta,v-\sin(2\pi q\theta)).
\end{split}                                                    \tag{3}
\]
Substitution proves both inverse identities between (2) and \(B_{dq}\). Conversely every preimage determines its \(d,q\) from its actual register and digit, so (3) exhausts the inverse.
At a given target register, M/K/V enumerate every positive solution \(d+q=m\); H enumerates every divisor \(d\mid m\), \(q=m/d\), when \(m\ge1\). There is no artificial cutoff. For M/K/V registers 0 and 1 have no predecessors; for H register 0 has none. Target forward legality is not an inverse-domain condition.
Each inverse has a smooth extension on its whole target cylinder. The integer \(q\) makes the sine circle-periodic. In local \((\beta,v)\) charts, with \(s'=2\pi q\cos(2\pi q\theta)\), the M/H derivative is
\[
 \begin{pmatrix}1&-1\\-ds'&d(1+s')\end{pmatrix}.
\]
K has matrix \(\left(\begin{smallmatrix}1&-1\\0&d\end{smallmatrix}\right)\); V has the displayed M/H matrix with the prefactor \(d\) replaced by 1. Therefore the prescribed versions are
\[
 J_M=J_K=J_H=d,\qquad J_V=1,\qquad
 \kappa_M=\kappa_K=\kappa_H=-\log d,\quad \kappa_V=0.              \tag{4}
\]
These are positive finite inverse Jacobians at every actual target, including null digit cuts and the circle seam. The representative is never differentiated. A seam is only a chart change, and each included lower cut uses its assigned branch extension.
The extension is a cylinder diffeomorphism: first undo the angular shear, then rescale/translate momentum. Change of variables on circle charts, followed by countable Borel partitioning, proves for every Borel \(E\subset E^O_{dq}\)
\[
 \mu(I^O_{dq}E)=\int_E J_O\,d\mu.                               \tag{5}
\]
The counting coordinates contribute exactly one for their actual singleton-to-singleton branch correspondence. They do not supply another factor \(d\). Formula (5) permits infinite measures and does not merely hold off a null set.
To distinguish actual unions from multiplicity, for Borel legal \(A\) define
\[
 N_A(y)=\sum_{d,q}\mathbf1_{E^O_{dq}}(y)\mathbf1_A(I^O_{dq}y).
\]
Each summand is zero outside its own domain. The branch atlas gives
\[
 \mu(F_OA)=\int\mathbf1_{\{N_A>0\}}\,d\mu,\qquad
 \int N_A\,d\mu=\int_A e^{\kappa_O}\,d\mu.                        \tag{6}
\]
Thus overlapping target branch images are counted once in the actual image, not silently added. The disjoint source cells and injective Borel branches also make these images Borel.
For H the whole partial map is injective: from \((m,\beta,v)\), the only possible old register is \(m\), and the old angle \(\beta-v\) fixes its unique digit. Divisibility then fixes \(q\) and (3) fixes momentum. This statement includes boundaries.

## 3. Full history owner, kernels, isotropy, and phases

All subsequent definitions are made separately for each owner \(O\). An iterate is defined only while its preceding steps are legal; an endpoint may be terminal. Length zero is defined everywhere.
Put \(S_a(z)=\sum_{j<a}\kappa_O(F_O^jz)\), \(S_0=0\). For M/K/H also put \(D_a(z)=\prod_{j<a}d(F_O^jz)\), \(D_0=1\), so \(S_a=-\log D_a\).
The actual retained-lag groupoid is
\[
 G_O=\{(z,a-b,w):a,b\ge0,\ F_O^az=F_O^bw\},\quad
 c(z,a-b,w)=S_a(z)-S_b(w).                                     \tag{7}
\]
Its source is \(w\), range \(z\); equal triples, not equal witnesses, are identified. In particular neither actual lag nor multiple distinct incoming states are discarded.
If two witnesses have the same lag, their lengths differ by a common integer; extending the shorter pair adds identical sums along their common future. Hence \(c\) is well-defined. To compose, extend the shorter middle history to the longer one; legality follows from equality of its endpoint with the available common future. The middle sums cancel, proving additivity and \(c(g^{-1})=-c(g)\).
The equality loci of the partial Borel iterates are Borel, and the finite one-step inverse atlas gives countable source fibers. This is an actual countable Borel groupoid, not an invented smooth manifold.
Successive inverse IMAGE factors multiply to \(e^{-S_a}\). A branch-pair chart in (7), from \(w\) to \(z\), consequently has inverse-history ratio \(e^{-c}\); these use the same versions as (4), on every Borel chart. No second measure clock is substituted.
For M/K/H the complete kernel descriptions, over all actual witnesses, are
\[
\begin{split}
 \ker c&=\{(z,a-b,w):F^az=F^bw,\ D_a(z)=D_b(w)\},\\
 \ker\ell&=\{(z,0,w):\exists a,\ F^az=F^aw\},\\
 \ker c\cap\ker\ell
 &=\{(z,0,w):\exists a,\ F^az=F^aw,\ D_a(z)=D_a(w)\}.
\end{split}                                                    \tag{8}
\]
Here \(\ell\) is lag. In V, \(\ker c=G_V\), and the intersection is \(\ker\ell\). In H, partial injectivity makes \(\ker\ell\) and the intersection precisely the units. These formulas include terminals and units; an absent step is not assigned zero clock.
Nonzero source isotropy occurs exactly when the full forward state is eventually periodic. Indeed a nonzero isotropy witness is a repeated state; conversely a repeated state gives its actual period lag. If its least eventual full-state period is \(k\), every repeated-state lag is divisible by \(k\), and every multiple is realized after entry. Thus \(G_z^z=k\mathbb Z\); otherwise isotropy is trivial.
For an M/K/H cycle with least period \(k\), let \(P=\prod_{j<k}d_j\). The entire isotropy image is
\[
 c(jk)=-j\log P,\qquad H_z=c(G_z^z)=(\log P)\mathbb Z.            \tag{9}
\]
Transient factors cancel. In V, \(H_z=\{0\}\) for every state, even one with nontrivial source isotropy. In M/K a cycle cannot have \(P=1\): every digit would be 1 and every step would increase its register from \(n\) to \(n+1\).
The real extension retains all \((z,h)\in X\times\mathbb R\), with \((w,h)\mapsto(z,h+c(g))\). Extension isotropy is \(\ker(c|_{G_z^z})\): it is trivial for \(P>1\), equals \(k\mathbb Z\) for \(P=1\), and in V retains all source isotropy. Thus M/K have no nontrivial extension isotropy anywhere. H may retain zero-clock isotropy; higher-period H unit cycles are not classified here.
Physical height translation on extension orbit sets has stabilizer exactly \(H_z\). For \(P>1\) its least positive generator is \(L=\log P\), and repetitions have times \(rL\). It is not \(L/k\), an arbitrarily selected subgroup, or a sign-repaired roof. For \(H_z=0\) the height orbit is free, even when source isotropy is ineffective.
A packet is one full height-translation orbit over a full source orbit. Its phases form \(\mathbb R/H_z\); phases are not additional packets, and distinct source orbits are not identified by equal periods.
Every incoming state is specified without truncation by \(\mathcal P_0(z)=\{z\}\) and
\[
 \mathcal P_{a+1}(z)=\bigcup_{u\in\mathcal P_a(z)}
       \{I^O_{dq}u:u\in E^O_{dq}\},\qquad
 [z]_{G_O}=\bigcup_{\substack{b\ge0\\F_O^bz\ {\rm defined}}}
                  \bigcup_{a\ge0}\mathcal P_a(F_O^bz).           \tag{10}
\]
This includes incoming trees of terminals and nonperiodic states as well as cycles.
For a reference \(f_0\) on a \(k\)-cycle, write \(f_j=F^jf_0\). If \(F^ay=f_j\), the complete height phase is
\[
 h+S_j(f_0)-S_a(y)\pmod{H_{f_0}}.                               \tag{11}
\]
Alternative witnesses change it by precisely isotropy values. For a fixed core \(f\), this is \(h-S_a(y)\pmod{H_f}\); for \(H_f=0\) it is a real phase. More generally an actual arrow \(y\to z\) identifies phases by \(h+c(g)\pmod{H_z}\). All heights are kept.
Distinct fixed cores cannot share a source orbit: equality of their constant futures would force equality of the cores. Incoming states and height phases therefore never merge different fixed packets.

## 4. Complete MAIN fixed set and its full incoming

A fixed point must obey \(dq=d+q\), or \((d-1)(q-1)=1\). Thus \(d=q=2\), \(n=4\). Angular fixity requires \(p\in\mathbb Z\); momentum fixity is \(\sin(4\pi a)=p/2\), with the actual half-open digit strip \(a\in[1/4,1/2)\).
On \(4\pi a\in[\pi,2\pi)\), the complete possibilities are
\[
\begin{array}{c|c}
 f_0&(4,1/4,0)\\
 f_1&(4,7/24,-1)\\
 f_2&(4,3/8,-2)\\
 f_3&(4,11/24,-1).
\end{array}                                                    \tag{12}
\]
Only \(p=0,-1,-2\) are possible. The lower cut is included and \(a=1/2\) is excluded by its different assigned digit. This is an exhaustive solution on the full cylinder, not a selected finite sample.
Each core has source isotropy \(\mathbb Z\), \(\kappa=-\log2\), the entire \(H=(\log2)\mathbb Z\), trivial extension isotropy, and primitive height time \(\log2\).
For completeness, the only inverse pairs at register 4 are \((1,3),(2,2),(3,1)\). At a fixed target its integer momentum makes the inverse angle its core angle. Pair \((2,2)\) returns the core; \((1,3)\) adds a predecessor exactly for \(f_0,f_1\), whose angles are below \(1/3\); \((3,1)\), with strip \([2/3,1)\), adds none.
At register 3 the two possible pairs \((1,2),(2,1)\) have old register 2 and complementary half-circle strips, hence exactly one predecessor. At register 2 only \((1,1)\) gives old register 1; register 1 has none. Consequently the first two basins have four states each, and the last two are singletons.
The first complete chain is
\[
 (1,1/4,0)\longmapsto(2,1/4,1)\longmapsto(3,1/4,1)
 \longmapsto f_0\longmapsto f_0.                               \tag{13}
\]
For the second, define
\[
\begin{gathered}
 a=7/24,\quad b=-1+\sqrt2/2,\quad \eta=31/24-\sqrt2/2,\\
 c_*=2[b-\sin(2\pi\eta)],\quad
 \gamma=\eta-c_*\pmod1,\quad \delta=c_*-\sin(2\pi\gamma).
\end{gathered}
\]
Then the entire chain is
\[
 (1,\gamma,\delta)\longmapsto(2,\eta,c_*)\longmapsto(3,a,b)
 \longmapsto f_1\longmapsto f_1.                               \tag{14}
\]
The exact bounds \(7/24<\sqrt2/2<19/24\), proved by squaring positive quantities, give \(1/2<\eta<1\), so its assigned digit is 2. The identities \(\eta+b=a\) and \(\sin(6\pi a)=-\sqrt2/2\) verify the remaining arrows. Their transient digits are \(1,2,1\); those in (13) are \(1,1,1\).
Every height over these finite basins is covered by (11); for (13) all transient sums vanish, and for (14) they are integer multiples of \(-\log2\). Thus in each case the phase can be read as \(h\bmod\log2\). The singleton basins have the same phase description.
The four distinct fixed cores give four distinct positive packets of prime-2 time, with all incoming and all phases retained. The frozen uniqueness condition therefore fails decisively. Nothing about unidentified higher periods is needed to make this stop.

## 5. The three complete own-control fixed ledgers

### K: removing the kick

The register equation again forces \(d=q=2,n=4\). Momentum fixity \(p=p/2\) forces \(p=0\), and the angle is arbitrary in its full strip:
\[
 \operatorname{Fix}(F_K)=\{(4,\theta,0):\operatorname{rep}\theta\in[1/4,1/2)\}.
                                                               \tag{15}
\]
For \(a\in[1/4,1/3)\), the full chain is
\[
 (1,\theta,0)\to(2,\theta,0)\to(3,\theta,0)\to(4,\theta,0)\to(4,\theta,0).
\]
For \(a\in[1/3,1/2)\), the basin is just its core. This includes the \(1/3\) boundary in the latter case, as the register-3 digit-1 branch excludes that endpoint. The same complete pair enumeration used above proves that nothing is missing.
Each core has source isotropy \(\mathbb Z\), \(H=(\log2)\mathbb Z\), trivial extension isotropy, phase \(h\bmod\log2\), and primitive time \(\log2\). The uncountable set of cores gives uncountably many different prime-2 packets. This uses K's own \(J=d\), not MAIN's clock by transfer.

### V: removing the geometric index

Again \(n=4,d=q=2\). Momentum fixity requires \(\sin(4\pi a)=0\), so the strip admits only \(a=1/4\); angular fixity requires \(p\in\mathbb Z\). Thus
\[
 \operatorname{Fix}(F_V)=\{(4,1/4,k):k\in\mathbb Z\}.             \tag{16}
\]
For every integer \(k\), its full basin is precisely
\[
 (1,1/4,k)\to(2,1/4,k+1)\to(3,1/4,k+1)
 \to(4,1/4,k)\to(4,1/4,k).
\]
The inverse enumeration is exhaustive as before, with V's own inverse momentum. Every step has \(\kappa_V=0\). These countably many distinct cores have source and extension isotropy \(\mathbb Z\), \(H=0\), and free real phase \(h\); they are not positive-period packets. In fact V's entire groupoid clock is zero, not merely the clock in this window.

### H: holding the register

Fixity now leaves \(n=dq\) arbitrary. With \(b=q\,\operatorname{rep}\theta\in[(d-1)/d,1)\), it requires
\[
 p\in\mathbb Z,\qquad (d-1)p=d\sin(2\pi b).                     \tag{17}
\]
The complete solutions, with every \(q\ge1\), are:

- \(d=1\): \(b=0\) or \(1/2\), and every \(p\in\mathbb Z\).
- \(d=2\): \((b,p)=(1/2,0),(7/12,-1),(3/4,-2),(11/12,-1)\).
- \(d=3,4,5,6\): \(p=-1\) and \(b=1-\arcsin((d-1)/d)/(2\pi)\).
- \(d\ge7\): no fixed solution.

Each listed state is \((dq,b/q,p)\). Here is the exhaustive bound, rather than a finite parameter scan. For \(d\ge3\), the strip makes the sine strictly negative, and \(\lvert p\rvert\le d/(d-1)<2\), hence \(p=-1\).
Set \(\alpha_d=\arcsin((d-1)/d)\). The two sine solutions are \(b_1=1/2+\alpha_d/(2\pi)\) and \(b_2=1-\alpha_d/(2\pi)\). For \(d\ge4\), \(b_1<3/4\le1-1/d\); for \(d=3\), \(\alpha_3<\pi/3\) because \(2/3<\sqrt3/2\), also excluding \(b_1\).
For \(d=3\), \(b_2>3/4>2/3\). For \(4\le d\le6\), \(\sin(2\pi/d)\ge\sqrt3/2>5/6\ge(d-1)/d\), so \(\alpha_d<2\pi/d\), admitting \(b_2\). For \(d\ge7\),
\[
 \sin(2\pi/d)\le\sin(2\pi/7)<\sin(3\pi/10)
 =(1+\sqrt5)/4<6/7\le(d-1)/d,
\]
which excludes \(b_2\). All comparisons are exact and occur in the monotonic sine interval; \(d=1,2\) follow directly from (17).
H is partially injective, so a fixed core's unique predecessor is itself. Every listed fixed basin is a singleton, with source isotropy \(\mathbb Z\). At digit \(d>1\), its entire \(H=(\log d)\mathbb Z\), primitive time is \(\log d\), extension isotropy is trivial, and phase is \(h\bmod\log d\).
At digit 1, its entire \(H=0\), source and extension isotropy both remain \(\mathbb Z\), and phase is the whole real line. These are all zero-clock fixed cores, not a classification of every H zero-clock higher cycle.
For each \(q\), H has four digit-2 cores and one each of digits 3,4,5,6, as well as its digit-1 family. Equal times do not merge cores or different registers. In particular its \(\log4,\log6\) primitives are H-control results, not MAIN counterexamples.

## 6. Decision, limitations, and reproducibility

The same-object chain is intact: the legal map supplies its complete inverse, cylinder Jacobian, every-Borel IMAGE, all-point clock, actual history groupoid, entire isotropy image, and packet multiplicities. MAIN's full fixed ledger is nonempty and its four fixed primitive times are ordinary-prime times, but the uniqueness requirement already fails. Portfolio decision: STOP / FORK, without a selector, roof change, branch deletion, or parameter repair.
The step clocks of M/K/H are nonpositive and vanish exactly on digit-1 legal steps; V is everywhere zero on legal steps. They are signed groupoid clocks, not positive classical suspension roofs. The counting-cylinder owner is not silently promoted to a classical symplectic flow or an invariant probability system.
No higher-period census, global prime-only statement, all-prime coverage theorem, entropy/spectral/trace result, or external novelty claim is made. Strong naturalness and arbitrary-encoding/PROVES_TOO_MUCH remain OPEN. The controls own their formulas and conclusions separately. T3 is not audited, formal evaluation is unassigned, and Route B is not invoked.
The method is exact substitution, Borel change of variables, integer factorization, and complete trigonometric inequalities. There was no scientific code, numerical cutoff, simulation, external search/API, Git operation, PDF, operator construction, or publication. Mechanical full-file, link, identity/status, and hash checks are recorded in the author handoff.
Author exposure is not blind: the frozen card records readme lines 1–55, the complete 83-line 405 batch summary, a targeted old-card kick/cylinder search, and the complete 46-line 150 card including its outcome. Shared 407/402 author history and brief unverified design-time derivative/fixed-relation mental algebra were retained and disclosed; they were not reported as preregistered results or used for parameter tuning.
AI assistance disclosure: AI agents supplied the mathematical derivation, drafting, and internal checking; no human or external verification is certified. Main author `bilateral_transport_review` read the complete frozen 94-line 412 card and derived this paper. Same-author helper `direct_controls` first saw only the proposal message, then after release read only that frozen card and supplied the disjoint K/V/H control derivation; it read no main paper, peer/raw review, or evidence and wrote no files. The main author separately rederived the control conclusions. This helper is not an independent reviewer.
ARS-Codex supplied the workflow discipline for owner separation, scope, provenance, and explicit assistance disclosure, not mathematical evidence. Shared-history same-model assistance is NOT_CALIBRATED. No peer/raw/evidence files were read by this author. Root owns the card, independent-review workflow, and integration.
Related surfaces: [claim ledger](claim-ledger.md), [package README](README.md). Only the frozen short gate has been completed; no next candidate or higher census is started.

<!-- EOF: ANG-20260923-DKC01 paper -->
