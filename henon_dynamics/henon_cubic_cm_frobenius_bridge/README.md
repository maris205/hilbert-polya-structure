# HCS-C41: cubic CM Frobenius bridge

Status: `PROVED_ARITHMETIC_CONNECTION_NOT_HENON_DETERMINANT`.

C41 replaces C40's artificial prime damping by the minimal geometric carrier
of cubic symmetry,

\[
E:\ y^2=x^3+1.
\]

The automorphism \((x,y)\mapsto(\zeta_3x,y)\) gives \(j(E)=0\) and complex
multiplication by \(\mathbf Z[\zeta_3]\).  At every good prime define

\[
a_p=p+1-\#E(\mathbf F_p),\qquad
L_p(T)=1-a_pT+pT^2.
\]

## Main result

For every prime \(p\equiv2\pmod3\), the cube map is a bijection and an exact
character-sum argument gives \(a_p=0\).  For split primes the trace is
generally nonzero; for example \(a_7=-4\).  The local degree-two factors have
intrinsic square-root normalization and satisfy the Hasse bound.

An exact certificate counts all good primes below 2,000 and independently
recounts \(E(\mathbf F_{p^2})\) for four primes using explicit quadratic
extension arithmetic.  This is a genuine new arithmetic connection for the
cubic channel, but it is the CM elliptic \(L\)-function, not the Riemann
\(\xi\)-function and not yet a determinant derived from H\'enon periodic
orbits.

## Research extraction

- **Strongest positive result:** an intrinsic degree-two Frobenius factor
  with exact inert-prime trace vanishing and square-root-sized eigenvalues.
- **Strongest obstruction:** the arithmetic carrier is added geometry; its
  local factors do not arise from the original H\'enon orbit ledger.
- **Open theorem:** determine whether a finite virtual cohomological
  combination of the cubic curve and Tate pieces can reduce to the Riemann
  local factor without post-hoc cancellation.
- **Reusable structure:** exact \(\mathbf F_p/\mathbf F_{p^2}\) point-count
  certificate and CM inert/split controls.
- **ROUND2_CLUE:** test cohomological supercancellation locally before trying
  any global operator construction.

## Route evaluation

`(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE,
A4_FORMAL_HINT)`, overall `ROUTE_A_EXPLORATORY_ARITHMETIC_BRIDGE`.  A limited
Route-B entry audit stops at B1 because no H\'enon-derived operator/domain is
defined.

## Reproduce

```bash
python -B code/c41_cm_checker.py
python -B -m unittest code/test_c41.py
```

Paper: [`paper/paper.pdf`](paper/paper.pdf).
