# P215 Review B independent initial DATA receiver method

2026-09-11 UTC. `SOURCE_ONLY / PRECOMMITTED_BEFORE_CAPTURE_READ`.

This receiver is independently written from the preparation contract, the
frozen Round1 definition and proof, and the accepted B source receipt. It does
not import, invoke, or read `reviews/p215_b/verify.cjs`. At runtime that file is
only checked by `lstat` to be a non-symlink regular file. Its accepted digest
must occur consistently in the preparation and review-package manifests, and
the receiver requires the capture's complete before/after package-check logs
to be raw-identical and to contain the exact successful row for that pin.

For each of the 30 carriers, the receiver enumerates every state, evaluates
the literal prefix-drawdown map, builds the full transition array and complete
predecessor buckets, removes indegree-zero vertices, and reverse-layers from
the surviving recurrent set. It requires that the recurrent set is exactly
the zero state and that every layer depth is the first-zero time and equals
the compressed sign-run statistic.

For every target beginning in zero, block barriers are computed directly.
The inverse is then constructed by dynamic programming whose state is
`(block index, last height)`: every partial nondecreasing height word is
extended through every height allowed by the next barrier. Every completed
height word is converted to a predecessor, checked by the literal map, and
compared as an exact set with the predecessor bucket. The fibre size is also
computed separately from the manuscript's first-violation binomial
recurrence. Targets outside the image must have empty buckets.

The receiver requires the exact 27-file capture, all zero exits, all twelve
empty stderr files, raw-identical before/after logs for preparation, runtime,
preparation package, scientific inputs and review package, and exact current
pin hashes (apart from the verifier-byte exception above). It parses stdout
as strict printable ASCII plus LF, requires a final LF and exactly 34 lines,
then accepts only the fixed header, parameter row, 30 exact pipe-delimited
carrier rows, one exact total row with a positive observed assertion count,
and `PASS`. It independently derives all carrier summaries and 5,704 states.

Successful reception is initial DATA only. It is not canonical adoption,
strict replay credit, a delta, final Review B, a build, Round2, a central
state update, Git synchronization, or external action. `HOLD_EXTERNAL`.

