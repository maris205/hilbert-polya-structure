# Narrative report

The mathematical gain is a single closed description of *all* finite dynamics
of a linear map, rather than a list of isolated examples.  The kernel of
`A^n-I` on the cyclic module `F_q[X]/(f_i)` has dimension
`deg gcd(f_i,X^n-1)`, so direct sums give the fixed formula.  Writing
`f_i=X^{e_i}g_i` with `g_i(0) != 0` separates a nilpotent transient of height
`max e_i` from a periodic subspace of dimension `sum deg g_i`.  Möbius
inversion then finishes the orbit census.

On the full space of complex-valued functions, every functional-graph
component with cycle length `d` and `t` noncycle vertices contributes
`X^t(X^d-1)`.  Hence the zero multiplicity is exactly the number of transient
states.  This was checked by six direct symbolic characteristic polynomials,
including a nontrivial transient tree.

The GF(4) witness uses irreducible-polynomial arithmetic: `a^2=a+1`; it is not
integer arithmetic modulo four.  A hostile `Z/4Z` substitution is rejected.
The Route-A result is deliberately negative beyond formal dynamical structure:
`overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.
