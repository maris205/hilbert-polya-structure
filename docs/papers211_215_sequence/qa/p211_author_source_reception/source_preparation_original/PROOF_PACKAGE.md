# P211 self-contained proof package

## Claim and status

**PROVABLE AS STATED.** The four admitted claims remain unchanged; this
is an author-written self-contained presentation, not a new proof repair,
new theorem, finite execution, or independent review.

1. Exact first image: for $g=f_{Z,W}$, $g\in T(O_n)$ iff
   $w_i\le z_i<w_{i+1}$ for $i<k$ and $w_k=z_k=n$.
2. In the image, persistent equal endpoint/value pairs separate strict
   alternating lists. An update deletes their first and last endpoints.
   If $R(g)$ is the largest number of strict pairs in such a list, then
   the exact remaining entrance time is $R(g)$.
3. Fixed and recurrent states are exactly $e_C$ with $n\in C$. The terminal
   state of $f_{Y,X}$ is $e_{X\cap(Y\cup\{n\})}$. Fixed sources have time
   zero; every other source has time $1+R(T(f))$. The maximum is $H_1=0$
   and $H_n=\lceil n/2\rceil$ for $n\ge2$.
4. Off-image targets have zero predecessors. For an image target, put
   $z_0=0$, $d_i=w_i-z_{i-1}-1$ and
   $$P_d(u)=\sum_{a,b\ge0,\ a+b\le d}\binom d{a+b}u^{b-a}.$$
   Ordered gap-colour choices give all predecessors uniquely, with count
   $$|T^{-1}(g)|=([u^0]+[u^1])\prod_i P_{d_i}(u).$$

## Assumptions and notation

Let $n\ge1$ and $[n]=\{1,\ldots,n\}$. The carrier $O_n$ consists of
all nondecreasing functions $[n]\to[n]$, with no top-fixing or extensive
restriction on the source. For $X=\{x_1<\cdots<x_r=n\}$ and
$Y=\{y_1<\cdots<y_r\}$, let $x_0=0$ and
$$f_{Y,X}(i)=y_j\quad\text{if }x_{j-1}<i\le x_j.$$
Thus $X$ is the set of right kernel endpoints, $Y$ is the image, and
these two sets uniquely describe every carrier element. For $S\subseteq[n]$
containing $n$, define $e_S(i)=\min\{s\in S:s\ge i\}$. Put
$A=Y\cup\{n\}$ and define the autonomous operation
$$T(f_{Y,X})=e_X\circ e_A.$$
The right factor acts first; supports are recomputed after each step.
The entrance time is the first time an orbit reaches a fixed state.
A recurrent state means a whole-function state on a cycle of $T$.

For an image target $g=f_{Z,W}$, equal pairs $(c,c)$ are anchors. A strict
list between successive anchors (also before the first anchor) is
$w_1<z_1<\cdots<w_r<z_r<c$. The final pair $(n,n)$ is always an
anchor. Set $R(g)$ to the largest such $r$, or zero if all lists are empty.
The coefficient notation $[u^j]$ permits negative exponents.

## Strategy and dependency map

1. Direct composition of ceiling blocks proves the product lemma, the
   image iff criterion and the exact common-anchor identity.
2. Recomputing the two supports on the first image explicitly swaps the
   endpoint roles and removes two outside labels from each strict list.
   Induction gives exact pointwise time and recurrent/terminal structure.
3. The label budget gives the upper clock bound; separate odd/even sources
   attain it, with the initial normalization and $n=1$ checked explicitly.
4. Reverse the product using forced endpoints and forbidden intervals.
   Independent free-gap choices and the published zero/one rank branches
   give the full source decoder and its finite binomial/Laurent count.
   This branch uses no temporal theorem or numerical enumeration.

## Published primitives: zero contribution credit

The carrier coordinates, ceiling projections, completed-image support,
and unique support-pair reconstruction with $|A|-|X|\in\{0,1\}$ are
published in Stein, *Semigroup Forum* 111 (2025), Section 5.1, especially
the paragraph after Lemma 5.12 (DOI 10.1007/s00233-025-10595-2).
The rank branch in Step 4 below is an explicit use of that known fact,
not a new theorem. Static idempotent-product criteria in Andrenšek
arXiv:2604.15497v1 Section 4 and v3 Theorem 3.6, order duality and
plain deletion budgets likewise receive zero independent contribution
credit. The retained scope is the exact recomputed dynamics and
labelled-target gap factorization. See SOURCE_AUDIT.md for distinct
versions and actual primary read boundaries.

## Proof


### 1. The product of two ceiling projections

Take any $X,A\subseteq[n]$ containing $n$. For $z\in e_X(A)$, define
$$B_z=\{a\in A:e_X(a)=z\},\qquad w_z=\max B_z.$$
Each $B_z$ is a nonempty interval in the ordered set $A$. The value of
$e_Xe_A$ is $z$ on exactly the union of the consecutive $e_A$-blocks
indexed by $B_z$. Its rightmost domain point is $w_z$. Thus the image
values are $Z=e_X(A)$ and the kernel endpoints are
$W=\{w_z:z\in Z\}$. In increasing order they satisfy $w_i\le z_i$.
For the next distinct value, every $a\in B_{z_{i+1}}$ is greater than
$z_i$: an $a\le z_i$ would have $e_X(a)\le z_i$ because $z_i\in X$.
Therefore $z_i<w_{i+1}$. Finally $n\in X\cap A$ gives $w_k=z_k=n$.

Moreover,
$$W\subseteq A,\quad Z\subseteq X,\quad W\cap Z=X\cap A.$$
For the nontrivial inclusion, if $c\in X\cap A$, then $e_X(c)=c$.
No $a>c$ maps to $c$, while $c$ itself belongs to $B_c$, so $w_c=c$.
Consequently $c$ belongs to both $W$ and $Z$; the reverse inclusion follows
from the two containments.

Conversely, suppose $W,Z$ satisfy the image condition. Use the valid
source $f=f_{W,Z}$, whose kernel endpoints are $Z$ and image is $W$.
Both sets contain $n$ and have $k$ elements. For each $i$,
$z_{i-1}<w_i\le z_i$ (with $z_0=0$), so $e_Z(w_i)=z_i$.
No two $w_i$ collapse under this projection, and therefore
$T(f)=e_Ze_W=f_{Z,W}=g$. This proves necessity and sufficiency on the
full $O_n$, without restricting the source to be extensive.

### 2. Exact endpoint peeling on the first image

For an image state $g=f_{Z,W}$, the input to the next product is now
$X=W$, $A=Z$ because $n\in Z$. Lemma 1 shows that common endpoints
$C=W\cap Z$ persist exactly. In particular $n$ is an anchor, so every
strict-pair list ends at an anchor.

Consider one such list before an anchor $c$:
$$w_1<z_1<w_2<z_2<\cdots<w_r<z_r<c.$$
The preceding anchor, when it exists, is smaller than all these labels.
For $i<r$, the least member of $W$ not below $z_i$ is $w_{i+1}$.
Both $z_r$ and $c$ have ceiling $c$ in $W$. Thus after recomputing
rightmost kernel endpoints, the next strict pairs are exactly
$$ (z_1,w_2),\ (z_2,w_3),\ldots,\ (z_{r-1},w_r),$$
followed by the unchanged pair $(c,c)$. If $r=1$, there are no strict
pairs left; if $r=0$, the anchor is unchanged. This is precisely deletion
of the first and last symbols of the increasing $2r$-endpoint list.
The lists evolve independently because the common anchor belongs to both
projection sets and separates their ceiling intervals.

Induction therefore leaves the middle $2\max(r-t,0)$ labels of each
initial list after $t$ updates, alternating the endpoint roles at every
step. It reaches its anchor-only state at exactly time $r$. A nonempty
strict list changes at that step because two distinct endpoints disappear.
Taking the largest list proves the pointwise time $R(g)$.

An anchor-only state has $W=Z=C$ and is $e_C$, which is fixed directly
from the literal definition. Every orbit enters the image after one step
and then loses all strict lists. Hence every recurrent state is one of
these fixed states. For a source $f=f_{Y,X}$, Lemma 1 gives its first-image
anchor set $X\cap(Y\cup\{n\})$; this proves the stated terminal map.
For a nonfixed source, first-image entry plus its exact remaining time
gives $1+R(Tf)$. Fixed sources have time zero separately.

### 3. Sharp height on the full carrier

A strict list of length $r$ uses $2r$ distinct labels below its next
anchor. Since there are only $n$ labels altogether,
$r\le\lfloor(n-1)/2\rfloor$. The preceding formula gives
$H_n\le1+\lfloor(n-1)/2\rfloor=\lceil n/2\rceil$ for $n\ge2$.

For odd $n=2m+1\ge3$, choose
$$X=\{2,4,\ldots,2m,n\},\qquad
  Y=\{1,3,\ldots,2m-1,n\}.$$
This is a valid source with $|X|=|Y|=m+1$. Its first image has the $m$
strict pairs $(1,2),(3,4),\ldots,(2m-1,2m)$ followed by $(n,n)$.
Its remaining time is $m$. The source is not fixed, since $f(1)=1$
but $T(f)(1)=2$, so its full time is $m+1=\lceil n/2\rceil$.

For even $n=2m\ge2$, choose
$$X=\{2,4,\ldots,2m\},\qquad
  Y=\{1,3,\ldots,2m-1\}.$$
Here the actual definition adds $n$ to $Y$ for the second projection.
The first image has $m-1$ strict pairs
$(1,2),\ldots,(2m-3,2m-2)$ and the anchor $(n,n)$.
Again $f(1)=1$ while $T(f)(1)=2$, so the time is $m$.
This includes $m=1$, where the first image is already the constant map
with value two. At $n=1$ there is only one function and it is fixed.

### 4. Every-target inverse construction

Let $g=f_{Z,W}$ be an image state with $k$ pairs, and put $z_0=0$.
In any source $f=f_{Y,X}$, write $A=Y\cup\{n\}$. Lemma 1 forces
$z_i\in X$ and $w_i\in A$ for every $i$. If $w_i<z_i$, it also forces
$$X\cap[w_i,z_i)=\varnothing,\qquad
  A\cap(w_i,z_i]=\varnothing.$$
The first prohibition is needed for $e_X(w_i)=z_i$. For the second,
any extra $a\in A$ with $w_i<a\le z_i$ would also have ceiling $z_i$,
contradicting the maximality of $w_i$ in $B_{z_i}$.

The only remaining sites lie in the free intervals
$$D_i=\{z_{i-1}+1,\ldots,w_i-1\},\qquad |D_i|=d_i.$$
Each selected site here is in $X\setminus A$ or $A\setminus X$, not
both. A common site would produce an extra common anchor, contradicting
$W\cap Z=X\cap A$. In this free interval, every chosen $X$-site must
precede every chosen $A$-site. Indeed, an $A$-site $a$ at or before an
$X$-site $x$ in $D_i$ would satisfy $e_X(a)\le x<z_i$, yielding an
extra output value strictly between $z_{i-1}$ and $z_i$.

These conditions are also sufficient. Choose any number $a_i$ of
$X$-sites and $b_i$ of $A$-sites in $D_i$, with all $X$-sites first;
all remaining sites are in neither set. Include the forced $z_i$ in
$X$, the forced $w_i$ in $A$, and no other sites in the forbidden
intervals. Every $A$-site in $(z_{i-1},w_i]$ then has ceiling exactly
$z_i$ in $X$, with the last such site $w_i$. The resulting product is
therefore exactly $g$.

For fixed $a_i,b_i$ there are $\binom{d_i}{a_i+b_i}$ choices: choose
the selected locations, mark their first $a_i$ as $X$ and their last
$b_i$ as $A$. This creates no duplicated descriptions.

The forced endpoints contribute equally many members to $X$ and $A$,
even when $w_i=z_i$. Consequently
$$|A|-|X|=\sum_i(b_i-a_i).$$
There are exactly two admissible rank-balance branches. If this difference
is zero, set $Y=A$. If it is one, set $Y=A\setminus\{n\}$.
In both cases $|X|=|Y|\ge1$, so there is exactly one valid $f_{Y,X}$.
In the second branch $|A|=|X|+1\ge2$, ensuring $Y$ is nonempty.
No other difference can come from a source of the full carrier, because
$A=Y\cup\{n\}$ and $|Y|=|X|$.

Thus the independent gap choices and the two rank branches reconstruct
all and only the source functions, uniquely. Their Laurent weight is
$u^{|A|-|X|}$, giving precisely
$$|T^{-1}(g)|=([u^0]+[u^1])\prod_i P_{d_i}(u).\qquad\square$$


## Corrections and boundary checks

No admitted formula was weakened or enlarged. The earlier informal
one-ended-erasure phrase is not used: Step 2 removes two endpoint labels.
The fixed-source zero time is separated from the initial normalization.
The even witness uses the actual completed image, including the case
$n=2$. In the rank-one-difference inverse branch, $|A|\ge2$ prevents an
empty reconstructed image. Empty gaps and $n=1$ are covered by $P_0=1$.

## Open risks and excluded claims

No global maximum fibre or maximizer, basin census, all-time inverse,
priority or universal no-factor/no-lift theorem is claimed. The labelled
peeling description is not by itself a whole-carrier equivalence to an
old system, nor is it evidence that no such transfer could exist.
The separately accepted candidate gate is not a manuscript review.

The original exploratory pilot's strict prelock failure remains immutable
and ineligible for a strict replay. The paper-local verifier has not yet
been run and its canonical does not yet exist. Its later finite checks
cannot establish these all-size proofs. Current author/source preparation
must be followed by the actual project A/B and artifact obligations.

