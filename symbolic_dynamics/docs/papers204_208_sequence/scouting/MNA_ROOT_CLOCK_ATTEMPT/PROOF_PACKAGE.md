# Root check of the maximal-nondecreasing-run merger clock

## Claim

For $n\ge1$, let $\mathcal C_n$ be the positive integer compositions of
$n$. The autonomous map $F$ replaces every maximal weakly increasing run
by its sum, simultaneously. If $\tau(x)$ is the first time the orbit is
fixed, then

$$\max_{x\in\mathcal C_n}\tau(x)
=H(n):=\left\lfloor\frac{\sqrt{8n-7}-1}{2}\right\rfloor.$$

The only recurrent states are the strictly decreasing compositions.

## Status

PROVABLE AS STATED. This is a deductive proof check, not candidate
admission, an independent manuscript review, or a novelty verdict.
No scientific enumeration was executed for this note.

## Assumptions

- Parts are positive integers, and total mass $n$ is fixed.
- Comparisons use the old composition; maximal runs are merged in parallel.
- Equal adjacent parts belong to the same run.
- The composition of one part is fixed. The empty composition is not in
  the stated carrier.

## Notation

Each current part is an interval block of the original composition. Its
mass is the sum of its original parts. Interval boundaries can disappear
but are never created. A block is newly formed at round $t\ge1$ when it
contains at least two blocks from time $t-1$. Put
$T_t=1+t(t+1)/2$ for $t\ge0$.

## Proof strategy

Trace a late disappearing boundary one round backward. The right block
must itself have been formed in the preceding round. Integer strictness
then yields a growing lower bound on its left neighbour. A second
induction adds disjoint masses to obtain the triangular threshold.

## Dependency map

1. Positivity preserves mass and the interval-block representation.
2. Lemma A: a boundary disappearing in round $t$ has old left mass at
   least $t$.
3. Lemma B: a block newly formed in round $t$ has mass at least $T_t$.
4. A last nontrivial round gives the upper bound from Lemma B.
5. A descending-prefix witness with arbitrary terminal surplus attains
   the bound.

## Proof

### Step 1. Eventual fixed points

A composition is fixed exactly when every adjacent pair is a strict
descent. Otherwise at least one run has two parts and the number of
parts decreases. Therefore every orbit becomes fixed in finitely many
steps, and a periodic orbit must already be a fixed point. No boundary
can reappear, because the update only joins adjacent interval blocks.

### Step 2. Backward dependency and Lemma A

At round $1$, the old left block at any disappearing boundary has mass
at least $1$, proving the base case. Suppose the claim holds for round
$t-1$, where $t\ge2$. Consider a boundary disappearing in round $t$.
Let $A,B$ be its adjacent blocks at time $t-1$; then $|A|\le|B|$.
At time $t-2$, let $a$ be the rightmost parent block of $A$ and $c$ the
leftmost parent block of $B$.

This outer boundary still exists at time $t-1$, so it was not removed
in round $t-1$. The old comparison across it therefore gives
$|a|>|c|$. If $B$ were unchanged in round $t-1$, it would equal $c$,
and positivity would give $|A|\ge|a|>|B|$, contradicting
$|A|\le|B|$. Hence $B$ was newly formed in round $t-1$.

In particular $B$ has at least two parent blocks, and the first internal
boundary of $B$ disappeared in round $t-1$. Its left parent is $c$.
The induction hypothesis implies $|c|\ge t-1$. Since masses are
integers and $|a|>|c|$, we obtain $|A|\ge|a|\ge t$.
This proves Lemma A, and also proves the preceding-round formation
statement for the right block of any such boundary.

### Step 3. Lemma B

A newly formed block in round $1$ contains at least two positive parts,
so its mass is at least $2=T_1$. Suppose $t\ge2$ and the assertion
holds for round $t-1$. Write the consecutive old blocks of a block
newly formed at round $t$ as $A_1,\ldots,A_k$, with $k\ge2$.
The first internal boundary disappears in round $t$. Step 2 gives
$|A_1|\ge t$ and says that $A_2$ was newly formed in round $t-1$.
The induction hypothesis therefore gives $|A_2|\ge T_{t-1}$.
They are disjoint, so the new block has mass at least

$$|A_1|+|A_2|\ge t+T_{t-1}=T_t.$$

This proves Lemma B without assuming that other merges are absent.

### Step 4. Global upper bound

If $\tau(x)=t\ge1$, round $t$ makes a nontrivial merge; otherwise
the state would have been fixed already at time $t-1$. Lemma B gives
$n\ge T_t$. Solving $1+t(t+1)/2\le n$ for the nonnegative integer
$t$ yields $t\le H(n)$. The case $\tau(x)=0$ satisfies the same
bound because $H(n)\ge0$.

### Step 5. Exact witnesses and all masses

For $h\ge1$ and any integer $r\ge0$, use

$$x=(h,h-1,\ldots,2,1,1+r),\qquad n=T_h+r.$$

At time $1$ its final two parts merge and all earlier cuts survive.
For $1\le t\le h$, induction gives the current composition

$$F^t(x)=(h,h-1,\ldots,t+1,\ r+T_t),$$

where the prefix is empty at $t=h$. For $t<h$, its prefix is strictly
decreasing, while $r+T_t\ge t+1$. Thus in the next round exactly the
last prefix part joins the final block. Earlier prefix parts cannot
join in that same round, because their old comparisons remain strict
descents. This proves the formula and shows that $\tau(x)=h$.
For a prescribed $n\ge2$, take $h=H(n)$ and $r=n-T_h\ge0$.
For $n=1$, the sole composition $(1)$ has time $0=H(1)$.
The upper bound is attained for every mass. $\square$

## Corrections or missing assumptions

The surplus must not be silently added to the first part: doing so may
prevent the last merge. The terminal-surplus witness above avoids that
problem. No sharp claim is made for signed or zero parts, asynchronous
updates, cyclic compositions, or another comparison predicate.

## Authorship and reading boundary

The lane40 scout formulated MNA and the descending witness locally before
root sent a similar witness hint. The scout subsequently supplied the
two-induction Lemma A/Lemma B route and the terminal-surplus witness.
Root independently checked its parent-block implications and wrote the
explicit argument here on 2026-09-07 UTC. This is collaborative proof work;
neither contributor is an independent manuscript reviewer of this system.
The live lane40 intake still described its first two negative literals
when root read it; the third literal was confirmed directly with its
owner before this proof check. The scout's full intake/source package
must be inspected after its actual handoff.

## Open risks

The clock proof is closed, but source subtraction and a materially
separate residual inverse/image contribution remain candidate-gate
obligations. This note does not establish global novelty or grant a
paper number. It changes no old manuscript or accepted artifact.
OWNER_AMBER / HOLD_EXTERNAL.
