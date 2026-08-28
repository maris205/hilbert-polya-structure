# Narrative report

## What moved

C222 closes the whole minimum-time problem, not merely the familiar statement
that a double integrator is “bang--bang.”  The package gives an explicit value
on every state, identifies which side of the switching parabola selects which
control order, proves both arc lengths are admissible, and derives the switch
and terminal states.  Its decisive global step is the exact reachable-moment
interval: it supplies a sharp lower bound and makes the one-switch control a
sufficient optimum, while Pontryagin and HJB serve as independent structural
checks.

The singular pieces are not hidden.  The origin, direct-braking parabola,
zero acceleration, reflection and parabolic scaling are separate theorem
branches.  The value is continuous but nonsmooth at the switch curve.

## Evidence boundary

The 105 rational rows exercise all branches but do not prove the continuum
theorem.  Proof comes from the rearrangement inequality and exact algebra.
The independent checker reconstructs each row without importing the producer;
the symbolic script reconstructs generic identities; replay and hostile
mutation tests audit provenance and schema.

## Route-A result

The result is a substantial source-system theorem and still a strict Route-A
rejection.  The Pontryagin Hamiltonian is a formal variational device, not a
same-clock arithmetic spectral bridge.  There is no rational-prime carrier,
primitive-orbit owner, target determinant, target analytic structure or
Hilbert--Polya operator.  Route B remains unauthorized.
