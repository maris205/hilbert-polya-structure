# Proof package: one complete reconstruction and one unclosed contract

2026-09-08. The [frozen contracts](FROZEN_CONTRACTS.md) precede this file.
No mathematical program, census or numerical approximation was executed.

## Claims and status

- **CF1: PROVABLE AS STATED.** The entire all-polynomial/all-prime count
  and zeta dichotomy below is proved. This does not imply that its
  classical/owned reconstruction is substantial enough for admission.
- **CF2: PROVABLE AS STATED by direct source coverage.** The short
  application is recorded in the scout report, not offered as a new proof.
- **CF3: NOT CURRENTLY JUSTIFIED.** Only the universal nonreduced-iterate
  obstruction below is proved. It is not a rationality classification.

## CF1: assumptions and notation

Fix a prime $p$ and $a\in\mathbb F_p[x]$. Set
$\bar k=\overline{\mathbb F}_p$ and
$F_a(x,y)=(x^p,y^p+a(x)y)$ on the entire $\mathbb A^2(\bar k)$.
For each $n\ge1$, let

$$
Q=p^n,\qquad r=p^{v_p(n)},\qquad n=rm,\quad p\nmid m.
$$

$N_a(n)$ denotes distinct fixed points of $F_a^n$ and
$Z_a(t)=\exp(\sum_{n\ge1}N_a(n)t^n/n)$.
For $x\in\mathbb F_Q$ with $a(x)\ne0$, let
$\rho_x=\operatorname{Norm}_{\mathbb F_Q/\mathbb F_p}(a(x))$.
Let $R_a(n)$ count those $x$ with $\rho_x=1$.

### Strategy and dependency map

1. Frobenius in the first coordinate fixes exactly $\mathbb F_Q$.
2. The Kummer change $y=tz$, $t^{p-1}=a(x)$, changes the fiber map into
   $z\mapsto z^p+z$ while Frobenius transports $t$.
3. The first nonzero term of a linearized polynomial gives its number of
   distinct geometric roots, including inseparable returns.
4. Finite-field cyclic-group arithmetic identifies $R_a(n)$ with the
   point count of a fixed Kummer curve.
5. The classical Weil bound on the finitely many components separates
   their dimension-one leading contribution from a holomorphic error.
6. The characteristic-divisibility decomposition and radial-order proof
   already used in C404 yields the stated natural boundary.

The only non-elementary numerical estimate imported in Step 5 is the
classical bound $\#Y(\mathbb F_{q^s})=q^s+O(q^{s/2})$ for a fixed smooth
geometrically integral affine curve $Y/\mathbb F_q$. Compactifying $Y$
adds a bounded number of points, so it follows from the Hasse–Weil bound.
The full hypothesis and bound were checked in Poonen's author-hosted
text, §7.2/Corollary 7.2.1; §7.7.1(ii) also gives the affine form.
[Author text](https://math.mit.edu/~poonen/papers/Qpoints.pdf).
Rojas-León's primary Kummer-curve paper supplies the same classical
context; none of its stronger generic estimates is assumed here.

### Step 1. The base and the zero fibers

If $(x,y)$ is fixed by $F_a^n$, then $x^Q=x$, hence $x\in\mathbb F_Q$.
For such $x$ put $x_j=x^{p^j}$. Since $a$ has coefficients in
$\mathbb F_p$, $a(x_j)=a(x)^{p^j}$.

If $a(x)=0$, then $a(x_j)=0$ at every step. The fiber return is
$y\mapsto y^Q$, whose fixed polynomial $y^Q-y$ has exactly $Q$ distinct
roots: its derivative is $-1$. No zero fiber is deleted.

### Step 2. Kummer trivialization and its actual return twist

Suppose $a(x)\ne0$. Choose $t\in\bar k^*$ with $t^{p-1}=a(x)$ and put
$y=tz$. At step $j$ use $t_j=t^{p^j}$. Then

$$
(t_jz)^p+a(x_j)t_jz=t_{j+1}(z^p+z).
$$

Thus the lifted dynamics is
$(x,t,z)\mapsto(x^p,t^p,z^p+z)$ on
$C_a^*\times\mathbb A^1$, where

$$C_a^*=\{(x,t):t^{p-1}=a(x),\ t\ne0\}.$$

The chosen $t$ need not belong to $\mathbb F_Q$ and must not be assumed
to return unchanged. In fact

$$
\frac{t^Q}{t}=a(x)^{(Q-1)/(p-1)}=\rho_x\in\mathbb F_p^*.
$$

Writing $\tau(z)=z^p$ as an $\mathbb F_p$-linear operator, the fixed
equation in this fiber is therefore

$$[(\tau+1)^n-\rho_x^{-1}](z)=0.\tag{1}$$

This is a polynomial of degree $Q$, not a statement that the point
$z$ itself must be rational over $\mathbb F_Q$.

### Step 3. Distinct roots, not polynomial degree

If $\rho_x\ne1$, the coefficient of $z$ in (1) is
$1-\rho_x^{-1}\ne0$. The polynomial is separable and has $Q$ distinct
roots in $\bar k$.

If $\rho_x=1$, in the ordinary commutative polynomial ring
$\mathbb F_p[T]$ we have

$$
(1+T)^n-1=(1+T^r)^m-1=mT^r+\text{terms of higher degree}.
$$

The coefficient $m$ is nonzero in $\mathbb F_p$ and the top degree is
$n$. Substituting $T=\tau$ shows that the lowest power of $z$ in (1) is
$z^{p^r}$ and the highest is $z^{p^n}$. Over the perfect field $\bar k$
the polynomial is the $p^r$-th power of a separable polynomial of degree
$p^{n-r}$. Consequently this fiber has exactly $p^{n-r}$ distinct roots.

There are $Q$ base points and only the $R_a(n)$ norm-one nonzero fibers
lose distinct roots. We conclude

$$
\boxed{N_a(n)=p^{2n}-(p^n-p^{n-r})R_a(n).}\tag{2}
$$

This proves finiteness for every $n$. The total fixed-scheme length is
$Q^2$, since the base equation is separable of degree $Q$ and each
monic fiber equation has degree $Q$. Formula (2) is the ordinary count;
using that scheme length instead would erase its entire correction.

### Step 4. The exact arithmetic curve carrier

For $b\in\mathbb F_Q^*$, the cyclic group $\mathbb F_Q^*$ implies that
$t^{p-1}=b$ has $p-1$ solutions in $\mathbb F_Q$ precisely when
$b^{(Q-1)/(p-1)}=1$, and none otherwise. Hence

$$\boxed{\#C_a^*(\mathbb F_Q)=(p-1)R_a(n).}\tag{3}$$

When $a=0$, $C_a^*$ is empty and (2) gives $N_a(n)=p^{2n}$, so
$Z_a(t)=(1-p^2t)^{-1}$. This proves that entire stratum.

Assume from now on that $a\ne0$. Let
$U=\mathbb A^1\setminus\{a=0\}$. The cover $C_a^*\to U$ is finite
étale of degree $p-1$, because its derivative in $t$ is
$(p-1)t^{p-2}\ne0$. In particular $C_a^*$ is a smooth curve with at least
one and at most $p-1$ geometric connected components. Its irreducible
components are disjoint, because a regular one-dimensional local ring
cannot contain two distinct local branches.

Let Frobenius permute the geometric components in $s\ge1$ cycles of
lengths $h_1,\ldots,h_s$. Then $1\le h_j\le p-1$, so $p\nmid h_j$.
The number of components fixed by its $n$-th power is

$$d_n=\sum_{j=1}^s h_j\,\mathbf1_{h_j\mid n}.$$

A component not fixed by Frobenius to the $n$-th power has no
$\mathbb F_Q$-point: such a point would lie both on that component and
on a distinct Frobenius translate. Each fixed component descends to
$\mathbb F_Q$ and has $Q+O(Q^{1/2})$ points by the curve estimate above.
There are only finitely many components, with fixed genera and boundary
sets. Thus for a constant depending on $p,a$ but not $n$,

$$
\frac{R_a(n)}{p^n}=
\frac{1}{p-1}\sum_{j=1}^s h_j\mathbf1_{h_j\mid n}+E_n,
\qquad |E_n|\le C p^{-n/2}.\tag{4}
$$

No uniform constant across polynomials of unbounded degree is needed:
the theorem fixes each map and proves all its times. Constants and
repeated-root polynomials require no geometric-irreducibility assumption.

### Step 5. A product with a holomorphic error

Put $u=p^2t$ and $b_n=p^{-p^{v_p(n)}}$. Since $0\le N_a(n)\le p^{2n}$,
the defining logarithmic series converges for $|u|<1$. By (2) and (4),

$$
\frac{N_a(n)}{p^{2n}}=
1+\frac{b_n-1}{p-1}\sum_{j=1}^s h_j\mathbf1_{h_j\mid n}
+(b_n-1)E_n.
$$

Define

$$H(u)=\sum_{n\ge1}(b_n-1)E_n\frac{u^n}{n}.$$

This is holomorphic for $|u|<\sqrt p$ by (4). In particular its
exponential is nonzero throughout a neighborhood of the unit circle.
For $k\ge1$ define positive, summable real numbers

$$
\gamma_k=\frac{p^{-p^{k-1}}-p^{-p^k}}{(p-1)p^k}.
$$

The elementary finite telescoping identity

$$
b_n=p^{-1}+\sum_{k\ge1}
(p^{-p^k}-p^{-p^{k-1}})\mathbf1_{p^k\mid n}
$$

and $p\nmid h_j$ give, with every logarithm normalized to vanish at zero,

$$
\boxed{
\log Z_a(u/p^2)=H(u)-\log(1-u)
+\frac1p\sum_{j=1}^s\log(1-u^{h_j})
+\sum_{j=1}^s\sum_{k\ge1}
\gamma_k\log(1-u^{h_jp^k}).}\tag{5}
$$

To check the coefficient, substitute $n=h_jm$ in the relevant sum:
$h_j/n=1/m$ and $b_{h_jm}=b_m$. The nondistorted term contributes
$+(p-1)^{-1}\log(1-u^{h_j})$ and the $p^{-1}$ term contributes
$-[p(p-1)]^{-1}\log(1-u^{h_j})$; their sum is $p^{-1}$.
Absolute convergence on each closed subdisc of $|u|<1$ justifies all
interchanges. Formula (5) therefore gives the same analytic germ, not a
formally chosen alternative branch.

### Step 6. Fractional radial orders at a dense set

Let $\xi$ be a primitive $p^e$-th root of unity, $e\ge1$.
Since every $h_j$ is prime to $p$, the factors in (5) with $k<e$, and
the finitely many factors $1-u$ and $1-u^{h_j}$, are nonzero at $u=\xi$.
For $k\ge e$, $\xi^{h_jp^k}=1$. For each positive integer $M$,

$$
0\le\frac{\log(1-\rho^M)}{\log(1-\rho)}\le1,
\qquad
\lim_{\rho\uparrow1}
\frac{\log(1-\rho^M)}{\log(1-\rho)}=1.
$$

Dominated convergence against the summable $\gamma_k$ yields

$$
\lim_{\rho\uparrow1}
\frac{\log|Z_a(\rho\xi/p^2)|}{\log(1-\rho)}
=\sigma_e:=s\sum_{k\ge e}\gamma_k>0.
$$

Moreover

$$
\sigma_e\le
\frac{s}{(p-1)p^e}p^{-p^{e-1}}\longrightarrow0.
$$

A nonzero meromorphic function near $\xi$ has an integral radial
logarithmic order: write it as $(u-\xi)^j g(u)$ with $j\in\mathbb Z$ and
$g$ holomorphic and nonzero at $\xi$. For any fixed positive integer
$L$, take $e$ large enough that $0<L\sigma_e<1$. The radial order of
$Z_a(u/p^2)^L$ is then not an integer, so it cannot extend meromorphically
through any primitive $p^e$-th root of unity.

These roots, for arbitrarily large $e$, are dense on the unit circle.
An extension across any open arc would include one of them, a
contradiction. Thus $|t|=p^{-2}$ is a natural boundary for every such
power. An algebraic germ has only finitely many finite branch/pole
locations, so $Z_a$ is not algebraic over $\mathbb C(t)$. This proves
the full frozen CF1 dichotomy. $\square$

### Step 7. Actual cycles and edge-case audit

Let $P_a(d)$ be the number of points of least period $d$. A point fixed
by $F_a^n$ has least period dividing $n$, whether or not $F_a$ is globally
invertible. Hence $N_a(n)=\sum_{d\mid n}P_a(d)$ and Möbius inversion
gives $P_a(n)=\sum_{d\mid n}\mu(n/d)N_a(d)$. The restriction to one
periodic orbit is a cyclic permutation of $n$ points, giving the frozen
primitive-cycle count $P_a(n)/n$.

- $a=0$ was handled before any nonempty-cover argument.
- $p=2$ has $p-1=1$, so the cover and component argument remain valid.
- At $n=1$, $r=1$; norm-one fibers have exactly one distinct fixed point.
- A constant $a\ne0$ has $\rho_x=a^n$ for every base point; no assumption
  that this norm is always one was made.
- Zeros and repeated zeros of $a$ were retained. The removed set in the
  cover is restored through Step 1, not removed from the original domain.
- No claim that $N_a(n)^{1/n}$ has a limit is used. For example, sparse
  $p$-power times can have a different exponential scale.

## CF3: a proved obstruction, not a completed zeta theorem

### Claim actually proved

Let $X/\mathbb F_q$ be any nonempty smooth geometrically integral surface
and $f$ an automorphism over $\mathbb F_q$. Assume $\operatorname{Fix}(f^n)$
is zero-dimensional for every $n\ge1$. For every geometric point $P$,
there is an integer $b\ge1$ such that, for every $n$ divisible by $b$,
$P$ is fixed by $f^n$ and its local fixed-scheme length is at least three.
Consequently the ordinary fixed-point count is strictly smaller than
the total fixed-scheme length at infinitely many native times.

This applies to CF3 as frozen. It does not prove nonrationality of $Z_X$.

### Proof and dependencies

1. $P$ lies in $X(\mathbb F_{q^v})$ for some finite $v$. The automorphism
   $f$ permutes this finite set, so $P$ has a least period $m$.
2. The derivative $D(f^m)_P$ is an element of the finite group
   $\mathrm{GL}_2(\mathbb F_{q^v})$. Let $e$ be its order and put $b=me$.
   By the chain rule, $D(f^n)_P=I$ for every multiple $n$ of $b$.
3. At $P$, the completed local ring after geometric base change is
   $\bar k[[u,v]]$. The local fixed ideal is generated by
   $f^{n*}(u)-u$ and $f^{n*}(v)-v$. Identity derivative places both
   generators in the square $\mathfrak m^2$ of the maximal ideal.
4. Confinement makes the quotient length finite. Its quotient onto
   $\bar k[[u,v]]/\mathfrak m^2$ shows that the length is at least
   $1+2=3$. Every other fixed point has local length at least one.
   Hence the total fixed-scheme length exceeds the ordinary count by at
   least two for every multiple of $b$. $\square$

The distinction is consistent with Hutz's Proposition 2.18(2), which
identifies multiplicity one with the absence of eigenvalue one, and
with his Theorem 1.3 allowing additional characteristic-power formal
periods. Those statements do not supply all the higher local lengths.
[Primary publisher PDF](https://nyjm.albany.edu/j/2010/16-8p.pdf).

### Exact missing step for the original CF3 question

Even if a cohomological trace supplies the total intersection length
$L_n$, the required ordinary count is

$$
N_X(n)=L_n-
\sum_{P\in\operatorname{Fix}(f^n)}(\operatorname{length}_P-1).
$$

No all-orbit formula or controlled all-$p$-power recurrence for that
correction sum has been proved here. Tangent eigenvalue orders specify
some possible times of nonreducedness, not the size of the correction.
The original rational/nonrational classification remains unclosed.
No nonrationality inference from strict inequality is valid on its own.

## Increment and remaining risks

CF1 is mathematically complete at this author stage, but its arithmetic
cover reduction is elementary and its analytic closure is the owned
C404 argument with finitely many prime-to-$p$ component-cycle factors
and a holomorphic Weil-error term. We recommend **retain as a complete
classical/owned reconstruction, no independent admission**. We do not
claim that an inspected publication states the literal CF1 formula.

CF2 has direct classical coverage; CF3 has only the stated helper and
an exact unresolved correction tower. Neither is a new full substantial
contract. This author package is internal AI-assisted work, not an
independent proof review or human peer review. No target Euler factor,
root number, automorphy, zero correspondence, or Hilbert–Pólya realization
is established.
