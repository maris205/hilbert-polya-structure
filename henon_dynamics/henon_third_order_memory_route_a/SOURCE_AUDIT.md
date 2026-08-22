# Source audit and boundary — C113

- The recurrence and rational parameters (a=-55/16,kappa=1/2) are frozen
  before solving the cycles.
- Fixed and period-two equations are solved directly from the map using exact
  symbolic arithmetic over (mathbb Q(\sqrt5)).
- The determinant/characteristic-polynomial prefix is finite-dimensional and
  is not called a Fredholm determinant.
- No prime, zero, Euler, root-number, or automorphy data are imported.

Novelty is `UNVERIFIED`; this is a scoped dynamics pilot.
