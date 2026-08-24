# Research question — C120

## Frozen question

For the exact quartic variational map

\[
F(q,p)=(q^3-2q-p,q),
\]

can one exhibit a primitive period-three orbit for which reversibility,
area preservation, generating-function stationarity, chronological tangent
monodromy, action, nondegeneracy, and Morse index are all certified without
floating-point input?

## Admissible answer

The package may certify the three named fixed points and one named primitive
three-cycle, together with exact local variational data. It must also show
that the result depends on the frozen map and cyclic word by explicit negative
controls.

## Excluded extrapolations

The finite witness does not establish completeness of periodic orbits, a
target prime correspondence or log-prime clock, global twist or minimax
classification, a source-owned dynamical zeta/Fredholm operator, a target
divisor, analytic continuation, arithmetic/local data, Euler factors, root
numbers, automorphy, a Hilbert–Pólya operator, or Route B.

## Route-A interpretation

- `A1_WEAK`: exact fixed points and one primitive period-three variational
  witness, but no complete enumeration or target prime correspondence.
- `A2_FAIL`: a finite tangent determinant is not a source-owned dynamical
  zeta/Fredholm object and supplies no target divisor.
- `A3_FAIL`: no global determinant, functional equation, Gamma/trivial-zero
  treatment, continuation theorem, or target divisor exists here.
- `A4_FORMAL_HINT`: the action and Morse data are variational structure,
  but no quantum/scattering object, Hilbert space, or operator domain is given.

The canonical tuple is `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` and the
overall status is `ROUTE_A_EXPLORATORY`.
