# Independent bounded owner supplement — CPE

**Audit date:** 2026-09-03 UTC  
**Decision use:** ingredient subtraction and direct-owner pressure only  
**External state:** `HOLD_EXTERNAL`

## Result

The bounded search did **not** locate an external source that defines and
iterates the literal map

```text
pi -> pi meet sigma(pi)
```

on every set partition of a cyclically labelled finite set, nor one that
states its point clock or its every-target time-fibre polynomial.  This is a
terminology-dependent non-hit, not a novelty, priority, or clearance result.
It does not cure the decisive internal collision with P110.

## Queries and records inspected

The search used exact-map and mechanism phrases, including:

```text
"x meet f(x)" lattice automorphism iteration
"meet" "cyclic shift" set partitions equivalence relations
"intersection of all translates" equivalence relation cyclic group
partition lattice cyclic shift meet orbit equivalence relation
"cyclic" "partition lattice" meet translates
aperiodic set partitions Bell numbers Mobius divisors
primitive set partitions Mobius Bell numbers
set partitions trivial rotational core enumeration
```

Searches covered arXiv records, publisher full text, general web indexing,
the current `partition-lattice` crate documentation/source, and the local
P1--P161 corpus.

## What the nearest external sources actually own

### Invariant partitions under permutation groups

Marina Anagnostopoulou-Merkouri, R. A. Bailey, and Peter J. Cameron,
*Permutation groups, partition lattices and block structures*, Forum of
Mathematics, Sigma 13 (2025), e180,
[DOI 10.1017/fms.2025.10126](https://doi.org/10.1017/fms.2025.10126),
[arXiv:2409.10461](https://arxiv.org/abs/2409.10461), explicitly records that
the invariant partitions of a transitive group form a sublattice and gives
the order-preserving correspondence with subgroups containing a point
stabilizer.  For the regular cyclic action this directly owns the
subgroup/coset classification of fixed partitions.  It does not define the
CPE endomap or its transient and fibre formulas.

The root scout's phrase “P. J. Cameron, C. E. Praeger, and collaborators” is
bibliographically wrong for this record: the three authors are
Anagnostopoulou-Merkouri, Bailey, and Cameron.  The mathematical subtraction
is nevertheless the right one.

John R. Britnell and Mark Wildon, *Orbit coherence in permutation groups*,
Journal of Group Theory 17 (2014), 73--109,
[DOI 10.1515/jgt-2013-0029](https://doi.org/10.1515/jgt-2013-0029), studies
when orbit partitions are closed under meet or join.  It is structural
partition-lattice background, not an owner of the literal adjacent-translate
iteration.

### The August 2026 `partition-lattice` crate

[`partition-lattice` 0.4.0](https://docs.rs/crate/partition-lattice/0.4.0),
released 2026-08-23, directly implements refinement/coarsening, incidence
coordinates, group-orbit partitions, and cyclic-pattern backends.  Its
documented `cyclic_refine(c1,c2)` computes the common refinement of **two
already periodic compact partitions**, with output period the lcm of their
periods when it fits the backend.  The documentation expressly says that the
compact backend is not for arbitrary partitions or for a refinement that
leaves the cyclic-pattern class.

Thus the crate supplies a one-step computational primitive and relevant
terminology.  The inspected public documentation/source does not rotate an
arbitrary `pi`, define `pi -> pi meet sigma(pi)` as an endomap, or state the
window, clock, target-fibre, or terminal-basin theorems.  It is adjacent
software and must be disclosed, but it is not a direct theorem owner found by
this audit.

### Möbius, Bell, and Touchard ingredients

Partition-lattice Möbius inversion, the interval value
`product (-1)^(r-1)(r-1)!`, Bell/Stirling/Touchard enumeration, and ordinary
divisor Möbius inversion are standard and must receive zero contribution
credit.  The exact terminal sequence/formula

```text
P_d(z) = sum_(e|d) mu(d/e) B_e(z)
```

did not produce a direct source in the bounded phrase and sequence searches.
It is, however, an immediate divisor inversion once fixed cores are indexed
by cyclic congruences; absence of a direct hit does not make the method an
independent dynamical mechanism.

## Internal search correction

The root scout's two statements that P110 acts on “integer partitions” and on
a “different carrier” are false.  P110's phase space is exactly the full set
partition lattice `Pi_n` of `Z/nZ`, with the same cyclic relabelling; its map
is `pi -> pi join sigma(pi)`.  This correction is decisive for the portfolio
gate and is developed in `HOSTILE_GATE.md`.

No external circulation or ownership claim is authorized.  Status remains
`HOLD_EXTERNAL`.
