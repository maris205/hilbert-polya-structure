# Intake and predeclared pilot

## Broad desk before literal selection

The original-only search first covered graph neighbourhood comparisons,
tournaments, trees, set families, clutters, simplicial complexes and poset
rowmotion. These are comparison groups, not extra literal attempts.
Clutter duality and rowmotion offer an old involution/permutation clock;
facet deletion and vertex pruning offer old extraction clocks; tournament
triangle reversal is a classical move/schedule surface. No such map was
instantiated or piloted in this lane. The original graph/relation report
and source adapter were then read in full.

## Literal 1: ONI, open-neighbourhood incomparability

For every integer $n\ge0$, the state space is all labelled simple graphs
$G$ on $[n]=\{0,\ldots,n-1\}$. Let $N_G(u)$ be the open neighbourhood.
Define $F(G)$ by
$$
uv\in E(F(G))\quad\Longleftrightarrow\quad
N_G(u)\not\subseteq N_G(v)\ \text{and}\
N_G(v)\not\subseteq N_G(u),\qquad u\ne v.
$$
Every comparison uses the original graph; all edges are regenerated at
once. No labels, timer, memory, queue or external schedule are added.
The $n=0$ empty graph is included.

Before pilot, immediate deductions are: existing edges persist, so all
recurrent states are fixed, and a generic edge-count clock is available.
Neither fact alone is a nontransferable temporal residual. If $T(A)$ is
the P143 row-inclusion matrix, then off-diagonal
$F(A)_{uv}=(1-T(A)_{uv})(1-T(A)_{vu})$. Static row comparison is deducted.
The old SND uses xor instead, so no literal identity with SND is asserted.

Potential obligations are a pointwise or sharp structural clock beyond
edge counting, plus a complete all-target inverse/extremum. No such result
is assumed before the pilot. Arbitrary Boolean encoding of preimages is
not a qualifying separate inverse mechanism.

## Pilot declaration, fixed before code execution

Exactly one original-state pilot, all simple labelled graphs for
$n=0,1,2,3,4,5$: $1+1+2+8+64+1024=1100$ states. Edge masks use
lexicographic pairs $0\le u<v<n$, least-significant bit first. Enumerate
the entire map, every source's tail/period and every target's indegree.
Print every source row and aggregate maxima, full extremizer lists and
named maximum-tail witnesses. Do not increase $n$ after seeing output.
Two executions of this same fixed pilot may check byte reproducibility;
they are not two different pilots. Expected CPU duration below one second
per execution; no GPU. Code is original to this lane and imports no old
scientific producer. Runtime is ordinary local Python, not a strict
terminal source-only replay or independent verifier.

As a bounded closed-form pressure check, test that fixed graphs are exactly
graphs with no induced $P_4$ or $2K_2$. This is a candidate static claim,
not an empirical all-size theorem. Failure must remain in raw stdout/stderr.
