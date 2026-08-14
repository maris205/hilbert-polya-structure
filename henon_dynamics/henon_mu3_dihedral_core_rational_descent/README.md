# HCS-C53: rational descent of the Hénon moment packets

Status: **RELEASE_CANDIDATE; implementation provenance backfilled**.

C53 implementation commit:
`0a7f0fdb8290eab4aa92ed5ade432401c40c22cf`.

Source lock: C52 implementation commit
`208feef86365cd92ace8dad02904acff6623eeec`; frozen C52 certificate
SHA-256
`a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94`.

## Result in one paragraph

For every `n >= 2`, the source-ordered complete intersection

\[
X_n=V\!\left(\sum_{i=0}^{2n-1}x_i^3,
\sum_{i=0}^{2n-2}x_ix_{i+1}+\rho x_{2n-1}x_0\right)
\subset\mathbf P_K^{2n-1},\qquad K=\mathbf Q(\rho),
\]

has an explicit model over \(\mathbf Q\). This is an equation-level theorem
for all \(n\); smoothness and motive statements are asserted only for the
certified rows \(n=2,3,4\). For those rows, the C51 moment packet descends to
a rational packet \(\mathsf W_n\) of rank \(4^n-1\). At every good split
rational prime, the C51 exponent \(2/n\) over the two \(K\)-places becomes
\(4/n\) on one rational local factor. In particular, the \(n=4\) half-power
is exactly one ordinary rank-255 rational local factor. This is a split-local
repair, not a global square root.

For \(n=4\), the order-24 dihedral Reynolds projector also descends. It gives
a rank-10 rational Chow summand of the middle cohomology and a complementary
rank-158 summand. The full rational packet decomposes by ranks
\(87+10+158=255\).

Every Frobenius formula uses geometric Frobenius, normalized by
\(F_p\mid\mathbf Q_\ell(-1)=p\).

## Proof firewall

Proved in C53:

- explicit semilinear and fixed-basis descent for the equations, for all
  \(n\ge2\);
- rational packet descent for certified smooth \(n=2,3,4\);
- descent of the order-24 Reynolds graph sum by restriction/corestriction;
- compatible projected Frobenius polynomials outside a finite bad set;
- split and inert local identities, including exact split-local clearing at
  \(n=4\).

Not claimed:

- smoothness or motive extraction for \(n\ge5\);
- an inert-prime or global square root;
- meromorphic continuation or a functional equation;
- automorphy, semisimplicity, or Chow indecomposability;
- an actual Calabi--Yau threefold realizing the rank-10 summand.

A conic-bundle/Prym realization is outside the C53 certificate. Any future
version requires an independent flatness theorem, discriminant analysis,
and source audit.

The default runner verifies the 20/20 semantic gates, 63/63 targeted tests,
both byte-identical Route-A records, and the full-project release manifest.
