# C135 source audit

## Frozen source

```text
B = [[1,1],[1,1]]
tau_00=1, tau_01=sqrt(2), tau_10=sqrt(3), tau_11=sqrt(6)
M(x) = [[x00,x01],[x10,x11]]
Delta(x)=det(I-M(x))
d_tau(s)=det(I-M(exp(-s tau_ij)))
clock = continuous suspension time with base return count retained
```

No paper, website, external database, prime table, zero table, arithmetic
local datum, fitted parameter, or Route-B input is used.  The primitive
product is a symbolic-dynamical identity and is never called an arithmetic
Euler factorization.

## Integrity boundary

The producer uses integer coefficient dictionaries indexed by exact edge-count
vectors.  It is reconstructed by a standard-library checker importing no
producer code, an independent SymPy implementation, byte replay, 42
repaired-payload-hash semantic mutations, and one stale-hash mutation.  The
period-ten ledger is replay evidence only; all determinant and primitive
formulas are proved for every period.

The package explicitly retains the first same-edge-count primitive collision
at period six and the theorem `N01=N10`.  It therefore claims edge-sector
injectivity, never orbit injectivity or recovery of off-diagonal orientation.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
