# LAR author proof package

Author: `/root/round211_tree_order_scout`, 2026-09-08 UTC.
Status: the explicit mathematics below is `PROVABLE AS STATED` on its
stated carrier. A fresh paper-sized residual is `NOT CURRENTLY JUSTIFIED`.
This is not an independent candidate or manuscript review.

## Claims and assumptions

Let $\mathcal T_n$ be all simple undirected trees on $[n]$. For $n\le2$
hold the unique state. For $n\ge3$, select the least leaf $v$, write its
neighbour as $u$, select the least farthest vertex $a$ from $v$, and replace
$uv$ by $av$. Call this map $L$.

For a labelled tree $S$ with at least two vertices, let
$f_S(x)=\min\operatorname{argmax}_{y\in S}d_S(x,y)$. Let $p(S)$ be its
least peripheral vertex (a vertex of eccentricity equal to its diameter),
and let $q(S)=f_S(p(S))$. The pair is unordered when written
$\{p(S),q(S)\}$.

The claims are:

1. Every orbit for $n\ge3$ enters a two-cycle. A target $T$ is recurrent
   exactly when, with least leaf $m$, $S=T-m$, and $a$ the neighbour of $m$,
   every leaf of $S$ exceeds $m$ and $a\in\{p(S),q(S)\}$.
2. The maximum entry time is $n-2$ for every $n\ge3$, and zero for $n\le2$.
3. The complete one-step inverse is the disjoint two-case formula below.
4. The maximum fibre is $1$ for $n=1,2$, $2$ for $n=3$, $3$ for $n=4$,
   and $n-2$ for every $n\ge5$.

No statewise closed entry-time formula, full maximum-fibre equality class,
basin enumeration, or novelty theorem is claimed. The sharpened piecewise
fibre maximum was derived after the sole run; that run predeclared and
asserted only the weaker $n-1$ bound, although its complete maxima are
consistent with the sharper statement. No second run tested that new
predicate. The proof, not the finite maxima, is the evidence for it.

## Dependency map and known inputs

Classical tree-center/diameter geometry gives the central vertex or edge
and its peripheral branches. The lexicographic refinement in Lemma 1 is
an immediate deduction and is credited to that primitive, not to LAR.
LAR recurrence and its clock use Lemma 1 plus the monotone least-leaf
scheduler. The inverse uses the possible new leaf under a single edge
move; its maximum uses the branch sizes in Lemma 1. These proofs differ
as forward-scheduler and reverse-surgery arguments, but mathematical
separation does not by itself establish two new substantive contributions.

## Lemma 1: the fixed-tree farthest map has two image vertices

For every tree $S$ of order $N\ge2$,
$$\operatorname{im}f_S=\{p(S),q(S)\},\qquad
f_S(p(S))=q(S),\quad f_S(q(S))=p(S).$$
Every fibre has size at most $N-1$. If $N\ge3$, a fibre has size $N-1$
if and only if $S$ is a star and its target is the least labelled leaf.

Proof. First suppose the diameter is $2h$, with central vertex $c$.
Every branch at $c$ has height at most $h$, and at least two have height
$h$. Peripheral vertices are precisely the vertices at depth $h$ from
$c$. Put $p=p(S)$, and let $B$ be the component of $S-c$ containing $p$.
The vertex $q$ is the least depth-$h$ vertex outside $B$.

For $x\in B$, of depth $r\ge1$, the distance to a depth-$h$ vertex
outside $B$ is $r+h$. Its distance to a vertex in $B$ is at most
$r+h-2$, since their paths to $c$ share at least their first edge.
Thus $f_S(x)=q$. For $x\notin B$, if $x=c$ then $p$ is the least
vertex at maximum distance. If $x$ is in another branch, a depth-$h$
vertex outside that branch is farthest and $p$ is the least such vertex.
Hence $f_S(x)=p$. Therefore
$$f_S^{-1}(q)=B,\qquad f_S^{-1}(p)=V(S)\setminus B.\tag{1}$$

If the diameter is $2h+1$, remove its central edge $cd$ and call the two
sides $C,D$. Every vertex in $C$ has depth at most $h$ from $c$, and
every vertex in $D$ has depth at most $h$ from $d$; both maxima occur.
For $x\in C$ of depth $r$, maximum distance to its own side is at most
$r+h$, whereas an opposite depth-$h$ vertex is at distance $r+h+1$.
Thus $f_S$ maps all of $C$ to the least depth-$h$ vertex of $D$, and
all of $D$ to the least depth-$h$ vertex of $C$. These are $p,q$ in one
order. This includes $h=0$, when $S$ is the single edge.

Both image fibres are nonempty, proving the $N-1$ bound. In the even
diameter case, $V(S)\setminus B$ contains $c$ and a second peripheral
branch, so it has at least two vertices. A singleton other fibre requires
$B=\{p\}$, which forces $h=1$ and $S$ to be a star. Conversely a star
has precisely that partition. In the odd diameter case, a singleton
side forces $h=0$, and then $N=2$. This proves the equality assertion.
\(\square\)

The standard central-vertex/edge description follows from any diameter:
its midpoint bounds all off-diameter branch lengths, since otherwise an
off-path vertex and the opposite endpoint would yield a longer path.
Consequently the midpoint is the unique center when the diameter is even,
and the two vertices incident to it are the centers when it is odd. No
different selector geometry is assumed in (1).

## Lemma 2: one nondropping step reaches recurrence

The selected leaf label never increases. If $v$ is selected in both $T$
and $L(T)$, then $L(T)$ is already recurrent.

Proof. Write $u$ for the old neighbour and $a$ for the new neighbour.
The vertex $a$ is an old leaf different from $v$, so $a>v$ and $a\ne u$.
All old leaves except $a$ stay leaves; $v$ stays a leaf. The only possible
new leaf is $u$, and it appears precisely when $\deg_T(u)=2$.
Thus the label drops exactly when $\deg_T(u)=2$ and $u<v$.

If there is no drop, all leaves of $S=T-v$ exceed $v$: they are the old
leaves other than $v$ and possibly the newly exposed $u$, which must then
exceed $v$. Deleting $v$ gives the same $S$ before and after the move.
Distances from $v$ to vertices of $S$ are $1+d_S(u,\cdot)$, so its new
attachment is $f_S(u)\in\{p(S),q(S)\}$. Attaching $v$ alternately to
$p(S)$ and $q(S)$ keeps $v$ the least leaf because every leaf of $S$
exceeds it. Lemma 1 shows these two distinct trees form a two-cycle.
\(\square\)

## Theorem 1: recurrence and sharp maximum time

The least-leaf labels must eventually stop strictly decreasing. Lemma 2
then puts the trajectory on a two-cycle; fixed points are impossible for
$n\ge3$ because $a\ne u$ and each step changes an edge.

On any recurrent orbit the least leaf cannot decrease anywhere, so its
label $m$ is constant. Its deletion leaves one fixed skeleton $S$.
Lemma 1 forces the attachment to alternate between $p(S)$ and $q(S)$.
Every leaf of $S$ appears as a leaf of at least one of those two attached
trees: $p$ and $q$ each appear in the other phase and every other leaf
appears in both. Thus every leaf of $S$ must exceed $m$. Conversely these
conditions construct the two-cycle in Lemma 2. This proves the stated
necessary-and-sufficient recurrence criterion.

For the sharp clock, let the initial least leaf be $m$. If $m\le n-2$,
there can be at most $m-1\le n-3$ initial strict drops. The first step
without a drop reaches recurrence, so the entry time is at most $n-2$.

If $m=n-1$, the initial leaves must be exactly $n-1,n$. A finite tree
with exactly two leaves is a path: the identity
$\sum_v(\deg(v)-2)=-2$ rules out any degree exceeding two when exactly
two vertices have degree one. Relay preserves paths because it takes one
endpoint to the other endpoint. If at most $n-3$ strict drops occur, the
previous bound applies. If $n-2$ strict drops occur, the new least leaf
is $1$. Every path with least endpoint $1$ is recurrent by the criterion:
its deleted skeleton is a path, the attachment is one of its endpoints,
and all other labels exceed $1$. Thus the bound remains $n-2$.

For equality, take the labelled path in order
$$n-1,n-2,\ldots,2,1,n.$$
At times $0,1,\ldots,n-2$ the selected labels are successively
$n-1,n-2,\ldots,1$. At each of the first $n-2$ transitions, the exposed
next vertex is a smaller new leaf, so states before time $n-2$ cannot be
recurrent. At time $n-2$ this path has least endpoint $1$ and is recurrent.
The maximum is therefore exactly $n-2$. The held cases $n=1,2$ have
entry time zero. \(\square\)

## Theorem 2: complete inverse formula

For a target $T\in\mathcal T_n$, $n\ge3$, let its two smallest leaves be
$m<v$. Write $a$ for the neighbour of $m$, and $b$ for the neighbour of
$v$. All comparisons below are label comparisons. Define
$$B(T)=\begin{cases}
\#\{u\in V(T-m): f_{T-m}(u)=a\},&\deg_T(a)=2\text{ and }a>m,\\
0,&\text{otherwise},
\end{cases}$$
and
$$E(T)=\mathbf1\{\deg_T(b)=2,\ b>v,\ f_{T-v}(m)=b\}.$$
Then the inverse is disjoint and complete, with
$$|L^{-1}(T)|=B(T)+E(T).\tag{2}$$
Lemma 1 explicitly evaluates $B(T)$ as one of two central-part sizes
(or zero), not an exhaustive scan of source trees.

Proof. Let $w$ be the moved leaf of a predecessor. Since the least leaf
cannot increase, $w\ge m$. If $w=m$, the predecessor is obtained by
deleting $ma$ and attaching $m$ to some vertex $u$ of $S=T-m$.
The new neighbour $a$ must have been a leaf before the update, so
$\deg_T(a)=2$. It was a source leaf different from the least leaf $m$,
so $a>m$. All other leaves of $S$ are target leaves other than $m$ and
are also larger than $m$. Thus every attachment $u$ with $f_S(u)=a$
produces a source whose least leaf is exactly $m$, and these are all
sources in this case. The map $u\mapsto S+mu$ is injective. This gives
$B(T)$.

If $w>m$, the vertex $m$ cannot have been a source leaf, so it must be
the only newly exposed leaf, namely the old neighbour of $w$. Every
other target leaf is an old source leaf or $w$ itself and is at least
$w$, forcing $w=v$, the second-smallest target leaf. Thus there is only
one possible source, obtained by replacing $vb$ with $vm$. The new
neighbour $b$ must be a larger source leaf, requiring
$\deg_T(b)=2$ and $b>v$. Every remaining source leaf exceeds $v$ by
the second-smallest condition. The exact farthest choice is then
$f_{T-v}(m)=b$. These conditions are necessary and sufficient, giving
$E(T)$. The two cases have different least source leaves and cannot
overlap. \(\square\)

## Theorem 3: sharp one-step fibre maximum

By Lemma 1, $B(T)\le n-2$, and $E(T)\le1$, so every fibre is at most
$n-1$. For $n=3$, the path $1-3-2$ has $B=1,E=1$ and reaches two.
For $n=4$, the path $1-2-4-3$ has $B=2,E=1$ and reaches three.

Suppose $n\ge5$. If $B(T)\le n-3$, (2) gives at most $n-2$.
If $B(T)=n-2$, Lemma 1 forces $S=T-m$ to be a star and $a$ to be its
least labelled leaf. The target is that star with a new leaf $m$
attached to $a$. Its second-smallest leaf $v$ is some other leaf of
the star. Its neighbour $b$ is the star center, whose target degree is
$n-2\ge3$. Hence $E(T)=0$. This again gives at most $n-2$.

For equality, let $S$ be the star on labels $2,\ldots,n$ with center
$3$, and attach leaf $1$ to leaf $2$. All leaves of $S$ exceed $1$,
and $2$ is its least labelled leaf. Lemma 1 gives $B=n-2$ and $E=0$.
The held singleton and edge have one predecessor each. The claimed
piecewise maximum follows. \(\square\)

## Residual-value and source risks

The proof does not assert equality or conjugacy with P195 or GG08. P195
keeps the entire tree fixed and moves an odd-side eligible neighbour
marker. GG08 keeps a metric graph fixed and maps a whole subset to all
farthest holes; taking a least farthest singleton is not generally a factor
of its full subset iteration. LAR instead changes one leaf edge and its
fixed skeleton changes at strict label drops.

Nevertheless every nondropping phase collapses in one step to the
classical two-antipode map. The sharp worst-case clock is the generic
least-label budget with an endpoint-path equality witness. The inverse
uses the standard reverse-edge surgery plus the same diameter branch
partition. These facts leave no demonstrated second pair of substantive
nontransferring mechanisms after full subtraction. This author therefore
does not recommend promotion. A missing direct leaf-relocation primary body
also remains a source limitation; bounded negative search is not clearance.
