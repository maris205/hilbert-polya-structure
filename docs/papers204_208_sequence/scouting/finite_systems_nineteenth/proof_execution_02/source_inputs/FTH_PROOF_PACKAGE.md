# Ordered fibre threading: complete author theorem package

Date: 2026-09-06 UTC. Author: nineteenth_finite_scout.
Root is also a contributor: after reading the intake, root independently
supplied component preservation, the fixed-fibre test, the noncreation of
weak-backward arrows, and the exact indegree/image identity. The first two
were independently present in this scout's initial checker before root's
message. The recurrent-height proof and path-cover inverse below were
developed by this scout. Neither contributor can independently review a
paper using these deductions.

## Claim and status

**PROVABLE AS STATED** for Theorems 1-3 below, on all endofunctions of every
finite linearly ordered labelled set $[n]$. The literal map is FTH in
[INTAKE.md](INTAKE.md), with no change of boundary or parameters.

This is a completed author proof, not candidate admission, independent
review, a proved sharp entrance clock, or global novelty clearance.
The observed global heights $0,0,1,2,3,4$ through $n=5$ do not establish
the conjectural $n-1$ clock. That sharper claim is excluded from this
contract. Only the original $n=0,\ldots,5$ boxes may be checked numerically.

### Theorem 1: exact recurrent carrier and period

A function $f$ is recurrent under $T$ if and only if every weak component
of its functional digraph has the following form:

1. a directed cycle $C$, whose length may be one;
2. vertex-disjoint directed paths feeding that cycle, with at most one path
   attached at each cycle vertex, and no branching at any noncycle vertex;
3. the final vertex $a$ of each nonempty feeding path (the vertex with
   $f(a)\in C$) satisfies $a<\min C$.

Cycles and every arrow internal to a feeding path are unchanged by $T$.
Each final path vertex moves its attachment one predecessor backwards
around its own directed cycle. Therefore the exact period is

$$\operatorname{lcm}\{|C|: C\text{ carries a nonempty feeding path}\},$$

with the least common multiple of an empty family equal to one. In
particular, a component that is a pure cycle is fixed, regardless of its
cycle length. Labels are retained; path attachments are not quotiented by
cycle rotation or graph isomorphism.

### Theorem 2: every target as increasing path covers

For any target $g:[n]\to[n]$, put

$$E_+(g)=\{i\in[n]:i<g(i)\}.$$

For $S\subseteq E_+(g)$ draw just the arrows $i\to g(i)$ with $i\in S$.
Call $S$ admissible if:

- the selected heads $g(i)$, $i\in S$, are pairwise distinct;
- the target values $g(j)$ at all path endpoints $j\notin S$ are
  pairwise distinct.

The selected graph is then a disjoint union of strictly increasing paths,
including singleton paths. If $e_S(i)$ is the endpoint of the selected
path containing $i$, then

$$f_S(i)=g(e_S(i))$$

is a bijection from admissible subsets $S$ onto $T^{-1}(g)$. Hence this is
a target-resolved fibre formula with a nonredundant structural code; an
inadmissible target has zero such codes. No search over arbitrary source
functions appears in the formula.

### Theorem 3: unique sharp maximum

For every $n\ge1$,

$$\max_g|T^{-1}(g)|=2^{n-1}.$$

The unique maximizing target is

$$g_*(i)=i+1\quad(0\le i<n-1),\qquad g_*(n-1)=0.$$

For $n=0$ the unique empty target has one predecessor. The $n=1$ formula
also gives the unique singleton target and fibre one.

## Assumptions, notation and dependency map

Functional-graph cycles refer to $f$ acting on vertices, whereas recurrence
and period refer to $T$ acting on **whole functions**. These are different
finite dynamical systems. Every vertex has one outgoing arrow; loops count
as cycles of length one. All comparisons use the original total order.

Write $I_k(f)=f^k([n])$ for $k\ge0$. Define the backward height

$$h_f(v)=\sup\{k\ge0:v\in I_k(f)\}\in\{0,\ldots,n-1\}\cup\{\infty\}.$$

Here $h_f(v)=\infty$ exactly on the directed cycles of $f$. Off the cycles
it is the largest length of a directed path ending at $v$. Order $\infty$
above all finite heights.

Dependencies:

1. Expanding each old arrow to a fibre-suffix path proves every image-set
   inclusion $I_k(f)\subseteq I_k(Tf)$.
2. Periodicity freezes all vertex backward heights. Comparing the heights
   of old and new arrow heads forces all sibling successors onto cycles.
3. That forces the path/cycle geometry; backward attachment motion forces
   the label bound. Conversely that geometry evolves by explicit rotation.
4. Strictly increasing selected arrows and injective endpoint values give
   the complete inverse independently of the recurrent classification.
5. The inverse code has at most $n-1$ optional edges. Equality forces the
   unique cyclic successor target.

## Proof

### Step 1. Local identities and expansion of every old walk

Let $f^{-1}(v)=\{i_1<\cdots<i_k\}$. The old arrow $i_j\to v$ can be
replaced in the new graph by the directed walk

$$i_j\to i_{j+1}\to\cdots\to i_k\to v.$$

The walk has at least one edge, even when labels repeat at its final
destination. Concatenating these replacements turns every old length-$r$
walk ending at $v$ into a new walk of length at least $r$ ending at $v$.
Its final $r$ arrows witness $v\in I_r(Tf)$. Therefore

$$I_r(f)\subseteq I_r(Tf)\qquad(r\ge0). \tag{1}$$

Each new arrow joins vertices in a single old weak component. Conversely,
the displayed replacement walk connects the endpoints of every old arrow.
The vertex sets of weak components are thus exactly preserved.

For completeness, root's exact one-step identity is

$$\deg^-_{Tf}(j)=\mathbf1_{j\in I_1(f)}+
\mathbf1_{j\ne\min f^{-1}(f(j))}. \tag{2}$$

The first summand comes from the maximum old predecessor of $j$, retaining
its target $j$. The second comes from the unique preceding sibling of $j$
in its own old fibre. These two sources cannot coincide: the latter is
not the maximum of its fibre, while the former is. Consequently every
image has indegree at most two, and $I_1(f)\subseteq I_1(Tf)$. Any changed
arrow has strictly larger head than source, so weak-backward arrows
$i\to v$ with $v\le i$ can disappear but cannot be newly created.

### Step 2. Heights freeze on a recurrent orbit

Suppose $T^p(f)=f$ for some $p\ge1$. Applying (1) around this finite
cycle forces equality at every step for every $I_r$. Thus $h_{T^t f}(v)$
is independent of $t$ at each vertex $v$; denote this fixed height by
$h(v)$. The cycle vertex set $C_\infty=\{v:h(v)=\infty\}$ is also fixed.

If an old arrow $j\to v$ ends at a noncycle vertex, then
$h(v)\ge h(j)+1$. If $j$ is a cycle vertex, its image $v$ is a cycle
vertex. Thus for every old arrow,

$$h(j)\le h(v),\qquad
h(j)=h(v)\Longrightarrow h(j)=h(v)=\infty. \tag{3}$$

Fix a source coordinate $i$. Either its image is unchanged, or its new
image is the next sibling $j$ and $f(j)=f(i)=v$. Equation (3) gives

$$h((Tf)(i))\le h(f(i)). \tag{4}$$

The same inequality holds at every epoch because the vertex heights have
already been proved fixed. A periodic finite sequence cannot decrease
strictly and then return. Consequently every selected next-sibling head
$j$ must have infinite height, including the case $j=v$ when an inserted
arrow happens to equal the old one.

### Step 3. Necessary recurrent geometry

An old fibre contains at most one cycle vertex: a cycle vertex has exactly
one predecessor on its own cycle, and no cycle points to a noncycle vertex.
Every element after the first in an ordered fibre is a selected next-sibling
head and hence, by Step 2, a cycle vertex. Therefore each fibre has at most
two members. A two-member fibre consists of a smaller noncycle vertex
followed by the unique cycle predecessor of its target.

It follows that every noncycle vertex has indegree at most one, while each
cycle vertex has at most one noncycle predecessor. Since each noncycle
vertex eventually reaches a cycle, its noncycle component is a directed
path. Distinct such paths cannot merge off the cycle, and at most one is
attached to each cycle vertex. Cycle arrows are retained, because their
source is the maximum member of the corresponding fibre. Arrows internal
to each path are retained because their target has a singleton fibre.

If a path-final vertex $a$ currently points to $v\in C$, its fibre sibling
is the cycle predecessor $u=f|_C^{-1}(v)$. The next attachment is $u$.
The cycle permutation is unchanged at every epoch. Thus the attachment
visits every vertex of $C$. For $a$ to remain the smaller member of every
such fibre, it is necessary that $a<\min C$. This proves all three
conditions of Theorem 1.

### Step 4. Sufficiency and exact period

Assume the stated geometry and label bound. Each cycle predecessor exceeds
each path-final vertex attached to its target. Thus the literal fibre rule
retains all cycle/internal-path arrows and moves each path attachment to
its cycle predecessor. Distinct attachments stay distinct because the
cycle predecessor map is a bijection. Every condition is preserved, and
after $|C|$ steps every attachment on $C$ returns.

A component without a path does not change. In a component with at least
one path, choose its final labelled vertex $a$. Its image returns for the
first time after exactly $|C|$ steps; no quotient identifies different
labels or phases. The component period is therefore exactly $|C|$.
Disjoint components update independently, so their joint period is the
least common multiple in Theorem 1. The empty function is fixed and obeys
the empty-family convention.

### Step 5. Complete and nonredundant path-cover inverse

Let $T(f)=g$. Select every source except the maximum in each old fibre;
call the selected set $S_f$. Its selected arrows in $g$ are exactly the
consecutive increasing links of that fibre. Thus $S_f\subseteq E_+(g)$,
their heads are distinct, and the selected graph is a disjoint union of
paths. The endpoint of each path is the maximum of one old fibre; its
retained target is the old fibre value. Different old fibres have different
values, proving injectivity of endpoint targets. The reconstruction formula
$f(i)=g(e_{S_f}(i))$ follows.

Conversely, take an admissible $S$. Since every selected arrow is increasing,
there are no selected cycles. Outdegree is at most one by construction and
indegree is at most one by the distinct-head condition, so every component
is an increasing path or singleton. Define $f_S$ by its endpoint value.
The distinct-endpoint-values condition makes its fibres exactly these
path vertex sets, with no unintended merger. Threading each such fibre
reproduces its selected $g$ arrows and the endpoint's retained $g$ arrow.
Hence $T(f_S)=g$. Recovering $S$ as all nonmaximal members of the fibres
of $f_S$ proves injectivity, including arrows whose numerical value happened
not to change under threading. This proves Theorem 2.

### Step 6. Sharp maximum and every equality case

The largest label $n-1$ cannot belong to $E_+(g)$. Theorem 2 therefore gives

$$|T^{-1}(g)|\le2^{|E_+(g)|}\le2^{n-1}. \tag{5}$$

For $g_*$ the eligible arrows form the increasing chain
$0\to1\to\cdots\to n-1$. Every subset has distinct selected heads.
All endpoint target values are distinct because $g_*$ is a permutation.
Thus every one of the $2^{n-1}$ subsets is admissible.

If equality holds in (5), all $n-1$ labels below $n-1$ are eligible and
every subset is admissible. In particular, the empty subset is admissible,
so $g$ is a permutation. The inequalities $g(i)>i$ for $i<n-1$ force,
working down from $i=n-2$, $g(n-2)=n-1$, then $g(n-3)=n-2$, down to
$g(0)=1$. The remaining image is $g(n-1)=0$. This is precisely $g_*$,
proving uniqueness. The cases $n=0,1$ were explicitly stated above. ∎

## Exact old-adapter subtraction and remaining risks

- Classical star-to-chain graph linearization is the local operation owner.
  A proof of sorted undirected-list convergence is **not** being transferred:
  FTH permits labelled nontrivial whole-function periods. The source body
  and the restricted-source/value comparison remain necessary gate inputs.
- FSP is not FTH: for a permutation FSP outputs identity, while FTH fixes
  every permutation. More strongly $f=(0,0)$ and $f=(1,1)$ have the same
  kernel but FTH outputs $(1,0)$ and $(1,1)$, respectively. FTH does not
  factor through the equality partition alone.
- PR retains/reverses old unordered edges. For $f=(2,2,2)$, FTH gives
  $(1,2,2)$ and creates the sibling edge $\{0,1\}$ absent from PR's old
  edge set. This rules out literal equality, not every imaginable factor.
- The increasing-path-cover enumeration is static combinatorics, and the
  period calculation on an already characterized core is an elementary
  rotation action. No credit is claimed for those primitives alone. The
  proposed residual conjunction is the exact recurrent carrier forced by
  **all** backward-image sets plus the actual all-target code and unique
  global fibre maximum for this non-kernel-only update.
- An independent assessor may still find a complete owner or old-template
  adapter. This author does not certify novelty, source clearance, candidate
  admission or an independent review. The unproved sharp entrance clock is
  not needed for the stated contract and is not silently included.
