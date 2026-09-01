# Root scout: Boolean Gram / row-intersection dynamics

## Literal carrier and map

On (n\times n) Boolean matrices define

\[
  \Gamma_n(A)=A A^{\mathsf T}
\]

over the Boolean semiring.  Equivalently, ((\Gamma_n(A))_{ij}=1) exactly when rows (i) and (j) have intersecting supports.

## Exact signal

The first image is a symmetric graph relation with a loop exactly on each nonempty row.  Thereafter

\[
 \Gamma_n^{t}(A)=G^{2^{t-1}},\qquad G=\Gamma_n(A),\quad t\ge1,
\]

where powers are Boolean relation powers.  Loops make successive graph squares monotone.  Hence all recurrent states are fixed and the fixed states are precisely partial equivalence relations: disjoint unions of looped cliques plus unlooped isolated vertices.

If (D(G)) is the largest component diameter, then every nonfixed source has exact depth

\[
  1+\lceil\log_2 D(G)\rceil,
\]

with the convention that the logarithmic term is zero for (D\le1).  Therefore the maximum depth is zero for (n=1), and

\[
  1+\lceil\log_2(n-1)\rceil
\]

for (n\ge2).  Incidence rows of the labelled path (P_n) give equality.

The fixed-state census is

\[
  \sum_{k=0}^{n}\binom{n}{k}B_k.
\]

## Every-target fibre formula

Let (H) be a loop-compatible graph relation.  Let \(\mathcal C(H)\) contain the empty set and every vertex subset inducing a fully looped clique.  Let \(E^*(H)\) consist of all active singleton loops and all unordered edges.  For (S\subseteq E^*(H)), put

\[
 c_H(S)=\#\{C\in\mathcal C(H):e\nsubseteq C\text{ for every }e\in S\}.
\]

Then ordered matrix columns are clique supports, and inclusion--exclusion gives

\[
 |\Gamma_n^{-1}(H)|=
 \sum_{S\subseteq E^*(H)}(-1)^{|S|}c_H(S)^n.
\]

Invalid targets have empty fibre.  Positivity is equivalent to an edge-and-loop clique cover of size at most (n), so the formula is also a complete image criterion.

## Exact replay

`verify_boolean_gram.py` exhausts all (2^{n^2}) states for (1\le n\le4), checks the graph-power clock and endpoint characterization source by source, verifies the fixed census and sharp path witness, and matches the fibre formula against every loop-compatible target.  The canonical run records 396,493 passing assertions.

## Collision assessment

The graph-squaring tail is classical and must be credited as zero novelty.  The candidate residual is the literal Boolean-Gram self-map, the exact source-dependent clock from the first row-intersection graph, the sharp matrix witness, the complete fixed census, and the every-target ordered clique-cover fibre atlas.  It is close in carrier but not in mechanism to P127; portfolio selection should normally retain at most one Boolean-matrix candidate in this batch.

Status: **strong reserve pending ownership and diversity gates; HOLD_EXTERNAL**.
