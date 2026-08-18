# Derivation package

## 1. Exact chain census

Every $n\ge1$ has a unique decomposition $n=q^v i$ with $q\nmid i$.
For a fixed $N$, the chain rooted at $i$ has length

$$
\ell_i(N)=1+\left\lfloor\log_q\frac Ni\right\rfloor.
$$

Constraints do not cross chains, hence

$$
Z(N)=\prod_{\substack{1\le i\le N\\q\nmid i}}W_{\ell_i(N)}.
$$

The number of chains of exact length $\ell$ is

$$
C_\ell(N)
=\left\lfloor\frac{N}{q^{\ell-1}}\right\rfloor
-2\left\lfloor\frac{N}{q^\ell}\right\rfloor
+\left\lfloor\frac{N}{q^{\ell+1}}\right\rfloor.
$$

Therefore $Z(N)=\prod_{\ell\ge1}W_\ell^{C_\ell(N)}$; the product is finite.

## 2. One-site increment

Let $v=\nu_q(N)$ and $i=N/q^v$. Before adding $N$, the $i$-chain has length
$v$; after adding it, that chain has length $v+1$. Every other chain is
unchanged. Thus

$$
\frac{Z(N)}{Z(N-1)}=\frac{W_{v+1}}{W_v},
$$

including $v=0$ because $W_0=1$.

## 3. Perron normalization

Primitivity gives positive left/right Perron vectors and a spectral gap. For
some $C>0$, $0<\theta<1$, and integer $m\ge0$,

$$
W_\ell=C\rho^{\ell-1}
\left(1+O(\ell^m\theta^\ell)\right).
$$

Consequently

$$
d_v=c_v-\log\rho=O(v^m\theta^v),
$$

and both $\sum|d_v|$ and $\sum|d_v-d_{v-1}|$ converge.

## 4. Exact mean and remainder

The exact number of $n\le N$ with $\nu_q(n)=v$ is

$$
A_v(N)=\left\lfloor\frac N{q^v}\right\rfloor
-\left\lfloor\frac N{q^{v+1}}\right\rfloor.
$$

Writing $r_v(N)=N\bmod q^v$ gives

$$
A_v(N)
=N\frac{q-1}{q^{v+1}}
-\frac{r_v(N)}{q^v}
+\frac{r_{v+1}(N)}{q^{v+1}}.
$$

Summing $c_vA_v(N)$ and then separating $c_v=\log\rho+d_v$ yields

$$
\log Z(N)=hN+E(N),
$$

$$
E(N)=-\sum_{v\ge1}(d_v-d_{v-1})\frac{r_v(N)}{q^v}.
$$

## 5. Inverse-limit boundary

For $x\in\mathbb Z_q$, replace $r_v(N)$ by the canonical representative
$r_v(x)$. Since $0\le r_v(x)/q^v<1$ and the coefficient differences are
absolutely summable, the resulting series converges uniformly. It defines a
continuous function $E_{A,q}$.

Compactness gives a $q$-adically convergent subsequence of every integer
sequence. Conversely,

$$
N_j=(x\bmod q^j)+q^j
$$

tends to infinity and to $x$ $q$-adically. These two observations give both
inclusions in the accumulation equality.

## 6. Golden coefficient series

For the golden adjacency,

$$
W_\ell=F_{\ell+2},\qquad
d_v=\log\frac{1-r^{v+3}}{1-r^{v+2}},
\qquad r=-\varphi^{-2}.
$$

If $x=\sum\varepsilon_k2^k$, reordering an absolutely convergent double
series gives

$$
E(x)=\sum_{k\ge0}\gamma_k\varepsilon_k,
$$

$$
\gamma_k=-\sum_{v\ge k+1}(d_v-d_{v-1})2^{k-v}.
$$

A geometric summation followed by
$\log(1-u)=-\sum_{m\ge1}u^m/m$ gives

$$
\gamma_k=\sum_{m\ge1}
\frac{(1-r^m)^2}{m(2-r^m)}r^{m(k+2)}.
$$

The exact tail bound and its consequences are proved, not assumed, in
`PROOF_PACKAGE.md`.

## 7. Cantor scales

Strong separation supplies sibling gaps comparable to $t^k$, while
$|\gamma_k|$ and the remaining tail are comparable to $t^k$. Thus level-$n$
cylinders have diameter $\asymp t^n$, mutual separation $\asymp t^n$, and
cardinality $2^n$. Covering and Bernoulli-mass estimates give dimension

$$
\frac{\log2}{-\log t}=\frac{\log2}{2\log\varphi}.
$$

## 8. Radial singularities

Let $\Delta_v=d_v-d_{v-1}$ and

$$
R_Q(z)=\sum_{N\ge0}(N\bmod Q)z^N
=\frac{\sum_{a=0}^{Q-1}az^a}{1-z^Q}.
$$

Then, for $|z|<1$,

$$
G(z)=-\sum_{v\ge1}\frac{\Delta_v}{2^v}R_{2^v}(z).
$$

If $\xi$ is primitive of order $2^v$, every level $w\ge v$ has the same
normalized radial limit

$$
\lim_{r\uparrow1}(1-r)R_{2^w}(r\xi)=-\frac1{1-\xi}.
$$

Therefore

$$
\lim_{r\uparrow1}(1-r)G(r\xi)
=\frac{1}{1-\xi}\sum_{w\ge v}\frac{\Delta_w}{2^w}
=-\frac{\gamma_{v-1}}{2^{v-1}(1-\xi)}\ne0.
$$

The primitive dyadic roots are dense, so analytic continuation across any
unit-circle point is impossible.

## 9. Ownership and scope derivation

The chain product, entropy, and leading dimensions are derivation inputs and
receive zero novelty credit. The ordinary generating function is not a
determinant. The natural-boundary result is a secondary consequence of the
same $\gamma$ coefficients. Ordinary Minkowski content remains outside the
claim because continuous covering scales were not analyzed.

