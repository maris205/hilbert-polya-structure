# Source and collision audit — HCS-C300

## Verified literature owners

1. P. D. Lax, “Hyperbolic systems of conservation laws II,”
   *Communications on Pure and Applied Mathematics* 10 (1957), 537--566,
   DOI [10.1002/cpa.3160100406](https://doi.org/10.1002/cpa.3160100406).
   The publisher record verifies author, title, year, volume and pages.  This
   is the owner token for characteristic families, admissible shocks and the
   classical Riemann construction.
2. B. L. Rozhdestvenskii and N. N. Janenko, *Systems of Quasilinear
   Equations and Their Applications to Gas Dynamics*, AMS Translations of
   Mathematical Monographs 55 (1983), DOI
   [10.1090/mmono/055](https://doi.org/10.1090/mmono/055).  The official AMS
   contents explicitly list isentropic/isothermal flow, Riemann invariants,
   compression and rarefaction waves.  This is the gas-dynamics context
   owner.
3. C. M. Dafermos, *Hyperbolic Conservation Laws in Continuum Physics*,
   Springer, DOI
   [10.1007/978-3-642-04048-1](https://doi.org/10.1007/978-3-642-04048-1).
   This is a modern framework reference for admissible wave fans and convex
   entropy, not evidence of novelty.

The paper rederives every specialized isothermal formula.  It claims neither
that the Riemann method is new nor literary priority for its monotone scalar
solver.

## Workspace collision scan

Direct searches of all C1--C298 titles, registries and recent idea reports
found no positive-density isothermal Euler package.  C195 is the closest
named neighbor, but it treats periodic viscous scalar Burgers flow.  C300 has
two conserved fields, two genuinely nonlinear characteristic families, four
elementary-wave combinations and a different entropy/state-space contract.

An earlier idea ledger rejected a one-wave inviscid Burgers Riemann problem as
too small and too close to C195.  C300 is the deliberate repair: it proves the
complete arbitrary-data solver for a strict `2 x 2` system, not a renamed
scalar slice.

## Claim/source separation

- The eigenvalues `u-a,u+a`, wave curves, shock speeds and mechanical entropy
  are source PDE data.
- Finite regression cases do not prove the all-data theorem; strict
  monotonicity and the Rankine--Hugoniot/Lax argument do.
- “No vacuum” is restricted to finite velocities, positive input densities
  and `a>0`.  Vacuum inputs and pressureless limits are explicitly excluded.
- No target arithmetic local datum, Euler factor, root number, automorphy,
  target divisor/counting law, functional equation, target zero match or
  Hilbert--Polya operator is present.  Route B is not authorized.

Verified on 2026-09-02 under scope `NO_BAD_EULER_OR_ROOT_NUMBER`.
