# ORR: bounded root clock proof attempt

2026-09-07 UTC. A separate pure deduction note; the sealed twenty-second
scout and all its proofs, pilots and failures are unchanged. No new map,
parameter box, program, scientific execution or candidate gate is started.

## Claim and status

For a permutation of $[n]=\{1,\ldots,n\}$, ORR reverses each old maximal
increasing run of odd length and holds each even run, simultaneously.
The empty permutation is held. Let $H_n$ be the largest number of nonfixed
epochs before a fixed point. The old finite observation suggests
$$H_n=\left\lfloor\frac{n-1}{2}\right\rfloor\quad(n\ge1),\qquad H_0=0.$$

**Status of that all-parameter claim: NOT CURRENTLY JUSTIFIED.** This note
does not turn the finite values through seven into a theorem. It supplies
one proved local ancestry lemma and an explicit obstruction to a naive
induction. Neither closes the missing temporal axis.

## Assumptions, strategy and dependencies

Positions are linear, labels are distinct and the old maximal runs are
computed before any reversal. An active run means an odd run of length at
least three. The proposed strategy is to trace an active run backwards and
force a support of at least $2t+1$ positions for the $t$-th nonfixed epoch,
counted from $t=1$. Equivalently, activity in $x_s=T^s(x_0)$ at zero-based
time $s$ would require at least $2s+3$ positions.
It requires a global no-reuse or suitable overlap-counting lemma; the local
lemma below alone does not imply that statement.

Root read the complete original
[pre-code deductions](finite_systems_twenty_second/PRECODE_PROOFS.md) and
[Fibonacci inverse proof and retained clock gap](finite_systems_twenty_second/ORR_FIBRE_PROOF.md).
The inverse argument is not used in the following deduction. No source-owner
claim or new literature clearance is made.

## Proof of the local successor-run lemma

Let $x$ be an arbitrary input and $y=T(x)$. Every active maximal increasing
run in $y$ has exactly one of the following forms:

1. One complete old even increasing run, together with exactly one endpoint
   from an immediately adjacent old active run.
2. One old singleton run, together with one endpoint from each of the old
   active runs immediately on its two sides. Its new length is three.

To prove this, an old active interval is strictly decreasing after reversal.
A new increasing run cannot contain two adjacent positions from it. If the
new run meets it and also extends outside it, the intersection must therefore
be its leftmost or rightmost position. A new active run cannot lie wholly
inside an old active interval, since the latter is decreasing.

Every inactive old run is either a singleton or has even length. Its values
and all its internal increasing adjacencies are unchanged. A maximal new
increasing run meeting an inactive old run must contain the entire old run:
otherwise the omitted adjacent part would extend it. Two adjacent inactive
old runs retain their separating descent. If two inactive old runs have an
active interval between them, a new increasing run cannot cross that whole
decreasing interval. Hence a new increasing run contains at most one old
inactive run.

Without any old inactive run, a new increasing run can use at most the two
facing endpoints of adjacent old active intervals, so has length at most
two. A new active run must consequently have a single old inactive central
run and at most one adjacent active endpoint on each side. If the central
length is even, an odd new length requires exactly one such endpoint. If
the central length is one, odd length at least three requires both. These
are precisely the two alternatives, proving the lemma. $\square$

## Why the intended global inference is missing

The complete symbolic trajectory
$$
(2,5\mid1,4,7\mid3,6)
\longmapsto(2,5,7\mid4\mid1,3,6)
\longmapsto(7\mid5\mid2,4,6\mid3\mid1)
\longmapsto(7\mid5,6\mid4\mid2,3\mid1)
$$
uses bars to display all maximal increasing runs at each epoch. Each arrow
is verified directly by reversing exactly the displayed odd nontrivial
blocks. The final word is fixed, since its run lengths are one or two.
This is displayed arithmetic on one already allowed size, not a program run
or a new exhaustive seven-point check.

Positions $3,4,5$ form an active run in the initial word, split their activity
to the two sides in the next epoch, then form an active run again two epochs
later. Thus active position intervals are not consumed permanently, and
backward ancestry can branch and return to a previously active interval.
The local successor lemma does not justify adding two *previously unused*
positions at every epoch. A bound on the union of an overlapping ancestry
tree requires a further proved invariant; none is established here.

The example is consistent with $H_7=3$ and is **not** a counterexample to
the conjectured formula. It refutes only the unqualified no-reuse step.
Likewise, parity preservation and inversion increase do not prove that
an individual label moves in only one direction or crosses a new parity
position on every remaining epoch.

## Corrections, scope and disposition

The existing generic potential bound and fixed-locus classification remain
the proved temporal results. The sharp Fibonacci target-fibre maximum does
not repair the missing clock argument. The desired formula is unchanged
and unproved; no extra assumption is silently substituted. Root contributes
the local lemma, not a successful clock proof or an independent review.
The original ORR scout actually read this separate note, checked the complete
lemma and displayed trajectory, and found no substantive defect. Its
epoch-indexing clarification is incorporated above. That is author-level
cross-checking, not candidate admission or nonauthor review.

Close this bounded attempt **NO_PROMOTION**, with no larger pilot or paper
number. Any later reopening needs an actual new global lemma and the usual
source/value gate. All external actions remain HOLD_EXTERNAL.
