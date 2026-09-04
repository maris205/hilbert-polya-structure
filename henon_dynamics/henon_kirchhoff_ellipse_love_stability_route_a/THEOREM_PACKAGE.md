# Theorem package

Let `E_0={x^2/a^2+y^2/b^2<1}`, where `a>=b>0`, and let the vorticity be the
real constant `omega` on `E_0` and zero outside.  Put

```text
gamma=a/b,  delta=(a-b)/(a+b),
kappa=2ab/(a+b)^2=(1-delta^2)/2.
```

## Main theorem

1. The Euler patch is an exact relative equilibrium.  Its shape is
   `E_t=R_{Omega t}E_0`, with
   `Omega=omega*ab/(a+b)^2`.  Inside the patch,
   `u=(-omega*a*y/(a+b), omega*b*x/(a+b))`.
2. Resolve the perturbation in elliptic coordinates co-rotating with the
   unperturbed ellipse: the Fourier label is measured relative to its
   instantaneous principal axes, and `lambda_m` is the co-rotating-frame
   frequency under the convention `exp(-i lambda_m t)`.  The Love mode
   satisfies

   ```text
   lambda_m^2 = omega^2/4 *
     ([2mab/(a+b)^2-1]^2 - [(a-b)/(a+b)]^(2m)).
   ```

3. `lambda_1^2=Omega^2`, and `lambda_2^2=0` for the entire ellipse family.
4. For every `m>=3`, define

   ```text
   F_m(delta)=m(1-delta^2)/2-1-delta^m,
   G_m(delta)=m(1-delta^2)/2-1+delta^m.
   ```

   There is exactly one `delta_m in (0,1)` with `F_m(delta_m)=0`, and
   `G_m>0` on `[0,1)`.  For nonzero vorticity, mode `m` is oscillatory for
   `delta<delta_m`, critical at equality, and exponentially split above it.
5. `delta_{m+1}>delta_m` and therefore
   `gamma_{m+1}>gamma_m`, where
   `gamma_m=(1+delta_m)/(1-delta_m)`.
6. `delta_3=1/2` and `gamma_3=3`.  Hence every `m>=3` is oscillatory for
   `1<=gamma<3`; at 3 only `m=3` reaches its wall; above 3 that mode is
   exponentially split.
7. Put `c*=1+W(exp(-1))`.  Then

   ```text
   m(1-delta_m) -> c*,       gamma_m/m -> 2/c*.
   ```

   Numerically, `c*` is about 1.27846 and `2/c*` about 1.56438; the theorem
   is the exact implicit statement.

## Proof

The displayed interior velocity has zero divergence and curl `omega`.
At `(a cos theta,b sin theta)`, its difference from
`Omega*(-y,x)` has zero dot product with the ellipse normal precisely for
`Omega=omega*ab/(a+b)^2`; tangential velocity only reparametrizes the
boundary.  The classical matched exterior streamfunction completes the
Euler patch solution.

The Love square factorizes, without dividing by the possibly zero vorticity,
as

```text
4 lambda_m^2 = omega^2 F_m(delta) G_m(delta).
```

Direct substitution proves the `m=1` and `m=2` identities.  For `m>=3`,
`F_m(0)=m/2-1>0`, `F_m(1)=-2`, and
`F_m'=-m delta-m delta^(m-1)<0` in `(0,1)`, so its root is unique.  Also

```text
G_m'=m delta(delta^(m-2)-1)<0,   G_m(1)=0,
```

so `G_m(delta)>0` before the strip limit.  The ordering follows from

```text
F_{m+1}-F_m=(1-delta^2)/2+delta^m(1-delta)>0.
```

At the root of `F_m`, mode `m+1` is therefore still on its positive side.
For `m=3`,

```text
16 lambda_3^2=omega^2(1-delta^2)^2(1-4delta^2),
```

which gives the first wall.

For the asymptotic, set `c_m=m(1-delta_m)`.  Its equation becomes

```text
c_m-c_m^2/(2m)=1+(1-c_m/m)^m.
```

Evaluating its two sides at `c=1` and `c=2` gives `1<c_m<2`.  Every
subsequential limit therefore obeys `c=1+exp(-c)`, whose unique solution is
`1+W(exp(-1))`.  Finally
`gamma_m/m=(2-c_m/m)/c_m`, proving the limit.

## Boundaries and route

For a noncircular, nonstationary patch, the vorticity field has minimal
period `pi/|Omega|`; an oriented-axis lift has period `2pi/|Omega|`.  At
`a=b` the Rankine patch shape is stationary and orientation is unobservable.
At `omega=0` every frequency and the rotation rate vanish.  Swapping axes
restores `gamma>=1` without changing the modal square.  The limit
`delta->1` is a singular strip boundary, not a bounded ellipse.

These are spectral linear statements only.  The tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route A is rejected.
