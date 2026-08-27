# C193 research question

Can the positive Markoff equation supply an intrinsic arithmetic dynamical
owner strong enough for Route A, and what exact global theorem survives if the
answer is no?

The frozen phase space consists of sorted positive integer triples satisfying
`x^2+y^2+z^2=3xyz`.  The autonomous map replaces the unique largest
coordinate by the other Vieta root and sorts again.  Its clock is one descent
step and its Lyapunov function is the largest coordinate.

The required large step is global:

- prove invariance under all three coordinate Vieta involutions;
- prove that every non-root normalized solution has a unique maximum;
- prove positivity and strict height decrease of its canonical parent;
- prove finite termination at `(1,1,1)`;
- reverse the edges to generate every positive solution;
- identify the permutation quotient as a rooted tree and rule out non-root
  recurrence.

The arithmetic hypothesis is deliberately bold but graded strictly.  The
integer cubic and its transformations are intrinsic Diophantine data, so the
candidate is not `A0_FAIL`.  Yet the object contains no canonical rational
prime-to-orbit correspondence, prime-power repetition, von Mangoldt weight or
logarithmic prime clock.  It cannot pass A0 structurally.

No statement about reductions modulo primes is allowed, and the open
Frobenius claim that a Markoff number determines a unique triple is not needed
or asserted.
