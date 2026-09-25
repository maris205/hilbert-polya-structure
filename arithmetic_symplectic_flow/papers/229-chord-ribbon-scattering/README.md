# 229 — Chord-ribbon scattering

**Candidate:** `ANG-20260918-CRS01`
**Status:** **STOP — T2 ORBIT LEDGER ESTABLISHED, BUT T1 SOURCE SELECTIVITY FAILS.**
**Classical A0/A1/A2:** `NOT APPLICABLE`. **Formal Route-A:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

For each integer `n >= 2`, this candidate forms a finite graph on
`V_n = {1,...,n}` from the backbone edges `{j,j+1}` and the factor chords
`{d,n/d}` for `d | n`, `d < sqrt(n)`, with duplicate edges removed.  Its
oriented darts are scattered by the cyclic successor of the incoming
neighbor at the arrival vertex.  The disjoint union of these finite
permutations is owned by the transformation groupoid
`X ⋊_sigma Z`, and the roof is the intrinsic edge metric
`tau(u,v) = (1/2)|log(v/u)|`.

The local map is bijective, and every finite component has an exact primitive
cycle/repetition ledger.  At `n=8` the canonical cycles have lengths
`[3,8,7]` (listed by the chord, forward-backbone, and mixed cycles) and roof
times `[log 2, log 8, log 8]`.  At `n=10` the corresponding control is
`[4,8,10]` with times `[log(5/2), log 10, log 10]`.  Thus composite labels
carry intrinsic primitive cycles, and the `n=8` cycle of time `log 2` collides
with the prime `p=2` time without being the same orbit or a repetition.

The arithmetic inputs are endogenous only in the weak sense that divisibility
determines which chords are present.  They do not select a prime-only packet:
primes have backbone cycles, while composites have additional primitive cycles,
and removing chords or shuffling vertex labels gives nearby controls.  The
candidate is therefore stopped at the broadened T1/T2 source-selectivity gate.
Classical A0/A1/A2 are `NOT APPLICABLE` because no finite-dimensional
symplectic lift is supplied. No transfer operator, determinant, formal Route-A
coordinate, or Route-B evaluation is supplied or borrowed.

- [Frozen candidate and appended audit](candidate-card.md)
- [Full definitions, proof, orbit ledger and controls](paper.md)
- [Claim ledger](claim-ledger.md)
- [Reproducibility checks](evidence/README.md)
