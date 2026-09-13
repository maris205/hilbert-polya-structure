# Proof package: joint reversible-cycle laws for one random polynomial Henon map

Date: 2026-09-07. Author proof V1. No formal Paper30 selection, novelty
verdict, manuscript, experiment, or capacity exception is implied.

## Claim

Let $p$ be an odd prime, let $1\le d<p$, and choose uniformly one monic
polynomial $P\in\mathbb F_p[X]$ of degree $d$. Iterate the same map
$$H_P(x,y)=(P(x)-y,x)$$
throughout. Let $R(x,y)=(y,x)$. Write $S_n$ for the number of primitive
period-$n$ cycles preserved as sets by $R$, and $B_n$ for the number of
unordered pairs of distinct primitive period-$n$ cycles interchanged by $R$.
In particular the total number of period-$n$ cycles is $S_n+2B_n$.

Set
$$
\lambda_n=\begin{cases}1/2,&n=2,\\1,&n\ne2,\end{cases}
\qquad \mu_n=\frac1{2n}\quad(n\ge3).
$$
The exact identities $B_1=B_2=0$ hold. For $L\ge1$, retain the vector
$$Z_L=(S_1,\ldots,S_L,B_3,\ldots,B_L),$$
where the second list is empty if $L<3$. Let $Y_L$ have independent Poisson
coordinates of means $(\lambda_1,\ldots,\lambda_L,\mu_3,\ldots,\mu_L)$.

**Finite bound.** For any integer $K\ge1$ with $M=KL\le d$, put
$D_M=(M^M+M^2)/p$. Then the total variation distance satisfies
$$
d_{\rm TV}(\mathcal L(Z_L),\mathcal L(Y_L))
\le 2e^{4L}D_M+2\frac{(4L)^K}{K!}.                         \tag{1}
$$
An upper bound exceeding 1 is simply uninformative; the distance is, as
usual, one half of the sum of absolute probability-mass differences.

**Fixed-window limit.** For every fixed $L$, if $p\to\infty$ through odd
primes, $d(p)\to\infty$, and $d(p)<p$, then this total variation distance
tends to zero.

**Growing-window instance.** With natural logarithms, the same conclusion
holds for
$$d(p)=\lceil(\log p)^2\rceil,
\qquad L(p)=\lfloor(\log p)^{1/4}\rfloor$$
for all sufficiently large primes. More generally, (1) with $K=32L$ gives
$$
d_{\rm TV}\le\frac{2e^{4L}((32L^2)^{32L^2}+(32L^2)^2)}p
                 +2(e/8)^{32L},                            \tag{2}
$$
whenever $32L^2\le d<p$. Hence any $L\to\infty$ satisfying
$32L^2\le d$ and
$32L^2\log(32L^2)+4L-\log p\to-\infty$ is admissible.
No optimal growth window or fixed-degree universality is claimed.

The means for $n\ge3$ agree with classical random-involution predictions;
that agreement is not claimed as new. The period-two exception, the exact
polynomial ensemble, and the proved error bound must be distinguished from
those predictions. Literature and substantive scope are evaluated separately.

## Status

PROVABLE AS STATED — author proof. Independent full-package check pending.
The exploratory question did not prescribe Poisson means or independence;
the displayed law is derived below, including the exceptional low periods.

## Assumptions and notation

- Randomness is only in the $d$ lower coefficients of $P$; there is no new
  random kick or new polynomial at each iterate.
- A primitive cycle is a cycle of exact period $n$, not a repeated shorter
  coordinate word. Counting is of cycles, not periodic points.
- For $a,k\in\mathbb Z_{\ge0}$, $(a)_k=a(a-1)\cdots(a-k+1)$ and
  $\binom ak=(a)_k/k!$, with $(a)_0=1$ and $\binom ak=0$ for $k>a$.
- A multi-index $\alpha$ is over the retained coordinates of $Z_L$;
  $|\alpha|$ is its sum and $\alpha!$ the product of its factorials.
  Coordinate $S_n$ or $B_n$ has length weight $n$.
- An equality partition of coordinate slots records exactly which slots
  have equal field values; its blocks always receive distinct values.

The inverse is $H_P^{-1}(x,y)=(y,P(y)-x)$, so $RH_PR=H_P^{-1}$.
The polynomial Jacobian determinant of $H_P$ is 1. These identities justify
the reversible symplectic setting but are not probabilistic assumptions.

## Strategy and dependency map

1. Periodic coordinate words reduce the map to constraints on the values of
   $P$. Monic-polynomial interpolation supplies exact probabilities up to
   $d$ distinct arguments.
2. Integer rank-zero equality partitions have only ring or folded-path
   components. Primitive distinct reversal classes cannot share a component.
   All nonzero constraints remain nonzero in every odd characteristic.
3. Counting rooted words gives all mixed factorial moments with a uniform
   error bounded by a Bell-number estimate divided by $p$.
4. A finite multivariate inclusion-exclusion lemma turns these moments into
   total variation control; it does not assume a dependency graph for the
   values of a low-degree random polynomial.

The first structural lemma was also independently derived in the parallel
[zero-rank author probe](PAPER30_REVERSIBLE_ZERO_RANK_PROBE_V1_20260907.md).
That parallel derivation is not a final independent review of this file.
All steps needed for the present theorem are included below.

## Proof

### Step 1. Coordinate words and interpolation

Write a lifted cycle on $\mathbb F_p^2$ as $(x_i,x_{i-1})$, with indices
modulo $n$. Its equations are exactly
$$P(x_i)=x_{i-1}+x_{i+1}.                                   \tag{3}$$
The least period of the coordinate word equals the least period of the
state cycle. Reversal acts on the coordinate word by reversing its order,
up to a cyclic shift. A symmetric primitive cycle has $n$ rooted words;
an asymmetric unordered reversal pair has $2n$. This remains correct at
$n=1,2$, where every cycle is symmetric and there are no asymmetric pairs.

For $b\le d$ distinct field arguments $a_1,\ldots,a_b$, the vector of
values $(P(a_1),\ldots,P(a_b))$ is uniform in $\mathbb F_p^b$.
Indeed the $d$ random lower coefficients enter linearly, and their first
$b$ columns form an invertible Vandermonde matrix. The fixed monic term
only translates this surjective linear map. Therefore every prescribed
value vector has probability $p^{-b}$.

For a fixed equality partition with $b$ blocks, let $e_a$ be the formal
basis vector of block $a$. Repeated occurrences of block $a$ in (3)
impose the vector differences of their neighboring sums
$e_{a_-}+e_{a_+}$. These rows define an integer matrix $C$ with entries
in $\{0,\pm1,\pm2\}$. For a distinct assignment $u\in\mathbb F_p^b$,
all equations are consistent exactly when $Cu=0$. If consistent and
$b\le d$, their probability is $p^{-b}$ by interpolation.

### Step 2. Classification of rank-zero components

Suppose $C=0$ over the integers. Every occurrence of a block $a$ then has
the same unordered neighbor multiset $N(a)$, of total size two with
multiplicity. Form the simple graph on blocks by joining distinct blocks
that occur adjacently. Adjacency is symmetric because it comes from a word.
Each vertex has degree at most two. Every connected component supporting a
word is consequently a single vertex, a simple path, or a simple ring of
at least three vertices.

At a degree-two vertex, $N(a)$ consists of the two different neighbors, so
an entering word must exit by the other neighbor. At a degree-one endpoint
with neighbor $b$, the only possibilities are
$$N(a)=\{b,b\}\quad\hbox{or}\quad N(a)=\{a,b\}.$$
Call these a bounce and a loop, respectively. A degree-zero vertex has
$N(a)=\{a,a\}$ and supports only the constant word. Given any adjacent
ordered pair of blocks, the next block is determined by subtracting the
previous block from $N(a)$; this proves determinism of the traversal.

On a ring with $b\ge3$ vertices, a traversal keeps one orientation and its
primitive length is $b$. The two orientations are distinct reversal cycles.
On a path with $b\ge2$ vertices, the traversal goes from one endpoint to
the other and back, spending one additional step at each loop endpoint.
If $\ell\in\{0,1,2\}$ endpoints have loops, its primitive length is
$$n=2(b-1)+\ell.                                           \tag{4}$$
It is one symmetric cycle. To see that this tour is primitive, any shorter
period would return to the same directed internal edge before the tour had
visited both endpoints, contradicting its determined succession. For the
two-vertex path the same statement follows by directly listing the bounce
and loop steps. A singleton instead has primitive period 1.

If two primitive words share a block, their neighbor multisets, and hence
the entire connected graph and deterministic tours, are shared. On a path
they are the same cycle; on a ring they are the same or reversed cycle.
Thus two distinct objects in the retained counts cannot share any block
in a joint rank-zero partition. This conclusion uses distinct reversal
classes, not merely distinct rooted starting positions.

For odd $p$, an integer-nonzero matrix $C$ cannot become the zero matrix
modulo $p$, since a nonzero entry is $\pm1$ or $\pm2$. We need only
$\operatorname{rank}_{\mathbb F_p}C\ge1$, not preservation of the full
integer rank. Its kernel has at most $p^{b-1}$ assignments, even before
requiring their coordinates to be distinct. This handles all odd primes
without an unproved uniform minor bound.

### Step 3. Exact count of the rank-zero word patterns

For an asymmetric reversal pair of period $n\ge3$, the only rank-zero
partition of its $n$ rooted slots is the all-distinct ring partition.
Its weight after dividing by $2n$ is $\mu_n=1/(2n)$.

For a symmetric word, consider reflections $i\mapsto t-i$ on
$\mathbb Z/n\mathbb Z$. Their slot orbits are the folded-path partitions.
If $n\ge3$ is odd, every one of the $n$ reflections gives a path with
one bounce endpoint and one loop endpoint, with $(n+1)/2$ blocks.
If $n\ge4$ is even, $n/2$ reflections have two fixed slots, giving
$n/2+1$ blocks and two bounces; the other $n/2$ have no fixed slots,
giving $n/2$ blocks and two loops. All these partitions are primitive.

No two reflections produce the same primitive partition: invariance under
two different reflections would give a nontrivial rotational period.
Conversely every path tour in Step 2 has the stated reflection and slot
partition. Hence the number of rank-zero symmetric rooted-slot partitions
is $n$ for every $n\ge3$.

At $n=1$ it is one. At $n=2$ the two-bounce path gives the all-distinct
two-slot partition. The other reflection identifies both slots, producing
a nonprimitive constant word, and is excluded. There is thus only one
rank-zero symmetric partition at $n=2$. Dividing by the number $n$ of
rooted representatives yields exactly $\lambda_n$ in the claim.

This also explains the structural exception: writing
$H_P=R\circ T_P$ with $T_P(x,y)=(x,P(x)-y)$, a nontrivial two-cycle
whose two points both lie in $\operatorname{Fix}(R)$ is impossible because
$T_P$ preserves the first coordinate. Treating $T_P$ as a generic random
involution would incorrectly restore the missing type.

### Step 4. Uniform mixed factorial moments

Let $\alpha$ describe an ordered selection of $\alpha_{S_n}$ distinct
symmetric cycles and $\alpha_{B_n}$ distinct asymmetric reversal pairs.
The mixed falling factorial
$$f_\alpha=\mathbb E\prod_i(Z_{L,i})_{\alpha_i}$$
counts these selections. Rooting each object represents it with total
constant multiplicity
$$w=\prod_n n^{\alpha_{S_n}}\prod_{n\ge3}(2n)^{\alpha_{B_n}}.$$
There are $s=\sum_i n_i\alpha_i$ coordinate slots. We suppose $s\le d$.
The conditions of primitivity, reversal type, and distinctness of the
selected objects depend only on their equality partition; no choice of
distinct field labels can change these combinatorial conditions.

For a rank-zero admissible partition with $b$ blocks, its contribution to
$f_\alpha$ is $(p)_b/(w p^b)$. By Step 2 its objects have disjoint block
sets, and by Step 3 the number of such partitions divided by $w$ is
$$\nu^\alpha=\prod_n\lambda_n^{\alpha_{S_n}}
                     \prod_{n\ge3}\mu_n^{\alpha_{B_n}}.$$
The elementary collision union bound for $b$ independent uniform field
values gives
$$0\le1-(p)_b/p^b\le\frac{b(b-1)}{2p}.$$
Thus the zero-rank contribution differs from $\nu^\alpha$ by at most
$s^2\nu^\alpha/(2p)\le s^2/(2p)$, since all retained means are at most 1.

For every other admissible partition, Step 2 bounds the number of
consistent assignments by $p^{b-1}$ and Step 1 gives probability $p^{-b}$.
Its contribution is at most $1/(wp)\le1/p$. The number of partitions of
$s$ slots is the Bell number, at most $s^s$ for $s\ge1$: encode each
partition by assigning to every slot the least index in its block.
It follows that
$$|f_\alpha-\nu^\alpha|\le\frac{s^s+s^2}{p}.                 \tag{5}$$
The empty multi-index has exact moment 1. In particular if $|\alpha|\le K$
and $KL=M\le d$, the error in (5) is at most $D_M$ uniformly in $\alpha$.
At the two smallest periods one may also read off the exact first moments
$\mathbb ES_1=1$ and, when $d\ge2$, $\mathbb ES_2=(p-1)/(2p)$.

### Step 5. A finite multivariate moment-to-variation bound

We give the elementary inversion argument, so no independence assumption
about a low-degree polynomial outside a small set of arguments is needed.
Let $Z,Y\in\mathbb Z_{\ge0}^r$, and suppose their falling factorial moments
up to total order $K$ differ by at most $D$. Suppose also that $Y$ has
independent Poisson coordinates of means $\nu_i$ and put
$\Lambda=\sum_i\nu_i$. Then
$$d_{\rm TV}(\mathcal L(Z),\mathcal L(Y))
\le2D e^{2r}+2(2\Lambda)^K/K!.                             \tag{6}$$

To prove this, set $m_\alpha(Z)=\mathbb E\prod_i\binom{Z_i}{\alpha_i}$.
For a deterministic vector $z\ge x$ coordinatewise, use the binomial
identity $\sum_{j=0}^k(-1)^j\binom tj=(-1)^k\binom{t-1}k$ for $t>k$
and its full-sum form for $t\le k$. Truncating the exact indicator expansion
at total degree $K-1$, for $|x|<K$, gives
$$
\left|\mathbb P(Z=x)-
\sum_{\substack{\alpha\ge x\\|\alpha|<K}}
(-1)^{|\alpha-x|}\binom\alpha x\,m_\alpha(Z)\right|
\le\sum_{\substack{\alpha\ge x\\|\alpha|=K}}
\binom\alpha x\,m_\alpha(Z).                              \tag{7}
$$
Here $\binom\alpha x=\prod_i\binom{\alpha_i}{x_i}$.
The remainder inequality follows from
$\binom{t-1}k\le\binom t{k+1}$ for $t\ge k+1$, after multiplying by
$\prod_i\binom{z_i}{x_i}$ and applying multivariate Vandermonde.
If some $z_i<x_i$, all terms are zero, so the same bound holds.

Summing (7) over $|x|<K$ uses
$\sum_{x\le\alpha}\binom\alpha x=2^{|\alpha|}$.
The omitted tail has probability at most
$\mathbb E\binom{\sum_iZ_i}{K}=\sum_{|\alpha|=K}m_\alpha(Z)$;
the same holds for $Y$. The interior remainders together with these tails
are therefore bounded in $\ell^1$ by
$2^K\sum_{|\alpha|=K}(m_\alpha(Z)+m_\alpha(Y))$.
The retained moment-difference part is at most
$$\sum_{|\alpha|<K}\frac{2^{|\alpha|}D}{\alpha!}\le D e^{2r}.$$
Since $m_\alpha(Y)=\nu^\alpha/\alpha!$,
$$
\sum_{|\alpha|=K}(m_\alpha(Z)+m_\alpha(Y))
\le 2\Lambda^K/K!+D r^K/K!.
$$
Finally $(2r)^K/K!\le e^{2r}$. Dividing the $\ell^1$ bound by 2 and
loosening the constants gives (6). All factorial moments used are finite
in the present finite-state model and in the Poisson comparison.

### Step 6. Quantifiers and the two limits

The vector $Z_L$ has $r=L+\max(L-2,0)\le2L$ coordinates, and
$\Lambda=\sum_{n\le L}\lambda_n+\sum_{3\le n\le L}1/(2n)\le2L$.
Apply (6) with the uniform bound (5) for $M=KL\le d$ to obtain (1).

For fixed $L$, choose
$$K(p)=\min\{\lfloor d(p)/L\rfloor,
                 \lfloor\sqrt{\log p}/L\rfloor\}.$$
This tends to infinity. Its $M=KL$ is at most $\sqrt{\log p}$, so
$M^M=p^{o(1)}$ and the first term in (1) vanishes. The second term
vanishes because $(4L)^K/K!\le(4eL/K)^K\to0$.
This proves the fixed-window assertion for every permitted degree sequence,
not only a selected fast-growing one.

For growing $L$, take $K=32L$ and use $K!\ge(K/e)^K$ to obtain (2).
For the stated example, $32L^2\le d$ eventually and
$M\log M+4L=O(\sqrt{\log p}\log\log p)=o(\log p)$.
Both terms in (2) tend to zero. The more general condition in the claim
controls the same first term and $L\to\infty$ controls the second.
All limits concern one sampled polynomial followed by its fixed iterates.
This completes the proof. $\square$

## Corrections or missing assumptions

No unproved Poisson means were imposed on the initial exploratory problem.
The exception $S_2\Rightarrow\operatorname{Pois}(1/2)$ and the exact absence
of $B_1,B_2$ are necessary; replacing these by a generic random-involution
law would be false. The finite-degree hypothesis $KL\le d$ is explicit in
the quantitative theorem, and the fixed-window limit genuinely allows every
$d(p)\to\infty$ with $d(p)<p$.

## Open risks and evaluation boundaries

- Independent review must check primitive versus rooted reversal classes,
  joint shared-block exclusion, characteristic three, the missing second
  period-two type, and the multivariate inversion remainder and tails.
- The finite bound is deliberately coarse and no optimal period window is
  asserted. Standard interpolation, partition counting, and factorial-moment
  inversion are not new methods merely because their constants are explicit.
- Literature matching and natural 22–30-page capacity remain separate.
  A growing window obtained by routine estimates does not automatically make
  this an independent long-form Paper30 candidate.
- No numerical study, empirical Poisson fit, PDF build, external message,
  formal Route evaluation, or acceptance-counter update accompanies this file.
