# Lane40 author proof and exact subtraction

Author: `/root/twenty_seventh_finite_scout`. Root later independently
suggested the same LLG rule and clock after the scout's derivation, then
confirmed the factor-value boundary. This document is author work, not an
independent manuscript review. No experiment is a proof dependency.

## Claims, assumptions and status

The carriers and simultaneous updates are exactly those in INTAKE.md.
All sets and trees are finite; labels are retained under LLG. Put $0^0=1$.
Empty products are one. A recurrent point means a point on a finite cycle.

**PROVABLE AS STATED:** LLG carrier closure; exact iterates; unique fixed/
recurrent star and its pointwise entrance clock; complete target-resolved
predecessors and counts; the sharp maximum and its unique target. OMP
closure, absorption at the minimum, and exact direct-source identity.

**NOT JUSTIFIED:** a new two-axis contribution after source/history
subtraction, global ownership clearance, or admission of either literal.

Dependencies: LLG's nonleaf factor is exactly P114 peeling; the stated
all-target law uses choices of input internal vertices and independent
local functions hitting specified recipients. The sharp maximum uses a
reversible compression into height-at-most-two trees. OMP uses only finite
posets, connected subsets of a tree and coordinate intersections.

## 1. LLG closure, the exact old factor, and every iterate

For an initial tree $X$, write $p_X$ for its parent map, $d_X(v)$ for root
distance, $h_X(v)$ for the height of the fringe subtree at $v$, and $H(X)$
for its height. The root-only tree has height zero. Let $S_N$ be the rooted
star on the full label set, including the root-only case.

Every changed edge points to a proper old ancestor. Thus parent orbits in
the new graph strictly decrease old depth until reaching the root. This
proves carrier closure without a sequential interpretation of the updates.
An old nonroot leaf cannot acquire a child: a newly attached child would
require it to have been an old grandparent, which a leaf is not. Old leaves
therefore remain leaves.

Let $P$ be the old parallel map that deletes all nonroot leaves, retaining
the root and the induced parent edges, on rooted trees supported on subsets
of the ambient labels. Put $C(X)=P(X)$; this is a projection to a variable-
support carrier, not a bijection on $\mathcal T_N$. We claim

$$C(F(X))=P(C(X)).\tag{1}$$

For a nonroot vertex $u$, if it has an old nonleaf child, that child keeps
its parent, so $u$ is still a nonleaf after $F$. If all its old children are
leaves, they all move to $p_X(u)$, and $u$ cannot gain a child from an old
grandchild. Thus $u$ becomes a leaf. An old leaf remains a leaf by the
previous paragraph. Consequently the nonroot vertices retained by
$C(F(X))$ are exactly those surviving two rounds of $P$. Every such
retained vertex was an old nonleaf and kept its edge. Both sides of (1)
also retain the root. This proves equality of the labelled parent maps.

Induction now gives

$$C(F^t(X))=P^{t+1}(X).\tag{2}$$

The original P114 proof in `papers/114-rooted-forest-leaf-peeling/main.tex`,
Section 2, proves directly by fringe-height induction that a nonroot vertex
is deleted in round $h_X(v)+1$, and that the root-only entrance time is the
initial tree height. Restricting its forest carrier to the fixed root $0$
and relabelling the ambient ground set changes neither proof nor map.
Moreover

$$C^{-1}(\{0\})=\{S_N\},\qquad
H(C(X))=\max(0,H(X)-1).$$

It follows from (1)--(2), with the minimum entrance time on both sides,
that

$$\tau_F(X)=\max(0,H(X)-1).\tag{3}$$

The star is fixed by its literal update. Equation (3) sends every state to
it, so there are no other fixed or recurrent states. This transfers the
**whole** clock, not merely an upper bound. For $N\ge1$, its maximum is
$N-1$ and equality requires a rooted path through all labels; the $N!$
orders of the nonroot labels give all such paths. At $N=0$ the maximum is
zero and there is one state. These are height/path consequences, not new
contribution claims.

For completeness the entire labelled parent map, not just its clock, has
the following formula for every $t\ge0$ and $v\ne0$:

$$p_{F^t(X)}(v)=p_X^{\,\min\{d_X(v),\,1+\max(0,t-h_X(v))\}}(v),
\qquad p_{F^t(X)}(0)=0.\tag{4}$$

Indeed (2) and P114's deletion-round statement show that $v$ is a current
leaf exactly when $h_X(v)\le t$. Before that time it has never moved.
Assume (4) at time $t$. If $v$ is still a nonleaf, its exponent stays one.
If its current parent is the root, it remains so. Otherwise put
$j=\max(0,t-h_X(v))$ for a current leaf. Its current parent is
$a=p_X^{j+1}(v)$. The original fringe height satisfies
$h_X(a)\ge h_X(v)+j+1\ge t+1$ (with $j=t-h_X(v)$ in this leaf case).
Thus $a$ is still a nonleaf and has never moved; its current parent is
$p_X(a)$. The leaf therefore moves exactly one more edge up its original
ancestor chain, as required at time $t+1$. This proves (4) by induction.

Equations (1)--(3) provide the decisive value subtraction. Extra labels
moving along the original ancestor paths do not supply a second temporal
mechanism after this singleton-terminal-fibre factor has been deducted.

## 2. Every LLG predecessor of an arbitrary labelled target

Fix $Y\in\mathcal T_N$. Let $L_Y$ be its nonroot leaves and
$I_Y=\{1,\ldots,N\}\setminus L_Y$ its nonroot internal vertices. For each
choice $B\subseteq L_Y$, put

$$S=I_Y\cup B,\qquad L=L_Y\setminus B.$$

These will be exactly the nonroot internal vertices and leaves of a
predecessor $X$. For every target vertex $w$, write $\operatorname{Ch}_Y(w)$
for its children and define

$$A_w=S\cap\operatorname{Ch}_Y(w),\qquad
L_w=L\cap\operatorname{Ch}_Y(w),$$
$$a_w=|A_w|,\quad \ell_w=|L_w|,\quad
b_w=|\{u\in A_w:S\cap\operatorname{Ch}_Y(u)=\varnothing\}|,
\quad e_w=\mathbf1_{w=0}.$$

Every predecessor is obtained exactly once as follows:

1. Set $p_X(u)=p_Y(u)$ for $u\in S$ and $p_X(0)=0$.
2. For each $w$, send each labelled $v\in L_w$ to a parent in $A_w$;
   additionally allow parent $0$ when $w=0$.
3. Require each $u\in A_w$ having no child in $S$ to be chosen by at least
   one of the leaves in $L_w$.

### Necessity

Input leaves remain leaves, so $I_Y\subseteq I_X$ and necessarily
$I_X=I_Y\cup B$ for the unique set $B=I_X\cap L_Y$. Input internal
vertices keep their parent edges. Their parents are internal vertices or
the root, so Step 1 determines their complete skeleton.

An input leaf attached to the root remains a root child. Every other input
leaf $v$ attached to $u\in I_X$ acquires parent $p_X(u)=p_Y(u)$. Thus
$p_Y(v)=p_Y(u)$: the chosen input parent and the leaf are siblings in the
target. These are exactly the parent choices in Step 2. An input internal
vertex that has no child in the skeleton must receive at least one input
leaf; Step 3 is therefore necessary.

### Sufficiency and uniqueness

The set $S$ is ancestor-closed in $Y$ apart from the root, because it
contains every nonroot internal vertex of $Y$; adding target leaves cannot
violate this property. Step 1 consequently gives a rooted skeleton on
$S\cup\{0\}$. Step 2 attaches all remaining labels as leaves to that
skeleton, never to themselves or to other new leaves. The result is a
rooted tree on the original full label set. Step 3 makes each vertex of
$S$ internal, and the other vertices are leaves. Applying the literal LLG
map now restores every edge of $Y$ by the necessity calculation. All
choices are recovered from the input parent map, so there is no overlap
between choices or branches.

Define the finite, explicitly evaluated onto-recipient sum

$$Q(a,\ell,b,e)=\sum_{j=0}^{b}(-1)^j\binom bj(a+e-j)^\ell.$$

There are $a+e$ possible parents for each of $\ell$ distinct leaves, and
$b$ specified parents must all be hit. Inclusion--exclusion on the missed
specified parents proves the displayed formula, including empty cases.
Different sibling groups use disjoint leaf sets and independent choices.
The full target law is therefore

$$|F^{-1}(Y)|=
\sum_{B\subseteq L_Y}\ \prod_{w\in\{0,\ldots,N\}}
Q(a_w,\ell_w,b_w,e_w).\tag{5}$$

Formula (5) includes impossible targets with value zero. It is a complete
structural decoder and finite arithmetic formula, not a request to
enumerate all rooted trees. Its hit-recipient primitive is ordinary
inclusion--exclusion, also present in the original P114 inverse proof;
that primitive itself receives no contribution credit.

## 3. Sharp LLG maximum and its unique maximizing target

Let $\mathcal H_N$ be the rooted labelled trees of height at most two on
the same full vertex set. By (3), these are exactly the predecessors of
the star. Choosing its $k$ depth-one labels and then the parent of every
remaining label gives

$$|F^{-1}(S_N)|=|\mathcal H_N|=M_N
=\sum_{k=0}^{N}\binom Nk k^{N-k}.\tag{6}$$

For $N=0$, the $0^0$ convention gives the required one tree. This count is
also the elementary number of idempotent functions on the $N$ nonroot
labels: replace each height-one parent $0$ by a self-loop, and leave each
height-two parent unchanged. This is an explicit classical count adapter,
not a new enumerative sequence or a priority claim.

Fix an arbitrary target $Y$ and an input $X\in F^{-1}(Y)$. Let $S=I_X$.
Compress $X$ into a tree $K$ by setting

$$p_K(v)=\begin{cases}0,&v\in S,\\p_X(v),&v\notin S,
\end{cases}\qquad p_K(0)=0.$$

Every original leaf has its parent in $S\cup\{0\}$, so $K\in\mathcal H_N$.
This compression is injective **within the fixed target fibre**. To prove
that, let $I_K$ denote the nonroot internal vertices of $K$. Then

$$B=L_Y\cap I_K,\qquad S=I_Y\cup B.\tag{7}$$

For a target leaf $u$ that was input-internal, every input child of $u$
was an input leaf: an input-internal child would have kept its edge and
made $u$ nonleaf in the target. Thus at least one child of $u$ is retained
by compression, and $u\in I_K$. Conversely an input leaf has no child in
$K$. This proves (7). Once $S$ is known, recover $p_X(v)=p_Y(v)$ on $S$
and $p_X(v)=p_K(v)$ on its complement. Hence the compression has an
explicit left inverse and

$$|F^{-1}(Y)|\le M_N.\tag{8}$$

If $Y\ne S_N$, it has a nonroot leaf $v$ of depth at least two. The
compressed tree $K=S_N$ cannot arise from its fibre: in that case
$I_K=\varnothing$, so (7) gives $B=\varnothing$ and this target leaf is
an input leaf attached to $0$. Its output parent would then be $0$,
contradicting its depth in $Y$. Therefore the injection misses at least
the star itself, and

$$Y\ne S_N\quad\Longrightarrow\quad |F^{-1}(Y)|\le M_N-1.\tag{9}$$

Equations (6)--(9) prove the sharp maximum and its unique maximizing target
for every $N$, with the vacuous nonstar cases at $N=0,1$ included. The
injection does not assert a global conjugacy or a general parametrization
of all idempotents by every target fibre.

## 4. OMP closure and identity with the directly owned operator

Use the exact ornamentation carrier in INTAKE.md. A connected vertex set
of a tree contains the unique path between any two of its vertices.
Thus an intersection of connected sets all containing $v$ is connected
and still contains $v$; its highest vertex remains $v$.

Coordinatewise intersection also preserves the required laminarity. If
vertices $u,v$ are incomparable in the ancestor order, their descendant
sets are disjoint. Otherwise assume $u$ is a strict ancestor of $v$.
Whenever the two intersected ornaments have a common vertex, every
original pair has a common vertex. Laminarity then forces each ornament
at $v$ to be contained in the corresponding ornament at $u$; the reverse
containment is impossible because the ornament at $v$ cannot contain its
strict ancestor $u$. Taking intersections retains this containment. This
proves meet closure, including intersections over all immediate predecessors.

The carrier is finite, and $\delta_{\min}(v)=\{v\}$ is its minimum.
Every nonminimum element has a maximal strict lower element, so its update
is strictly smaller than itself. Therefore every orbit reaches the minimum,
which is the unique fixed/recurrent point. The integer potential
$\sum_v(|\delta(v)|-1)$ strictly decreases until then. These generic facts
are supporting checks only; no new sharp time theorem is asserted here.

The identity map on assignments takes this exact carrier, order, covers
and coordinate meet to Ajran--Defant's $\mathcal O(T)$ and $\mathrm{Pop}$
in arXiv:2501.10311v1, §§1.1--1.2. Their §1.3 Theorems 1.1--1.2 explicitly
address the sharp maximum forward-orbit size and image characterization.
The main agent read the actual definitions and theorem statements, and
Lemma 2.4's cover/update proof; it did not independently audit every source
theorem. A chain base tree is the stated Tamari specialization, not an
additional fresh literal or independent contribution.

## Final disposition

LLG's nontrivial inverse formula and sharp maximum survive mathematically,
but its temporal axis is transferred in full from the old peeling factor.
OMP is a direct entire-carrier source collision. Neither supplies a new
two-axis contract. **NO_PROMOTION / HOLD_EXTERNAL.** No pilot, admission,
number, gate or manuscript is requested; no unproved larger-size claim is
being deferred to a numerical experiment.
