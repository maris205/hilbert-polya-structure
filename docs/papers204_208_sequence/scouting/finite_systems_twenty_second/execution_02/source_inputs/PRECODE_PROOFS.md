# Pre-code deductions and zero-credit mechanisms

## Status and assumptions

The finite maps and all conventions are exactly those in `INTAKE.md`.
The elementary results below are PROVABLE AS STATED. Neither map currently
has a proved nontrivial temporal-plus-independent-inverse paper contract.
No sharp all-size clock is claimed. The route is direct proof, followed by
finite pressure on the same hypotheses; experiments do not prove them.

## ORR dependencies and proof

1. Reversing a contiguous increasing run of length $r$ introduces exactly
   $\binom r2$ inversions inside the run. Pairs with both entries outside it
   are unchanged. For a fixed outside position, the number of inversions
   with the run depends only on its multiset of values, which is unchanged.
   Therefore the total inversion increase is the sum of $\binom r2$ over
   reversed odd runs of length at least three. A changed epoch increases
   it by at least three. Thus all recurrent states are fixed and every
   orbit reaches the fixed locus in at most $\lfloor\binom n2/3\rfloor$
   steps. This is explicitly a generic, not asserted sharp, potential bound.
2. The map fixes a permutation exactly when every maximal increasing run
   has length one or even length. If an odd run has length at least three,
   its first/last entries change and disjoint run operations cannot cancel
   that change. Conversely each permitted run is held. An odd interval
   reversal sends position $i$ to $a+b-i$ with $a+b$ even, proving parity
   of every labelled entry's position is preserved.
3. For a target $y$, partition its positions into nonempty consecutive
   blocks. A block of odd length must be strictly decreasing; a block of
   even length must be strictly increasing. Reverse odd blocks and leave
   even blocks. The reconstructed blocks are increasing. Demand at each
   block boundary that the preceding block's maximum exceeds the next
   block's minimum. This makes precisely these blocks the maximal
   increasing runs of the reconstructed source, so its ORR image is $y$.
   Conversely every source gives exactly this partition by its unique
   maximal increasing runs. Distinct valid partitions yield distinct
   sources because their maximal-run partitions would otherwise coincide.
   The decoder is therefore complete and nonredundant. It is ordinary
   interval-partition inversion, provisionally deducted as background.

## HXC dependencies and proof

1. Symmetric difference of two distinct sets is nonempty; an isolated edge
   stays nonempty. Consequently the literal is total on the stated family
   carrier without an exception or deletion of an invalid output.
2. If some intersection exists, take the least-coded nonisolated edge $e$.
   Its least intersecting partner $f$ is also nonisolated. Every neighbour
   of $f$ is nonisolated, so none is smaller than $e$. Hence $m_H(f)=e$.
   Both $e$ and $f$ output $e\triangle f$; with one output per input edge
   the next family has cardinality at most $|H|-1$.
3. A disjoint-edge family is held, whereas any other family loses size and
   cannot be fixed or periodic. Therefore the complete recurrent locus is
   exactly the pairwise-disjoint families. A nonempty family never maps to
   empty, so its entrance time is at most $|H|-1$. This is generic finite
   cardinality descent and is not claimed sharp or sufficient for admission.
4. Fixed families correspond to partitions of some subset of $[n]$; add one
   extra element to the unused vertices to obtain a bijection with set
   partitions of $[n+1]$. The fixed count is $B_{n+1}$, the Bell number.
   This elementary partial-partition count is static background, not a
   second research contribution.

## Missing claims

ORR has no proved sharp clock, all-time normal form or nontrivial basin
classification here. HXC has no evaluated structural full-target inverse,
sharp extremum or stronger temporal mechanism. The finite program reports
all target fibres, but full-map enumeration is not a new inverse theorem.
Source comparisons and ordinary primitive subtraction remain necessary.
