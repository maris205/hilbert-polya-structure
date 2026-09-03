# Source verification and owner subtraction — P177

**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`  
**Rule:** a direct source removes claim credit; a query miss contributes no
novelty, priority, or freedom-to-operate evidence.

## Verified primary or authoritative controls

| Key | Verified record | Independent surfaces | Zero-credit assignment |
|---|---|---|---|
| `KwiatkowskiPankovPasini2018` | Mariusz Kwiatkowski, Mark Pankov, Antonio Pasini, “The Graphs of Projective Codes,” *Finite Fields and Their Applications* 54 (2018), 15–29, DOI `10.1016/j.ffa.2018.07.003` | Elsevier/ScienceDirect article and Crossref DOI metadata/BibTeX | projective-code terminology, projective systems, and the identification of full binary projective systems with simplex codes |
| `Tonchev1993` | Vladimir D. Tonchev, “Quasi-Symmetric Designs, Codes, Quadrics, and Hyperplane Sections,” *Geometriae Dedicata* 48(3) (1993), 295–308, DOI `10.1007/BF01264073` | Springer version-of-record page and Crossref DOI metadata/BibTeX | symmetric-difference design language and the established relation among binary codes, simplex codes, and projective hyperplane sections |
| `DiaconisSaloffCoste1996` | P. Diaconis and L. Saloff-Coste, “Walks on Generating Sets of Abelian Groups,” *Probability Theory and Related Fields* 105(3) (1996), 393–421, DOI `10.1007/BF01192214` | Springer version-of-record page and Crossref DOI metadata/BibTeX | broad context for Markov walks whose states are generating sets of Abelian groups; not ownership of P177's fixed-generator character calculation |
| `Brown2000` | Kenneth S. Brown, “Semigroups, Rings, and Markov Chains,” *Journal of Theoretical Probability* 13(3) (2000), 871–938, DOI `10.1023/A:1007822931408` | Springer version-of-record page, Crossref DOI metadata/BibTeX, and author preprint `arXiv:math/0006145` | generic algebraic spectral treatment of finite Markov chains and the nearby but distinct phrase “hyperplane chamber walks” |

The DOI `10.1007/BF01192214` is the canonical DOI for the Diaconis–Saloff-
Coste record.  No alias is used in the bibliography.  The projective-code
paper has three authors; shortening it to “Pankov” would be incorrect.

## Claim-level source check

The Elsevier text explicitly describes a binary simplex code as the code
whose projective system contains all points of the relevant projective
space.  Tonchev's abstract explicitly links binary codes spanned by the
simplex code with hyperplane-section incidence and symmetric-difference
designs.  These sources justify treating the code/design dictionary as
background; neither source is being cited as an owner of the stochastic
toggle theorem.

The Springer record for Diaconis and Saloff-Coste concerns random walks whose
states are generating sets of Abelian groups and uses comparison and
logarithmic-Sobolev methods.  It is broad context, not a direct source for
P177's fixed-generator Fourier diagonalization.  The latter elementary
Cayley/character method is nevertheless assigned zero credit and is proved
in the manuscript.  Brown studies
left-regular-band and hyperplane-*chamber* walks, calculates spectra and
multiplicities, and supplies an important terminology collision.  P177 does
not identify its XOR subset walk with Brown's chamber walk.

The crown graph `K_(q,q)` minus a perfect matching, its regularity, and its
four elementary adjacency eigenvalues are also zero-credit background.  The
manuscript proves the needed neighborhood and spectrum statements directly,
so no unverifiable or unnecessary crown-graph citation is added.

## Internal collision firewall

| Existing paper/system | Shared shell assigned zero credit | Literal separation |
|---|---|---|
| P145, random vertex-push orientation chain | finite binary quotient, Cayley support, Fourier characters, periodicity and spectral multiplicities | P145 acts on orientation push-orbits and reduces to folded hypercubes; P177 acts on all subsets of projective points with hyperplane-incidence masks and splits into crown components |
| P172, fresh-map self-image erosion | finite subset carrier and exact transition powers | P172 is a nested absorbing intersection chain driven by random endomaps; P177 is a reversible XOR toggle with no transient state |
| P173, quotient-leakage erosion | quotient coordinates and class counting | P173's leakage/erosion update is monotone and its owner boundary is occupancy/quotient based; P177's generator code and bipartite Cayley classes are different |
| P175, commutator system | binary/matrix algebra vocabulary | P177 contains no commutator update or commutator proof engine |

## Retained claim ceiling and kill switch

No credit is claimed for simplex codes, projective hyperplanes, incidence
designs, symmetric difference as an operation, crown graphs, Cayley graphs,
Fourier inversion, character spectra, uniform stationarity, or generic
finite-chain recurrence.  The remaining conjunction is:

```text
literal nonzero projective-hyperplane toggling
+ disjoint-crown communicating-class conjugacy
+ every-time/every-target ordered-history kernel
+ parity-phase TV formula
+ full-carrier multiplicity lift.
```

A primary source stating that conjunction, or a routine proof transfer from
an occupied literal system, is an immediate kill switch.  The present owner
search is bounded and leaves the paper `OWNER_AMBER / HOLD_EXTERNAL`.
