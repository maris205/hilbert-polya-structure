# Focused theorem contract — cyclic substitution collapse

## Audit decision

- **Mathematical status:** `PROVABLE AS STATED` for the finite-field scout;
  the ring extension requires the explicit nonzero-ring normalization below.
- **Research status:** `KILL_INTERNAL_ENGINE_TRANSFER`.
- **External status:** `HOLD_EXTERNAL`.
- This is a theorem audit, not a paper plan.  No paper number is allocated and no novelty or priority claim is made.

The breadth-scout field formulation survives, and in fact extends verbatim to finite commutative coefficient rings.  That extension does not rescue the candidate: after the standard coefficient-pushforward reduction, the entire proof package is a direct specialization of finite linear dynamics over finite rings and transfers almost line-for-line from the internal P115 theorem engine.  The exact formulas below are retained as a closed negative result.

## Assumptions and notation

- Let $A$ be a finite nonzero commutative ring with identity and cardinality $q=|A|\ge 2$.
- Let $m,k\ge 1$ be integers.
- Let
  $$
  \mathcal R_{A,m}=A[X]/(X^m-1).
  $$
  Every class is represented uniquely as $f=\sum_{j=0}^{m-1}a_jX^j$.
- Define the ring endomorphism
  $$
  T_k(f)(X)=f(X^k)\pmod{X^m-1}.
  $$
- For $t\ge0$, set
  $$
  g_t=\gcd(k^t,m).
  $$
- Define the part of $m$ supported on primes dividing $k$ and its coprime complement by
  $$
  m_{\parallel}=\prod_{\substack{\ell\mid m\\ \ell\mid k}}
       \ell^{v_\ell(m)},
  \qquad n=m/m_{\parallel}.
  $$
  Thus $\gcd(k,n)=1$.
- Define
  $$
  h=\max_{\substack{\ell\mid m\\ \ell\mid k}}
      \left\lceil\frac{v_\ell(m)}{v_\ell(k)}\right\rceil,
  $$
  with the empty maximum equal to $0$.
- For every divisor $g\mid m$, let
  $$
  V_g=\left\{\sum_{j=0}^{m-1}b_jX^j:
  b_j=0\text{ whenever }g\nmid j\right\}.
  $$
- The transient depth $\tau(f)$ is the least $t\ge0$ such that $T_k^t(f)$ is periodic.

The notation $q$ means only the ring cardinality.  It is not assumed to be a prime power in the ring version.  When $A=\mathbb F_q$, it has its usual finite-field meaning.

## Zero-contribution reduction

Let $\varphi_k:\mathbb Z/m\mathbb Z\to\mathbb Z/m\mathbb Z$ be multiplication by $k$.  In coefficient coordinates,
$$
(T_k a)_r=\sum_{\substack{j\bmod m\\ kj\equiv r\pmod m}}a_j.
$$
Thus $T_k$ is the additive pushforward along $\varphi_k$: basis vector $e_j$ is sent to $e_{kj}$.  Identifying substitution with this coefficient-fibre merge is standard functorial algebra and receives **zero contribution credit**.  All theorems below begin only after this reduction, but the reduction also exposes why the residual proof is generic.

## Contract T1 — every iterate, image, and target fibre

For every $t\ge0$,
$$
T_k^t(f)(X)=f(X^{k^t})\pmod{X^m-1},
$$
and, coefficientwise,
$$
(T_k^t a)_r=
\sum_{\substack{j\bmod m\\ k^tj\equiv r\pmod m}}a_j.
$$
The image and its cardinality are
$$
\operatorname{im}(T_k^t)=V_{g_t},
\qquad |V_{g_t}|=q^{m/g_t}.
$$
For every target $b\in\mathcal R_{A,m}$,
$$
\#(T_k^t)^{-1}(b)=
\begin{cases}
q^{m-m/g_t},&b\in V_{g_t},\\
0,&b\notin V_{g_t}.
\end{cases}
$$
This includes $t=0$, $m=1$, $k=1$, $k\equiv0\pmod m$, unreachable targets, and coefficient rings with zero divisors.

## Contract T2 — stable image, exact depth census, and sharp height

The gcd staircase satisfies
$$
g_t=\prod_{\ell\mid m}
\ell^{\min\{t\,v_\ell(k),v_\ell(m)\}},
$$
where a prime with $v_\ell(k)=0$ contributes exponent $0$.  Hence
$$
g_t=m_{\parallel}\quad\Longleftrightarrow\quad t\ge h,
$$
and
$$
\bigcap_{t\ge0}\operatorname{im}(T_k^t)
=\operatorname{im}(T_k^h)=V_{m_{\parallel}}.
$$

For every $t\ge0$, the exact cumulative depth census is
$$
D_t:=\#\{f:\tau(f)\le t\}
=q^{m-m/g_t+n}.
$$
With $D_{-1}=0$, the exact depth-$t$ shell has size $D_t-D_{t-1}$.  The sharp maximum depth is
$$
\max_f\tau(f)=h.
$$
If $h>0$, the deepest shell has size
$$
q^m-q^{m-m/g_{h-1}+n}.
$$
Sharpness uses $q\ge2$.  For the excluded zero ring of size one, the unique state has depth zero regardless of the arithmetic value of $h$.

## Contract T3 — final permutation core

Write a core element as
$$
f=\sum_{s=0}^{n-1}b_sX^{m_{\parallel}s}.
$$
On $V_{m_{\parallel}}$, the basis positions evolve by
$$
s\longmapsto ks\pmod n.
$$
Because $\gcd(k,n)=1$, this is a permutation of $\mathbb Z/n\mathbb Z$.  Therefore
$$
\operatorname{Per}(T_k)=V_{m_{\parallel}},
\qquad \#\operatorname{Per}(T_k)=q^n,
$$
and every non-core point is transient.

## Contract T4 — fixed points, cycles, and zeta

Let $c_r$ be the number of cycles of the position permutation
$s\mapsto k^rs$ on $\mathbb Z/n\mathbb Z$.  Then
$$
c_r=\sum_{d\mid n}\frac{\varphi(d)}{\operatorname{ord}_d(k^r)},
$$
where $\operatorname{ord}_1(k^r)=1$.  For every $r\ge1$,
$$
F_r:=\#\operatorname{Fix}(T_k^r)=q^{c_r}.
$$

Set $L=\operatorname{ord}_n(k)$, with $L=1$ when $n=1$.  All state periods divide $L$.  For every $d\mid L$, the exact least-period and cycle counts are
$$
P_d=\sum_{e\mid d}\mu(d/e)F_e,
\qquad C_d=P_d/d.
$$
Thus
$$
\zeta_{T_k}(z)
=\exp\left(\sum_{r\ge1}\frac{F_r}{r}z^r\right)
=\prod_{d\mid L}(1-z^d)^{-C_d}.
$$
These are ordinary finite-map Möbius and zeta conversions and receive zero contribution credit.

## Rejected stronger or false formulations

1. **False:** $\gcd(k,m)$ is already the stable support divisor.  For $(m,k)=(12,6)$, the staircase is $1,6,12,12,\ldots$; the first image contains nonperiodic states.
2. **False:** the height is $\lceil\log_k m_{\parallel}\rceil$.  For $(m,k)=(48,6)$, that scalar logarithm is $3$ but the exact height is $4$.
3. **False:** the height is $\max_{\ell\mid m_{\parallel}}v_\ell(m)$.  For $(m,k)=(16,4)$, the exact height is $2$, not $4$.
4. **False:** every target has the displayed uniform fibre.  Targets outside $V_{g_t}$ have empty fibre.
5. **False:** field rank-nullity is needed.  The fibre calculation uses only the additive group of $A$; for each nonempty congruence block, choosing all but one coefficient freely determines the last.
6. **False:** the number of fixed states is $q$ raised to the number of fixed positions.  It is $q$ raised to the number of cycles of the position permutation.

## Research kill clause

The theorem package is correct but is not retained as a paper candidate.  Its complete engine is:

$$
\text{finite-ring linear map}
\longrightarrow \text{stable image / automorphism core}
\longrightarrow \text{uniform fibres and depth CDF}
\longrightarrow \text{fixed counts / Möbius / zeta}.
$$

That engine is directly established externally for finite linear systems and already instantiated internally in P115 with the same theorem sequence.  P102, P103, P108, P127, and P143 supply further direct component engines.  The only family-specific arithmetic is the elementary valuation formula for $\gcd(k^t,m)$.  Under the stated “direct proof-engine transfer implies KILL” rule, the verdict is final:

**`KILL_INTERNAL_ENGINE_TRANSFER / DO_NOT_DRAFT`**.
