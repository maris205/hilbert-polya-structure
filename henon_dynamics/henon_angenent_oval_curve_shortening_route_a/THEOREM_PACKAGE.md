# C314 proof package: exact Angenent-oval geometry

## Claim and status

Let `t<0`, put `r=e^t`, and let

\[
\Gamma_t=\{(x,y)\in\mathbb R^2:\cos x=r\cosh y,\ |x|<\pi/2\}.
\]

This central component is a smooth embedded strictly convex compact ancient solution of
curve shortening with extinction at the origin at time zero.  Its complete
geometry is

\[
W=2\arccos r,\qquad H=2\operatorname{arcosh}(r^{-1}),
\]
\[
\kappa_{\min}=\frac r{\sqrt{1-r^2}},\qquad
\kappa_{\max}=\frac1{\sqrt{1-r^2}},\qquad A=-2\pi t,
\]
\[
L=4\sqrt{1-r^2}\,K\!\left(\sqrt{1-r^2}\right),
\]

where `K(k)` uses the elliptic **modulus** convention.  Its negative-time
leaves foliate `(-pi/2,pi/2) x R` minus the origin; adding the origin gives
the zero-time extinction leaf.  Parabolic extinction rescaling tends
smoothly to the unit circle, and the translated upper/lower tips tend
smoothly on compact sub-strips to opposite Grim-Reaper profiles.

Status: `PROVABLE AS STATED`.  “Complete” refers to this explicit family,
not to a new classification of all ancient solutions.

The unrestricted equation in `R^2` has the countable disjoint union
`union_{k in Z}(Gamma_t+(2*pi*k,0))`; it is not itself one compact curve.

## Proof

Set `F=cos x-r cosh y`.  The component in the strip is the two graphs

\[
y=\pm\operatorname{arcosh}(r^{-1}\cos x),qquad
|x|\le\arccos r.
\]

On `F=0`,

\[
|\nabla F|^2=\sin^2x+r^2\sinh^2y=1-r^2>0,
\qquad D^2F=-\cos x\,I.
\]

Thus the central level component is smooth.  With outward normal
`n_out=-grad(F)/|grad(F)|`, its positive curvature is

\[
\kappa=\frac{\cos x}{\sqrt{1-r^2}}>0.
\]

Differentiating `F=0` in time gives outward normal velocity
`V_out=-cos(x)/sqrt(1-r^2)=-kappa`; this is precisely inward
curve shortening.  Since `r<=cos x<=1`, the curvature extrema and their
locations follow, as do the displayed spans.

For the upper graph,

\[
\frac{dy}{dx}=-\frac{\sin x}{\sqrt{\cos^2x-r^2}},\qquad
ds=\frac{\sqrt{1-r^2}}{\sqrt{\cos^2x-r^2}}\,dx.
\]

Substitute `sin x=sqrt(1-r^2) sin phi`; both halves and both graphs give the
stated `4 sqrt(1-r^2) K(sqrt(1-r^2))`.  Direct differentiation of the area
integral has no endpoint term and yields

\[
A'(t)=-4\int_0^{\arccos r}
 \frac{\cos x}{\sqrt{\cos^2x-r^2}}\,dx=-2\pi.
\]

The area vanishes as `t` increases to zero, hence `A=-2*pi*t`.

On the open strip define

\[
T(x,y)=\log\cos x-\log\cosh y.
\]

It is nonpositive and vanishes only at the origin.  Therefore every other
strip point lies on exactly one negative level `T=t`.  Away from the origin,
direct differentiation gives

\[
-|\nabla T|\operatorname{div}
 \left(\frac{\nabla T}{|\nabla T|}\right)=1,
\]

which is the arrival-time form of the fixed normal-speed convention.

In tangent-angle coordinates, after a harmless angle shift,

\[
\kappa^2(\theta,t)=\frac1{1-e^{2t}}-\sin^2\theta.
\]

Multiplying by `-2t` makes this curvature converge with every angular
derivative to one as `t` increases to zero.  Axis symmetry fixes translation;
the fundamental theorem for strictly convex plane curves then gives smooth
convergence of `(-2t)^(-1/2) Gamma_t` to the unit circle.

Finally, on every compact subinterval of `(-pi/2,pi/2)`,

\[
\operatorname{arcosh}(e^{-t}\cos x)+t-\log2
=\log\cos x+O(e^{2t})
\]

with all spatial derivatives.  Subtracting the top height changes only the
vanishing `O(e^{2t})` constant.  This proves the upper Grim-Reaper limit;
reflection proves the lower limit.

## Boundary and Route-A stop

Time zero is a point, not a smooth timeslice; minus infinity is an
asymptotic regime, not a timeslice.  Euclidean similarities give equivalent
families.  No all-ancient-solution classification or stability theorem is
inferred.

There is no arithmetic origin, primitive periodic ledger, determinant, Weil
compression, or natural unitary lift.  The strict tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, Route A is rejected, and Route
B remains false under `NO_BAD_EULER_OR_ROOT_NUMBER`.
