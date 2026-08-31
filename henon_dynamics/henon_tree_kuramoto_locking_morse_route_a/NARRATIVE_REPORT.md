# Narrative report

The decisive tree feature is not generic synchrony but uniqueness of flow.
After subtracting the mean natural frequency, a locked state must solve
`B f=eta`.  A tree incidence matrix is injective on edge space, and summing
this equation over the child side of an edge shows that the edge flow is the
frequency imbalance of that subtree.  Thus the nonlinear network problem
first becomes an exact linear cut calculation.

The remaining nonlinear step is independent edge by edge.  The flow law
`f_e=K_e sin(delta_e)` has a solution exactly when the cut demand does not
exceed the coupling.  Because a tree has no cycle consistency relation, every
choice of inverse-sine branch integrates uniquely to vertex phases after one
root phase is fixed.  Strict inequalities give two choices per edge;
saturation merges the two choices and violation destroys every locked state.

The same edge separation controls stability.  On a local lift of the torus,
the potential Hessian is `B diag(K_e cos(delta_e)) B^T`.  Restriction to any
basis of the rotation quotient is congruent to the diagonal edge matrix.
Sylvester inertia therefore converts a network eigenvalue question into a
sign count: negative edge cosines are exactly the Morse index, saturated edges
are exactly the nullity, and the strict all-positive-cosine branch is the
unique linearly stable branch modulo rotation.

The result is complete for phase-locked states on positively weighted trees.
It does not classify all unlocked running states, does not extend unchanged
to graphs with cycle-flow freedom, and supplies no arithmetic primitive-orbit
or target determinant mechanism.
