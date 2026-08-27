# Source audit

## Frozen owner

The owner is the constant-parameter Polyak heavy-ball iteration on
`f(x)=x^T A x/2-b^T x`, with real SPD `A`, `m I <= A <= L I`, real
`alpha,beta`, phase state `(e_k,e_(k-1))`, and integer clock `k`.

## Primary and official sources checked

- B. T. Polyak, *Some Methods of Speeding up the Convergence of Iteration
  Methods*, USSR Comput. Math. Math. Phys. 4 (1964), DOI
  [10.1016/0041-5553(64)90137-5](https://doi.org/10.1016/0041-5553(64)90137-5).
- V. Ugrinovskii, I. R. Petersen and I. Shames, *A Robust Control Approach to
  Asymptotic Optimality of the Heavy Ball Method for Optimization of Quadratic
  Functions*, Automatica 155 (2023), DOI
  [10.1016/j.automatica.2023.111129](https://doi.org/10.1016/j.automatica.2023.111129).
- L. Lessard, B. Recht and A. Packard, *Analysis and Design of Optimization
  Algorithms via Integral Quadratic Constraints*, SIAM J. Optim. 26 (2016),
  DOI [10.1137/15M1009597](https://doi.org/10.1137/15M1009597), used to police
  the nonlinear-objective boundary.

The paper proves the stated quadratic formulas directly and claims no
historical priority or external review.

## Collision and scope audit

C197 is relaxed Douglas--Rachford on principal-angle blocks; C191 is positive
matrix scaling; C185 is a continuous isospectral gradient flow.  None owns the
two-step inertial companion map, its all-real Jury triangle or Jordan-correct
minimax boundary.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic
or Route-B object is used.
