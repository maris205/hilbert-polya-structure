# Methodology blueprint

## Frozen object

- System: \(H_6(q,p)=(1-6q^2-p,q)\).
- Orbit: the exact primitive period-four source used in HCS-P49--P51.
- Multiplier: \(L=289+24\sqrt{145}\), satisfying \(L+L^{-1}=578\).
- Packet index: \(n\ge3\).
- Packet mass: \(b_n=\log\beta_n=\|D_n\|_{\rm tag}\).
- Boundary coordinate: \(u=e^{-\tau}\uparrow1\), \(\tau\downarrow0\).

## Mathematical route

1. Expand \(\Phi_n(L)\) by Möbius inversion.
2. Prove the uniform formula
   \(b_n=\frac12\varphi(n)\log L+\varepsilon_n\),
   with \(|\varepsilon_n|\le C_L<\infty\).
3. Derive \(\sum_{n\le x}\varphi(n)=3x^2/\pi^2+O(x\log x)\)
   directly from \(\varphi(n)=n\sum_{d\mid n}\mu(d)/d\).
4. Apply summation by parts to obtain the Abel asymptotic.
5. Normalize packet mass to a probability measure on the blown-up index
   \(\tau n\) and identify its Laplace transform.
6. Use disjoint source tags to test convergence in the original weighted
   \(\ell^1\) divisor space.

## Computational route

- Producer: exact reciprocal trace polynomials and high-precision Abel rows.
- Independent checker: separate totient/Möbius implementation, dependency
  rehashing and claim-boundary checks.
- Controls: half-normalization, \(\tau^2\) scaling, Gamma shape, fixed-prefix
  escape, vector-limit promotion and open all-orbit claims.

## Evidence labels

- Exact algebra and asymptotic proofs: `PROVED`.
- Finite convergence tables: `NUMERICALLY_CERTIFIED` for the recorded rows,
  but only illustrative of the separately proved limits.
- Original tagged boundary limit: `REFUTED_NO_CONVERGENT_SUBNET`.
- All-orbit boundary interchange: `OPEN`.
