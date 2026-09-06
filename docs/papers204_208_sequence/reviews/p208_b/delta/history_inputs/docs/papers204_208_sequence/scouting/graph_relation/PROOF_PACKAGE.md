# Proof Package: zero-credit distinct-meet erosion

## Claim

For every integer $n\geq0$, let $\mathcal X_n=2^{2^{[n]}}$. Define
$$
D(\mathcal H)=\{A\cap B:A,B\in\mathcal H,\ A\ne B\}.
$$
Then $D^{n+1}(\mathcal H)=\varnothing$ for every
$\mathcal H\in\mathcal X_n$, and the bound $n+1$ is attained by
$\mathcal H=2^{[n]}$. In particular the empty family is the only recurrent
state and the maximum transient depth is $n+1$.

## Status

PROVABLE AS STATED. **Zero new-contribution credit; candidate not admitted.**
This is a direct finite maximal-layer erosion argument, not a second
independent structural axis. Author: batch197_fifth_scout.

## Assumptions

- The ground set is $[n]=\{1,\ldots,n\}$, with $[0]=\varnothing$.
- States are families without multiplicity; the empty family and the empty
  member are both permitted and are different objects.
- Pair arguments must be distinct. The update is simultaneous.

## Notation

For a family $\mathcal H$, define its downward closure by
$$
I(\mathcal H)=\{C:C\subseteq A\text{ for some }A\in\mathcal H\}.
$$
For a nonempty family $I$, let $\operatorname{Max}(I)$ be its
inclusion-maximal elements. Define
$L_k=\{A\subseteq[n]:|A|\leq k\}$ for $0\leq k\leq n$ and
$L_{-1}=\varnothing$.

## Proof Strategy

Compare the downward closure after an update with deletion of all maximal
elements. This is an internal proof device, not an assertion that the literal
DI map itself deletes only maximal elements.

## Dependency Map

1. The universal bound follows from strict decrease of maximum set size in
   the nonempty downward closure.
2. That decrease follows because distinct inputs cannot intersect to an
   inclusion-maximal old element.
3. Sharpness follows from the explicit rank-ideal orbit $D(L_k)=L_{k-1}$.
4. Recurrence follows from universal termination at the fixed empty family.

## Proof

Step 1. Let $I=I(\mathcal H)$. Every intersection of members of
$\mathcal H$ is in $I$, so $I(D(\mathcal H))\subseteq I$.
Suppose some $M\in\operatorname{Max}(I)$ belonged to
$I(D(\mathcal H))$. Then there would be distinct $A,B\in\mathcal H$
with $M\subseteq A\cap B$. Since $A,B\in I$ and $M$ is maximal,
both $A=M$ and $B=M$, contradicting distinctness. Consequently
$$
I(D(\mathcal H))\subseteq I(\mathcal H)
\setminus\operatorname{Max}(I(\mathcal H)).
$$

Step 2. If $I(\mathcal H)$ has maximum set size $r$, every size-$r$
member is maximal. Step 1 therefore shows that the next nonempty downward
closure has maximum set size at most $r-1$. Initially $r\leq n$.
After at most $n$ updates a nonempty downward closure can contain only
$\varnothing$; its next update is empty. Thus
$D^{n+1}(\mathcal H)=\varnothing$. If the initial family is empty, the
same conclusion holds because $D(\varnothing)=\varnothing$.

Step 3. For $1\leq k\leq n$, distinct sets of sizes at most $k$
cannot have an intersection of size $k$: that would force both to equal
that intersection. Hence $D(L_k)\subseteq L_{k-1}$. Conversely, for
$C\in L_{k-1}$ there is an element $x\in[n]\setminus C$, since
$|C|\leq k-1<n$. The two distinct members $C$ and $C\cup\{x\}$
of $L_k$ intersect to $C$. Thus $D(L_k)=L_{k-1}$.
Also $L_0=\{\varnothing\}$ is a singleton family, so $D(L_0)=L_{-1}$.
Starting from $L_n$, the first empty state occurs exactly at time $n+1$.
For $n=0$ the same statement is the single update
$\{\varnothing\}\mapsto\varnothing$.

Step 4. Every orbit eventually reaches the empty family, and that family is
fixed. A recurrent state on any other cycle could not have this property.
Therefore the empty family is the only recurrent state. Step 3 and Step 2
give maximum transient depth exactly $n+1$. $\square$

## Corrections or Missing Assumptions

None for the displayed DI claim. The diagonal-pair exclusion is essential:
allowing $A=B$ would preserve each old member and destroy this erosion proof.

## Open Risks

No claim is made about every-target fibres, maximum-fibre targets, or a
nontransferable second axis. The proof is a generic rank-peeling mechanism
near previously killed MEP/SFP probes. Small-case depth agreement is only a
falsification check, and this note has no independent manuscript review.

The SND hypotheses suggested by the pilot (termination by $n-1$ and unique
largest fibre at the empty target for all $n\geq2$) remain
**NOT CURRENTLY JUSTIFIED**. No all-parameter SND proof is asserted here.
