# C315 proof package: positive-root-pencil goldfish scattering

## Claim and status

Fix a finite `N>=2`, ordered real numbers `x_1<...<x_N`, and `v_i>0`.
Define

\[
P(z)=\prod_{i=1}^N(z-x_i),\qquad
Q(z)=\sum_{i=1}^Nv_i\prod_{j\ne i}(z-x_j),\qquad
p(z,t)=P(z)-tQ(z).
\]

Let `y_1<...<y_{N-1}` be the roots of `Q`, put

\[
V=\sum_i v_i,\qquad M=\sum_i v_i x_i,\qquad c=M/V,
\qquad \beta_i=-P(y_i)/Q'(y_i).
\]

Then `x_i<y_i<x_{i+1}` and `beta_i>0`.  For every real `t`, `p` has
simple real roots `z_1(t)<...<z_N(t)`.  At positive time,

\[
x_i<z_i(t)<y_i\ (i<N),\qquad x_N<z_N(t),
\]

whereas at negative time,

\[
z_1(t)<x_1,\qquad y_i<z_{i+1}(t)<x_{i+1}\ (i<N).
\]

All velocities are positive, their sum is `V`, and the roots solve

\[
\ddot z_i=2\sum_{j\ne i}\frac{\dot z_i\dot z_j}{z_i-z_j}
\]

globally without collision.  With `B=sum_i beta_i`, the complete first
asymptotic layer is

\[
\begin{array}{ll}
t\to-\infty:&z_1=Vt+c+B/t+O(t^{-2}),\quad
z_{i+1}=y_i-\beta_i/t+O(t^{-2}),\\
t\to+\infty:&z_i=y_i-\beta_i/t+O(t^{-2}),\quad
z_N=Vt+c+B/t+O(t^{-2}).
\end{array}
\]

Consequently the incoming velocity vector tends to `(V,0,...,0)` and the
outgoing vector to `(0,...,0,V)` in rank order.

Status: `PROVABLE AS STATED`.  The statement is the positive real cone of a
classical source model, not a priority claim.

## Proof

Partial fractions give

\[
R(z):=\frac{Q(z)}{P(z)}=\sum_{i=1}^N\frac{v_i}{z-x_i},
\qquad R'(z)=-\sum_{i=1}^N\frac{v_i}{(z-x_i)^2}<0.
\]

Thus `R` crosses zero exactly once in every gap `(x_i,x_{i+1})`, which
proves the strict interlacing of the `y_i`.  For `t!=0`, a root of `p` is
equivalent to `R(z)=1/t`.  Monotonicity and the one-sided pole limits put
one root in `(x_i,y_i)` and one in `(x_N,infinity)` when `t>0`; for `t<0`
they put one in `(-infinity,x_1)` and one in `(y_i,x_{i+1})`.  These roots
are simple.  At `t=0` they are the simple roots `x_i` of `P`, so the ordered
solution is complete for all real time.

Differentiating `R(z_i(t))=1/t` gives

\[
\dot z_i=-\frac{1}{t^2R'(z_i)}>0\qquad(t\ne0),
\]

and at time zero implicit differentiation gives
`dot z_i(0)=Q(x_i)/P'(x_i)=v_i`.  The coefficient of `z^{N-1}` in `p`
gives the exact Vieta law

\[
\sum_i z_i(t)=\sum_i x_i+Vt,
\]

hence `sum_i dot z_i=V`.  Moreover

\[
Q(z)=\sum_i\dot z_i(t)\prod_{j\ne i}(z-z_j(t))
\]

is independent of time.  Twice differentiating
`p(z_i(t),t)=0`, and using

\[
\frac{p_{zz}(z_i,t)}{p_z(z_i,t)}
=2\sum_{j\ne i}\frac1{z_i-z_j},\qquad
\frac{Q'(z_i)}{p_z(z_i,t)}
=\sum_{j\ne i}\frac{\dot z_i+\dot z_j}{z_i-z_j},
\]

gives the displayed goldfish equation.  Also
`p(z,t+s)=p(z,t)-sQ(z)`, so the polynomial construction has the exact flow
group law rather than merely a local parametrization.

At each simple root `y_i` of `Q`, the implicit function theorem in `1/t`
gives

\[
z=y_i+\frac{P(y_i)}{tQ'(y_i)}+O(t^{-2})
=y_i-\frac{\beta_i}{t}+O(t^{-2}).
\]

The alternating signs of `P(y_i)` and `Q'(y_i)` are opposite, so
`beta_i>0`.  Since `Q=V product_i(z-y_i)`, coefficient comparison gives
`sum_i y_i=sum_i x_i-c`.  Subtracting all finite-root expansions from the
exact Vieta sum produces `Vt+c+B/t+O(t^-2)` for the exterior root.  The
interlacing identifies which ordered rank is exterior at each end, and
differentiation of these analytic expansions proves the velocity limits.

## Boundary and Route-A stop

For `N=1` the system is a free particle.  Strict positivity is sharp:
`x=(0,1), v=(1,0)` gives `p=(z-1)(z-t)` and a collision at `t=1`; mixed
signs `v=(1,-1)` give `p=z^2-z+t`, a double root at `t=1/4` and complex
roots afterwards.  Coincident initial positions lie on the singular
Newtonian boundary.  All-negative velocities follow by time reversal but
are not merged into the positive-cone statement.

There is no prime carrier, periodic-orbit ledger, target determinant, Weil
compression, or canonical self-adjoint lift.  The strict tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, Route A is rejected,
and Route B remains false under `NO_BAD_EULER_OR_ROOT_NUMBER`.
