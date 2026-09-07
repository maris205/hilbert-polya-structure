# LGB re-entry: complete mathematics, insufficient new contribution

## Claim and status

**PROVABLE AS STATED**, for the temporal and inverse claims below. This is
an author-side bounded re-entry audit, **not** a newly accepted system or an
independent Stage-1 gate. Selection recommendation: `KILL_VALUE_THIN`.

## Assumptions and notation

Fix an integer $n\geq1$. The carrier consists of all labelled trees on
$\{0,\ldots,n-1\}$ rooted at $0$. A state is its parent function $p$, with
$p(0)=0$ and every nonroot orbit reaching $0$. Write $d(v)$ for depth,
$C(u)=\{v\ne0:p(v)=u\}$ for the children of $u$, and $L$ for the nonroot
leaves. A deep leaf has $d(v)\geq2$. If there is one, let $v$ be the least
labelled deep leaf and replace $p(v)$ by $p(p(v))$, leaving every other
parent unchanged. If there is none, hold. This is exactly the previously
reserved LGB literal, not a modification.

Let $S_n$ be the rooted star and put

$$D(T)=\sum_{v\ne0}(d(v)-1).$$

For a nonstar target $T$, list its deep leaves as $m_1<m_2<\cdots$ and put

$$r=|C(0)|,\qquad
a=|\{v\in L:p(v)=0,\ v<m_1\}|,\qquad
s=|C(p(m_1))|.$$

Set $\epsilon=1$ if at least two deep leaves exist and
$p(m_1)=p(m_2)$, and set $\epsilon=0$ otherwise.

## Strategy and dependency map

1. A single leaf move lowers only that leaf's depth. This yields the exact
   point clock and unique recurrent star without an enumerative theorem.
2. An inverse move changes a target leaf's parent to a sibling. Checking
   which target deep leaves could be smaller than the moved leaf reduces
   the old sibling atlas to two cases. This yields every source **set**,
   the compressed count and an image criterion.
3. Ordered pairs of distinct nonroot labels bound every nontrivial inverse.
   The star realizes every pair and also supplies its hold source.
4. A decomposition by the root branch containing label $1$ counts the
   depth statistic; this classical labelled-tree construction is zero credit.

## Temporal theorem

Every trajectory enters $S_n$ after exactly $D(T)$ steps. The only
recurrent state is $S_n$. The maximum entry time is

$$H_n=\frac{(n-1)(n-2)}2,$$

and exactly $(n-1)!$ states attain it. For $n=1,2$ the carrier is a
singleton and the same formulas apply.

### Proof

The selected vertex is a leaf, so changing its parent does not change any
other vertex's depth. Its new parent was its grandparent and its new depth
is one less. The result is a tree: the new parent is an ancestor, outside
the detached singleton. Thus every nonholding move lowers $D$ by exactly
one. Every summand defining $D$ is nonnegative. If a tree has a vertex at
depth at least two, a descendant of maximal depth is a deep leaf, so a
move is possible. Hence holding, $D=0$, and being $S_n$ are equivalent.
This proves the exact clock and excludes every nonstar cycle.

Sort the nonroot depths as $e_1\leq\cdots\leq e_{n-1}$. A vertex at
depth $e_i$ has distinct ancestors at depths $1,\ldots,e_i-1$, all of
which precede it in this ordering; hence $e_i\leq i$. Therefore

$$D(T)\leq\sum_{i=1}^{n-1}(i-1)=H_n.$$

Equality requires $e_i=i$ for every $i$. In particular there is a vertex
at depth $n-1$, so its root path uses every vertex. Conversely every such
endpoint-rooted path attains equality. Ordering the $n-1$ nonroot labels
along the path gives exactly $(n-1)!$ states. For the singleton the empty
ordering gives one state and depth zero.

## Complete inverse-set theorem

For every target $T$, each nonholding predecessor is uniquely obtained by
choosing a target leaf $v$ and a distinct sibling $u$ and replacing
$p(v)$ by $u$. The permitted pairs are exactly:

- If $T=S_n$, every ordered pair of distinct nonroot labels $(v,u)$.
- If $T\ne S_n$, every target leaf $v\leq m_1$ paired with any distinct
  sibling $u$, together with the one additional pair $(m_2,m_1)$ when
  $\epsilon=1$.

The target itself is an additional predecessor exactly for $T=S_n$.
Consequently,

$$|F^{-1}(T)|=
\begin{cases}
1+(n-1)(n-2),&T=S_n,\\
(r-1)a+(s-1)+\epsilon,&T\ne S_n.
\end{cases}$$

A nonstar target lies in the image if and only if

$$s\geq2\quad\text{or}\quad(r\geq2\text{ and }a\geq1).$$

For all $n\geq1$, the unique maximum-fibre target is $S_n$, with size
$1+(n-1)(n-2)$.

### Proof: necessary reconstruction and selector

Suppose a nonholding source moves $v$ from $u$ to $g=p(u)$. In the target
$v$ is still a leaf, both $u$ and $v$ are children of $g$, and $u\ne v$.
Undoing this single parent change therefore recovers the source uniquely.
Conversely, choosing a target leaf and distinct sibling and attaching that
leaf below the sibling produces a tree, because a leaf contains no other
vertex in its descendant subtree. The moved leaf has source depth at least
two, since the sibling $u$ is nonroot.

The only leaf that can disappear in this inverse move is $u$; it disappears
from the leaf set precisely when it was a target leaf. All other target
leaves remain leaves, and their depths are unchanged. The source's deep
leaves are therefore the target's deep leaves with $u$ removed if present,
together with $v$ (which may previously have had depth one). Thus $v$ is
selected if and only if no target deep leaf outside $\{v,u\}$ has label
less than $v$.

For a star this restriction is empty. For a nonstar and $v\leq m_1$ it is
also empty. Suppose instead $v>m_1$. Then $u=m_1$ is necessary, or the
smaller deep leaf $m_1$ remains eligible. Because $v$ and $m_1$ are siblings,
$v$ is itself a deep target leaf. To remove every smaller eligible leaf,
$v$ must be exactly $m_2$, and the pair exists exactly when the first two
deep leaves have the same parent. These conditions are also sufficient.

Different pairs give different parent tuples: the unique altered coordinate
identifies $v$ and its new parent identifies $u$. No such tuple equals the
target. This proves the complete source set, including all empty fibres.

### Proof: compressed count, image and equality

When $v<m_1$ is a target leaf it must be a root leaf, since $m_1$ is the
least deep leaf. Each of the $a$ such leaves has $r-1$ sibling choices.
For $v=m_1$ there are $s-1$ sibling choices. The exceptional pair contributes
$\epsilon$. These classes are disjoint, proving the nonstar formula.
In a star all $n-1$ nonroot vertices are root leaves, so there are
$(n-1)(n-2)$ ordered distinct pairs and the extra hold source.

The three terms of the nonstar formula are nonnegative. If $\epsilon=1$
then already $s\geq2$, so it introduces no additional image case. The
remaining positive alternatives are exactly the two displayed conditions.

For any nonstar target its inverse pairs are a subset of the
$(n-1)(n-2)$ ordered pairs of distinct nonroot labels. It has no hold
source. Thus its fibre is strictly smaller than the star's. For $n=1,2$
there are no nonstar targets, and the asserted unique maximizer still holds.

## Every depth layer (old reserve result, rechecked)

Let $A_n(z)=\sum_T z^{D(T)}$, over the fixed-root labelled carrier. Then
$A_1(z)=1$, and for $n\geq2$,

$$A_n(z)=\sum_{k=1}^{n-1}\binom{n-2}{k-1}\,k\,z^{k-1}
              A_k(z)A_{n-k}(z).$$

Choose the root branch containing label $1$. Its $k$ labels are selected
in $\binom{n-2}{k-1}$ ways, its root in $k$ ways, and its rooted shape and
remaining root branches contribute $A_k$ and $A_{n-k}$. Placing the branch
root one level below $0$ adds $k-1$ to the branch's local excess-depth
statistic. The branch is recovered uniquely from the resulting tree, so the
construction neither omits nor repeats a state. Coefficients give all exact
depth layers by the temporal theorem. No separate claim of innovation is
attached to this rooted-tree recurrence.

## Contribution gate: what is and is not proved

The two mathematical proofs are logically independent: the inverse is not
deduced from a depth histogram. The inverse is label-sensitive: at $n=4$,
parent tuples $(0,0,0,2)$ and $(0,0,1,0)$ have the same unlabelled rooted
shape but fibre sizes $1$ and $0$. Thus an unlabelled shape count alone does
not own it.

Nevertheless, the original graph/matching scout already supplied the exact
clock, depth recurrence, complete sibling reconstruction and sharp star
fibre. The current closed formula only eliminates a one-edge undo selector
from that existing atlas. It is a useful simplification, not a newly found
second theorem mechanism. After subtracting unit-potential descent,
rootward leaf surgery, classical depth enumeration, and the generic
least-eligible inverse filter, this re-entry has not established two
substantive nontransferring axes. That is the basis for `KILL_VALUE_THIN`;
it is **not** a claim of exact conjugacy to P114/P148/RLR or a discovered
external literal owner.

## Open risks and scope

No mathematical gap remains in the displayed all-$n$ statements. The owner
search is bounded and cannot certify novelty. No all-time inverse theorem,
closed all-$n$ image census, or new paper acceptance is claimed. The old
reserve, its code and all historical manuscripts remain unmodified.
