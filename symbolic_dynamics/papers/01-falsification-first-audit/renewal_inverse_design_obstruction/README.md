# SD-C03 — Renewal Inverse-Design Obstruction

## Frozen construction

The graph has one base vertex and one aggregate first-return loop of length
\(n\) with complex weight \(a_n\) for every \(n\ge1\):

\[
F(z)=\sum_{n\ge1}a_nz^n,\qquad
D_{\rm ren}(z)=1-F(z),\qquad
\zeta_{\rm ren}(z)=D_{\rm ren}(z)^{-1}.
\]

## Findings

- **PROVED:** every holomorphic germ \(H(0)=1\) can be represented exactly by
  choosing \(a_n=-[z^n]H\).  The same mechanism represents preregistered
  on-circle and off-circle controls.
- **PROVED:** for nonnegative coefficients, if \(F(r)\) crosses one before its
  convergence boundary, then \(D_{\rm ren}\) has a positive real zero.
- **PROVED:** a shared-base renewal grammar necessarily creates mixed
  primitive words.  With two atoms \(a,b\), the coefficient of \(x_ax_b\) in
  \(1/(1-x_a-x_b)\) is two, while it is one in the independent Euler product
  \((1-x_a)^{-1}(1-x_b)^{-1}\).
- **PROVED:** a finite-dimensional unitary cocycle cannot make the mixed
  primitive factor identically one.
- **PROVED:** a unary regular or context-free return language cannot select
  exactly the prime lengths, because its length set is ultimately periodic.

These are model-identifiability and grammar obstructions.  Exact fitting is a
PROVES_TOO_MUCH failure, so no Riemann target is fitted and Route B is not
invoked.

## Artifacts

- [Derivation package](DERIVATION_PACKAGE.md)
- [Proof package](PROOF_PACKAGE.md)
- preregistered synthetic-control outputs under the session-level results/
  directory
