# Paired coprime stacks: an owned clock with a wrong primitive return time

**Paper:** 377-paired-coprime-stack. **Candidate:** ANG-20260922-PCS01; 2026-09-22.
**Batch:** HARD-NONLOCAL-20260922-F, round 3/5.
**Status:** OWNED STACK CLOCK; WRONG PRIMITIVE TIME — STOP / FORK.
Owner-level T0 and chart-clock ownership established; target T2 fails.
Strong naturalness OPEN; T3 NOT AUDITED; classical A0/A1/A2 NOT APPLICABLE;
formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

The full finite-initial-stack path source has its frozen probability,
every-point inverse-chart density and signed real cocycle. Its complete
return classification is by primitive directed closed walks, with all legal
incoming histories and height phases retained. The prescribed two-edge walk
through stack (2) has least physical time log(4-2 log 2), strictly between
log 2 and log 3. It therefore fails the fixed prime-time target. The three
controls have their own laws and clocks; none repairs the main object.

## 1. Identity, definitions and claim boundary

The [frozen card](candidate-card.md) specifies rho(n)=1/[n(n-1)], n>=2,
the empty stack e, and all finite ordered pairwise-coprime stacks S.
A(s) consists of integers coprime to EVERY entry of s. Edges push n from s
to sn, or pop the actual top n from sn to s. The label n is retained.
X contains ALL infinite legal state-and-edge paths, from EVERY s in S;
T deletes the first edge and its starting state. Cylinders fix an initial
state and a finite edge history; they generate the stated Borel structure.

The arithmetic lineage is the deformation from divisor witnesses to hard
admission against all unclosed entries and matched nesting. The carrier is
still a countable-state Markov graph. No nonconjugacy or novelty is claimed.
Finite initial stacks, unbounded later depths, never-returning paths and all
null paths belong to this owner. Infinite initial stacks are outside its freeze.
The clock is an IMAGE cocycle, not a positive classical roof; its extension
and physical action below are defined on the entire orbit SET.
There is no symplectic, Hamiltonian, contact, operator or trace identification.

## 2. Entire source and its own probability

Write a(s)=sum_(n in A(s)) rho(n), so Z_e=1 and Z_s=1+a(s) for s!=e.
The telescoping identity sum_(n>=2) rho(n)=1 gives a(s)<=1.
For nonempty s, let M be the product of its entries: every kM+1, k>=1,
belongs to A(s). Hence 0<a(s)<1; strict upper inequality follows because
the top entry is forbidden. All graph states have outgoing and incoming edges.
Every state can reach every other by popping to e and rebuilding the target.

At each state use exactly P_s(push n)=rho(n)/Z_s and, when nonempty,
P_s(pop)=1/Z_s. These positive edge probabilities sum to one.
Let b(s)=2^(-|s|-1)product_(entries n) rho(n), B=sum_s b(s), eta(s)=b(s)/B.
For each height h, its b-sum is bounded by 2^(-h-1), using the larger
unrestricted set of all h-tuples. Thus 1/2<=B<=1, with eta(s)>0 for all s.
Consistent cylinder probabilities construct the conditional path laws and
their probability mixture mu=sum_s eta(s)P_s^path:
\[
 \mu([f_0\cdots f_{m-1}])
   =\eta(s_0)\prod_{i=0}^{m-1}P_{s_i}(f_i).                 \tag{1}
\]
Every nonempty cylinder is positive, so mu has full topological support.
Every infinite path has infinitely many pushes: finitely many pushes would
leave only finitely many possible pops from its finite initial height.
Every push has probability at most 1/2. Successively longer cylinders around
any path therefore have masses tending to zero. All singletons, including
periodic paths, are null; on this standard Borel path space mu is atomless.

This probability is not stationary. Only singleton stacks can enter e, and
eta((n))=eta(e)rho(n)/2. Consequently
\[
 \mu(T^{-1}X_e)=\frac{\eta(e)}2\sum_{n\ge2}\frac{\rho(n)}{Z_{(n)}}
 \le\frac{\eta(e)}2<\mu(X_e).                             \tag{2}
\]
No invariant probability or recurrence claim is substituted for (1).

## 3. Exhaustive inverse atlas and every-Borel IMAGE

At a target t!=e there is exactly one incoming push from its parent.
At EVERY target t there is an incoming pop from tn for each n in A(t).
These are all predecessors; at e only the latter type occurs.
For each actual f:s->t, prefix insertion I_f:X_t->[f] is a Borel bijection
with inverse T restricted to [f]. It is defined on ALL of X_t.
Conditional factorization of (1), extended from cylinders by uniqueness of
finite measures, proves for every Borel E subset X_t
\[
 \mu(I_fE)=J_f\mu(E),\qquad J_f=\frac{\eta(s)P_s(f)}{\eta(t)}.
                                                               \tag{3}
\]
Because eta(sn)/eta(s)=rho(n)/2, the frozen version is explicitly
\[
 J_{\mathrm{push}\ n:s\to sn}=\frac2{Z_s},\qquad
 J_{\mathrm{pop}\ n:sn\to s}=\frac{\rho(n)}{2Z_{sn}}.       \tag{4}
\]
It is positive and finite at every tail, not merely almost everywhere.
The same constants are exact image/source cylinder ratios at EVERY length.
All Borel-null tails remain in each chart. Countability, positivity and the
exhaustive predecessor list give mu(E)=0 iff mu(T^(-1)E)=0.

Define kappa(x)=-log J_(first edge)(Tx). Push values are log(Z_s/2),
strictly negative in MAIN; pop values are log(2Z_sn/rho(n)), positive.
In particular monotone step-time and a positive suspension roof are absent.

## 4. Full history cocycle and all three kernels

For a finite path u:s->r let |u| be its edge length, p(u) its P-product,
N(u)=product_(pops of n in u) n(n-1), and Z(u)=product_(edge departures) Z_s.
Empty products are one. Put
\[
 K(u)=2^{|s|}N(u)Z(u),\qquad
 D(u)=\frac{\eta(s)p(u)}{\eta(r)}
     =\frac{2^{|r|-|s|}}{N(u)Z(u)}=\frac{2^{|r|}}{K(u)}.   \tag{5}
\]
The middle identity follows either by multiplying (4), or by cancelling
the initial-stack weights in (1). Prefix insertion has EVERY-Borel
IMAGE D(u); prefix replacement I_u I_v^{-1}, for u,v ending at the same r,
has IMAGE D(u)/D(v), on every Borel subset of its full domain [v].

Take exactly G={(z,m-n,y):T^m z=T^n y}, with source y, range z, lag ell(z,k,y)=k,
and identify equal triples only. For u=z|m and v=y|n the clock is
\[
 c(z,m-n,y)=A_m(z)-A_n(y)=\log\frac{K(u)}{K(v)},\qquad
 A_m(z)=\sum_{i<m}\kappa(T^iz).                           \tag{6}
\]
The actual prefix-replacement IMAGE is exp(-c).
Two presentations of the same triple differ by an equal number of appended
common-tail edges, whose kappa sums cancel. Thus c descends everywhere.
Aligning common tails in a product proves addition of c; inversion negates it.
This proves the full finite-history law, not only a one-step identity.

Here are exact exhaustive kernel criteria, with no unproved independence
assumption about the real numbers Z_s:
\[
 \ker c=\{(z,m-n,y):T^mz=T^ny,\ K(z|m)=K(y|n)\},
\]
\[
 \ker\ell=\{(z,0,y):T^Nz=T^Ny\text{ for some }N\ge0\},
\]
\[
 \ker c\cap\ker\ell
 =\{(z,0,y):T^Nz=T^Ny,\ K(z|N)=K(y|N)\text{ for some }N\}.
                                                               \tag{7}
\]
These tests include all incoming weights and hold in every presentation.
Prepending the root excursions through 2 and 3 in opposite orders to the
same tail gives distinct length-four prefixes with equal K, hence nonunit
intersection arrows. No algebraic-independence or finite-census claim is made.

## 5. All isotropy, packets, incoming histories and phases

A nonzero source isotropy arrow is precisely an equality T^m x=T^n x
with m!=n, hence an eventually periodic FULL edge-and-state path.
Let q be its tail's least positive edge period. Its entire isotropy is qZ;
otherwise it is {0}. The periodic core is a primitive directed closed walk
w of length q, modulo cyclic rotation. It need not be a simple cycle.
Conversely every such walk supplies exactly one periodic tail-equivalence
class. Repeated words are not primitive, and different cyclic primitive
state-and-edge words cannot become equal by removing finite prefixes.

Along a closed walk, pushes and pops balance for each integer label.
The eta factors telescope, and
\[
 L(w)=-\log p(w)=
 \log\left(\prod_{f\in w}Z_{\operatorname{start}(f)}
             \prod_{\mathrm{pops}\ n\in w}n(n-1)\right)>0. \tag{8}
\]
A nonempty closed walk contains a push with probability <=1/2, so its
P-product is strictly below one. Heights change by one, so q is even.
For ANY incoming eventually periodic path x, the entire clock image is
H_x=L(w)Z, with c(x,kq,x)=kL(w); finite transient contributions cancel.
For every noneventually-periodic x, H_x={0}. Thus the clock kernel,
lag kernel and their intersection all have trivial isotropy.

Retain all X times R and arrows (y,h)->(z,h+c(z,k,y)). Their isotropy
is the source isotropy with c=0, therefore trivial at EVERY (x,h).
Height translation defines a complete R-action on the orbit SET;
no Hausdorff, smooth, contact or measure-preserving quotient is asserted.
Its return subgroup at [(x,h)] is exactly H_x, not an arbitrary group
generated by all closed walks elsewhere in the connected state graph.

Explicitly the full source orbit is
O_x={u T^n x:n>=0, u any finite legal path ending at the start of T^n x}.
It includes every allowable initial state and all legal prefixes, not just e.
Fix a reference a in this orbit. For any y in O_a choose g:y->a.
The phase of (y,h) is h+c(g) modulo H_a; another choice changes it by H_a.
This gives a bijection from the quotient over O_a to R/H_a. Indeed equal
phases differ by an isotropy correction, which supplies an actual arrow.
Thus a primitive w gives ONE physical packet, all phases R/L(w)Z, least
positive time L(w), and all repeats jL(w), j>=1. Its q source phases are
not q packets. Aperiodic source classes instead have phase line R and no
nonzero time return. These statements cover every path and every height.

## 6. The precommitted MAIN packet

Let a repeat e->(2)->e and b=Ta. The full states differ, so the least source
period is exactly 2. At (2), allowed pushes are precisely odd n>=3.
By nonnegative termwise integration,
\[
 a((2))=\sum_{k\ge1}\frac1{(2k)(2k+1)}
 =\int_0^1\frac{x}{1+x}\,dx=1-\log2.                     \tag{9}
\]
The integrand is strictly between 0 and 1/2 on (0,1), so 0<a((2))<1/2.
The two transition probabilities are 1/2 and 1/[1+a((2))]. Equations
(8)-(9), together with the entire source isotropy 2Z, give
\[
 H_a=H_b=L_2\mathbb Z,\qquad
 L_2=\log(2[1+a((2))])=\log(4-2\log2),\quad
 \log2<L_2<\log3.                                       \tag{10}
\]
There is no prime, or integer, strictly between 2 and 3. This is a wrong
PRIMITIVE time in the fixed normalization, not merely a wrong repetition.
The phases of (a,h) and (b,h) referred to a are respectively h and
h-log2 modulo L_2, since c(a,1,b)=kappa(a)=-log2.
For every y=uT^n a, m=|u|, its phase is h+A_n(a)-A_m(y) modulo L_2.
All such incoming paths and both source phases remain in this one packet.

## 7. Three separate full-source controls

Each control uses ITS OWN graph, Z,P,b,B,eta and cylinder formula (1).
The normalization bound, full support, atomlessness and nonstationarity
proofs in Section 2 apply independently: each legal push costs at most 1/2,
all paths require infinitely many pushes, and singleton-stack mass ratios
remain rho(n)/2. Formulas (3)-(8) follow again from these own probabilities.
Incoming charts are exactly each graph's parent push and legal child pops.
The complete kernel criteria, eventual-periodic isotropy, full incoming
orbits, extension isotropy and phase classification therefore apply with
that control's K, not with MAIN's transition probabilities.

**ARITHMETIC-OFF.** All finite integer stacks are allowed. Here B=1,
Z_e=1 and every nonempty Z_s=2. Let d(u) count nonempty edge departures.
Its explicit K(u)=2^(|start(u)|+d(u))N(u), so (7) is an integer-product
equality, with the stated lag condition where required. J_push is 2 at e
and 1 elsewhere; J_pop=rho(n)/4. Every primitive closed walk has
L=log(2^(d(w))N(w)). The full e->(2)->e packet has q=2, H=log4 Z,
least time log4, trivial extension isotropy and all phases R/log4 Z.
Its two source phases have offsets 0 and -log2; every legal incoming prefix
uses the Section 5 phase formula with this control's A_m.

**TOP-ONLY.** All finite stacks with adjacent entries coprime are allowed.
At nonempty s with top n, Z_s=1+sum_(gcd(j,n)=1)rho(j); Z_e=1.
Again 1/2<=B<=1, but B and eta are recomputed on this larger state set.
Every top-coprime child, including those violating distant coprimality,
is an actual predecessor-pop chart; none is discarded. K and L are exactly
(5) and (8) using these top-dependent Z_s. The e->(2)->e packet independently
has q=2 and H=log(4-2 log2) Z by the same odd-integer integral (9).
Its least time is strictly between log2 and log3; both phase offsets and
ALL top-only incoming paths are handled with its own A_m, not MAIN's.

**DEPTH-ONE.** States are e and (n). The own constants are B=3/4,
eta(e)=2/3, eta((n))=rho(n)/3, Z_e=Z_(n)=1.
P_e(push n)=rho(n), P_(n)(pop)=1, J_push=2, J_pop=rho(n)/2.
All predecessors of e are the singleton pops; each (n) has only its parent
push. Here K(u)=2^(|start(u)|)N(u), again giving explicit integer kernels.
Every primitive closed walk is a primitive finite necklace (n_1,...,n_r)
of excursions e->(n_i)->e, with q=2r and
L=sum_i log[n_i(n_i-1)]. This exhausts the graph, not only a chosen section.
The full e->(2)->e packet has H=log2 Z and least time log2.
Separately e->(3)->e has H=log6 Z and least time log6: a wrong primitive.
Both have q=2, source offsets 0 and -log2, all legal incoming excursions,
trivial extension isotropy and the entire corresponding phase circles.
The prime-looking first control packet does not repair the second or MAIN.

## 8. Gates, limitations and reproducibility

T0 full-source and measure ownership and the all-point signed chart clock
are established. T1 clock ownership is not strong arithmetic naturalness,
which remains OPEN. T2 target promotion stops by (10); the entire
closed-walk formula is established without claiming a prime packet law.
T3 is NOT AUDITED. No rescaling, endpoint quotient, root-only selection,
infinite-initial-stack completion, geometric lift or Route evaluation follows.
Portfolio decision: STOP / FORK for this frozen target and law.

All derivations use the [81-line frozen card](candidate-card.md) and the
repository template; no raw/peer answer, outside source or numerical output
was read. This author supplied the definition scout and authored 370/372;
shared history is disclosed, not blind independence. ARS supplied writing
and disclosure discipline; root owns subsequent review/integration.
Internal model scrutiny is NOT_CALIBRATED, not external peer review or
novelty certification. Data availability: exact definitions and proofs here;
no dataset or scientific computation. Human subjects: not applicable.
AI contribution: definition, derivation and drafting; human author/CRediT attribution, funding and conflicts were not supplied.

EOF — complete finite-initial-stack owner; full signed clock and scoped stop.
