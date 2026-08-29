# Theorem package

Fix \(\omega>0\), \(c\ge0\), and write
\[
 \dot x=v,\qquad \dot v=-\omega^2x-c\xi,
 \qquad \xi\in\operatorname{Sign}(v),
\]
where \(\operatorname{Sign}(v)=\{1\}\) for \(v>0\), \(\{-1\}\) for
\(v<0\), and \([-1,1]\) for \(v=0\).  Put
\(a_f=c/\omega^2\).  The frozen viability law selects \(v=0\) (sticking)
when \(|x|\le a_f\); for \(x>a_f\) it releases with negative acceleration,
and for \(x<-a_f\) with positive acceleration.

## Theorem 1 — well-posedness and energy

The maximal-monotone graph plus the stated viability selection gives one
global forward absolutely continuous trajectory for every initial
\((x_0,v_0)\).  Backward uniqueness is not asserted after trajectories have
entered the sticking set.
On a slip interval,
\[
 E=\tfrac12(v^2+\omega^2x^2),\qquad \dot E=-c|v|, \tag{1}
\]
and on a sticking interval \(\dot E=0\).  At the thresholds the selected
state sticks, so no artificial chattering branch is introduced.

## Theorem 2 — rest map and finite capture

Assume \(c>0\).  For a positive rest \(x(0)=A>a_f,v(0)=0\), the first slip has sign \(v<0\),
center \(+a_f\), and
\[
 x(t)=a_f+(A-a_f)\cos(\omega t),\qquad
 x_1=x(\pi/\omega)=2a_f-A. \tag{2}
\]
If \(A_k\) denotes the signed turning point after the \(k\)-th complete
moving half-cycle, then
\[
 A_k=(-1)^k(A-2ka_f),\qquad
 |A_{k+1}|=|A_k|-2a_f
\]
until the static interval is reached.  The exact number of moving half-cycles
is
\[
 n=\left\lceil\frac{A-a_f}{2a_f}\right\rceil,\qquad A>a_f, \tag{3}
\]
and the stopping turn is \(A_n\), whose absolute value is at most \(a_f\).
For \(0\le A\le a_f\), the initial state already sticks.  Negative rests are
the odd reflection of this formula.

## Theorem 3 — arbitrary signed initial velocity

Suppose \(c>0\) and \(v_0>0\).  The first slip branch has center \(-a_f\),
radius
\[
 R=\sqrt{(x_0+a_f)^2+(v_0/\omega)^2},
\]
phase \(\theta_0=\operatorname{atan2}(-v_0/\omega,x_0+a_f)\in(-\pi,0)\),
first-turn time \(\tau_0=-\theta_0/\omega\), and next turn
\(X_1=-a_f+R\).  If \(|X_1|>a_f\), the remaining complete half-cycles have
integer count
\[
 r=\left\lceil\frac{|X_1|-a_f}{2a_f}\right\rceil,
\]
and the stopping time is \(\tau_0+r\pi/\omega\).  If \(|X_1|\le a_f\),
the first partial arc already ends in the static set and \(r=0\).

For \(v_0<0\), the center is \(+a_f\),
\[
 R=\sqrt{(x_0-a_f)^2+(v_0/\omega)^2},\quad
 \theta_0=\operatorname{atan2}(-v_0/\omega,x_0-a_f)\in(0,\pi),
\]
the first-turn time is \((\pi-\theta_0)/\omega\), and the next turn is
\(X_1=a_f-R\).  The same ceiling rule gives the finite capture.  The initial
segment in either case is a partial slip arc; only the `r` later segments are
complete half-cycles.

For an exterior rest, the positive side has center \(+a_f\), phase zero, and
first-turn time \(\pi/\omega\); the negative side has center \(-a_f\), phase
\(\pi\), and the same time.  This fixes the phase convention at \(v_0=0\).

## Theorem 4 — harmonic face and Route-A boundary

If \(c=0\),
\[
 x(t)=x_0\cos(\omega t)+(v_0/\omega)\sin(\omega t),\qquad
 v(t)=v_0\cos(\omega t)-\omega x_0\sin(\omega t),
\]
and \(E\) is constant; there is no finite frictional capture.  The mechanical
flow has no intrinsic arithmetic labels, primitive repetition law, target
determinant, or Hilbert–Pólya operator.  The strict tuple is
\[
(\mathtt{A0\_FAIL},\mathtt{A1\_FAIL},\mathtt{A2\_FAIL},
 \mathtt{A3\_FAIL},\mathtt{A4\_FORMAL\_HINT}),
\]
with `ROUTE_A_REJECTED` and Route B disabled.
