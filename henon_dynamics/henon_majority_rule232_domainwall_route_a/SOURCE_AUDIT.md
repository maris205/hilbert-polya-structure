# Source and scope audit

## Frozen provenance

The package records the elementary radius-one majority rule in the standard
cellular-automaton taxonomy.  Wolfram's review (DOI
[`10.1103/RevModPhys.55.601`](https://doi.org/10.1103/RevModPhys.55.601)) is
used only for classification context.  Toom's monotone cellular-dynamics
work (DOI
[`10.1007/978-1-4613-3044-2_19`](https://doi.org/10.1007/978-1-4613-3044-2_19))
is context for erosion-style arguments.  The wall identity, periodic
classification, transfer matrices, and all finite receipts are reconstructed
independently in this package.

## Distinct owner

This is a nonlinear, non-invertible, synchronous threshold automaton.  It is
not the additive Rule-90 family, the conservative Rule-184 traffic rule, a
reversible Margolus partition, a substitution shift, or a finite permutation.
The proof uses domain-wall erosion and a fixed forbidden-word language rather
than a recoding of those owners.

## Evidence boundary

The producer uses integer arithmetic and exhaustive states through (n=14),
with independent transfer traces through (n=64).  The checker does not
import producer functions.  SymPy verifies the characteristic polynomial and
all transfer rows; replay checks exact bytes; hostile mutations test repaired
hashes, semantic fields, unknown keys, and route/scope flags.

No target primes or zeros, arithmetic local data, Euler factors, root numbers,
automorphy, target divisor/counting law, functional equation, or
Hilbert--Pólya operator is used.  Route B is disabled.
