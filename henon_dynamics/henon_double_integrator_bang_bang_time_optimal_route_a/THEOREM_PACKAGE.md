# Theorem package

Let

\[
 \dot x=v,\qquad \dot v=u,\qquad |u|\le a,
\]

where `a>0`, and let `T_a(x,v)` be the least physical time needed to reach
`(0,0)`.  Define

\[
 F_a(x,v)=x+\frac{v|v|}{2a}.
\]

## Main theorem (global minimum-time synthesis)

At the origin, `T_a=0`.  If `F_a=0` and `v` is nonzero, direct braking
`u=-a sign(v)` reaches the origin in `T_a=|v|/a`.

If `F_a` is nonzero, put `s=sign(F_a)` and

\[
 D=\frac{v^2}{2a^2}+\frac{s x}{a}>0.
\]

Then

\[
 t_1=\frac{s v}{a}+\sqrt D,\qquad t_2=\sqrt D,
 \qquad T_a=\frac{s v}{a}+2\sqrt D .
\]

Both durations are nonnegative.  The unique extremal control up to null sets
is

\[
 u(t)=-sa\quad(0\le t<t_1),\qquad
 u(t)=sa\quad(t_1\le t\le T_a).
\]

Its switch state is

\[
 (x_1,v_1)=\left(\frac{saD}{2},-sa\sqrt D\right),
\]

which lies on `F_a=0`, and the second arc terminates exactly at `(0,0)`.

## Global lower-bound proof

Any admissible transfer in time `T` satisfies, after integrating twice,

\[
 \int_0^T u(t)\,dt=-v,\qquad
 \int_0^T t\,u(t)\,dt=x.
\]

Among functions with `|u|<=a` and the displayed mean, the bathtub/rearrangement
principle places `+a` as late as possible to maximize the first moment and as
early as possible to minimize it.  Therefore every reachable endpoint obeys

\[
 -\frac{aT^2}{4}-\frac{vT}{2}+\frac{v^2}{4a}
 \le x\le
 \frac{aT^2}{4}-\frac{vT}{2}-\frac{v^2}{4a}.
\]

Equality holds only for the corresponding one-switch bang--bang control,
apart from null sets.  On `F_a>0`, solving the right equality gives the stated
`s=1` time; on `F_a<0`, solving the left equality gives the `s=-1` time.
Thus no shorter admissible transfer exists, and the constructed transfer is
globally optimal.  This sufficiency argument does not rely only on a
necessary maximum principle.

## HJB, Pontryagin and boundaries

Off the switching curve,

\[
 T_x=\frac{s}{a\sqrt D},\qquad
 T_v=\frac{s}{a}+\frac{v}{a^2\sqrt D},\qquad
 \operatorname{sign}(T_v)=s,
\]

so `1+v T_x-a|T_v|=0`.  The continuous value is the viscosity solution of
the minimum-time HJB equation globally.  Pontryagin's costate for `v` is
affine in time, so a normal extremal has at most one switch, agreeing with the
sharp reachable-set construction.

Reflection and parabolic scaling give

\[
 T_a(-x,-v)=T_a(x,v),\qquad
 T_a(\lambda^2x,\lambda v)=\lambda T_a(x,v),\quad \lambda>0.
\]

At `a=0`, only the origin has finite rest-to-rest time; every other state has
infinite value.  The two off-curve formulas meet the direct-braking value
continuously at `F_a=0`, although the value is not classically smooth there.
