# Background proof / residual blockage package

Author: `round211_finite_matching_scout`, 2026-09-09 UTC.
These are subtraction controls, not newly proposed literal candidates.

## Claim and status

For the source-class symmetric conflict-veto map $R$ defined below,
$R^3=R$; every state enters a fixed point or two-cycle by time one; its
fixed states are maximal independent sets; and every target's inverse
is the stated neighborhood-cover family.

**PROVABLE AS STATED — elementary background deduction.**
The separate proposed research requirement, a new paper-scale temporal
mechanism together with a materially independent inverse/enumeration
mechanism in this desk, is **NOT CURRENTLY JUSTIFIED**.

## Assumptions and notation

$H=(W,F)$ is a finite labelled loopless undirected simple graph. For
$S\subseteq W$, let

$$
N(S)=\{v\in W:\exists s\in S,\ \{s,v\}\in F\},\qquad
R(S)=W\setminus N(S).
$$

These are open neighborhoods, so membership of $s$ in $S$ does not itself
exclude $s$ from $R(S)$. The carrier is all of $2^W$, not just its
independent subsets. A maximal independent set is an independent set not
properly contained in another independent set; it need not be maximum.
A state is recurrent if it lies on a directed cycle. Its entry time is
the least nonnegative number of iterations needed to reach a recurrent
state.

## Strategy and dependency map

1. Symmetry gives an antitone Galois relation and an extensive second iterate.
2. Apply antitonicity and extensivity twice to obtain $R^3=R$.
3. Translate the fixed equation into independence plus domination.
4. Translate a target equation into permitted sources and coverage, then
   apply finite inclusion-exclusion only as a generic count identity.

The deductions are self-contained; source ownership and exact read limits
are in `HANDOFF.md`. No executable check or all-graph enumeration supports
or is needed by this author background proof.

## Proof

### Step 1. Symmetric antitone relation

For any $A,B\subseteq W$, symmetry of adjacency gives

$$
A\subseteq R(B)\quad\Longleftrightarrow\quad B\subseteq R(A).
$$

Indeed both sides mean that no edge of $H$ joins any element of $A$ to
any element of $B$. If $A\subseteq B$, then $N(A)\subseteq N(B)$ and
thus $R(B)\subseteq R(A)$. Taking $B=R(A)$ in the displayed equivalence
gives $A\subseteq R^2(A)$, because $R(A)\subseteq R(A)$.

### Step 2. One-step recurrent entry

Apply the antitone map $R$ to $A\subseteq R^2(A)$. This gives
$R^3(A)\subseteq R(A)$. Apply the extensivity result from Step 1 to the
set $R(A)$ itself, giving $R(A)\subseteq R^2(R(A))=R^3(A)$.
Consequently $R^3(A)=R(A)$ for every $A$. Thus $R(A)$ is fixed by $R^2$
and lies on a cycle whose length divides two. Every state is recurrent
exactly when $R^2(A)=A$: one direction follows from the identity on all
images, since a recurrent state is an image; the other follows from the
equation itself. Entry time is zero on those states and one otherwise.
This does not imply every graph has an entry-time-one state.

### Step 3. Fixed states and failure of the matching-only carrier

The equality $S=R(S)$ is equivalent to both $S\cap N(S)=\varnothing$
and $W\setminus S\subseteq N(S)$. The first condition is independence.
For an independent $S$, the second is equivalent to maximality: if an
outsider has no neighbor in $S$, it can be added, and otherwise no outsider
can be added. This proves the fixed-state characterization.

If $H=L(G)$, independent edge sets are matchings and maximal independent
edge sets are maximal matchings. But the unrestricted update is not a
self-map of matchings. Let $G$ be the labelled path with vertices
$\{1,2,3\}$ and edges $e_1=\{1,2\}$ and $e_2=\{2,3\}$. The empty
matching is valid, while $R(\varnothing)=\{e_1,e_2\}$ is not a matching.
This is a symbolic two-edge boundary counterexample, not a graph pilot.

### Step 4. Full target inverse is a generic coverage family

Fix $Y\subseteq W$. The exact equivalence is

$$
R(S)=Y
\quad\Longleftrightarrow\quad
S\subseteq R(Y)\ \text{ and }\ N(S)\supseteq W\setminus Y.
$$

For the forward implication, $N(S)=W\setminus Y$. In particular no edge
joins $S$ and $Y$, so symmetry gives $S\subseteq R(Y)$. The coverage
condition follows from that equality. Conversely the allowed-source
condition prevents every vertex of $Y$ from lying in $N(S)$, so
$N(S)\subseteq W\setminus Y$. Coverage supplies the reverse inclusion
and therefore $R(S)=Y$.

Let $A=R(Y)$ and $B=W\setminus Y$. For each $b\in B$, a source fails
to cover $b$ exactly when it is a subset of $A\setminus N(\{b\})$.
For any $J\subseteq B$, all failures indexed by $J$ hold exactly for
sources contained in $A\setminus N(J)$; there are
$2^{|A\setminus N(J)|}$ such sources. Finite inclusion-exclusion yields

$$
|R^{-1}(Y)|
=\sum_{J\subseteq W\setminus Y}(-1)^{|J|}
  2^{|R(Y)\setminus N(J)|}.
$$

This is the ordinary coverage inclusion-exclusion identity, not a new
evaluated matching fibre theorem. It retains exponentially many subset
terms and proves neither a new extremal formula nor a line-graph census.

If $W=\varnothing$, the sole empty state is fixed and the sum has one
term equal to one. If $H$ is edgeless with $W\ne\varnothing$, $R(S)=W$
for every $S$, and the preceding identity gives $2^{|W|}$ at $Y=W$ and
zero elsewhere. Isolated vertices otherwise cause no exception: they
belong to every image and to every maximal independent set.
All stated background claims follow. $\square$

## Corrections or missing assumptions

No correction is needed for the full Boolean carrier. Treating that
carrier as only the feasible matchings would be invalid, as Step 3 shows.
An added conflict-resolution selector would be a different literal and
has not been defined, proved, tested or nominated here. We do not silently
add a scheduler to cure the carrier failure.

## Open risks / blockage

The concurrent matching source law has a known potential, but this desk
does not supply a surviving sharp full-carrier clock or independent
inverse atlas. The NOR comparison has a rigid but elementary polarity
time law and a generic covering inverse. The conjunction needed for
admission is missing, so the desk closes without a candidate or reserve.
This does not assert global exhaustion, novelty clearance, or acceptance
by an independent reviewer.
