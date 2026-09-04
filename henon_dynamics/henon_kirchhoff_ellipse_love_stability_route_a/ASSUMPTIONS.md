# Assumptions and conventions

- The fluid occupies the unbounded plane and solves inviscid,
  incompressible two-dimensional Euler.
- Vorticity equals the real constant `omega` inside a bounded ellipse and
  zero outside.  Semiaxes satisfy `a>=b>0`.
- Positive vorticity is counterclockwise.  Boundary Fourier labels are
  measured in elliptic coordinates whose axes co-rotate with the unperturbed
  ellipse, hence relative to its instantaneous principal axes.  The quantity
  `lambda_m` is the co-rotating-frame frequency under time dependence
  `exp(-i lambda_m t)`: positive `lambda_m^2` is oscillatory, while negative
  `lambda_m^2` gives an exponentially growing/decaying pair.
- `delta=(a-b)/(a+b)` and `gamma=a/b`.  The analysis uses `delta in [0,1)`.
- Stability refers only to the spectrum of the linearized contour equation
  within the Love mode decomposition.
- For a noncircular patch, the unmarked vorticity field has minimal period
  `pi/|Omega|`; an oriented-axis lift has period `2pi/|Omega|`.  A circle
  has no observable shape orientation, so neither is assigned to it.
- The quadratic vorticity moment is defined without a factor `1/2` as
  `int |x|^2 omega(x) dx`.
