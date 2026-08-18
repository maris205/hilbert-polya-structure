# Proof package

## Claim

### Theorem A: exact q-adic finite-size boundary law

Let $q\ge2$ and let $A$ be a finite primitive zero-one matrix. Define
$X_A^{(q)}$, $Z(N)$, $W_\ell$, $c_v$, $d_v$, and $h$ exactly as in
`SOURCE_LOCK.md`. Then, for every $N\ge1$,

$$
\log Z(N)-\log Z(N-1)=c_{\nu_q(N)},
$$

and

$$
\log Z(N)-hN
=-\sum_{v\ge1}(d_v-d_{v-1})
  \frac{N\bmod q^v}{q^v}.
$$

The same series, with $N\bmod q^v$ replaced by the canonical coordinate
$x\bmod q^v$, converges uniformly on $\mathbb Z_q$ to a continuous map
$E_{A,q}:\mathbb Z_q\to\mathbb R$. Moreover,

$$
\operatorname{Acc}_{N\to\infty}(\log Z(N)-hN)
=E_{A,q}(\mathbb Z_q),
$$

and

$$
\operatorname{Acc}_{N\to\infty}(Z(N)e^{-hN})
=\exp(E_{A,q}(\mathbb Z_q)).
$$

### Theorem B: golden boundary Cantor geometry

For

$$
q=2,
\qquad
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},
$$

write $\varphi=(1+\sqrt5)/2$, $t=\varphi^{-2}$, and $r=-t$. Every
$x\in\mathbb Z_2$ has a unique expansion
$x=\sum_{k\ge0}\varepsilon_k2^k$ with $\varepsilon_k\in\{0,1\}$, and

$$
E_{A,2}(x)=\sum_{k\ge0}\gamma_k\varepsilon_k.
$$

The coefficients satisfy

$$
\operatorname{sgn}(\gamma_k)=(-1)^k,
\qquad
|\gamma_k|>\sum_{j>k}|\gamma_j|,
\qquad
\frac{\gamma_{k+1}}{\gamma_k}\longrightarrow-\varphi^{-2}.
$$

Consequently $E_{A,2}(\mathbb Z_2)$ is a Cantor set and

$$
\dim_H E_{A,2}(\mathbb Z_2)
=\dim_B E_{A,2}(\mathbb Z_2)
=\frac{\log2}{2\log\varphi}.
$$

### Theorem C: dense radial singularities

In the same golden case, write $E(N)=\log Z(N)-hN$ for $N\ge1$, set
$E(0)=0$, and

$$
G(z)=\sum_{N\ge0}E(N)z^N.
$$

If $\xi$ is a primitive $2^v$-th root of unity, $v\ge1$, then

$$
\lim_{r_0\uparrow1}(1-r_0)G(r_0\xi)
=-\frac{\gamma_{v-1}}{2^{v-1}(1-\xi)}\ne0.
$$

The unit circle is therefore a natural boundary for $G$.

## Status

`LOCAL PROOF COMPLETE / PROVABLE AS STATED` for Theorems A--C under the
frozen assumptions. This is an unreviewed proof classification inside a
preauthority candidate, not a claimed published or experimentally validated
result.

Ordinary Minkowski-content nonexistence is not part of the claim and is
classified `NOT_CURRENTLY_JUSTIFIED` by this package.

## Assumptions

1. $q$ is an integer with $q\ge2$.
2. $A$ is a finite primitive matrix with entries in $\{0,1\}$.
3. Prefixes are indexed by $\{1,\ldots,N\}$ and contain only constraints
   whose endpoints both lie in that set.
4. $\nu_q(N)=\max\{v\ge0:q^v\mid N\}$.
5. Logarithms are real logarithms.
6. $\mathbb Z_q$ is the inverse limit of $\mathbb Z/q^v\mathbb Z$; $q$ need
   not be prime.
7. Theorems B and C use only the stated binary golden adjacency.

No irreducible-periodic, reducible, countable-state, higher-step, or
continuous-scale covering theorem is inferred.

## Notation

- $\rho=\rho(A)$ is the Perron eigenvalue.
- $r_v(N)=N\bmod q^v$ and $r_v(x)=x\bmod q^v$ are canonical representatives
  in $\{0,\ldots,q^v-1\}$.
- $\Delta_v=d_v-d_{v-1}$ for $v\ge1$.
- `Acc` means subsequential limits along integer cutoffs tending to infinity.
- In the golden proof, $F_0=0,F_1=1$.

## Proof strategy

Theorem A is proved by an exact chain partition, a Perron spectral-gap
estimate, and summation by parts in the valuation census. Uniform convergence
then turns the finite remainder into an inverse-limit function, and explicit
representatives prove surjectivity onto every accumulation value.

Theorem B is proved by converting Binet's formula to a positive-coefficient
series in the negative contraction $r=-\varphi^{-2}$. One exact algebraic
bound controls all higher modes and all future digit tails simultaneously.
Cylinder separation gives topology and box dimension; a Bernoulli measure
gives the Hausdorff lower bound.

Theorem C rewrites the ordinary generating function as an absolutely
convergent sum of rational residue functions. A dominated radial limit at
each primitive dyadic root is exactly a nonzero tail of the coefficients from
Theorem B.

## Dependency map

1. The exact increment depends only on Lemmas 1--2.
2. The uniformly convergent remainder depends on Lemmas 3--5.
3. The complete accumulation equality depends on Lemma 6 in both directions.
4. The golden digit expansion depends on Lemmas 7--8.
5. Strong separation depends on the exact scalar estimate in Lemma 9.
6. Cantor topology and dimension depend on Lemmas 10--11.
7. The radial formula and natural boundary depend on Lemmas 12--14.

## Proof

### Lemma 1: exact chain partition and product

Every integer $n\ge1$ has a unique representation

$$
n=q^v i,\qquad v=\nu_q(n),\qquad q\nmid i.
$$

For every root $i$ with $q\nmid i$, define its truncated chain

$$
\mathcal C_i(N)=\{i,qi,\ldots,q^{\ell_i-1}i\},
$$

where $\ell_i$ is maximal subject to $q^{\ell_i-1}i\le N$. Uniqueness of the
representation shows that the nonempty $\mathcal C_i(N)$ partition
$\{1,\ldots,N\}$.

The only constraints involving a coordinate $q^j i$ join it to
$q^{j+1}i$, so constraints do not cross chains. A chain of length $\ell$
admits exactly

$$
\mathbf1^TA^{\ell-1}\mathbf1=W_\ell
$$

labelings. Independence of disjoint coordinate sets gives

$$
Z(N)=\prod_{\substack{1\le i\le N\\q\nmid i}}W_{\ell_i(N)}.
$$

This is an exact integer identity. $\square$

### Lemma 2: exact one-site increment

Let $v=\nu_q(N)$ and $i=N/q^v$. The site $N$ is the $(v+1)$-st vertex of
the $i$-chain. At cutoff $N-1$, that chain has exactly the preceding $v$
vertices. All other chains have the same vertices at cutoffs $N-1$ and $N$.
Lemma 1 therefore gives

$$
\frac{Z(N)}{Z(N-1)}=\frac{W_{v+1}}{W_v}.
$$

When $v=0$, a new one-vertex chain is created and the formula uses
$W_0=1$. Taking logarithms proves the increment assertion. $\square$

### Lemma 3: Perron decay of $d_v$

Because $A$ is primitive, the Perron--Frobenius theorem gives a simple
eigenvalue $\rho>0$ with positive right and left eigenvectors $u,w$, and
every other eigenvalue has modulus strictly smaller than $\rho$. Normalize
$w^Tu=1$. The finite-dimensional Jordan decomposition gives constants
$C_0>0$, $C_1>0$, an integer $m\ge0$, and $0<\theta<1$ such that

$$
W_\ell
=(\mathbf1^Tu)(w^T\mathbf1)\rho^{\ell-1}
+O(C_1\ell^m(\theta\rho)^\ell).
$$

The leading coefficient is positive. After dividing by it and by
$\rho^{\ell-1}$,

$$
W_\ell=C_0\rho^{\ell-1}
\left(1+O(\ell^m\theta^\ell)\right).
$$

For all sufficiently large $\ell$ the relative error has modulus below
$1/2$, so applying the Lipschitz bound for $\log(1+y)$ on
$[-1/2,1/2]$ gives

$$
c_v=\log\rho+O(v^m\theta^v).
$$

Changing finitely many initial terms does not affect summability. Hence

$$
\sum_{v\ge0}|d_v|<\infty,
\qquad
\sum_{v\ge1}|d_v-d_{v-1}|<\infty.
$$

$\square$

### Lemma 4: exact valuation census

For $v\ge0$, the number of $n\le N$ with $\nu_q(n)=v$ is

$$
A_v(N)=\left\lfloor\frac N{q^v}\right\rfloor
-\left\lfloor\frac N{q^{v+1}}\right\rfloor.
$$

Since

$$
\left\lfloor\frac N{q^v}\right\rfloor
=\frac{N-r_v(N)}{q^v},
$$

we have the exact identity

$$
A_v(N)
=N\frac{q-1}{q^{v+1}}
-\frac{r_v(N)}{q^v}
+\frac{r_{v+1}(N)}{q^{v+1}}.
$$

$\square$

### Lemma 5: exact remainder formula and uniform extension

Summing Lemma 2 over $1\le n\le N$ and grouping by valuations gives

$$
\log Z(N)=\sum_{v\ge0}c_vA_v(N).
$$

The sum is finite at fixed $N$. Write $c_v=\log\rho+d_v$. Since
$\sum_vA_v(N)=N$ and

$$
\sum_{v\ge0}\frac{q-1}{q^{v+1}}=1,
$$

the proposed entropy is

$$
h=\log\rho+
\sum_{v\ge0}\frac{q-1}{q^{v+1}}d_v.
$$

The latter series is absolutely convergent by Lemma 3. Substituting Lemma 4
and subtracting $hN$ yields

$$
\begin{aligned}
\log Z(N)-hN
&=\sum_{v\ge0}d_v
\left(-\frac{r_v(N)}{q^v}
+\frac{r_{v+1}(N)}{q^{v+1}}\right)\\
&=-\sum_{v\ge1}(d_v-d_{v-1})
\frac{r_v(N)}{q^v},
\end{aligned}
$$

where $r_0(N)=0$ and the second equality is an index shift justified by
absolute convergence.

For $x\in\mathbb Z_q$, every $r_v(x)$ is locally constant and
$0\le r_v(x)/q^v<1$. Lemma 3 gives the uniform majorant

$$
\sum_{v\ge1}|d_v-d_{v-1}|.
$$

The Weierstrass M-test therefore gives uniform convergence on $\mathbb Z_q$.
Uniform limits of continuous real-valued functions are continuous, so the
series defines $E_{A,q}$. $\square$

### Lemma 6: complete accumulation image

First take a convergent subsequence of real remainders
$E(N_j)\to y$ with $N_j\to\infty$. Compactness of $\mathbb Z_q$ gives a
further subsequence, still denoted $N_j$, converging $q$-adically to some
$x\in\mathbb Z_q$. Lemma 5 and continuity give

$$
y=\lim_jE(N_j)=E_{A,q}(x).
$$

Thus every accumulation value lies in the image.

Conversely, fix $x\in\mathbb Z_q$ and set

$$
N_j=r_j(x)+q^j.
$$

Then $N_j\ge q^j\to\infty$. For every fixed $v$ and every $j\ge v$,

$$
N_j\equiv r_j(x)\equiv r_v(x)\pmod{q^v},
$$

so $N_j\to x$ in $\mathbb Z_q$. Continuity gives
$E(N_j)\to E_{A,q}(x)$. This proves the reverse inclusion.

The exponential is continuous and injective on $\mathbb R$, so applying it
to convergent subsequences gives the normalized-count equality. $\square$

### Lemma 7: golden Binet normalization

For the golden adjacency, the number of admissible words satisfies the
Fibonacci recurrence with $W_1=2$ and $W_2=3$. Hence

$$
W_\ell=F_{\ell+2}.
$$

Binet's formula can be written as

$$
F_n=\frac{\varphi^n}{\sqrt5}(1-r^n),
\qquad r=-\varphi^{-2}.
$$

Therefore

$$
\frac{W_{v+1}}{W_v}
=\varphi\frac{1-r^{v+3}}{1-r^{v+2}},
$$

and

$$
d_v=\log\frac{1-r^{v+3}}{1-r^{v+2}}.
$$

$\square$

### Lemma 8: exact golden digit coefficients

Write $x=\sum_{k\ge0}\varepsilon_k2^k$. Then

$$
r_v(x)=\sum_{k=0}^{v-1}\varepsilon_k2^k.
$$

The double series obtained by substituting this into Lemma 5 is absolutely
convergent because

$$
\sum_{v\ge1}|\Delta_v|2^{-v}
\sum_{k=0}^{v-1}2^k
\le\sum_{v\ge1}|\Delta_v|.
$$

Thus it may be reordered, giving

$$
E(x)=\sum_{k\ge0}\gamma_k\varepsilon_k,
\qquad
\gamma_k=-\sum_{v\ge k+1}\Delta_v2^{k-v}.
$$

Let

$$
B_k=\sum_{j\ge1}\frac{d_{k+j}}{2^j}.
$$

An index shift gives

$$
\gamma_k=\frac12(d_k-B_k).
$$

Since $|r|<1$, the expansion
$\log(1-u)=-\sum_{m\ge1}u^m/m$ is absolutely convergent at every power of
$r$. Lemma 7 yields

$$
d_k=\sum_{m\ge1}\frac{1-r^m}{m}r^{m(k+2)}.
$$

For each $m$,

$$
\sum_{j\ge1}\frac{r^{mj}}{2^j}=\frac{r^m}{2-r^m}.
$$

Absolute convergence permits summation in either order. Hence

$$
\boxed{
\gamma_k=\sum_{m\ge1}a_mr^{m(k+2)},
\qquad
a_m=\frac{(1-r^m)^2}{m(2-r^m)}>0.}
$$

$\square$

### Lemma 9: exact all-level strong-separation estimate

Put $t=-r=(3-\sqrt5)/2$. Then $0<t<1/2$ and

$$
t^2-3t+1=0.
$$

For $m\ge2$,

$$
|1-r^m|\le1+t^m\le1+t^2,
$$

and

$$
2-r^m\ge2-t^2.
$$

Therefore

$$
a_m\le\frac{K}{m},
\qquad
K=\frac{(1+t^2)^2}{2-t^2}=-6+3\sqrt5.
$$

Define

$$
S=\sum_{m\ge2}\frac{a_mt^{2m}}{1-t^m}.
$$

Since $1/(1-t^m)\le1/(1-t^2)$ and $1/m\le1/2$ for $m\ge2$,

$$
\begin{aligned}
S
&\le\frac{K}{1-t^2}\sum_{m\ge2}\frac{t^{2m}}m\\
&\le\frac{Kt^4}{2(1-t^2)^2}\\
&=\frac{-87+39\sqrt5}{20}.
\end{aligned}
$$

Also

$$
a_1t^3=\frac{280-125\sqrt5}{11}.
$$

Their difference is

$$
a_1t^3-\frac{Kt^4}{2(1-t^2)^2}
=\frac{6557-2929\sqrt5}{220}>0.
$$

The last inequality is exact: both terms before comparison are positive and

$$
6557^2-5\cdot2929^2=99044>0.
$$

Consequently

$$
S<a_1t^3. \tag{1}
$$

Separate the first mode in Lemma 8:

$$
\gamma_k=a_1r^{k+2}+R_k,
\qquad
R_k=\sum_{m\ge2}a_mr^{m(k+2)}.
$$

For every $k\ge0$,

$$
\begin{aligned}
|R_k|+\sum_{j>k}|R_j|
&\le\sum_{m\ge2}
\frac{a_mt^{m(k+2)}}{1-t^m}\\
&\le t^kS\\
&<a_1t^{k+3},
\end{aligned}
$$

where $t^{mk}\le t^k$ for $m\ge2$. In particular
$|R_k|<a_1t^{k+2}$, so $\gamma_k$ has the sign of $r^{k+2}$, namely
$(-1)^k$.

For the first modes alone,

$$
\begin{aligned}
a_1t^{k+2}-\sum_{j>k}a_1t^{j+2}
&=a_1t^{k+2}\frac{1-2t}{1-t}\\
&=a_1t^{k+3},
\end{aligned}
$$

because $1-2t=t(1-t)$ follows from $t^2-3t+1=0$. Subtracting the total
higher-mode error and using (1) proves

$$
|\gamma_k|-\sum_{j>k}|\gamma_j|>0.
$$

Finally,

$$
\frac{R_k}{a_1r^{k+2}}\longrightarrow0
$$

by the geometric factor $t^{(m-1)(k+2)}$ in every $m\ge2$ term and the
same summable majorant. Hence

$$
\frac{\gamma_{k+1}}{\gamma_k}\longrightarrow r=-\varphi^{-2}.
$$

$\square$

### Lemma 10: Cantor topology

Let

$$
K=E_{A,2}(\mathbb Z_2)
=\left\{\sum_{k\ge0}\varepsilon_k\gamma_k:
\varepsilon_k\in\{0,1\}\right\}.
$$

If two digit sequences first differ at position $k$, Lemma 9 gives

$$
\left|\sum_{j\ge0}(\varepsilon_j-\varepsilon_j')\gamma_j\right|
\ge |\gamma_k|-\sum_{j>k}|\gamma_j|>0.
$$

Thus the digit map is injective. It is continuous by absolute convergence.
Since $\mathbb Z_2$ is compact and $\mathbb R$ is Hausdorff, it is a
homeomorphism onto $K$. The space $\mathbb Z_2$ is compact, perfect, and
totally disconnected, so $K$ is a Cantor set. $\square$

### Lemma 11: exact Hausdorff and box dimensions

Lemma 9 and the ratio limit give constants $b_1,b_2>0$ such that

$$
b_1t^k\le|\gamma_k|\le b_2t^k
$$

for all $k\ge0$, after reducing $b_1$ and enlarging $b_2$ to absorb finitely
many initial terms. Hence the tail diameter

$$
T_n=\sum_{k\ge n}|\gamma_k|
$$

satisfies $T_n\le C_2t^n$.

The proof of Lemma 9 gives the uniform sibling-gap bound

$$
g_k=|\gamma_k|-\sum_{j>k}|\gamma_j|
\ge C_1t^k,
$$

where $C_1=a_1t^3-S>0$. A level-$n$ cylinder fixes digits
$0,\ldots,n-1$ and has diameter at most $C_2t^n$. Two different level-$n$
cylinders first differ at some $k<n$, so their mutual distance is at least
$C_1t^k\ge C_1t^{n-1}$.

Let

$$
s_0=\frac{\log2}{-\log t}.
$$

There are $2^n$ level-$n$ cylinders. For every $s>s_0$ they give covers
whose total $s$-content is at most

$$
2^n(C_2t^n)^s=C_2^s(2t^s)^n\longrightarrow0.
$$

Thus $\dim_HK\le s_0$ and the upper box dimension is at most $s_0$.

For the reverse inequality, push the fair Bernoulli measure on
$\{0,1\}^{\mathbb N}$ to a probability measure $\mu$ on $K$. Every level-$n$
cylinder has mass $2^{-n}$. Choose $n$ so that

$$
t^{n+1}<R\le t^n.
$$

The level-$n$ separation and diameter bounds imply that an interval of radius
$R$ intersects at most a constant number $M$ of level-$n$ cylinders; $M$ is
independent of $n$ and $R$. Therefore

$$
\mu(I)\le M2^{-n}
=M(t^n)^{s_0}
\le Mt^{-s_0}R^{s_0}.
$$

The mass-distribution principle gives $\dim_HK\ge s_0$. The same separation
forces any cover at scale comparable to $t^n$ to use at least a fixed
multiple of $2^n$ sets, so the lower box dimension is at least $s_0$.

Since $t=\varphi^{-2}$,

$$
s_0=\frac{\log2}{2\log\varphi}.
$$

$\square$

### Lemma 12: rational residue generating functions

For an integer $Q\ge2$ and $|z|<1$, periodicity gives

$$
R_Q(z):=\sum_{N\ge0}(N\bmod Q)z^N
=\frac{P_Q(z)}{1-z^Q},
$$

where

$$
P_Q(z)=\sum_{a=0}^{Q-1}az^a.
$$

Lemma 5 and absolute convergence permit interchange of the $N$ and $v$ sums:

$$
G(z)=-\sum_{v\ge1}\frac{\Delta_v}{2^v}R_{2^v}(z).
$$

Indeed, $(N\bmod2^v)/2^v\le1$ and
$\sum_v|\Delta_v|<\infty$. $\square$

### Lemma 13: exact radial coefficient

Let $\xi$ be primitive of order $2^v$, $v\ge1$. For $w<v$,
$1-\xi^{2^w}\ne0$, so

$$
\lim_{r_0\uparrow1}(1-r_0)R_{2^w}(r_0\xi)=0.
$$

For $w\ge v$, set $Q=2^w$. Then $\xi^Q=1$ and $\xi\ne1$. Differentiating
the finite geometric sum, or evaluating its elementary closed form, gives

$$
P_Q(\xi)=-\frac{Q}{1-\xi}.
$$

Also

$$
1-r_0^Q\sim Q(1-r_0).
$$

Therefore

$$
\lim_{r_0\uparrow1}(1-r_0)R_Q(r_0\xi)
=-\frac1{1-\xi}.
$$

The infinite sum may be passed through this limit. In fact,

$$
\frac{1-r_0}{Q}|R_Q(r_0\xi)|
\le\frac{1-r_0}{Q}\sum_{N\ge0}Q r_0^N=1,
$$

so the level-$w$ contribution is dominated by $|\Delta_w|$, a summable
sequence. Dominated convergence and Lemma 12 yield

$$
\lim_{r_0\uparrow1}(1-r_0)G(r_0\xi)
=\frac1{1-\xi}\sum_{w\ge v}\frac{\Delta_w}{2^w}.
$$

From the definition in Lemma 8,

$$
\gamma_{v-1}
=-\sum_{w\ge v}\Delta_w2^{v-1-w},
$$

so

$$
\sum_{w\ge v}\frac{\Delta_w}{2^w}
=-\frac{\gamma_{v-1}}{2^{v-1}}.
$$

Lemma 9 proves this is nonzero. The asserted radial formula follows.
$\square$

### Lemma 14: natural boundary

Lemma 5 shows that $E(N)$ is bounded, so the power series for $G$ is analytic
on $|z|<1$. Lemma 13 gives an unbounded radial approach at every primitive
dyadic root of unity. The union of these roots is dense in the unit circle.

Suppose $G$ admitted analytic continuation across some unit-circle point.
The continuation domain would contain an open boundary arc. That arc
contains a primitive dyadic root $\xi$. By the identity theorem, the
continuation agrees with $G$ in the portion of its neighborhood inside the
unit disk and therefore has a finite limit as $r_0\xi\to\xi$. This
contradicts Lemma 13. Hence no point of the unit circle admits analytic
continuation, and the unit circle is a natural boundary. $\square$

### Completion of the proof

Lemmas 1--6 prove Theorem A. Lemmas 7--11 prove Theorem B. Lemmas 12--14
prove Theorem C. $\square$

## Corrections or missing assumptions

- The primitive hypothesis is explicit and essential to the supplied Perron
  decay proof. Some nonprimitive matrices may satisfy variants, but no such
  extension is included.
- The natural-boundary points are called radial pole-type singularities, not
  isolated meromorphic poles.
- The ordinary Minkowski-content statement from an early idea draft is
  removed. Dyadic/integer-cutoff accumulation does not control every real
  covering scale.
- The chain product, entropy, and leading dimensions are retained only as
  cited inputs and exact controls.
- The Phase-2 prose proportionality involving $\xi/(1-\xi)$ is superseded by
  the exact Lemma-13 Abelian coefficient $-1/(1-\xi)$. This normalization
  correction does not change nonvanishing or the natural-boundary conclusion.

## Open risks

1. **Literature risk:** an exact same-object finite-size theorem may exist
   under digital-sum, renewal, or boundary-pressure terminology not reached
   by the bounded search. This is a `STOP_DUPLICATE` risk, not a proof gap.
2. **Presentation risk:** a reader may confuse $\mathbb Z_q$ for composite
   $q$ with a field or confuse the real-valued series with $q$-adic analysis.
   The type contract must remain explicit.
3. **Scope risk:** continuous-scale Minkowski content must remain excluded
   unless a separate theorem is proved and reviewed.
4. **Independence risk:** the two evaluators are plans until separately
   implemented and sealed; no agreement result is claimed in this package.
