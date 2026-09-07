# OTC: oriented two-step cancellation — literal 1 / pre-pilot declaration

This is the only literal map currently admitted to this bounded desk. The
other structures in search04 were history comparison groups, not new maps.

For n >= 1, carrier X_n consists of ALL loopless oriented graphs on labelled
[n]: each unordered pair has one of no arc, low-to-high, high-to-low.
Let B_uv = OR_w (A_uw AND A_wv). Define

    F(A)_uv = B_uv AND NOT B_vu   (u != v),   F(A)_uu = 0.

Both directions cancel when both two-walks exist. This is a closed autonomous
deterministic map on the entire carrier, not a tournament-only restriction,
not Gram symmetrization, and not neighborhood incomparability. OTC is a desk
label, not a literature novelty claim.

## History deductions before pilot

Commands 04 and 06 searched actual original bodies. Source/sink clicks,
Kreweras, rowmotion, Ferrers canonicalization and score-tournament maps are
consumed comparison surfaces. P171 consumes Boolean graph-power closure;
its Gram map is NOT asserted equal to OTC on the full oriented carrier.

On DAGs, cancellation can never occur: opposite directed two-walks would
give a directed closed walk. Inductively F^t(A)=A^(2^t) (Boolean powers).
If L is the longest directed path length, the first zero time is the least
t with 2^t > L, with time zero for the initially empty graph. This is an
ordinary Boolean-power restriction and receives zero temporal credit.

On a directed odd cycle of length m >= 3, F^t has arcs i -> i+2^t modulo m.
There are no opposite arcs or loops, since 2 is invertible modulo m.
The exact period is ord_m(2), not universally two: m=5 gives period four
and m=7 gives period three. These are pre-pilot analytic examples, NOT
executions outside the declared box. They prevent a naive 1/2-cycle claim.

The remaining possible value would have to be a genuine whole-carrier
recurrent classification and a separate structural every-target decoder.
Neither is currently proved. A formula that just re-evaluates the Boolean
definition on every input will not count as the second axis.

## One tiny original complete pilot, fixed in advance

Exactly n=1,2,3,4, all 3^(n choose 2) labelled states. No sample, seed,
randomness, isomorphism quotient, extra graph, or later larger n. Maximum
729 states in one carrier. For every state output its literal target, exact
tail length, exact period, minimum cycle representative, and target fibre
size. Emit complete transition/orbit/fibre tables plus every cycle and
per-n histograms. A second raw-byte-identical execution repeats this same
pilot; it is not a second scientific family or larger cutoff.

Implementation is a self-contained freestanding static x86-64 C program,
with no headers, library calls, input files, argv/environment reads, imported
code/data or dynamic linker. Runtime inputs are exactly its executable
bytes; mathematical parameters are fixed in source. Its only system calls
are stdout write and exit. Record source, compiler command/version and
binary, inspect ELF program headers and symbols, pin all producer inputs
before/after two executions, and use actual raw cmp comparisons. This is
not a claim of a hermetic compiler build or independent mathematical review.
