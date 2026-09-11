# Proof package — branch-gated grandparent rewiring (BGR)

Author/proof contributor: `/root/round211_functional_surgery_residual`.
2026-09-09 UTC. One literal desk attempt; zero scientific executions.
This is an author deduction, not an independent candidate or manuscript review.

## Claim

On all labelled endofunctions, the literal BGR map below has the following
deductively established properties:

1. Its complete fixed locus consists of bare nonloop cycles and loop-rooted
   components in which every vertex at depth at least two has at most one
   child. Its fixed-state exponential generating function is
   $$\mathcal F(z)=\frac{\exp\!\left(z\exp\!\left(z\exp\!\left(\frac z{1-z}\right)\right)-z\right)}{1-z}.$$
2. Uniformly leaf-decorated permutation sectors are invariant and execute
   exactly ordinary permutation squaring. Their entrance times and periods
   are the classical valuation/order formulas proved below.
3. Every permutation target has exactly one BGR predecessor, itself.
4. For the constant target $s_r(v)=r$ on $n\ge1$ labels, the complete fibre
   has size $n$ when $n\ge3$, and size one when $n\le2$, with every
   predecessor explicitly specified in Step 5.

## Status

**PROVABLE AS STATED** for Claims 1–4.

**NOT CURRENTLY JUSTIFIED** for a complete temporal/recurrent theorem on the
whole carrier, a general image or every-target inverse theorem, a global
maximum-fibre theorem, or a new two-axis contribution after subtraction.
Disposition: **NO_PROMOTION / ZERO_RESERVES / HOLD_EXTERNAL**.

## Assumptions and notation

For $n\ge0$, let $V_n=\{0,\ldots,n-1\}$ and
$\mathcal X_n=V_n^{V_n}$. At $n=0$, this carrier contains its unique empty map.
For $f\in\mathcal X_n$, write
$$d_f(v)=|\{u\in V_n:f(u)=v\}|.$$
Define one simultaneous autonomous tick by
$$B(f)(v)=
\begin{cases}
f(f(v)),&d_f(v)\ge2,\\
f(v),&d_f(v)\le1.
\end{cases}\tag{1}$$
All right-hand sides refer to the old $f$. Only the outgoing edge at an
old branching vertex is bypassed to its grandparent; there is no sequential
sweep, tie choice, register, nil, external schedule or loss of vertex labels.
No private leaves are added to the carrier by the update: the decorated
states in Step 3 are existing states used only to prove an invariant-sector
subtraction.

A child of $v$ in a loop-rooted component is a nonroot vertex pointing to
$v$; the root's self-loop is not one of its tree children. Depth is distance
to that root. A bare nonloop cycle has length at least two and no attached
vertices. A recurrent state means a periodic state of $B$, not merely an
eventually periodic state. Exponential generating functions count labelled
states, not isomorphism types. All power series are formal.

## Proof strategy

Read the fixed equation locally, decompose its functional graph, and count
that static structure. Separately expose an injective decorated-permutation
embedding and subtract its known power dynamics. For inverse claims use
rank monotonicity or a direct forbidden-predecessor argument. No finite
census, asymptotic observation, source search non-hit or program is a premise.

## Dependency map

1. Step 1 uses only positive forward jumps in (1).
2. Step 2 uses the fixed equation and the finite functional-graph
   decomposition; its count uses ordinary labelled sequences, sets and cycles.
3. Step 3 uses a direct invariant-sector calculation and elementary integer
   divisibility. The sector's classical square-root enumeration is sourced
   separately, not credited as a new theorem.
4. Step 4 uses Step 1 and the indegree-one permutation slice.
5. Step 5 uses (1) at a target-constant vertex and then at its predecessors.

## Proof

### Step 1. Closure and the exact scope of the support observations

Each output in (1) is an old vertex, so $B$ is a self-map of the stated
finite carrier, including the empty map. Every output is an old positive
iterate of its argument. Therefore
$$\operatorname{im}B(f)\subseteq\operatorname{im}f.\tag{2}$$
Each new edge is represented by a directed old path of length one or two;
it stays inside one old weak component. A new directed cycle concatenates
to a positive closed old directed walk, and every vertex on that walk is
old-cyclic. Thus weak components may split but do not merge, and cyclic
vertex support cannot increase. Relabelling commutes with (1), because
indegrees and composition commute with bijective relabelling.

These are precisely the old forward-jump support arguments in DFJ. They
are not a full time theorem: Step 3 supplies states with constant image,
constant cyclic support and a genuine period-three orbit.

### Step 2. Complete fixed locus and its labelled count

The equation $B(f)=f$ is equivalent to
$$d_f(v)\ge2\quad\Longrightarrow\quad f(f(v))=f(v).\tag{3}$$
Thus every branching vertex must point to a fixed vertex of $f$.

On a nonloop directed cycle, the parent of a cycle vertex is not fixed.
Equation (3) forces its indegree to be one; its incoming cycle edge already
accounts for that one predecessor. No attached tree is therefore possible,
and the component is a bare cycle. Conversely every bare cycle satisfies
(3), since all indegrees are one.

Consider a component with a loop root $r$. A nonroot vertex $v$ of depth
at least two does not point to $r$, and its parent is not fixed. Hence
it has at most one child. At depth one there is no child-number constraint,
since its parent is the fixed root. The root itself satisfies (3) regardless
of its child count. Conversely every loop-rooted tree with these stated
restrictions satisfies (3) at every vertex. This proves the classification
in both directions; it does not classify nonfixed recurrent states.

For its EGF, a nonempty directed chain on $k$ prescribed labels has $k!$
linear orders, so its EGF is
$$P(z)=\sum_{k\ge1}z^k=\frac z{1-z}.$$
Each child of the loop root has an unordered collection of such chains
below it. Thus its rooted branch EGF is
$$D(z)=z\exp(P(z)).$$
The loop root has an unordered collection of those branches, giving
$$R(z)=z\exp(D(z)).$$
The bare directed cycles of lengths at least two have connected EGF
$\sum_{k\ge2}z^k/k=-\log(1-z)-z$. A fixed endofunction is an unordered
labelled set of these two component types. Consequently
$$\mathcal F(z)=\exp\left(R(z)+\sum_{k\ge2}\frac{z^k}{k}\right)
=\frac{\exp(R(z)-z)}{1-z},\tag{4}$$
which is exactly the formula in Claim 1. The constant term one is the
empty map. This proof supplies no experimental coefficient check and no
new credit for the labelled SET/SEQ/CYC identities.

### Step 3. The apparently rigid temporal sector is an old power map

Fix a prescribed core $C$ with $c\ge1$ labels and pairwise disjoint private
label sets $L_x$ of a common size $r\ge1$ for $x\in C$. Let the whole label
set be $C\sqcup\bigsqcup_{x\in C}L_x$. For $\pi\in S_C$, define
$$\Phi_r(\pi)(x)=\pi(x)\ (x\in C),\qquad
\Phi_r(\pi)(\ell)=x\ (\ell\in L_x).$$
The embedding $\Phi_r$ is injective because its restriction to $C$ recovers
$\pi$. Every private leaf has indegree zero. Every core vertex has one
incoming permutation edge and $r$ incoming leaf edges, so its indegree is
$r+1\ge2$. Formula (1) therefore gives
$$B(\Phi_r(\pi))=\Phi_r(\pi^2),\qquad
B^t(\Phi_r(\pi))=\Phi_r(\pi^{2^t})\quad(t\ge0).\tag{5}$$
Since $\pi^2$ is again a permutation, the same indegrees persist and the
iteration identity follows by induction. It is an exact conjugacy onto an
invariant sector, not a full-carrier conjugacy and not a new candidate.

Let the order of $\pi$ be $L=2^aM$, with $M$ odd, and put
$\operatorname{ord}_1(2)=1$. Equality of the states at times $t$ and
$t+p$, for $p\ge1$, is equivalent by injectivity to
$$L\mid 2^t(2^p-1).$$
The second factor is odd, so this requires $t\ge a$. Since $M$ is odd,
the remaining condition is $M\mid 2^p-1$. Hence the exact entrance time
of this sector state is $a$ and its exact eventual period is
$\operatorname{ord}_M(2)$. These are the ordinary permutation-squaring
formulas already proved in the DFJ original.

For a direct symbolic obstruction, take $C=\{0,\ldots,6\}$, one leaf
$7+x$ at each $x$, and $\pi=(0\,1\,2\,3\,4\,5\,6)$. The successive
core permutations are $\pi,\pi^2,\pi^4,\pi$, with unchanged leaf arrows.
They are distinct, proving exact period three on fourteen labels without
an execution. Image and cyclic support remain $C$ throughout. This rules
out universal eventual fixedness or eventual period at most two; it does
not classify the rest of the carrier.

When $r=0$, the bare-permutation slice is instead fixed pointwise by (1),
because its indegrees are one. This boundary is essential and is not
covered by (5). It distinguishes BGR literally from DFJ, whose bare
permutations square.

For a target $\Phi_r(\sigma)$, predecessors **restricted to this same
fixed decorated sector** correspond exactly to $\pi^2=\sigma$. Their
counts are the classical permutation square-root counts, covered by the
primary theorem recorded in SOURCES_AND_SUBTRACTION.md. No assertion is
made that all full-carrier predecessors lie in that sector.

### Step 4. All permutation-target fibres are singletons

Let $\sigma\in S_{V_n}$ and suppose $B(f)=\sigma$. Equation (2) implies
$|\operatorname{im}f|\ge n$, hence $f$ is a permutation. Every indegree
is then one, so (1) gives $B(f)=f$. Thus $f=\sigma$. Conversely $\sigma$
is fixed by (1), proving
$$B^{-1}(\sigma)=\{\sigma\}.\tag{6}$$
This includes the empty permutation and every $n\ge0$.

### Step 5. Every constant-target predecessor, including small sizes

Fix $n\ge1$ and $r\in V_n$, and suppose $B(f)=s_r$. If there were a
vertex $v\ne r$ with $f(v)\ne r$, (1) at $v$ would force
$d_f(v)\ge2$ and $f(f(v))=r$. For any $u$ with $f(u)=v$, the unchanged
branch at $u$ cannot return $r$, because $v\ne r$. Its changed branch
would return $f(v)\ne r$ and also cannot return $r$. Thus $v$ has no
predecessor, contradicting $d_f(v)\ge2$. It follows that
$$f(v)=r\qquad\text{for every }v\ne r.\tag{7}$$

If $f(r)=r$, the source is the star $s_r$, which is fixed. Otherwise put
$f(r)=u\ne r$. In the source specified by (7), vertex $r$ has indegree
$n-1$, vertex $u$ has indegree one, and every remaining vertex has
indegree zero. All nonroot outputs are therefore $r$. The root output is
$f(f(r))=r$ precisely when $n-1\ge2$; if $n\le2$, the root keeps its
old output $u\ne r$ and fails the target condition.

Thus, defining $f_{r,u}(v)=r$ for $v\ne r$ and $f_{r,u}(r)=u$, we have
the explicit complete formula
$$B^{-1}(s_r)=
\begin{cases}
\{s_r\},&n=1,2,\\
\{f_{r,u}:u\in V_n\},&n\ge3.
\end{cases}\tag{8}$$
The choices of $u$ give different source functions, so their cardinalities
are exactly as claimed. At $n=0$ there is no distinguished constant target;
the unique empty-map fibre was already included in (6).

Claims 1–4 follow. ∎

## Corrections or missing assumptions

No pilot or global period-one/two conjecture was used. The period-three
state above is a deductive counterexample, not a finite census. The EGF
counts fixed points only, not all recurrent states. The square-root inverse
in Step 3 is sector-restricted; (6) and (8) are full-carrier fibres but cover
only permutation and constant targets. No global maximal-fibre value or
equality class has been inferred from (8).

## Open risks and disposition

There is no full-carrier temporal theorem beyond generic support nesting
and known invariant power sectors. There is no evaluated general inverse,
image or extremal theorem beyond the elementary special targets above.
Static fixed-component counting cannot replace the missing temporal axis.
The local selector differs from DFJ, LLG and HDA, but literal difference is
not a two-axis contribution. BGR closes **NO_PROMOTION** now; it is not a
reserve awaiting a larger cutoff. No second literal is proposed.

The author of this package contributed the fixed-locus derivation, the
explicit star-fibre argument and these subtraction proofs, and cannot later
review a resulting BGR manuscript as an independent nonauthor.
