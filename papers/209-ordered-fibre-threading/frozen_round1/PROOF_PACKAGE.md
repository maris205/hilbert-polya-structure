# Ordered fibre threading: paper-local proof package

2026-09-07 UTC. **PROVABLE AS STATED** for the three admitted theorems below.
This is an author exposition of the admitted deductions, not an independent
review or a new candidate gate. The original deductions belong to
nineteenth_finite_scout and root; the P209 writer is also a contributor.

## Claim, assumptions and notation

Let $n\ge0$, $[n]=\{0,\ldots,n-1\}$, and $X_n=[n]^{[n]}$. The empty
set has exactly one endofunction. Every label and its original total order
are retained. For a nonempty old fibre
$f^{-1}(v)=\{i_1<\cdots<i_k\}$, define $g=T(f)$ simultaneously by

$$g(i_j)=i_{j+1}\quad(j<k),\qquad g(i_k)=v.$$

Old fibres partition the domain, so this defines exactly one new value at
every coordinate. There is no within-step re-evaluation of a fibre.
Loops are permitted. No probability, quotient by graph isomorphism, or
choice of asynchronous schedule occurs.

The graph of $f$ has arrows $i\to f(i)$. A *vertex cycle* is a directed
cycle in this graph. Recurrence and period instead refer to the self-map
$T:X_n\to X_n$ on whole functions: $f$ is recurrent if $T^p(f)=f$ for
some positive $p$, and its period is the least such positive $p$.

**Theorem 1 (recurrent geometry and exact period).** A function is recurrent
if and only if each weak component of its graph is a directed cycle $C$
with pairwise disjoint unbranched noncycle paths feeding it, at most one
path at each cycle vertex. The final vertex $a$ of every nonempty such
path satisfies $a<\min C$. Internal path labels need not increase.
On this set, cycle and internal-path arrows stay unchanged, and each path
attachment moves one predecessor backwards on its cycle. The exact
whole-function period is

$$\operatorname{lcm}\{|C|:C\text{ has at least one nonempty feeding path}\},$$

where the empty least common multiple is one. A pure vertex cycle is
therefore fixed under $T$, even if its length exceeds one.

**Theorem 2 (every target's inverse).** For $g\in X_n$ let
$E_+(g)=\{i:i<g(i)\}$. A subset $S\subseteq E_+(g)$ is admissible when
the values $(g(i))_{i\in S}$ are pairwise distinct and the values
$(g(j))_{j\notin S}$ are pairwise distinct. The selected arrows
$i\to g(i)$, $i\in S$, form disjoint increasing paths, including
singleton paths. If $e_S(i)$ is the final vertex of the selected path
containing $i$, then

$$f_S(i)=g(e_S(i))$$

is a bijection from admissible subsets to $T^{-1}(g)$. In particular, a
target with no admissible subset has an empty inverse fibre.

**Theorem 3 (unique maximum).** For $n\ge1$,

$$\max_{g\in X_n}|T^{-1}(g)|=2^{n-1},$$

uniquely at $g_*(i)=i+1$ for $i<n-1$ and $g_*(n-1)=0$. At $n=0$ the
unique target has one predecessor, and the $n=1$ formula gives one as well.

## Strategy and dependency map

Theorem 1 uses all backward-image sets, not only rank or first-image size:
old walks expand into new walks; inclusions around a recurrent orbit
become equalities; the resulting fixed finite/infinite vertex heights
force a next sibling onto a vertex cycle; this forces path geometry and
the label condition. Explicit rotation proves sufficiency and exact period.

Theorem 2 instead recovers each old fibre as a selected increasing path.
Its two distinctness conditions enforce disjoint paths and forbid merging
their reconstructed fibre values. It does not use Theorem 1. Theorem 3
uses only Theorem 2 and the equality cases of its Boolean bound.

All arguments below hold for each fixed $n$ without a numerical cutoff.
The empty case is separate wherever a vertex is chosen.

## Proof

### 1. Expand every old walk

An old arrow $i_j\to v$ in a fibre is replaced in the new graph by

$$i_j\to i_{j+1}\to\cdots\to i_k\to v.$$

This is a directed walk of positive length, not necessarily a simple
path: its destination may already be a fibre member. Concatenating the
replacements for an old walk of length $r$ ending at $v$ produces a new
walk of length at least $r$ ending there. Its final $r$ arrows witness

$$I_r(f):=f^r([n])\subseteq I_r(Tf)\qquad(r\ge0).\tag{1}$$

In this notation $f^r$ means vertex-map composition, not $T^r$.
Every new arrow joins vertices in a single old weak component. Conversely
the replacement connects the endpoints of each old arrow. Thus the weak
component vertex sets are preserved exactly. This connectivity argument is
an old path-substitution primitive; it is not a separate contribution.

### 2. Freeze heights before comparing coordinate heads

For a vertex $v$ define its backward height by

$$h_f(v)=\sup\{r\ge0:v\in I_r(f)\}\in\{0,\ldots,n-1\}\cup\{\infty\}.$$

The sets $I_r(f)$ decrease with $r$. On a finite graph, $h_f(v)=\infty$
exactly at the vertex cycles: one can continue backwards around a cycle
arbitrarily many times; conversely an arbitrarily long walk ending at $v$
repeats a vertex and hence contains a cycle, whose forward iterates remain
on that cycle. For an off-cycle vertex, $h_f(v)$ is the largest length of
a directed path ending at $v$. Order $\infty$ above every finite value.

Suppose $T^p(f)=f$. Applying (1) for each fixed $r$ around the $p$-step
orbit forces equality at every step. Therefore the height at each labelled
vertex is independent of the epoch; write it as $h(v)$. The vertex-cycle
set $C_\infty=\{v:h(v)=\infty\}$ is fixed as a set as well.

For an arrow $j\to v$ in any epoch, if $v$ is off-cycle then so is $j$,
and appending that arrow to a longest backward path into $j$ gives
$h(v)\ge h(j)+1$. If $v$ is on a cycle then $h(v)=\infty$. Hence

$$h(j)\le h(v),\qquad h(j)=h(v)\Longrightarrow h(j)=h(v)=\infty.\tag{2}$$

Fix a source coordinate $i$. If it is maximal in its old fibre, its head
is unchanged. Otherwise let $j$ be its next old sibling and $v=f(i)=f(j)$.
The new head is $j$, so (2) gives

$$h((Tf)(i))\le h(f(i)).\tag{3}$$

This comparison is now valid with the **same** height function at every
epoch; that fact was proved before (3). As the labelled head sequence is
periodic, it cannot have a strict drop. In the nonmaximal case equality
in (2) forces $j$ onto a vertex cycle. This includes $j=v$, when the
selected arrow happens to have the same numerical head before and after
threading. Selecting an arrow and changing its value are different notions.

### 3. Necessity of the geometry and label bound

A fibre contains at most one cycle vertex: a cycle target has exactly one
cycle predecessor, while an off-cycle target has none. Every member of an
ordered fibre after its first is the next sibling of the preceding member,
so Step 2 puts it on a cycle. It follows that a fibre has size at most two;
a two-member fibre consists of a smaller noncycle vertex and a larger
cycle vertex. Its target lies on the latter's cycle.

An off-cycle vertex thus has indegree at most one. A cycle vertex has at
most one additional noncycle predecessor. Following the unique outgoing
arrows from any off-cycle vertex eventually reaches a cycle, and backwards
the indegree condition allows no merge or branch. The off-cycle vertices
therefore form pairwise disjoint directed paths, at most one ending at each
cycle vertex. Cycle arrows are retained because their sources are maximal
in their fibres. Internal-path arrows are retained because their targets
have singleton fibres.

Let $a$ be a final path vertex with $f(a)=v\in C$, and let $u$ be the
cycle predecessor of $v$. The two-member fibre of $v$ is ordered $(a,u)$,
so $T(f)(a)=u$. Cycle arrows remain unchanged at every epoch. Iterating
this rule moves the attachment through every vertex of $C$. At each epoch
$a$ must be below the corresponding cycle predecessor. These predecessors
run through all of $C$, so $a<\min C$. This proves necessity in Theorem 1.

### 4. Sufficiency and the exact labelled period

Assume the geometry and label condition of Theorem 1. Every path-final
vertex lies below the cycle predecessor sharing its target. Thus the fibre
rule fixes every cycle arrow and every internal-path arrow, and moves every
attachment to its cycle predecessor. Distinct attachments stay distinct
because the predecessor map on the cycle is bijective. The conditions
persist, and after $|C|$ updates all attachments on $C$ return.

If a component has no path, all its fibres are singleton and it is fixed.
If it has a nonempty path, fix one final labelled vertex $a$. Its head
successively visits all $|C|$ distinct cycle labels, so it first returns
after exactly $|C|$ updates. Therefore that component has exact period
$|C|$, without quotienting by a rotational symmetry of an unlabelled graph.
Components update independently on preserved vertex sets. The entire
function returns exactly when all attached components return, giving the
least common multiple in Theorem 1. The empty function has period one.

### 5. Recover every one-step source

First suppose $T(f)=g$. Select every nonmaximal member of every nonempty
old fibre; call the set $S_f$. The selected $g$-arrows are exactly the
consecutive increasing links within the ordered fibres. Thus they form
disjoint increasing paths, their heads are distinct, and their endpoints
are exactly the fibre maxima. At each endpoint the old fibre value is
retained. Distinct old fibres have distinct values, so the endpoint values
are also distinct. Therefore $S_f$ is admissible, and
$f(i)=g(e_{S_f}(i))$.

Conversely, let $S$ be admissible. Each selected vertex has one outgoing
selected arrow, and every vertex has at most one incoming selected arrow
by distinctness of heads. Every selected arrow strictly increases its label,
so a selected directed cycle is impossible. The selected graph is a
disjoint union of paths and singletons; its endpoints are exactly the
vertices outside $S$. Define $f_S(i)=g(e_S(i))$. Endpoint-value
distinctness makes the fibres of $f_S$ exactly these path vertex sets,
not unions of multiple paths. Their increasing order agrees with their
path order. Threading them therefore restores the selected $g$-arrows,
and at each endpoint restores the retained $g$-arrow. Hence $T(f_S)=g$.

The nonmaximal members of the fibres of $f_S$ recover exactly $S$, so the
construction is injective as well as surjective. For example $f=(1,1)$
has $T(f)=(1,1)$, but its correct code still selects coordinate $0$.
For the empty target the empty subset is admissible and reconstructs the
empty function. This completes Theorem 2, including zero fibres.

### 6. Maximum and equality

For $n\ge1$ the largest label cannot be eligible. Theorem 2 gives

$$|T^{-1}(g)|\le 2^{|E_+(g)|}\le2^{n-1}.\tag{4}$$

For $g_*$ the eligible arrows are the increasing chain through all labels.
Every subset has distinct heads, and all endpoint values are distinct
because $g_*$ is a permutation. Thus every one of its $2^{n-1}$ subsets
is admissible, giving equality.

Conversely equality in (4) forces $|E_+(g)|=n-1$ and every subset to be
admissible. The empty subset then says that $g$ itself is a permutation.
Every $i<n-1$ satisfies $g(i)>i$. Descending from $i=n-2$, injectivity
forces $g(n-2)=n-1$, then $g(n-3)=n-2$, and finally $g(0)=1$.
The sole remaining value is $g(n-1)=0$. At $n=1$ the single permutation
is already $(0)$; at $n=0$ the empty function has one predecessor.
This proves Theorem 3. ∎

## Corrections, bounded evidence and open risks

No admitted statement is weakened or extended. There is no appeal to an
external theorem as a hidden proof premise. Ordinary functional-graph
decomposition, path substitution, subset counting and rotation/LCM are
background. [SOURCE_AUDIT.md](SOURCE_AUDIT.md) records the exact source and
historical subtraction, with bounded reading/search scope.

The paper-local verifier will check only the original $n=0,\ldots,5$
boxes. Its observed orbit entrance indices are not a sharp all-size clock
theorem. No general-time inverse, recurrent generating function,
arbitrary-size period census, global owner-nonexistence or publication
priority follows. Candidate admission remains revisable if manuscript
review identifies a complete owner adapter or a substantive defect.
