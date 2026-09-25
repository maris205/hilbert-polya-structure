# Random-lookback coprime histories: an owned infinite-memory clock with composite primitive times

**Paper:** `371-random-lookback-coprime`  
**Candidate:** `ANG-20260922-RLC01`  
**Batch / date:** `MEASURED-HISTORY-20260922-E`, round 2/5; 2026-09-22  
**Status:** `OWNED INFINITE-MEMORY IMAGE CLOCK; COMPOSITE CONSTANT PACKETS — STOP / FORK`  
**Coordinates:** broadened T0–T2 only; classical A0/A1/A2 NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED.

## Abstract

The frozen source is the full one-sided history space on all integers at least two, with a probability constructed from resetting random ancestry and arbitrarily remote coprimality witnesses. We prove the construction, its entire-past conditional law, every-Borel prefix IMAGE identities, full support, absence of atoms, and the uniquely determined continuous all-point conditional version. The output is genuinely nonproduct and has no finite conditional memory. Its actual retained-lag groupoid owns an additive clock and a complete primitive-necklace ledger. Nevertheless, every constant history \(a^\infty\) has primitive time \(\log(2a(a-1))\); in particular, the full time stabilizer at \(2^\infty\) is \((\log4)\mathbb Z\), not \((\log2)\mathbb Z\). This violates the frozen prime-time target. Three independently measured controls receive the same complete ownership and word-ledger audit. The result is a scoped stop, not a no-go theorem for nonproduct histories or other clocks.

## 1. Identity, lineage, and scope

The governing source is the [frozen card](candidate-card.md), not a selected conull subset. Put \(A=\{2,3,\ldots\}\), \(X=A^{\mathbb N_0}\), with coordinates running from recent to distant past, and give \(X\) its discrete product topology and Borel structure. This is a Polish source; no local compactness, symplectic form, or manifold quotient is assumed. The map \(T(x_0,x_1,\ldots)=(x_1,x_2,\ldots)\) is everywhere defined, with every inverse \(I_a(x)=ax\). There are no terminal points.

The exact lineage is common-divisor exclusion in full histories, deformed into selection of one arbitrarily remote witness followed by coprime sampling and an explicit reset. Hard all-pair exclusion is not preserved: this is a probabilistic deformation, not a conjugacy to the earlier hard language. Every integer letter, null periodic history, and exceptional history remains in the carrier. The laws \(\rho\), reset probability \(1/2\), and lookback probabilities \(2^{-r}\) are declared designs, not consequences of prime periods.

The same-object chain is \((X,T,\mu,q)\), its actual prefix-replacement groupoid \(G\), its IMAGE cocycle \(c\), and the full real extension. There is no inserted roof, noise-coordinate dynamical owner, determinant, operator, or later geometric lift. Physical time here means the specified height-translation action on the orbit **set**, not an unproved manifold flow or invariant flow measure.

## 2. Four separately constructed probability owners

Write \(R_a=\rho(a)=1/[a(a-1)]\), and define
\[
Z_b=\sum_{\gcd(a,b)=1}R_a,\qquad W_b=\sum_{\gcd(a,b)>1}R_a,\qquad
K_b(a)=\frac{R_a1_{\gcd(a,b)=1}}{Z_b},\qquad K_b^{\rm sh}(a)=\frac{R_a1_{\gcd(a,b)>1}}{W_b}.
\]
Telescoping gives \(\sum_{a=2}^N R_a=1-1/N\). Also \(Z_b\ge R_{b+1}>0\), \(W_b\ge R_b>0\), and \(Z_b+W_b=1\); both denominators are strictly less than one. Thus both displayed kernels are probability laws, independently of any later construction.

The following table specifies four distinct noise/output owners. In each row the reset law is \(R\), the reset probability is \(1/2\), and all source points and prefix branches are retained.

| Owner | Nonreset kernel \(D_b(a)\) | Lookback law \(\ell_r\) | Conditional prescription |
| --- | --- | --- | --- |
| MAIN | \(K_b(a)\) | \(2^{-r}\), \(r\ge1\) | \(q_a(x)=R_a/2+\frac12\sum_r\ell_rD_{x_{r-1}}(a)\) |
| ARITHMETIC-OFF | \(R_a\) | \(2^{-r}\) | \(q_a^{\rm off}(x)=R_a\) |
| NEAREST-ONLY | \(K_b(a)\) | \(1_{r=1}\) | \(q_a^{\rm near}(x)=(R_a+K_{x_0}(a))/2\) |
| SHARED-DIVISOR | \(K_b^{\rm sh}(a)\) | \(2^{-r}\) | \(q_a^{\rm sh}(x)=R_a/2+\frac12\sum_r2^{-r}K_{x_{r-1}}^{\rm sh}(a)\) |

For each row separately, take independent triples \((B_t,L_t,U_t)\), \(t\in\mathbb Z\), with fair \(B_t\), law \(\ell\) for \(L_t\), and uniform \(U_t\in[0,1)\). For a probability \(P\) on \(A\), let \(Q_P(u)=\min\{a:\sum_{j=2}^aP(j)>u\}\); this exists for every \(u<1\). Starting at \(t\), follow \(s\mapsto s-L_s\) when \(B_s=1\), stopping at \(B_s=0\). At the stopping site set \(Y_s=Q_R(U_s)\); along the finite chain back to \(t\), set \(Y_v=Q_{D_{Y_{v-L_v}}}(U_v)\). For a never-stopping chain, set \(Y_t=2\), exactly as frozen. Define the row's own \(\mu=\operatorname{Law}(Y_0,Y_{-1},\ldots)\).

**Proposition 1 (construction and conditioning).** Each row defines a measurable stationary output process and a probability \(\mu\) with
\[
\mathbb P(Y_t=a\mid \sigma(Y_s:s<t))=\frac{R_a}{2}+\frac12\sum_{r\ge1}\ell_rD_{Y_{t-r}}(a)\quad\text{a.s.},
\qquad \mu(I_aE)=\int_Eq_a\,d\mu
\tag{1}
\]
for every Borel \(E\subset X\).

**Proof.** The ancestor indices strictly decrease, so no site is queried twice. Conditional on the finite indices and noise already exposed along the exploration, the next unqueried \(B\) is still fair. Induction gives probability \(2^{-n}\) of surviving the first \(n\) reset tests, hence zero probability of a never-stopping chain. A countable union over \(t\) gives a probability-one event on which all chains terminate. The finite-chain events are measurable, as are their quantile outputs; their countable union and the constant fallback make every \(Y_t\) measurable.

On that probability-one event, the ancestor chain of a parent is exactly the corresponding tail of the child's chain. Consequently shared ancestors have consistent values, and the stated recursion holds simultaneously at all sites. On its null complement the fallback defines outputs but is **not** asserted to satisfy the recursion. Both the finite-chain rule and fallback commute with translations of the noise indices; the product noise is stationary, so the output is stationary.

Each \(Y_s\), \(s<t\), is measurable with respect to noise at indices at most \(s\). The entire output past is therefore independent of the fresh triple at \(t\). Conditioning the almost-sure recursion on this whole past, rather than on a finite truncation, gives the first formula in (1). Stationarity identifies the law of \((Y_{-1},Y_{-2},\ldots)\) with \(\mu\); testing the conditional identity on an arbitrary Borel past event gives the second formula. This proof is applied to each row's own product noise and output law; no control borrows MAIN's measure. \(\square\)

## 3. Full support, atoms, regular versions, and genuine memory

For every owner, letter, and history,
\[
0<R_a/2\le q_a(x)\le R_a/2+1/2\le3/4,\qquad \sum_aq_a(x)=1.
\tag{2}
\]
For a finite word \(u=a_0\cdots a_{m-1}\), set
\[
q_u(x)=\prod_{j=0}^{m-1}q_{a_j}(a_{j+1}\cdots a_{m-1}x),\qquad q_\varnothing=1.
\tag{3}
\]
Iterating (1), including its integral change-of-variable form for nonnegative Borel functions, yields \(\mu(uE)=\int_Eq_u\,d\mu\). Therefore every cylinder has mass at least \(\prod_{j<m}(R_{a_j}/2)>0\), and at most \((3/4)^m\). Cylinders form a topology basis, proving full support; decreasing cylinders at any specified history prove that every singleton has mass zero. In particular, all periodic histories below are null but are not removed.

For MAIN and SHARED, agreement of \(x,y\) in the first \(N\) coordinates gives
\[
|q_a(x)-q_a(y)|\le\frac12\sum_{r>N}2^{-r}=2^{-N-1}.
\tag{4}
\]
Thus the prescribed \(q_a\) is continuous everywhere; NEAR is locally constant and OFF is constant. Positivity makes every finite prefix product, logarithm, and prefix ratio continuous on its actual branch domain. The every-Borel identity determines \(q_a\) almost everywhere; full support then makes its continuous version unique everywhere. Indeed, two different continuous versions differ on a nonempty open set, contradicting almost-everywhere equality. Consequently the values at null cycles are fixed by the regular version, not fitted afterward.

**Proposition 2 (actual memory).** MAIN and SHARED are nonproduct and admit no conditional law depending on only finitely many most recent coordinates. NEAR is nonproduct with one-step conditional memory. OFF is the product law \(R^{\mathbb N_0}\).

**Proof.** For any \(N\ge0\), compare the all-2 history with the history differing only at coordinate \(N\), where the letter is 3. In MAIN, \(K_2(2)=0<K_3(2)\); in SHARED, \(K^{\rm sh}_2(2)>0=K^{\rm sh}_3(2)\). Their \(q_2\) values differ although their first \(N\) coordinates agree. This is not just a discrepancy at two null points: if \(q_2\) agreed almost everywhere with a function of that finite prefix, it would be constant almost everywhere on each prefix cylinder. Continuity and full support within that cylinder would force it to be constant everywhere there, a contradiction. A stationary product law would have constant whole-past conditional probabilities, so both laws are nonproduct.

For NEAR the same comparison at coordinate zero makes \(q_2^{\rm near}\) nonconstant; the displayed rule proves its one-step conditional property. For OFF, (1)–(3) give \(\mu([u])=\prod_{j<m}R_{a_j}\), determining the product probability on the cylinder-generated Borel sigma field. \(\square\)

## 4. Actual groupoid, every-Borel IMAGE, and complete kernels

For each owner use the same underlying retained-lag set
\[
G=\{(z,k,y): k=m-n,\ m,n\ge0,\ T^mz=T^ny\}.
\tag{5}
\]
Source is \(y\), range is \(z\), inverse is \((y,-k,z)\), and \((z,k,y)(y,l,w)=(z,k+l,w)\). Equal triples, not distinct presentations, are identified. Its topology is generated by prefix bisections
\[
B(u,v;O)=\{(u\xi,|u|-|v|,v\xi):\xi\in O\},\quad O\subset X\text{ open},
\]
with the resulting Borel structure. All finite words, empty words, and all tails occur. The source and range restrictions are homeomorphisms on these sets.

For the actual branch \(\theta_{u,v}(v\xi)=u\xi\), its IMAGE derivative is
\[
J_{u,v}(v\xi)=q_u(\xi)/q_v(\xi).
\tag{6}
\]
Indeed, for every Borel \(E\), \(\mu(uE)=\int_Eq_u\,d\mu=\int_{vE}J_{u,v}\,d\mu\), using (3). This establishes every-Borel IMAGE, not an aggregate degree or a formal count of inverse branches.

Put \(\kappa(z)=-\log q_{z_0}(Tz)\), \(A_m(z)=\sum_{i=0}^{m-1}\kappa(T^iz)\), \(A_0=0\). Then
\[
c(z,m-n,y)=A_m(z)-A_n(y)
             =-\log\frac{q_u(\xi)}{q_v(\xi)},\quad z=u\xi,\ y=v\xi.
\tag{7}
\]
The identity \(q_{uw}(\xi)=q_u(w\xi)q_w(\xi)\) shows cancellation under a common extension of the prefixes. Two witnesses of the same triple have equal length difference and can be aligned by just such a common extension; hence (7) is independent of witnesses at every point. Aligning middle prefixes in two composable arrows gives cancellation of their intermediate products, proving additivity. Thus inverses negate \(c\), identities have \(c=0\), and this is the clock of the IMAGE owner (6), not of another measure.

Here are complete, explicit membership formulas for all kernels, including nonperiodic tails. For MAIN or SHARED use its own \(D\) and define \(h_a(\xi)=\sum_{r\ge1}2^{-r}D_{\xi_{r-1}}(a)\). For \(u=a_0\cdots a_{m-1}\), write
\[
P_u(\xi)=\prod_{j=0}^{m-1}
\left[\frac{R_{a_j}}2+\frac12\left(
\sum_{r=1}^{m-j-1}2^{-r}D_{a_{j+r}}(a_j)
+2^{-(m-j-1)}h_{a_j}(\xi)\right)\right],\qquad P_\varnothing=1.
\tag{8}
\]
Splitting the geometric tail in (3) proves \(P_u=q_u\). The tail profiles are only evaluations, never a quotient identifying different histories. For NEAR and OFF the corresponding full formulas are
\[
P_u^{\rm near}(\xi)=
\left[\prod_{j=0}^{m-2}\frac{R_{a_j}+K_{a_{j+1}}(a_j)}2\right]
\frac{R_{a_{m-1}}+K_{\xi_0}(a_{m-1})}2\quad(m\ge1),\qquad
P_u^{\rm off}=\prod_{j<m}R_{a_j},
\tag{9}
\]
with both empty products equal to one. If \(\lambda(z,k,y)=k\), the following conditions are necessary and sufficient, for every \(u,v,\xi\), without a length or tail cutoff:
\[
\begin{aligned}
(u\xi,|u|-|v|,v\xi)\in\ker\lambda&\iff |u|=|v|,\\
(u\xi,|u|-|v|,v\xi)\in\ker c&\iff P_u(\xi)=P_v(\xi),\\
(u\xi,|u|-|v|,v\xi)\in\ker\lambda\cap\ker c
&\iff |u|=|v|\ \text{and}\ P_u(\xi)=P_v(\xi).
\end{aligned}\tag{10}
\]
Equations (8)–(10) give full kernel sets, not only their isotropy parts or a finite test. In OFF the clock condition is exactly \(\prod_{a\in u}a(a-1)=\prod_{b\in v}b(b-1)\), with occurrences counted. For example \(u=(4)\), \(v=(2,3)\) satisfy it although their lengths differ. Thus clock zero must not be conflated with lag zero.

## 5. Entire isotropy, incoming histories, phases, and repetitions

Retain \(X\times\mathbb R\), with every arrow
\[
(y,h)\longrightarrow(z,h+c(g)),\quad g=(z,k,y).
\tag{11}
\]
Height translation descends to the orbit set since it commutes with (11). At a target \((z,s)\), **all** incoming arrows are enumerated by \(m,n\ge0\), \(v\in A^n\),
\[
y=vT^mz,\quad g=(z,m-n,y),\quad\text{source height }s-c(g).
\tag{12}
\]
Repeated descriptions are identified exactly when the underlying triples agree. No finite incoming depth, noise ancestry, representative section, or conull deletion is imposed.

For a nonempty primitive word \(w=w_0\cdots w_{d-1}\), with indices modulo \(d\), define
\[
Q_j(w)=q_{w_j}((w_{j+1}\cdots w_{d-1}w_0\cdots w_j)^\infty),
\quad \mathcal T_w=-\log\prod_{j=0}^{d-1}Q_j(w)>0.
\tag{13}
\]
Strict positivity follows from (2). Source isotropy is trivial at histories that are not eventually periodic. At a history with least eventual period \(d\), it is exactly \(d\mathbb Z\): a nonzero equality \(T^mx=T^nx\) is precisely an eventual period, and the integer periods of its eventual periodic tail are the multiples of its least period. If \(x\) enters the periodic tail \(w^\infty\) after \(N\) shifts, the lag-\(d\) isotropy arrow has
\[
c(x,d,x)=A_{N+d}(x)-A_N(x)=\mathcal T_w.
\tag{14}
\]
Consequently on this entire isotropy group \(c(x,kd,x)=k\mathcal T_w\). The finite prehistory cancels; changing the cyclic starting point merely permutes the factors in (13).

Define \(H_x=\{c(g):g\in G_x^x\}\). It equals \(\{0\}\) in the noneventually-periodic case and \(\mathcal T_w\mathbb Z\) otherwise. The fixed-object isotropy of the **real extension** is trivial everywhere, because it is the clock-zero part of source isotropy and (14) is injective. This does not erase source isotropy: its nonidentity arrows move the real height. Nor does it eliminate time periods: the height-translation stabilizer of an orbit-set point is exactly \(H_x\).

Each source orbit over a periodic tail is identified by one primitive word up to cyclic rotation; arbitrary finite prefixes and all rotations lie in that same source orbit. Conversely tail equality of two periodic sequences forces the same primitive cyclic word. Thus primitive closed-time packets are precisely primitive necklaces, one per necklace, even when their numerical times coincide. All their phases are retained: over any source orbit the extension orbits are parametrized, as sets, by \(\mathbb R/H_x\). To verify this, fix one reference source point and transport height there using an actual arrow; changing that arrow changes height by exactly \(H_x\). This coordinate device removes no source objects and asserts no Hausdorff quotient topology.

Repeating a word \(k\) times gives \(k\mathcal T_w\), not a new primitive packet; finite prefixes do not change its primitive time. Nonperiodic-tail classes have phase set \(\mathbb R\) and no positive stabilizer. These statements, (8)–(12), and the entire word formula (13) apply separately to all four owners.

## 6. Complete word formulas and all constant/two-letter packets

For MAIN and SHARED, grouping the geometric lookback sum by its residue modulo \(d\) gives the exact all-word formula
\[
Q_j(w)=\frac{R_{w_j}}2+
\frac{1}{2(1-2^{-d})}\sum_{r=1}^{d}2^{-r}D_{w_{j+r}}(w_j).
\tag{15}
\]
Every \(r\ge1\) appears once in these geometric series, which are absolutely convergent. For NEAR, \(Q_j(w)=(R_{w_j}+K_{w_{j+1}}(w_j))/2\); for OFF, \(Q_j(w)=R_{w_j}\). These formulas and (13) constitute the full primitive ledger without an enumeration cutoff.

Every constant \(a^\infty\), \(a\ge2\), is primitive of source period one. Its factor and its least positive time are:

| Owner | Constant factor \(Q(a^\infty)\) | Primitive time |
| --- | --- | --- |
| MAIN | \(R_a/2\) | \(\log(2a(a-1))\) |
| OFF | \(R_a\) | \(\log(a(a-1))\) |
| NEAR | \(R_a/2\) | \(\log(2a(a-1))\) |
| SHARED | \(R_a(1/2+1/(2W_a))\) | \(-\log[R_a(1/2+1/(2W_a))]\) |

For every pair \(a\ne b\), the word \(ab\) is primitive of source period two. Put \(\delta=1_{\gcd(a,b)=1}\), \(\epsilon=1-\delta\). The following table gives \(F_a=Q_0(ab)\); its second factor \(F_b\) is obtained by exchanging \(a,b\), and the exact least time is always \(-\log(F_aF_b)\).

| Owner | \(F_a\) for all \(a\ne b\) |
| --- | --- |
| MAIN | \(R_a(1/2+\delta/(3Z_b))\) |
| OFF | \(R_a\) |
| NEAR | \(R_a(1/2+\delta/(2Z_b))\) |
| SHARED | \(R_a(1/2+\epsilon/(3W_b)+1/(6W_a))\) |

Indeed, odd lookbacks see \(b\) with total weight \(2/3\) and even lookbacks see \(a\) with weight \(1/3\). The coprime self-kernel is zero, whereas the shared-divisor self-kernel is \(R_a/W_a\); substitution proves the table. When \(a=b\), the displayed two-letter word is a repetition of the constant packet and has twice its primitive time, not a new packet. For MAIN noncoprime distinct pairs, the formula simplifies to \(\log(4a(a-1)b(b-1))\), with no prime filtering.

In particular, the frozen \((2,3)^\infty\) test gives
\[
\begin{aligned}
\mathcal T_{23}^{\rm MAIN}&=-\log\!\left[\frac1{12}
  \left(\frac12+\frac1{3Z_3}\right)\left(\frac12+\frac1{3Z_2}\right)\right],\\
\mathcal T_{23}^{\rm NEAR}&=-\log\!\left[\frac1{12}
  \left(\frac12+\frac1{2Z_3}\right)\left(\frac12+\frac1{2Z_2}\right)\right],\\
\mathcal T_{23}^{\rm OFF}&=\log12,\\
\mathcal T_{23}^{\rm SHARED}&=-\log\!\left[\frac1{12}
  \left(\frac12+\frac1{6W_2}\right)\left(\frac12+\frac1{6W_3}\right)\right].
\end{aligned}\tag{16}
\]
These are exact convergent-series expressions, not numerical approximations. Their full stabilizers are the corresponding times times \(\mathbb Z\); their extension fixed-object isotropy is trivial.

## 7. Decisive adverse finding, own controls, and stop

MAIN's constant packet \(2^\infty\) has \(Q=1/4\) and \(\mathcal T=\log4\). Equations (13)–(14) prove its **entire** time stabilizer is \((\log4)\mathbb Z\). It cannot be called the second repetition of a hidden \(\log2\) packet in this orbit: that smaller time is absent from its stabilizer. More generally \(2a(a-1)\) is composite for every \(a\ge2\), so all MAIN constant packets violate the prescribed prime-time target. This is a full-carrier obstruction, not a measure-zero deletion license.

Each control has its own completed construction, regular IMAGE, kernels, incoming arrows, and full necklace ledger above. OFF has the constant \(2^\infty\) time \(\log2\), but already \(3^\infty\) has primitive time \(\log6\); its apparent prime example does not rescue its target. NEAR has the same composite constant times as MAIN. SHARED's constant-2 factor is \(\frac14(1+1/W_2)>1/2\), since \(W_2<1\), and is at most \(3/4<1\) by (2). Hence its primitive time lies strictly between zero and \(\log2\), smaller than every prime logarithm. These are control-specific conclusions, not transfers of MAIN's measure or times.

| Obligation | Established for this owner | Boundary |
| --- | --- | --- |
| T0 source and IMAGE ownership | Full-history probability, all branches, all-point version, retained lag and real extension | No classical symplectic or manifold claim |
| T1 arithmetic and clock | Coprime conditional feedback, genuine infinite memory, own IMAGE cocycle | Design constants and strong naturalness remain OPEN |
| T2 packets and target | Complete necklace/stabilizer/repetition formula; all constant and two-letter cases | Prime-time target FAILS at \(2^\infty\) |
| T3 / formal coordinates / B | NOT AUDITED / UNASSIGNED / NOT INVOKED | No operator, determinant, external roof, or Route transfer |

**Decision: STOP / FORK.** The arithmetic conditional owner is rigorous but does not satisfy the frozen prime-period normalization. No reset, lag, weight, scaling, subsource, or regular-version adjustment is authorized within this candidate. Higher-word prime equalities and prime coverage are unnecessary for this stop and are not classified beyond the exact general ledger. Infinite-memory dependence itself is not evidence that primitive times have the required arithmetic meaning.

## 8. Evidence, provenance, and integrity

This is an exact proof record using the [candidate card](candidate-card.md); the integrated [claim ledger](claim-ledger.md) and separately assigned [review record](evidence/review.md) are root-owned integration artifacts, whose completion is not presupposed by this proof. No scientific numerical experiment, external source, prime table, literature search, or novelty claim is used. Reproduction consists of checking the probability construction, the every-Borel change of variables, and the exact word identities above; there is no finite-truncation inference.

The source proposer previously authored the hard-memory 367 paper. During definition scouting it read card 065 lines 1–11 and card 369 lines 1–94, including that card's appended outcome, but not their proofs/papers/reviews. Root had prior 365–369 results and anticipated a constant-history test. The definitions preceded the frozen-card/CP1 mathematical release; this author then read the complete 94-line card and paper template, and independently derived this main proof without reading peer or independent-review material. Shared history is NOT_CALIBRATED, and the source author is not an independent reviewer. Null-noise fallback is explicitly limited as in Proposition 1.

The work is AI-assisted internal mathematical research, with root-owned integration and separately assigned review, not external peer review. There are no human-subject, private-data, or empirical-data claims. Funding and conflict declarations have not been supplied and are not inferred. All claims concern this unchanged owner; all missing geometric, analytic, naturalness, and formal-Route obligations remain unfilled.
