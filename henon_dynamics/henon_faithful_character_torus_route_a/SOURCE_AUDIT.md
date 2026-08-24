# C134 source audit

## Frozen source

```text
A = [[3/16,-1/32],[1/4,0]]
B = [[1,1,0],[1,0,1],[1,0,0]]
c = (1/2,1/3,1/5)
k >= 1
t = any branch permutation of (-2k,0,2k)
domain = three copies of D_(3k)^2
chi_X(m)=X^m in Q[X,X^(-1)]
q=(3+4i)/5
D_t,u(z)=det(I-z L_t,u)
```

No paper, website, numerical database, prime table, zero table, arithmetic
local datum, fitted parameter, or Route-B artifact enters the construction.
The package makes no literature-novelty claim and has no external citation.

## Exact evidence boundary

All Laurent coefficients use `Fraction`; the faithful anchor uses Gaussian
rationals.  The producer is reconstructed by a standard-library checker that
imports no producer code, an independent SymPy implementation, byte replay,
and 47 repaired-payload-hash plus one stale-hash mutations.  Period eight is
only a replay prefix; the theorems are all-period.

The identity

```text
D_{-t,u}(z)=D_{t,u^{-1}}(z)
```

denotes inversion of the labelled character parameter, never a reciprocal
determinant.  Removing that parameter orientation leaves a sign ambiguity.
Exact faithful-character injectivity is not promoted to floating-point
stability or geometry outside the frozen family.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
