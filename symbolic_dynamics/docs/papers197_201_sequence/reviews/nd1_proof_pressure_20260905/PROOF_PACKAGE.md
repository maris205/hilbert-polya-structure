# ND1 bounded proof pressure

## Claim

On all simple undirected labelled graphs on $[n]$, including $n=0$, define
$D(G)$ by $uv\in E(D(G))$ iff $|N_G(u)\triangle N_G(v)|=1$.
Neighborhoods are open, the old edge set is discarded, and loops are excluded.

Pressure targets: are the only recurrent states the empty graph and
$S(c,z)$ (a star centered at $c$, with the single other isolated vertex $z$)
for $n\ge4$? Does every orbit enter this set by time four? Is the empty
target the unique maximum fibre for all sizes, with a substantive complete
target inverse rather than just the forward distance constraints?

## Status

**NOT CURRENTLY JUSTIFIED** for the full temporal/exhaustion and extremum
claims. **NO_PROMOTION**. The weaker results and the component-potential
parameterization below are proved. No counterexample to the all-size
conjecture is claimed; the independent finite boxes confirm only $n\le6$.

## Assumptions and notation

All vertices remain labelled and the map acts on the full carrier.
An adjacency row $a_u$ is a vector in $\mathbb F_2^n$; its Hamming weight
is written $|a_u|$. The unit vector at coordinate $w$ is $e_w$.
Addition below is over $\mathbb F_2$. A twin class means equal *open*
neighborhoods. No assumption of distinct rows, connectedness or a fixed
bipartition is introduced silently.

## Proof strategy and dependency map

1. Direct local set comparisons prove the fixed point, bipartition,
   persistent twins and explicit two-cycles.
2. Hamming geometry proves a necessary output restriction. This is a
   structural observation, not an orbit clock.
3. Unique witness labels on target edges give XOR row potentials.
   Diagonal and symmetry equations eliminate most row-offset variables.
4. Cross-component nonedge exclusions remain. At the empty target they
   retain the original counting difficulty, so no maximum-fibre theorem
   follows from the parameterization.
5. Full tiny graphs and a separate exhaustive decoder test apply pressure
   to these proofs, not to the missing all-size inference.

## Proof

### Step 1. Elementary dynamics, independently recovered

If $uv\in E(G)$, then $u$ and $v$ both belong to
$N_G(u)\triangle N_G(v)$, so $uv\notin E(D(G))$. The input/output edge
sets are disjoint. Hence the empty graph is fixed and is the unique fixed
point. Since the parity of a symmetric difference is the sum of the two
set-size parities, every output edge joins vertices of opposite old-degree
parity. Thus every output is bipartite.

If $a_u=a_v$, the two distance-one tests against each other row agree,
and the pair $uv$ is absent. Their output neighborhoods agree. Therefore
twin classes can merge but never split. This alone bounds only the number
of strict mergers, not the time between mergers.

For $n\ge4$, put $L=[n]\setminus\{c,z\}$. In $S(c,z)$ the rows are
$L$ at $c$, $\varnothing$ at $z$, and $\{c\}$ at each $\ell\in L$.
Since $|L|\ge2$, exactly the pairs $z\ell$ have difference one.
Consequently $D(S(c,z))=S(z,c)$. These are distinct two-cycles, one for
each unordered pair $\{c,z\}$. This proves a recurrent family, not its
exhaustiveness. The small sizes are handled separately in the exact boxes.

### Step 2. Output cube restriction

Merge vertices having the same input row and retain their multiplicities.
The distinct row vectors are distinct vertices of the binary $n$-cube.
Two corresponding classes in the output are completely joined exactly
when their vectors have Hamming distance one. Within each class there are
no output edges. Hence $D(G)$ is a false-twin blow-up of the induced
subgraph of the cube on the distinct input rows. The word 'induced' is
necessary: no cube edge between two occurring vectors is omitted.

If two distinct input rows have a common distance-one neighbor vector,
their difference is $e_r+e_s$ with $r\ne s$. Such a vector must be either
$a_u+e_r$ or $a_u+e_s$. Thus any two distinct input-row classes have at
most two common neighbor *row types* in $D(G)$. There may be many vertices
of either type, so replacing this with a bound of two common vertices is
invalid. Persistent equal rows are essential to the star examples.

This cube restriction is stronger than bipartiteness but does not give
the proposed four-step bound or force a merger at a specified time. No
strict potential, bounded waiting lemma, or complete classification of
cycles in the realizable cube-blow-up class was closed in this task.

### Step 3. A complete target-component parameterization

Fix a target graph $H$ with connected components $C_1,\ldots,C_c$ and
choose root $r_i=\min C_i$ in each. For every target edge $uv$, choose
a label $\lambda(uv)\in[n]\setminus\{u,v\}$. It represents the sole
coordinate at which source rows differ. Impose the cycle condition that
the XOR of $e_{\lambda(e)}$ around every target cycle is zero. This is
equivalent to path-independent potentials $p_u\in\mathbb F_2^n$ with
$p_{r_i}=0$ and $p_u+p_v=e_{\lambda(uv)}$ on each edge of $H$.

For vertices in the same component impose both

$$p_v(v)+p_u(v)=p_u(u)+p_v(u)$$

and $|p_u+p_v|=1$ iff $uv\in E(H)$. The former is the internal source
symmetry condition, the latter excludes unwanted internal target edges.
For $u\in C_i$, $v\in C_j$, $i\ne j$, impose

$$p_v(r_i)+p_u(v)=p_u(r_j)+p_v(u).$$

For each unordered component pair choose one bit $b_{ij}=b_{ji}$.
Define a symmetric zero-diagonal adjacency matrix by, for distinct $u,v$,

$$A_{uv}=\begin{cases}
p_v(v)+p_u(v),&u,v\in C_i,\\
b_{ij}+p_v(r_i)+p_u(v),&u\in C_i,\ v\in C_j,\ i\ne j.
\end{cases}$$

The imposed equalities make these formulas symmetric. Finally retain
exactly those bit choices for which $|A_u+A_v|\ne1$ for every pair in
different target components. The resulting matrices are precisely all
sources of $H$, without multiplicity.

To prove necessity, any source gives the unique labels
$A_u+A_v=e_{\lambda(uv)}$ on edges. Its row differences yield the cycle
condition and $A_u=A_{r_i}+p_u$. The diagonal condition determines
$A_{r_i}(v)=p_v(v)$ within a component. Across two components,
$A_{r_i}(r_j)=b_{ij}$ and symmetry at a root gives
$A_{r_i}(v)=b_{ij}+p_v(r_i)$. Substitution yields the displayed formulas
and their symmetry constraints. All nonedge exclusions are necessary.

For sufficiency, the displayed formula gives $A_u+A_v=p_u+p_v$ for two
vertices in one component, coordinate by coordinate, including coordinates
in other components. It therefore produces exactly the internal target
edges. The final cross-component exclusions prohibit every other target
edge. Thus $D(A)=H$. The labels are recoverable from $A$ and $H$, and
$b_{ij}=A_{r_i r_j}$; no source occurs twice. For $n=0$, the empty product
gives the single empty matrix and the statement still holds.

For fixed admissible labels, at most $2^{\binom c2}$ sources occur. In
particular a connected target has at most one source per label assignment.
This is a correct target-resolved reduction, but it is not offered as a
closed fibre census or a fresh generic inverse method.

### Step 4. Why this does not close the second required axis

At $H=\overline K_n$, all components are singletons, there are no witness
labels, all potentials vanish and every pair bit $b_{ij}$ survives the
linear constraints. The final test is exactly that no two source rows
have Hamming distance one. Thus the parameterization still enumerates
the full $2^{\binom n2}$ graph carrier at the crucial empty target. It
does not evaluate its fibre or prove an injection from every other fibre.

The original scout's proposed injection $G\mapsto G\cup D(G)$ is already
false on five vertices (recorded codes $21\to802$, union image $72$).
Neither changing to XOR potentials nor the trivial component bound fixes
that gap. A genuine all-size extremum or useful exact enumeration still
needs a new argument. No claim of independent two-axis closure is made.

## Exact control and remaining missing lemmas

The independent verifier uses neighborhood sets and Kahn pruning, not
imports from the scout or its orbit-path census. All graphs at $n=0,\ldots,6$
reproduce its finite counts. The entire potential decoder is independently
enumerated for every target at $n=0,\ldots,4$, including zero fibres.
The two-common-row-type lemma is checked on every source up to $n=6$.
Two fresh runs each pass $1,524,572$ assertions with identical stdout.

Missing temporal step: prove exhaustive recurrence in the realizable
cube-blow-up class, with a uniform time bound or a genuine point clock.
The apparent bound $D^6(G)=D^4(G)$ is a conjecture here, not a theorem.
Missing inverse/extremal step: eliminate or evaluate the cross-component
nonedge constraints in a way that solves the empty fibre and compares all
targets. Generic finite enumeration is insufficient under the anchor.

## Open risks and disposition

No all-size temporal counterexample was found or claimed. No larger graph
box was run. Exact old iteration ownership was not established by the
bounded primary/history check, but the static singleton-witness motif is
owned and search non-hits have no novelty weight. P51--P56 history remains
missing. Preserve ND1 as an unpromoted reserve; do not allocate a paper
number, count a candidate gate as accepted, or claim a manuscript review.
