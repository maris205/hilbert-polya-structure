# Hostile audit

## Mathematical traps closed

- The jump sign and units are frozen before formulas.
- `2 kappa+alpha=0` is a bound-state pole, not evaluated as a resolvent cell.
- The heat image coefficient is `alpha/4`, not `alpha/2`.
- The attractive eigenfunction has squared prefactor `-alpha/2`.
- The free odd channel is not double counted.
- Heat growth for negative energy is not described as unitary instability.
- The odd sine and even Robin transforms identify a purely absolutely
  continuous continuum and exclude singular-continuous spectrum; the only
  extra spectral mass is the attractive bound-state atom.

## Evidence independence

The checker imports no producer code.  It rejects duplicate JSON keys,
requires exact keys and types at every schema layer, and proves that every
resolvent, pole, scattering, bound-state, and heat grid is unique and
complete.  It reconstructs the Green interface and obtains each heat cell by
numerical inverse Laplace transformation of that independently derived
resolvent.  The relative trace comes from the integrated diagonal resolvent
before inversion, not from a copied erfc formula.  SymPy uses a third
symbolic route.  All 30/30 repaired-hash semantic/structural, duplicate/drop,
raw duplicate-key, unknown/missing/type-confusion, and stale-hash attacks
fail.

## Scope firewall

Every prohibited target flag is false.  The source resolvent, scattering
matrix, and relative heat trace are not target arithmetic local data, Euler
factors, root numbers, automorphy, a target divisor, a target zero match, or a
Hilbert–Pólya operator.  Route B remains disabled.
