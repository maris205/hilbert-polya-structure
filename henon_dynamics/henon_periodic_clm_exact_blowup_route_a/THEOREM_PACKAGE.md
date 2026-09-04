# Theorem package

Let `μ=<ω_0>`, `f=ω-μ`, `h=Hf`, and `z=h+if`, under `H(e^{ikx})=-i sign(k)e^{ikx}`. The periodic Tricomi identity is

`H(fHf)=((Hf)^2-f^2)/2`.

It implies the pointwise Riccati equation `z_t=iμz+z²/2`.

This reduction is two-way, not only PDE-to-ODE: `z_0` belongs to the strictly negative-frequency Hardy subspace, which is invariant under the locally Lipschitz vector field `iμz+z²/2`. Hence the explicit pointwise flow preserves `h=Hf` and `<f>=0`. Equivalently, the constraint defect `g=h-Hf` solves `g_t=(Hf)g+g²/2-μHg-H(fg)` and uniqueness forces `g=0`. A positive denominator lower bound on a compact time interval preserves smoothness and supplies continuation.

## Main theorem

1. The mean is conserved. For `μ=0`, `z=2z_0/(2-tz_0)` and
   `ω=4ω_0/[(2-th_0)^2+t²ω_0²]`.
2. For `μ≠0`,
   `z=e^{iμt}z_0/[1-(e^{iμt}-1)z_0/(2iμ)]` and
   `ω=4μ²ω_0/|2iμ-(e^{iμt}-1)z_0|²`.
3. With `a=|μ|`, nonzero-mean data break down forward exactly when `ω_0` has a zero. The first time is
   `min_{ω_0(x)=0} (2/a) arccot(h_0(x)/a)`, where `arccot:R→(0,π)`. Zero-free data are global and have period `2π/a`.
4. At zero mean, the first time is `min 2/h_0(x)` over zeros with `h_0(x)>0`; if that set is empty, the solution is global forward.
5. For `ω_0=μ+A sin(kx)`, the nonzero-mean regimes are: global for `|μ|>|A|`; tangent first time `π/|μ|` at equality; crossing first time `(2/|μ|)arccot(sqrt(A²-μ²)/|μ|)` below equality. At zero mean, the time is `2/|A|`.
6. At a simple first zero, rescaling `x=x*+(T-t)y` gives the explicit rational profiles stated in the paper. If all first poles are simple, `||ω(t)||∞` is bounded above and below by constants times `(T-t)^{-1}`.
7. Tangent and higher-order zeros remain in the exact breakdown criterion but are excluded from the simple-pole rate.

Full derivations and all boundary conditions are in `paper/main.pdf`.
