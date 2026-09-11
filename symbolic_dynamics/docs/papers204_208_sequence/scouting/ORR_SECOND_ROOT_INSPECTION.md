# ORR second proof attempt: root acceptance of the boundary

2026-09-07 UTC. **TWO_SIDED_BOUND_PROVED / SHARP_CLOCK_UNPROVED /
NO_PROMOTION / HOLD_EXTERNAL**. This closes the assigned pure-proof task;
it is not a twenty-sixth intake or a new candidate gate.

Root read all six new payloads, the complete original local-ancestry note
and original pre-code argument. The [new complete proof](ORR_SECOND_CLOCK_ATTEMPT/PROOF_PACKAGE.md)
establishes exactly
$$
\left\lfloor\frac{n-1}{2}\right\rfloor
\le H_n\le\binom{\lceil n/2\rceil}{2}\quad(n\ge1),\qquad H_0=0.
$$

The lower trajectory has a unique active triple at every step; its larger
two labels extend a descending prefix. Prepending a new maximum gives the
even case with a permanent descent boundary. The proof handles n=0,1,2.
This is an every-epoch symbolic induction, not extrapolation from a census.

For the upper bound, colours mean the parity of each label's **initial
position**, not its numerical label parity. Odd interval reversals preserve
these classes. A length 2r+1 active run gains exactly r(r+1) cross-colour
inversions, at least two. No cross-interval label order changes. Root checked
the colour-sorting comparison: swapping same-colour neighbours across one
opposite-colour label changes the statistic by two precisely when the middle
label lies between them, and by zero otherwise. Sorting each class therefore
gives its minimum/maximum comparison words. Odd-size reversal bounds the
range by m(m+1); for size 2m the m diagonal colour pairs keep their order,
and only m(m-1) off-diagonal pairs can increase. Division by the per-epoch
gain proves the displayed quadratic upper bound on the unchanged carrier.

The original seven-label orbit also refutes the proposed single-chain
two-fresh-label charge: the chain {1,4,7}->{2,5,7}->{2,4,6} adds only
label 6 in its final step. The other ancestry branch accounts for label 3;
it does not repair a false charge on the single chain. Endpoint-parity
inheritance is correct but provides no proven linear depth bound.

Accordingly the conjectured equality
$$H_n=\lfloor(n-1)/2\rfloor$$
remains **NOT CURRENTLY JUSTIFIED**. No counterexample to that equality is
claimed. The proof-writer discipline fixes the exact weakened statement
and explicit remaining overlap/depth gap; it does not promote a generic
quadratic potential to the missing qualifying temporal contribution.

Root checked all six payloads twice with complete nonself directory
coverage, no symlinks and all seven operative historical input pins twice.
Actual exit was zero; payload total is 21,973 bytes and outer seal is
`ab8212425ac8c4ff13c1b209925ce3197af03b30724589dbadbb83c2860bf37a`.
The [author check record](ORR_SECOND_CLOCK_ATTEMPT/CHECKS.md) separately
retains its actual seven original-check lines. No mathematical code,
old verifier, pilot, larger box, canonical pair or science comparison was
run by this attempt or the root closure.

The scout's additional flip-sort primary reading is explicitly bounded in
[SOURCE_READS](ORR_SECOND_CLOCK_ATTEMPT/SOURCE_READS.md); root does not
relabel that as a new root primary-body reading. No external clock theorem
is used in the two-sided proof. Original twenty-second proofs/pilots,
Fibonacci inverse, failed arguments and first root note remain unchanged.
Root, the original scout and its lower-bound helper are proof contributors,
not independent ORR assessors. No admission or paper number follows.
