# Theorem package

## Frozen model

Let \(G=(V,E)\) be a finite connected loopless undirected multigraph.  Every
parallel edge is a distinct labelled element of \(E\), and \(c_e>0\).  Freeze an
arbitrary orientation of each edge and put

\[
b_e=\delta_{\operatorname{tail}(e)}-\delta_{\operatorname{head}(e)},\qquad
B=(b_e)_{e\in E},\qquad C=\operatorname{diag}(c_e),\qquad L=BCB^{\mathsf T}.
\]

Fix \(r\in V\), write \(c(v)=\sum_{e\ni v}c_e\), and at each \(v\ne r\)
sample an infinite independent stack \(X_{v,1},X_{v,2},\ldots\), where
\(\Pr(X_{v,j}=e)=c_e/c(v)\) for \(e\ni v\).  A visible card points from its
stack vertex across its labelled edge.  A legal update selects any visible
directed cycle and advances exactly the pointers on its vertices by one.

## Main theorem

With the preceding conventions:

1. **Deterministic abelian lemma.**  For a fixed stack realization, if one
   finite legal sequence reaches an acyclic visible configuration, then every
   legal cycle-popping sequence does so.  All have the same vertexwise pop
   counts and the same terminal oriented tree.
2. **Almost-sure termination and LERW equivalence.**  With probability one a
   terminating sequence exists, hence every legal rule terminates.  For any
   fixed ordering of \(V\setminus\{r\}\), following visible cards from the
   first vertex outside the built tree and popping each loop when it closes is
   Wilson's chronological loop-erased random walk algorithm, card for card.
3. **Weighted law and matrix-tree normalization.**  The unoriented output is
   independent in law of the legal rule, vertex ordering, and root, and
   \[
   \Pr(\mathcal T=T)=\frac{\prod_{e\in T}c_e}{Z_c},\qquad
   Z_c=\sum_{T}\prod_{e\in T}c_e=\det L^{(r)}.
   \]
   Here \(L^{(r)}\) deletes the row and column of \(r\); the empty determinant
   is one.
4. **All transfer-current minors.**  Let \(L^+\) be the Moore--Penrose
   pseudoinverse and define
   \[
   H_{ef}=c_f b_e^{\mathsf T}L^+b_f.
   \]
   For pairwise distinct labelled edges \(e_1,\ldots,e_k\),
   \[
   \Pr(e_1,\ldots,e_k\in\mathcal T)
     =\det\bigl(H_{e_i e_j}\bigr)_{i,j=1}^k.
   \]
   The same determinant is obtained from the symmetric kernel
   \(K_{ef}=\sqrt{c_ec_f}\,b_e^{\mathsf T}L^+b_f\).

## Proof

### 1. Local diamonds imply the global abelian statement

Two distinct visible directed cycles are vertex-disjoint: in a functional
digraph, two directed cycles sharing a vertex coincide.  Popping disjoint
cycles changes disjoint stacks, each cycle stays visible after the other pop,
and the two updates commute.

Fix a terminating legal list \(\alpha=(C_1,\ldots,C_m)\) and let \(D\) be any
cycle visible initially.  If \(D\ne C_1\), the two are disjoint, so commute
\(D\) past \(C_1\).  Repeat.  The cycle \(D\) must eventually coincide with a
member of \(\alpha\); otherwise it would remain visible after \(\alpha\),
contradicting termination.  Thus \(D\) can be moved to the front of a
terminating list without changing the resulting pointer vector.  Induction on
\(m\) applies this strip argument after every arbitrary first choice.  No legal
sequence can have more than \(m\) pops, every maximal sequence terminates, and
the commuting construction gives the same pointer increments and terminal
configuration.

An acyclic visible functional digraph in which only \(r\) has no outgoing
arrow is an arborescence oriented toward \(r\): every forward orbit must end at
\(r\), since a repeated nonroot vertex would be a cycle.  This identifies the
unique terminal object as an oriented spanning tree.

### 2. Wilson provides a terminating legal list almost surely

Start with the tree \(\{r\}\).  From the first vertex outside the current tree,
follow visible arrows.  On revisiting a vertex of the current path, the arrows
between the two visits form a visible directed cycle; pop precisely that cycle
and retain the chronological loop erasure.  Stop upon hitting the built tree
and adjoin the remaining path.  Repeat over the fixed vertex order.

Every newly exposed card is independent with transition probability
\(p(e)=c_e/c(v)\).  Hence each exploration is the conductance random walk on a
finite irreducible chain, stopped on a nonempty set, and hits that set in
finite time almost surely.  There are finitely many vertices.  The construction
therefore supplies a finite legal pop list almost surely, and its retained
arrows are exactly Wilson's loop-erased paths.  Part 1 promotes this one
terminating list to every legal cycle rule.

### 3. Last exits give the weighted law without a hidden normalization

Let \(P(x,y)=\sum_{e:x\leftrightarrow y}c_e/c(x)\).  For a target set \(A\),
consider a labelled self-avoiding path
\(\gamma=(x_0,e_0,x_1,\ldots,e_{q-1},x_q)\) with \(x_q\in A\) and the earlier
vertices outside \(A\).  Put
\(D_i=V\setminus(A\cup\{x_0,\ldots,x_{i-1}\})\) and
\(G_{D_i}=(I-P_{D_i})^{-1}\).  Splitting the walk at its last visit to
\(x_i\) before advancing along the retained labelled edge gives

\[
\Pr(\operatorname{LE}=\gamma)
=\prod_{i=0}^{q-1}G_{D_i}(x_i,x_i)\frac{c_{e_i}}{c(x_i)}.
\]

This is a direct last-exit decomposition: the sum of the probabilities of all
loops at \(x_i\) within \(D_i\) is the diagonal Green entry, after which the
specified fresh edge is taken.  Cramer's rule supplies

\[
G_D(x,x)=\frac{\det(I-P_{D\setminus\{x\}})}{\det(I-P_D)}.
\]

The Green factors telescope along each path and then across all Wilson phases,
from \(D=V\setminus\{r\}\) to the empty set.  Thus, for a fixed labelled tree
\(T\) oriented toward \(r\),

\[
\Pr(\mathcal T=T)
=\frac{\prod_{v\ne r}c_{e(v)}/c(v)}{\det(I-P^{(r)})}
=\frac{\prod_{e\in T}c_e}{\det L^{(r)}},
\]

because \(I-P^{(r)}=D_r^{-1}L^{(r)}\), where
\(D_r=\operatorname{diag}(c(v):v\ne r)\).  The output is almost surely one
tree, so summing this identity over all labelled spanning trees proves, rather
than assumes,
\(Z_c=\det L^{(r)}\).  The displayed law follows and is visibly root-free.

### 4. Conductance perturbations give every transfer-current determinant

Delete the root row of \(B\), obtaining \(R\), and put
\(A=RCR^{\mathsf T}=L^{(r)}\).  For zero-sum incidence vectors,
\(b_e^{\mathsf T}L^+b_f=(R_{e})^{\mathsf T}A^{-1}R_f\): solving either
Laplacian equation changes a solution only by an additive constant, which the
incidence vector annihilates.  Hence

\[
H=R^{\mathsf T}A^{-1}RC,
\]

independently of the deleted root.  Replace every conductance by
\(c_e(1+t_e)\).  The matrix determinant lemma and Sylvester's identity give

\[
\frac{Z(c_e(1+t_e))}{Z(c_e)}
=\det(I+\operatorname{diag}(t_e)H).
\]

The coefficient of \(\prod_{e\in S}t_e\) on the left is
\(\Pr(S\subseteq\mathcal T)\); on the right it is the principal minor
\(\det H_S\).  This proves the claim for every distinct edge set \(S\).
Finally, with \(D=\operatorname{diag}(\sqrt{c_e})\), the symmetric kernel is
\(K=DHD^{-1}\), so corresponding principal determinants agree.  Changing an
edge orientation conjugates the kernel by a diagonal sign matrix and cannot
change a principal determinant.

## Boundary closure

- **Singleton:** \(V=\{r\}\), \(E=\varnothing\).  The empty tree has probability
  one, \(Z_c=\det(0\times0)=1\), and the order-zero minor is one.
- **Already a tree:** only that labelled tree is possible.  Since
  \(|E|=|V|-1\), the edge-space projection \(K\) is the identity, so every
  admissible inclusion event has probability one.
- **Parallel edges:** labels and conductances remain separate.  Parallel
  incidence columns coincide up to sign, so a principal minor containing two
  parallel edges is zero, matching the impossibility of placing both in a
  multigraph tree.
- **Root change:** stacks and orientations-to-root change, but the unoriented
  law \(\prod c_e/Z_c\), all cofactors, the \(L^+\) kernel, and its principal
  determinants do not.

## Evidence boundary and Route A

Exact finite evidence covers 772 connected labelled simple graphs through
five vertices, 8,136 graph-tree pairs, 55,895 simple edge-subset events, 24
weighted multigraph cases with 846 weighted tree rows and 7,032 subset events,
and 12,754 finite stack tables.  This audits formulas and conventions only.

The Route-A tuple is
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` with overall
`ROUTE_A_REJECTED`.  The projection structure is a source-only formal hint.
Route B is false, and no target Euler factor or target zeta interpretation is
permitted.
