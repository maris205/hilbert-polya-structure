# Negative proof package: set/code desk

Author: /root/round211_set_code_scout, 2026-09-08 UTC. These are deductive
negative adapters, not admitted claims or independent review.

## Claims, status and dependencies

| Claim | Status | Value boundary |
|---|---|---|
| DHC eventual period at most two on every finite metric space | PROVABLE AS STATED | Optimum-distance increase followed by symmetric-relation polarity; exact old MFS family. |
| MWD eventual period at most two for every $q,n$ | PROVABLE AS STATED | Minimum-weight ranks on each parity, then increasing spans; no sharp or separately valued axis. |
| CDU all iterates and exact statewise absorption | PROVABLE AS STATED | Disjoint subset-convolution powers and matching capacity; no independent axis. |
| CCC conjugacy, recurrence, rank bound, all inverse fibres and maximizers | PROVABLE AS STATED | Dual rank identity plus arbitrary closure-difference facts; includes current CBF exactly. |
| Any row as a fresh two-axis paper | NOT CURRENTLY JUSTIFIED | Literal-family collisions or consumed time value without a separate theorem. |

## 1. DHC: threshold polarity consumes the period theorem

Let $(X,d)$ be a nonempty finite metric space and use all nonempty subsets.
Write
$$r(C)=\max_{x\in X}\min_{c\in C}d(x,c),\qquad
D(C)=\{x:\min_{c\in C}d(x,c)=r(C)\}.$$
Every $c\in C$ is at distance at least $r(C)$ from every $y\in D(C)$,
by symmetry. Thus $r(D(C))\ge r(C)$. The radii eventually stabilize
because they belong to the finite set of pairwise distances.

For a fixed radius $r$, put
$$P_r(A)=\{x\in X:(\forall a\in A)\ d(x,a)\ge r\}.$$
This is antitone, and symmetry gives $A\subseteq P_r^2(A)$. Applying
antitonicity gives $P_r^3(A)\subseteq P_r(A)$; applying the inclusion
to $P_r(A)$ gives the reverse. Hence $P_r^3=P_r$.

Once the orbit radii stabilize at $r$, the literal update is exactly
$P_r$, since no point has minimum distance greater than the optimum.
Thus the eventual period is one or two. In fact, if
$r(C)=r(D(C))=r$, then $C\subseteq D^2(C)$, so
$r(D^2(C))\le r(C)$. Radius nondecrease gives equality, and the three
successive threshold maps give $D^3(C)=D(C)$. This is stabilization
from the first plateau, not a Hamming-specific mechanism.

For the cube, the full cube is fixed, and every proper nonempty $C$
has $r(C)>0$, hence $D(C)\cap C=\varnothing$. There is no other fixed
state. At $n=0$ the carrier has one fixed state. No sharp cube clock,
evaluated all-target inverse or new basin census is claimed.

Old GG08/MFS explicitly takes nonempty subsets of a finite graph metric
to all points maximizing distance to the subset. The fixed graph can be
the Hamming cube, so this is its exact literal slice, even though the old
pilot used paths and cycles. P106's symmetric-polarity proof and MHT's
optimum-rank descent further deduct the mechanism.

## 2. MWD: minimum-word selection supplies only generic stabilization

Let $V=\mathbb F_q^n$, with $m(C)$ and $T(C)$ as in INTAKE.md.
The standard dot product is nondegenerate, including characteristic two,
so $(U^\perp)^\perp=U$. Since $m(T(C))\subseteq m(C)^\perp$,
$$m(C)\subseteq T^2(C). \tag{1}$$
For $n>0$, zero and $V$ form a two-cycle: the coordinate weight-one
vectors span $m(V)=V$. Any orbit reaching zero is thus handled.

For an orbit $C_t$ avoiding zero, let $d_t\in\{1,\ldots,n\}$ be its
minimum weight. Equation (1) gives $d_{t+2}\le d_t$, so each parity's
minimum weights eventually stabilize. After this, every minimum-weight
word of $C_t$ is in $C_{t+2}$ and still has minimum weight, giving
$$m(C_t)\subseteq m(C_{t+2}). \tag{2}$$
The parity subsequences of these finite-dimensional subspaces stabilize.
Their perpendiculars then give $C_{t+3}=C_{t+1}$ eventually. Every orbit
therefore has period one or two. At $n=0$ there is a single fixed subspace,
not a two-element cycle.

This is minimum-weight selection plus symmetric annihilation, not P165's
support-budget doubling. But its only obtained time conclusion is generic
rank-then-inclusion stabilization, already excluded in the MHT mechanism
corridor. No sharp clock or non-generic recurrent classification is proved.

The inverse requirement $m(C)=Y^\perp$ merely restates the target
condition. No evaluated all-$q,n$ fibre, maximum or equality-target
theorem is supplied. Ding--Key directly study the minimum-word span;
their Reed--Muller results are not evidence for this feedback's novelty.

## 3. CDU: a matching clock from associative powers

For $k\ge1$, let $U_k(\mathcal H)$ be all unions of $k$ pairwise disjoint
members of $\mathcal H$, with $U_1(\mathcal H)=\mathcal H$.
Two disjoint unions of $k$ disjoint original edges together give $2k$
mutually disjoint original edges. Conversely, any $2k$ such edges can be
partitioned into two groups of $k$. Therefore
$$U_2(U_k(\mathcal H))=U_{2k}(\mathcal H),\qquad
T^t(\mathcal H)=U_{2^t}(\mathcal H). \tag{3}$$
Let $\nu(\mathcal H)$ be the maximum matching size. For nonempty
$\mathcal H$, equation (3) is nonempty exactly when
$2^t\le\nu(\mathcal H)$. Since its edges are nonempty,
$\nu(\mathcal H)\le n$, and all orbits reach the empty family. Hence
$$\tau(\mathcal H)=\lfloor\log_2\nu(\mathcal H)\rfloor+1
\quad(\mathcal H\ne\varnothing),\qquad \tau(\varnothing)=0.$$
All singleton edges attain global height $\lfloor\log_2 n\rfloor+1$
for $n\ge1$. At $n=0$ the sole empty family has height zero.

Boolean indicator arithmetic identifies the update with subset
convolution. Its primary source explicitly defines disjoint-union
convolution and its associativity. P97's $2^t$-fold sumset identity uses
the same power-unfolding mechanism; no conjugacy to its prime-group
carrier is asserted. The matching-capacity cutoff follows directly
from (3). No independently valued inverse-root theorem is obtained.

## 4. CCC: exact CBF family hit and a complete closure adapter

### Assumptions and literal conjugacy

Fix a finite labelled matroid $M$ on $E$. For $S\subseteq E$, an element
$e\in S$ is a coloop of $M|S$ iff
$r_M(S)-r_M(S\setminus\{e\})=1$. Put $R=E\setminus S$.
Using the dual rank identity
$$r_{M^*}(A)=|A|-r_M(E)+r_M(E\setminus A),$$
the formula follows directly from complementary bases: maximizing the
intersection of $A$ with a dual basis is $|A|$ minus the minimum
intersection with a primal basis, which is $r_M(E)-r_M(E\setminus A)$
by extending a basis of $E\setminus A$ to one of $E$.
Applying this identity,
we have, for $e\notin R$,
$$r_{M^*}(R\cup\{e\})-r_{M^*}(R)
=1+r_M(S\setminus\{e\})-r_M(S).$$
Thus
$$\operatorname{coloops}(M|S)
=\operatorname{cl}_{M^*}(R)\setminus R.$$
If $J(A)=E\setminus A$, then
$$J\circ F_M\circ J(R)=\delta(R),\qquad
\delta(R)=\operatorname{cl}_{M^*}(R)\setminus R. \tag{4}$$

For $M=M(K_n)$, the restriction's coloops are exactly bridges of the
spanning edge-subgraph, so $F_M$ is **literally current CBF**. This is a
forbidden family enlargement, not a new candidate. The following negative
adapter does not reopen CBF or alter its accepted/rejected evidence.

### Generic closure time and recurrent states

Let $c:2^E\to2^E$ be any extensive, monotone, idempotent closure and
$\delta(R)=c(R)\setminus R$. Since $\delta(R)\subseteq c(R)$,
$$c(\delta(R))\subseteq c(R),\qquad
\delta^2(R)=c(\delta(R))\setminus(c(R)\setminus R)\subseteq R. \tag{5}$$
If $c(\delta(R))=c(R)$, then
$\delta^2(R)=c(R)\setminus(c(R)\setminus R)=R$.
Conversely, if $\delta^2(R)=R$, the nested closures in that periodic
orbit must coincide. Since a finite descending chain of closed sets
eventually stops, every orbit ends in period one or two.

Recurrent states are exactly $R$ for which $R$ and $c(R)\setminus R$
both generate $c(R)$: ordered complementary generating pairs inside one
closed set. Since $R$ and $\delta(R)$ are disjoint, a fixed state must
be empty; it is fixed exactly when $c(\varnothing)=\varnothing$.

For matroid closure, strict inclusion between flats strictly decreases
rank. Hence every nonrecurrent step lowers the closure rank, and
$$\tau(R)=\min\{t:r(c(R_t))=r(c(R_{t+1}))\}\le r(c(R_0)). \tag{6}$$
There is no sharp attainment claim for any specified field/rank/ground-size
class. This is a generic ranked-closure bound.

### All inverse fibres and all maximizing targets

Write $\mathcal L=\{A:c(A)=A\}$ and $L=c(\varnothing)$.
There is an exact bijection
$$\delta^{-1}(Y)\longleftrightarrow
\{A\in\mathcal L:Y\subseteq A,\ c(A\setminus Y)=A\},\qquad
R=A\setminus Y. \tag{7}$$
Indeed, $\delta(R)=Y$ implies disjointness of $R,Y$ and
$A=c(R)=R\cup Y$, giving the indicated closed set and unique source.
Conversely every indicated $A$ has
$\delta(A\setminus Y)=A\setminus(A\setminus Y)=Y$.
Distinct such closed sets yield distinct sources because all contain $Y$.

Thus $|\delta^{-1}(Y)|\le|\mathcal L|$. If $Y\subseteq L$, every closed
$A$ contains $Y$, and
$$A\subseteq(A\setminus Y)\cup L\subseteq c(A\setminus Y)\subseteq A.$$
Every closed set then contributes, giving equality. If
$Y\not\subseteq L$, the closed set $L$ cannot contribute, making the
inequality strict. The exact maximum is therefore $|\mathcal L|$,
attained **exactly** at all subsets of $L$.

For dual-matroid closure, $L$ is the loop set of $M^*$, namely the
global coloop set of $M$. Under (4), the CCC maximizing targets are
$E\setminus Y$ for $Y\subseteq L$. At $E=\varnothing$ the formulas give
one state, one closed set, one fibre and zero entrance time.

The complete inverse/extremal package holds for *every finite closure*.
It is a generic closed-generator count, not a separate matroid-specific
inverse contribution.

## Corrections and open risks

1. DHC's code-specific framing was defeated by the actual old GG08/MFS
   literal. This late collision is retained, not counted as a fresh pilot.
2. CCC's broader carrier was defeated by exact specialization to current
   CBF. It cannot refill that mechanism under a geometry label.
3. MWD/CDU have no independently proved second axis; the generic time
   deductions do not remove this value defect.
4. These are desk proofs with **zero scientific execution**. No exhaustive
   verification, independent acceptance or novelty certification is implied.
   Source scopes are in SOURCE_AND_COLLISION.md. HOLD_EXTERNAL remains.
