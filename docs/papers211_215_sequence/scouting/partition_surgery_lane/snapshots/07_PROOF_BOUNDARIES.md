# Eighth finite structures — proved facts and rejected extrapolations

2026-09-06 UTC. Author notes, not independently accepted manuscript results.
The literal maps and original bounds are in [INTAKE.md](INTAKE.md).
Every candidate is **NO_PROMOTION**. No proof below supplies both required
residual axes. Source deductions are in [SOURCES.md](SOURCES.md).

## 1. WGP: mass only, with nonuniform finite cycle structure

Writing $g_i=\lambda_i-\lambda_{i+1}$ gives
$\sum_i i g_i=|\lambda|$, so the map is a self-map on partitions of
each fixed mass. Equivalently, conjugate the partition, group all columns
of each equal height, and replace such a group by its total area.
This is an elementary static regrouping identity, not a temporal theorem.

WGP takes one part $ig_i$ per positive gap. It does not take $i$ copies
of $g_i$: $(4,2,1)$ goes to $(3,2,2)$, while that desk alternative
would give $(2,1,1,1,1,1)$. The old desk slate is not silently substituted.

The fixed original boxes contain periods 9 at $N=19$ and 11 at $N=23$.
There is no proved all-mass core, transient bound, period classification,
or independent evaluated inverse here. Uneven finite periods are evidence
against a premature short-cycle guess, not evidence of novelty.

## 2. DSR: complete fixed points, but no convergence proof

**Proposition.** A nonempty partition of Durfee size $d$ is DSR-fixed
if and only if it consists of the first $d$ parts

$$d^2,d(d-1),\ldots,2d,d$$

followed by an arbitrary partition with all parts at most $d$.

**Proof.** Let $S$ be the multiset of the first $d$ old parts, and $T$
the unchanged tail. All members of $S$ are at least $d$; all of $T$
are at most $d$. If the whole partition is fixed, cancellation of the
unchanged multiset $T$ gives

$$S=\{d^2\}\uplus\{s-d:s\in S,\ s>d\}.$$

The right side must have $d$ positive members, so precisely one member
of $S$ is $d$. Its largest member is $d^2$: if $m=\max S$, the other
new members are at most $m-d<m$, hence the maximum can only come from
the appended part. If $c(u)$ is the multiplicity of $u>0$ in $S$, then

$$c(u)=\mathbf1_{u=d^2}+c(u+d).$$

Starting above $d^2$, where $c=0$, this recurrence forces multiplicity
one at $d,2d,\ldots,d^2$ and zero elsewhere. Conversely, subtracting
$d$ from exactly this staircase deletes its last part and shifts the
others down one place; appending $d^2$ restores it. An arbitrary tail
with parts at most $d$ is unaffected and makes the actual Durfee size
exactly $d$. This proves both directions. The empty partition is fixed.

Consequently, with $p_{\le d}(m)=0$ for $m<0$, the fixed-point count is

$$\mathbf1_{N=0}+\sum_{d\ge1}
 p_{\le d}\left(N-\frac{d^2(d+1)}2\right).$$

This uses ordinary bounded-part partition enumeration; it is a static
fixed-state result and does **not** count general inverse fibres.
For $N=24$, the $d=1,2,3$ contributions are $1,10,7$, totaling 18.
The independent implementation checks the characterization on every
partition in all 25 original boxes, including both directions.

All tested DSR cycles are fixed, but global convergence has not been
proved. In particular, Durfee size is not decreasing:
$(10,10)\mapsto(8,8,4)$ changes it from 2 to 3. Nor is the sum of
squares decreasing: $(2,2)\mapsto(4)$ increases it from 8 to 16.
The $N=4$ maximum entrance time is 4, refuting a guessed $N-1$ bound.
The old C11 Durfee-row rule sends $(2,2)$ to $(2,1,1)$; P113 sends it
to principal hooks $(3,1)$. No old clock transfers by the shared word
“Durfee.” Missing all-parameter time and independent inverse means
NO_PROMOTION despite the proved static characterization.

## 3. UPA: two large deductions, not an all-matrix theorem

Let $U$ denote exact-one integer-permanent cofactor feedback with the
transposed deleted-row/deleted-column convention from INTAKE.

### 3.1 Characteristic-two slice

For $n\le3$, each minor has order at most 2 and integer permanent in
$\{0,1,2\}$ (with the empty minor convention). Its permanent equals
one exactly when it is odd. In characteristic two determinant equals
permanent. Thus this entire slice is ordinary adjugation over
$\mathbb F_2$, already consumed by P103/Jacobi mechanisms. This does
not extend to order-three minors. The first lexicographic row-major-bit
sentinel in the original $n=4$ box is

$$A=\begin{pmatrix}1&1&1&0\\1&0&1&0\\1&1&0&0\\0&0&0&0\end{pmatrix}
\quad\text{(bits 855)}.$$

The top-left $3\times3$ minor has permanent 3. All other $3\times3$
minors vanish because they contain the zero fourth row or column.
Therefore $U(A)=0$, whereas characteristic-two adjugation has only
entry $(4,4)=1$ (bits 32768). The sentinel is inside the original box.

### 3.2 Unique-perfect-matching branch is the old UPC adapter

For permutation matrices $L,R$, cofactor covariance gives

$$U(LAR)=R^{-1}U(A)L^{-1}.$$

This follows by the row/column relabeling bijection of minor matchings;
no determinant sign or numerical approximation is involved.

Suppose $\operatorname{per}A=1$, and let $P$ be its unique perfect
matching. Then $B=AP^{-1}$ contains the identity matrix and has only
that perfect matching. The directed graph of $B-I$ has no directed
cycle: such a cycle, completed by the remaining diagonal loops, would
give another perfect matching. Thus a simultaneous permutation makes
$B=I+D$ with $D$ strictly upper triangular. This is exactly the static
triangularization in Izhakian–Rhodes, Lemma 3.2, and receives zero credit.

A partial matching deleting row $j$, column $i$ in $I+D$ consists of
one directed path $i\to j$ and identity loops at unused vertices.
There are no other cycles. Conversely each such path completes in
exactly that way. Diagonal cofactors have the identity as unique
matching. Hence

$$U(I+D)=I+V(D),$$

where $V$ is the old exactly-one-positive-path DAG map UPC.
Here the plus is disjoint Boolean support, not modulo-three feedback.
The previously proved UPC identity $V^4=V^2$ therefore gives
$U^4(B)=U^2(B)$. Cofactor covariance alternates the outer permutation:

$$U^{2r}(A)=U^{2r}(B)P,\qquad
 U^{2r+1}(A)=P^{-1}U^{2r+1}(B).$$

So $U^4(A)=U^2(A)$ throughout this invariant unique-matching branch.
This is a fully deducted adapter, not an independent temporal advance.
All 13,190 unique-matching states across $n=0,\ldots,4$ satisfy the
identity in the separate author check (the empty matrix is included).

The remaining matrices have zero or at least two perfect matchings.
No all-$n$ temporal classification or evaluated inverse for those
branches is proved here. The full $n=4$ finite profile has height 3
and periods at most 2, but does not establish either claim for $n>4$.

## 4. DP3: generic triangular reset/flip theorem is deducted

For $i<j$, write the positive-path count modulo 3 as

$$p_{ij}=a_{ij}+q_{ij}\pmod3,$$

where $q_{ij}$ counts paths of length at least two. Every edge in
such a path has span strictly smaller than $j-i$. For fixed lower
spans, the Boolean coordinate update $a\mapsto\mathbf1_{a+q=1\ (3)}$
is identity if $q=0$, flip if $q=1$, and constant zero if $q=2$.

**Generic bound.** Every trajectory on $n\ge2$ ordered vertices is
periodic after at most $2^{n-2}-1$ steps, with eventual period dividing
$2^{n-2}$. For $n=0,1$, the single graph is fixed.

**Proof.** Adjacent-edge coordinates never change. Suppose coordinates
of smaller span are periodic after time $T$ with a common period $L$,
a power of two. A coordinate of the next span then follows a periodic
word of identity, flip, and constant-zero updates. The composition
over one forcing period is identity, flip, or a constant map (possibly
constant one when a flip follows a reset). After at most one such
period, its stroboscopic orbit has period dividing 2; the full coordinate
sequence has period dividing $2L$. This holds simultaneously for every
coordinate of that span, since none depends on another of equal span.
Starting with $(T,L)=(0,1)$ and adding spans 2 through $n-1$ gives
$L=2^{n-2}$ and $T\le1+2+\cdots+2^{n-3}=2^{n-2}-1$.

This proof is a generic triangular Boolean-cascade argument. It is
neither a sharp pointwise clock nor a new path-residue-specific core,
so its temporal credit is deducted. All original graph boxes check
the stated coarse bound, but the proof, not those checks, gives all-$n$.

For one-step inversion by increasing span, once the lower edges of a
preimage are chosen, a target bit $b$ requires $a=b$ for $q=0$,
$a=1-b$ for $q=1$, and requires $b=0$ with $a$ free for $q=2$.
This is a branching decoder, not an evaluated fibre formula or a
separate residual inverse theorem. Counts, image, and extreme fibres
remain finite-pilot data. DP3 is not UPC: in the complete ordered DAG
on four vertices, the pair $0\to3$ has four paths and is kept by DP3
but not UPC. Both the generic deduction and that literal distinction
are needed; neither creates an independent paper axis.

## 5. BRF: named classical fibres do not close the system

The backward count includes the starting vertex, so each output lies
in $[1,n]$. Its value at a cycle vertex is the size of that entire
functional-graph component; at a noncycle vertex it is the size of
its incoming rooted subtree. This follows directly by splitting an
orbit into its incoming tree and terminal cycle.

For $n\ge1$, the fibre of $(n,\ldots,n)$ consists precisely of the
single directed $n$-cycles, giving $(n-1)!$ labeled self-maps.
For $n\ge2$, fix a vertex $i$ and prescribe backward count 1 at $i$
and $n$ elsewhere. Then the other vertices must form one directed
$(n-1)$-cycle, and $i$ must be a leaf pointing to any vertex of that
cycle. Conversely every such map has the prescribed counts. The
number is $(n-2)!(n-1)=(n-1)!$. At $n=1$ the two target descriptions
coincide and the fibre has size 1; at $n=0$ the empty fibre has size 1.

These are elementary functional-graph/Cayley-style counts. They do
not establish that these are the largest fibres for every $n$, nor
evaluate arbitrary subtree-size constraints. In particular the fact
that these targets maximize the fibre at tested $n=6$ is finite data.
The original boxes have cycles of lengths 3, 4, 5, and 8 at different
sizes. No all-$n$ core or clock is proved. NO_PROMOTION.

## 6. FFR: a static residual inequality, and a genuine 3-cycle

Suppose bin $i$ is opened before bin $j$. Any item $a$ assigned to
bin $j$ failed to fit in bin $i$ when processed. Unused capacities
can only decrease during the packing pass, so $a>r_i$, the final
residual of bin $i$. Also bin $j$ has final load at least $a$, so
$r_j\le M-a$. Therefore

$$r_i+r_j<M$$

for every two distinct bins. This is an elementary first-fit property;
at most one bin has residual at least $M/2$. The statement is vacuous
when there is at most one bin, covering capacity zero conventions.
It is not a theorem about iterating the residual vector.

Indeed within the original box $M=5,k=2$ there is the exact cycle

$$(1,1)\longmapsto(3,3)\longmapsto(2,2)\longmapsto(1,1).$$

The first and last transitions pack both items together; the middle
transition puts the two size-three items in separate bins. Thus any
claim that all FFR cycles have length at most two is false already
inside the intake. A bin-assignment feasibility decoder, by itself,
would remain a static first-fit reformulation. No all-parameter
temporal result and no separately evaluated inverse is supplied.

## 7. Excluded positivity-adjugate branch: why it was not piloted

For completeness, let $C(A)$ use positive rather than unique minor
permanents. If $A$ has a perfect matching $P$, then $B=AP^{-1}$ has
all diagonal entries. A partial matching cofactor is a directed path
plus disjoint cycles; a path can always be completed by identity
loops. Hence $C(B)=B^*$, the reflexive transitive closure. In a reflexive
transitive graph the same argument gives $C(B^*)=B^*$.
Permutation covariance yields

$$C(A)=P^{-1}B^*,\quad C^2(A)=B^*P,\quad C^3(A)=C(A).$$

This perfect-matching branch is an old closure wrapper. It was
excluded before the frozen intake and never piloted. No assertion
about the no-perfect-matching branch is made here. This exclusion
must not be confused with unique-permanent UPA, which was tested.
