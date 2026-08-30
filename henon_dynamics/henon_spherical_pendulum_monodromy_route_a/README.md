# HCS-C244 — spherical-pendulum monodromy (Route A)

This package freezes the unit spherical pendulum
\[
 H=\tfrac12(p_\theta^2+j^2/\sin^2\theta)+\cos\theta,\qquad J=j=p_\phi ,
\]
and gives one theorem-scale step: reduction with \(u=\cos\theta\) produces
the exact cubic \(P_{h,j}(u)=2(1-u^2)(h-u)-j^2\).  The certificate contains
the critical-value components, regular root chambers, period/angle/action
quadratures, and the focus-focus transport matrix
\(\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]\) in a declared
oriented basis.

The pole faces \(u=\pm1\) are audited in global embedding coordinates; no
singular local \((\theta,\phi)\) value is promoted to a theorem.  Quadratures
are endpoint-cancelled and high precision, but no claim is made that every one
has an elementary closed form.  The top focus-focus value is isolated from the
interior elliptic double-root branch.  This is source-local mechanics, not an
arithmetic or target-zeta construction.

Locked metadata: source baseline
5f357e2d2b78604f6c286bfbd05da922e1d6791f, evaluator SHA
6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c, fixed
epoch 1788048000, scope NO_BAD_EULER_OR_ROOT_NUMBER, date 2026-08-30.
Route tuple: (A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION);
overall ROUTE_A_REJECTED.

Run from this directory:

    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c244_pendulum_producer.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c244_pendulum_checker.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c244_pendulum_sympy_crosscheck.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c244_pendulum_replay.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c244_pendulum_mutation.py
    PYTHONDONTWRITEBYTECODE=1 python3 -B code/c244_release_manifest.py
