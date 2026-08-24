# Exact results — HCS-C126

## All-period laws

- \(f^n=T_{3^n}\) for all \(n\ge1\).
- \(T_{3^n}(x)-x\) has \(3^n\) distinct real roots.
- every root has a unique closing fiber coordinate;
- \(\#\operatorname{Fix}(F^n)=3^n\);
- \(E_n=\sum_{d\mid n}\mu(d)3^{n/d}\) and \(P_n=E_n/n\);
- \(\zeta_F(z)=1/(1-3z)\).

The primitive counts for \(n=1,\ldots,12\) are

```text
3, 3, 8, 18, 48, 116, 312, 810, 2184, 5880, 16104, 44220.
```

## Stability laws

For \(m=3^n\), the fixed-point unstable multipliers are:

- \(m^2\) at the two endpoints;
- \(+m\) at \((m-3)/2\) interior points;
- \(-m\) at \((m-1)/2\) interior points.

The stable multiplier is \(4^{-n}\), so every fixed point is a saddle and

\[
\det(I-DF^n)=(1-T_m'(x))(1-4^{-n})\ne0.
\]

For a primitive orbit with period \(p\), multiplier \(\alpha\), and repetition
\(r\), the repeated multipliers are \(\alpha^r,4^{-pr}\); the orientation is
\(\operatorname{sgn}(\alpha)^r\).

## Exact controls

- fiber multiplier one: a whole fixed line at \(x=0\), and no fiber closure
  above \(x=\pm1\);
- base \(4x^3-2x\):
  \(g^2-x=x(2x-1)^3(2x+1)^3(4x^2-3)\), only five distinct roots, with the
  neutral two-cycle \(\{\pm1/2\}\).

Evidence SHA-256 is recorded by the release manifest after final closure.
