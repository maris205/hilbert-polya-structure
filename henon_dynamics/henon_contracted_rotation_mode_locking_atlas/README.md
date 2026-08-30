# HCS-C240 — Contracted rotation mode-locking atlas

This package freezes the discontinuous piecewise-affine map

\[
 f_{\lambda,\delta}(x)=\{\lambda x+\delta\},\qquad
 0<\lambda<1,
 \quad x\in[0,1),\quad 0\leq\delta<1 .
\]

The fractional-part convention is implemented by a binary carry
\(k_j\in\{0,1\}\):
\(x_{j+1}=\lambda x_j+\delta-k_j\) with
\(k_j\leq\lambda x_j+\delta<k_j+1\).  For every primitive cyclic word of
length at most 12 and each of the three frozen rational slopes
\(\lambda\in\{1/2,2/3,3/4\}\), the producer computes the affine fixed point,
all state affines, the exact half-open \(\delta\)-interval, derivative,
rotation number, and an equality audit at both endpoints.  There are 747
primitive canonical words per slope (2241 rows total) and 138 nonempty
word-certified components.  A separate high-precision iteration ledger uses
295 base-grid and endpoint probes.

The finite atlas is deliberately conservative.  A word has one fixed point
because \(1-\lambda^n>0\); no global one-periodic-orbit theorem is claimed.
The cited general two-branch piecewise-contraction theorem gives only an
at-most-two bound under its hypotheses.
Grouped rows are unions of certified components, not asserted maximal plateaux.
The source-local factor \(1-z^n\lambda^n\) is bookkeeping for a declared
itinerary only, never a target determinant or an arithmetic Euler factor.

The release has 28 physical files (27 manifest-listed payload files plus the
self-excluded manifest), fixed epoch `1788048000`, source/code baseline
`489506cf92bfed721f94f22dd0444a60427f90a5`, and scope literal
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target primes, zeros, local factors, root
data, automorphy, target divisor, or Hilbert–Pólya operator is used or claimed.
“NEW” is workspace-local and is not a literature-priority statement.

Run the deterministic audit from this directory:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c240_contracted_rotation_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c240_contracted_rotation_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c240_contracted_rotation_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c240_contracted_rotation_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c240_contracted_rotation_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c240_release_manifest.py
```

The strict Route-A tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B is
disabled.  A1 refers only to the declared finite word/interval certificate;
A2 is an explicit target-match failure.
