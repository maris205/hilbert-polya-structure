# P26 Round-3 conjugacy-owner theorem

Date: **2026-08-27**

Scope: the owner of the time-change period on `Y_0(11)`; no Hecke recurrence,
prime dictionary, or complete conjugacy-class enumeration is asserted.

## Theorem

Let

```text
f(z)=eta(z)^2 eta(11z)^2,
omega_f=2 pi i f(z) dz,
alpha_f=Re(omega_f).
```

For a hyperbolic element `M in Gamma_0(11)`, let `I(M)` denote the integral of
`alpha_f` over the oriented quotient loop obtained from an oriented axis
segment from `z` to `M z`. Then:

```text
I(C M C^(-1)) = I(M)       for C in Gamma_0(11),
I(M^(-1))     = -I(M),
I(M^r)        = r I(M)     for every integer r>=1.
```

Thus the first-variation coefficient

```text
d T_epsilon(M)/d epsilon at epsilon=0 = I(M)
```

is owned by an **oriented `Gamma_0(11)` conjugacy class**, with orientation
reversal and repetition retained as separate operations. Evidence token:
`[PROVED]`.

## Proof

The eta product is a weight-two cusp form for `Gamma_0(11)` with trivial
character. Therefore, for

```text
C=[[a,b],[c,d]] in Gamma_0(11),
f(C z)=(c z+d)^2 f(z),
d(C z)=dz/(c z+d)^2.
```

Consequently `C^* omega_f=omega_f`, and taking real parts gives
`C^* alpha_f=alpha_f`. If an axis segment `sigma` joins `z` to `M z`, then
`C sigma` joins `C z` to `(C M C^(-1)) C z`. Hence

```text
integral_(C sigma) alpha_f = integral_sigma C^* alpha_f
                           = integral_sigma alpha_f.
```

Reversing the oriented path negates an integral. A path for `M^r` is the
concatenation of `r` translates of a path for `M`; invariance of the descended
one-form makes all `r` integrals equal. This proves the three identities.

The proof is quotient-geometric and does not depend on the finite positive-word
cutoff used in Round 2 or Round 3.

## Executable regression check

The deterministic Round-3 ledger applies nine bounded conjugators in
`Gamma_0(11)` to each of the 11 Round-2 selected positive-word elements. It
checks determinant one, the `c=0 mod 11` condition, trace invariance, powers
`r=2,3`, and inverse orientation exactly over the integers:

```text
selected elements                 11
bounded conjugators                9
exact owner rows                  99
failed exact identities            0
```

For the four stable direct-evaluation conjugators `z -> z+k`,
`k=-2,-1,1,2`, a separate q-series/axis-quadrature check has 44 rows. The
largest observed binary64 residual is

```text
1.5543122344752192e-15.
```

This residual is a `[NUMERICAL_OBSERVATION]`, not a rigorous error bound. The
integer group checks are `NUMERICALLY_CERTIFIED` finite checks; neither is the
proof of the theorem.

## Claim boundary and next gate

The 11 positive-word elements remain a cutoff-bounded subset. Round 3 does not
certify that they enumerate all primitive `Gamma_0(11)` conjugacy classes, and
it does not prove that their newform periods satisfy a Hecke recurrence. The
formal Route-A tuple remains unassigned and Route B remains disallowed.

The next arithmetic gate is unchanged but now better posed: any proposed
Hecke/Euler rule must be a rule on the same **oriented conjugacy-class owner**
and must respect both `I(M^(-1))=-I(M)` and `I(M^r)=r I(M)` without importing
prime labels.
