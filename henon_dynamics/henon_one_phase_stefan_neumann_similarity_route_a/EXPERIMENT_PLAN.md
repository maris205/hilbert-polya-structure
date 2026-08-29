# Exact-computation plan

1. Freeze the dimensionless one-phase problem
   `u_t=u_xx`, `u(0,t)=1`, `u(s,t)=0`, `beta*s'=-u_x(s^-)`, `s(0)=0`.
2. Derive the Neumann ansatz `s=2 lambda sqrt(t)` and certify the scalar
   equation `sqrt(pi)*lambda*exp(lambda^2)*erf(lambda)=Ste=1/beta`.
3. Prove strict monotonicity and endpoint limits of the root function. Check
   the five-term small-Stefan inverse series and the two-sided large-Stefan
   Lambert-W enclosure using the elementary erfc bound.
4. Serialize eight exact rational Stefan probes, wall/interface flux
   coefficients, sensible/latent/input energy coefficients, and three labelled
   singular boundaries (zero superheat, zero latent heat, zero diffusivity).
5. Recompute every row in an independent checker, verify PDE/boundary/energy
   identities in SymPy, replay canonical bytes in a clean process, and run
   repaired-hash/stale-hash/nested-key mutation attacks.
6. Compile three substantive LuaLaTeX revisions at
   `SOURCE_DATE_EPOCH=1787875200`; remove sidecars and close the self-excluded
   27-payload manifest only after two settled round-2 builds.

The certificate is source-local and does not use target arithmetic data.
