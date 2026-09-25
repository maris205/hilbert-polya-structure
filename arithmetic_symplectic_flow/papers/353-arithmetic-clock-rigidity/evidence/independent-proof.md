# Independent arithmetic-clock control and rigidity proof

**Audit:** `ANG-AUDIT-20260921-CRG01`; reference `ANG-20260921-RCF01`.
**New control:** `ANG-CONTROL-20260921-ACF01`.
**Finding:** The full control owns the same primitive selection with different
lengths. Logarithmic rigidity follows only with additional integer-order data.
**Standing:** Inherited model/shared history; internal `NOT_CALIBRATED`.

## 1. Input, access and scope

After explicit round4 release I personally read original353 card lines1–88
through EOF and measured SHA-256
`f970fce9b8d1b68607e82937f677fc51eb7c27609cd3d5ae331cadfa9785ee2a`.
The only new scientific input was that card; retained348/349 context was
available, but no dependency manuscript was reopened. I rederived the word
basins below after checking the literal C rule in this card, and proved the
changed geometric claims rather than transferring RCF01's clock conclusion.
The previously read ARS/stream instructions remain applicable.

I sent the parent the completed mathematical findings before writing this
sole assigned file. No root353 manuscript, scope/peer answer, other scientific
file, network source, numerical experiment, auxiliary agent or other write
was used. The card discloses additive-clock/order-rigidity expectations;
this review is not blind, external peer review or error-independent evidence.
No analytic operator, spectral target or formal Route evaluation is added.

## 2. Entire word basins and every reverse branch

For a word of length>=2, repeated C operations reduce it in length-1 steps
to the singleton of the gcd of ALL its entries. A singleton1 goes to empty.
A singleton n>=2 factors into its complete sorted atom list. If n=p^e,
the list reduces to singleton p; if n has distinct prime factors, its full
gcd is1 and the word subsequently reaches empty. Singleton p is fixed by C.
Thus every word reaches exactly one core, empty or singleton p, in finite
time. The p basin consists exactly of words with gcd p^e, e>=1. Empty and
all other words belong to the terminal basin. There are no other C cycles.

Let d(w) be the FIRST core entrance depth and
A(w)=sum_(0<=i<d(w)) h_*(head(C^i w)), with A=0 at a core.
Units and composite transients are included in this definition.
Unique factorization gives Omega(mn)=Omega(m)+Omega(n), so h_* is completely
additive, h_*(1)=0, and h_*(n)>0 for n>=2. At core p put
L_p^*=h_*(p)=log p+1>0. In (u,v,z), S_* is the translation
(w,u,v,z)->(Cw,u-h_*(head(w)),v,z).

The complete reverse WORD list is as follows. Empty has only singleton1.
For a nonempty target (d,tail), every pair(a,b,tail) with gcd(a,b)=d is a
predecessor. Additionally there is precisely one singleton predecessor n
when the ENTIRE target word is the sorted atom factorization of n; otherwise
there is none of this type. This includes the core singleton p itself.
Every listed reverse branch is defined on the whole target chart and is
(Q,X,Z)->(exp(h_*(a))Q,exp(-h_*(a))X,Z). These are all possibilities by C's
two cases. Every target has a predecessor, so S_* is onto; nonempty targets
have countably infinitely many predecessor words, not a chosen inverse.

## 3. Every-Borel IMAGE and the actual retained-lag groupoid

For each whole-chart branch, the real-coordinate Jacobian is
exp(h_*(a))exp(-h_*(a))=1. Equivalently it is a translation in u with v,z
fixed, preserving du dv dz=dq dxi dz. The inverse IMAGE law is therefore
mu(I(E))=mu(E) for EVERY Borel E in that target chart, with pointwise J=1,
including all null axes and transverse values. The source IMAGE cocycle is
zero on every actual arrow. It is not the physical-time parameter.
This branch law is not global invariance of the many-to-one S_*: a positive
finite-volume box in a nonempty target chart has infinitely many disjoint
equal-volume preimages in the countable-chart cover.

Write s_x=u_x-A(w_x) and likewise for y. Completing any common tail to its
core gives the following EXACT criterion for (y,k,x) in G_*:

```text
same core, v_y=v_x, z_y=z_x;
empty core: s_y=s_x and k=d(w_y)-d(w_x);
p core: s_y-s_x=j L_p^*, j in Z,
        k=d(w_y)-d(w_x)+j.                               (1)
```

Conversely, choose nonnegative post-core iterate counts with difference j
to realize every p-core arrow in(1); the terminal equality is realized at
the two entrance depths. This proves sufficiency as well as necessity.
The lag is unique for each related pair: ALL source isotropy is trivial.
In particular, a fixed word is not a fixed full state, since its u coordinate
moves by the nonzero L_p^*. Zero unit transport does not create an omitted
isotropy group: singleton1 and empty are distinct words.

For fixed word pair and integer lag, any nonempty arrow piece is the full
graph of a fixed u translation with v,z unchanged. In the inherited product
topology these pieces are open; source and range are homeomorphisms there.
Hence G_* is Hausdorff, locally compact, second countable and étale, with
exactly its actual arrows and no extra affine or free-word completion.

## 4. Full quotient and contact/Reeb ownership

Map each chart to its core component using (s,v,z), reducing s modulo L_p^*
only for a p core. By(1), its fibers are exactly the actual G_* orbits.
This map is continuous, surjective and OPEN on the complete coproduct, since
each chart map is a translation followed, where needed, by a covering map.
It therefore proves the quotient topology is precisely

```text
Q_*=R^3_terminal disjoint-union coproduct_p
                     (R/(L_p^*)Z) x R^2.                 (2)
```

These coordinate transitions give its full Hausdorff smooth structure.
All source arrows preserve beta because they only translate u. Directly,
d beta=alpha wedge eta, beta wedge d beta=du wedge dv wedge dz,
beta(R)=1 and i_R d beta=0, where R=partial_u+v partial_v-z partial_z.
Thus beta descends as a contact form everywhere, including vz=-1, and the
frozen R is its normalized Reeb field. The quotient volume is the descended
contact volume, not the pushforward of infinitely many overlapping charts.

The complete flow in every component is
Phi^t(s,v,z)=(s+t,exp(t)v,exp(-t)z). It commutes with every source branch
and with(1); its inverse has domain the ENTIRE Q_* for every real t.
Its Jacobian is1, so it preserves the descended volume for every Borel set.
No geometric state, incoming source basin or null stratum was deleted.

## 5. Entire physical orbit and primitive ledger

In the terminal component the real s coordinate forbids a nonzero return.
In a p component a return requires t in L_p^* Z. If t!=0, the two transverse
equations force v=z=0. Consequently the full physical return groups are

```text
H_x=L_p^* Z on each p circle with v=z=0;
H_x={0} at every other point of Q_*.                       (3)
```

Each zero-transverse circle is ONE primitive flow orbit, of least positive
time L_p^*, with all kth repetitions kL_p^*. Different core components never
merge. Every source predecessor in its full basin maps by s=u-A(w); no
nonzero transverse state can enter a periodic orbit in finite physical time.
Thus there is exactly one primitive per atom and no additional primitive.

For completeness, all terminal flow orbits are classified by
(V,Z)=(exp(-s)v,exp(s)z). In a circular component the same pair is defined
up to (V,Z)->(exp(-L_p^*)V,exp(L_p^*)Z); its orbit under this integer action
classifies the full physical orbit. Its origin class is the closed orbit;
all other physical orbits are free. Periodic phase is s modulo L_p^*.
Source isotropy remains trivial despite these physical return groups; the
zero source IMAGE character does not replace physical time.

## 6. Reference, scale and zero-holonomy controls

The same calculation with h(n)=log n gives RCF01's lengths L_p=log p,
its same prime selection and trivial full-state source isotropy. It is the
unchanged reference, not an ACF01 clock retrospectively assigned to it.
No label-preserving common positive time scale identifies both ledgers:
L_p^*=c log p would require c-1=1/log p for every p, already contradicted
by p=2 and p=3. This does NOT prove unrestricted global nonconjugacy.

For full UNIT-HOLONOMY, all source geometric shifts are zero. Every core
quotient component then has REAL u and is R^3. In a p basin, for related
points with identical geometric coordinates every integer lag occurs:
the source isotropy is Z, with its entire zero-IMAGE kernel retained.
The terminal basin still has trivial source isotropy. The same physical
Phi translates real u, so ALL physical return groups are zero and there
are no primitive physical circles. Source lag does not supply their time.
Every reverse branch is still whole-chart identity in geometric coordinates;
the word multiplicities and transient basins are unchanged.

## 7. Integer-order rigidity and its exact assumption boundary

Let h satisfy the frozen arithmetic hypotheses. Since h(1)=0 and order is
nondecreasing, h(n)>=0. For n>=2, k>=1 set
m_k=floor(k log n/log2), so 2^(m_k)<=n^k<2^(m_k+1). Additivity and order give

```text
m_k h(2) <= k h(n) <= (m_k+1)h(2).
```

Divide by k and let k grow. Since m_k/k tends to log n/log2,
h(n)=c log n for every positive integer n, c=h(2)/log2>=0. Conversely every
such c satisfies the hypotheses. This includes c=0; no continuity or
extension to all positive reals is used. The normalization h(2)=log2 would
select c=1, but it is an EXTRA assumption, not a contact/volume consequence.

The fixed h_* passes additivity but FAILS ordinary integer monotonicity:
8<9, yet h_*(8)-h_*(9)=1-log(9/8)>0, since log(9/8)<1/8<1.
It also fails the common-scale test above, while satisfying the full contact,
volume, completeness and primitive-selection conclusions. Thus these
geometric/source ownership conditions do not force the order hypothesis.
Nor does strict-contact transport itself impose additivity: each branch
calculation uses only a constant translation, with no equation relating
h(mn), h(m) and h(n). The entire quotient/ledger argument likewise needs
only finite entrance sums A(w) and positive core shifts h(p), not additivity.
A separate rule must impose that relation.

The strongest positive statement is the conditional rigidity theorem with
all hypotheses visible. Its limitation is decisive: contact Reeb normalization
fixes time for a GIVEN global contact owner, but does not select its integer
transport or period list among these explicitly different owners. ACF01 is
an adverse, fully owned arithmetic control, not a replacement main candidate
or a proof that every stronger naturalness programme is impossible.
RCF01 remains unchanged; strong naturalness is OPEN and formal Route B absent.

EOF — full ACF01 owner/ledger and conditional arithmetic rigidity audited.
