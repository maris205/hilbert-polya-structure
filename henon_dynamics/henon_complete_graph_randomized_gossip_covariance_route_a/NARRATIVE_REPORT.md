# Narrative report

The complete graph makes randomized gossip exactly solvable beyond its usual
mean-square rate.  Each update is a symmetric rank-one relaxation, and the
complete-graph edge sum is the Laplacian `NP`.  This already determines the
mean and the trace of the second moment.  The larger step is to diagonalize
the entire second-moment transfer.

Centered symmetric matrices split orthogonally into three natural pieces.  A
multiple of the centering projector records total disagreement energy.  A
trace-free diagonal pattern generates the standard block after centering.
The remaining matrices have zero diagonal and zero row sum.  Direct edge-sum
identities show that the transfer is scalar on each piece, so its powers and
the full covariance are explicit at every time.

The pieces are invariant for the full closed relaxation interval.  For
positive relaxation their present eigenvalues are pairwise distinct, making
the nonzero pieces full eigenspaces.  At zero relaxation the transfer is the
identity, so the pieces instead merge into the eigenvalue-one eigenspace of
the whole centered symmetric space.

This closure also clarifies the endpoints.  Interior relaxation parameters
strictly contract mean-square disagreement and yield almost-sure consensus.
At zero relaxation nothing moves and the full second-moment eigenspace is
degenerate.  At unit relaxation every interaction is a
coordinate swap: the law mixes labels but never reduces disagreement energy.
That endpoint touches the random-transposition subject of C183, but it is not
the owner of the present dissipative theorem.

The source mathematics is useful and exact, but it contains no intrinsic
rational-prime carrier, logarithmic prime clock, primitive-orbit determinant,
target analytic divisor, or natural unitary quantization.  The symmetric
moment transfer supplies only a formal source-local lift hint.  Route A is
therefore rejected and Route B remains locked.
