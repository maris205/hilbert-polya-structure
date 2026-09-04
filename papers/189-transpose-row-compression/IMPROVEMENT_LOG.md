# P189 author improvement log

## Pre-freeze counterexample pass

The first derivation was stress-tested before Round 0 was frozen.  Three
failure modes were resolved in the theorem statement and proof:

1. The shallow orbit does **not** satisfy `F^2=F` or `F^3=F`; explicit
   two-dimensional witnesses force the correct identity `F^4=F^2` and the
   alternating `F^2/F^3` phases.
2. The labelled row-sum vector controls time one and depth at most one, while
   only its multiset controls time two.  The proof now keeps `r`, `r*`, and
   `r_down` distinct throughout.
3. In the time-two fibre, multiplicities belong to `lambda=mu*`, the required
   row-sum multiset, not directly to the target column-height partition `mu`.
   Empty and repeated parts, including zero, are included.

The `n=1` carrier was then separated from the sharp height-two statement, and
zero-fibre target criteria were made explicit.

## Round-0 typesetting pass

The theorem and inverse atlas were compressed into a four-page anonymous A4
`amsart` artifact.  A case-array line-break delimiter was corrected during
the first compile; this was a syntax repair only and did not change a claim.
All references, fonts, metadata, and page surfaces passed the author QA.

Round 0 is now frozen as `main_round0_original.pdf`.  No reviewer-directed
change existed at that freeze.

## Hostile Review A and Round 1

The process-separated reviewer rebuilt the carrier as tuples of row-support
sets, recovered recurrence and depth by indegree peeling and reverse BFS, and
compared every one- and two-step target fibre in complete boxes through
`n=4`.  Its 1,493,113 exact assertions and all proof/source/rendering attacks
returned `Critical 0 / Major 0 / Minor 0` and `PASS`.

No source delta was requested.  `main_round1.pdf` is therefore an intentional
byte-identical receipt of the accepted Round-0 manuscript, with SHA-256
`6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`.
This records a no-change review decision; it is not evidence of novelty or
external readiness.

## Hostile Review B and Round 2

Fresh Review B represented matrices as tuples of column-bit tuples and
reconstructed the literal transition from displayed row sums. It recovered
recurrence by memoized orbit-repeat detection, rather than Review A's graph
peeling, and independently checked Ferrers reflection, partition sums,
self-conjugate counts, and both fibre masses. Exhaustive carriers through
`n=4` and transfer controls through `n=12` produced 1,493,195 exact
assertions. No Critical, Major, or Minor finding was opened.

No source or PDF delta was requested.  `main_round2.pdf` is a byte-identical
receipt of Round 0 and Round 1, again with SHA-256
`6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`.
Terminal QA remains required for the dual-review freeze, two source-only cold
builds, and final manifests. `OWNER_AMBER / HOLD_EXTERNAL` remains active.
