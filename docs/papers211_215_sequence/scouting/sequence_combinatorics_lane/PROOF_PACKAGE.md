# Two sequence proposals — exact collision proof

Author: /root/round211_tree_order_scout. Date: 2026-09-08 UTC.
Status: PROVABLE AS STATED (closure and conjugacy only).
Disposition: KILL_EXACT_CONJUGACY / NO_PROMOTION.

## Claim and assumptions

For every integer $n\ge1$, the two literal maps below are conjugate to
specified old internal maps. Their time, image and fibre statements transfer
exactly, so they create no fresh dynamical system for this batch.

## Strategy and dependency map

1. Identify the complete carriers and prove closure directly.
2. Give an explicit bijective change of labels for each map.
3. Prove the conjugacy equation at every input.
4. Deduct all dynamical and inverse claims through that bijection.

The old ISE definition is inspected in CANDIDATES.md and the function
interval_span_echo in pilot.py. The complete old CBF_DERIVATION.md was
read. These exact historical files are pinned in HISTORY_INPUTS.sha256.
No finite experiment is used in this proof.

## 1. SIF — positive span feedback

On $[n]^n$, for each used letter $a$ let $f_w(a)$ and $l_w(a)$ be the
first and last positions containing it. Set
$$
H_n(w)_i=l_w(w_i)-f_w(w_i)+1.
$$
Positions remain fixed, and all values are computed from the old word.
Every position belongs to a nonempty occurrence class; hence
$0\le l_w(w_i)-f_w(w_i)\le n-1$, proving $H_n(w)\in[n]^n$.
For $n=1$ the unique state is fixed.

Old C19_ISE acts on $\{0,\ldots,n-1\}^n$ by
$$
F_n(v)_i=l_v(v_i)-f_v(v_i).
$$
Define $A_n(w)_i=w_i-1$, a bijection onto that old carrier.
Changing every letter by the same injective translation preserves each
occurrence class and its first/last positions. Therefore, at every $i$,
$$
(A_n H_n(w))_i
=l_w(w_i)-f_w(w_i)
=(F_n A_n(w))_i.
$$
Thus $A_nH_n=F_nA_n$ and $H_n=A_n^{-1}F_nA_n$ for every $n$.

This is a full-carrier conjugacy, not a matching finite histogram.
The inclusive-span convention contributes only a label translation.
No new fixed-point, clock or inverse claim is promoted.

## 2. MCB — max-Cartesian breadth-first readout

For $w\in S_n$, recursively construct its ordered max-Cartesian tree:
the largest entry is the root, and the left and right subtrees are built
from the subwords respectively before and after that entry. Empty
subwords give empty children. Define $B_n(w)$ as its breadth-first
left-before-right label sequence.

Each original label occurs at exactly one tree vertex, and breadth-first
reading visits every vertex exactly once. Thus $B_n(w)\in S_n$; the
rule is total and autonomous. For $n=1$ it is the identity.

Let $\Phi_n$ be old Q02_CBF: build the min-Cartesian tree and read it in
the same breadth-first left-before-right order. Define the involution
$C_n(w)_i=n+1-w_i$. Complementing labels turns a largest root into a
smallest root, preserves its position in the inorder word, and preserves
the left/right subwords. Induction on subtree size therefore proves
$$
\operatorname{Cart}_{\min}(C_n(w))
=C_n(\operatorname{Cart}_{\max}(w)),
$$
where the right side complements node labels without changing shape.
Breadth-first readout commutes with this label operation, giving
$$
\Phi_n C_n=C_n B_n,\qquad B_n=C_n\Phi_n C_n.
$$

The old original already proves the sharp $n-1$ clock, unique identity
attractor, every-target compatible-tree fibre formula and Catalan fibre
maximum for $\Phi_n$. Under the displayed conjugacy, the attractor
becomes the descending permutation and all these theorems transfer.
No fresh clock or inverse argument is obtained by reversing heap order.

## 3. Why conjugacy deducts both axes

If $A H=F A$ with $A$ bijective, induction gives $A H^t=F^t A$ for every
$t\ge0$. It follows that $A$ carries every orbit and its first recurrence
time to the corresponding old orbit. It also restricts to a bijection
$$
(H^t)^{-1}(y)\longrightarrow(F^t)^{-1}(A(y)).
$$
Thus all cycle, time, image, target-fibre and extremal claims carry over.
A new evaluator or shifted alphabet cannot restore an independent axis.

## Boundaries

Two literal desk proposals were assessed, both duplicates; zero fresh
systems, zero reserves, zero promotions, zero scientific pilots.
There is no third instantiated proposal. Josephus, NOG, PD/CNE/CNM,
prefix ranks, LIS-layer recoding and pruning were source/preflight leads,
not additional candidate counts. The old word-statistic acronym SPR in a
historical report is unrelated to the current arithmetic SPR; this lane
made no contribution to the latter or to MPR/LAR.
