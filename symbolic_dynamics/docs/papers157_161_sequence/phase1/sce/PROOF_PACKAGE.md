# Proof Package

## Claim

Let $A$ be a finite nonzero commutative ring with identity, let
$q=|A|\ge2$, and let $m,k\ge1$.  On
$$
\mathcal R_{A,m}=A[X]/(X^m-1),
$$
define $T_k(f)=f(X^k)$.  For $t\ge0$, put $g_t=\gcd(k^t,m)$.  Define
$$
m_{\parallel}=\prod_{\substack{\ell\mid m\\\ell\mid k}}
\ell^{v_\ell(m)},
\qquad n=m/m_{\parallel},
$$
and
$$
h=\max_{\substack{\ell\mid m\\\ell\mid k}}
\left\lceil\frac{v_\ell(m)}{v_\ell(k)}\right\rceil,
$$
with empty maximum $0$.  For $g\mid m$, let
$$
V_g=\left\{\sum_{r=0}^{m-1}b_rX^r:b_r=0\text{ if }g\nmid r\right\}.
$$
Then all of the following hold.

1. For every $t\ge0$,
   $$
   T_k^t(f)(X)=f(X^{k^t})\pmod{X^m-1},
   \qquad
   (T_k^ta)_r=\sum_{k^tj\equiv r\pmod m}a_j.
   $$
   Moreover,
   $$
   \operatorname{im}(T_k^t)=V_{g_t},
   \qquad |V_{g_t}|=q^{m/g_t},
   $$
   and for every target $b$,
   $$
   \#(T_k^t)^{-1}(b)=
   \begin{cases}
   q^{m-m/g_t},&b\in V_{g_t},\\
   0,&b\notin V_{g_t}.
   \end{cases}
   $$
2. The image chain stabilizes sharply at time $h$:
   $$
   g_t=\prod_{\ell\mid m}
   \ell^{\min\{t\,v_\ell(k),v_\ell(m)\}},
   \qquad
   g_t=m_{\parallel}\Longleftrightarrow t\ge h.
   $$
   The stable image and periodic set are both $V_{m_{\parallel}}$, of
   cardinality $q^n$.  If $\tau(a)$ is first entry time into the periodic
   set, then for every $t\ge0$,
   $$
   \#\{a:\tau(a)\le t\}=q^{m-m/g_t+n}.
   $$
   Consecutive differences, with the artificial convention $D_{-1}=0$,
   give every exact depth shell.  The maximum depth is exactly $h$; for
   $h>0$, its shell contains
   $$
   q^m-q^{m-m/g_{h-1}+n}
   $$
   states.
3. Under the coordinate identification
   $$
   V_{m_{\parallel}}\cong A^n,
   \qquad
   (b_s)_{s\bmod n}\longleftrightarrow
   \sum_{s=0}^{n-1}b_sX^{m_{\parallel}s},
   $$
   the core action is the coordinate permutation induced by
   $s\mapsto ks\pmod n$.
4. If $c_r$ is the number of cycles of multiplication by $k^r$ on
   $\mathbb Z/n\mathbb Z$, then
   $$
   c_r=\sum_{d\mid n}\frac{\varphi(d)}{\operatorname{ord}_d(k^r)},
   \qquad
   \#\operatorname{Fix}(T_k^r)=F_r=q^{c_r},
   $$
   where $\operatorname{ord}_1(k^r)=1$.  With
   $L=\operatorname{ord}_n(k)$ and $L=1$ when $n=1$, all state periods
   divide $L$, and for $d\mid L$,
   $$
   P_d=\sum_{e\mid d}\mu(d/e)F_e,
   \qquad C_d=P_d/d,
   $$
   count exact-period states and cycles.  Therefore
   $$
   \zeta_{T_k}(z)
   =\exp\left(\sum_{r\ge1}\frac{F_r}{r}z^r\right)
   =\prod_{d\mid L}(1-z^d)^{-C_d}.
   $$

The claim is mathematical only.  Its research disposition is separately
`KILL_INTERNAL_ENGINE_TRANSFER`.

## Status

`PROVABLE AS STATED`.

The stated version already includes the assumptions needed for the sharp
height, including $q\ge2$, and the conventions needed for $n=1$ and an empty
prime maximum.

## Assumptions

- $A$ is finite, nonzero, commutative, and unital.
- $q=|A|\ge2$.
- $m,k\ge1$.
- The polynomial variable is central.
- Depth is first entry time into the periodic set.

## Notation

- $e_j$ denotes the class of $X^j$, with $j$ read modulo $m$.
- $v_\ell(u)$ is the $\ell$-adic valuation of a positive integer $u$.
- $\varphi$ and $\mu$ are the Euler and Möbius functions.
- $\operatorname{ord}_d(u)$ is the multiplicative order of $u$ modulo $d$;
  the order modulo $1$ is defined as $1$.
- $D_t=\#\{a:\tau(a)\le t\}$ for $t\ge0$, and $D_{-1}=0$ is only a
  bookkeeping convention for the depth-zero shell.

## Proof Strategy

Use the coefficient basis to reduce every iterate to multiplication by
$k^t$ on exponent positions.  Solve the associated congruence to obtain
disjoint additive block-sum maps, which gives images and all fibres without
field assumptions.  Read stabilization prime by prime.  Prove that the
stable image is the periodic set by showing that the restriction is a
coordinate permutation and that every periodic point lies in every image.
Count the preimage of this core to obtain depth.  Finally, stratify the core
positions by additive order and apply finite permutation counting and Möbius
inversion.

## Dependency Map

1. The iterate formula depends only on the basis identity
   $T_k(e_j)=e_{kj\bmod m}$.
2. The image and fibre theorem depends on the elementary linear-congruence
   lemma and surjectivity of addition $A^g\to A$.
3. The stable image and height depend on the valuation identity
   $v_\ell(\gcd(k^t,m))=\min\{t v_\ell(k),v_\ell(m)\}$.
4. Identification of the periodic set depends on $\gcd(k,n)=1$ and the
   finite-set fact that a permutation has only periodic points.
5. The depth CDF depends on the complete target-fibre theorem and the
   periodic-core identification.
6. Fixed counts depend on cycles of the multiplier permutation; the divisor
   formula depends on stratifying $\mathbb Z/n\mathbb Z$ by additive order.
7. Least-period, cycle, and zeta formulas depend on the fixed counts and
   finite-map Möbius inversion.
8. The degenerate cases $m=1$, $\gcd(k,m)=1$, $n=1$, and an empty prime set
   are handled by the stated conventions rather than by an implicit limit.

## Proof

**Step 1: the substitution is well defined and the coefficient basis is
unique.**  Since $X^m-1$ is monic, division by it gives every class in
$A[X]/(X^m-1)$ a unique representative of degree less than $m$.  Also,
$$
(X^m-1)(X^{m(k-1)}+X^{m(k-2)}+\cdots+1)=X^{mk}-1.
$$
Therefore substituting $X^k$ into a multiple of $X^m-1$ again produces a
multiple of $X^m-1$, so $T_k$ is well defined on the quotient.

**Step 2: derive every iterate.**  In the quotient,
$$
T_k(e_j)=e_{kj\bmod m}.
$$
Induction on $t$ gives
$$
T_k^t(e_j)=e_{k^tj\bmod m}.
$$
The base $t=0$ is the identity.  The induction step follows by applying
$T_k$ once more to $e_{k^tj}$.  Extending additively yields
$$
T_k^t(f)(X)=f(X^{k^t})\pmod{X^m-1}
$$
and, after collecting all source basis vectors that reach position $r$,
$$
(T_k^ta)_r=\sum_{\substack{j\bmod m\\k^tj\equiv r\pmod m}}a_j.
$$

**Step 3: solve the exponent congruence.**  Let $u=k^t$ and
$g=\gcd(u,m)=g_t$.  Write $u=gu'$ and $m=gm'$ with
$\gcd(u',m')=1$.  If $uj\equiv r\pmod m$, then $g\mid r$.  Conversely,
if $r=gr'$, the congruence becomes
$$
u'j\equiv r'\pmod{m'}.
$$
The coefficient $u'$ is invertible modulo $m'$, so this congruence has one
solution modulo $m'$.  That residue class has exactly $g$ lifts modulo
$m=gm'$.  Hence $uj\equiv r\pmod m$ is solvable precisely for
$r\in g\mathbb Z/m\mathbb Z$, and every solvable target position has
exactly $g$ source positions.

**Step 4: compute the image and every target fibre.**  The congruence fibres
from Step 3 partition all source indices into $m/g_t$ disjoint blocks, one
for each multiple of $g_t$.  On each block the coefficient map is
$$
(x_1,\ldots,x_{g_t})\longmapsto x_1+\cdots+x_{g_t}.
$$
For a prescribed output $y\in A$, choose the first $g_t-1$ entries freely
and set the last entry equal to $y$ minus their sum.  Thus this block map is
surjective and each block fibre has $q^{g_t-1}$ elements.  The blocks are
independent, while all output coordinates outside the multiples of $g_t$
are forced to zero.  It follows that
$$
\operatorname{im}(T_k^t)=V_{g_t},
\qquad |V_{g_t}|=q^{m/g_t}.
$$
For a target in $V_{g_t}$, multiplying the block-fibre sizes gives
$$
\left(q^{g_t-1}\right)^{m/g_t}=q^{m-m/g_t}.
$$
A target outside $V_{g_t}$ asks for a nonzero coefficient at an unreachable
position and has no preimage.  This proves the complete fibre formula.  The
argument invokes no division or nonzero-product property in $A$, so zero
divisors cause no exception.

**Step 5: calculate the exact stabilization time.**  For each prime
$\ell\mid m$,
$$
v_\ell(k^t)=t\,v_\ell(k)
$$
and therefore
$$
v_\ell(g_t)
=\min\{t\,v_\ell(k),v_\ell(m)\}.
$$
Multiplication over the prime factors of $m$ gives the displayed formula for
$g_t$.  If $\ell\nmid k$, its exponent in every $g_t$ is zero.  If
$\ell\mid k$, its exponent reaches $v_\ell(m)$ exactly when
$$
t\ge\left\lceil\frac{v_\ell(m)}{v_\ell(k)}\right\rceil.
$$
All supported prime exponents have saturated exactly when $t\ge h$.  This
proves
$$
g_t=m_{\parallel}\quad\Longleftrightarrow\quad t\ge h.
$$
It also shows $g_t\mid g_{t+1}$, so $V_{g_{t+1}}\subseteq V_{g_t}$ and
$$
\bigcap_{t\ge0}\operatorname{im}(T_k^t)=V_{m_{\parallel}}.
$$
When no prime of $m$ divides $k$, the empty-product and empty-maximum
conventions give $m_{\parallel}=1$ and $h=0$, and the same conclusion holds.

**Step 6: identify the periodic set.**  Put
$n=m/m_{\parallel}$.  Every prime common to $k$ and $m$ was placed entirely
in $m_{\parallel}$, so $\gcd(k,n)=1$.  On a core basis vector,
$$
T_k(e_{m_{\parallel}s})
=e_{m_{\parallel}(ks\bmod n)}.
$$
Thus $T_k$ restricts to the coordinate permutation induced by multiplication
by $k$ on $\mathbb Z/n\mathbb Z$.  Every core point is periodic because this
is a permutation of a finite set.

For the reverse inclusion, suppose $a$ has period $r\ge1$.  Given any
$t\ge0$, choose a multiple $ur\ge t$.  Then
$$
a=T_k^{ur}(a)=T_k^t\bigl(T_k^{ur-t}(a)\bigr),
$$
so $a\in\operatorname{im}(T_k^t)$.  This holds for every $t$, hence
$a\in V_{m_{\parallel}}$ by Step 5.  Therefore
$$
\operatorname{Per}(T_k)=V_{m_{\parallel}}.
$$
There are $n$ supported coefficient positions, giving
$|\operatorname{Per}(T_k)|=q^n$.

**Step 7: derive the depth CDF and prove sharpness.**  For every $t\ge0$,
$$
\tau(a)\le t
\quad\Longleftrightarrow\quad
T_k^t(a)\in V_{m_{\parallel}}.
$$
The forward implication holds because a forward iterate of a periodic point
is periodic; the reverse implication uses Step 6.  Since
$g_t\mid m_{\parallel}$, the inclusion
$V_{m_{\parallel}}\subseteq V_{g_t}$ holds.  Consequently all $q^n$ core
targets are reachable at time $t$, and Step 4 assigns each the fibre size
$q^{m-m/g_t}$.  Hence
$$
D_t=q^{m-m/g_t+n}.
$$
The exact shell at depth $t$ is $D_t-D_{t-1}$, taking $D_{-1}=0$ only when
$t=0$.

At $t=h$, Step 5 gives $g_h=m_{\parallel}$, so
$$
D_h=q^{m-m/m_{\parallel}+n}=q^m.
$$
Every state has depth at most $h$.  If $t<h$, then
$g_t<m_{\parallel}$, hence $m/g_t>n$.  The exponent
$m-m/g_t+n$ is strictly less than $m$, and $q\ge2$ implies
$D_t<q^m$.  At least one state has depth greater than $t$.  Therefore the
maximum depth is exactly $h$.  When $h>0$, subtracting $D_{h-1}$ from
$D_h=q^m$ gives the claimed deepest-shell count.

**Step 8: count fixed states.**  Let $r\ge1$.  A state fixed by $T_k^r$ is
periodic, so Step 6 places it in the core.  There, $T_k^r$ permutes coordinate
positions by
$$
\pi_r(s)=k^rs\pmod n.
$$
A coefficient vector is fixed exactly when it is constant on every cycle of
$\pi_r$.  If $c_r$ is the number of these cycles, choosing one arbitrary
element of $A$ per cycle gives
$$
F_r=q^{c_r}.
$$

It remains to derive $c_r$.  For every $d\mid n$, precisely $\varphi(d)$
elements of the additive cyclic group $\mathbb Z/n\mathbb Z$ have additive
order $d$.  If $s$ has additive order $d$, then its orbit length under
$\pi_r$ is the least $u\ge1$ satisfying
$$
k^{ru}s=s,
$$
which is equivalent to $d\mid k^{ru}-1$.  Since $\gcd(k,d)=1$, this least
$u$ is $\operatorname{ord}_d(k^r)$.  The order-$d$ stratum therefore splits
into
$$
\frac{\varphi(d)}{\operatorname{ord}_d(k^r)}
$$
cycles.  Summing over $d\mid n$ proves the divisor formula for $c_r$.

**Step 9: convert fixed counts into cycles and zeta.**  Multiplication by
$k$ on $\mathbb Z/n\mathbb Z$ has order
$L=\operatorname{ord}_n(k)$; when $n=1$, the unique position is fixed and
the convention $L=1$ has the same effect.  Hence every core state, and thus
every periodic state, has period dividing $L$.

For $d\mid L$, let $P_d$ be the number of states of exact period $d$.  A
state is fixed by $T_k^d$ exactly when its exact period divides $d$, so
$$
F_d=\sum_{e\mid d}P_e.
$$
Möbius inversion on the divisor lattice gives
$$
P_d=\sum_{e\mid d}\mu(d/e)F_e.
$$
Every cycle of length $d$ contributes exactly $d$ states, yielding
$C_d=P_d/d$.  Multiplying one factor $(1-z^d)^{-1}$ for every directed cycle
gives
$$
\prod_{d\mid L}(1-z^d)^{-C_d}.
$$
Expanding the logarithm of this product and grouping the divisors of each
iterate index gives
$$
\exp\left(\sum_{r\ge1}\frac{F_r}{r}z^r\right),
$$
which proves the stated zeta identity.

**Step 10: verify the degenerate legal boundaries.**  If $m=1$, then
$X=1$ in the quotient and $T_k$ is the identity on $A$; the formulas give
$m_{\parallel}=n=1$, $h=0$, and $F_r=q$.  If $\gcd(k,m)=1$, then
$m_{\parallel}=1$ and $h=0$, so the entire carrier is the permutation core.
If $m>1$ and $m\mid k$, then $m_{\parallel}=m$, $n=1$, and $h=1$; the first
step merges all coefficients into the output at position zero.  All three
cases agree with the general formulas.

Therefore every part of the claim follows. $\square$

## Corrections or Missing Assumptions

- No correction is needed for the exact claim above.
- If the coefficient class were allowed to include the zero ring of
  cardinality one, the uniform counting identities would collapse to $1$,
  but the sharp maximum-depth statement could report a positive arithmetic
  $h$ for a one-state identity graph.  Either retain $q\ge2$ or replace the
  height conclusion by the separate zero-ring value $0$.
- If one begins with the breadth-scout finite-field statement, the proof is
  stronger than required: it extends to every finite nonzero commutative
  unital ring.  This is an extension, not an extra assumption.

## Open Risks

- There is no unresolved mathematical implication in the normalized theorem.
- The notation $q$ must not be described as a prime power in the ring-general
  version; it is only $|A|$.
- Bounded enumeration cannot replace any proof step and is used only to seek
  counterexamples.
- The research-level risk is terminal: the proof is a direct specialization
  of generic finite-linear stable-image/permutation-core machinery and the
  internal P115 engine.  The correct disposition is
  `KILL_INTERNAL_ENGINE_TRANSFER / DO_NOT_DRAFT`, not a novelty claim.
