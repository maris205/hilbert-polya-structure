# Methodology blueprint

The proof is local-to-global and sign-locked to the relative P72 object.

- Start from `log C_rel=H_rel-sum_(m>=2)c_m Phi(t^m)`.
- Put the multiplier sign in the definition
  `log W=sum_(m>=2)d_m Phi(t^m)+G`; cancellation must therefore give
  `d_m=c_m`, not `-c_m`.
- Use the fact that the `2m` poles of channel `m` lie on the unique radius
  `rho_m=2^(-1/(2m))`; no other channel contributes a pole there.
- Separate coefficient rigidity from holomorphic gauge freedom.
- At `w=1+sqrt(2)t`, use the exact identity
  `H_rel=3/(4w)-(1/2)log w-3/2`.
- Construct primary factors pole by pole.  The weighted root-of-unity filter
  determines exactly what their compensating Taylor polynomials retain.
- Treat finite computations only as sign, coefficient, schema, dependency,
  and mutation certificates.  Infinite normal convergence and uniqueness
  are proved analytically.
