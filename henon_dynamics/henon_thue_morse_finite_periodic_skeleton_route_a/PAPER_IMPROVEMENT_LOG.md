# C149 paper improvement log

No external reviewer transport or numeric score was used.  Both passes were
internal proof, scope, and presentation audits, each followed by compilation.

## Round 0 to round 1

Findings:

- The first draft gave the zeta product before distinguishing exact-period
  points from primitive cycles.
- Compactness of the finite topological disjoint union was asserted without
  naming the componentwise topology.
- The phrase “finite extension” could be misread as an intrinsic symbolic
  extension.

Repairs:

- Inserted Möbius inversion and the division-by-period boundary.
- Added the finite-disjoint-union compactness argument.
- Replaced “extension” by “tagged topological disjoint attachment.”

## Round 1 to round 2

Findings:

- The aperiodicity dependency on the infinite component was too compressed;
  a seed mismatch alone would not exclude periodic points in the whole
  language subshift.
- The minimality obstruction was stated for the frozen four cycles but not for
  an arbitrary nonempty finite skeleton.
- The Route-A paragraph needed to reject “almost minimal” explicitly.

Repairs:

- Added `b=bit_length(d)`, proved that every length-`2^(b+1)` interval
  contains a full `b`-aligned block, and transferred its offset-`0,d`
  mismatch to every language window.
- Generalized the closed-invariant-subset proof to any nonempty finite union.
- Added the explicit nonclaim and separated intrinsic orbit creation from
  declared decoration.

Final internal audit: no unresolved issue remains inside the frozen scope.
