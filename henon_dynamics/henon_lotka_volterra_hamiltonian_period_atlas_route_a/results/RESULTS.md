# C211 exact results

- Six positive rational parameter sets; four energies per set (24 levels).
- Every Lambert-W branch endpoint, area, period, action, and center-period
  ratio is serialized at 34 significant digits from 45 working digits.
- The independent checker passes 732 assertions.  Its SciPy DOP853 event path
  starts at the right turning point and recovers the next positive `v=0`
  crossing; all 24 periods agree within `1e-8 max(1,T)`.
- SymPy passes 12 Hamiltonian, Hessian, linearization, and normalization
  identities.  Byte replay is exact.
- Hostile audit rejects 11 repaired-hash semantic mutations and one stale-hash
  mutation (12 total), including branch, period, action, route, and scope
  changes.

The numerical ledger is a finite control for the proved global theorem.  It is
not evidence for period monotonicity or a high-energy expansion.
