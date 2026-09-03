# Research question

Let \(G=(V,E)\) be a finite connected loopless undirected multigraph whose
parallel edges remain distinctly labelled, let \(c_e>0\), and fix a root \(r\).
At every \(v\ne r\), place an independent infinite stack of incident labelled
edges, each card choosing \(e\ni v\) with probability \(c_e/c(v)\).  Whenever
the visible arrows contain a directed cycle, pop every card on that cycle.

Can one prove in a single convention-locked theorem that:

1. every legal cycle choice is order-independent and terminates almost surely;
2. a canonical legal choice is exactly Wilson chronological loop erasure;
3. the output tree has probability
   \[
   \mathbb P(\mathcal T=T)=\frac{\prod_{e\in T}c_e}
   {\sum_{S\text{ spanning tree}}\prod_{e\in S}c_e};
   \]
4. the denominator is every reduced conductance-Laplacian determinant; and
5. for distinct labelled edges \(e_1,\ldots,e_k\), the joint inclusion
   probability is the principal determinant of one explicitly oriented
   transfer-current kernel?

The answer proved here is yes, including singleton, tree, parallel-edge, and
root-change boundaries.  The question is entirely source-local.  It does not
ask for arithmetic local data, an Euler factor, a root number, automorphy, a
target divisor or functional equation, a target zero match, or a
Hilbert--Pólya operator.
