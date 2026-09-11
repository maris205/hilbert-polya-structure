# Sixteenth bounded finite-system intake

Author: `/root/sixteenth_finite_scout`. Date: 2026-09-06 UTC.
This file is written before any pilot code or numerical map execution.
One slate only; no admission, numbering, reserve, manuscript work, external
upload/contact, or automatic next slate is authorized here.

## Scope and selection

Six literal proposals span binary/ternary words, labelled simple graphs,
binary rectangular matrices, and permutations. These are six proposed
updates, **not six established new mechanisms**. Source-owned and
proof-template failures remain failures. Only CNL, D2LC and LRG are selected
for numerical pilots. The three remaining proposals are desk-only.

Prior exclusions, not counted among the six: BWT/CPD; Foata; Lyndon-factor
reversal; RSK row-reading or transpose lifts (including this batch C08_TIR);
ordinary doubly lexical sorting; rotor routing; tree-centre and Prüfer depth
feedback. Exact source and historical paths are recorded separately.
All arithmetic/divisor/antichain, current OFS/P208, rank/count-word and
previously assigned active-lane rules are outside the slate.

## Literal maps, boundaries and predeclared complete boxes

Positions are zero-based except the permutation value/position convention
explicitly stated for LMH. Lexicographic order uses the displayed natural
alphabet order. A cyclic rotation rotates left; duplicate rotations cause
no output ambiguity. No clipping, changed boundary or enlarged box is allowed.

1. **CNL — canonical-necklace XOR.** For every $n\ge1$, the carrier is
   $\{0,1\}^n$. Let $m(w)$ be the lexicographically least among all $n$
   cyclic rotations of $w$. Set $F(w)=w\mathbin\oplus m(w)$ coordinatewise.
   This is not the adjacent Ducci map and not necklace reflection.
   **Pilot:** every word, for every $1\le n\le12$.
   Desired temporal question: all-size recurrent structure, with the
   power-of-two length stratum separately identified. Desired inverse:
   actual whole-target fibres after subtracting fixed-rotation linear algebra
   and static minimum-rotation recognition. No such theorem is assumed.

2. **D2LC — least degree-two local complementation.** For every $n\ge1$,
   the carrier is all simple undirected graphs on $[n]=\{0,\ldots,n-1\}$.
   If no vertex has degree two, hold. Otherwise let $v$ be the least
   degree-two vertex and let $\{a,b\}=N_G(v)$. Toggle the edge $ab$ and
   change no other edge. The pivot is recomputed at each epoch.
   **Pilot:** all $2^{\binom n2}$ graphs for each $1\le n\le6$.
   Desired temporal question: sharp entry time after subtracting the
   generic nonincreasing-selector involution argument of P200. Desired
   inverse: a materially stronger target/extremal theorem than trying
   each possible inverse local complement. Classical local complementation
   itself earns zero credit.

3. **LRG — opposing row/column rotations.** For every $r,c\ge1$, the carrier
   is $\{0,1\}^{r\times c}$ with labelled row and column positions.
   First, independently replace each row by its least cyclic rotation.
   In the resulting matrix, independently replace each top-to-bottom
   column word by its greatest cyclic rotation. Their composition is one
   epoch; no alternation phase is an extra state. These operations rotate
   entries within lines, not reorder whole rows or whole columns.
   **Pilot:** exactly $(r,c)=(1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(3,3),(3,4)$,
   every labelled binary matrix in each box.
   Desired temporal question: all-shape convergence/core or explicit
   recurrent obstruction. Desired inverse: a target-resolved structural
   mechanism after removing static cyclic-rotation orbit counts.

4. **LIR — lex-first longest increasing subsequence reversal.** For
   every $n\ge1$, the carrier is $S_n$ in one-line notation on $1,\ldots,n$.
   Among all longest strictly increasing subsequences, choose the
   lexicographically least tuple of positions. Reverse the values at those
   positions, leaving every unchosen position unchanged. If the selected
   length is one the state holds. **Desk-only; no numerical box/run.**
   Need more than inversion-potential sorting and a generic finite
   subsequence-test inverse. LIS/patience-sorting tools earn zero credit.

5. **LMH — leftmost-misplaced homing.** For every $n\ge1$, the carrier is
   $S_n$, now with positions $1,\ldots,n$. If the permutation is the identity,
   hold. Otherwise choose the least position $i$ with $w_i\ne i$, remove
   $a=w_i$, and insert $a$ in position $a$, shifting intervening entries
   one position and preserving their order. **Desk-only; no numerical
   box/run.** The source-first question is whether the autonomous scheduler
   adds anything beyond the full placement-and-shift theorem and its
   actual extremal scheduler example. No source nonhit implies novelty.

6. **KFR — first lex-increasing Knuth rewrite.** For every $n\ge1$, the
   carrier is $\{0,1,2\}^n$. At each consecutive triple allow the elementary
   Knuth moves $xzy\leftrightarrow zxy$ for $x\le y<z$ and
   $yxz\leftrightarrow yzx$ for $x<y\le z$. Retain only replacements whose
   resulting triple is lexicographically larger. Choose the leftmost
   position where such a replacement is possible; if several results
   existed at that position choose the lexicographically least resulting
   triple. Apply only this one replacement; hold if none exists.
   **Desk-only; no numerical box/run.** Need a recurrent/temporal theorem
   and inverse theorem that survive classical Knuth-equivalence and
   well-founded rewrite-order deductions. Confluence is not assumed.

## Execution and decision contract

The selected pilots use exact CPU integer/tuple operations, zero GPU-hours,
no random sampling and no cap on an orbit inside a fixed finite carrier.
Every state gets an image, exact indegree, entry time and cycle period.
Entire functional graphs and all-target fibre histograms are derived from
complete carriers, with explicit longest-tail and longest-cycle witnesses.
Expected runtime is under a minute per process; stop on a failed assertion
and retain stdout/stderr rather than repairing the literal or enlarging a box.
At least two isolated source-only processes must succeed, with actual raw
`cmp`, before author numerical results are accepted. Mathematical code,
intake, source record, consumed history and runtime are pinned before/after.
Finite census alone never supplies a missing all-parameter theorem.

The decision choices are NO_PROMOTION with an explicit source/value/proof
reason, or a separate author proof dossier needing a noncontributor gate.
The scout cannot independently review any theorem it contributes.
