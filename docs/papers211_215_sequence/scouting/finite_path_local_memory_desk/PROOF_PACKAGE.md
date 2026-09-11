# Reflected M1 negative-control proof

Author: `round211_rational_scout`, 2026-09-08 UTC.

## Claim and status

**PROVABLE AS STATED — author proof only; NO_PROMOTION.**
For the precisely defined finite-path control below, every state has exact
period $4n$, with $2^{n-1}$ cycles and one preimage per target. Its complete
left-end return map is identity. The global dynamics are conjugate to one
fixed cyclic phase times a binary memory label. The inverse remains trivial
under the restrictions, factors and returns specified in Step 5.

This is a finite boundary instance of the published M1 swap-memory
primitive, not a fresh qualifying literal. The source subtraction and the
acknowledged discovery-access limitation are in [REPORT.md](REPORT.md).

## Assumptions and notation

Let $n\ge1$ be an integer and let

$$
X_n=\{1,\ldots,n\}\times\{-1,+1\}\times\{-1,+1\}^n.
$$

A state $(p,d,a)$ has hand position $p$, hand direction $d$, and site
memory $a=(a_1,\ldots,a_n)$. All these coordinates are independent; no
alignment or boundary restriction is imposed on the carrier. A step is
one unit of the autonomous map defined next, including a wall interaction.
The symbols $+$ and $-$ in words abbreviate $+1$ and $-1$.

Define the reflected hand step $B$ by leaving $a$ unchanged and setting

$$
B(p,d,a)=
\begin{cases}
(p+d,d,a),&1\le p+d\le n,\\
(p,-d,a),&p+d\notin\{1,\ldots,n\}.
\end{cases}
$$

Thus an outward wall step reflects in place; it does not move immediately
to the adjacent interior site. Define $C$ to swap $d$ and $a_p$ without
changing position or the other memories. The update is

$$T=C\circ B.$$

The swap is applied at the position **after** $B$, including when $B$ was
an in-place reflection. Every operation remains in $X_n$. No random clock,
external scheduler, clipping, erasure or quotient state is implicit.

Call $(p,d,a)$ aligned when $a_p=d$. Define the section

$$S=\{(1,+,(+,b_2,\ldots,b_n)):b_j\in\{-,+\}\}.$$

For $n=1$, the suffix is the empty word and $|S|=1$.

## Strategy and dependency map

1. $B$ is a cycle on the hand states and $C$ is an involution: this gives
   an explicit inverse on the full carrier.
2. An aligned hand advances one site in its current direction in one or
   three steps, exchanging the two site memories; an outward wall turn
   takes exactly two steps.
3. A complete outward-and-back sweep from $S$ restores every memory. Its
   exact length is $4n$, independent of the suffix.
4. No intermediate state belongs to $S$. The resulting distinct cycles
   account for all of $X_n$, proving exact periods and the conjugacy.
5. Elementary permutation arguments show why restrictions, factors and
   first returns cannot manufacture a nontrivial inverse axis.

## Proof

### Step 1. Exact inverse and singleton fibres

On the $2n$ hand states, $B$ follows the cycle

$$
(1,+),(2,+),\ldots,(n,+),(n,-),(n-1,-),\ldots,(1,-).
$$

For $n=1$ this is the two-cycle $(1,+),(1,-)$. Hence $B$ is a permutation
on the whole carrier. Since $C^2$ is identity, $C$ is also a permutation.
Consequently

$$T^{-1}=B^{-1}\circ C.$$

This is an evaluated decoder for every target $(p,d,a)$: exchange $d$ and
$a_p$, then take the immediately preceding hand state in the displayed
$2n$-cycle, leaving the now updated memories unchanged. It produces exactly
one source, with no branch or feasibility condition. Thus the image is all
of $X_n$ and every target fibre is one.

If the order is reversed to $\widetilde T=B\circ C$, then
$C\circ T\circ C=\widetilde T$ because $C^2$ is identity. The two complete
finite maps are therefore conjugate by the site/hand swap itself.

### Step 2. The two local propagation cases and a wall turn

Start aligned at site $p$ with direction $d$, and suppose $q=p+d$ is a
site in the path. The only memories involved in reaching the next aligned
state are those at $p$ and $q$.

If $a_q=d$, one application of $T$ moves to $q$ and exchanges equal
directions. The result is aligned at $q$ with direction $d$ and both
memories still $d$.

If $a_q=-d$, the three successive states, writing only position, hand
direction and the pair $(a_p,a_q)$, are

$$
\begin{aligned}
(p,d;(d,-d))
&\longmapsto(q,-d;(d,d))\\
&\longmapsto(p,d;(-d,d))\\
&\longmapsto(q,d;(-d,d)).
\end{aligned}
$$

Both intermediate states are unaligned; the last is aligned. All three
moves are along the same interior edge, so the calculation also applies
when either endpoint of that edge is a path endpoint. In both cases the
net effect is to move the aligned hand from $p$ to $q$ and swap the old
site memories. The time is one for agreement and three for disagreement.

At an endpoint with outward direction $d$ and $a_p=d$, the first wall
step reflects the hand and then swaps, producing hand $d$ and site
memory $-d$ at the same position. That state is unaligned and its hand is
still outward. The second wall step reflects and swaps equal signs,
producing hand $-d$ and site memory $-d$. This is the first aligned state
after the turn. Thus an aligned outward turn takes exactly two steps and
reverses both hand and endpoint memory.

### Step 3. The exact return from every left-end seed

For now let $n\ge2$ and take the seed

$$s_b=(1,+,(+,b_2,\ldots,b_n))\in S.$$

Let $L$ and $R$ be the numbers of minus and plus signs in the suffix
$(b_2,\ldots,b_n)$, so $L+R=n-1$.

Repeatedly applying the interior propagation calculation in Step 2 moves
the aligned plus hand from site $1$ to site $n$. Since its site memory is
swapped with the next memory at every aligned advance, the endpoint state
is hand plus and tape

$$ (b_2,b_3,\ldots,b_n,+). $$

The time for this sweep is $(n-1)+2L$. Each originally negative suffix
symbol costs three steps, and each positive symbol costs one.

The two-step right wall turn gives tape $(b_2,\ldots,b_n,-)$ and an
aligned minus hand at $n$. The return sweep carries that minus sign left,
swapping it with the other memories in reverse order. Its final tape is
$(-,b_2,\ldots,b_n)$, and its time is $(n-1)+2R$: now the positive suffix
symbols are the disagreements. The two-step left wall turn restores
$s_b$. The total is exactly

$$
[(n-1)+2L]+2+[(n-1)+2R]+2=4n.
$$

There is no visit to $S$ at an intermediate time. During the outward
aligned sweep the positions are $2,\ldots,n$ after the seed; during the
return aligned sweep the hand has direction minus. The only other aligned
states are the right-wall post-turn state and the final left-wall state.
All microstates between successive aligned states in Step 2 are
unaligned. Therefore the displayed return is the **first** positive return
to $S$, and it returns to the identical suffix $b$.

When $n=1$, position is fixed and direct application of the two definitions
gives $T(d,a_1)=(a_1,-d)$ and $T^2(d,a_1)=(-d,-a_1)$. Hence $T^4$ is
identity and $T^2$ has no fixed state. Since any period under $T^4$ must
divide four, all four states have exact period four. The unique seed in
$S$ consequently has first return four and is restored. This is the same
$4n$ law; it is a symbolic boundary calculation, not a program run.

### Step 4. Full-carrier classification and conjugacy

Each of the $2^{n-1}$ seeds in $S$ has a cycle of exact length $4n$:
any shorter period would give an earlier return to $S$. Two distinct
seeds cannot lie in the same cycle, because then a forward traversal from
one seed would encounter another section point before returning to itself,
contrary to Step 3. Their disjoint cycles contain

$$4n\,2^{n-1}=n\,2^{n+1}=|X_n|$$

states. They exhaust the full carrier, including every initially unaligned
state. Therefore every state is recurrent with exact period $4n$, and the
number of cycles is $2^{n-1}$.

The map

$$
\Phi:\{-,+\}^{n-1}\times\mathbb Z/(4n)\mathbb Z\longrightarrow X_n,
\qquad\Phi(b,t)=T^t(s_b)
$$

is a bijection by that disjoint exhaustive decomposition. It satisfies
$T\Phi(b,t)=\Phi(b,t+1)$, which proves the claimed product-phase conjugacy.
In particular the exact temporal fixed-count law, for every integer
$k\ge0$, is

$$
|\operatorname{Fix}(T^k)|=
\begin{cases}
n2^{n+1},&4n\mid k,\\
0,&4n\nmid k.
\end{cases}
$$

The convention at $k=0$ is included: $4n$ divides zero and $T^0$ fixes
every state. The maximum transient depth is zero.

### Step 5. Exact inverse-axis obstruction, with its quantifiers

If $U\subseteq X_n$ is forward invariant, then $T|_U$ is injective on a
finite set and hence surjective on $U$. It remains a permutation with
singleton target fibres. This assertion is not about an arbitrary subset
that fails to be forward invariant.

If $\pi:X_n\to Y$ is a surjection onto a finite set and a self-map
$F:Y\to Y$ satisfies $\pi T=F\pi$, then
$F^{4n}\pi=\pi T^{4n}=\pi$. Surjectivity gives $F^{4n}=\mathrm{id}_Y$,
so $F^{-1}=F^{4n-1}$. Thus every genuine finite autonomous factor also has
singleton target fibres. Forgetting the hand or some memory without a
well-defined commuting factor is not covered and does not define a new
autonomous system automatically.

More generally, let $P$ be a permutation of any finite set $Z$, and let
$A\subseteq Z$. Every point of $A$ returns to $A$ because it lies on a
finite cycle. In each $P$-cycle meeting $A$, the positive first-return map
visits the points of $A$ on that cycle in their cyclic order. It is a
cyclic permutation of those section points. Taking the disjoint union
over cycles shows the entire first-return map on $A$ is a permutation.
Therefore complete first returns cannot create the missing inverse axis
either. For the particular section $S$ above, that permutation is identity.

All claims follow. $\square$

## Corrections or missing assumptions

None are required for this stated control. Changing an outward wall step
to an immediate interior move changes the clock and possibly the closed
carrier. Absorbing boundaries, erased memories, restricted hand states,
random swaps, multiple simultaneous walkers or a noncommuting observation
are different rules; no theorem or authorization for them is inferred.

## Open risks and credit

These are complete author deductions without an independent review or
scientific execution. The published M1 definition and its one-or-three-step
aligned propagation are credited in the report. The finite wall and exact
round-trip argument do not establish global novelty, and the global
permutation/product-phase structure defeats this lane's nontrivial inverse
requirement. No unrelated local-memory family is declared exhausted.
