# KIP: exact author deduction and negative mechanism boundary

Author/proof contributor: `/root/round211_queue_scout`, 2026-09-08 UTC.
No computation, independent review or admission accompanies these proofs.

## Claim, status, assumptions and notation

Assume $n\ge1$ and use the full carrier and literal $T$ of `INTAKE.md`.
Write $f=f_{Y,X}$ for the unique nondecreasing function whose increasing
kernel-block endpoints are $X=\{x_1<\cdots<x_r=n\}$ and whose corresponding
values are $Y=\{y_1<\cdots<y_r\}$. Thus $f(i)=y_j$ for
$x_{j-1}<i\le x_j$, with $x_0=0$. Put $A=Y\cup\{n\}$.

The following are **PROVABLE AS STATED**, as author deductions:

1. A target $g=f_{Z,W}$ is in the image of $T$ exactly when its endpoint
   lists have equal length $k\ge1$ and satisfy
   $$w_i\le z_i<w_{i+1}\quad(1\le i<k),\qquad w_k=z_k=n.$$
2. On this image, every pair with $w_i=z_i$ is a permanent common anchor.
   Before the first anchor and between successive anchors, a list of $r$
   strict pairs evolves by deleting its first and last endpoints, leaving
   $r-1$ strict pairs; empty lists remain empty. The pointwise entrance time
   of $g$ is the largest such $r$, denoted $R(g)$.
3. The fixed/recurrent states are exactly $e_C$ for $n\in C\subseteq[n]$.
   Every $f=f_{Y,X}$ ends at $e_{X\cap A}$. If $f$ is not one of these fixed
   states then its entrance time is $1+R(Tf)$. The maximum on $O_n$ is
   $$H_n=\begin{cases}0,&n=1,\\ \lceil n/2\rceil,&n\ge2.\end{cases}$$
4. Every target outside the displayed image has zero predecessors. For an
   image target, set $z_0=0$ and $d_i=w_i-z_{i-1}-1\ge0$. Define the finite
   Laurent polynomial
   $$P_d(u)=\sum_{\substack{a,b\ge0\\a+b\le d}}
                 \binom d{a+b}u^{b-a}.$$
   Then the complete one-step fibre has size
   $$|T^{-1}(g)|=([u^0]+[u^1])\prod_{i=1}^kP_{d_i}(u).$$
   The proof gives every source, not only its count.

There is **no** global maximum-fibre claim, fibre maximizer classification,
basin-size census, finite-check PASS, independent correctness certificate,
or global novelty claim.

## Strategy and dependency map

The endpoint-pair parametrization and ceiling projections are established
semigroup coordinates; here their definitions suffice for a direct proof.
One projection-product calculation gives the image and the common anchors.
On the image, alternating endpoint lists give the entire temporal rule.
An independent reversal of the same one-step product gives all inverse
sources as ordered colours in target-local gaps, followed by a rank-balance
coefficient extraction.

1. Endpoint pairs and ceiling composition imply Lemma 1 (image and anchors).
2. Lemma 1 plus an explicit update of a strict list imply the pointwise clock.
3. Counting two distinct endpoints per strict pair and explicit witnesses
   imply the sharp all-carrier bound, including the first normalization.
4. The target switch locations force two colours in each free gap;
   global equality $|X|=|Y|$ gives the inverse formula. This last proof
   does not use the clock or a finite enumeration.

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

## Exact subtraction and unresolved stronger directions

The ceiling/projection and endpoint-pair objects are directly published;
no credit is assigned to naming them as kernel/image feedback. Nor does
noncommutativity by itself provide an advance: for $X=\{1,3\}$ and
$A=\{2,3\}$ the two ceiling products differ, but both are still the
ordinary canonical projections used above.

More decisively, after the first normalization the **entire labelled
temporal map**, not just a bound, has the above anchored-list peeling
description. Its time is merely the maximum half-length; the full-carrier
ceiling is one extra normalization step plus the same count. P190's
good-run formula and the older erasure literature already make generic
support/run erosion zero-credit. This is a proof-mechanism subtraction,
**not** a claim that KIP is literally P190 or conjugate to its whole
cyclic Brandt carrier. The parity obstruction of P190 is not imported.

The inverse proof is separate logically from the time proof, but it is
entirely the two-ceiling-product factorization into ordered gap colours and
the source rank balance. The displayed coefficient is not an evaluated
global fibre extremum. Neither this inverse nor a future extremum restores
an independent temporal contribution already removed by the exact peeling
adapter. The author disposition is therefore `NO_PROMOTION`, with no pilot
and no manuscript proposed. This is not a mathematical impossibility result
for other natural finite semigroup systems.

## Development correction and open risks

A preliminary message described the likely erosion as "one-ended" before
the image calculation was completed. The proved update above removes the
first and last endpoints of each strict list. The parameter $r$ drops by
one, but this does **not** mean a single endpoint is removed. The earlier
informal phrase is superseded explicitly, not used in any proof or check.

Direct ownership of this literal $T$ has not been excluded globally.
No independent review has checked these author proofs. No source article
is credited with the new time or inverse formulas merely because it
provides the coordinates. All stronger claims excluded above stay unproved.
