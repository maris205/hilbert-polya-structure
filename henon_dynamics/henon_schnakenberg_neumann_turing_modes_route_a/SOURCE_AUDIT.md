# Source audit

## Primary lineage

1. J. Schnakenberg, “Simple chemical reaction systems with limit cycle
   behaviour,” *Journal of Theoretical Biology* **81** (1979), 389--400,
   DOI [10.1016/0022-5193(79)90042-0](https://www.sciencedirect.com/science/article/pii/0022519379900420).
   This is the primary source owner for the named autocatalytic reaction
   kinetics.  Its abstract concerns chemical reaction systems and limit-cycle
   selection; it is not cited as the owner of this package's finite-interval
   mode-count formula.
2. A. M. Turing, “The Chemical Basis of Morphogenesis,” *Philosophical
   Transactions of the Royal Society of London B* **237** (1952), 37--72,
   DOI [10.1098/rstb.1952.0012](https://royalsocietypublishing.org/doi/10.1098/rstb.1952.0012).
   This is the original reaction--diffusion instability lineage.  The present
   package uses the standard modal mechanism but claims no priority over it.

## Claim boundary

The package is a source-local, convention-locked reconstruction of the exact
linear dispersion and discrete Neumann selection problem for one normalized
Schnakenberg system.  It does not claim invention of Schnakenberg kinetics,
Turing instability, reaction--diffusion mode analysis, or pattern formation.
It proves neither a nonlinear patterned branch nor nonlinear global dynamics.

## Workspace collision audit

- C311 proves an ODE Brusselator Hopf normal form, not a spatial Turing mode
  atlas.
- C304 studies a scalar fourth-order linear Cahn--Hilliard shell problem, not
  a two-species reaction Jacobian with unequal diffusion.
- C347 studies a nonlocal nonlinear Kuramoto Fokker--Planck equation, not a
  local activator--inhibitor Neumann system.
- C202 studies scalar Fisher--KPP traveling fronts, not stationary
  diffusion-driven modal instability.

The finite-domain strict mode count and length-wall ledger are local derived
results.  “NEW” means only that no earlier workspace package owns this frozen
mechanism.
