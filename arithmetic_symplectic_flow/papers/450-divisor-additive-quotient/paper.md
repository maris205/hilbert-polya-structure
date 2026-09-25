# An owned logarithmic-measure clock with a nonprime fixed primitive

Candidate ID: `ANG-20260924-DAQ01`.
Outcome: `OWNED LOG-MEASURE CLOCK; NONPRIME FIXED PRIMITIVE — STOP / FORK`.
Paper: `450-divisor-additive-quotient`; date: 2026-09-24.
Batch: `TRANSPORT-PACKET-20260924-U`, round 1/5, authorized range 450–454.
Status: exact same-owner negative result; no numerical or higher-period census.
T0: owned Borel groupoid/clock; arithmetic T1 NOT PASSED; T2 prime support FAILS.
T3 NOT AUDITED; classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.
Internal AI work is `NOT_CALIBRATED`, not human or external verification.

## Abstract

We study three separately owned maps on the full positive quadrant with the
frozen measure \(dx\,dy/(xy)\). The MAIN map admits precisely the floor-divisibility
source and adds its integer quotient before a multiplicative exchange.
All actual inverse branches have the every-point IMAGE factor
\(J_q(U,V)=UV/(UV-q)\); the resulting signed source clock is
\(\kappa=\log(x/(x+q))\), not the Lebesgue inverse determinant.
We prove complete inverse coverage, global injectivity, the actual-lag groupoid,
all kernels, isotropy, incoming recursion and extension phases.
The complete MAIN fixed set is the singleton \((\varphi,\varphi)\),
\(\varphi=(1+\sqrt5)/2\), whose entire incoming source class is itself and whose
primitive positive clock is \(\log\varphi\). Since \(1<\varphi<2\), this violates
ordinary-prime support. The permission-OFF control has its own same fixed
primitive; the feedback-OFF control has a zero-clock fixed packet.
No higher-period classification, prime coverage, operator or Route result follows.

## 1. Frozen owners, arithmetic interface and question

For each owner separately let
\[
 X=(0,\infty)^2,\qquad d\mu(x,y)=\frac{dx\,dy}{xy},\qquad
 n=\lfloor x\rfloor,\quad d=\lfloor y\rfloor,\qquad
 A=\{(x,y)\in X:n\ge1,\ d\ge1,\ d\mid n\}.
\tag{1}
\]
The sigma-finite Borel measure is finite on every \([1/j,j]^2\), \(j\ge2\);
these boxes cover \(X\). No probability normalization or invariant measure is
assumed. The owner table gives the additive integer actually used by the map.

| Owner | Legal step source | Additive integer \(q\) | Actual map |
| --- | --- | --- | --- |
| MAIN \(M\) | \(A\) | \(n/d\) | \((y,(x+q)/y)\) |
| Permission-OFF \(G\) | \(X\) | \(0\) if \(d=0\), otherwise \(\lfloor n/d\rfloor\) | \((y,(x+q)/y)\) |
| Feedback-OFF \(Q\) | \(A\) | \(0\), regardless of the permission quotient | \((y,x/y)\) |

Every displayed output is positive: \(y>0\), \(x+q>0\), and \(q\ge0\).
All source sets and quotient functions are Borel. In \(M,Q\), \(X\setminus A\)
consists of terminal objects, not absorbing loops; units and every actual
incoming arrow remain. Integer cuts use the literal floor convention.
Axes and infinity are outside \(X\), not deleted exceptional states.

On \([N,N+1)\times[D,D+1)\) with integers \(1<D<N\), MAIN permission is
exactly \(D\mid N\). Its quotient enters the actual real update; both outputs
are reread next time. Thus divisor/composite symbolic admissibility feeds
geometry and geometry determines subsequent admissibility. Unit cells are also
part of the full owner and cannot be removed when they yield an adverse return.
There is no prime table, inserted \(\log p\), passive memory or borrowed clock.
The formula's strong naturalness and the `PROVES_TOO_MUCH` question remain OPEN.

The frozen gate is the complete fixed set of each owner, with its whole packet.
The necessary MAIN target is a nonempty positive ledger, only primitives
\(\log p\) for ordinary integer primes, and at most one full packet per prime;
all-prime coverage is an additional question. One actual adverse MAIN primitive
is enough to stop. Controls cannot supply that counterexample by transfer.

## 2. Complete inverses, including cuts and zero quotients

For \(Z=(U,V)\in X\), put \(P=UV\), \(d_Z=\lfloor U\rfloor\) and
\(m=\lfloor P\rfloor\). For every integer \(q\ge0\), define
\[
 \theta_q(Z)=(P-q,U),\qquad
 E_q=\{Z\in X:P>q\}.
\tag{2}
\]
The following are the actual inverse domains, not relaxed symbolic tests:
\[
\begin{aligned}
 B_{M,q}&=\{Z\in E_q:d_Z\ge1,\ \lfloor P-q\rfloor=d_Zq\},
       &&q\ge1,\\
 B_{G,q}&=\{Z\in E_q:
   [d_Z=0,\ q=0]\ \text{or}
   [d_Z\ge1,\ q=\lfloor\lfloor P-q\rfloor/d_Z\rfloor]\},
       &&q\ge0,\\
 B_Q&=\{Z\in X:\lfloor U\rfloor\ge1,\ \lfloor P\rfloor\ge1,
                          \lfloor U\rfloor\mid\lfloor P\rfloor\}.
\end{aligned}
\tag{3}
\]
For \(Q\), use only \(\theta_0\) on \(B_Q\).
All tests are Borel. In \(M\), (3) forces the reconstructed source integers
to be \(n=d_Zq\ge1,d=d_Z\ge1\), so its true quotient is exactly \(q\).
In \(G\), (3) is its own quotient law, including \(d_Z=0,q=0\); it does not
borrow MAIN permission. In \(Q\), \(B_Q\) is exactly the reconstructed source
condition \(A\). Direct substitution gives \(T_O\theta_q Z=Z\).
Conversely any legal predecessor satisfies \(y=U,x=P-q\), with its actual
quotient \(q\) and exactly these checks; hence \(\theta_qT_Oz=z\).
This proves both inverse identities and coverage of every predecessor.

For fixed \(q\), \(F_q(x,y)=(y,(x+q)/y)\) is a smooth bijection from \(X\)
onto \(E_q\), with smooth inverse (2). Restricting to (3) gives its actual
Borel source and image. Images of Borel subsets remain Borel because this
ambient map is a homeomorphism. No full map is asserted to be globally smooth
across the quotient cuts, nor is total \(G\) thereby asserted surjective.

In fact all three actual maps are injective, although all candidates in (3)
were retained. For integer \(q\),
\(\lfloor P-q\rfloor=m-q\), including integer \(P\).
For MAIN, (3) implies \(m=(d_Z+1)q\), permitting at most one \(q\).
For \(G\), \(d_Z=0\) already forces \(q=0\). If \(d_Z\ge1\), the function
\(q\mapsto\lfloor(m-q)/d_Z\rfloor\) is nonincreasing, so it cannot equal
two distinct increasing values \(q\). Thus again at most one actual inverse
exists. \(Q\) has only \(\theta_0\). This is an exact all-label argument,
not an imposed branch cutoff or a selected predecessor.

## 3. Every-point IMAGE for the frozen measure

Write \(\rho(x,y)=1/(xy)\). On the prescribed fixed-\(q\) inverse extension,
\[
 D\theta_q=
 \begin{pmatrix}V&U\\1&0\end{pmatrix},\quad
 |\det D\theta_q|=U,\quad
 J_q(Z)=\frac{\rho(\theta_qZ)U}{\rho(Z)}
       =\frac{UV}{UV-q}.
\tag{4}
\]
It is finite and positive at every point of each actual inverse domain;
\(J_0=1\). For every Borel \(E\) contained in that domain, smooth weighted
change of variables on the ambient diffeomorphism gives, also for infinite
integrals,
\[
 \mu(\theta_qE)=
 \int_E\frac{U}{U(UV-q)}\,dU\,dV
 =\int_E J_q(Z)\,d\mu(Z).
\tag{5}
\]
The proof covers any Borel subset, not only cell interiors. At assigned cuts
the fixed-\(q\) derivative in (4) prescribes the pointwise value. A measure
identity alone would determine a Radon--Nikodym version only almost everywhere;
we instead retain the card's analytic-germ version at every null state.

At a legal source \(z=(x,y)\), \(UV=x+q\), so its owned source clock is
\[
 \kappa_O(z)=-\log J_q(T_Oz)
           =\log\frac{x}{x+q}.
\tag{6}
\]
Consequently MAIN clocks are strictly negative, \(G\) clocks are nonpositive
and vanish exactly when its own \(q_G=0\), and every legal \(Q\) clock is zero.
There is no clock for a nonexistent terminal step. The Lebesgue determinant
\(U\) is not (4); using it alone would change the frozen owner.
For a specified legal length-\(r\) history, composition of its inverse germs
has IMAGE \(\exp(-S_r)\) at its target, by the density chain rule and (5);
the associated Borel identities follow by iterated change of variables.
No positive classical roof, invariant probability or measure repair is claimed.

## 4. All legal histories, actual lag and complete kernels

Let \(D_O^r\) be the set where \(r\) successive steps are legal;
\(D_O^0=X\), and \(T_O^0\) is the identity also at terminals. Put
\(S_0=0\) and \(S_r(z)=\sum_{j=0}^{r-1}\kappa_O(T_O^jz)\) on \(D_O^r\).
Retain the full groupoid
\[
 \mathcal G_O=\{(z,r-s,w):z\in D_O^r,\ w\in D_O^s,
                  T_O^rz=T_O^sw,\ r,s\ge0\},
 \qquad c(z,r-s,w)=S_r(z)-S_s(w).
\tag{7}
\]
Source is \(w\), range is \(z\); equal triples, not unequal lags, are identified.
If two witnesses give the same triple, their depths differ by a common integer.
The longer witnesses add the same legal sum after the same meeting state,
so their differences agree. Composition is
\((z,k,w)(w,l,v)=(z,k+l,v)\). To check this with witnesses \((r,s)\)
and \((u,v')\), if \(u\ge s\), extend the first range history by \(u-s\);
this is legal because its meeting state is \(T_O^sw\), whose next \(u-s\)
steps are available. The product has depths \((r+u-s,v')\);
the added sum equals \(S_u(w)-S_s(w)\), proving additivity.
If \(s\ge u\), extend the second source history by \(s-u\) instead.
Thus composition is legal and \(c\) is additive; reversal negates it.
In particular the forward arrow \((T_Oz,-1,z)\) has clock \(-\kappa_O(z)\).

Injectivity from Section 2 gives the useful complete normal form:
\[
\begin{array}{ll}
 k\ge0:&(z,k,w)\in\mathcal G_O
        \Longleftrightarrow z\in D_O^k,\ w=T_O^kz,
        \qquad c=S_k(z),\\
 k<0:&(z,k,w)\in\mathcal G_O
        \Longleftrightarrow w\in D_O^{-k},\ z=T_O^{-k}w,
        \qquad c=-S_{-k}(w).
\end{array}
\tag{8}
\]
Indeed, for \(r\ge s\), cancel the injective \(T_O^s\) in (7);
the other case reverses the arrow. The displayed shorter witnesses prove
the converses. Formula (8) retains every possible lag between periodic states.
The legal domains and iterates are Borel by induction. Formula (8) expresses
\(\mathcal G_O\subset X\times\mathbb Z\times X\) as countably many Borel
graphs and reversed graphs, supplying the stated Borel groupoid structure.
The Borel sums in (8) also make \(c\) Borel.

Let \(\ell(z,k,w)=k\) and let \(\mathcal U_O=\{(z,0,z):z\in X\}\).
For all three owners,
\(\ker\ell=\ker\ell\cap\ker c=\mathcal U_O\).
MAIN has \(\ker c=\mathcal U_M\), since every nonempty connecting segment
in (8) has strictly negative \(S\).
For \(G\), \(\ker c\) consists of units and exactly the nonzero-lag arrows
whose connecting segment in (8) has \(q_G=0\) at every step.
Nonpositive summands prove both necessity and sufficiency.
For \(Q\), \(c=0\) on all of \(\mathcal G_Q\), so \(\ker c=\mathcal G_Q\).
These are global kernel descriptions, not deductions from the fixed window.

## 5. Entire incoming sets, isotropy, heights and repetitions

For an arbitrary subset \(B\subset X\), define its full predecessor set by
\[
 I_M(B)=\bigcup_{q\ge1}\theta_q(B\cap B_{M,q}),\quad
 I_G(B)=\bigcup_{q\ge0}\theta_q(B\cap B_{G,q}),\quad
 I_Q(B)=\theta_0(B\cap B_Q).
\tag{9}
\]
Set \(I_O^0(B)=B\) and iterate (9) with no depth restriction.
The entire source orbit of \(z\) is
\[
 [z]_O=\bigcup_{\substack{s\ge0\\z\in D_O^s}}\ 
                   \bigcup_{r\ge0}I_O^r(\{T_O^sz\}).
\tag{10}
\]
This is equivalent to (7), hence includes every incoming depth and all
terminal classes: for a terminal \(t\), (10) is just
\(\bigcup_{r\ge0}I_O^r(\{t\})\). It is an exact unrestricted recursion,
not a finite census or a claim that the recursion terminates.

For each owner, a nonperiodic source state has only unit isotropy, by (8).
If \(z\) has least positive source period \(p\), every legal period is a
multiple of \(p\): divide an arbitrary period by \(p\) along the actual cycle,
and a nonzero remainder would contradict minimality. Thus, writing
\[
 K=S_p(z),\qquad
 \mathcal G_{O,z}^{z}=\{(z,mp,z):m\in\mathbb Z\},\qquad
 c(z,mp,z)=mK,\qquad H_z=K\mathbb Z,
\tag{11}
\]
gives the entire isotropy and its image, not just one observed return.
All source-cycle states have the same \(K\).
There are no off-cycle incoming states to a cycle: each cycle point already
has its cycle predecessor, which is its unique actual predecessor;
induction on incoming depth proves the claim.
For nonperiodic states, including every terminal class, \(H_z=\{0\}\).

The real extension keeps every \((z,h)\in X\times\mathbb R\).
An arrow \(g=(z,k,w)\) sends \((w,h)\) to \((z,h+c(g))\).
Its isotropy at \((z,h)\) is exactly the source isotropy with zero clock.
For a cycle in (11), this is all \(p\mathbb Z\) if \(K=0\), and only the
unit if \(K\ne0\); nonperiodic extension isotropy is trivial.
In particular MAIN cycles always have \(K<0\); \(G\) cycles have \(K\le0\),
with equality exactly when all their step quotients vanish; \(Q\) has
\(H_z=\{0\}\) everywhere, while retaining any source-cycle isotropy.
These statements are conditional on actual cycles, not a higher-period census.

Translation of height by \(t\in\mathbb R\) commutes with every extension arrow
and acts on its orbit SET. Its stabilizer at a class over \(z\) is exactly
\(H_z\): returning to that class means precisely an isotropy arrow of clock \(t\).
For a fixed source orbit choose one anchor \(a\) and one actual arrow
\(g_z:a\to z\), and write \(b_z=c(g_z)\). All extension classes over this orbit
are parameterized by
\[
                  h-b_z\pmod{H_a}\ \in\mathbb R/H_a.
\tag{12}
\]
A different connecting arrow changes \(b_z\) by an element of \(H_a\), so
the phase is well-defined. This describes all phases, not a selection.
No global measurable selector, Hausdorff quotient or smooth flow is assumed.
For \(K\ne0\), the full packet has primitive \(|K|\) and positive repeats
\(j|K|\), \(j\ge1\); if \(K=0\) there is no positive primitive.
The source cycle, every incoming state and every phase belong to that packet.
Distinct source orbits are never merged just because their primitive lengths agree.

## 6. Complete global fixed gate and separate controls

Let \(\varphi=(1+\sqrt5)/2\), \(f=(\varphi,\varphi)\), and \(e=(1,1)\).
The first coordinate of every fixed equation forces \(x=y=a>0\).
For MAIN, legality forces \(a\ge1\), hence \(n=d=\lfloor a\rfloor\ge1\)
and the actual quotient is \(1\). The second equation is
\(a^2=a+1\), whose only positive root is \(\varphi\).
Since \(1<\varphi<2\), its floors are both \(1\), verifying all source checks.
Thus \(\operatorname{Fix}(T_M)=\{f\}\) globally, not merely in a selected cell.

For the independently owned \(G\) control, \(0<a<1\) gives \(n=d=0,q_G=0\);
its equation \(a^2=a\) has no root in that interval.
For \(a\ge1\), its own quotient is \(\lfloor n/d\rfloor=1\), so the same
quadratic has exactly the admissible root \(\varphi\).
Thus \(\operatorname{Fix}(T_G)=\{f\}\) on its whole positive source.
This proof retains every zero quotient, \(n=0\) state and cut, including \(a=1\).

For the separately owned \(Q\) control the equation is \(a^2=a\).
Its unique positive root \(a=1\) is legal in \(A\), including the assigned cut.
Consequently \(\operatorname{Fix}(T_Q)=\{e\}\).
The excluded root \(0\) is not a state of \(X\); no terminal state becomes a loop.

At target \(f\), \(d_Z=1\) and
\(m=\lfloor\varphi^2\rfloor=\lfloor\varphi+1\rfloor=2\).
MAIN's full inverse test is \(2-q=q\), so only \(q=1\) survives.
\(G\)'s own test is also \(q=\lfloor(2-q)/1\rfloor=2-q\).
Both reconstruct \(f\), so (9) proves at every depth
\(I_M^r(\{f\})=I_G^r(\{f\})=\{f\}\).
For \(Q\), the sole candidate \(\theta_0(e)=(1,1)\) is legal, giving
\(I_Q^r(\{e\})=\{e\}\). These exhaust the incoming source classes;
all height phases are kept below, with no feeders removed.

For MAIN and \(G\) separately, (4)–(6) give
\[
 J(f)=\frac{\varphi^2}{\varphi^2-1}=\varphi,\qquad
 \kappa(f)=-L,\qquad L=\log\varphi>0.
\tag{13}
\]
Each source least period is \(1\), with all isotropy lags \(k\in\mathbb Z\),
clock \(c(f,k,f)=-kL\), and entire \(H_f=L\mathbb Z\).
On each fixed packet the clock, lag and joint kernels are just the unit;
extension isotropy is trivial, and every phase \(h\bmod L\) is retained.
There is one full physical height-translation circle per owner, primitive
\(L\) and positive repeats \(jL\), not one packet for each phase.
The two owners' packets are not identified or transferred.

For \(Q\) at \(e\), \(J=1,\kappa=0\), with source isotropy \(\mathbb Z\),
all of it in the clock kernel, and lag/joint kernels equal to the unit.
Its entire \(H_e=\{0\}\), extension isotropy remains \(\mathbb Z\), and phases
are all \(h\in\mathbb R\). Height translation is free there: a zero-clock
source fixed point does not make a positive physical return.

MAIN therefore has a nonempty positive ledger, but its actual primitive
satisfies \(0<L<\log2\). No ordinary integer prime lies in \((1,2)\);
hence \(L\ne\log p\) for every such prime. Equation (11) and the complete
incoming proof exclude a smaller hidden positive generator.
This MAIN counterexample, not the similar control, decides STOP / FORK.
No higher-period calculation, packet selector or clock rescaling is needed.

## 7. Gate, limits and reproducibility

| Obligation | Exact evidence | Assessment |
| --- | --- | --- |
| Full owner and same-object ledger | (1)–(12), every actual inverse and null-point clock retained | T0 owned |
| Divisor interface / endogenous clock | True floor-divisibility feedback and own log-measure IMAGE | Arithmetic T1 NOT PASSED; naturalness OPEN |
| Positive primitive target | MAIN full fixed packet with \(0<\log\varphi<\log2\) | Necessary prime support FAILS; STOP / FORK |
| Higher periods / uniqueness / all-prime coverage | General ledger only, no period-\(\ge2\) classification | Not certified; unnecessary for this stop |
| Classical / analytic / formal Routes | No classical roof, operator, determinant or trace supplied | Classical NOT APPLICABLE; T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED |

The frozen measure, source, maps, lag convention and all phases stayed intact.
No universal no-go for divisor dynamics, logarithmic measures or other owners
is asserted. This record neither constructs a new fork nor authorizes round 455.
Exact algebra and weighted change of variables are the proof method;
no scientific numerical computation, finite scan or external source is used.
The input is the complete 93-line [frozen card](candidate-card.md), SHA256
`853f2b6f2bb36613c162614ebadf7fadf2a2f447a6f24669ed1766b0e45f8b59`.
The [claim ledger](claim-ledger.md) and [package README](README.md) delimit the
same result. Reproduction requires these definitions and the proofs above,
not unavailable data or an unpublished numerical output.

## 8. Design exposure and AI assistance

Root proposed the tuple with informal fixed/clock feasibility thoughts;
the author supplied inverse-domain design before freeze. This is not blind
prediction or sealed preregistration. The shared historical author context
includes prior packages, but no old proof is used as a lemma here.
Design collision reads were card 400 lines 1–76 (not EOF, total 104;
prefix SHA256 `dc8c1c17380197b700b47fae8019da9a7a0c0a623003a123dd9357607b29294b`)
and card 433 lines 1–72 (not EOF, total 104;
prefix SHA256 `fab0e9d7d7b3e661c154968d6ef8440fcc12ba70f9d21728b3931de6d7196303`).
Metadata search additionally exposed 400 line 77's informal Lyness-density
wording. No result or nonconjugacy/novelty certificate is imported from them.
During author guidance refresh, historical summary prefixes
`papers/README.md` lines 1–200 and `readme.md` lines 1–160
(neither to EOF) were also displayed, exposing outcome metadata; this exceeded
minimal card-only access and is disclosed, not relabelled as independence.
Their displayed-prefix SHA256 receipts are respectively
`949a4a18f7927f174e6fe3ccd898aac90ca5d1b232cc85cf83e50f3009c7d26c`
and `2e27f68db5a84071c119346f3285a33228a46afc59378df2eec7e3b1796087de`.
No current scope, raw review, reviewer answer or peer proof was read.

AI agents supplied mathematical derivation, drafting and internal checking.
Author `bilateral_transport_review` owns these three author surfaces.
Same-author helper `bilateral_transport_review/direct_controls` supplied
only bounded \(G/Q\) fixed/incoming/clock/kernel/phase checks. Its scientific
access receipt is the same frozen 93-line card, read through EOF with the SHA256
above; it additionally read the ARS router, academic-paper workflow and
argument-builder role instructions. It read no author MAIN proof or review
answer and wrote no file. This is author aid, not an independent review seat;
the author derived and checked the three-owner proofs presented here.
ARS research-writing guidance informed claim boundaries, evidence organization
and this disclosure; it did not supply a theorem or an external review.
Same-model/shared-history work is `NOT_CALIBRATED`; no human, external or
cross-model verification is certified, and no venue-specific compliance is claimed.
There are no human/animal subjects or private datasets. Funding information
was not supplied; conflicts of interest were not assessed.

EOF — DAQ01 author proof; frozen after final self-read and receipt.
