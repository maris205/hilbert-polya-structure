# Coprime exchange heaps: complete transport ownership and composite primitive clocks

Candidate `ANG-20260922-CEH01`; paper `381-coprime-exchange-heap`.  
Batch `FULL-TRANSPORT-20260922-G`, round 2/5; 2026-09-22.  
Outcome: `OWNED HEAP IMAGE CLOCK; COMPOSITE PRIMITIVE TIMES — STOP / FORK`

## Abstract

We audit the full path space of the frozen arithmetic heap process, with every finite initial heap and every legal infinite path retained. An elementary dependence-poset argument proves cancellation and the exact distinct-state predecessor lists without importing a normal-form theorem. The word-pushforward initial probability and actual transition probabilities give a full-support nonatomic Markov law and a unique continuous all-point version of each inverse IMAGE derivative. The law is not stationary, and its local clock is signed. We classify full clock/lag kernels, source and extension isotropy, incoming histories, phases, and all primitive closed-state-walk packets, including walks that never visit the empty heap. The first prescribed packet has full time stabilizer \((\log4)\mathbb Z\); the commuting-letter packet has \((\log192)\mathbb Z\). More generally every nonempty closed walk in each of the four frozen owners has an integer composite multiplier. Thus transport ownership succeeds but the prime-time target fails. No arithmetic naturalness, Markov-escape, classical suspension, or formal Route result follows.

## 1. Frozen identity and a common notation for four independent owners

The [candidate card](candidate-card.md), original lines 1–61, governs this paper. Set \(A=\{2,3,\ldots\}\). For a symmetric irreflexive independence relation \(I\subset A^2\), let \(H_I=A^*/{\sim_I}\), where the only elementary relations are \(uabv\sim_I ubav\) when \((a,b)\in I\). These are actual finite-word classes, with concatenation as multiplication and unit \(e=[\varnothing]\); no representative is selected as the dynamical state.

| Owner | Exact independence relation \(I\) |
| --- | --- |
| MAIN | \(\gcd(a,b)=1\) |
| FREE-WORD | empty relation |
| COMMUTATIVE | \(a\ne b\) |
| NONCOPRIME | \(a\ne b\) and \(\gcd(a,b)>1\) |

All lemmas below are proved for an arbitrary one of these relations and then applied to each one's own \(H,L,R,\pi,P,X,\mu,j\). This is not permission to use MAIN's state counts or measure for a control. Define
\[
L(h)=\{g:h=[a]g\text{ for some }a\in A\},\qquad
R(h)=\{g:h=g[a]\text{ for some }a\in A\}.
\tag{1}
\]
Both are sets of actual quotient states. MAIN's lineage is the common-divisor observable determining which symbols may cross older symbols and become deletable left factors. Proper-divisor witnesses affect this actual permission; no prime predicate, prime alphabet, or prime-dependent roof is supplied. This is a countable Markov lift, not an asserted escape from closed-walk splicing or a classical conservative realization. Strong naturalness remains OPEN.

## 2. Elementary heap representation, cancellation, and exact enumeration

For a word \(w\), distinguish the \(k\)-th occurrence of letter \(a\) by the node \((a,k)\). Orient an order constraint from an earlier to a later occurrence whenever their labels are not independent, including equal labels, and take the transitive closure. This gives a finite labelled poset \(D(w)\). Swapping adjacent independent letters preserves every relative order of dependent occurrences, hence preserves this poset on the occurrence-indexed nodes.

Conversely, every linear extension of \(D(w)\) produces a word equivalent to \(w\). To prove this rather than invoke a normal form, fix a desired extension and bring its first node to the front of the current extension. Each node it crosses is incomparable with it: it cannot precede that node in the poset while occurring after it currently, nor follow it while being first in the desired extension. Incomparable nodes have independent labels, since dependent occurrences are directly ordered. The necessary adjacent swaps are therefore allowed. Delete the first node and repeat inductively. This also shows that two words giving the same occurrence-indexed poset are equivalent. Equal-label occurrences are ordered, so a label word fixes the occurrence indices; no extra permutations of identical occurrences are counted.

Thus the representatives of a heap are exactly the linear extensions of its dependence poset. In particular, length \(n=|h|\), the content counts \(m_a(h)\), and the finite number
\[
r(h)=\#\{w:[w]=h\},\qquad 1\le r(h)\le n!,\quad r(e)=1,
\tag{2}
\]
are well-defined. The countable state set contains only posets arising from words; no arbitrary poset states are added.

A node can be first in a representative exactly when it is minimal. Deleting such a node gives the heap of the remaining poset. There is no path between surviving nodes passing through a removed minimal node, so the induced surviving order is precisely the dependence order of a remaining representative. Different minimal nodes have different labels, since equal-label nodes form a chain. Their deletion results have different content vectors and are therefore distinct actual heaps. Consequently \(L(h)\) is exactly the set of minimal-node deletions, and
\[
\ell(h):=|L(h)|=\#\min D(h),\qquad 1\le\ell(h)\le |h|\quad(h\ne e).
\tag{3}
\]
The symmetric argument gives \(R(h)\) as the distinct maximal-node deletions. These statements prove finiteness and exhaustive enumeration, not merely a bound on proposed candidates.

If \([a]g=[a]g'\), the unique minimal occurrence labelled \(a\) is identifiable in the common poset; deleting it recovers both \(g\) and \(g'\). Hence left cancellation holds. Deleting the unique maximal occurrence labelled \(a\) similarly proves right cancellation. Iterating these letter cancellations gives cancellation by any common finite word. Appends \(h[a]\) with different \(a\) are distinct by their content vectors. Append and deletion targets have lengths \(|h|+1\) and \(|h|-1\), so never coincide. Thus none of the frozen transitions below carries an overlooked sum of hidden edge multiplicities.

## 3. Own probabilities, all source points, and every predecessor

Let \(\rho(a)=1/[a(a-1)]\); telescoping gives \(\sum_{a\ge2}\rho(a)=1\). Sampling length \(n\) with probability \(2^{-n-1}\) and then independent \(\rho\)-letters gives, for each owner's quotient,
\[
\pi(h)=2^{-|h|-1}r(h)\prod_{a\ge2}\rho(a)^{m_a(h)}>0.
\tag{4}
\]
This is its word-pushforward probability: summing over the partition into classes gives one. Word representatives are counted in this probability construction, not as distinct arrows or periodic packets.

With \(\alpha(e)=1\) and \(\alpha(h)=1/2\) for \(h\ne e\), the exact transition rule is
\[
P(h,g)=
\begin{cases}
\alpha(h)\rho(a),&g=h[a],\\
1/(2\ell(h)),&h\ne e,\ g\in L(h),\\
0,&\text{otherwise}.
\end{cases}\tag{5}
\]
Section 2 proves the cases are disjoint and all targets within a case are distinct. Thus every row sums to one. Every positive entry is at most \(1/2\) and is the reciprocal of a positive even integer. The empty heap has no deletion transition but has all append transitions; all other heaps also have append transitions. There are no terminal states.

Let \(X\) be all infinite state sequences satisfying \(P(h_i,h_{i+1})>0\), with the discrete-product subspace topology and Borel structure. This is a closed Polish path space. The Markov construction starting with \(\pi\) and successively applying (5) defines
\[
\mu([h_0,\ldots,h_n])=\pi(h_0)\prod_{i=0}^{n-1}P(h_i,h_{i+1}).
\tag{6}
\]
It can be realized by independent draws for the initial finite word and each append/delete decision, using the uniform finite set \(L(h)\) for deletion. Consistency follows from the row sums. Every nonempty legal cylinder has positive mass, giving full support. Its mass is at most \(2^{-n}\pi(h_0)\), so decreasing cylinders at any path prove that \(\mu\) has no atoms. All null paths, arbitrarily high future heaps, and every finite initial heap remain in \(X\); no infinite initial heap is silently adjoined.

The law is not stationary, for every owner:
\[
\mu(X_e)=\pi(e)=\tfrac12,\qquad
\mu(T^{-1}X_e)=\sum_{a\ge2}\pi([a])P([a],e)
=\sum_a\frac{\rho(a)}4\frac12=\tfrac18.
\tag{7}
\]
Here \(X_h=\{x:x_0=h\}\). Nonstationarity is not repaired by changing the initial distribution.

The actual evolution is left shift \(T\). For a target path starting at \(h\), all predecessor states are exactly
\[
\operatorname{Pred}(h)=R(h)\ \cup\ \{[a]h:a\ge2\}.
\tag{8}
\]
Indeed, an incoming append removes a maximal node of \(h\), and an incoming deletion must come from a heap \([a]h\). Conversely each listed state has the required positive transition. The two families have lengths \(|h|-1\) and \(|h|+1\), respectively, and Section 2 proves their internal distinctness. At \(e\), only the second family is present. Every actual inverse branch is \(I_c(y)=(c,y_0,y_1,\ldots)\) on \(E_c=\bigcup_{P(c,h)>0}X_h\), with image \(X_c\). These Borel bijections enumerate all inverses.

Every heap reaches \(e\) by finitely many minimal-node deletions, and \(e\) reaches every heap by appending any representative. Hence the state graph is strongly connected. This does not identify all infinite histories in one source orbit, and it does not justify retaining only paths visiting \(e\).

## 4. Every-Borel IMAGE and the complete actual clock kernels

On the entire domain of an inverse branch prescribe
\[
j_c(y)=\frac{\pi(c)P(c,h)}{\pi(h)},\qquad y\in X_h,\quad P(c,h)>0.
\tag{9}
\]
Let \(\mathbb P_h\) be the Markov future law starting at \(h\). On \(X_h\), (6) says \(\mu=\pi(h)\mathbb P_h\), whereas prefixing \(c\) gives \(\pi(c)P(c,h)\mathbb P_h\). The cylinder identities extend to every Borel set by the monotone-class argument. Summing over the countably many possible \(h\) proves
\[
\mu(I_cE)=\int_Ej_c\,d\mu\qquad(E\subset E_c\text{ Borel}).
\tag{10}
\]
Each \(j_c\) is finite, strictly positive, and locally constant on its whole domain. In particular every null periodic or exceptional path has the same frozen formula. Full support on the open set \(E_c\) makes this continuous version unique: two continuous versions equal almost everywhere cannot differ on a nonempty relatively open set of positive measure. No arbitrary null-boundary completion is needed.

For a finite prefix of states \(u=(u_0,\ldots,u_{m-1})\) followed by a tail with first state \(h\), require every displayed edge to be legal and put
\[
B(u;h)=\prod_{i=0}^{m-1}P(s_i,s_{i+1}),\quad
s_i=u_i\ (i<m),\ s_m=h,\qquad
r_u(h)=\begin{cases}u_0,&m>0,\\h,&m=0.\end{cases}
\]
Empty prefixes have \(B(\varnothing;h)=1\). Iterating (10) gives the full-history IMAGE
\[
J_u(y)=\frac{\pi(r_u(h))B(u;h)}{\pi(h)}.
\tag{11}
\]
This also follows directly from (6) for every Borel tail set. A prefix replacement \(v\xi\mapsto u\xi\) has density \(J_u(\xi)/J_v(\xi)\) on its entire actual domain; illegal prefixes are absent.

Use actual triples \(G=\{(z,m-n,y):m,n\ge0,\ T^mz=T^ny\}\), with source \(y\), range \(z\), inverse \((y,-k,z)\), and composition \((z,k,y)(y,l,w)=(z,k+l,w)\). Equal triples are identified but lag is retained. This is the Borel subspace of \(X\times\mathbb Z\times X\), with every legal prefix presentation included. Define
\[
\kappa(z)=-\log j_{z_0}(Tz),\quad A_m(z)=\sum_{i=0}^{m-1}\kappa(T^iz),\quad A_0=0,\qquad
c(z,m-n,y)=A_m(z)-A_n(y).
\tag{12}
\]
For \(z=u\xi,y=v\xi,\xi_0=h\), this is the explicit finite-data expression
\[
c(g)=\log\frac{\pi(r_v(h))B(v;h)}{\pi(r_u(h))B(u;h)}.
\tag{13}
\]
The identity \(J_{uw}(\eta)=J_u(w\eta)J_w(\eta)\) cancels every common extension of two prefix witnesses of the same triple. Equal lag lets one align their lengths by such an extension, proving all-point witness independence. Aligning the middle prefixes of composable arrows proves additivity; inverses negate \(c\). Thus (12) is the cocycle of (10), not a borrowed roof.

For \(\lambda(z,k,y)=k\), the FULL kernels are
\[
\begin{aligned}
\ker\lambda&=\{(u\xi,|u|-|v|,v\xi):|u|=|v|\},\\
\ker c&=\{(u\xi,|u|-|v|,v\xi):
\pi(r_u(h))B(u;h)=\pi(r_v(h))B(v;h),\ h=\xi_0\},\\
\ker\lambda\cap\ker c&=\{(u\xi,0,v\xi):|u|=|v|,\
\pi(r_u(h))B(u;h)=\pi(r_v(h))B(v;h)\}.
\end{aligned}\tag{14}
\]
Every set here is restricted to all actual legal prefix pairs; no finite depth or tail cutoff is imposed. Equations (2)–(5) make the equality a complete finite-data membership test, not an unspecified derivative condition. These are not merely isotropy kernels. For example the actual edge \([2]\to[22]\) has \(j=1\) in every owner, hence its inverse-prefix arrow has clock zero but lag one. Equal clock and equal lag are not interchangeable.

## 5. Whole-source isotropy, physical phases, and the closed-walk ledger

Retain all \(X\times\mathbb R\), with arrows \((y,s)\to(z,s+c(g))\). Height translation acts on its orbit SET and no invariant flow measure, positive roof, or manifold quotient is asserted. All incoming arrows at \((z,t)\) are exactly
\[
m,n\ge0,\quad y=vT^mz\in X,\quad |v|=n,\quad
g=(z,m-n,y),\quad\text{source height }t-c(g).
\tag{15}
\]
All finite legal prefixes and every real height are included, with duplicate actual triples identified. Source orbits are precisely eventual tail equality up to shifts; graph connectivity does not collapse different infinite tails.

Source isotropy is trivial at noneventually-periodic paths. If a path has least eventual visible-state period \(d\), its entire source isotropy is \(d\mathbb Z\): a nonzero equality \(T^mx=T^nx\) is exactly an eventual period, whose integer periods are multiples of its least one. Such a tail is a primitive closed state walk \(C=(h_0,\ldots,h_{d-1},h_d=h_0)\), up to cyclic rotation, not a chosen word representative of a heap.

For every such closed walk, without requiring a visit to \(e\), define
\[
W(C)=\prod_{i=0}^{d-1}P(h_i,h_{i+1}),\qquad
\tau_C=-\log W(C)>0.
\tag{16}
\]
The root probabilities in (11) telescope around a closed walk. If the periodic tail begins after \(N\) steps, (12) gives \(c(x,d,x)=A_{N+d}(x)-A_N(x)=\tau_C\); any finite prehistory cancels. Hence the entire isotropy map is \(kd\mapsto k\tau_C\), and
\[
H_x=c(G_x^x)=
\begin{cases}\tau_C\mathbb Z,&x\text{ eventually follows }C,\\
\{0\},&x\text{ not eventually periodic}.
\end{cases}\tag{17}
\]
Positivity follows already from \(P\le1/2\). Extension fixed-object isotropy is trivial everywhere, being the clock-zero part of source isotropy. Nontrivial source isotropy is retained as height-moving arrows, not deleted. The stabilizer of the height-translation action at an extension orbit is exactly \(H_x\).

All periodic paths with the same primitive cyclic state walk, including every legal finite prehistory, lie in one source orbit. Tail equality of periodic paths forces the same primitive cyclic state walk. Thus primitive physical packets are precisely primitive closed-state-walk necklaces. Distinct necklaces are not identified when their times agree. All phases over a source orbit are \(\mathbb R/H_x\), as sets: transport height to a reference source point by any actual arrow; two choices differ by exactly \(H_x\). This choice of coordinate removes no objects. Repeating a primitive walk \(k\) times gives time \(k\tau_C\), not a new primitive packet.

There is also a fully explicit integer formula for the whole ledger. Let \(v_e(C)\) count departures from \(e\), and use the actual appended letter \(a_i\) on each append edge. By (5),
\[
M(C):=W(C)^{-1}
=2^{d-v_e(C)}
\prod_{\text{append }i}a_i(a_i-1)
\prod_{\text{delete }i}\ell(h_i),\qquad \tau_C=\log M(C).
\tag{18}
\]
Each transition changes heap length by one. Therefore a nonempty closed walk has even length \(d\ge2\), and (18) retains all visits and all distinct deletion counts. Each reciprocal \(P^{-1}\) is an even integer, so \(M(C)\) is divisible by \(2^d\) and is composite. The length-zero identity is retained with clock zero and is not a positive primitive packet. This proves a scoped nonempty-closed-walk statement for these four frozen recipes, not a no-go for arbitrary Markov sources or other transition laws.

## 6. Prescribed MAIN tests, followed by the full target decision

First take \(C_2=(e,[2],e)\). Here \(\pi(e)=1/2,\pi([2])=1/8\), and both transition probabilities are \(1/2\). The two all-point inverse IMAGE values are
\[
j_e|_{X_{[2]}}=2,\qquad j_{[2]}|_{X_e}=1/8.
\]
Thus the local clock includes \(-\log2\) and \(\log8\); it is signed, not a positive roof. The source walk has least period two because \(e\ne[2]\). Equations (16)–(17) give its ENTIRE \(H=(\log4)\mathbb Z\), with all phases and trivial extension isotropy. It is not a repetition of a hidden \(\log2\) packet in that orbit. This already violates the frozen prime-time target.

The next prescribed test uses an actual exchange. Since 2 and 3 are coprime, \(h=[23]=[32]\) has two minimal nodes and \(L(h)=\{[2],[3]\}\). The legal walk
\[
C_{\rm ex}=(e,[2],h,[2],e)
\]
deletes 3 while the older 2 remains. Its probabilities are \(1/2,1/12,1/4,1/2\), so \(W=1/192\). The empty heap occurs once in its cyclic word, proving least period four. Its full stabilizer is \((\log192)\mathbb Z\), not just a listed return. The alternative walk through \([3]\) after \(h\) is a different packet even though its product is the same; no representative or equal-time quotient identifies them.

Walks not visiting \(e\) have not been omitted. For example \(([2],[22],[2])\) is primitive, with probabilities \(1/4,1/2\), hence full \(H=(\log8)\mathbb Z\). The exhaustive classification is nevertheless (16)–(18), not these examples. Every primitive closed packet in MAIN has composite multiplier, so none meets the prescribed prime-time condition in this normalization.

## 7. Three complete own controls

The poset and measure proofs were uniform in a symmetric irreflexive independence relation. The following instantiations therefore supply each control's own exhaustive inverses (8), every-Borel IMAGE (9)–(11), full kernels (14), incoming histories (15), source/extension isotropy and phases (17), and the complete primitive-walk/repetition ledger (16)–(18). They do not reuse MAIN's \(\pi\), \(\ell\), or state identities.

**FREE-WORD.** A heap is an ordinary word, \(r(h)=1\). A nonempty word has exactly one left deletion, removing its first letter, and one right deletion, removing its last. Right append together with left deletion is this control's actual queue-like evolution, not stack-top deletion. Its own \(\pi(h)=2^{-|h|-1}\prod_i\rho(h_i)\), \(\ell(h)=1\), and (5) specify all transitions. All closed word-state walks, including those avoiding \(e\), use (18) with deletion factors one. Its own root-2 packet has \(\tau=\log4\). MAIN's exchange walk to \([2]\) after the word \(23\) is illegal here; the legal walk \(e\to2\to23\to3\to e\) instead has probabilities \(1/2,1/12,1/2,1/2\), and least time \(\log96\).

**COMMUTATIVE.** A state is a finite multiset of letters, with \(r(h)=|h|!/\prod_a m_a(h)!\): the representatives are all distinct arrangements of that multiset. Left and right deletions remove one copy of any present label; the number of distinct target states is \(\ell(h)=|\{a:m_a(h)>0\}|\), not the number of occurrences. Equation (4) with this multinomial factor is its own initial law. The uniform choice is over those distinct targets, so multiplicities are not silently counted as extra arrows. All primitive multiset-state walks have the complete ledger (18). Its root-2 and the \(2,3\) exchange packets have least times \(\log4,\log192\), respectively; equality with MAIN's examples supplies no naturalness credit.

**NONCOPRIME.** Use its own dependence poset with exchanges only for distinct letters sharing a nontrivial divisor. Its \(r(h)\), minimal/maximal deletion sets, \(\ell(h)\), word-pushforward probability, and all transition counts are those of this different quotient. The same direct poset proof establishes them without borrowing MAIN's classes. The root-2 packet still has least time \(\log4\). Letters 2 and 3 do not exchange, so MAIN's exchange walk is illegal. The actual control exchange is \(e\to[2]\to[24]=[42]\to[2]\to e\), with probabilities \(1/2,1/24,1/4,1/2\); it has least period four and full \(H=(\log384)\mathbb Z\).

For every control, (7) proves nonstationarity, (6) proves full support and no atoms, and the full clock includes the signed root-2 values above. Every nonempty closed walk has the composite integer multiplier (18), all extension isotropy is trivial, and every source orbit keeps its full \(\mathbb R/H_x\) phases. The identical short-loop failure is an adverse control, not a replacement measure or a rescue of MAIN.

## 8. Gate boundary and conclusion

| Obligation | Exact same-owner result | Limitation |
| --- | --- | --- |
| Source / transport | Cancellation, distinct quotient-state counts, full probability, all predecessors and every-Borel IMAGE | Finite heaps and all their infinite paths; no infinite initial heaps |
| Whole-point clock | Unique continuous branch versions, signed cocycle, complete kernels and real extension | No stationary source law or classical positive-roof assertion |
| Returns / target | All primitive closed-state-walk packets, full H, incoming, phases and repeats | Composite primitive times; target FAILS |
| Arithmetic / naturalness | Divisor relation changes actual crossing and deletion permissions | Strong naturalness OPEN; countable Markov splicing remains |
| Later coordinates | T3 NOT AUDITED; formal UNASSIGNED; B NOT INVOKED | Classical A0/A1/A2 NOT APPLICABLE |

**STOP / FORK.** The same-object ledger is intact, but the full prime-packet target fails at the first prescribed primitive and, by (18), at every primitive in this owner's ledger. There is no probability tuning, clock rescaling, deletion of closed walks, selected root, borrowed operator, or post-return reinterpretation. The common-divisor mechanism changes the state graph but does not remove the complete Markov closed-walk owner. A new architecture would require a fresh frozen card.

## 9. Evidence and integrity

The [card](candidate-card.md), [claim ledger](claim-ledger.md), and [package overview](README.md) record this exact object. This paper is an exact derivation; there are no scientific numerical experiments, external citations, prime tables, finite-cutoff inferences, or global novelty claims. The finite poset argument supplies the cancellation and enumeration actually used.

The source author previously worked on 367, 371 and 376. Definition scouting read the 375–379 batch summary, lines 1–73, and prior-work guide lines 44–108 and 361–432, with heading discovery through line 433; it did not read the 377 card. Root retains that stack comparison. This proof was written only after explicit CP1 release, from the full 61-line card and paper template, without raw independent derivations, peer messages, or other current-batch manuscripts. Shared history is NOT_CALIBRATED; source authorship is not independent review.

Data availability: the full definitions, inputs, and proofs are in this Markdown package; no empirical data were collected. Contributions: this AI-assisted author supplied the source proposal and independently derived/wrote the main proof; root owns freeze, integration, and separate review. Ethics: no human subjects or private data. Funding and conflict declarations were not supplied and are not inferred. ARS discipline informed the separation of definition, proof, owner, and target claims; it is not mathematical validation or external peer review.
