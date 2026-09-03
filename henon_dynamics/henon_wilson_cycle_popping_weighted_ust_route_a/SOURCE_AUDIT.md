# Source audit

Checked on 2026-09-03.  The package reconstructs every proof it uses and makes
no novelty or literature-priority claim.

## Direct sources and ownership

1. David Bruce Wilson, *Generating random spanning trees more quickly than the
   cover time*, STOC 1996, pp. 296--303,
   DOI [10.1145/237814.237880](https://doi.org/10.1145/237814.237880).
   An author-era readable copy is available from
   [CMU course hosting](https://www.cs.cmu.edu/~15859n/RelatedWork/RandomTrees-Wilson.pdf).
   Ownership: the loop-erased random-walk sampler and cycle-popping proof line.

2. Robert Burton and Robin Pemantle, *Local Characteristics, Entropy and Limit
   Theorems for Spanning Trees and Domino Tilings Via Transfer-Impedances*,
   **Annals of Probability** 21 (1993), 1329--1371,
   DOI [10.1214/aop/1176989121](https://doi.org/10.1214/aop/1176989121).
   The author's exact article copy is
   [burton.pdf](https://www2.math.upenn.edu/~pemantle/papers/burton.pdf).
   Ownership: the transfer-impedance/current determinantal law.  The DOI is
   `...9121`; `...9016` belongs to a different article and is not used.

3. Gustav Kirchhoff, *Ueber die Auflösung der Gleichungen, auf welche man bei
   der Untersuchung der linearen Vertheilung galvanischer Ströme geführt
   wird*, **Annalen der Physik** 148 (1847), 497--508,
   DOI [10.1002/andp.18471481202](https://doi.org/10.1002/andp.18471481202).
   Ownership: the electrical-network determinant lineage behind the
   matrix-tree theorem.

4. Seth Chaiken, *A Combinatorial Proof of the All Minors Matrix Tree
   Theorem*, **SIAM Journal on Algebraic Discrete Methods** 3(3) (1982),
   319--329, DOI [10.1137/0603033](https://doi.org/10.1137/0603033).
   Ownership: a modern primary all-minors matrix-tree treatment.  The present
   paper needs only the one-cofactor weighted case and proves it probabilistically.

5. Russell Lyons and Yuval Peres, *Probability on Trees and Networks*,
   Cambridge University Press (2016), ISBN 978-1-107-16015-6.  The authors'
   [official free book page](https://rdlyons.pages.iu.edu/prbtree/) identifies
   the published edition and hosts corrected versions.  Ownership: an
   authoritative synthesis of Wilson's method, electrical networks, effective
   resistance, and the transfer-current theorem.

## Claim boundaries

- Wilson owns the sampler/cycle-popping lineage; Burton--Pemantle own the
  transfer-impedance theorem lineage; Kirchhoff and Chaiken own the determinant
  lineage.  This package's value is a self-contained convention-locked
  reconstruction plus an exact executable audit, not a priority claim.
- The sources cover much broader settings than this package.  We assert only a
  finite connected loopless undirected multigraph with positive conductances
  and distinctly labelled parallel edges.
- The weighted spanning-tree partition polynomial is not a target Euler factor,
  the transfer-current determinant is not a target dynamical zeta, and no
  target arithmetic or Hilbert--Pólya conclusion is imported from any source.
