# Experiment plan

## Claim-led objective

Audit one complete finite open Toda theorem from Hamiltonian coordinates through
the Lax pair, global positivity, fixed Jacobi spectrum, sorted scattering, and
simple-spectrum norming coordinates.  The ledger also isolates the exact
two-particle formula and a repeated-root boundary so that regular claims are
not silently extended to singular blocks.

## Frozen source grid

Six rational Flaschka initial rows are frozen: three \(N=2\) rows and three
\(N=3\) rows.  Every row is integrated at \(t=-2,-1,0,1,2\) with a classical
RK4 scheme using 256 steps per unit time and 90-decimal arithmetic.  The
receipt records every \(a_j,b_j\), all \(I_k=\operatorname{tr}(L^k)/k\), the
sorted eigenvalues, positivity, drift, and \(H=4I_2\).  A separate \(T=8\)
endpoint diagnostic reports the reversed/forward sorting errors but does not
call a finite endpoint an asymptotic limit.

For all \(N=2\) rows, the same times are evaluated by the closed
\(\operatorname{sech}/\tanh\) solution.  For all \(N=3\) rows, first-component
spectral weights are compared with the exact normalized exponential law at
\(t=-1,0,1\).  The singular ledger includes the block matrix
\(\operatorname{diag}(0,0,1)\), whose characteristic polynomial is
\(x^2(x-1)\).

## Independent checks and release gates

The checker duplicates matrix construction, RK4, eigensystem, norming weights,
and the \(N=2\) formula without importing producer functions.  SymPy checks the
entrywise commutator, trace invariants, concrete characteristic polynomials,
the closed \(N=2\) equations, and the norming logistic law.  Clean replay must
reproduce canonical bytes; hostile mutations repair payload hashes before
validation and must all be rejected.

The release requires three content-distinct LuaLaTeX PDFs, two fresh fixed-epoch
builds for every revision, embedded subset fonts, no sidecars, exact 27-file
manifest closure, and a visible Route-A rejection boundary.  No prime/zero
tables, Euler factors, root numbers, automorphy, target divisor, or
Hilbert--Polya operator enters any artifact.

