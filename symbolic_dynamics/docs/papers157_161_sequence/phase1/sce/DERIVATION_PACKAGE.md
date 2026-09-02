# Derivation package — cyclic substitution collapse

## Target

For the finite self-map
$$
T_k:A[X]/(X^m-1)\longrightarrow A[X]/(X^m-1),
\qquad T_k(f)=f(X^k),
$$
derive, for every time $t\ge0$:

1. the literal iterate and coefficient rule;
2. the exact image and the fibre over every target, including empty fibres;
3. the stable image, periodic core, depth CDF, every depth shell, and sharp
   maximum depth;
4. all iterate-fixed counts, least-period counts, cycles, and the finite zeta
   product;
5. all ring and arithmetic boundary conditions relevant to those statements.

The derivation is retained as a closed audit result.  It is not a manuscript
seed and makes no novelty or priority claim.

## Status

- **Mathematics:** `COHERENT AFTER REFRAMING`.
- **Research disposition:** `KILL_INTERNAL_ENGINE_TRANSFER`.
- **External state:** `HOLD_EXTERNAL`.

The normalization is that $A$ is a finite nonzero commutative unital ring,
$q=|A|\ge2$, and $m,k\ge1$.  No field hypothesis is needed.  Conversely,
the zero ring must be excluded from the sharp-height assertion.

## Invariant Object

The useful invariant is not polynomial factorization.  It is the image
staircase of multiplication maps on the exponent group:
$$
\varphi_{k^t}:\mathbb Z/m\mathbb Z\longrightarrow\mathbb Z/m\mathbb Z,
\qquad j\longmapsto k^tj.
$$
Its image is the subgroup $g_t\mathbb Z/m\mathbb Z$, where
$g_t=\gcd(k^t,m)$, and every point of that subgroup has exactly $g_t$
preimages.  The polynomial map is the additive coefficient pushforward along
this finite-set map.

This identification is standard and earns zero contribution credit.  It is
also the reason the candidate fails the research gate: once it is made, only
generic finite-linear stable-image machinery and elementary valuations remain.

## Assumptions

1. $A$ is a finite nonzero commutative ring with identity.
2. $q=|A|\ge2$.
3. $m,k$ are positive integers.
4. $X$ is central, and the quotient is by the monic polynomial $X^m-1$.
5. Depth means first entry into the periodic set, not first repetition of an
   arbitrary forward orbit value.

The monic divisor gives every quotient class a unique coefficient vector
$(a_0,\ldots,a_{m-1})\in A^m$.  Substitution descends to the quotient because
$X^{km}-1$ is divisible by $X^m-1$.

## Notation

Set
$$
g_t=\gcd(k^t,m),
\qquad
m_{\parallel}=\prod_{\substack{\ell\mid m\\\ell\mid k}}
\ell^{v_\ell(m)},
\qquad n=\frac{m}{m_{\parallel}}.
$$
Then $\gcd(k,n)=1$.  Put
$$
h=\max_{\substack{\ell\mid m\\\ell\mid k}}
\left\lceil\frac{v_\ell(m)}{v_\ell(k)}\right\rceil,
$$
with empty maximum $0$.  For $g\mid m$, define the support module
$$
V_g=\{b\in A^m:b_r=0\text{ when }g\nmid r\}.
$$
It has $m/g$ free coordinates and hence cardinality $q^{m/g}$.

For a state $a$, let
$$
\tau(a)=\min\{t\ge0:T_k^t(a)\text{ is periodic}\}.
$$

## Derivation Strategy

The argument has four layers:

1. follow each basis coefficient under exponent multiplication;
2. solve the resulting linear congruence and count independent block-sum
   maps over the additive group of $A$;
3. read stabilization prime by prime and identify the surviving restriction
   as a coordinate permutation;
4. count configurations fixed by powers of that coordinate permutation, then
   apply finite-map Möbius inversion.

No semisimplicity, Fourier transform, Chinese-remainder factorization of
$X^m-1$, division in $A$, or field rank-nullity is used.

## Derivation Map

$$
T_k(e_j)=e_{kj}
\Longrightarrow
T_k^t(e_j)=e_{k^tj}
\Longrightarrow
\begin{cases}
\operatorname{im}T_k^t=V_{g_t},\\
\text{uniform nonempty fibres}
\end{cases}
$$
$$
g_t\nearrow m_{\parallel}
\Longrightarrow
V_{g_t}\searrow V_{m_{\parallel}}
\Longrightarrow
\begin{cases}
\operatorname{Per}(T_k)=V_{m_{\parallel}},\\
\text{depth CDF and height }h,
\end{cases}
$$
$$
T_k|_{V_{m_{\parallel}}}\cong(s\mapsto ks\bmod n)
\Longrightarrow
F_r=q^{c_r}
\Longrightarrow
\{P_d,C_d\}_{d\mid L}
\Longrightarrow
\zeta_{T_k}.
$$

## Main Derivation

### 1. Coefficient pushforward and arbitrary iterates

Let $e_j=X^j$ for $0\le j<m$, with exponents read modulo $m$.  Directly,
$$
T_k(e_j)=e_{kj\bmod m}.
$$
Iteration therefore gives
$$
T_k^t(e_j)=e_{k^tj\bmod m},
$$
including $t=0$.  By additivity, if $a=(a_j)_{j\bmod m}$, then the output
coefficient at $r$ is
$$
(T_k^ta)_r=
\sum_{\substack{j\bmod m\\k^tj\equiv r\pmod m}}a_j.
$$
Equivalently,
$$
T_k^t(f)(X)=f(X^{k^t})\pmod{X^m-1}.
$$

This is exactly additive pushforward along $\varphi_{k^t}$; recognizing it
is a standard reduction and contributes no research claim.

### 2. Congruence geometry, image, and every target fibre

The congruence
$$
k^tj\equiv r\pmod m
$$
is solvable exactly when $g_t\mid r$.  When it is solvable, it has exactly
$g_t$ solutions modulo $m$.  Consequently:

- the reachable exponent positions are precisely the multiples of $g_t$;
- the $m/g_t$ nonempty source blocks each contain $g_t$ input coordinates;
- those blocks partition all $m$ source coordinates.

For one block, the output map is
$$
\Sigma:A^{g_t}\longrightarrow A,
\qquad (x_1,\ldots,x_{g_t})\longmapsto x_1+\cdots+x_{g_t}.
$$
It is surjective: choose $x_1=y$ and all other entries zero.  For a prescribed
$y$, choose $x_1,\ldots,x_{g_t-1}$ freely and force
$$
x_{g_t}=y-(x_1+\cdots+x_{g_t-1}).
$$
Thus every block fibre has $q^{g_t-1}$ elements.  Since the blocks are
independent,
$$
\operatorname{im}(T_k^t)=V_{g_t},
\qquad
|\operatorname{im}(T_k^t)|=q^{m/g_t},
$$
and, for every target $b\in A^m$,
$$
\#(T_k^t)^{-1}(b)=
\begin{cases}
q^{(g_t-1)m/g_t}=q^{m-m/g_t},&b\in V_{g_t},\\
0,&b\notin V_{g_t}.
\end{cases}
$$

This proof uses only addition, additive inverses, and $|A|=q$.  It remains
valid for rings with zero divisors such as $\mathbb Z/4\mathbb Z$ and
$\mathbb Z/6\mathbb Z$.  Indeed, after the coordinate model is defined, it
works for an arbitrary finite abelian coefficient group.  That further
extension weakens, rather than strengthens, the candidate's originality.

### 3. Primewise image staircase and exact stabilization

Write $a_\ell=v_\ell(m)$ and $b_\ell=v_\ell(k)$.  Then
$$
v_\ell(g_t)=\min\{t b_\ell,a_\ell\},
$$
so
$$
g_t=\prod_{\ell\mid m}
\ell^{\min\{t\,v_\ell(k),v_\ell(m)\}}.
$$
If $b_\ell=0$, that prime never appears in $g_t$.  If $b_\ell>0$, its
exponent first reaches $a_\ell$ at
$\lceil a_\ell/b_\ell\rceil$.  Hence
$$
g_t=m_{\parallel}\quad\Longleftrightarrow\quad t\ge h.
$$
Since $g_t\mid g_{t+1}$, the image modules form a descending chain, and
$$
\bigcap_{t\ge0}\operatorname{im}(T_k^t)
=\operatorname{im}(T_k^h)=V_{m_{\parallel}}.
$$

This calculation also exposes two unsafe shortcuts.  The one-step value
$\gcd(k,m)$ need not be stable, and a scalar logarithm ignores unequal
$\ell$-adic speeds.  Concrete failures are recorded below.

### 4. The stable image is exactly the permutation core

Every element of $V_{m_{\parallel}}$ has a unique form
$$
\sum_{s=0}^{n-1}b_sX^{m_{\parallel}s}.
$$
On its basis positions,
$$
m_{\parallel}s\longmapsto km_{\parallel}s
=m_{\parallel}(ks)\pmod m.
$$
Thus the restriction of $T_k$ to the stable image is the coordinate
permutation induced by
$$
s\longmapsto ks\pmod n.
$$
It is a permutation because $\gcd(k,n)=1$.  Every core state is therefore
periodic.

Conversely, if $a$ is periodic of period $r$, then for every $t$ one can
choose a multiple $ur\ge t$ and write
$$
a=T_k^{ur}(a)=T_k^t\bigl(T_k^{ur-t}(a)\bigr).
$$
Hence a periodic state lies in every iterated image and therefore in
$V_{m_{\parallel}}$.  We obtain
$$
\operatorname{Per}(T_k)=V_{m_{\parallel}},
\qquad
\#\operatorname{Per}(T_k)=q^n.
$$

### 5. Exact depth CDF, shells, and sharp height

A state has depth at most $t$ precisely when its $t$th image is in the
periodic core:
$$
\tau(a)\le t\quad\Longleftrightarrow\quad
T_k^t(a)\in V_{m_{\parallel}}.
$$
Because $g_t\mid m_{\parallel}$, every one of the $q^n$ core targets lies in
$V_{g_t}$ and has the same $t$-fibre found above.  Therefore
$$
D_t:=\#\{a:\tau(a)\le t\}
=q^nq^{m-m/g_t}
=q^{m-m/g_t+n}.
$$
With $D_{-1}=0$, the exact depth-$t$ shell is
$$
D_t-D_{t-1}.
$$

At $t=h$, $g_h=m_{\parallel}$ and therefore $D_h=q^m$: every state has
entered the core.  If $t<h$, then $g_t<m_{\parallel}$, so
$m/g_t>m/m_{\parallel}=n$.  Because $q\ge2$,
$$
D_t=q^{m-m/g_t+n}<q^m.
$$
Some state has not entered the core.  Thus the maximum depth is sharply
$$
\max_a\tau(a)=h.
$$
For $h>0$, the deepest shell is
$$
D_h-D_{h-1}
=q^m-q^{m-m/g_{h-1}+n}.
$$

### 6. Fixed configurations on the core

Let $\pi_r$ be multiplication by $k^r$ on $\mathbb Z/n\mathbb Z$.  A
coefficient vector is fixed by the induced coordinate permutation exactly
when its entries are constant around each cycle of $\pi_r$.  If $c_r$ is
the number of those position cycles, then there are independently $q$
choices per cycle, so
$$
F_r:=\#\operatorname{Fix}(T_k^r)=q^{c_r}.
$$

To compute $c_r$, stratify positions by their additive order $d\mid n$.
There are $\varphi(d)$ such positions.  On that stratum, multiplication by
$k^r$ has orbit length $\operatorname{ord}_d(k^r)$, because $k$ is a unit
modulo every divisor of $n$.  Therefore
$$
c_r=\sum_{d\mid n}
\frac{\varphi(d)}{\operatorname{ord}_d(k^r)},
$$
with $\operatorname{ord}_1(k^r)=1$.

The exponent is the number of position cycles, not the number of fixed
positions.  This distinction is necessary already for nontrivial coordinate
transpositions.

### 7. Least periods, cycles, and zeta

Let
$$
L=\operatorname{ord}_n(k),
$$
with $L=1$ for $n=1$.  The core coordinate permutation has order $L$, so
every state period divides $L$.  For each $d\mid L$, ordinary Möbius
inversion gives the number of states of exact least period $d$:
$$
P_d=\sum_{e\mid d}\mu(d/e)F_e.
$$
Each $d$-cycle contains $d$ such states, hence
$$
C_d=\frac{P_d}{d}.
$$
Finally,
$$
\zeta_{T_k}(z)
=\exp\left(\sum_{r\ge1}\frac{F_r}{r}z^r\right)
=\prod_{d\mid L}(1-z^d)^{-C_d}.
$$
Möbius inversion and the finite-map zeta conversion are standard and earn
zero contribution credit.

## Remarks and Interpretation

- The polynomial presentation is only a wrapper.  The organizing object is
  the coefficient pushforward along multiplication on $\mathbb Z/m\mathbb Z$.
- The transient axis and periodic axis separate arithmetically.  Primes of
  $m$ that divide $k$ determine $m_{\parallel}$ and the height $h$; the
  complementary modulus $n$ determines the final multiplier permutation.
- Ring multiplication and the factorization of $X^m-1$ never enter the
  dynamic formulas.  This explains both the clean nonfield extension and the
  severe generic-engine ownership collision.
- Every step above is an exact identity or proposition.  No approximation,
  asymptotic passage, probabilistic heuristic, or unproved genericity
  assumption is used.

## Boundaries and Non-Claims

### Boundary ledger

| Boundary | Correct outcome |
|---|---|
| $t=0$ | $g_0=1$; the image is all of $A^m$ and every fibre is a singleton. |
| $\gcd(k,m)=1$ | $m_{\parallel}=1$, $n=m$, $h=0$; the entire map is a coordinate permutation. |
| $m=1$ | The map is the identity on $A$; $h=0$, $F_r=q$, and $L=1$. |
| $m>1$ and $m\mid k$ | $m_{\parallel}=m$, $n=1$, $h=1$; one step merges every input coefficient into the output at position zero. |
| $k=1$ | Same as the coprime boundary: identity on all coefficient positions. |
| $A$ nonfield | All formulas remain valid; no multiplication or division of coefficients enters the count. |
| $|A|=1$ | Fibre formulas are formally trivial, but the claimed sharp maximum $h$ can fail; this case is excluded. |
| unreachable target | Its fibre is exactly empty, never the uniform nonempty value. |

### Counterexample pressure

1. For $(m,k)=(12,6)$,
   $$
   (g_0,g_1,g_2,g_3)=(1,6,12,12).
   $$
   Therefore $\gcd(k,m)=6$ is not the stable support divisor.
2. For $(m,k)=(48,6)$,
   $$
   (g_0,\ldots,g_5)=(1,6,12,24,48,48),
   $$
   and $h=4$, while $\lceil\log_6 48\rceil=3$.
3. For $(m,k)=(16,4)$, $h=2$, not the largest exponent
   $v_2(m)=4$.
4. For $A=\mathbb Z/4\mathbb Z$ and
   $A=(\mathbb Z/2\mathbb Z)^2$, both of cardinality four, the audit obtains
   identical image, fibre, depth, fixed, and cycle counts for the same
   $(m,k)$.  This confirms that the claimed censuses use only cardinality,
   while not claiming the two functional graphs are canonically ring-isomorphic.

### Independent audit routes

- **Route A:** repeatedly send each coefficient at $j$ to $kj\bmod m$ and
  merge arrivals using the ring addition.
- **Route B:** for a requested time $t$ and output coordinate $r$, solve
  $k^tj\equiv r\pmod m$ afresh and sum exactly those input coefficients.
- **Formula route:** construct neither output algorithm; use gcd block sizes,
  the stable core, and the divisor formula for multiplier cycles.

`verify_sce_focused.py` compares Routes A and B state by state and checks both
against the formula route on all bounded boxes.  Enumeration is only
falsification pressure, not proof.

## Open Risks

There is no open mathematical gap in the normalized contract.  The terminal
risk is instead ownership: the reduction is a finite-ring linear map; its
stable-image/permutation-core split, uniform fibres, depth-from-image-chain,
and cycle/zeta conversion are generic.  Internal P115 already executes that
same proof engine with a coefficient operator.  Only the elementary formula
for $\gcd(k^t,m)$ is family-specific.

Accordingly this coherent derivation is archived with verdict
**`KILL_INTERNAL_ENGINE_TRANSFER / DO_NOT_DRAFT`**.
