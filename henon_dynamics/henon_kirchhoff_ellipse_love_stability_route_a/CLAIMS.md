# Claims

1. A constant-vorticity ellipse is an exact planar Euler relative
   equilibrium with shape rotation rate `Omega=omega*a*b/(a+b)^2`.
2. The stated Love formula is the exact spectral characteristic equation
   for each Fourier boundary mode relative to the instantaneous ellipse axes;
   `lambda_m` is the frequency in the co-rotating frame under the declared
   time convention.
3. `lambda_1^2=Omega^2`; `lambda_2^2=0` is the tangent mode along the exact
   ellipse family.
4. For each `m>=3`, there is a unique critical eccentricity parameter
   `delta_m` and aspect `gamma_m`; the mode is oscillatory below its wall and
   exponentially growing above it when `omega` is nonzero.
5. The thresholds strictly increase with `m`.  The first is exactly
   `delta_3=1/2`, equivalently `gamma_3=3`.
6. If `c*=1+W(exp(-1))`, then
   `m(1-delta_m)->c*` and `gamma_m/m->2/c*`.
7. The boundary and period conventions in `THEOREM_PACKAGE.md` are exact.

Every stability claim is spectral and linear.  No nonlinear orbital,
Lyapunov, or finite-amplitude stability theorem is claimed.
