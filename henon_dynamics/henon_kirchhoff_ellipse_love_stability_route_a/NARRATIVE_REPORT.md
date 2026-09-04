# Narrative report

C372 changes subtype to a free-boundary Hamiltonian fluid.  The Kirchhoff
ellipse is a true relative equilibrium of two-dimensional Euler, not a
finite-dimensional ellipse ansatz imposed on an unrelated PDE.  Its Love
modes turn the stability question into a factorized exact spectral problem.

The main advance is a complete threshold ladder.  Every mode `m>=3` has one
wall, those walls are strictly ordered, the first is exactly `a/b=3`, and
the high-mode aspects grow linearly with an explicit Lambert-W constant.
This is substantially stronger than checking a handful of modes.  Exact
finite evidence makes every implementation decision replayable.

The audit also repairs a subtle clock ambiguity: because an ellipse as a set
is invariant under a half-turn, its minimal patch period is `pi/|Omega|`,
whereas an oriented-axis lift has period `2pi/|Omega|`; at the circle the
orientation disappears entirely.

Despite the strong dynamics, Route A fails arithmetically.  Physical time,
continuous aspect, and Fourier mode number provide no rational-prime carrier
or primitive-orbit determinant.  The modal Hamiltonian structure remains
only an A4 formal hint.
