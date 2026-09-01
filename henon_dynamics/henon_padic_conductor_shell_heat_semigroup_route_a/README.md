# HCS-C283 — conductor-shell heat semigroup on \(\mathbb Z_p\)

This package gives a closed theorem-and-evidence certificate for one explicit
operator on the compact additive group \(\mathbb Z_p\).  For an arbitrary but
fixed prime \(p\), normalized Haar measure, and the character basis indexed by
\(\mathbb Q_p/\mathbb Z_p\), the operator is frozen by

\[
D_{p,\alpha}1=0,\qquad
D_{p,\alpha}\chi_\xi=p^{\alpha n(\xi)}\chi_\xi,
\quad \alpha>0,
\]

where \(n(\xi)\ge1\) is the exact conductor.  This definition is the owner: no
normalization of an operator called “Vladimirov” is imported.  Its positive
mean-zero spectrum, multiplicities, geometric zeta, and pole lattice coincide
with the dimension-one Taibleson example of
Chacón-Cortés--Zúñiga-Galindo and receive zero originality credit.  The
package is retained as a source-local Markov/scale/boundary certificate, not a
literature-priority claim.

The package proves the complete spectrum and multiplicities, the positive
Markov/contraction semigroup, trace formula, full mean-zero zeta pole lattice,
primed zeta determinant, exact staircase count and discrete-scale oscillation,
sharp resolvent Schatten threshold, and every declared \(\alpha=0\), \(\mu=0\),
and \(t=0\) face.  Finite quotients \(\mathbb Z/p^N\mathbb Z\) independently
reconstruct the same operator by a character DFT and a conditional-expectation
filtration.

## Reproduction

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c283_padic_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c283_padic_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c283_padic_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c283_padic_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c283_padic_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c283_release_manifest.py
```

The final command closes the exact 28-file release.  The build contract fixes
`SOURCE_DATE_EPOCH=1788220800`, uses two LuaLaTeX passes in two fresh
directories for each revision, and requires byte-identical replicas.

## Route-A boundary

The honest tuple is

`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`

with overall `ROUTE_A_REJECTED` and Route B disabled.  The fixed local prime
and its conductor filtration justify only A0 weak: they are not the family of
all rational primes, target Euler factors, bad-prime data, root numbers, a
target divisor, or a Hilbert–Pólya operator.  The literal scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
