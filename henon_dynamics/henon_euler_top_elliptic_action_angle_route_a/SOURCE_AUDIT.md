# C186 source audit

## Frozen primary sources

1. E. Celledoni, F. Fassò, N. Säfström, and A. Zanna, “The Exact Computation of the Free Rigid Body Motion and Its Use in Splitting Methods,” *SIAM Journal on Scientific Computing* **30** (2008), 2084--2112, DOI [10.1137/070704393](https://doi.org/10.1137/070704393). Role: modern primary account of exact free-rigid-body motion using Jacobi elliptic functions and integrals.
2. E. G. Pina, “Drawing the Free Rigid Body Dynamics According to Jacobi,” [arXiv:1505.06186](https://arxiv.org/abs/1505.06186). Role: explicit body-angular-momentum Jacobi coordinates and the common \(4K(k)\) real period convention.

The Euler equations, Jacobi solution, stability portrait, and action--angle integrability are classical. C186 claims no priority for them. The package contribution is a source-locked all-energy synthesis, exact consequence ledger, executable convention audit, and Route-A stopping certificate.

## Convention lock

Set \(a=I_1^{-1}>b=I_2^{-1}>c=I_3^{-1}\), \(G^2=|M|^2>0\), and \(e=2E/G^2\). The reduced equation is
\[
\dot M=M\times I^{-1}M,
\]
so \(c\le e\le a\). Jacobi's \(K(k)\) uses modulus \(k\), while the code passes the parameter \(m=k^2\) to `mpmath.ellipk`. The common vector period is \(4K(k)/\Omega\), not the \(2K\) period of `dn` alone.

## Evidence and citation boundary

- The cited sources justify the classical owner and elliptic representation.
- `THEOREM_PACKAGE.md` derives the exact amplitudes, moduli, frequencies, singular limit, action quadratures, and time-map fixed-set consequences in the frozen convention.
- The 180 rational sentinels and high-precision quadratures test signs and normalizations. They do not prove the all-parameter theorem.
- No external review, literature novelty certification, target comparison, or acceptance claim is made.
