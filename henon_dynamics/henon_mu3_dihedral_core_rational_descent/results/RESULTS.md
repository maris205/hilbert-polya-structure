# HCS-C53 exact-code results

The machine-readable certificate records the all-\(n\) algebraic-descent
theorem and its finite exact controls; it is not itself a substitute for the
mathematical proof.  The independent checker recomputes the fixed basis,
rational cubic and quadric for \(2\le n\le10\), and the closed formula

\[
\det B_n=(2\theta)^{n-1}\rho^{\lfloor(n-1)/2\rfloor}c_n,
\qquad c_n=1\ (n\text{ odd}),\quad c_n=1+\rho\ (n\text{ even}).
\]

For \(n=4\), the recorded theorem descends the nonconstant order-24 dihedral
group scheme and the middle Chow projectors, retaining the rank \(10+158\)
split.  The checker freezes the distinction among raw \(M_0\),
Calabi--Yau-type \(M_0(1)\), and source-normalized \(M_0(2)\), and verifies the
machine gates for the two-step argument from ell-independent rational
coefficients to integral raw local polynomials.

The principal Euler-factor gate is local and exact: at every good split prime,
the local `Log0` half-root of the two identical \(K\)-prime rank-255 factors is
one ordinary exponent-one \(\mathbf Q\)-local factor.  No inert-prime square
root, automorphy, global continuation, or functional equation is claimed.
The value \(-469\) at \(p=7\) has status
`PRE_C53_RECONNAISSANCE_REGRESSION_ANCHOR_UNCERTIFIED`.  It is retained only
as a frozen regression literal: the machine checks the displayed arithmetic,
but does not certify its provenance, does not perform an independent geometric
replay, and does not use it as theorem input in C53.

Status: full-project release freeze complete.  The machine passport is
`RELEASE_CANDIDATE`; the manifest inventories the frozen documentation,
manuscript and PDF, byte-identical root and archived Route-A records, code,
and results.  The default runner reconstructs both JSON artifacts in a
temporary directory, compares them byte-for-byte with the frozen copies, and
verifies the full-project manifest without modifying stable bytes.
