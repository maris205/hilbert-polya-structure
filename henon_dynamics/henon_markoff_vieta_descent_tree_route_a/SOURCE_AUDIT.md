# C193 source audit

## Verified primary and modern sources

1. A. Markoff, “Sur les formes quadratiques binaires indéfinies,”
   *Mathematische Annalen* 15 (1879), 381--406, DOI
   `10.1007/BF02086269`.

   This is the classical source for the Diophantine reduction setting.  The
   package does not claim priority for the equation or descent genealogy.

2. E. Bombieri, “Continued fractions and the Markoff tree,” *Expositiones
   Mathematicae* 25(3) (2007), 187--213, DOI
   `10.1016/j.exmath.2006.10.002`.

   This is the modern source lock for the Markoff tree and its classical
   continued-fraction setting.  Continued fractions are background here, not
   a transfer-operator owner.

3. J. Bourgain, A. Gamburd and P. Sarnak, “Markoff triples and strong
   approximation,” *Comptes Rendus Mathématique* 354(2) (2016), 131--135,
   DOI `10.1016/j.crma.2015.12.006`.

   The paper explicitly records that all positive Markoff triples form the
   Vieta-involution orbit of `(1,1,1)`.  Its modular strong-approximation
   program is cited only to establish the boundary: this package imports none
   of its mod-prime data.

## Package-owned derivations

The package chooses a deterministic orientation of the classical Vieta graph:
sort, replace the unique largest coordinate, and sort again.  It supplies the
elementary uniqueness/strict-descent proof, the resulting termination and
unique-parent certificate, and an executable comparison between a bounded
quadratic-root scan and a separately generated tree.

## Claim firewall

- The global solution theorem comes from source-locked descent/orbit theory;
  the finite census is only a regression oracle.
- “Rooted tree” concerns normalized triples and their unique parent, not the
  open uniqueness of a triple from its largest coordinate.
- No mod-`p` graph, prime table, local factor, Euler product, root number,
  automorphy object, target divisor or Route-B input is used.
- Diophantine origin supports only `A0_WEAK_ARITHMETIC_RELATION`; it is not
  silently promoted to rational-prime semantics.
