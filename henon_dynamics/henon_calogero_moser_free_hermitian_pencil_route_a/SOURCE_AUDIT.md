# C196 source and ownership audit

## Primary source lock

F. Calogero, “Solution of a Three-Body Problem in One Dimension,” *Journal of
Mathematical Physics* 10(12), 2191--2196 (1969), DOI
`10.1063/1.1664820`.  The DOI and Crossref publisher metadata were checked.
This is the required primary historical source for the inverse-square model;
it is not used alone to support the all-`N` theorem.

J. Moser, “Three integrable Hamiltonian systems connected with isospectral
deformations,” *Advances in Mathematics* 16(2), 197--220 (1975), DOI
`10.1016/0001-8708(75)90151-6`.  The DOI and Crossref metadata were checked.
Moser retains primary ownership of the rational many-body isospectral and
scattering solution used here.  The precise locator is Sections 3--4 together
with the Section-4 ``Note added in proof,'' which records the all-particle
verification of the zero-shift scattering statement.

## Convention audit

The package fixes

\[
H=\frac12\sum_jp_j^2+\sum_{j<k}\frac{g^2}{(q_j-q_k)^2},
\quad
L_{jk}=p_j\delta_{jk}+\frac{ig(1-\delta_{jk})}{q_j-q_k}.
\]

Therefore `[Q,L]=ig(J-I)`, `Tr L^2=2H`, and
`ddot q_j=2g^2 sum_(k!=j)(q_j-q_k)^(-3)`.  Reversing `ig`, summing the
potential over ordered pairs, or rescaling physical time would corrupt the
atlas sign or force factor.  All executable and written artifacts use the
same declared convention.

## Claim ownership and boundary

- **Classical attributed structure:** the inverse-square model, Moser Lax
  solution, and scattering coordinates.
- **Package closure:** one proof chain through pencil simplicity,
  completeness, trace invariants, both ordered ends, the forward/inverse
  atlas, and the periodic obstruction.
- **Executable role:** exact Gaussian-rational identities and finite
  regression under three independent algorithms.  Numerically, the inverse
  sentinel reconstructs the initial position spectrum; the full inverse
  phase-space atlas is established by the analytic proof, not by that census.
- **Not claimed:** classical priority, literature-wide novelty, symplecticity
  of the displayed atlas, a quantum spectral theorem, external peer review,
  or acceptance.

The two-source bibliography supplies no target zeros, prime tables,
arithmetic local data, Euler factors, root numbers, automorphy, target
divisors, or Route-B input.
