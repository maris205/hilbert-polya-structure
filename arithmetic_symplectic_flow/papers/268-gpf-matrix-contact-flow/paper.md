# GPF matrix contact flow: a complete owner with doubled and mixed returns

**Paper ID:** `268-gpf-matrix-contact-flow`  
**Candidate ID:** `ANG-20260919-GMC01`  
**Date:** 2026-09-19  
**Status:** `FULL LEAFWISE CONTACT OWNER; LOG-SCALE PRIME CLOCK; MIXED/DOUBLED PACKETS — STOP / FORK`  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

The frozen GPF matrix quotient has a free proper integer action, a Hausdorff
quotient with smooth three-dimensional plaques, and a complete leafwise Reeb
flow preserving its contact volume. These statements hold on the full path
space and every group fibre. Its complete primitive ledger contains exactly
two oriented circles for each prime source and two for the mixed GPF
four-cycle. There are no other periodic or stationary flow states. The
twofold multiplicity comes from the two possible eigenline orderings;
centralizer freedom contributes only the time phase, not further packets.
The prime period is
\(\ell_p=2\operatorname{arcosh}((p+1)/(2\sqrt{p-1}))\), strictly greater
than \(\log p\), although \(\ell_p=\log p+p^{-1}+O(p^{-2})\).
The mixed period is \(2\operatorname{arcosh}(49\sqrt3/4)\).
This establishes the declared geometric owner and its actual clock, while
the doubled multiplicity, retained mixed packet and exact-clock mismatch
stop target promotion. No orbit is deleted, no clock is repaired, and no
analytic object is introduced after that stop.

## 1. Frozen identity and input boundary

All definitions below are those of the unchanged
[version-1 candidate card](candidate-card.md). The source is

\[
S=\mathbb N_{>0}^{\,2},\quad
G(x,y)=(y,\operatorname{gpf}(x+y)),\quad
X_G=\{z\in S^{\mathbb Z}:z_{j+1}=G(z_j)\ \forall j\}.
\]

The topology is the product-subspace topology from discrete \(S\), and
\(\sigma\) is the left shift. For \(z_0=(x_0,y_0)\), the exact observable is

\[
a(z)=\operatorname{gpf}(x_0+y_0),\qquad
M_a=\frac1{\sqrt{a-1}}
\begin{pmatrix}a&1\\1&1\end{pmatrix},\qquad a\ge2.
\tag{1}
\]

Let \(L=PSL(2,\mathbb R)\), retaining every element, and set

\[
T(z,g)=(\sigma z,M_{a(z)}g),\qquad
Q=(X_G\times L)/\langle T\rangle,
\tag{2}
\]
\[
\Phi^t[z,g]=[z,gA_t],\qquad
A_t=\operatorname{diag}(e^{t/2},e^{-t/2}).
\tag{3}
\]

There is no separately specified roof. Physical time is exactly the
parameter \(t\) in (3). Positive and negative deck powers, all backward
histories and both eigenline orderings remain in the owner.

| Item | Same-object owner and scope |
| --- | --- |
| Arithmetic source | The full GPF path space and current-state output (1) |
| Carrier | The full quotient (2), with smooth three-dimensional plaques |
| Differential form | \(\alpha_g(v)=2\operatorname{tr}(H g^{-1}v)\), \(H=\operatorname{diag}(1/2,-1/2)\) |
| Physical flow | The complete right-diagonal action (3) |
| Primitive convention | All least-period point-flow orbits, modulo actual time translation only |
| Classical ASFS symplectic base / mapping torus | NOT SUPPLIED; no global manifold conclusion is inferred from plaques |
| Trace / transfer space / zeta / determinant / quantum owner | NOT SUPPLIED; T3 is not pursued |

The sole external-to-this-proof mathematical input is the corrected source
classification in [266, §§3–4](../266-prime-source-return-rescreen/paper.md):
the periodic \(G\)-states are all \((p,p)\), for primes \(p\), and the
single four-cycle

\[
C=((7,3),(3,5),(5,2),(2,7)).
\tag{4}
\]

Consequently the periodic shift orbits in the *full* \(X_G\) are the
constant paths \(z^{(p)}\) and this one four-phase orbit. This input does
not say that every bilateral history is periodic. Its source hypotheses
and correction are owned by 266; the group geometry and times proved below
do not follow from that input by analogy. No other candidate's clock or
geometric theorem is imported.

## 2. Full action and Hausdorff quotient

### 2.1 The two-sided owner

The path constraints are closed in the product of discrete spaces, so
\(X_G\) is Hausdorff, metrizable and second countable. Both shifts are
continuous and inverse on this complete path space. The map \(a\) is
locally constant. Each matrix in (1) has determinant one and an inverse;
hence (2) is a homeomorphism with the frozen inverse

\[
T^{-1}(z,g)=
\bigl(\sigma^{-1}z,M_{a(\sigma^{-1}z)}^{-1}g\bigr).
\tag{5}
\]

For \(k>0\) define the positive determinant-one lift of the cocycle by

\[
P_k(z)=M_{a(\sigma^{k-1}z)}\cdots M_{a(z)},\quad P_0(z)=I,
\quad P_{-k}(z)=P_k(\sigma^{-k}z)^{-1}.
\tag{6}
\]

Then \(T^k(z,g)=(\sigma^kz,P_k(z)g)\) for every integer \(k\). For a
class in \(PSL(2,\mathbb R)\), the Euclidean matrix operator norm of a lift
is well defined because replacing the lift by its negative does not
change that norm.

### Lemma 1 — Uniform deck escape

For all histories and integers \(k\),

\[
\|P_k(z)\|_2\ge2^{|k|}.
\tag{7}
\]

**Proof.** Consider the cone \(x>0,\ 0\le y\le x\). Its image under (1)
has slope
\((x+y)/(ax+y)\in[0,1]\), so the cone is preserved. The new first
coordinate satisfies

\[
x'=\frac{ax+y}{\sqrt{a-1}}
\ge\frac a{\sqrt{a-1}}x\ge2x,
\]

where the last inequality is \((a-2)^2\ge0\). Applying a length-\(k\)
product to \((1,0)\) proves (7) for positive \(k\). A real determinant-one
two-by-two matrix and its inverse have the same Euclidean operator norm:
its inverse is an orthogonal conjugate of its transpose. Apply this fact
to (6) to obtain the negative case. The zero case is immediate. ∎

### Proposition 2 — Free proper action and local plaques

The integer action generated by \(T\) is free and proper. Its quotient
\(Q\) is Hausdorff and second countable, and the projection has locally
disjoint deck translates. It therefore supplies charts with continuous
transverse coordinate in \(X_G\) and smooth three-dimensional group
plaques. No local compactness of \(X_G\) is needed for these claims.

**Proof.** A fixed point of a nonzero \(T^k\) would require
\(P_k(z)=I\) in \(PSL(2,\mathbb R)\), whose representatives have norm
one, contradicting (7).

More generally, if two sets have group coordinates in compact sets
\(K_1,K_2\subset L\), then any deck intersection between them requires

\[
2^{|k|}\le\|P_k(z)\|_2
=\|g'g^{-1}\|_2
\le\sup_{g'\in K_2}\|g'\|_2\,
\sup_{g\in K_1}\|g^{-1}\|_2.
\tag{8}
\]

Only finitely many \(k\) can satisfy this. In particular, for the action
map \((k,x)\mapsto(x,T^kx)\), the inverse image of a compact subset of
\((X_G\times L)^2\) lies in finitely many copies of its compact first
projection; the inverse image is closed there and is compact. This is
properness in the compact-preimage sense.

For the local statement, first choose a group neighbourhood with compact
closure. Inequality (8) leaves only finitely many nonzero deck powers that
could meet it. Freeness and the Hausdorff property let us shrink a product
neighbourhood \(U\) of any given point until
\(U\cap T^kU=\varnothing\) for every nonzero \(k\). The quotient
projection is open, and it is a homeomorphism from \(U\) onto its image.

For two points in distinct orbits, take two such bounded group
neighbourhoods. There are again finitely many potentially intersecting
deck powers. Since none takes the first centre to the second centre,
finite simultaneous shrinking separates their saturated images. Thus the
quotient is Hausdorff. The images of a countable base of the product form
a countable base of the quotient.

Choose the group neighbourhood in a smooth coordinate chart. A chart
overlap splits into open subsets of the form \(U\cap T^{-k}U'\), on
each of which the deck index \(k\) is fixed. Its matrix factor depends on
finitely many discrete source coordinates and is locally constant in the
transverse coordinate. The transitions are therefore smooth left
translations on the three-dimensional plaques. This proves precisely the
claimed transverse/leafwise structure, not a global finite-dimensional
manifold or a locally compact transverse space. ∎

Right multiplication by \(A_t\) commutes with all left cocycle factors.
Hence (3) is well defined and is a jointly continuous action for every
real \(t\), with inverse \(\Phi^{-t}\); it is smooth on plaques. Its
definition uses the globally defined group action for all real times, so
completeness does not require a selected return section or a roof estimate.

## 3. Contact form, Reeb field and conserved leaf volume

All differential claims here are leafwise. On \(SL(2,\mathbb R)\), the
formula for \(\alpha\) is unchanged under
\((g,v)\mapsto(-g,-v)\); it therefore defines a form on \(L\).
It is left invariant, and thus is preserved by every deck map in (2).
The local forms consequently descend consistently to the plaques of \(Q\).

Use the Lie algebra basis

\[
H=\begin{pmatrix}1/2&0\\0&-1/2\end{pmatrix},\quad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]

Direct multiplication gives

\[
[H,E]=E,\quad [H,F]=-F,\quad [E,F]=2H,
\quad \alpha(H)=1,\quad\alpha(E)=\alpha(F)=0.
\]

For left-invariant fields, the definition of exterior derivative gives
\(d\alpha(X,Y)=-\alpha([X,Y])\). Therefore

\[
d\alpha(E,F)=-2,\qquad d\alpha(H,E)=d\alpha(H,F)=0,
\quad (\alpha\wedge d\alpha)(H,E,F)=-2\ne0.
\tag{9}
\]

Thus \(\alpha\) is contact. The field generating right multiplication
by \(A_t=\exp(tH)\) is \(R_g=gH\), the left-invariant field with value
\(H\). Equation (9) proves exactly

\[
\alpha(R)=1,\qquad \iota_Rd\alpha=0.
\]

It is the Reeb field of the frozen form, without changing the time
normalization. Its flow preserves \(\alpha\): alternatively to the Reeb
identity, the right-translation formula gives
\(2\operatorname{tr}(H A_t^{-1}g^{-1}vA_t)
=2\operatorname{tr}(H g^{-1}v)\) because \(A_t\) commutes with \(H\).
It follows that \(\alpha\wedge d\alpha\) is a preserved, nonzero leaf
volume. No transverse measure or global finite invariant probability
measure is chosen or inferred. Since \(\alpha(R)=1\), no point is
stationary.

## 4. All return equations and exact primitive multiplicity

### 4.1 Nonperiodic histories and the zero deck power

A positive return of \([z,g]\) is equivalent to the existence of an
integer \(k\) such that

\[
\sigma^kz=z,\qquad gA_t=P_k(z)g,\qquad t>0.
\tag{10}
\]

Equality is in \(PSL(2,\mathbb R)\). If \(k=0\), it forces \(A_t=I\)
in that group, which for real \(t\) forces \(t=0\). Thus a nonperiodic
history has no positive return. This excludes its entire group fibre,
not only an observed or bounded part.

### 4.2 One periodic source orbit

Fix a source path of least shift period \(m\), and put \(P=P_m(z)\).
Every entry of its positive lift is strictly positive and \(\det P=1\).
Writing \(P=\left(\begin{smallmatrix}b&c\\d&e\end{smallmatrix}\right)\),
we have \(be=1+cd>1\), hence \(\operatorname{tr}P=b+e>2\).
It has distinct positive real eigenvalues \(\lambda,\lambda^{-1}\),
where \(\lambda>1\). Define

\[
\ell(P)=2\log\lambda
=2\operatorname{arcosh}\!\left(\frac{\operatorname{tr}P}{2}\right)>0.
\tag{11}
\]

Choose ordered real eigenvectors, first for \(\lambda\), then for
\(\lambda^{-1}\), and normalize their determinant to one by changing a
sign and a scale if necessary. The resulting \(c\in L\) satisfies

\[
Pc=cA_{\ell(P)}.
\tag{12}
\]

Let \(W\) be the class of
\(\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\).
Since \(W^{-1}A_tW=A_{-t}\), also
\(P(cW)=(cW)A_{-\ell(P)}\).

### Proposition 3 — Exactly two primitive circles per source cycle

Above this entire source orbit there are exactly two periodic point-flow
orbits. Both have least positive time \(\ell(P)\). Their full periodic
sets at the chosen source phase are

\[
\{[z,cA_u]:u\in\mathbb R\},\qquad
\{[z,cWA_u]:u\in\mathbb R\}.
\tag{13}
\]

They are distinct, and there are no additional periodic states in any
group fibre above the source orbit.

**Proof.** The first equation in (10) requires \(k=rm\) for some integer
\(r\). Periodicity of the cocycle then gives \(P_k(z)=P^r\), also for
negative \(r\). Comparing eigenvalues in the second equation of (10)
forces

\[
t=|r|\ell(P),\qquad r\ne0.
\tag{14}
\]

This follows also from the absolute trace in \(PSL(2,\mathbb R)\):
both positive lifts have eigenvalues of positive sign, so a representative
sign cannot create an additional time.

For \(r>0\), conjugation in (10) assigns the first column of a lift of
\(g\) to the expanding eigenline of \(P\) and the second to the contracting
line. Thus \(g=cA_u\) for some real \(u\). Explicitly, a determinant-one
matrix commuting with a diagonal matrix of distinct eigenvalues is
\(\operatorname{diag}(v,v^{-1})\), \(v\ne0\); modulo \(\pm I\),
take \(v>0\), giving exactly \(A_u\). For \(r<0\), the eigenline order
is reversed and the same argument gives exactly \(g=cWA_u\).
This proves that all centralizer freedom in each orientation is a single
right-\(A\) flow orbit, not a new continuous family of packets.

Conversely, (12) proves return at \(t=\ell(P)\) on the first set of
(13), using \(r=1\). On the second set, \(P^{-1}(cW)=(cW)A_{\ell(P)}\),
so \(r=-1\) gives the same positive return. Equation (14) proves
minimality and shows that all repetitions have times \(j\ell(P)\),
\(j=1,2,\ldots\).

The two right cosets in (13) are distinct because \(W\) is not diagonal.
They cannot become identified by the quotient or the flow: at the chosen
source phase any identifying deck map is \(P^r\), and left multiplication
by \(P^r\) preserves each of these cosets separately. The other \(m-1\)
source phases are already identified with this fibre by their prescribed
deck maps. They do not contribute \(m\) extra copies. This proves the
claimed exact multiplicity two. ∎

This proof applies to every group element before classifying the periodic
ones. The sets in (13) are consequences of (10), not a replacement carrier
or a selected section. Opposite orientations are distinct point-flow
orbits under the frozen convention, even though each circle's points are
identified up to time translation.

## 5. Complete prime and mixed ledger

### 5.1 Prime periods and their clock discrepancy

For the constant prime source, \(a(z^{(p)})=p\), \(m=1\), and
\(\operatorname{tr}M_p=(p+1)/\sqrt{p-1}\). The actual least period of
each of its two circles is therefore

\[
\boxed{\ell_p=
2\operatorname{arcosh}\!\left(\frac{p+1}{2\sqrt{p-1}}\right)
=\log\frac{p+1+\sqrt{(p-1)^2+4}}
                {p+1-\sqrt{(p-1)^2+4}}.}
\tag{15}
\]

The formula follows from the return equation, not from declaring an
eigenvalue to be time. In particular,

\[
\frac{p+1}{2\sqrt{p-1}}
>\frac{p+1}{2\sqrt p}
=\cosh\!\left(\frac{\log p}{2}\right),
\]

so monotonicity of \(\operatorname{arcosh}\) gives

\[
\ell_p>\log p\qquad\text{for every prime }p.
\tag{16}
\]

This includes the boundary prime:

\[
\ell_2=2\operatorname{arcosh}(3/2)
=2\log\frac{3+\sqrt5}{2}>\log2.
\tag{17}
\]

For clarity about the large-prime scale, the larger eigenvalue of the
unnormalized \(B_p\) is

\[
\beta_+(p)=\frac{p+1+\sqrt{(p-1)^2+4}}2
=p+\frac1{p-1}+O(p^{-3}).
\]

The elementary expansion follows by applying
\(\sqrt{1+x}=1+x/2+O(x^2)\) to \(x=4/(p-1)^2\). Since
\(\ell_p=2\log\beta_+(p)-\log(p-1)\), it yields

\[
\ell_p=\log p+\frac1p+\frac5{2p^2}+O(p^{-3}).
\tag{18}
\]

Thus the clock is asymptotic to \(\log p\), with an error tending to
zero, but it is not that exact clock. Nor could one constant global time
rescaling correct every prime: the asymptotic ratio would force that
constant to be one, leaving (16). No such rescaling is performed.

### 5.2 The full mixed four-cycle

At the source phase \(z_0=(7,3)\), the outputs \(a(\sigma^jz)\) are
exactly \(5,2,7,3\). Their order in the *left* cocycle is

\[
P_C=M_3M_7M_2M_5.
\]

Exact integer multiplication gives

\[
B_2B_5=\begin{pmatrix}11&3\\6&2\end{pmatrix},\quad
B_7B_2B_5=\begin{pmatrix}83&23\\17&5\end{pmatrix},\quad
B_3B_7B_2B_5=\begin{pmatrix}266&74\\100&28\end{pmatrix}.
\]

Its determinant is \(48=(5-1)(2-1)(7-1)(3-1)\). Consequently

\[
P_C=\frac1{\sqrt{48}}
\begin{pmatrix}266&74\\100&28\end{pmatrix},\qquad
\operatorname{tr}P_C=\frac{49\sqrt3}{2},
\]
\[
\boxed{\ell_C=2\operatorname{arcosh}(49\sqrt3/4).}
\tag{19}
\]

Proposition 3 gives exactly two primitive circles of this time, not eight
circles from counting the four source phases separately. The mixed
source survives intrinsically in the complete geometric owner. Its
four-step word is not a traversal of a constant prime source, so neither
circle is a repetition of a prime circle.

### 5.3 Exhaustive result

Combining the identified input from 266 with Propositions 2–3 proves:

| Complete source sector | Primitive point-flow circles | Least positive time | Repetitions |
| --- | --- | --- | --- |
| Each prime diagonal \(z^{(p)}\) | Exactly two, opposite eigenline orderings | \(\ell_p\) in (15) | \(j\ell_p\), \(j\ge1\), for each circle separately |
| The one mixed four-cycle \(C\) | Exactly two | \(\ell_C\) in (19) | \(j\ell_C\), \(j\ge1\), for each circle separately |
| Every nonperiodic history, all group states | None | No positive return | None |
| Stationary states anywhere | None | Not applicable | Not applicable |

No other periodic states are omitted: (10) first forces a periodic source,
266 exhausts those sources, and Proposition 3 exhausts every group fibre
above them. This is an infinite exact classification conditional only on
the explicitly identified source theorem, not a finite orbit census.

## 6. Controls, collision boundary and limits

The zero deck power does not create a stationary or period-zero exception;
negative deck powers are essential for the second orientation. Passing
from \(SL\) to the frozen \(PSL\) removes the central sign duplication,
not the two distinct orientations. Removing either orientation or the
mixed source would change the complete packet convention or carrier.

Replacing all \(M_a\) by identity matrices is a different proposed owner.
Over a constant source its integer deck action has an infinite stabilizer,
so it loses both freeness and properness. The Hausdorff/contact-owner
conclusions above must not be transferred to it. Its algebraic return
equation would require \(A_t=I\), which has no positive-time solution;
this observation alone is not a new full geometric-owner theorem. In
particular, merely counting periodic source words cannot replace the
geometrical return argument.

As the declared PROVES_TOO_MUCH comparison, replace \(X_G\) by the full
shift \(\{2,3,\ldots\}^{\mathbb Z}\), use \(a(w)=w_0\), and retain
the same matrix cocycle, deck action and right-diagonal flow. Every
constant integer \(n\ge2\), including a composite, would then produce
the same two-circle construction by the return calculation in §4, with
(15) evaluated at \(n\). No complete classification of this changed
source is claimed or needed here. Thus primality in this candidate is supplied by the specific
GPF periodic source, not generated by the contact geometry alone.

The nearest local clock comparison is
[232, CAC01](../232-source-feedback-frontier/candidate-card.md). Its
direction-history/scale carrier and integral-unimodular source matrices
are not this full group quotient. Here \(\det B_a=a-1\), and the
normalized matrices need not be integral. Neither its return theorem nor
its integral-unimodular clock obstruction was used. The geometric
extension also is not the passive plane of
[169](../169-ordered-cover-leafwise-symplectic-lift/candidate-card.md) or
the facewise cotangent owner of
[196](../196-face-cotangent-conservative-lift/candidate-card.md).
These are local mechanism comparisons, not a claim of literature-wide
novelty.

The retained lineage is prime-factor evaluation, GPF sequential recurrence,
full reversible histories, matrix holonomy and this right-diagonal flow.
This is consistent with the source/geometric arrow in the
[prior-work guide](../../docs/prior_work/README.md), without claiming a
Logistic or Hénon conjugacy. The choice \(a\mapsto B_a\) and the group
flow remain declared designs. Geometry does not feed back into the
arithmetic recurrence. A rigorously owned elapsed time is not evidence
that arithmetic uniquely or naturally selected that time law.

## 7. Gate assessment and stop decision

| Obligation | Result for this unchanged owner | Boundary |
| --- | --- | --- |
| Full action, quotient and local differential owner | ESTABLISHED by §§2–3 | Smooth plaques do not assert a classical global symplectic manifold |
| Contact / Reeb / preserved leaf volume | ESTABLISHED on the full carrier | No transverse probability measure or quantum owner |
| Actual physical clock and repetitions | ESTABLISHED by (10)–(19) | Not an assigned roof and not an exact prime-log clock |
| Full primitive packet ledger | ESTABLISHED: two per prime plus two mixed | Target multiplicity and prime-only organization fail |
| Arithmetic-source / clock naturalness | OPEN | Fixed matrix assignment is a design; no geometric feedback into GPF |
| T3 analytic owner | NOT SUPPLIED | No post-stop trace, zeta or operator construction |
| Classical ASFS A0/A1/A2 | NOT APPLICABLE | No classical ASFS tuple is supplied |
| Formal Route coordinates | UNASSIGNED / NOT EVALUATED | No formal Route assessment is performed |
| Route B | NOT INVOKED | No changed authorization or readiness claim |

**Decision: advance the scoped geometric owner; stop target promotion;
fork only under a separately frozen identity.** The frozen first-gate stop
is already decisive in three ways: two rather than one primitive circle
per prime, the retained mixed pair, and (16). The asymptotic agreement
(18) does not undo those exact findings. No states, matrix factors, time
units or orientation conventions have been changed to repair them.

## 8. Proof provenance and disclosures

This is a self-contained matrix/Lie-algebra and quotient proof, with the
complete source classification explicitly imported only from
[266, §§3–4](../266-prime-source-return-rescreen/paper.md). The matrix
multiplications displayed in §5.2 are exact proof arithmetic; no numerical
trajectory, eigensolver, optimization, zero-generation or finite-census
experiment was run for this paper. Definitions are reproducible from the
[frozen card](candidate-card.md), and every new geometric and return
claim is proved above. The relevant local comparison files are linked in
§6; no new external theorem or unverified bibliographic claim is needed.

The draft was produced with AI assistance in a bounded author invocation.
An additional same-family read-only invocation checked only the quotient
argument and its non-locally-compact transverse boundary, reporting no gap;
it did not review the contact or periodic classification. It is not
external peer review and does not replace the proof.
Root owns separate verification and integration. This text itself does
not certify that a later independent review has occurred. ARS writing
guidance was used for claim/evidence separation and explicit limitations,
not as mathematical evidence or a publication-readiness certificate.

Data availability: all mathematical inputs used here are the linked local
definitions and the displayed exact formulas; no new empirical dataset
exists. Human-subject ethics is not applicable to this mathematical
construction. Contribution disclosure: the bounded author invocation
developed and wrote the proof; root froze the owner and retains integration
responsibility. Funding and competing-interest declarations for human
authors were not supplied and are not inferred. The record is local
Markdown research, not an externally submitted or peer-reviewed article.
