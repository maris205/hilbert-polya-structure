# OTC proof package and bounded rejection

Author: scout33. No independent review, admission or paper number.

## Claim and status

The desired two-axis claim is: a structural classification of ALL recurrent
states of OTC on every labelled oriented carrier, and a separate structural
one-step inverse/fibre/extremal theorem for EVERY target.

Status: **NOT CURRENTLY JUSTIFIED**. The complete deductions below do not
establish either requested axis. They include zero-credit Boolean-power
restrictions, a restricted zero-fibre formula and explicit counterexamples
to two tempting global extrapolations. Disposition: **NO_PROMOTION**.

## Assumptions and notation

Fix $n\geq1$. An oriented graph $A$ on $[n]$ has no loop and at most one
direction on each unordered pair. We also write $A$ for its Boolean
adjacency matrix, with $A_{uv}=1$ for the arc $u\to v$. Products and powers
below are in the Boolean semiring (OR and AND), not over a field.

For $u\ne v$, put

$$F(A)_{uv}=(A^2)_{uv}\wedge\neg(A^2)_{vu},\qquad F(A)_{uu}=0.$$

A recurrent state satisfies $F^p(A)=A$ for some positive $p$; its period is
the least such $p$. For acyclic $A$, let $L(A)$ be its longest directed path
length in edges, including zero when it has no arc. The zero matrix is $0_n$.

## Strategy and dependency map

1. Boolean products represent exact-length directed walks; prove the needed
   walk identities directly. Primary sources identify this as old machinery.
2. Acyclicity rules out both reciprocal walks and loops, so OTC becomes
   unmodified Boolean squaring on this invariant subcarrier.
3. Odd cycles give a different invariant subcarrier, again ordinary powers.
4. A hand-derived circulant fixed point shows cancellation can persist on
   a recurrent state. This disproves extrapolation of Step 2 to the whole
   carrier; it is not a run at a larger cutoff.
5. The DAG portion of the zero fibre is bipartite edge enumeration. A
   separate four-vertex argument explains the measured zero-fibre count.
6. None of these statements depends on the pilot. Its complete $n\leq4$
   output pressures transcription only, not all-size truth.

## Proof 1: carrier closure and reachability subtraction

For distinct $u,v$, the Boolean expressions defining $F(A)_{uv}$ and
$F(A)_{vu}$ cannot both equal one. The diagonal is set to zero. Thus $F$ is
an autonomous self-map of the stated carrier.

Every arc of $F(A)$ has a directed two-walk in $A$. Concatenating such
witnesses shows that every positive-length walk in $F(A)$ has a walk in
$A$ with the same endpoints. Consequently the positive reachability
relation of $F(A)$ is contained in that of $A$. On a periodic orbit those
reachability relations must all coincide, because a finite descending cycle
of sets is constant. This is only a necessary invariant: constant
reachability does not imply fixed adjacency, no cancellation, or a clock.

## Proof 2: exact DAG time formula (old power mechanism)

Claim: for every acyclic $A$ and integer $t\geq0$,

$$F^t(A)=A^{2^t},\qquad
\min\{t\geq0:F^t(A)=0_n\}=\lceil\log_2(L(A)+1)\rceil.$$

Step 1. A positive diagonal entry of $A^r$ would witness a directed closed
walk. Opposite entries of $A^r$ would concatenate to one. Either gives a
directed cycle, contrary to acyclicity. Thus every positive power of $A$
is oriented. Its arcs remain within a topological ordering, so it is also
acyclic.

Step 2. The square of $A^{2^t}$ is $A^{2^{t+1}}$ by associativity. Step 1
shows there is nothing to cancel or remove from its diagonal. Induction
starting at $t=0$ proves the iterate identity.

Step 3. In a DAG every walk is a path. The matrix $A^r$ is zero exactly
when no path has length $r$. If $1\leq r\leq L(A)$, an initial segment of
a longest path witnesses a nonzero entry; if $r>L(A)$ none exists. The
first zero time is therefore the least $t$ with $2^t>L(A)$, which equals
the displayed ceiling. For $L(A)=0$ the graph is already zero and both
sides are zero. This entire temporal restriction is deducted as Boolean
matrix powers, not retained as OTC's all-carrier contribution.

## Proof 3: every positive period occurs in a subfamily

Let $m\geq3$ be odd, and identify the vertices with $\mathbb Z/m\mathbb Z$.
Start with the directed cycle $i\to i+1$. If a graph has the unique outgoing
arc $i\to i+a$ at every vertex and $a$ is invertible modulo $m$, its
two-walk relation consists of $i\to i+2a$. These arcs have no loops or
opposite pairs because $m$ is odd and $a$ is a unit. Hence induction gives

$$F^t(A):\quad i\longrightarrow i+2^t\pmod m.$$

Equality with the initial labelled graph is equivalent to $2^t\equiv1$
modulo $m$. Its exact period is $\operatorname{ord}_m(2)$. In particular,
$m=5$ has period four and $m=7$ has period three. More generally, for
$p\geq2$ use $m=2^p-1$: congruence holds at $p$, and for $0<q<p$ the
positive integer $2^q-1$ is smaller than $m$, so cannot be divisible by it.
Thus the exact period is $p$. The zero graph supplies period one.

This is an ordinary permutation-power construction. It refutes universal
fixed/two-cycle extrapolation, but does not classify recurrence on the
whole carrier. No $m>4$ instance was executed in the pilot.

## Proof 4: genuine cancellation at a nonempty fixed point

Claim: the oriented circulant on $\mathbb Z/15\mathbb Z$ with step set
$S=\{1,2,4,8\}$ is a nonempty fixed point of OTC, although $A^2\ne A$.

Step 1. The four negatives of $S$ are $14,13,11,7$, outside $S$, and zero
is outside $S$. Thus the graph is oriented.

Step 2. A two-walk has step $s+t$ with $s,t\in S$. The four doubled terms
are $2,4,8,1$, exactly $S$. The six unordered distinct sums are
$3,5,9,6,10,12$. Therefore

$$S+S=S\cup\{3,5,6,9,10,12\}\quad\text{in }\mathbb Z/15\mathbb Z.$$

Step 3. Each extra residue is paired with its negative:
$3\leftrightarrow12$, $5\leftrightarrow10$, $6\leftrightarrow9$.
None of the negatives of $S$ lies in $S+S$. OTC cancels exactly the six
extras and keeps precisely $S$. It follows that $F(A)=A$, whereas
$A^2\ne A$ since, for example, step three occurs only in the square.

Thus both proposed extrapolations “the only fixed state is empty” and
“every recurrent step has no cancellation and is ordinary squaring” are
false. They were exploratory proof ideas, not failed scientific commands
or prior claims accepted by a reviewer.

Step 4. Replace each of the 15 vertices by any nonempty labelled independent
class and replace every base arc by all arcs between the corresponding
classes. Existence of two-walks between different classes is exactly that
in the base graph; there are no two-walks returning to a class since the
base has no reciprocal pair. Thus OTC commutes with this blowup and these
graphs are fixed. Adding isolated vertices also commutes with OTC. This
gives nonempty fixed states for every $n\geq15$, but no claim that these
are all fixed states.

## Proof 5: restricted zero fibre, and its four-vertex boundary

For a general oriented $A$, the defining formula gives

$$F(A)=0_n\quad\Longleftrightarrow\quad A^2=(A^2)^{\mathsf T}.$$

This is an exact condition, NOT a structural all-target inverse theorem.
For acyclic $A$, Proof 2 strengthens it to $A^2=0_n$.

A graph has $A^2=0_n$ exactly when no vertex has both positive indegree and
positive outdegree. Its vertices therefore split uniquely into active
sources $S_0$, active sinks $T_0$, and isolates. Every arc goes from $S_0$
to $T_0$, and the bipartite incidence matrix has no zero row or column.
Conversely every such incidence matrix has no two-walk. If

$$b(s,t)=\sum_{i=0}^s\sum_{j=0}^t(-1)^{i+j}
\binom si\binom tj2^{(s-i)(t-j)},$$

inclusion–exclusion over missing rows/columns gives exactly $b(s,t)$ such
matrices. Consequently the complete DAG portion of the zero fibre has size

$$\sum_{s,t\geq0,\ s+t\leq n}
\frac{n!}{s!t!(n-s-t)!}\,b(s,t).$$

The empty-incidence conventions are $b(0,0)=1$ and $b(s,0)=b(0,t)=0$
for positive $s$ or $t$. This is standard bipartite graph enumeration,
deducted rather than claimed as a new inverse mechanism.

For $n=4$ this sum is
$1+12+12+12+4+4+6\cdot7=87$.
There are exactly six additional zero parents, namely the labelled directed
four-cycles. Here is a complete argument for the latter assertion.

Suppose $A^2$ is symmetric and $A$ has a directed triangle $a\to b\to c\to a$.
The reverse two-walk for every triangle arc then forces a forward two-walk
for that arc. Its intermediate vertex cannot be any of $a,b,c$; at four
vertices it must always be the single remaining vertex $x$. The two
requirements $a\to x\to b$ and $b\to x\to c$ would give opposite arcs
$x\to b$ and $b\to x$, impossible. Thus there is no directed triangle.

If there is any two-walk $a\to b\to c$, symmetry supplies $c\to x\to a$.
Looplessness and orientation force four distinct vertices. They form a
directed four-cycle. Adding a diagonal in either orientation creates a
directed triangle, which was just excluded. Hence the graph is precisely
that cycle. Conversely its square has the two antipodal pairs in both
directions and is symmetric. A labelled directed four-cycle has $4!/4=6$
possible cyclic orders. The full zero fibre at $n=4$ therefore has size
$87+6=93$, agreeing with the pilot. This does not establish maximality
for every $n$ or classify every target fibre.

## Proof boundary and final disposition

The finite pilot has 133 recurrent states at $n=4$, but it is not a formula
for arbitrary $n$. Proof 4 disproves a natural simplification of their
global structure. A general cycle decomposition incorporating persistent
reciprocal cancellation remains absent. For inverses, the tautological
Boolean condition and the restricted zero-fibre calculation do not provide
an all-target structural decoder, uniform extremal result or equality cases.

No source read here supplies those missing statements. No generic
inclusion–exclusion over all input graphs is promoted as a second axis.
The original bounded pilot is closed without enlargement. **NO_PROMOTION**;
this note does not self-admit a candidate or fill the final batch seat.
