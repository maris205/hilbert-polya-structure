# 431 — card-only independent derivation

Candidate: ANG-20260923-DCR01. Date: 2026-09-23.
Batch GLOBAL-GATE-FEEDBACK-20260923-Q; round2/5,430–434 only.
Root reported its full CP1 read and separately released this raw mathematics.
Sole scientific input: original candidate-card.md lines 1–90, completely
reread after release through its explicit original EOF line.
candidate-card.md original prefix — 90 lines; SHA256 ac780971592ee4b848898560e48290a2a2ab7e6a7b5de157d7b6cf605613be65
Frozen scope-review.md — 83 lines; SHA256 87d38e4fda591451bcce03c3468a210cc318b8b3f63f98f701a3aa9515f15d5c
No author paper/README/ledger, outcome append, peer, helper or sibling
science was read. Old-card references were seen only inside this card.
The card exposed its designer's informal cancellation expectation; this is
not blind preregistration. Earlier shared history remains exposed.
Retained ARS instructions govern this work, not claimed as freshly reread.
AI supplied this proof and checking; same-model internal NOT_CALIBRATED,
not external, human, cross-model or independent-of-shared-history validation.
No auxiliary agent, scientific code/numerics, literature, Git, publication,
fixed-point table or higher-period census was used.

## 1. Complete three owners and exact divisor interface

Each owner separately retains
\[
X=M_2(\mathbb R)\times M_2(\mathbb R),\qquad \mu=\mathrm{Leb}_8
\]
in the original matrix-entry coordinates. At \(z=(A,B)\), put
\(m=\lfloor B_{12}\rfloor,n=\lfloor A_{12}\rfloor\).
MAIN has domain \(\det B\ne0,m\ne0,m\mid n\), exponent \(q=n/m\), and
\[
T_{\rm M}(A,B)=(B,B^{-q}AB^q).
\]
G has domain \(\det B\ne0\), exponent
\(q_G=\lfloor n/m\rfloor\) if \(m\ne0\), and \(q_G=0\) if \(m=0\);
it uses the corresponding conjugation, without a divisibility condition.
Q has MAIN's domain but action \(T_Q(A,B)=(B,B^{-1}AB)\).
All powers used here exist for every signed integer exponent because B
is invertible. A need not be invertible.
Every owner is Borel: the floor-label domains are Borel and each
fixed-exponent formula is analytic on the open invertible-B set.
Every other point of X remains a terminal with identity and all incoming,
but no next step or next-step clock. No matrix slice has been selected.

At the stated integer seed, \(\det B_d=(d+1)-d=1\),
\(m=d,n=N\). MAIN permission is therefore exactly \(d\mid N\).
When permitted the actual exponent is \(q=N/d\). If
\(C=B_d^{-q}A_NB_d^q\), multiplication gives \(A_NB_d^q=B_d^qC\).
The successor is \((B_d,C)\); its own current-entry readings, not the
original labels, govern any next step. This proves the stated divisor
permission/transport interface, not interface invariance, prime-period
purity, conjugacy, symplecticity or strong naturalness of the readout.

## 2. Actual inverse completeness, without integer or source cutoffs

For every fixed integer k define
\[
\Theta_k(U,V)=(U^kVU^{-k},U),\qquad \det U\ne0.
\]
It is a real-analytic diffeomorphism from
\(\mathrm{GL}_2(\mathbb R)\times M_2(\mathbb R)\) onto
\(M_2(\mathbb R)\times\mathrm{GL}_2(\mathbb R)\), with inverse
\((A,B)\mapsto(B,B^{-k}AB^k)\). Direct substitution proves both identities.
Integer powers, including negative and zero powers, are analytic on GL2;
no eigenbasis, diagonalization or invertibility of V is needed.

MAIN labels are ALL \((m,n)\in\mathbb Z^2\) with \(m\ne0,m\mid n\).
For such a label set \(k=n/m\), and restrict \(\Theta_k\) to
\[
E^{\rm M}_{m,n}
=\{(U,V):\det U\ne0,\ \lfloor U_{12}\rfloor=m,\
        \lfloor(U^kVU^{-k})_{12}\rfloor=n\}.
\]
Every retained point reconstructs an actual legal source, whose own
exponent is k and whose forward image is exactly \((U,V)\).
Conversely, any actual source reaching \((U,V)\) has \(B=U\), its actual
floors give m,n,k, and its forward equation forces \(A=U^kVU^{-k}\).
It is therefore in exactly its actual source-label branch above.

G uses ALL integer pairs m,n, with its OWN integer k=q_G(m,n), and
\[
E^G_{m,n}
=\{(U,V):\det U\ne0,\ \lfloor U_{12}\rfloor=m,\
        \lfloor(U^kVU^{-k})_{12}\rfloor=n\}.
\]
There is no \(m\mid n\) or \(m\ne0\) requirement here.
Substitution proves its own forward identity. Every actual G predecessor
conversely has precisely those floors and exponent, proving completeness,
including the entire m=0 branch family with k=0.

Q has only the one proposed inverse \(\Theta_1\), on the Borel domain
\[
E^Q=\{(U,V):\det U\ne0,\ m=\lfloor U_{12}\rfloor\ne0,\
                       m\mid \lfloor(UVU^{-1})_{12}\rfloor\}.
\]
Its forward identity follows by conjugation with U and its inverse.
Any actual Q predecessor must equal this proposal and pass these tests.
Thus Q is a partial injective map. Unused arithmetic q labels do not
generate additional branches or copies of this predecessor.

All inverse domains are Borel restrictions of the stated open analytic
domains. MAIN/G have at most countably many predecessors at every point;
Q has at most one. An actual source fixes its two floors uniquely, so
identical source descriptions never increase multiplicity.
The target needs no next step: V can be singular, and its own permission
can fail, while a predecessor above remains legal.
If \(\det U=0\), the target has no one-step predecessor in any owner,
since every legal forward first matrix is its invertible B.
This does not itself make that target terminal; its forward permission
uses its own second matrix and digits. Every such object is retained.

## 3. FULL eight-coordinate determinant and every-Borel IMAGE

Use four matrix entries for each matrix, in the same order in each block.
At every \((U,V)\) with \(\det U\ne0\), differentiation of \(\Theta_k\)
has the full eight-by-eight block form
\[
D\Theta_k=
\begin{pmatrix}K_{U,V,k}&L_{U,k}\\ I_4&0\end{pmatrix},
\qquad L_{U,k}(W)=U^kWU^{-k}.
\]
Here K is the entire derivative with respect to U; none of its feedback
terms has been dropped or assumed zero. Swapping the two groups of four
columns contributes sign \((-1)^{4\cdot4}=1\), leaving a block upper
triangular matrix with diagonal \(L_{U,k},I_4\). Hence
\[
\det_{\mathbb R^8}D\Theta_k=\det_{\mathbb R^4}L_{U,k}.
\]
This equality is an eight-coordinate block determinant calculation,
not restriction to a four-dimensional conjugation slice.

For an invertible two-by-two S, left multiplication \(W\mapsto SW\)
acts on each of the two columns and has determinant \((\det S)^2\).
Right multiplication \(W\mapsto WS^{-1}\) acts on each of the two rows
and has determinant \((\det S^{-1})^2\); transposition of a row's matrix
does not change that determinant. Multiplying these two determinants,
\[
\det(W\mapsto SWS^{-1})
=(\det S)^2(\det S^{-1})^2=1 .
\]
This argument includes negative \(\det S\) without an orientation shortcut.
Taking \(S=U^k\) proves the full identity
\[
\boxed{\det_{\mathbb R^8}D\Theta_k=1}
\]
at EVERY point of its full open domain and for EVERY signed integer k.
In particular k=0 retains the full block swap, not a zero-dimensional map.

Apply this calculation to each MAIN actual k, each G actual q_G, and
independently to Q's single k=1 inverse. Their own prescribed versions are
\[
J^{\rm M}_{m,n}=1,\qquad J^G_{m,n}=1,\qquad J^Q=1
\]
on their respective actual domains, including every assigned floor face.
The Q calculation uses its fixed exponent and MAIN permission only as
specified; it is not a conclusion imported from a MAIN quotient branch.

Each \(\Theta_k\) is an injective analytic diffeomorphism of the two open
sets established above. Change of variables, restricted to ANY Borel
subset E of an actual inverse domain, therefore gives
\[
\mu(\Theta_k E)=\int_E|\det D\Theta_k|\,d\mu=\int_E1\,d\mu=\mu(E).
\]
The same proof on Q's own actual domain gives its every-Borel IMAGE.
It applies to unbounded sets as an equality of nonnegative extended
integrals, and to null sets as well as positive-measure sets.
The analytic germ prescribes the point value on all arithmetic faces;
measure-theoretic a.e. uniqueness is not claimed to fix null-point values.
No periodic-point version, measure change or coordinate slice is inserted.

This is unit IMAGE on every actual inverse branch. No global MAIN/G injectivity
is asserted; unit branch Jacobians alone do not rule out overlapping forward images.
Thus no unsupported global set-volume preservation assertion for a
possibly many-to-one forward map, nor classical symplectic claim, is used.

## 4. All actual histories and complete kernels

For each of the three OWNERS separately, the legal clock is now proved
\[
\kappa_O(z)=-\log J_{\theta_z}(T_Oz)=0
\]
at EVERY legal source. At a terminal this expression remains undefined.
For every finite legal r-step history, \(S_r(z)=0\), with \(S_0=0\)
also at terminals. There is no infinite history or infinite product here.

Let \(P_O(y)\) be the set of ALL passing inverse proposals from Section 2,
with identical actual points identified. Define
\[
P_O^0(y)=\{y\},\qquad
P_O^{j+1}(y)=\bigcup_{x\in P_O^j(y)}P_O(x).
\]
Both inverse identities prove inductively that these are exactly all
legal j-step starting points into y. These countable sets use every
integer label and every depth; they may be infinite and are not truncated.
Q's predecessor sets have at most one element at each depth.

The full retained-lag groupoid is
\[
\mathscr G_O=\{(z,r-s,w):T_O^rz=T_O^sw,\ r,s\ge0
                  \text{ with both histories legal}\}.
\]
It is Borel as a countable union of equal-iterate Borel relations with
integer lag, and has countable source/range fibres by the inverse atlas.
Identities use r=s=0. Inversion exchanges the two endpoints and negates lag.
For composition with presentations \(T^rz=T^sw\) and \(T^uw=T^vx\),
put \(t=\max(s,u)\). The already legal middle history to t lets both
equalities extend to
\(T^{r+t-s}z=T^{v+t-u}x\). The lag is \((r-s)+(u-v)\).
No unavailable step after a terminal is introduced.
This proves closure of the ACTUAL groupoid, not a freely completed graph.

Every presentation has
\[
c_O(z,r-s,w)=S_r(z)-S_s(w)=0.
\]
It therefore descends to identified triples, is additive under the above
composition, and changes sign on inversion. The forward arrow
\((T_Oz,-1,z)\) has clock \(-\kappa_O(z)=0\).
Every finite history bisection is a composition of the actual analytic
branches and their inverses; all have IMAGE density one by Section 3.
Countable disjoint Borel restrictions preserve that identity on injective
history charts. Thus its density is exactly \(e^{-c_O}=1\).

The COMPLETE kernels, with no suppression of coalescing branches, are
\[
\begin{aligned}
\ker c_O&=\mathscr G_O,\\
\ker\ell_O&=\{(z,0,w):T_O^rz=T_O^rw\text{ for some legal }r\},\\
\ker\ell_O\cap\ker c_O&=\ker\ell_O.
\end{aligned}
\]
Equivalently the lag kernel is the union, over every r and target y, of
ALL zero-lag pairs from \(P_O^r(y)\times P_O^r(y)\).
This inverse-recursion description is exhaustive and retains every
possible nonunit zero-lag arrow for MAIN/G; it assumes no global injectivity.
For Q, each legal iterate is injective, since its one-step map is.
Its lag and joint kernels therefore consist exactly of units, whereas its
clock kernel remains the entire Q groupoid, not merely its units.

## 5. Entire isotropy, ALL incoming, phases and repetitions

A nonzero source self-lag for any partial deterministic map means two
distinct times in its legal future coincide. The repeated legal segment
then repeats forever. Conversely an eventual legal cycle produces such
equalities. If its least source period is p, advancing any equality into
that core shows every self-lag is a multiple of p, and sufficiently late
core times realize every signed multiple. Consequently, for each owner,
\[
\mathscr G_{O,z}^{\,z}=p\mathbb Z
\quad\hbox{for an eventual least-period-p future}.
\]
A finite-terminal or non-eventually-periodic legal future has only the
identity self-arrow. No periodic-existence assertion or census is needed
for this complete conditional classification.

Because the ENTIRE cocycle is zero, at EVERY retained source, regardless
of which of these cases occurs,
\[
\boxed{H_{O,z}=c_O(\mathscr G_{O,z}^{\,z})=\{0\}}.
\]
This is equality of the full return group, not a selected subgroup.
In the full extension each arrow acts by \((w,h)\mapsto(z,h)\).
The extension isotropy equals source isotropy: pZ on eventual periodic
packets and trivial in the other cases. Ineffective pZ is not deleted.

For every target z, ALL incoming arrows are precisely
\[
(z,r-s,w),\quad r\text{ legal at }z,\quad s\ge0,\quad
w\in P_O^s(T_O^rz),
\]
with equal triples identified. At range height h every source height is
the SAME h. This includes every incoming tail, arbitrary coalescence,
all integer labels and all finite depths.
At a terminal z only r=0 is allowed, leaving every \(P_O^s(z)\) and its
actual arrows; the identity survives even if all positive-depth sets empty.
Predecessor-free points are not deleted or assumed forward terminal.

Write \(\mathcal O_z\) for the entire source equivalence packet of z.
Since arrows leave h unchanged, extension orbits are exactly
\(\mathcal O_z\times\{h\}\). Its orbit SET is therefore identified with
the set of pairs \((\mathcal O_z,h)\), with every \(h\in\mathbb R\).
Height translation sends that pair to \((\mathcal O_z,h+t)\); its
stabilizer is exactly \(\{0\}\). All real phases remain and translation
is free on every physical packet, even when source isotropy is pZ.
No measurable regularity or manifold structure of this quotient is claimed.
Different source packets are not merged because their clocks agree.

There is no least positive element of \(\{0\}\), hence no positive
primitive or positive repetition in ANY of these three physical ledgers.
If an actual source cycle exists, its repeated source loops and ineffective
isotropy remain, all with clock zero. “No positive primitive” does NOT
mean “no source cycle” or “no incoming arrow.”

## 6. Decisive global result and stop boundary

MAIN has a complete actual inverse owner and its prescribed native
eight-dimensional IMAGE clock, but its positive primitive ledger is EMPTY
on the ENTIRE frozen source. This fails the mandatory nonemptiness target
globally, independently of existence or classification of any source cycle.
The result is STOP / FORK, not a vacuous prime-purity pass or bounded
fixed-window observation. The two controls independently share this
unit-IMAGE/zero-cocycle outcome while retaining their own domains and fibres.

The same-object ledger has stayed intact: full X, Lebesgue8, actual
transport, analytic point version, retained lag, incoming, isotropy and
all-height extension were not changed to obtain this result.
There is no switch to eigenvalue/unstable determinants, a matrix slice,
selected representatives, alternative measure or an external positive roof.
The all-entry conjugation determinant is the decisive obstruction for
THIS frozen object, not a theorem against every arithmetic groupoid.
Strong naturalness remains unestablished; no repair or continuation of this
stopped source is authorized by the card.
Classical NOT APPLICABLE; arithmetic T1 NOT PASSED; T3 NOT AUDITED;
formal Route UNASSIGNED; B NOT INVOKED.

The decisive full-eight-dimensional argument was sent to root before this
report was written. All work above is exact proof from the released card;
no new fixed-point or periodic census was performed.
EOF — freeze after full self-read; HOLD for root's full read and a distinct PAPER UNLOCK.
