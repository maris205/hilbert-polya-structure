# Derivation Package

## Target

Derive an all-period, data-free obstruction to a raw rational-prime derivative
multiplier for the frozen PCF quadratic

$$
g(z)=z^2-u,\qquad u^3-2u^2+2u-2=0,
$$

and identify exactly what survives when the target is changed from
$|\lambda|=p$ to $|\lambda|=p^n$.

## Status

`COHERENT AS STATED`

The raw-prime target survives unchanged.  The exponent-prime target must
retain the source-locked open case $p=2$ for $n\ge 2$.

## Invariant Object

The organizing object is the **raw return multiplier**

$$
\lambda_{n,\alpha}=(F^{\circ n})'(\alpha),
$$

not its logarithm, spectral radius, numerical approximation, or a fitted
prime label.  The decisive arithmetic invariant is the quotient

$$
\beta_{n,\alpha}=\lambda_{n,\alpha}/m^n.
$$

## Assumptions

- $K$ is a number field and $\mathcal O_K$ is its ring of integers.
- $F\in\mathcal O_K[X]$ is monic of degree at least two.
- $F'=mH$ coefficientwise for $m\in\mathbb Z$, $m\ge2$, and
  $H\in\mathcal O_K[X]$.
- $\alpha$ is a finite point with $F^{\circ n}(\alpha)=\alpha$.
- The arithmetic conclusion assumes $\lambda_{n,\alpha}\in\mathbb Q$.
- For a real orbit, $|\lambda|=p$ automatically gives
  $\lambda=\pm p\in\mathbb Q$.  For a complex orbit, rational modulus alone
  does not imply a rational multiplier and is outside this derivation.

## Notation

- $F^{\circ j}$: $j$-fold iterate.
- $\overline{\mathbb Z}$: algebraic integers in $\overline{\mathbb Q}$.
- $p$: a positive rational prime.
- Raw-prime target: $\lambda\in\mathbb Q$ and $|\lambda|=p$.
- Rational exponent-prime target: $\lambda\in\mathbb Q$ and
  $|\lambda|=p^n$.

## Derivation Strategy

Use monicity to place every point on a finite periodic orbit in
$\overline{\mathbb Z}$.  Use the chain rule and the coefficient content of
$F'$ to extract a factor $m^n$.  The remaining factor is an algebraic integer.
If the full multiplier is rational, the remaining factor belongs to
$\mathbb Q\cap\overline{\mathbb Z}=\mathbb Z$.  Specialize to $m=2$ and
handle the only period-one residue directly.

## Derivation Map

1. `Identity`: $F^{\circ n}(\alpha)-\alpha=0$.
2. `Proposition`: monicity of $F^{\circ n}-X$ implies
   $\alpha\in\overline{\mathbb Z}$.
3. `Identity`: the chain rule factors
   $\lambda=m^n\prod_j H(F^{\circ j}(\alpha))$.
4. `Proposition`: the product after $m^n$ is an algebraic integer.
5. `Proposition`: rationality of $\lambda$ makes that product an ordinary
   integer, so $\lambda\in m^n\mathbb Z$.
6. `Specialization`: $g'=2z$ gives $m=2$.
7. `Corollary`: $n\ge2$ excludes raw primes by divisibility by $4$.
8. `Boundary calculation`: $n=1$ and $\lambda=\pm2$ force respectively
   $u=0$ and $u=2$, both incompatible with the frozen cubic.
9. `Scope split`: $|\lambda|=p^n$ excludes odd $p$, but leaves $p=2$ open.
10. `Interpretation`: on a regular cotangent branch the return spectrum is
    $(\lambda,\lambda^{-1})$; this does not globalize through $q=0$.

## Main Derivation

### Step 1: periodic-point integrality

Because $F$ is monic over $\mathcal O_K$, every iterate $F^{\circ n}$ is
monic over $\mathcal O_K$.  Hence $F^{\circ n}(X)-X$ is monic.  Every finite
periodic point is a root of this polynomial, is integral over $\mathcal O_K$,
and therefore is integral over $\mathbb Z$.  All points
$F^{\circ j}(\alpha)$ on the orbit are algebraic integers as well.

### Step 2: derivative-content factorization

The exact chain-rule identity is

$$
\lambda_{n,\alpha}
=\prod_{j=0}^{n-1}F'(F^{\circ j}(\alpha))
=m^n\prod_{j=0}^{n-1}H(F^{\circ j}(\alpha)).
$$

The second product, denoted $\beta_{n,\alpha}$, is an algebraic integer.

### Step 3: rational specialization

If $\lambda_{n,\alpha}\in\mathbb Q$, then

$$
\beta_{n,\alpha}=\lambda_{n,\alpha}/m^n\in\mathbb Q.
$$

Thus $\beta_{n,\alpha}\in\mathbb Q\cap\overline{\mathbb Z}=\mathbb Z$, and

$$
\lambda_{n,\alpha}\in m^n\mathbb Z.
$$

This is exact for every $n$ and is not inferred from a cutoff.

### Step 4: frozen quadratic and raw primes

The cubic defining $u$ is monic, hence $u$ is an algebraic integer.  For
$g(z)=z^2-u$, the derivative is $2z$, so any rational period-$n$ multiplier
lies in $2^n\mathbb Z$.  If $n\ge2$ and $|\lambda|$ is a positive rational
prime, then that prime is divisible by $4$, which is impossible.

At $n=1$, a raw-prime absolute value can only be $2$.  The equations

$$
2z=2,\quad z^2-u=z
$$

give $z=1$ and $u=0$; the equations

$$
2z=-2,\quad z^2-u=z
$$

give $z=-1$ and $u=2$.  Since the frozen cubic evaluates to $-2$ at $0$
and $2$ at $2$, neither case occurs.

### Step 5: exponent-prime boundary

If $|\lambda|=p^n$ and $\lambda\in\mathbb Q$, write
$\lambda=2^n k$ with $k\in\mathbb Z$.  An odd $p$ gives incompatible
$2$-adic valuations.  For $p=2$, the equation only yields $|k|=1$, so no
contradiction follows.  The all-period $p=2$ residue remains open.

### Step 6: conjugacy and symplectic interpretation

The linear coordinate change $\phi(x)=-ux$ satisfies
$\phi\circ f_u=g\circ\phi$ and preserves periodic multipliers.  On $q\ne0$,

$$
\widehat g(q,p)=\left(q^2-u,\frac{p}{2q}\right)
$$

satisfies $\widehat g^*(P\,dQ)=p\,dq$.  At $p=0$, the one-step derivative is
$\operatorname{diag}(g'(q),g'(q)^{-1})$, so the return spectrum is
$(\lambda,\lambda^{-1})$.  This is an exact branchwise interpretation, not a
compact global symplectomorphism.

## Remarks and Interpretation

- The nonlinear derivative clock escapes Paper 1's finite-rank locally
  constant hypothesis, yet a different arithmetic obstruction closes its raw
  rational-prime target.
- The exact low-period resultants are implementation certificates only.
- The nonintegral control $z^2-3/4$ can have fixed multiplier $3$, showing
  that monic state dynamics alone is insufficient when the coefficient is not
  an algebraic integer.

## Boundaries and Non-Claims

- No claim is made about a complex multiplier with rational modulus but
  nonrational phase.
- No claim is made that all rational multipliers are absent.
- No claim is made that $\pm2^n$ is absent for exact period $n\ge2$.
- No numerical near-prime or approximate equality is relevant.
- The cotangent relation is singular at the critical line, noncompact, and
  globally many-to-one.
- No zeta-zero, quantization, or Route-B stage is opened.

## Open Risks

- The general divisibility lemma is elementary and should be presented as a
  certificate, not a new arithmetic-dynamics theory.
- A dynatomic factor can contain lower exact periods at root-of-unity
  collisions; the exact audit must explicitly remove such contamination.
- The phrase “prime multiplier” must always retain the rational-multiplier
  hypothesis, or be restricted to real periodic orbits.
