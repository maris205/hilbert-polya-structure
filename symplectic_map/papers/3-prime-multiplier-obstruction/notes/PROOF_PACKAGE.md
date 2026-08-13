# Proof Package

## Claim

### Theorem A (derivative-content divisibility)

Let $K$ be a number field with ring of integers $\mathcal O_K$.  Let
$F\in\mathcal O_K[X]$ be a monic polynomial of degree at least two.  Suppose
that

$$
F'(X)=mH(X)
$$

for an integer $m\ge2$ and a polynomial $H\in\mathcal O_K[X]$.  Let
$\alpha\in\overline{\mathbb Q}$ be a finite point satisfying
$F^{\circ n}(\alpha)=\alpha$ for some $n\ge1$, and put

$$
\lambda_{n,\alpha}=(F^{\circ n})'(\alpha).
$$

If $\lambda_{n,\alpha}\in\mathbb Q$, then

$$
\lambda_{n,\alpha}\in m^n\mathbb Z.
$$

The statement does not require $n$ to be the exact period.  When $n$ is the
exact period, $\lambda_{n,\alpha}$ is the usual cycle multiplier.

### Corollary B (frozen all-period raw-prime obstruction)

Let $u$ be the real root of $u^3-2u^2+2u-2=0$, and let
$g(z)=z^2-u$.  No finite periodic orbit of $g$ has a rational multiplier
$\lambda$ with $|\lambda|$ a rational prime.  The same is true for
$f_u(x)=1-u x^2$.

### Corollary C (exponent-prime boundary)

If an exact period-$n$ multiplier of $g$ is rational and satisfies
$|\lambda|=p^n$ for a rational prime $p$, then $p=2$.  This corollary does
not assert that the $p=2$ case occurs or does not occur.  For $n\ge2$ that
case remains open here.

## Status

`PROVABLE AS STATED`

The original all-period raw-prime claim survives unchanged.  The
exponent-prime claim is deliberately weaker: odd primes are excluded, while
$p=2$ is not decided.

## Assumptions

- $K$ is a number field and $\mathcal O_K$ is its full ring of integers.
- $F$ is monic and all coefficients of $F$ lie in $\mathcal O_K$.
- The formal derivative has the coefficient-wise factorization
  $F'=mH$ with $m\ge2$ in $\mathbb Z$ and $H\in\mathcal O_K[X]$.
- Only finite periodic points are considered.  The point at infinity of a
  polynomial map is not part of Theorem A.
- “Rational multiplier” means membership in $\mathbb Q$, not merely rational
  absolute value.
- In Corollary B, $u$ is the selected real algebraic number, although the
  proof of divisibility works for every conjugate of $u$.

## Notation

- $F^{\circ j}$ is the $j$-fold iterate, with $F^{\circ0}$ the identity.
- A complex number is an algebraic integer if it is integral over $\mathbb Z$.
- $\lambda_{n,\alpha}$ is the derivative of the $n$th iterate at $\alpha$.
- A raw prime target is $|\lambda|=p$.
- A rational exponent-prime target is $\lambda\in\mathbb Q$ and
  $|\lambda|=p^n$.

## Proof Strategy

The monicity of $F$ makes every finite periodic point an algebraic integer.
The chain rule then exhibits the multiplier as $m^n$ times an algebraic
integer.  If the multiplier is rational, division by $m^n$ is simultaneously
rational and an algebraic integer, hence an ordinary integer.  The frozen
quadratic has $m=2$; divisibility excludes raw primes at every period at
least two, and a direct fixed-point calculation closes period one.

## Dependency Map

1. Theorem A depends on the monicity of $F^{\circ n}(X)-X$ and transitivity
   of integrality.
2. Its multiplier factorization depends only on the chain rule and
   $F'=mH$.
3. The last arithmetic step uses
   $\mathbb Q\cap\overline{\mathbb Z}=\mathbb Z$.
4. Corollary B depends on $u$ being an algebraic integer, Theorem A with
   $m=2$, and a separate exact fixed-point check for $\lambda=\pm2$.
5. Transfer from $g$ to $f_u$ uses the invertible linear conjugacy
   $\phi(x)=-ux$ and conjugacy invariance of multipliers.
6. Corollary C depends on the $2$-adic valuation of the equality
   $2^n k=\pm p^n$.
7. The cotangent statement is logically downstream and is not used to prove
   the arithmetic obstruction.

## Proof

### Step 1: finite periodic points are algebraic integers

Because $F$ is monic and has coefficients in $\mathcal O_K$, every iterate
$F^{\circ n}$ is monic and belongs to $\mathcal O_K[X]$.  Consequently,

$$
F^{\circ n}(X)-X
$$

is monic.  The equality $F^{\circ n}(\alpha)=\alpha$ says that $\alpha$ is a
root of this monic polynomial, so $\alpha$ is integral over $\mathcal O_K$.
The ring $\mathcal O_K$ is integral over $\mathbb Z$.  By transitivity of
integrality, $\alpha$ is integral over $\mathbb Z$ and therefore is an
algebraic integer.

For each $0\le j<n$, the value $F^{\circ j}(\alpha)$ is a polynomial in the
algebraic integer $\alpha$ with algebraic-integer coefficients.  Hence each
$F^{\circ j}(\alpha)$ is an algebraic integer.

### Step 2: factor the multiplier by $m^n$

The chain rule gives

$$
\lambda_{n,\alpha}
=\prod_{j=0}^{n-1}F'\!\left(F^{\circ j}(\alpha)\right)
=m^n\prod_{j=0}^{n-1}H\!\left(F^{\circ j}(\alpha)\right).
$$

Every coefficient of $H$ is an algebraic integer and every argument
$F^{\circ j}(\alpha)$ is an algebraic integer by Step 1.  Thus

$$
\beta:=\prod_{j=0}^{n-1}H\!\left(F^{\circ j}(\alpha)\right)
$$

is an algebraic integer, and $\lambda_{n,\alpha}=m^n\beta$.

### Step 3: use rationality

Assume $\lambda_{n,\alpha}\in\mathbb Q$.  Since $m^n$ is a nonzero rational
integer,

$$
\beta=\frac{\lambda_{n,\alpha}}{m^n}\in\mathbb Q.
$$

Step 2 also shows that $\beta$ is an algebraic integer.  A rational
algebraic integer is an integer, so $\beta\in\mathbb Z$.  Therefore

$$
\lambda_{n,\alpha}=m^n\beta\in m^n\mathbb Z.
$$

This proves Theorem A. $\square$

### Step 4: specialize to $g(z)=z^2-u$

The polynomial

$$
P(U)=U^3-2U^2+2U-2
$$

is monic, so each of its roots, including the selected real root $u$, is an
algebraic integer.  Moreover,

$$
P'(U)=3U^2-4U+2
$$

has discriminant $(-4)^2-4\cdot3\cdot2=-8<0$ and positive leading
coefficient.  Hence $P'(U)>0$ for every real $U$, so $P$ is strictly
increasing and has exactly one real root.  The rational-root test excludes
$\pm1$ and $\pm2$, so the cubic is irreducible over $\mathbb Q$; this also
justifies using $1,u,u^2$ as a basis of $K=\mathbb Q(u)$.  Then

$$
g(z)=z^2-u\in\mathcal O_K[z],
\qquad g'(z)=2z.
$$

Theorem A applies with $m=2$ and $H(z)=z$.  For every finite point fixed by
$g^{\circ n}$,

$$
\lambda\in\mathbb Q \quad\Longrightarrow\quad \lambda\in2^n\mathbb Z.
$$

### Step 5: exclude raw primes for periods $n\ge2$

Let the exact period be $n\ge2$ and suppose $\lambda\in\mathbb Q$ with
$|\lambda|=p$ prime.  Step 4 gives $\lambda=2^n k$ for some $k\in\mathbb Z$.
The equality $|\lambda|=p>0$ implies $k\ne0$, so $4$ divides $p$.  No positive
prime is divisible by $4$.  This is a contradiction.

### Step 6: close the period-one residue $p=2$

For a fixed point $z$ of $g$, the multiplier is $g'(z)=2z$.  Divisibility by
$2$ shows that a raw rational-prime absolute value can only be $2$.

If $2z=2$, then $z=1$, and the fixed-point equation gives

$$
1-u=g(1)=1,
$$

so $u=0$.  But $P(0)=-2$, so the selected $u$ is not $0$.

If $2z=-2$, then $z=-1$, and the fixed-point equation gives

$$
1-u=g(-1)=-1,
$$

so $u=2$.  But $P(2)=2$, so the selected $u$ is not $2$.

Thus neither multiplier $2$ nor multiplier $-2$ occurs at a fixed point.
Combined with Step 5, this proves the all-period assertion for $g$.

### Step 7: transfer the result to $f_u$

Since $P(0)\ne0$, $u\ne0$ and the linear map $\phi(x)=-ux$ is invertible.
A direct computation gives

$$
\phi(f_u(x))=-u(1-ux^2)=(-ux)^2-u=g(\phi(x)).
$$

Hence $\phi\circ f_u=g\circ\phi$.  The conjugacy maps period-$n$ points to
period-$n$ points.  Differentiating
$\phi\circ f_u^{\circ n}=g^{\circ n}\circ\phi$ at a periodic point and
cancelling the nonzero constant derivative $\phi'=-u$ shows that the two
multipliers agree.  The raw-prime obstruction for $g$ therefore also holds
for $f_u$.  This proves Corollary B. $\square$

### Step 8: prove the stated exponent-prime boundary

Suppose $\lambda\in\mathbb Q$, the exact period is $n$, and
$|\lambda|=p^n$.  Step 4 gives $\lambda=2^n k$ with $k\in\mathbb Z$.  If $p$
is odd, the right side of

$$
2^n|k|=p^n
$$

has $2$-adic valuation zero while the left side has $2$-adic valuation at
least $n$, a contradiction.  Therefore $p=2$ is necessary.  When $p=2$ the
equality reduces to $|k|=1$, which the divisibility theorem does not forbid.
This proves exactly Corollary C and no more. $\square$

## Classical Cotangent Bridge (not used in the proof)

Let $\theta=p\,dq$ be the canonical one-form on $T^*\mathbb R$.  On the
regular locus $q\ne0$, define

$$
\widehat g(q,p)=\left(Q,P\right)
=\left(q^2-u,\frac{p}{2q}\right).
$$

Then

$$
\widehat g^*\theta
=\widehat g^*(P\,dQ)
=\frac{p}{2q}\,d(q^2-u)
=p\,dq
=\theta.
$$

Thus the map is exact symplectic on each branch $q>0$ and $q<0$.  If a
periodic orbit avoids the critical point $q=0$, the orbit on the zero
section $p=0$ is defined, and the derivative of one lifted step there is

$$
D\widehat g(q,0)
=\begin{pmatrix}g'(q)&0\\0&g'(q)^{-1}\end{pmatrix}.
$$

The return derivative therefore has eigenvalues $\lambda$ and
$\lambda^{-1}$.

This calculation does not produce a global symplectomorphism.  The formula
is singular at $q=0$; the two regular branches have overlapping images; the
phase space is noncompact; and a critical periodic orbit has multiplier
zero, for which the reciprocal-multiplier lift is not defined.  These are
structural limitations, not numerical defects.

## Corrections or Missing Assumptions

- The rationality hypothesis on $\lambda$ is essential.  An algebraic
  integer can have rational absolute value without itself lying in
  $\mathbb Q$.
- For the condition $|\lambda|=p^n$ on complex periodic orbits, the theorem
  applies only when $\lambda\in\mathbb Q$.  A modulus-only claim would need a
  different argument.
- Monicity is used to prove periodic-point integrality.  It cannot be
  removed without replacing it by an explicit integrality hypothesis on the
  periodic point or by controlling the leading coefficient.
- The $p=2$ exponent-prime target for $n\ge2$ is not settled by this package.

## Open Risks

- The main theorem is elementary once formulated.  Its value is as an exact
  obstruction certificate for a frozen candidate, not as a claimed new
  general theorem in arithmetic dynamics.
- Formal dynatomic period can differ from exact period at parabolic
  collisions.  The low-period audit must distinguish these notions and must
  not use a resultant root alone as an exact-period certificate.
- The branchwise cotangent map must never be described as compact, globally
  invertible, globally defined, or a smooth symplectic lift through the
  critical line.
