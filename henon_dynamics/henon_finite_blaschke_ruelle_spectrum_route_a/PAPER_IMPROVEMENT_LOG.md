# Internal improvement and review record

The three snapshots are staged theorem layers, not claims of three independent external review cycles.

Round 0 audit: distinguish angular derivatives from arbitrary complex-map derivatives; retain conjugation as a commuting symmetry rather than a time reversal.

Round 1 audit: inverse branches are not global on the annulus. The branch sum is single valued; t<r is the larger extension annulus. Trace-class factorization precedes finite sections. The zero-parameter Perron operator is explicitly not rank one.

Round 2 audit: sphere index uses local infinity coordinates, primitive stability product begins j=1, and log-tail ratio extends across common zeros. a=1 is a cancelled degree-one wall. A same-model author-swapped reviewer (C382 builder) checked these points and reported no blocker.

Implementation correction: the first symbolic derivative test compared differently factored expressions structurally. It was changed to exact cancellation of their difference; the final symbolic/direct-orbit test passed. This was a test implementation error, not a discovered counterexample.
