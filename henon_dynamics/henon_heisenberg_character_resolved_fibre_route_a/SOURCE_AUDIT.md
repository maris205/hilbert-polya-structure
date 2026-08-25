# C151 source audit

## Source class and lock

C151 is an exact continuation of the source-locked C146 Heisenberg
automorphism.  It uses the real group law
`(x,y,z)(X,Y,Z)=(x+X,y+Y,z+Z+xY)`, lattice `Z^3`, matrix
`A=((2,1),(1,1))`, and the forced integer-valued correction
`q(x,y)=x(x-1)+xy+y(y-1)/2`.  The quotient is the left quotient
`Gamma\H`, and the clock is the iterate `n`.  No parameter is fitted.

Horizontal classes are represented by `m` modulo `(A^n-I)Z^2`, with
`v=(A^n-I)^(-1)m`.  A column Hermite fundamental rectangle supplies one
representative per class.  The theorem is all-iterate; the exact histogram
cutoff `n<=12` is a validation receipt, not a source of extrapolation.

## Independence

The producer evaluates a precomputed exact quadratic cocycle.  The checker
imports no producer code and instead advances numerator pairs iterate by
iterate over a common denominator.  SymPy supplies a third path through its
matrix powers, Hermite normal form, and rational algebra.  Replay demands byte
identity.  Mutations repair the payload hash before semantic rejection.

## Claim firewall

The finite central cyclic root-of-unity projector counts clean fixed circles;
it is not a horizontal-quotient character formula, a trace formula, or an
isolated-orbit determinant.  No target table, prime table,
arithmetic/local factor, Euler factor, root number, automorphy datum, target
divisor, Hilbert--Polya operator, or Route-B input is present.  Literal scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
