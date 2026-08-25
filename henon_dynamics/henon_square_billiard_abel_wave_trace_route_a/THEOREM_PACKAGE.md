# C157 proof package

## Status and notation

**Status: PROVABLE AS STATED.**  On the unit square let

```text
W_D(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2)),   Re(s)>0.          (1)
```

This is `Tr exp(-s sqrt(Delta_D))` for the ordinary Dirichlet Laplacian.  We
use the Fourier convention
`fhat(m)=integral_R2 f(x) exp(-2*pi*i*m dot x) dx` and the principal
power on the right half-plane.

## Theorem 1: exact Poisson formula

For `Re(s)>0`,

```text
W_D(s)=s/(2pi) sum_(m in Z^2)(s^2+4|m|^2)^(-3/2)
       -1/4-1/(exp(pi s)-1).                                  (2)
```

Both sides converge absolutely and locally uniformly.

**Proof.**  For real `s>0`, radial Fourier transformation gives

```text
Fourier[exp(-pi*s*|x|)](m)
 =2pi integral_0^infty r exp(-pi*s*r)J_0(2pi|m|r)dr
 =2s/[pi(s^2+4|m|^2)^(3/2)].                                 (3)
```

The last identity is the derivative in `pi*s` of the elementary
Laplace--Bessel transform.  Gaussian regularization justifies Poisson
summation and passage to the limit.  If `Theta` is the full lattice sum, its
origin, four axes, and four open quadrants give

```text
Theta(s)=1+4/(exp(pi*s)-1)+4W_D(s).
```

Combining this with (3) proves (2) for real `s>0`.  The primal sum is locally
normally convergent by exponential decay.  For the dual sum, compact subsets
of `Re(s)>0` have a uniform `O(|m|^-3)` majorant.  Moreover
`s^2+4|m|^2` never meets the nonpositive real axis: its imaginary part is
`2 Re(s) Im(s)` unless `Im(s)=0`, when it is positive.  Thus the principal
power is holomorphic.  Analytic continuation proves (2) throughout the right
half-plane.  ∎

## Theorem 2: primitive clean-family rearrangement

Separating the zero mode and axes in (2) yields the Weyl term
`1/(2pi s^2)` and the axis term

```text
2s/pi sum_(r>=1)(s^2+4r^2)^(-3/2).
```

Every nonaxis dual vector has the unique form
`(plus_or_minus r a, plus_or_minus r b)`, where `a,b>=1`, `gcd(a,b)=1`.
Therefore the remaining part is

```text
2s/pi sum_(a,b>=1,gcd=1) sum_(r>=1)
       (s^2+r^2 L_(a,b)^2)^(-3/2),              (4)
L_(a,b)=2sqrt(a^2+b^2).
```

**Proof.**  Take `r=gcd(|m_1|,|m_2|)`.  Division gives one ordered positive
primitive direction; coordinate swaps remain distinct.  The four sign choices
multiply the coefficient `s/(2pi)` in (2) by four, giving `2s/pi`.  Absolute
convergence permits the rearrangement.  The lengths in (4) are precisely the
square-billiard clean-family lengths and all repetitions are retained.  ∎

## Theorem 3: Abel-boundary strata

Put `s=epsilon-it`, `epsilon>0`, and let `epsilon` decrease to zero.

1. The dual zero mode is the Weyl term `1/(2pi s^2)`.
2. Axis terms have `-3/2` branch points at `t=plus_or_minus 2r`.
3. Interior primitive terms have `-3/2` branch points at
   `t=plus_or_minus r L_(a,b)`.
4. Independently, `-1/(exp(pi s)-1)` has simple poles at `s=2iq`, hence
   `t in 2Z`.

At an axis time a branch point may coincide with a boundary-subtraction pole,
but the singularity types differ and no cancellation is asserted.  Thus the
branch list is not advertised as the complete boundary singular set.

**Proof.**  The first statement is direct.  Each denominator in (4) vanishes
at `s=plus_or_minus i rL`; the fixed principal power supplies the boundary
branch.  For example, at `t=rL`, its modulus grows as
`(2rL*epsilon)^(-3/2)`.  The exponential denominator vanishes simply at
`s=2iq`, with residue `-1/pi`.  ∎

## Exact and numerical certificate

Integer shell reconstruction through squared norm 500 gives 98 primitive
shells, 239 ordered primitive directions, 161 occupied dual shells, and 373
ordered positive vectors.  Squared norm 65 is the first shell with four
ordered primitive directions: `(1,8),(4,7),(7,4),(8,1)`.

For numerical verification, the primal square tail is bounded by
`2q^(J+2)/(1-q)^2`, `q=exp(-pi Re(s)/sqrt(2))`.  On the dual side use

```text
E_alpha=sum_(m!=0)|m|^(-2alpha)=4 zeta(alpha) beta(alpha)
```

and subtract `1/(8|m|^3)-3s^2/(64|m|^5)`.  To make the complex remainder
explicit, apply the integral Taylor formula to
`g(z)=(4|m|^2+z)^(-3/2)` along the segment from zero to `z=s^2`:

```text
g(s^2)-g(0)-g'(0)s^2
 =s^4 integral_0^1 (1-t) g''(t s^2) dt.
```

Here `g''(z)=(15/4)(4|m|^2+z)^(-7/2)`.  If
`|m|>=M>=|s|`, then
`|4|m|^2+t s^2|>=4|m|^2-|s|^2>=3|m|^2`, so each remainder is at most

```text
15|s|^4/[8*3^(7/2)|m|^7].
```

Outside the max-norm square there are exactly `8k` lattice points with max
norm `k`, and their Euclidean norm is at least `k`.  Therefore

```text
sum_(maxnorm(m)>M)|remainder_m|
 <=15|s|^4/3^(7/2) sum_(k>M)k^(-6)
 <=|s|^4/[3^(5/2)M^5].
```

Multiplication by the outer factor `|s|/(2pi)` gives the dual tail

```text
|s|^5/(2pi 3^(5/2) M^5).                         (5)
```

The analytic truncation envelopes in (5) are rigorous.  The corresponding
55-decimal `mpmath` centers are deterministic sentinels, not
interval-arithmetic outputs; the full checker reserves an explicit `1e-34`
serialization/rounding margin when comparing independently truncated centers.

## Route-A boundary

The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  Equation (2) is a
genuine source Dirichlet trace and `sqrt(Delta_D)` is a natural self-adjoint
quantization.  Clean families are still not isolated primitive orbits, and no
isolated stability determinant, target trace/divisor/functional equation or
counting law, arithmetic local/Euler factor, root number, automorphy,
Hilbert--Polya construction, or Route-B authorization is claimed.
