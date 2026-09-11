# P200 retained narrative

The state is a full labelled binary matrix. Each step flips its least
alternating rectangle, ordered by row pair before column pair. This is
a deterministic schedule of Ryser's existing interchange, not a new move.
The schedule has two related but distinct pieces of geometry.

For time evolution, all rows before the first pivot are comparable with
every row. An earlier row comparable with two incomparable supports must
lie below their intersection or above their union. Switching preserves
both, making the first pivot invariant. The partner can only decrease.
Within one partner, the first two differing columns become the persistent
column choice after at most one preliminary switch. Thus each partner is
seen at most twice through first recurrence, yielding tau<=2r−3. A full
descending-partner itinerary attains it for every width s>=r+1.

For inversion, reversing a target rectangle must exchange the first
difference with an opposite-type column before the next same-type
difference. Its reconstructed pivot must be comparable with every
earlier partner. These are target conditions, not a call to the literal
selector on each trial source. They give every source and force the
maximum fibre (r−1)(s−1), with exactly two nontrivial equality targets.

Fixed matrices are lonesum and the only other recurrent periods are two.
Those facts do not imply a complete narrow-box maximum or a transpose
bound. The wide restriction is explicit; the unproved square/narrow
formula is not promoted.

The code exhausts thirteen boxes plus thirty-eight wide witnesses.
This manuscript author adapts their prior Stage-1 graph verifier and
labels the reuse honestly. Mathematical proofs, finite counterexample
pressure and external ownership are separate obligations.
