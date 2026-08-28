# HCS-C214 theorem package: Brownian resetting and first passage

## Frozen object and two realizations

Let `D,r,a>0`.  In the **free realization**, `X_t` evolves on `R` by

```text
dX_t = sqrt(2D) dW_t,
```

and, independently, a Poisson clock of rate `r` resets `X_t` to `0`.  Its
transition density from `0` is denoted `p_r(x,t|0)`.  In the **killed-search
realization**, the same process is started at `0` and stopped at

```text
T_a = inf{t>=0 : X_t = a};
```

The killed law is sub-Markov after `T_a`; it is not assigned the free process's
stationary density.  The generator before killing is

```text
L f(x) = D f''(x) + r(f(0)-f(x)).
```

The clock is physical time and the reset point is fixed, not fitted.

## Main theorem

For every `D,r,a>0`:

1. **Free renewal propagator.**  With

   ```text
   G_D(x,t)=(4*pi*D*t)^(-1/2) exp(-x^2/(4*D*t)),
   ```

   ```text
   p_r(x,t|0)=exp(-r*t)G_D(x,t)
                  + r integral_0^t exp(-r*u)G_D(x,u)du.
   ```

   For `x != 0` the integral is

   ```text
   [ exp(-|x|sqrt(r/D)) erfc(|x|/(2sqrt(Dt))-sqrt(rt))
    -exp( |x|sqrt(r/D)) erfc(|x|/(2sqrt(Dt))+sqrt(rt)) ]/(4sqrt(D*r)),
   ```

   with its continuous `x=0` branch `erf(sqrt(rt))/(2sqrt(D*r))`.

2. **Free stationary law.**  The free, unkilled process has the unique
   invariant density

   ```text
   p_st(x)=sqrt(r/D) exp(-|x|sqrt(r/D))/2,
   ```

   and its integral over `R` is one.  This statement is not transferred to the
   killed-search realization.

3. **Killed-search transforms.**  The no-reset first-passage transform from
   `0` to `a` is `f_0(q)=exp(-a sqrt(q/D))`.  Renewal over the first reset gives

   ```text
   F_r(s)=E[exp(-s T_a)]
        = ((s+r) exp(-a sqrt((s+r)/D)))
          /(s+r exp(-a sqrt((s+r)/D))),
   ```

   and

   ```text
   S_r(s)=integral_0^infinity exp(-s*t) P(T_a>t)dt
        = (1-exp(-a sqrt((s+r)/D)))
          /(s+r exp(-a sqrt((s+r)/D))).
   ```

   For `s>0`, `1-F_r(s)=s S_r(s)`; at `s=0`, `S_r(0)=E[T_a]`.

4. **MFPT and all moments.**

   ```text
   E[T_a] = -F_r'(0) = S_r(0)
          = (exp(a sqrt(r/D))-1)/r.
   ```

   All moments are finite for `D,r,a>0`, and

   ```text
   (-1)^n F_r^(n)(0) = E[T_a^n]                 (n>=0),
   (-1)^n S_r^(n)(0) = E[T_a^(n+1)]/(n+1)       (n>=0).
   ```

5. **Unique optimum.**  Put `z=a sqrt(r/D)`.  Then

   ```text
   (D/a^2) E[T_a] = (exp(z)-1)/z^2.
   ```

   Its limits at `z=0+` and `z=infinity` are infinite.  There is exactly one
   positive minimizer, the root

   ```text
   z*=2(1-exp(-z*)),  z*=1.5936242600400400923...,
   r*=D(z*/a)^2.
   ```

6. **Boundaries.**  At `r=0` ordinary Brownian motion has no normalizable
   stationary density and infinite mean hitting time on the half-line.  At
   `a=0`, `T_a=0`.  At `D=0`, a path reset to `0` cannot reach a positive target,
   so the hitting time is infinite.  These are limits/boundaries, not points
   in the positive-parameter denominator theorem.

## Proof and evidence boundary

The propagator follows by conditioning on the last reset.  The erfc expression
is the elementary integral of the heat kernel against `exp(-ru)`.  The free
stationary density follows from the renewal limit and is normalized directly.
For the killed process, conditioning on whether the first reset occurs before
the no-reset hit gives `F_r=f_0(s+r)/(1-r(1-f_0(s+r))/(s+r))`, which reduces to
the displayed fraction.  The survival identity is integration by parts.  The
moment formulas are the standard Laplace derivative identities and the
survival integration-by-parts formula, with the powers, signs, and `n>=0`
indexing shown explicitly; exponential resetting gives finiteness of every
moment in the positive-parameter regime.  Differentiating the dimensionless MFPT yields a positive-factor
multiple of `z-2(1-exp(-z))`; monotonicity of its derivative away from zero
gives the unique positive root.

The producer records a fixed rational grid.  The checker uses independent
high-precision quadrature for the renewal integral and normalization, while
the SymPy script checks the heat equation, renewal algebra, transform limits,
optimality derivative, and moment derivative relation.  These finite checks do
not replace the all-parameter proof.

## Scope and route verdict

The process is a non-arithmetic stochastic control.  It has no intrinsic
rational-prime carrier, primitive periodic-orbit owner, or arithmetic divisor.
The Laplace denominator is explicitly **not** a dynamical zeta.  No target
prime/zero table, Euler factor, root number, automorphy assertion, target
divisor, functional equation, or Hilbert–Pólya operator is used.

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
overall = ROUTE_A_REJECTED; route_b_invocation_allowed = false.
```

## References (attribution only)

* M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*,
  Physical Review Letters 106, 160601 (2011), DOI
  `10.1103/PhysRevLett.106.160601`.
* M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, Journal
  of Physics A: Mathematical and Theoretical 44, 435001 (2011), DOI
  `10.1088/1751-8113/44/43/435001`.
* M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic resetting and
  applications*, Journal of Physics A 53, 193001 (2020), DOI
  `10.1088/1751-8121/ab7cfe`.
