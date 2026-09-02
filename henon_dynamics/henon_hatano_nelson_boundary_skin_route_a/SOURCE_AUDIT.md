# Source and claim audit

## Primary owners

- Hatano and Nelson, *Localization Transitions in Non-Hermitian Quantum Mechanics*, Physical Review Letters 77 (1996), DOI `10.1103/PhysRevLett.77.570` (also arXiv `cond-mat/9603165`): model provenance for asymmetric non-Hermitian hopping.
- Hatano and Nelson, *Non-Hermitian Delocalization and Eigenfunctions*, Physical Review B 58 (1998), DOI `10.1103/PhysRevB.58.8384` (also arXiv `cond-mat/9805195`): left/right eigenfunction context.
- Yao and Wang, *Edge States and Topological Invariants of Non-Hermitian Systems*, Physical Review Letters 121 (2018), DOI `10.1103/PhysRevLett.121.086803`: used only to locate modern boundary-sensitivity/skin terminology.  C308 does **not** inherit or assert its topological claims.

The exact continuant, diagonal similarity, discrete-sine diagonalization, cyclic Fourier diagonalization, resolvent identity, and Jordan-rank statements are proved directly in this package.  No novelty or priority claim is made for the model or standard linear-algebra ingredients.

## Repository collision audit

- C267 studies a Hermitian infinite Wannier--Stark lattice, not this finite asymmetric-hopping OBC/PBC family.
- C288 studies a self-adjoint delta point interaction, not a nonnormal lattice or its singular boundary limit.
- C297 studies two-mode PT gain/loss ray dynamics, not asymmetric nearest-neighbor hopping.
- C303 studies a dissipative CPTP qubit semigroup, not wave-amplitude evolution by a nonnormal hopping matrix.

These are structural neighbors, not source owners.  Earlier tentative associations with C185, C242, and C293 were rejected after registry inspection because those packages concern, respectively, Brockett sorting flow, ellipsoid Reeb dynamics, and a magnetic Grushin cylinder.

## Scope firewall

The finite Chebyshev determinant is not an Euler factor.  The matrix spectrum is not a target zero set.  Similarity to a real symmetric path matrix is not a construction of a Hilbert--Polya operator.  No disorder, interactions, bulk invariant, winding number, protected edge mode, automorphy, root number, or Route-B datum is asserted.
