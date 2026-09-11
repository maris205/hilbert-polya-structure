# P208 paper-local author proof package

Status: PROVABLE AS STATED under the admitted narrow contract. This is an
adapted paper-local preservation of the original author proof below, not a
review. Historical gate-pending and no-number wording in the original has
been preserved verbatim in provenance/OFS_PROOF_PACKAGE_original.md; the
following body is the complete mathematical deduction, with current scope
clarified here. The static image series in Step 4 is fully old/deducted and
is not a headline contribution or required manuscript result. All original
false guesses/counterexamples remain in the source scouting packages.

Proof contributors: fosp/lzk; integration root; manuscript p208_author.
No external result or finite output supplies an all-size proof step.

## Claim

On all triangulations of the convex polygon with labelled vertices
$0,\ldots,n-1$, snapshot the internal diagonals in increasing lexicographic
order and flip those original diagonals, in that order, in the current
triangulation. Call the resulting self-map $F_n$ (OFS).

For $n=3$ the only triangulation is fixed. For every $n\ge4$ there is one
recurrent component, a two-cycle described below. The maximum distance to
that cycle is zero for $n=4$ and $n-2$ for $n\ge5$.
Every target has the explicit recursive fibre formula in Step 3; every
positive fibre is a power of two. For $n\ge5$ the maximum fibre is
$2^{n-4}$, attained only by the fan at vertex $1$. At $n=3,4$ every target
has one predecessor. The image generating function in Step 4 is a
consequence of the literal inverse, not a claimed new static sequence.

## Status and assumptions

**PROVABLE AS STATED**, by the deductions below. This is the author
mathematical status only; the admitted candidate gate does not substitute
for the two still-required nonauthor manuscript reviews. The full finite carrier includes every triangulation and
uses the labelled, fixed snapshot order. No dihedral quotient or refreshed
diagonal list is substituted. All cutoffs remain exactly $n=3,\ldots,10$
for the separate finite verification.

## Notation

A full plane binary tree is a leaf $e$ or an ordered pair $(L,R)$.
Root the usual triangulation dual decomposition at boundary edge
$(0,n-1)$: the two children encode the subpolygons on either side of the
third vertex of its incident triangle. There are $N=n-1$ leaves and
$m=n-2$ internal vertices. The formal one-leaf tree is added only to
express recursion; it is not an extra polygon state.

Let $\operatorname{LC}_a$ be the left comb with $a$ leaves, so
$\operatorname{LC}_1=e$ and
$\operatorname{LC}_{a+1}=(\operatorname{LC}_a,e)$. Put $c=(e,e)$.
Let $\iota(S,A)$ replace the leftmost leaf of $S$ by $A$; it satisfies
$\iota(e,A)=A$ and
$\iota((L,R),A)=(\iota(L,A),R)$.
For a nonleaf tree $T$, its left-spine list is the unique list
$\operatorname{LS}(T)=[B_1,\ldots,B_k]$ such that

$$T=(\cdots((e,B_1),B_2),\ldots,B_k).$$

The operation $F$ denotes the same literal polygon map in this dictionary,
with $F(e)=e$ as a formal extension. Define $G(B)=F(e,B)$.

## Strategy and dependency map

1. Protected new fan diagonals split the remaining scheduled flips into
   smaller independent polygons. This proves the recursive dictionary.
2. That dictionary gives a bijective inverse by cutting a left-spine list
   into one seed block and subsequent blocks. Evaluating these cuts gives
   the fibre formula and its sharp maximum.
3. A size-preserving map $K$, defined by $G^2(B)=(c,K(B))$, freezes a
   two-leaf prefix after each step on its image class. This proves global
   convergence, and a comb family proves the precise worst-case clock.

No numerical observation, static pattern-avoidance formula or unproved
external sorting theorem is used in this chain.

## Proof

### Step 1. Exact protected-cell recursion

For a list of length at least two define

$$P(B_1,B_2)=F(B_1,B_2),\qquad
P(B_1,\ldots,B_k)=\iota(G(B_k),P(B_1,\ldots,B_{k-1}))\quad(k\ge3).$$

The following recursion is exact:

$$\begin{aligned}
F(e)&=e, &F(c)&=c,\\
F(T)&=(e,P(\operatorname{LS}(T)))
 &&(|\operatorname{LS}(T)|\ge2),\\
G(e,C)&=\iota(G(C),c),\\
G(B)&=(c,P(\operatorname{LS}(B)))
 &&(|\operatorname{LS}(B)|\ge2).
\end{aligned}\tag{1}$$

Here $G(e,C)$ means $G((e,C))$; this notation never means two arguments
to $G$. Every right-hand recursive call uses fewer leaves, so (1),
together with the definition of $P$, is well founded.

To prove (1), first note that an original unvisited diagonal is still
present: flipping one diagonal removes only that diagonal. Inductively
every original diagonal is therefore visited exactly once. An inserted
diagonal crosses the one just removed, so it was not an original diagonal
and is never scheduled. This also shows that protected edges inserted
during the first fan sweep cannot be removed subsequently.

Suppose vertex $0$ is not an ear. Write its original neighbors as
$1=a_0<a_1<\cdots<a_k=n-1$, with $k\ge2$. The successive original
triangles incident to $0$ are $(0,a_{j-1},a_j)$; their other-side
subpolygons encode the branches $B_j$ of $\operatorname{LS}(T)$.
The first scheduled edges are $(0,a_1),\ldots,(0,a_{k-1})$.
At its turn $(0,a_i)$ has incident triangles $(0,1,a_i)$ and
$(0,a_i,a_{i+1})$, because the first of these is created at the preceding
turn when $i>1$. Its flip inserts $(1,a_{i+1})$.

Consequently the new edge $(1,n-1)$ protects the ear at $0$ and the new
edges $(1,a_j)$ partition its complement into cells. The first cell has
the old tree $(B_1,B_2)$; each later cell has the old tree $(e,B_j)$.
Within each cell the original lexicographic schedule restricts to its
own lexicographic schedule under the increasing relabelling of vertices.
Different cells share only their protected boundary edges, so their
remaining flips cannot alter each other's diagonals. Their final trees
are $F(B_1,B_2)$ and $G(B_j)$, respectively. Gluing the cells in their
increasing order replaces the leftmost leaf of each later cell by the
previous union. This is exactly $P$, and proves the third line of (1).

Suppose vertex $0$ is an ear, so $T=(e,B)$. The case $B=e$ is the
triangle. Otherwise first process the original fan at vertex $1$.
Its final scheduled edge $(1,n-1)$ flips to $(0,2)$, protecting the
new ear at $1$. If $\operatorname{LS}(B)=[C]$, this is the only edge
of that fan: contracting the new cherry on intervals $(0,1),(1,2)$
leaves precisely the smaller sweep on $(e,C)$. Expanding that cherry
is $\iota(G(C),c)$. If $|\operatorname{LS}(B)|\ge2$, the intermediate
fan flips insert protected edges $(2,a_j)$. The complementary cells
have exactly the seed and subsequent forms just proved, with total
tree $P(\operatorname{LS}(B))$. The protected ear has tree $c$ as
left child, giving $(c,P(\operatorname{LS}(B)))$.
These arguments include a cell that is just a triangle, whose $F$ is
the identity. Thus induction on leaves establishes all of (1).

For $n\ge4$ this proof also shows the phase factor: ear $0$ toggles.
In the first branch $(1,n-1)$ is newly protected. In the second branch
it is removed and cannot reappear, since a diagonal crossing it must
have endpoint $0$, whereas all remaining original edges have neither
endpoint $0$. Every first image has ear $0$ or ear $1$.

### Step 2. Output shape and the block inverse

Induction in (1) shows that every nonleaf $F$ output has form
$(\operatorname{LC}_l,R)$ with $l\ge1$. Every $G(B)$ has this form,
with $l\ge2$ when $B\ne e$; $G(e)=c$ has $l=1,R=e$.
For example the fourth line of (1) extends the root left comb by one
leaf, and the last line starts it at $c$.

For a nonleaf $R$, let $p(R)$ count all lists $[B_1,\ldots,B_k]$,
$k\ge2$, with $P(B_1,\ldots,B_k)=R$. This is a finite count because
the list reconstructs the source left spine, whose total number of
leaves is $1+|R|$. The following statements follow by simultaneous
induction on the number of leaves:

- Every $(\operatorname{LC}_l,R)$ with nonleaf $R$ has exactly $p(R)$
  $F$-preimages, regardless of $l\ge1$.
- It has exactly $p(R)$ $G$-preimages when $l\ge2$, and none for $l=1$.
- A left comb has exactly one $F$-preimage, a right comb, and a left
  comb of at least two leaves has exactly one $G$-preimage.

For the first item at $l=1$, sources have a nonleaf left child and
are precisely the lists counted by $p$. For $l\ge2$, sources must
be $(e,B)$ and hence are $G$-preimages. For the second item at $l=2$
and nonleaf $R$, the last line of (1) supplies exactly the lists counted
by $p$. The other branch would require $G(C)$ with root left leaf
and nonleaf right child, which is excluded by the established output
shape. At $l>2$ the fourth line of (1) uniquely removes one leading
$e$ from the source, reducing $l$ by one. For a comb target, the
same reduction ends at $G(e)=c$; the $F$ base is $F(c)=c$.
Thus the stated inverses exist, are unique in the comb case, and no
additional source branch has been omitted.

It remains to evaluate $p(R)$. The identity

$$\operatorname{LS}(\iota(S,A))=
\operatorname{LS}(A)\,\operatorname{LS}(S)$$

holds by following the leftmost branch; concatenation is on the right.
The list of $R$ is therefore partitioned into blocks. The first (seed)
block is the left-spine list of an $F$ output, and each later block is
the list of a $G$ output. A block ending in a nonleaf $D$ has form
$e^kD$, with $k\ge0$ for a seed and $k\ge1$ for a later block.
A block of only leaves may have any positive length in either position.
For a block ending in nonleaf $D$, the multiplicity is $p(D)$;
for an all-leaf block it is one. These multiplicities involve smaller
trees than $R$, so they are already justified by the simultaneous
induction. Choosing the cuts and choosing a preimage for each block
reconstructs $(B_1,B_2)$ uniquely from the seed, then each $B_j$ uniquely
from its later block. Conversely every source list gives those cuts.
This proves a bijection, not merely a count bound.

### Step 3. Evaluated all-target fibres and their maximum

Define $h(e)=1$. For nonleaf $R$, write its unique left-spine list as

$$\operatorname{LS}(R)=e^{a_0}D_1e^{a_1}D_2\cdots D_re^{a_r},$$

where all $D_j$ are nonleaves and $a_i\ge0$. If $r=0$, let
$s=a_0\ge1$ and set $h(R)=2^{s-1}$. If $r\ge1$ and either an
internal gap $a_i$ ($1\le i<r$) is zero or one $h(D_j)$ is zero,
set $h(R)=0$. Otherwise set

$$h(R)=2^E\prod_{j=1}^r h(D_j),\qquad
E=\max(a_0-1,0)+\sum_{i=1}^{r-1}(a_i-1)+\max(a_r-1,0).\tag{2}$$

The block bijection proves $p(R)=h(R)$. For an all-leaf list of length
$s$, all compositions of $s$ give the cuts, in number $2^{s-1}$.
For an internal gap $a_i$, its last $k\ge1$ leaves must belong to
the following nonleaf block. The remaining $a_i-k$ leaves are cut
into all-leaf blocks, with one choice for length zero and
$2^{a_i-k-1}$ otherwise. Summing gives $2^{a_i-1}$, and gives
zero if $a_i=0$. At the beginning, the first nonleaf block may itself
be the seed (one choice), or a later block with at least one leading
leaf after a nonempty composition. This sum is one for $a_0=0$ and
$2^{a_0-1}$ otherwise. The final gap is an unrestricted composition,
giving one for $a_r=0$ and $2^{a_r-1}$ otherwise. These choices are
independent and give exactly (2).

Thus, for every polygon target $Y$,

$$|F^{-1}(Y)|=\begin{cases}
h(R),&Y=(\operatorname{LC}_l,R),\ l\ge1,\\
0,&\text{otherwise}.
\end{cases}\tag{3}$$

The formula includes unreachable targets, the comb boundary and all
singular zero factors. It also gives an explicit predecessor decoder
through its block cuts, rather than a search over candidate sources.

To prove sharpness, let $q(R)$ be the number of internal vertices.
For any nonleaf with $h(R)>0$, induction in (2) gives

$$h(R)\le2^{q(R)-1},$$

with equality only for a left comb. In fact, a left comb is the $r=0$
case, which gives equality. For $r\ge1$, put $A=\sum a_i$ and let
$b$ be the number of nonempty boundary runs $a_0,a_r$. The exponent
in (2), including the inductive exponents from $D_j$, is at most

$$A-b-r+1+\sum_j(q(D_j)-1)
 =q(R)-3r+1-b\le q(R)-2,$$

since $q(R)=A+r+\sum_jq(D_j)$. This is strictly below $q(R)-1$.
For a target with $m\ge3$ internal vertices, (3) now gives at most
$2^{m-2}$, with equality only if $l=1$ and
$R=\operatorname{LC}_m$. Its triangulation is precisely the fan at
vertex $1$. For $m=1$ there is one state, and for $m=2$ both states
have one preimage by (3). These prove the claimed maxima and every
equality case.

### Step 4. Image enumeration, with static credit deducted

Let $H(z)$ count trees $R$ with $h(R)>0$ by internal vertices, including
the leaf. Their left-spine branches are leaves of weight $z$ and
nonleaf branches of weight $z(H-1)$, with no two consecutive nonleaf
branches and with the same condition recursively inside each branch.
For atoms of weights $A,B$, respectively, all sequences with no
consecutive $B$ have series $(1+B)/(1-A-AB)$: write such a sequence
as an optional initial $B$ followed by a sequence of units $A$ or $AB$.
Therefore

$$H=\frac{1+z(H-1)}{1-z-z^2(H-1)},\qquad
(1-z)^2H=1-z+z^2H^2.$$

Let $C(w)$ be the unique series with constant coefficient one satisfying
$C=1+wC^2$. Direct substitution yields

$$H(z)=\frac1{1-z}C\!\left(\frac{z^2}{(1-z)^3}\right),\qquad
I(z)=1+\frac{z}{(1-z)^2}C\!\left(\frac{z^2}{(1-z)^3}\right),\tag{4}$$

where $I$ counts the full $F$ image with the formal leaf included.
For internal size $m\ge1$ the coefficient is

$$[z^m]I(z)=\sum_{k=0}^{\lfloor(m-1)/2\rfloor}
C_k\binom{m+k}{3k+1}.$$

The first values are $1,1,2,4,9,22,57,154,429$ including size zero.
Their coincidence with the old avoidance sequence does not identify
the literal image under the standard Dyck-word bijection. That earlier
identification is false, with preserved counterexample in the initial
follow-up record. No novelty credit is assigned to an old count.

### Step 5. The size-reducing temporal mechanism

For any $B$, write $G(B)=(\operatorname{LC}_l,Q)$ in its unique form.
If $B=e$ define $K(e)=e$. If $B\ne e$ then $l\ge2$ and applying
(1) once more gives

$$G^2(B)=(c,K(B)),\qquad
K(B)=\iota(G(Q),\operatorname{LC}_{l-1}).\tag{5}$$

To verify the displayed formula, note for every $a\ge2$ that

$$G(\operatorname{LC}_a,R)
 =(c,\iota(G(R),\operatorname{LC}_{a-1})).\tag{6}$$

For $a=2$, its product is $F(e,R)=G(R)$, and for $a>2$ the preceding
all-leaf product is $\operatorname{LC}_{a-1}$; this gives (6) from (1).
For $B=e$, $G^2(e)=G(c)=\operatorname{LC}_3=(c,e)$ also satisfies (5).

The map $K$ preserves the number of leaves. Two intertwining identities
are

$$KG=GK,\qquad K(c,R)=(c,K(R)).\tag{7}$$

For the first, evaluate $G^3(B)$ as $G(G^2(B))$ and $G^2(G(B))$,
using $G(c,S)=(c,G(S))$, the $a=2$ case of (6), and cancel the
common left child $c$. For the second, apply this same identity twice
to $G^2(c,R)$, or substitute $a=2$ into (5)--(6).

Define a class $\mathcal C_N$ of trees with $N$ leaves: for $N\ge3$
these are $(\operatorname{LC}_a,R)$ with $a\ge2$, and set
$\mathcal C_1=\{e\}$, $\mathcal C_2=\{c\}$ as boundary classes.
For any tree $T$ with $N\ge3$ leaves, $K(T)\in\mathcal C_N$.
To check this directly in (5), write $G(Q)=(\operatorname{LC}_b,S)$.
If $Q$ is nonleaf then $b\ge2$, and substitution gives root left
comb size $b+l-2\ge2$. If $Q=e$, then $b=1$ and the left size is
$l-1$; the case $l=2$ would force $N=2$, so $N\ge3$ gives $l\ge3$.

More strongly, for $T\in\mathcal C_N$, $N\ge3$,

$$K(T)\in\{(c,S):S\in\mathcal C_{N-2}\}.\tag{8}$$

For $N=3$ the only such tree is $\operatorname{LC}_3=(c,e)$,
which (5) fixes. For $N\ge4$, write $T=(\operatorname{LC}_a,R)$,
$a\ge2$, and $D=\iota(G(R),\operatorname{LC}_{a-1})$.
Equation (6) says $G(T)=(c,D)$, so $K(T)=G(D)$.
Here $D\in\mathcal C_{N-1}$: if $R=e$ it is
$\operatorname{LC}_a$ with $a=N-1\ge3$; if $R$ is nonleaf,
$G(R)$ has a nonleaf left comb and the substitution cannot shorten it.
Thus (6) applied to $D$ writes $G(D)=(c,S)$, where $S$ is a
substitution of the same form. Its root left comb is nonleaf whenever
its size is at least three, by the preceding two-case argument; at
sizes one and two it is $e$ or $c$. This proves (8).

Put $Z_1=e$, $Z_2=c$, and $Z_N=(c,Z_{N-2})$ for $N\ge3$.
These are fixed by $K$ by (7). In (8) one application of $K$ freezes
the first cherry, after which (7) applies $K$ only to the remaining
$N-2$ leaves. Induction gives, for $N\ge2$, entrance to $Z_N$ from
$\mathcal C_N$ in at most

$$d_C(N)=\left\lfloor\frac{N-2}{2}\right\rfloor$$

steps, with the size-three base already fixed. Every arbitrary tree
enters $\mathcal C_N$ after one $K$ step, so for $N\ge3$ its
entrance time to $Z_N$ is at most $\lfloor N/2\rfloor$.
The size-one and size-two arbitrary classes are already fixed.
Consequently $K$ has exactly one recurrent state at each size.

### Step 6. Translate the clock back to OFS

Equation (1) implies the two exact square identities

$$F^2(e,R)=(e,K(R)),\qquad
F^2(T)=K(T)\quad\text{if the left child of }T\text{ is nonleaf}.\tag{9}$$

For the first, write $G(R)=(\operatorname{LC}_l,Q)$ and use the
same product as in (5). For the second, if $P=P(\operatorname{LS}(T))$
then $F(T)=(e,P)$ and $G(T)=(c,P)$; hence both $F^2(T)$ and $K(T)$
equal $G(P)$. The second identity does not require $T\in\mathcal C_N$.

One also has

$$G(Z_j)=Z_{j+1},\qquad F(Z_N)=(e,Z_{N-1})\quad(N\ge3).\tag{10}$$

The first follows from the bases $G(e)=c$, $G(c)=(c,e)$ and
$G(c,S)=(c,G(S))$. The second follows from (1), since the product
for $(c,Z_{N-2})$ is $G(Z_{N-2})=Z_{N-1}$. Thus for $N\ge3$
the two distinct trees $Z_N$ and $(e,Z_{N-1})$ are exchanged by $F$.

Every first image is either $(e,R)$ or in $\mathcal C_N$. From an
image of the latter kind, (9) gives entrance to $Z_N$ in at most
$2d_C(N)\le N-2$ steps. From $(e,R)$ the even iterates are
$(e,K^t(R))$. The odd iterates are $GK^t(R)=K^tG(R)$ by (7),
and $G(R)\in\mathcal C_N$ when $N\ge3$. Hence, for $N\ge4$,
the two available bounds have minimum

$$\min\left\{2\left\lfloor\frac{N-1}{2}\right\rfloor,
1+2\left\lfloor\frac{N-2}{2}\right\rfloor\right\}=N-2.$$

The small sizes use the already fixed $K$ boundary classes directly.
Thus every $F$ orbit at size $N\ge4$ reaches the displayed two-cycle
within $N-1=n-2$ steps, including its first image step. This proves
that no additional periodic component exists. At $N=3$ the entire
carrier consists of the two displayed states, and at $N=2$ it is the
single fixed cherry.

### Step 7. Sharp witnesses

Let $T^*_3=(e,c)$ be the three-leaf right comb and set
$T^*_N=(T^*_{N-1},e)$ for $N\ge4$. These trees have a nonleaf left
child for $N\ge4$, but need not lie in $\mathcal C_N$; this is why
the full second clause of (9) is required.
The product definition gives

$$F(T^*_N)=(e,T^*_{N-1})\quad(N\ge4),$$

because $\operatorname{LS}(T^*_N)=[c,e,\ldots,e]$, its seed is
$F(c,e)=(e,c)=T^*_3$, and each subsequent $G(e)=c$ appends one
right leaf. Therefore

$$K(T^*_4)=\operatorname{LC}_4,\qquad
K(T^*_N)=(c,T^*_{N-2})\quad(N\ge5).\tag{11}$$

Indeed $K(T^*_N)=G(T^*_{N-1})$ by (9), and the last line of (1)
and the just-computed product give (11). Also
$G(T^*_3)=\operatorname{LC}_4$ by the fourth line of (1).

Write $J(S)=(c,S)$ and let $J^r$ denote iteration. For even
$N=2k\ge4$, (7), (9) and (11) yield

$$F^{N-2}(T^*_N)=K^{k-1}(T^*_N)=J^{k-2}(\operatorname{LC}_4).$$

This is in the nonleaf-left phase but differs from $Z_N=J^{k-1}(c)$,
since $\operatorname{LC}_4\ne(c,c)$. For odd $N=2k+1\ge5$,
the same identities give

$$K^{k-1}(T^*_N)=J^{k-1}(T^*_3),\qquad
F^{N-2}(T^*_N)=(e,J^{k-2}(\operatorname{LC}_4)).$$

The second equality uses $F(c,S)=(e,G(S))$ and
$G(c,S)=(c,G(S))$. It is in the leaf-left phase but differs from
$(e,Z_{N-1})$ by the same four-leaf-tail comparison.
Thus the witness is still outside the core at time $N-2$; Step 6
puts it inside by time $N-1$. Its height is exactly $N-1=n-2$,
which proves sharpness for every $n\ge5$.

## Corrections and open risks

- The original guesses identifying the image with standard-word
  $UUDU$ avoidance and a naive left-edge fibre exponent were false.
  Their original declarations and actual counterexamples remain unchanged.
  Equations (2)--(4) are a new, explicitly derived literal description.
- This proof does not claim a novel enumeration of the old integer
  sequence, or exclusion of every rotation/sorting composite adapter.
  The admission already deducts those mechanisms; the manuscript must
  maintain the same deductions.
- Both named workers are proof contributors. Bounded author verification
  is separate from this all-size proof and is not an independent review.
- The protected-cell dictionary and the exact $K$ closure are substantive
  lemmas requiring particular pressure in an eventual nonauthor gate.
  This author proof does not establish manuscript-review acceptance or
  authorize external release.
