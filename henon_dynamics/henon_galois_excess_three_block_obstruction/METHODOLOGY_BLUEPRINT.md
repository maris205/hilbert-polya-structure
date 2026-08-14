# Methodology blueprint

## Object lock

1. Freeze the HCS-P31 four-state adjacency matrix.
2. Freeze the P54 definition `Mahler height = physical length + Galois
   excess`.
3. Enumerate primitive symbolic cycles through period five without numerical
   ranking.

## Symbolic method

For each cyclic word and each width `r`, form its exact cyclic block-incidence
vector.  Compute the first integer row relations.  Any width-`r` potential is
a linear functional on these vectors, so a proposed periodic-sum assignment
must annihilate every relation.

## Algebraic method

- derive the second period-four orbit in radicals;
- exploit the reflection pattern `(a,b,c,c,b)` for the target period-five
  orbit;
- eliminate `a` to obtain the exact trace polynomial;
- substitute `T=z+z^{-1}` to obtain the reciprocal multiplier polynomial;
- use Sturm root counts on rational intervals, not decimal root labels;
- derive the strict excess inequality from exact interval order.

## Validity controls

- independent DFS enumeration rather than producer product enumeration;
- independent resultant and Sturm reconstruction;
- eight SHA-256 dependency locks;
- 17 hostile claim/interface mutations;
- 14 unit tests;
- explicit finite-interpolation countercontrol against overclaiming a
  general Hölder obstruction.

## Evidence labels

- Symbolic relations and exact polynomials: **PROVED**.
- Decimal expansions: reports of exact objects.
- Width-at-most-three obstruction: **PROVED**.
- General Hölder realization or obstruction: **OPEN**.
- Full Galois-weighted zeta completion: **OPEN**.
