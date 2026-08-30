# Experiment and proof plan

1. Freeze the map, cyclic indexing, labelled-word convention, one-tick clock,
   wall coordinate, and all degenerate (n=1,2) faces.
2. Derive (and independently test) the wall update.  Enumerate every local
   neighbourhood and every finite state through (n=14); record period,
   wall-run maximum, entry time, and trajectory.
3. Prove block erosion and the sharp $\lfloor(n-1)/2\rfloor$ entry bound.
   Separate the even-$n$ all-one wall word before applying the finite-run
   transfer matrices.
4. Build the four-state pair de Bruijn matrix for the fixed language and
   derive its characteristic polynomial and Lucas/cosine closed count.
5. Build parity-twisted run matrices $B_m,B_m^-$, compare their traces with
   exhaustive state counts, and publish cumulative/depth receipts.
6. Run producer, independent checker, SymPy reconstruction, byte replay, and
   40 hostile mutations.  Compile three substantive manuscript revisions in
   two fresh fixed-epoch trees and close the release manifest.

The finite computation is a certificate of the all-size source theorem.  It
is not a target comparison and does not authorize Route B.
