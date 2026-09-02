# Narrative report

Newton–Schulz is often introduced through a norm bound. The exact dynamics are cleaner: the left residual squares at every iteration. Powers of a finite matrix vanish exactly when its spectral radius is below one, so the true square basin is spectral, not norm-dependent. Jordan blocks then expose the missing nonnormal factor: at dyadic power `N=2^k`, the largest peripheral block contributes `N^(s-1)rho^N`.

Singular matrices add a real obstruction. Residual behavior on `Ran(A)` is insufficient unless the initial inverse estimate has exactly the Moore–Penrose row and column supports. In SVD coordinates, the unsupported blocks obey multiplicative recurrences whose factors converge through an invertible infinite product, or an explicit doubling recurrence. Therefore they cannot disappear accidentally inside the compressed residual basin. This yields an iff theorem rather than a sufficient construction.

For `X_0=alpha A*`, every nonzero singular direction becomes scalar. The sharp open corridor is `0<alpha<2/sigma_max^2`. At equality, all maximal singular directions are permanently deleted while smaller directions may still converge; this is spectral truncation, not pseudoinverse convergence. At alpha zero the iteration is fixed at zero, and outside or for negative alpha a maximal direction diverges. If `A=0`, the canonical start is zero for every alpha and the full convergence basin consists only of `X_0=0`.

At spectral radius one, semisimple peripheral residuals are bounded and nonvanishing; the residual sequence itself may or may not converge, so no stronger label is used. The results are exact-arithmetic theorems, not floating-point stability guarantees.
