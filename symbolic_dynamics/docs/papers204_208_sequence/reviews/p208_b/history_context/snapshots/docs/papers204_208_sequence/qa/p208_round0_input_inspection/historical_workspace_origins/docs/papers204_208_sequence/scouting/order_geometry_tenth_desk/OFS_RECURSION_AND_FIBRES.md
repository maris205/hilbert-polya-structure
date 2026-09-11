# OFS protected-cell recursion and complete recursive fibres

2026-09-06 UTC. The main scout `batch197_fosp_gate` proposed the tree
recursion and fibre parser. This desk, `batch197_lzk_gate`, independently
reconstructed the protected-cell induction and checked the parser and its
boundary cases below. Both are mathematical contributors to these claims;
this is not a manuscript review or a global novelty verdict.

**Later same-day supplement:** the historical temporal-hold wording below
records the state when this recursion/fibre proof was first written.
[OFS_TEMPORAL_CHECK.md](OFS_TEMPORAL_CHECK.md) now supplies the complete
deductive temporal argument. It supersedes that mathematical hold, not the
still-open source/value gate or the missing affected numerical receipts.

## Claim, status and dependencies

**PROVABLE AS STATED:** the exact all-size tree recursion for the declared
OFS map; the targetwise fibre formula below; its maximum and equality
target; and the associated recursively specified image count. This does
**not** prove a unique two-cycle, a global height bound, or a sharp temporal
statement. Those remain **NOT CURRENTLY JUSTIFIED** in this desk.

The carrier is every triangulation of the convex polygon with cyclic
labels $0,\ldots,n-1$, for $n\ge3$. OFS snapshots its original internal
diagonals in increasing lexicographic endpoint order, then flips each once
in the current triangulation. New diagonals are not scheduled. The presence
condition never skips an original diagonal before its own visit, since no
other flip removes that diagonal.

Dependencies are: rooted-tree triangulation encoding; the first active
vertex fan; protected new diagonals; induction on leaf count; then a
weighted decomposition of a left-spine branch list. Binary compositions,
Catalan enumeration and formal generating-function algebra receive no
standalone novelty credit. No source theorem is invoked to prove the
specific OFS recursion. The actual author's original-box comparison is
separate pressure, not the proof's induction hypothesis.

## 1. Notation and the exact recursive map

Use full ordered binary trees rooted at the boundary edge $(0,n-1)$.
An internal node is the triangle touching its root edge, with its left and
right subpolygons as children; a leaf $e$ is a boundary interval. Thus
a triangulation has $n-1$ leaves and $m=n-2$ internal nodes. The isolated
leaf is an auxiliary empty interval case, not an additional polygon
state. Put $L_1=e$ and $L_{l+1}=(L_l,e)$ for the left comb with $l$ leaves.

Every nonleaf tree has a unique left-spine branch list

$$\operatorname{LS}(T)=(B_1,\ldots,B_k),\qquad
T=(\cdots((e,B_1),B_2),\ldots,B_k).$$

Let $\operatorname{first}(S,A)$ replace the first (leftmost) leaf of $S$
by $A$. Define auxiliary operations

$$G(B)=F((e,B)),$$
$$P(B_1,B_2)=F((B_1,B_2)),$$
$$P(B_1,\ldots,B_k)=\operatorname{first}
 \bigl(G(B_k),P(B_1,\ldots,B_{k-1})\bigr)\quad(k\ge3).$$

The exact OFS map in this encoding is

$$F(e)=e,\qquad F((e,e))=(e,e),$$
$$F(T)=(e,P(\operatorname{LS}(T)))
 \quad\text{if }|\operatorname{LS}(T)|\ge2,$$
$$F((e,B))=\operatorname{first}(G(C_1),(e,e))
 \quad\text{if }\operatorname{LS}(B)=(C_1),$$
$$F((e,B))=((e,e),P(\operatorname{LS}(B)))
 \quad\text{if }|\operatorname{LS}(B)|\ge2.$$

The final two cases assume $B\ne e$. Each recursive use of $F$ has fewer
leaves than the tree whose output is being defined, so these equations
are well-founded. All operations preserve leaf count.

## 2. Protected-cell proof of the recursion

### Step 1: initial vertex 0 is not an ear

Write $\operatorname{LS}(T)=(B_1,\ldots,B_k)$ with $k\ge2$.
The neighbors of vertex $0$ are

$$1=a_0<a_1<\cdots<a_k=n-1,$$

where $B_i$ spans the boundary interval from $a_{i-1}$ to $a_i$.
The first scheduled diagonals are exactly
$(0,a_1),\ldots,(0,a_{k-1})$. At visit $i$, the adjacent triangles
have vertices $(0,1,a_i)$ and $(0,a_i,a_{i+1})$, by induction through
the preceding fan flips. The replacement is therefore $(1,a_{i+1})$.
It crosses the old diagonal just removed, so it was not original and is
never scheduled. These new diagonals are protected for the rest of the
update. In particular the last one makes vertex $0$ an ear.

The cell bounded by $(1,a_2)$ has encoded triangulation $(B_1,B_2)$
before its remaining original diagonals are visited. Its interior original
diagonals are exactly the old roots/descendants in these two branches.
Since its boundary is protected, no outside flip changes the cell. The
remaining lexicographic schedule restricted to it is exactly its own OFS
schedule, after the order-preserving relabelling of its vertices. Its
output is $F((B_1,B_2))$ by induction on the smaller leaf count.

For $i\ge3$, the next cell is bounded by the two protected diagonals
$(1,a_{i-1})$ and $(1,a_i)$ and the boundary arc through $B_i$. Treat
the earlier protected prefix as one boundary leaf. The cell's initial
tree is $(e,B_i)$, and its scheduled diagonals are exactly the old root
of $B_i$ if nonleaf and that root's descendants. Thus the cell output
is $G(B_i)$. Restoring the earlier prefix is precisely substitution into
its first leaf. The protected boundaries ensure that the cell operations
do not interfere; their original endpoint order restricts to the declared
order within every cell. Gluing these outputs yields $P(B_1,\ldots,B_k)$.
The outer ear adds the first leaf, proving the third displayed equation.

### Step 2: initial vertex 0 is an ear

Now $T=(e,B)$; the case $B=e$ is the triangle and is fixed. Suppose
first $B=(e,C_1)$, equivalently $|\operatorname{LS}(B)|=1$.
The only original vertex-$1$ diagonal is $(1,n-1)$. Its opposite
vertices are $0$ and $2$, so its flip creates the new protected diagonal
$(0,2)$, bounding the triangle on vertices $0,1,2$. Contract this
triangle to a boundary leaf. The remaining initial tree is $(e,C_1)$,
and its old diagonals are exactly the remaining scheduled diagonals.
After the order-preserving relabelling of $0,2,\ldots,n-1$, induction
gives output $G(C_1)$. Restoring the triangle substitutes $(e,e)$ into
the first leaf. This proves the fourth equation, including $C_1=e$.

If $\operatorname{LS}(B)=(C_1,\ldots,C_r)$ with $r\ge2$, write
the neighbors of vertex $1$ as $0,2=b_0<b_1<\cdots<b_r=n-1$.
The first $r-1$ fan flips create protected $(2,b_2),\ldots,(2,b_r)$,
just as in Step 1 with the starting labels shifted. The last original
fan diagonal $(1,n-1)$ then flips to $(0,2)$. Its adjacent triangles
are $(0,1,n-1)$ and $(1,2,n-1)$. The triangle on $0,1,2$ is protected,
and the remaining cells beyond $(2,n-1)$ are exactly the Step 1 cells
for $C_1,\ldots,C_r$. Their output is $P(C_1,\ldots,C_r)$, with
the left cherry attached at the outer root. This proves the last equation.

Every case reduces to strictly smaller cells, so this is an all-$n$
induction, independent of any finite functional-graph data.

## 3. All possible targets and the full fibre recursion

The equations first imply that every output nonleaf has the form
$(L_l,R)$, with $l\ge1$. Indeed the first branch has a leaf as its
left subtree, the final branch has a cherry, and first-leaf substitution
by a cherry extends the left comb of the smaller inductive output.

Define $h(e)=1$. For a nonleaf $R$, write its unique left-spine list as

$$\operatorname{LS}(R)=
 e^{a_0}D_1e^{a_1}\cdots D_re^{a_r},$$

where each $D_j$ is nonleaf and all $a_i\ge0$. If $r=0$, let $s\ge1$
be the list length and put

$$h(R)=2^{s-1}.$$

If $r\ge1$ and some internal gap $a_i$ for $1\le i<r$ is zero, put
$h(R)=0$. Otherwise put

$$h(R)=2^{\max(a_0-1,0)+\sum_{i=1}^{r-1}(a_i-1)
                       +\max(a_r-1,0)}
          \prod_{j=1}^r h(D_j).$$

The full targetwise formula is

$$|F^{-1}((L_l,R))|=h(R)\quad(l\ge1),$$

and every target whose left child is not a left comb has fibre zero.
This includes all sizes and the exceptional triangle/cherry boundaries.

### Step 3: why the fibre is independent of the left comb length

Let $A(l,R)$ denote the fibre of $(L_l,R)$. For $l=1$ and $R\ne e$,
the preimages are exactly left-spine lists of length at least two whose
$P$ output is $R$. For $l=2$ and $R\ne e$, they are exactly sources
$(e,B)$ with a left-spine list of $B$ of length at least two and the
same $P$ output $R$. This is a bijection with the preceding lists.

There is no extra contribution to these $l=2,R\ne e$ targets from
the first-leaf branch: $G(C)$ has a leaf as its root's left child only
when $C=e$, which gives $G(e)=(e,e)$ and hence $R=e$. This follows
directly from the recursive cases: all other $G$ outputs have a left
comb of at least two leaves.

At $R=e$, $A(1,e)=1$ is the fixed triangle and $A(2,e)=1$ is the
unique source $(e,(e,e))$ of $((e,e),e)$. A $P$ output cannot be a
leaf, since its initial pair has at least two leaves and all maps
preserve leaf count.

For $l\ge3$, every preimage must be in the first-leaf branch. Remove
the first cherry from the target to obtain $(L_{l-1},R)$. Its
preimages under $G$ are precisely all its preimages under $F$, because
its left child is nonleaf, so every $F$ source has first child $e$.
Thus $A(l,R)=A(l-1,R)$. Induction proves independence of $l$.

### Step 4: parse the branch list and count every source exactly once

It remains to count the $P$ lists producing a nonleaf $R$. A seed block
$F((B_1,B_2))$ has a left-spine list either $e^aD$ with $D$ nonleaf
and $a\ge0$, or a positive all-leaf block. A later block $G(B_i)$
has the same alternatives except that $a\ge1$ before a nonleaf $D$.
For either nonleaf-ending block, Step 3 gives multiplicity $h(D)$;
every positive all-leaf block has multiplicity one. Substitution into
the first leaf concatenates the left-spine lists.

Consequently two nonleaf decorations cannot be consecutive. When their
gap has $a\ge1$ leaves, those leaves split into any number of positive
all-leaf blocks followed by a positive prefix for the next decorated
block. There are exactly $2^{a-1}$ such compositions. A leading run
of $a\ge1$ leaves has the same count: its entire run may belong to
the seed ending at the first decoration, or it is divided before that
decorated block. A zero-length leading run has one choice. A trailing
run of $a\ge1$ leaves is an arbitrary positive composition, again
giving $2^{a-1}$; an empty trailing run gives one choice. With no
decorations, the entire positive all-leaf list has $2^{s-1}$ choices.

Each resulting block partition, seed preimage pair $(B_1,B_2)$ and
later $G$ preimage $B_i$ reconstructs a unique original branch list.
Conversely the original branch list fixes those blocks and inputs.
Thus no extra choice, collision or multiplicity is omitted. Multiplying
the independent composition factors and the recursively smaller $h(D_j)$
gives exactly the formula above.

## 4. Maximum fibres and the equality target

Write $q(R)$ for the number of internal nodes. For every nonleaf $R$,

$$h(R)\le2^{q(R)-1},$$

with equality exactly when $R$ is a left comb. The all-leaf list is
the left-comb case and gives equality. If there is at least one nonleaf
decoration and the fibre is positive, let $a=\sum a_i$ and $r\ge1$.
There are $a+r$ spine nodes, so
$q(R)=a+r+\sum q(D_j)$. By induction each decoration contributes at
most exponent $q(D_j)-1$. The explicit gap exponent is at most $a$.
Hence the total exponent is at most
$a+\sum q(D_j)-r=q(R)-2r\le q(R)-2$, which is strictly smaller
than $q(R)-1$. Zero fibres also cannot attain the positive bound.

For a target with $m$ internal nodes of form $(L_l,R)$, one has
$q(R)=m-l$. For $m\ge3$ the maximum fibre is

$$2^{m-2}=2^{n-4},$$

and equality forces $l=1$ and $R=L_m$. This is the unique polygon
fan target based at vertex $1$. At $m=1$ the unique triangle has fibre
one; at $m=2$ both quadrilateral triangulations have fibre one. These
small cases are not incorrectly included in the uniqueness claim.

## 5. Actual recursive image class and known static counting deduction

Let $\mathcal H$ consist of the leaf and trees $R$ for which $h(R)>0$.
Equivalently, each nonleaf decoration in $\operatorname{LS}(R)$ lies
in $\mathcal H$, and no two such decorations are adjacent. This is
the exact recursive class used by the fibre decoder, not the refuted
standard UUDU word class in the earlier guess.

Let $H(z)$ count $\mathcal H$ by internal nodes, including its leaf.
A leaf branch has weight $z$, and a nonleaf branch has weight
$z(H-1)$. Branch lists without adjacent nonleaf branches have series

$$H=\frac{1+z(H-1)}{1-z-z^2(H-1)},$$

where the empty branch list supplies the isolated leaf. Algebra gives

$$H=\frac1{1-z}C\!\left(\frac{z^2}{(1-z)^3}\right).$$

Every image nonleaf is uniquely $(L_l,R)$ with $l\ge1$ and
$R\in\mathcal H$. Including the auxiliary leaf, its series is

$$I(z)=1+\frac{zH(z)}{1-z}
 =1+\frac{z}{(1-z)^2}
       C\!\left(\frac{z^2}{(1-z)^3}\right).$$

Substitution, using the defining quadratic for $C$, yields
$I=1+z(1-z)I^2+z^2I$, the same equation as the old UUDU-avoidance
series discussed in the source audit. This is equality of counting
series, not the refuted literal rooted-tree word dictionary. The old
static sequence and generic regular-tree enumeration remain deducted.

## 6. Verification boundary and remaining risk

The main scout's archived `tree_execution_01` comparison was read in
full: it checks all original $n=3,\ldots,10$ trees against the declared
literal, with 6,171 graph/tree assertions and 26,932 literal flip
assertions. Its code imports its frozen `pilot.py`; that dependency is
explicitly included in the desk pins. This desk did not execute that
producer and does not label the read as an independent replay.

The polynomial checker in this desk concerns QAS/DTC, not this tree
proof. The newly deduced all-size fibre formula still requires a
separately declared affected original-box check before it can be
presented as verified computational evidence. No cutoff expansion is
licensed by these proofs. A new reviewer of a retained paper must be
a noncontributor, not either worker who supplied the recursion/parser.

The temporal axis and complete source/value assessment of any retained
contract remain open. A full source decoder does not by itself admit
this candidate or establish novelty of its mechanism.

**Final same-day evidence update:** the affected standalone author pair
has now completed and was actually read, including full code, canonical
and process receipts; see [REPORT.md](REPORT.md). Each run reports
62,087 assertions on the unchanged original boxes. This supersedes the
above pending-numerical status, but is not a desk numerical rerun or an
independent candidate review. The earlier temporal hold was already
superseded by the temporal supplement linked at the start of this file.
