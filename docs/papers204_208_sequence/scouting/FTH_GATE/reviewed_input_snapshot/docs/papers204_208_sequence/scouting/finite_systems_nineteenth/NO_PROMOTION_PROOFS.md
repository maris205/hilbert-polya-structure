# MCR and TCR: deductive residues and closed negative dispositions

2026-09-06 UTC. Author deductions, not independent review. Definitions and
the immutable boxes remain those of `INTAKE.md`. No parameter expansion.

## MCR — generic consensus growth, no separate inverse theorem

For an ordered matching triple $X=(A,B,D)$, let

$$C(X)=A\cap B\cap D,\qquad
M(X)=(A\cap B)\cup(B\cap D)\cup(D\cap A).$$

Distinct edges of $M(X)$ cannot share a vertex. Indeed, two such edges
each belong to at least two of three matchings, so some matching would
contain both incident edges. Thus $M(X)$ is a partial matching.

**Proposition (PROVABLE AS STATED).** Every majority edge becomes common
after one MCR step, every common edge persists, and

$$F(X)=X\quad\Longleftrightarrow\quad M(X)=C(X).$$

Every orbit therefore reaches a fixed point after at most
$n-|C(X)|$ nonfixed steps. No nontrivial recurrent cycle exists.

Proof. If $e\in B\cap D$, it is imposed on $A$. Repairs imposed on $B$
belong to $A\cap D$, so any such edge meeting $e$ must equal $e$, since
$D$ already contains $e$. Hence repair cannot break $e$ in $B$; the same
argument applies to $D$. Thus $M(X)\subseteq C(F(X))$. If $M=C$, each
imposed intersection already belongs to the matching on which it is
imposed, so all three repairs do nothing. If $M\ne C$, some majority edge
is absent from one matching and is added, so the state changes and $|C|$
strictly increases. There are at most $n$ common edges. ∎

This is the generic finite monotone-support clock and receives no new
temporal credit. It is not a sharp-clock theorem. Nor does the observed
height at most one in the original $n\le3$ boxes prove idempotence.
For clarity, the following **symbolic calculation**, not an additional
producer or exhaustive box, disproves all-size idempotence. On eight labels,

$$A=\{01,23,45,67\},\quad B=\{01,26,34,57\},\quad
D=\{02,13,46,57\}.$$

The respective imposed intersections are $\{57\},\varnothing,\{01\}$.
Direct alternating-path repair gives

$$F(A,B,D)=(Q,B,Q),\quad Q=\{01,23,46,57\};\qquad
F(Q,B,Q)=(Q,Q,Q).$$

No code was run on $n=4$. The first step is not fixed, whereas every pilot
state at $n\le3$ reaches a fixed state within one step. No structural
all-target inverse or evaluated sharp global fibre maximum has been
proved. The small inverse tables are observations, not that missing axis.

Disposition: `NO_PROMOTION_GENERIC_TEMPORAL_AND_MISSING_INVERSE`.

## TCR — two-binary-coordinate slice, full-shape proof gap

The literal is a positive Boolean map and hence inclusion-monotone, but
not inflationary: every singleton relation maps to empty.

Suppose the shape is $(2,2,c)$, and set
$A_{ij}=\{k:(i,j,k)\in R\}$. Write $\bar i=1-i$, $\bar j=1-j$.
The update reads exactly

$$A'_{ij}=\{k\in A_{\bar i\bar j}:
 (A_{i\bar j}\cap A_{\bar i j})\setminus\{k\}\ne\varnothing\}.$$

In particular $A'_{ij}\subseteq A_{\bar i\bar j}$, so applying the same
inclusion once more gives $A''_{ij}\subseteq A_{ij}$. Therefore
$F^2(R)\subseteq R$ for every $c$. Since $F$ is monotone, the even
and odd subsequences are separately decreasing and eventually constant.
Every orbit in this slice has period at most two. This proof is
**PROVABLE AS STATED** only for the specified two-binary-coordinate slice
(and its coordinate permutations), not arbitrary grid shapes.

For shapes with a coordinate at most one the literal sends everything
to empty, as the nondegenerate witness does not exist. These trivial
boundaries and the conjunctive/erosion slice receive no new credit.

The complete $(2,3,3)$ pilot has height seven and only periods one and two,
but no all-shape recurrent classification or general period-two theorem
has been proved. Generic Boolean-circuit encoding or a truth-table inverse
would not supply an independent evaluated inverse/extremal axis. Neither
axis is repaired by enlarging the grid.

Disposition: `NO_PROMOTION_FULL_SHAPE_PROOF_GAP_AND_MISSING_INVERSE`.

## Desk-only descriptions

FRC, cycle reversal with trees retained, and the degenerate-allowed corner
rule retain their exact desk deductions in `INTAKE.md`. They ran zero
producers and were not counted as three fresh pilot candidates. This lane
obtained three new literal pilots, not a six-new-system slate.
