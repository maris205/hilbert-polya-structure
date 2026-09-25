# Positive variable-step advancement: actual arrow image and weighted-cycle clocks

Candidate ID: `ANG-AUDIT-20260924-VSA01`.
Outcome: `VARIABLE-STEP PACKET AND CLOCK TRANSPORT ESTABLISHED; NO ARITHMETIC ADMISSION`.
Paper459; batch `RECURRENCE-OWNER-20260924-V`, round5/5; 2026-09-24.
Status: exact conditional theorem and four complete external controls.
Classical NOT APPLICABLE; formal UNASSIGNED; B NOT INVOKED.

## Abstract

A partial measured map is advanced by a prescribed positive finite number of its actual steps, evaluated at each macrostep source, without restricting the carrier to a section.
The complete inverse-word product owns the new map's every-Borel IMAGE and integrated clock.
Accumulated parent time defines a well-defined injective functor on actual lag groupoids, but its exact image requires common sampled histories and need not contain all parent arrows.
On each finite parent cycle, the full weighted functional graph determines all advanced cycles, incoming packets and primitive clocks through positive integer winding numbers.
Finite histories are classified by their actual last legal sampled endpoint, including advancement stopping before the parent does.
The rational-parent prime criterion and four complete controls distinguish retained packets, duplicated packets, enlarged primitive time and genuine terminal arrow loss.
No arithmetic source or naturalness of the freely chosen step rule is thereby supplied.

## 1. Identity and same-object ledger

| Item | Frozen owner |
| --- | --- |
| Parent | Standard Borel \(X\), \(\sigma\)-finite \(\mu\), partial Borel \(T:D\to X\) |
| Inverse data | Complete countable disjoint injective partition of \(D\), actual Borel inverses \(I_i\), positive finite all-point Borel IMAGE versions \(J_i\) |
| Step rule | One Borel \(r:X\to\mathbb N_{\ge1}\), finite at every point |
| New owner | Same full \(X,\mu\); \(V(x)=T^{r(x)}x\) exactly when the entire requested block is legal |
| Terminals | All parent terminals and all newly terminal V-states remain objects with units and actual incoming |
| Clock / physical action | Own inverse-word IMAGE; actual lag-clock extension on full \(X\times\mathbb R\), then unrestricted height translation on its orbit set |
| Primitive | Least positive generator of the entire isotropy-clock image; every positive integer repetition; packet multiplicity retained |
| Classical / operator fields | No positive roof, symplectic suspension, Hamiltonian lift, operator, trace or zeta is constructed |

The conditional lineage is intrinsic prime-symbolic current-state batching → same-source finite-step evolution → actual clock and packet transport.
A use of this filter still needs its own arithmetic source and justification of \(r\); no target prime or desired period selects the schedule here.
This is neither a first-return section construction nor a fixed-stride theorem imported from another owner.

## 2. Question, boundary and frozen inputs

The question is how actual variable-step histories transport the full groupoid, its clock and its positive packet ledger, including partial-domain boundaries.
The strongest claim is an exact injective clock-compatible functor with its precise sampled-time image, together with full weighted-cycle and terminal-history laws.
It is not a surjectivity claim, a universal advancement no-go or an arithmetic admission.
Signed and zero clocks remain; positive step COUNTS are not asserted to make the clock a positive roof.
The [95-line card](candidate-card.md) has SHA256
`72facc556a4e30cebffd6970541b5b33a8748f5064445ec5faa7eb7906507c13`.
For each inverse branch and every Borel \(B\) in its actual domain,
\[
 \mu(I_i B)=\int_BJ_i\,d\mu,\qquad \kappa_T(x)=-\log J_i(Tx)
\]
on the uniquely assigned source piece. Versions include null points as frozen data.
An iterate \(U^n x\), \(U=T,V\), always requires all \(n\) actual steps; \(U^0x=x\) exists at every state.

## 3. Complete inverse words and the new owner's IMAGE

Let \(D_n\) be the Borel domain of \(n\) legal T-steps. The actual V-domain is
\[
 D_V=\bigcup_{n\ge1}\bigl(\{r=n\}\cap D_n\bigr).
\]
Refine it by \(n\), the unique legal T-piece word \(i_0,\ldots,i_{n-1}\), and the source condition \(r(x)=n\).
This is a countable disjoint Borel partition. Each restriction of \(T^n\) is injective, with inverse the corresponding legal composition of the actual \(I_i\)'s.
Further restricting that inverse by \(r(\theta y)=n\) makes its actual domain Borel.
Every actual predecessor satisfies exactly its own length, word and source rule, so all inverse roots are retained without artificial branch-label multiplicity.
Only the macrostep source reads \(r\); intermediate T-points impose their T-piece legality, not an extra V-step request.
The terminal status of the target never invalidates an otherwise legal inverse.

For an inverse word with forward states \(x_0=\theta y,x_1,\ldots,x_n=y\), prescribe
\[
 J_\theta(y)=\prod_{j=0}^{n-1}J_{i_j}(x_{j+1}) .
\]
This is Borel, positive and finite at every actual point.
The one-step IMAGE identity implies its weighted change-of-variables form, first for indicator functions, then nonnegative simple functions and monotone limits.
Applying this form successively to the inverse composition proves, for every Borel \(E\) in its actual domain,
\[
 \mu(\theta E)=\int_EJ_\theta\,d\mu .
\]
Restriction by the actual source rule preserves this identity.
Consequently the new owner's clock, rather than an independently inserted roof, is
\[
 \kappa_V(x)=-\log J_{\rm actual}(Vx)
      =\sum_{j=0}^{r(x)-1}\kappa_T(T^jx)=S^T_{r(x)}(x).
\]
There is no next-step clock at a V-terminal, even if that point still has a legal parent step.

## 4. Actual accumulated-time functor, exact image and kernels

On a legal V-history set \(R_0(x)=0\), \(R_m(x)=\sum_{j<m}r(V^jx)\).
Concatenating legal blocks proves
\[
 V^mx=T^{R_m(x)}x,\qquad S_m^V(x)=S_{R_m(x)}^T(x),\qquad R_m(x)\ge m .
\]
For either owner, use all actual triples \(G_U=\{(z,m-n,w):U^mz=U^nw\}\), identifying equal triples and retaining the integer lag.
The source is \(w\), the range is \(z\), and \(c_U(z,m-n,w)=S_m^U(z)-S_n^U(w)\).
Changing a witness shifts both depths equally and adds the same common-tail sum; composition extends the shorter middle history to the longer one and cancels those sums.
Thus \(c_U\) descends and is additive; inverse arrows negate clocks and \((Ux,-1,x)\) has clock \(-\kappa_U(x)\).

Define \(b(z,m-n,w)=R_m(z)-R_n(w)\).
The identity \(R_{m+s}(z)=R_m(z)+R_s(V^mz)\) shows that changing a witness of the SAME V-triple adds the same accumulated time on both sides.
The same middle-history cancellation proves that \(b\) is additive.
Therefore
\[
 \Phi:G_V\longrightarrow G_T,\qquad
 \Phi(z,m-n,w)=(z,b(z,m-n,w),w)
\]
is a well-defined functor, and \(c_V=c_T\circ\Phi\) by the independently proved clock identity.

To prove injectivity, first consider a nonunit V-isotropy arrow of positive lag \(k\), witnessed at the same state by \(m=n+k\).
Its accumulated parent lag is
\[
 b=R_{n+k}(z)-R_n(z)=\sum_{j=n}^{n+k-1}r(V^jz)>0.
\]
Negative isotropy lag similarly has negative \(b\); hence only the unit isotropy arrow maps to a parent unit.
If two arrows have the same \(\Phi\)-image, they have the same endpoints and their quotient is isotropy mapped to a unit; the quotient is therefore a unit.
This proves injectivity without assuming it. The argument uses strict positivity and finiteness of the actually traversed step counts.

For every state define its increasing set of actual sampled parent times
\[
 A_x=\{R_m(x):V^mx\text{ is defined}\}.
\]
The EXACT image is
\[
 \operatorname{im}\Phi=
 \{(z,a,w)\in G_T:\exists s\in A_z,\ t\in A_w,\
                  T^sz=T^tw,\ a=s-t\}.
\]
Every such pair supplies an actual V-witness at the unique sample indices of \(s,t\); the converse follows from the definition of \(\Phi\).
Injectivity ensures that different sampled witnesses for one such parent triple yield the same macro lag.
No full-parent-arrow conclusion follows merely from keeping the same object set \(X\).

The complete macro kernels are
\[
 K_{\rm lag}^V=\{(z,0,w):V^mz=V^mw\text{ for some legal }m\},\qquad
 K_c^V=\Phi^{-1}(K_c^T),\qquad K_{\rm joint}^V=K_{\rm lag}^V\cap K_c^V .
\]
Here \(K_c^T\) is all parent meeting triples with \(S_m^T(z)=S_n^T(w)\); the parent lag and joint kernels are given by the corresponding parent formulas.
The macro lag is not replaced by \(b\) in a kernel test.
These descriptions retain all actual merging/cancelling arrows and do not claim they are units.
All finite inverse histories use every legal inverse word of Section3; all compatible infinite sequences retain the infinite histories.

## 5. All terminal, infinite and physical histories

The full V-source packet relation is the exact sampled-tail condition
\[
 z\sim_V w\iff \exists s\in A_z,\ t\in A_w:\ T^sz=T^tw .
\]
It is a subrelation of the parent packet relation, with all objects retained.
Suppose a parent history has finite remaining length \(h(x)=\max\{n:T^nx\text{ exists}\}\), including \(h=0\) at a parent terminal.
Start \(a_0=0\); append \(a_{j+1}=a_j+r(T^{a_j}x)\) exactly while that value is at most \(h(x)\).
Strict increase gives a last value \(a_M\), and its actual endpoint \(E_r(x)=T^{a_M}x\) is V-terminal.
The endpoint need not be the parent terminal; the next requested block can exceed the remaining legal length.
Within every parent terminal-ending packet, the complete V-packets are precisely the nonempty fibres of \(E_r\).
Necessity follows because two V-histories that meet have the same subsequent terminal endpoint; sufficiency follows because equal endpoints give an actual meeting.
This includes every inverse depth and all newly terminal objects, not merely a depth residue or a padded continuation.

If the parent history is infinite, every finite requested block is legal, so the V-history is infinite and its sample times are unbounded.
For an infinite non-eventually-periodic parent packet, its V-packets are exactly the sampled-tail equivalence classes above.
A V-repetition would give a positive parent-time repetition, because all traversed \(r\)'s are positive; thus no such V-source is eventually periodic.
Meetings that never occur at two actual sample times supply no V-arrow, even when the parent histories merge.
No fixed number of split classes or automatic synchronization is presumed.

For either deterministic owner, a nonzero-lag loop is equivalent to an eventual repetition.
At a source eventually reaching a least-\(\ell\) core with signed cycle sum \(W\), the loop lags are exactly \(\ell\mathbb Z\), and their clock character is \(n\ell\mapsto nW\).
All such lags occur after core arrival, and every repetition difference is a multiple of the least period.
Hence the entire \(H=W\mathbb Z\); source isotropy is \(\ell\mathbb Z\), while extension isotropy is \(\ell\mathbb Z\) if \(W=0\), and zero otherwise.
Terminal-ending and non-eventually-periodic packets have zero source isotropy and \(H\).
The extension acts on all heights by \((w,h)\mapsto(z,h+c_U(g))\).
For a packet reference \(p\) and actual arrows \(g_z:p\to z\), let \(a_z=c_U(g_z)\); all phases are exactly \([h-a_z]\in\mathbb R/H_p\).
Choices differ by \(H_p\); changing reference translates the coordinate without a global measurable-selector or regular-quotient assumption.
Vertical translation has stabilizer precisely \(H_p\); nonzero \(W\) gives primitive \(|W|\) and returns \(n|W|\), while \(H=0\) retains every real phase and no positive return.

## 6. Entire weighted functional graphs over parent cycles

Fix a distinct parent least-\(q\) core \(\Gamma=\{x_j:j\in\mathbb Z/q\}\), \(Tx_j=x_{j+1}\), and signed parent clock \(C=\sum_{j=0}^{q-1}\kappa_T(x_j)\).
All requested blocks on this core are legal. Define the complete graph
\[
 f(j)=j+r(x_j)\pmod q,\qquad w_j=r(x_j)>0.
\]
Every vertex of this finite deterministic graph eventually enters one of its directed cycles; no transient phase is deleted.
For a graph cycle \(O=(j_0,\ldots,j_{\ell-1})\), its distinct actual states form a least-\(\ell\) V-core.
Its total parent time \(W_O^{\rm step}=\sum_{j\in O}w_j\) is a positive multiple of \(q\): the phase congruences telescope round the cycle, and every summand is positive.
Write \(a_O=W_O^{\rm step}/q\in\mathbb N_{\ge1}\).
Concatenating those parent blocks follows the original cycle for exactly \(a_O\) full turns, giving signed V-cycle clock
\[
 C_O=a_O C .
\]
This is an integer WINDING multiplier, not the number \(\ell\) of macrosteps in general.
Conversely any V-cycle gives a positive-time T-repetition and hence lies on a parent core, where it is exactly a cycle of this full graph.
Distinct graph cycles are distinct full V-packets, since deterministic eventual cores cannot merge.
Relabelling the parent reference phase rotates vertices and their weights together, so cycle, winding and packet conclusions do not depend on that reference.

For any parent incoming state \(x\), let \(h\) be its first T-arrival at the core, \(T^h x=x_j\).
Its V-samples are infinite; choose the first \(m\) with \(R_m(x)\ge h\).
That sample lies at phase \(j+R_m(x)-h\pmod q\); its eventual graph cycle \(O\) assigns \(x\) to exactly that full V-packet.
This gives all unrestricted incoming, including macrosteps which pass through the parent first-arrival point before their endpoint.
Every incoming state is covered, and every predecessor of a V-core has exactly this assignment.

For an entire such V-packet choose \(p\) on its core, and for each \(z\) any macro arrival depth \(d_z\) with \(V^{d_z}z=p\), putting \(b_z=S^V_{d_z}(z)\).
With \(\ell=|O|\) and \(W=C_O\), its complete restricted groupoid and clock are
\[
 (z,k,w)\in G_V\iff k-d_z+d_w\in\ell\mathbb Z,\qquad
 c_V(z,k,w)=b_z-b_w+\frac{k-d_z+d_w}{\ell}W .
\]
To prove necessity, extend a meeting to \(p\); to prove sufficiency, choose sufficiently large arrival depths with the prescribed difference.
The quotient displayed is an integer on actual arrows, not a division of physical primitive time.
This formula gives the whole lag kernel by \(k=0\), whole clock kernel by vanishing of its right side, and their full intersection.
Source isotropy is \(\ell\mathbb Z\), entire \(H=a_OC\mathbb Z\), extension isotropy follows Section5, and every phase is \([h-b_z]\in\mathbb R/a_OC\mathbb Z\).
On loops, \(\Phi\) sends \(\ell\) to \(q a_O\); the corresponding parent isotropy image can be a proper subgroup of \(q\mathbb Z\).
For \(C\ne0\) the primitive is \(a_O|C|\), with all integer repetitions; for \(C=0\) all these graph cycles retain source isotropy but have no positive physical return.

## 7. Exact prime criterion and its rational boundary

Counting each parent core once modulo phase, the full positive V-ledger is the multiset of \((\Gamma,O,a_O|C_\Gamma|)\) with \(C_\Gamma\ne0\).
No other positive packet exists by Sections5–6.
Nonemptiness is equivalent to at least one nonzero-clock parent core, since each finite graph has a cycle.
Without rationality, prime-only support is exactly that every \(M_\Gamma^{a_O}\) is an ordinary prime, where \(M_\Gamma=\exp(|C_\Gamma|)\); uniqueness counts every pair \((\Gamma,O)\) separately.

Under the stipulated \(M_\Gamma\in\mathbb Q\), \(M_\Gamma>1\), write \(M=u/v\) in lowest positive terms.
If \(M^a=p\) is prime, \(u^a=pv^a\) forces \(v=1\), and prime factorization forces \(a=1,u=p\).
The converse is immediate. Therefore the nonempty, prime-only and prime-unique benchmark holds exactly when:

1. At least one parent core has nonzero signed clock.
2. Every nonzero parent core has an ordinary prime multiplier \(M_\Gamma\).
3. Its complete weighted graph has exactly one cycle, and that cycle's total edge weight is \(q\), equivalently winding1.
4. Distinct nonzero parent cores have distinct prime multipliers.

Necessity of uniqueness includes the number of graph cycles; transients do not create extra closed packets but remain actual states and histories.
Conversely these conditions give exactly one packet per distinct parent prime and no other positive primitive.
Zero-clock parent graphs remain unrestricted, and all-prime coverage additionally requires these parent multipliers to exhaust the ordinary primes.
No rational implication is asserted for irrational \(M\); only the general power criterion applies there.
The rule \(r\equiv1\) is included, so this is not a universal advancement obstruction or proof that a freely designed schedule is arithmetic.

## 8. Complete external controls A/B/C

Write \(s=\sqrt2\), \(a=\log s\), \(L=2a=\log2\).
Each control has its own full \(X=\mathbb R\times\{0,1\}\), Lebesgue×counting, and parent \(T(x,j)=(sx,j+1\bmod2)\).
Its actual inverse is \((y,f)\mapsto(y/s,f-1\bmod2)\), with geometric every-point \(J=1/s\), including \(y=0\); ordinary scaling proves every-Borel IMAGE.
The parent clock is \(a\), and its whole groupoid is
\[
 ((s^{-h}y,f+h\bmod2),h,(y,f)),\qquad h\in\mathbb Z,\quad c_T=ha .
\]
All three parent kernels are units. The only periodic core is the two zero states, its full incoming packet; source isotropy is \(2\mathbb Z\), entire \(H=L\mathbb Z\), extension isotropy0 and phase \(h_{\rm ht}+ja\bmod L\).
No nonzero point is eventually periodic, since \(s^m x=s^n x\), \(m\ne n\), would force \(x=0\).
All nonzero parent packets are
\[
 \{(\epsilon2^n u,0),(\epsilon s2^n u,1):n\in\mathbb Z\},
 \quad \epsilon=\pm1,\quad u\in[1,2).
\]
Every state belongs to exactly one such packet by its unique sheet0 representative modulo scaling2.
They have zero source/extension isotropy and \(H\), and full real phase \(h_{\rm ht}+\log|x|\).
All histories are bilateral, with unique predecessors; neither sign nor the null zero core is removed.

### A: schedule \((1,1)\)

The new map is exactly the separately audited parent map: its actual inverse, all-point IMAGE and clock are as above, and \(\Phi\) is the identity on all actual arrows.
Its complete packets, kernels, isotropy and phases are therefore those just explicitly derived from this map.
The full positive ledger is one packet of primitive \(L\), with all repeats \(mL\).
It satisfies the necessary nonempty prime-only, prime-unique ledger properties, not all-prime coverage or an endogenous prime-source requirement.

### B: schedule \((2,2)\)

The actual new map is \(V(x,j)=(2x,j)\), with inverse \((y,j)\mapsto(y/2,j)\), geometric all-point \(J=1/2\) and every-Borel IMAGE by scaling.
Its clock is \(L\), and all arrows are \(((2^{-k}y,f),k,(y,f))\), with clock \(kL\).
All three kernels are units; \(\Phi\) sends the macro lag \(k\) to \(2k\), and its exact image is the even-lag parent arrows.
The two fixed singleton zero packets each have source isotropy \(\mathbb Z\), entire \(H=L\mathbb Z\), extension isotropy0 and phase \(h_{\rm ht}\bmod L\).
Every nonzero packet is \(\{(\epsilon2^n u,j):n\in\mathbb Z\}\), uniquely labelled by \(\epsilon=\pm1,\ u\in[1,2),j\in\{0,1\}\).
Its histories are bilateral, its source/extension isotropy and \(H\) are zero, and its full phase is \(h_{\rm ht}+\log|x|\).
The full positive ledger has two distinct \(\log2\) packets, each with repeats \(mL\): uniqueness fails without deleting a sheet.

### C: schedule \((1,3)\)

Here \(V(x,0)=(sx,1)\), \(V(x,1)=(s^3x,0)\).
The actual inverse at target sheet1 divides by \(s\) and returns sheet0; at target sheet0 it divides by \(s^3\) and returns sheet1.
These give their own geometric every-point IMAGE values \(s^{-1},s^{-3}\), and own source clocks \(a,3a\).
Both maps are global bijections; all positive and negative iterate histories are retained.
For every \(n\in\mathbb Z\),
\[
 V^{2n}(x,j)=(4^nx,j),\qquad
 V^{2n+1}(x,j)=(s^{r_j}4^nx,1-j),\quad r_0=1,\ r_1=3.
\]
For a source sheet \(f\), define \(b_{2n}(f)=4n\), \(b_{2n+1}(f)=4n+4-r_f\).
The complete arrows and their parent images are
\[
 ((s^{-b_k(f)}y,f+k\bmod2),k,(y,f)),\qquad
 \Phi\text{ replaces }k\text{ by }b_k(f),\qquad c_V=a\,b_k(f).
\]
The formulas follow by writing the range as \(V^{-k}(y,f)\); they apply to all integers, not just forward times.
The exact parent image consists of lag \(h\equiv0\pmod4\) for either source sheet, together with \(h\equiv3\pmod4\) at source sheet0 and \(h\equiv1\pmod4\) at source sheet1.
For \(k>0\), \(b_k(f)>0\), and for \(k<0\) it is negative; hence lag, clock and joint kernels are units.
The sole periodic core is the two zero states, of least V-period2 and full incoming equal to that core.
It has source isotropy \(2\mathbb Z\), entire \(H=4a\mathbb Z=2L\mathbb Z\), extension isotropy0 and phases \(h_{\rm ht}+ja\bmod4a\).
Its primitive is \(2L=\log4\), with repeats \(2mL\): the weighted graph makes two parent turns, not one.
The complete nonzero packets are
\[
 \{(\epsilon4^n u,0),(\epsilon s4^n u,1):n\in\mathbb Z\},
 \quad \epsilon=\pm1,\quad u\in[1,4).
\]
They exhaust both sheets and both signs, have zero source/extension isotropy and \(H\), and full real phase \(h_{\rm ht}+\log|x|\).
This control fails prime-only support; neither its clock nor its parent-arrow image is obtained by pretending that every macrostep has the same length.

## 9. Complete partial control D

The full carrier is \(\mathbb R\), with \(T(x)=x+1\) on \((-2,0)\), and all other objects retained.
Its complete inverse is \(I(y)=y-1\) on \((-1,1)\), with all-point \(J=1\) and every-Borel IMAGE by translation, so every legal parent clock is0.
The legal two-step domain is \((-2,-1)\), with inverse \(y-2\) on \((0,1)\); there are no legal three-step histories.
The entire parent packets are
\[
 P_t=\{t-2,t-1,t\}\ (0<t<1),\qquad P_0=\{-1,0\},
\]
and the isolated terminal singletons \(u\le-2\) or \(u\ge1\).
In \(P_t\), let the source and range be \(w=t-j,z=t-i\), \(i,j\in\{0,1,2\}\); all arrows are exactly \((z,i-j,w)\).
For \(P_0\) use the same formula with \(i,j\in\{0,1\}\); isolated packets have only units.
This lists every finite incoming history; there are no infinite histories or periodic/even eventual-periodic states.
All clocks vanish; the clock kernel is all \(G_T\), the lag and joint kernels are units, all source/extension isotropy and \(H\) are zero, and every packet has full phase \(h_{\rm ht}\in\mathbb R\).

With the frozen rule \(r=1\) for \(x<-1\) and2 otherwise, the actual V-domain is exactly \((-2,-1)\), and \(V(x)=x+1\) there.
Indeed all points at or above \(-1\) have fewer than two remaining parent steps; points at or below \(-2\) have none.
Its complete inverse is \(y-1\) on \((-1,0)\), with its own all-point IMAGE1 and clock0.
There is no legal second V-step. In particular, the allowed target \((-1,0)\) is V-terminal although it still has one parent step.
The complete V-packets are \(Q_t=\{t-2,t-1\}\), \(0<t<1\), and isolated terminal singletons at every point of \((-\infty,-2]\cup\{-1\}\cup[0,\infty)\).
Their arrows are all units and the pairs \((t-2,1,t-1)\), \((t-1,-1,t-2)\).
Thus \(\Phi\) is the inclusion of precisely these arrows into \(G_T\); every legal V-block happens here to have length1, but the omitted length2 requests remain part of the owner.
The lost parent arrows in each \(P_t\) are exactly those connecting \(t\) with either \(t-1\) or \(t-2\), in both directions; the two arrows connecting \(-1\) and0 are also lost.
No object is lost: \(P_t\) splits into \(Q_t\) and \(\{t\}\), and \(P_0\) into its two singletons.
For V, the clock kernel is all \(G_V\), the lag and joint kernels are units, every isotropy and \(H\) is zero, and every packet has full real phase \(h_{\rm ht}\).
Both complete positive ledgers are empty, not secretly absorbing zero-clock loops.
All excluded endpoints and terminal targets above are retained exactly; the half-open/open boundaries have not been padded.

## 10. Gate assessment and decision

| Gate | Evidence / status | Boundary |
| --- | --- | --- |
| T0 | Full source, legal inverse words, every-Borel IMAGE and actual arrow functor established | Same objects do not imply the same full parent arrows |
| T1 clock component | Own all-point integrated clock and exact compatibility established | Arithmetic T1 NOT PASSED; no naturalness proof for arbitrary \(r\) |
| T2 | Complete weighted graphs, incoming/terminal laws, entire \(H\), kernels, phases, repeats and rational criterion established | External A has necessary ledger properties only; B/C/D retain their adverse findings |
| T3 | NOT AUDITED | No operator, trace or zeta |
| Classical / formal / B | NOT APPLICABLE / UNASSIGNED / NOT INVOKED | No formal evaluator invoked |

Decision: retain this completed conditional filter and FORK the programme to genuinely arithmetic carriers; no control is promoted and no460 work is authorized.
The same-object distinction between parent and new owner stayed explicit throughout.
Strong naturalness and PROVES_TOO_MUCH remain OPEN; a freely chosen step field is not itself an endogenous prime mechanism.

## Reproducibility and integrity disclosure

All proofs are exact; input and records are the [card](candidate-card.md), [claim ledger](claim-ledger.md), [overview](README.md) and [template](../paper-template.md).
Author read the entire95-line card with `sed -n '1,135p'`, and the entire107-line template with `sed -n '1,125p'`; `wc -l` and `sha256sum` identify the frozen input.
The full class uses exact legal-word and sampled-time predicates; controls classify their complete displayed carriers, not a finite numerical window.
Mechanical checks are full author-file self-read, candidate/outcome agreement, local links, table columns and unchanged card hash.
No scientific code/numerics, network, old edits, Git mutation, PDF, publication, operator or target-zero work was used.

AI author `/root/batch_clock_scope_review` derived and drafted the owner, functor, weighted-cycle and criterion proofs; root owns card/integration.
Design-only collision reads were409card1–95 before Outcome, prefixSHA `3d9e251104c036e3cd11263e59cbd252a552fe55318451266b2d633632f4320c`, and453card1–91 original EOF, prefixSHA `9cbd785bb07b7461a3fcb94a51b4ae17068176567678143689b9844a375d1326`.
Their full files were only hashed beyond those prefixes; no old proof or Outcome appendix was read by this author. Registry and root messages exposed completion metadata and shared history.
Root and scout informal schedule-feasibility thoughts preceded freeze; the design was not blind or a sealed prediction.
Same-author helper `/root/batch_clock_scope_review/ccg_cotangent_probe` was assigned only complete partial control D from the frozen459 card, not a review seat.
Its only file read was `sed -n '1,130p'` on the459 card through the scientific EOF marker; `wc -l` returned95 and `sha256sum` matched the frozen hash in §2.
It reported no other files, writes, scientific code/numerics, network or additional agents; its complete D formulas were checked against this manuscript, not treated as independent-review evidence.
No 459 CP1 text, raw, reviewer final, current peer manuscript or old proof was read by this author.
AI agents supplied derivation, drafting and internal checking; same-model shared-history assistance is `NOT_CALIBRATED`, not blind, human, external or cross-model validation.
No human or external mathematical verification is certified; human contributions, funding and competing interests are unspecified, with no human-participant data.
ARS supplied bounded proof/draft and disclosure discipline, not a publication pipeline; `criteria_binding_unavailable`, and publication readiness is not claimed.
