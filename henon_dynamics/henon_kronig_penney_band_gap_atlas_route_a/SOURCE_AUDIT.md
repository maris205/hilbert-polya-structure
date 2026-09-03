# Source audit

## Search protocol

Sources were checked on 2026-09-03 by title, DOI, and model keywords.  The
audit preferred the original journal owner, an authoritative mathematical
monograph from its publisher, and a primary research source proving the
periodic-singular-operator spectral type.  Search snippets or pedagogical
pages were not used as theorem authority.

## Historical model owner

R. de L. Kronig and W. G. Penney, *Quantum Mechanics of Electrons in Crystal
Lattices*, Proceedings of the Royal Society A **130** (1931), 499--513,
DOI [`10.1098/rspa.1931.0019`](https://doi.org/10.1098/rspa.1931.0019).

This is the original periodic crystal band-model owner.  The present package
does not claim to introduce the Kronig--Penney dispersion or band-gap idea.

## Operator and spectral authorities

S. Albeverio, F. Gesztesy, R. Høegh-Krohn, and H. Holden, *Solvable Models in
Quantum Mechanics*, second edition, AMS Chelsea, 2005,
DOI [`10.1090/chel/350`](https://doi.org/10.1090/chel/350).  The AMS contents
identify chapters on one-dimensional delta interactions and infinitely many
centres; this is the operator-domain and point-interaction authority.

R. O. Hryniv and Ya. V. Mykytyuk, *Schrödinger Operators with Periodic
Singular Potentials*, [`arXiv:math/0109129`](https://arxiv.org/abs/math/0109129).
The authors prove self-adjoint, lower-semibounded realizations and pure
absolute continuity with band-gap structure for a class containing periodic
one-dimensional singular potentials.  This supports the spectral-type
boundary; HCS-C327 still gives its direct delta-comb derivation.

## Scope of the reconstruction

The package assembles, under one normalization and for all `a>0`, `g in R`,
the form owner, matching domain, exact discriminant, the full sign-dependent
negative/zero/positive atlas, simple/double edge ledger, every open Bragg gap,
the controlled width expansion, and band-indexed IDS/DOS.  These are
source-local derivations.  No literature-priority claim is made for any one
formula or for their combination.

## Workspace collision boundary

- C288 owns a single isolated point interaction and its scattering/resolvent
  data, not an infinite periodic delta comb or Floquet bands.
- C308 owns a non-Hermitian Hatano--Nelson lattice, not a self-adjoint
  continuum singular periodic operator.
- C318 owns a dimerized SSH chain and bulk--edge topology, not an equal-spacing
  continuum delta-comb atlas.
- C323 owns finite complete-graph oracle search, not an infinite-volume Bloch
  Hamiltonian.

## Evidence and forbidden-promotion boundaries

High-precision edges, transfer matrices, IDS/DOS samples, symbolic identities,
replay, and mutations are regression evidence.  They do not replace the
all-parameter proof in `THEOREM_PACKAGE.md`.

The determinant-one transfer matrix is not an Euler factor, and its Bloch
energies are not target zeros.  No target arithmetic local data, root number,
automorphy, target divisor/counting law, functional equation, Hilbert--Polya
operator, or Route-B input is introduced.
