# Source and assumption audit

## Frozen construction

The graph is the undirected 3-cycle, whose Laplacian is
\[
L=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}.
\]
The exact parameters are `a=7`, `kappa=1/5`; all arithmetic is rational.

## What is derived internally

- The producer derives the gradient, Hessian, Jacobian, inverse, and exact
  monodromy matrices from the frozen potential.
- The checker independently recomputes these objects and checks canonical JSON
  bytes, orbit closure, determinants, symplectic identities, and mode factors.
- SymPy independently verifies the polynomial identities and the degree-six
  period-two determinant prefix.

## Boundary of evidence

The finite ledger contains two fixed-point witnesses and one primitive
period-two witness. It is not an exhaustive orbit enumeration, a Markov
partition, a Fredholm determinant, or an analytic continuation result. No
external literature or arithmetic local data are imported into the claim.
