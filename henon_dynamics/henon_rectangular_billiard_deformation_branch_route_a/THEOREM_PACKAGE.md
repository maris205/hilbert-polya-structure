# C167 theorem package: deformation branches of rectangular billiards

Fix α>0 and let

```text
Q_alpha=(0,1)x(0,alpha),
W_alpha(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2/alpha^2)), Re(s)>0.
```

All fractional powers below use the principal branch.

## Theorem 1: exact source Poisson representation

For ℜ(s)>0,

```text
W_alpha(s)
 = alpha*s/(2*pi) * sum_((m,n) in Z^2)
     (s^2+4*(m^2+alpha^2*n^2))^(-3/2)
   - 1/4
   - 1/(2*(exp(pi*s)-1))
   - 1/(2*(exp(pi*s/alpha)-1)).
```

The dual sum is locally normally convergent in the right half-plane.

## Theorem 2: every shell has a canonical full-trace coefficient

Let

```text
R_alpha(E)=#{(m,n) in Z^2 : m^2+alpha^2*n^2=E},  E>0.
```

At the positive shell time (t_E=2\sqrt E),

```text
lim_(epsilon down to 0) epsilon^(3/2)
  W_alpha(epsilon-i*t_E)
 = alpha*exp(i*pi/4)*R_alpha(E)/(8*pi*E^(1/4)).
```

At (-t_E) the limit is the complex conjugate.  This is a statement about
the complete trace and complete signed shell, not one isolated summand.

### Proof

For every matching lattice point,

```text
s^2+4E=epsilon*(epsilon-2*i*t_E),
alpha*s/(2*pi) * epsilon^(3/2)*(s^2+4E)^(-3/2)
 -> alpha*exp(i*pi/4)/(8*pi*E^(1/4)).
```

Choose a radius after fixing α and (t_E).  Outside it,

```text
m^2+alpha^2*n^2 >= min(1,alpha^2)*(m^2+n^2),
```

so the nonmatching dual terms admit an ε-uniform summable
(|(m,n)|^{-3}) majorant.  The finitely many remaining nonmatching terms
stay bounded and vanish after multiplication by ε³⁄².

Each boundary subtraction has at most a simple (O(\epsilon^{-1})) pole.
When both boundary clocks coincide, they remain a sum of two simple poles,
not a second-order pole.  Therefore even the double-boundary contribution is
(O(\epsilon^{1/2})) after normalization.  This includes the β=4,
(E=4) control where the dual shell has two axis pairs and both boundary
subtractions are singular.  Conjugation follows from the real spectral
coefficients.

## Theorem 3: complete deformation-collision geometry

Set β=α².  For two distinct absolute representatives
(p=(m,n)) and (p'=(m',n')), a non-sign collision satisfies

```text
m^2+beta*n^2 = m'^2+beta*n'^2.
```

If (n^2=n'^2), equality forces (m^2=m'^2), so the representatives were
not distinct.  Otherwise the collision occurs exactly at

```text
beta=(m'^2-m^2)/(n^2-n'^2)>0.
```

Hence every non-sign collision parameter is positive rational, and every
irrational β has sign-only shell multiplicities.  At a collision β₀,

```text
d(E_p-E_p')/d beta = n^2-n'^2 != 0,
d(t_p-t_p')/d beta at beta_0
  = (n^2-n'^2)/sqrt(E_0) != 0.
```

Thus pairwise collisions are transverse.  Within a multiple fibre, distinct
absolute representatives have distinct (n^2), so all pairwise slopes are
distinct.

If β=u/v>0 in lowest terms, shells are precisely the finite fibres

```text
v*m^2+u*n^2=N.
```

This equation is the full rational classification used here.  No general
divisor formula for its representation numbers is claimed.

## Corollary: reciprocal aspect

Interchanging the rectangle sides gives the exact identity

```text
W_alpha(s)=W_(1/alpha)(s/alpha).
```

It sends the shell (m^2+\alpha^2n^2=E) to the reciprocal-aspect shell with
the same geometric source family after the corresponding clock rescaling.

## Finite receipts and negative controls

The released evidence records exact absolute-coordinate fibres through 24.
It finds the first positive primitive collisions at (N=5) for β=1 and at
(N=33) for β=2.  For β=4 it separately records the axis collision at
(N=4) and the first inequivalent primitive collision at (N=65).  Exact
coefficientwise comparison in (\mathbb Q(\sqrt2)) finds no non-sign
collision in the sentinel range.  Four numerical branch rows decrease
strictly toward the theorem coefficient.  None of these cutoffs proves the
all-parameter statements above.

The proof does **not** assert a uniform irrational shell gap, an isolated
primitive-orbit determinant, or an isolated stability amplitude.

## Route-A verdict

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
```

The natural operator is the rectangular Dirichlet half-wave generator.
Positive-dimensional clean families remain aggregated, no target global
structure is compared, and Route B is disabled.
