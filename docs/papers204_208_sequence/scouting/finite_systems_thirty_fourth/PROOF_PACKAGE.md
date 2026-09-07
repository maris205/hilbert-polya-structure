# Proof Package — MPL convergence and deducted inverse boundaries

## Claim

For every $n\ge1$, the exact MPL map on $E_n$ has no periodic orbit of
period greater than one. Put $q=M(x)$ and $N=n(n-1)/2$. Its first fixed
point is reached within

$$\tau(x)\le 1+N-\sum_{i=0}^{n-1}q_i.$$

This is a nonsharp potential bound, not the desired exact time theorem.
Two special-target fibres and a generic all-target constraint identity
below are also proved, with their lack of residual credit stated explicitly.

## Status

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION**, with a weakening only:
the original two-axis admission target is not justified. The displayed
weak claims are fully proved; no new assumption was imposed on the carrier.
Author: this scout agent, therefore a proof contributor and not its own
independent reviewer. Overall **NO_PROMOTION / HOLD_EXTERNAL**.

## Assumptions

The length $n$ is a positive integer. A word $x\in E_n$ has integer entries
$0\le x_i\le i$ for $0\le i<n$. Every factor in a palindromic factorization
is nonempty. The whole output array is interpreted as the next integer word.

## Notation

For a word $w$, let $\operatorname{pl}(w)$ be its minimum number of
nonempty palindrome factors, with $\operatorname{pl}(\epsilon)=0$.
Then $M(x)_i=\operatorname{pl}(x_0\cdots x_i)-1$.
Let $\mathcal W_n$ consist of the integer paths $q_0=0$, $q_i\ge0$ and
$|q_i-q_{i-1}|\le1$. Such paths automatically satisfy $q_i\le i$.
A state is recurrent if it lies on a directed cycle. The entrance time
$\tau$ is the least nonnegative time at which a fixed point is reached.

## Proof Strategy

Use the ordinary static prefix-length Lipschitz fact, then compare
palindromic-block endpoints along a numerical path. A bounded monotone
integer potential finishes the weak temporal result. For inverse boundaries,
use only direct target substitution and elementary short-palindrome tests.

## Dependency Map

1. Static Lipschitz lemma gives $M(E_n)\subseteq\mathcal W_n$.
2. Palindromic-block endpoint lemma gives $M(q)\ge q$ on $\mathcal W_n$.
3. Integer potential proves stabilization and the displayed bound.
4. Ordinary DP proves target constraints by induction, not a new decoder.
5. Center deletion reduces slope-target avoidance to length two and three.

## Proof

### 1. Closure and the credited Lipschitz lemma

Every nonempty prefix of length $i+1$ needs between one and $i+1$
palindromes, so $0\le M(x)_i\le i$ and $M(x)_0=0$.
For any word $w$ and letter $a$, appending the one-letter palindrome gives
$\operatorname{pl}(wa)\le\operatorname{pl}(w)+1$.
Conversely, remove the last letter from an optimal factorization of $wa$.
If its last palindrome has length one, deleting it uses one fewer factor.
Otherwise the last palindrome is $ara$ for a possibly empty palindrome $r$;
after deletion, replace it by $a$ and $r$, omitting $r$ when empty. This uses
at most one extra factor. Thus

$$|\operatorname{pl}(wa)-\operatorname{pl}(w)|\le1.$$

It follows that $M(x)\in\mathcal W_n$ for every $x\in E_n$.
This inequality is explicitly old: Lemma 2 in Borozdin et al., printed
page 23:2, credits their reference 10, Lemma 11. Its original proof above
fixes our boundary convention but claims no new static result. The same
primary body supplies the ordinary DP in Section 2.1.
See [the official paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol078-cpm2017/LIPIcs.CPM.2017.23/LIPIcs.CPM.2017.23.pdf).

### 2. Endpoint-height inequality

Fix $q\in\mathcal W_n$ and a prefix ending at $i$. Factor this prefix
into $k$ nonempty palindromes. The first block starts at height zero and,
because it is palindromic, ends at height zero. Suppose the $j$th block
ends at height at most $j-1$. The next block begins one coordinate later,
so its starting height is at most $j$ by the unit-step condition. Its
ending height equals its starting height, again by palindromicity.
Induction gives $q_i\le k-1$. This applies to an optimal factorization,
hence

$$M(q)_i=\operatorname{pl}(q_0\cdots q_i)-1\ge q_i.$$

Every coordinate satisfies this inequality. No assertion that $M$ is
order-preserving between two different input paths is needed or made.

### 3. All-carrier stabilization

Set $q^{(0)}=M(x)$ and $q^{(t+1)}=M(q^{(t)})$. Each path lies in
$\mathcal W_n$ by Step 1, and Step 2 gives $q^{(t+1)}\ge q^{(t)}$.
The integer sum $S(q)=\sum_iq_i$ lies between zero and $N=n(n-1)/2$.
At a nonfixed path at least one coordinate strictly increases, so its
sum increases by at least one. There can therefore be at most
$N-S(q^{(0)})$ nonfixed updates after the first image. Equality of two
consecutive states makes the future constant, because the rule is
autonomous. This proves the claimed entrance bound.

Any recurrent state is itself an image and hence lies in $\mathcal W_n$.
A nonconstant cycle would include a strict potential increase but would
return to its starting sum, a contradiction. Thus every cycle is fixed.
At $n=1$ the unique state $(0)$ is fixed; the general bound is valid but
not sharp there. Both $E_2$ states are also fixed, as is checked directly
from their two prefixes. No small-box evidence is used in this argument.

### 4. A generic all-target constraint identity, entirely deducted

Fix any target $p\in E_n$ and set $p_{-1}=-1$. For each $0\le i<n$,
let $B_i$ contain starts $0\le j\le i$ with $p_{j-1}+1<p_i$, and let
$G_i$ contain starts with $p_{j-1}+1=p_i$. Then $M(x)=p$ if and only if
for every $i$ both conditions hold:

- no suffix $x_j\cdots x_i$ with $j\in B_i$ is a palindrome;
- at least one suffix $x_j\cdots x_i$ with $j\in G_i$ is a palindrome.

To prove it, condition on the already correct target prefixes and use

$$M(x)_i=\min_{j:\ x_j\cdots x_i\text{ palindromic}}
   (p_{j-1}+1).$$

Every prefix has at least its last one-letter palindromic suffix, so the
minimum exists. Requiring it to equal $p_i$ is exactly the two displayed
conditions. Induction from $i=0$ proves necessity and sufficiency. Empty
$G_i$ gives no sources. This is a substitution into the owned static DP;
counting satisfying assignments or re-running prefix branching is not a
separate structural full-fibre theorem. No residual credit is claimed.

### 5. Two special fibres, neither a global extremum

For target $0^n$, each source prefix must itself be a palindrome. Its last
letter then equals its first letter, which is zero. Thus the sole source
is $0^n$, and this source does satisfy the condition.

Let $e=(0,1,\ldots,n-1)$. The equation $M(x)=e$ means that no prefix
can save even one factor over the all-single-letter factorization.
It is equivalent to $x$ containing no palindromic factor of length at
least two: one such factor shortens a factorization of the prefix at
its endpoint, while in its absence every factor must be one letter.
Every palindrome of length at least two has a central palindrome of
length two or three, obtained by repeatedly deleting the outer letters.
Therefore the condition is precisely

$$x_i\ne x_{i-1}\ (i\ge1),\qquad x_i\ne x_{i-2}\ (i\ge2).$$

At $n=1$ the count is one. For $n\ge2$, $x_0=0$ and $x_1=1$ are forced.
At position $i\ge2$ the preceding two letters are distinct and both
belong to $\{0,\ldots,i\}$, leaving exactly $i-1$ choices. Thus

$$|M^{-1}(e)|=(n-2)!\quad(n\ge2).$$

This is a proper-coloring count on the square of a path, with growing
palettes. It is fully deducted. It is not the maximum fibre: already at
$n=5$ the original pilot gives a fibre of size 14 while $(n-2)!=6$.
The finite comparison is not needed for the exact special-fibre proof.

### 6. Refuted shortcut and unclaimed stronger results

The hand-checkable original-box trajectory

$$00100\longmapsto00110\longmapsto00111\longmapsto00111$$

refutes $M^2=M$. In the original word $00100$ the first four prefixes
have minimum factor counts $1,1,2,2$ and the full word is a palindrome.
The middle word $00110$ has the same first four counts, is not itself a
palindrome, and factors as $0\mid0110$, so its full count is two. For
$00111$, the first two prefixes are palindromes; every longer prefix has
two unequal constant runs and therefore needs exactly two palindromes.
These segmentations verify all displayed arrows.
No new larger-box computation accompanies this example.

## Corrections or Missing Assumptions

No carrier correction is required. The claim was deliberately weakened
from a two-axis theorem contract to potential convergence plus deducted
inverse boundaries. Step 2 is not isotonicity, and the bound is not sharp.
The finite fixed-point sequence $1,2,5,11,26,58$ is not extrapolated.

## Open Risks

Missing are a sharp time law, an explicit fixed-point census/structure
beyond the fixed-point equation, a non-generic all-target inverse
decomposition and global fibre extremality/equality cases. Static DP
constraints and the two special targets do not resolve them. Search
non-hits confer no novelty, and no independent gate or reviewer has
accepted this package. The lane closes **NO_PROMOTION**.
