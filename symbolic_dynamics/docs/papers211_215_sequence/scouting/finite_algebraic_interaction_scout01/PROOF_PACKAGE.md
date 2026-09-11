# Proof package: exact old-mechanism subtractions

## Claim, status and assumptions

Research target: a fresh finite autonomous algebraic interaction map with an
explicit all-parameter temporal theorem and a materially separate new
orbit/fibre/enumeration mechanism after old/source subtraction.
**Status of that target: NOT CURRENTLY JUSTIFIED / NO_FRESH_SLATE.**

The two algebraic deductions below are **PROVABLE AS STATED**. They are author
subtraction controls, not new theorem nominations. No empirical observation
is used. All groups and quasigroups are nonempty and finite. Group products
are ordered, with no commutativity assumption. Integers $n,d$ satisfy $n\ge2$
and $d\ge1$ respectively. The degenerate $d=1$ case is separated explicitly.

Strategy and dependencies:

1. Multiply the prescribed Hurwitz moves in their actual application order;
   retain each coordinate and the invariant product.
2. Solve the local inverse and iterate the wraparound conjugation.
3. Compare the Steiner map to the actual opposite-pair retired P160 map by
   a commuting coordinate rotation, then verify its four strata directly.
4. Solve the ordered target equations. This is the old P160/Aryapoor inverse
   mechanism, not an independent source-free innovation.

Original/source anchors and reading limits are in [REPORT.md](REPORT.md).

## 1. A Hurwitz sweep is a twisted shift

For $g=(g_1,\ldots,g_n)\in G^n$, let $H_i$ replace $(g_i,g_{i+1})$ by
$(g_{i+1},g_{i+1}^{-1}g_i g_{i+1})$. Let $C$ mean apply $H_1$, then $H_2$,
up through $H_{n-1}$. Thus the convention is operational and does not depend
on an ambiguous braid-word composition convention. Set
$p=g_1\cdots g_n$ and $\phi_p(x)=p^{-1}xp$.

Step 1: the local product remains
$g_{i+1}(g_{i+1}^{-1}g_i g_{i+1})=g_i g_{i+1}$.
After the first $j$ moves, the transported $g_1$ has been conjugated by
$g_2\cdots g_{j+1}$; this follows by substituting the next conjugation and
using $(ab)^{-1}=b^{-1}a^{-1}$. Hence
$$
C(g)=(g_2,\ldots,g_n,(g_2\cdots g_n)^{-1}g_1(g_2\cdots g_n))
     =(g_2,\ldots,g_n,\phi_p(g_1)).
$$
The last equality uses $p=g_1(g_2\cdots g_n)$, without commuting factors.

Step 2: every $H_i$ has two-sided inverse
$(u,v)\mapsto(uvu^{-1},u)$. Indeed the right move of that pair is $(u,v)$,
and applying this inverse to the right move of $(x,y)$ gives $(x,y)$.
Consequently $C$ is a permutation of $G^n$, every state is recurrent, and
every target has exactly one predecessor under every $C^k$, $k\ge1$.
The inverse is not a separate fibre-enumeration theorem.

Step 3: $p$ stays fixed at every epoch. Each original coordinate moves left
and receives exactly one $\phi_p$ when it passes from first to last position.
For $k=an+r$, where $a\ge0$ and $0\le r<n$, the full ordered iterate is
$$
(C^k(g))_i=
\begin{cases}
 \phi_p^a(g_{i+r}),&i+r\le n,\\
 \phi_p^{a+1}(g_{i+r-n}),&i+r>n.
\end{cases}
$$
To justify all $k$, the formula at $k=0$ is the identity. One more application
of the shift formula increases the source index by one; the single crossing
of index $n$ applies one additional $\phi_p$. At $r=n-1$ these crossings
produce $\phi_p^{a+1}$ in every coordinate, which is the case $r=0$ of the
next block. This proves the formula by induction.

In particular $C^n(g)$ conjugates all entries by $p$, so the period divides
$n\,\operatorname{ord}(p)$. A sharper exact relation, not an evaluated census,
is available. Let $K=\langle g_1,\ldots,g_n\rangle$ and let $h$ be the order of
$pZ(K)$ in $K/Z(K)$. Then $(C^n)^a(g)=g$ exactly when $p^a$ commutes with
every generator, exactly when $p^a\in Z(K)$; thus $g$ has period $h$ under
$C^n$. If its period under $C$ is $\ell$, the period under $C^n$ is the least
positive $a$ such that $\ell$ divides $na$, namely $\ell/\gcd(\ell,n)$.
Therefore
$$
\ell/\gcd(\ell,n)=h.
$$
This does not determine $\ell$ from $h,n$ alone. For example when $p=1$,
$C$ is just coordinate rotation on the product-one fibre; shorter rotational
symmetries still matter. When $G$ is trivial, all formulas give period one.
No minimum-period census is hidden behind the general finite-permutation
identity counting fixed points of powers.

Contribution consequence: fixed-word composition does not invent the
Hurwitz action. The explicit clock is the old product-conjugation mechanism
with coordinate transport, and the inverse supplies only singleton fibres.
Arbitrary noncentral words are not covered by this formula, and are not
silently asserted to have the same temporal structure.

## 2. The cyclic Steiner triple is retired P160 plus rotation

Put $Q_d=\mathbb F_2^d\setminus\{0\}$ and $N=2^d-1$. Define $x*x=x$ and
$x*y=x+y$ for $x\ne y$. The operation is commutative and satisfies
$x*(x*y)=y$: for unequal inputs, $x+y$ differs from $x$ and is nonzero,
so $x+(x+y)=y$; equal inputs use idempotence. It is therefore a Steiner
quasigroup, not an associative multiplication in general.

Let
$$
T(x,y,z)=(x*y,y*z,z*x),\quad
S(x,y,z)=(y*z,z*x,x*y),\quad
R(x,y,z)=(z,x,y).
$$
The map $S$ is the original retired P160 update. Direct substitution gives
$RS=T=SR$. Since $R^3$ is the identity, induction yields
$T^k=R^k S^k$ for every $k\ge0$. This is a commuting output composition,
not a claim that $T$ and $S$ are conjugate or have identical periods.

Step 1: the following four disjoint strata exhaust $Q_d^3$.

- Diagonal: $(a,a,a)$ is fixed.
- Exactly two equal: for $a\ne b$ and $c=a+b$,
  $(a,a,b)\mapsto(a,c,c)\mapsto(b,c,b)\mapsto(a,a,b)$.
  Cyclic rotation gives the other equality positions. All three states
  differ, because $a,b,c$ are distinct.
- Three distinct with $x+y+z=0$: the image is $(z,x,y)$, a strict three-cycle.
- Three distinct with $x+y+z\ne0$: the coordinates are linearly independent
  over $\mathbb F_2$, and the image
  $(x+y,y+z,z+x)$ is a distinct nonzero zero-sum triple. Such a source has
  depth exactly one, because it does not belong to any of the first three
  invariant strata.

Every output is in the initial linear span, so the entire trajectory lies
in a span of dimension at most three. Increasing $d$ does not create a new
trajectory type. Counts are
$$
N,\qquad 3N(N-1),\qquad N(N-1),\qquad N(N-1)(N-3)
$$
in the four strata. For $d\ge2$, the second count chooses the repeated value,
different singleton and equality position; the third chooses distinct
$x,y$ and forces $z=x+y$; the fourth chooses $x\ne0$, then
$y\notin\{0,x\}$, then $z$ outside their four-element span.
The recurrent count is $4N^2-3N$, with $N$ fixed points and
$4N(N-1)/3$ strict three-cycles. For $d=1$ there is one state and no other
stratum. For $d=2$, all states are recurrent; for $d\ge3$ independent triples
exist, so the sharp maximum depth is one. This census follows the old
four-stratum mechanism; it is not an independent enumerative axis.

Step 2: solve every target fibre. A diagonal or two-equal target has exactly
one predecessor on its permutation stratum. No distinct input can map to a
repeated target; the displayed equality-stratum trajectories exhaust repeated
inputs. An independent target has no predecessor, since every distinct image
has zero sum and a repeated source stays repeated.

For a distinct zero-sum target $(u,v,w)$, every predecessor must have three
distinct entries and solve
$$
x+y=u,\quad y+z=v,\quad z+x=w.
$$
Set $x=t$. All solutions are
$$
(t,t+u,t+w),\qquad t\in\mathbb F_2^d\setminus\{0,u,w\}.
$$
The third equation holds by construction and the second follows from
$u+w=v$. These three excluded values are distinct. No equality between
source coordinates is possible because $u,w,u+w$ are nonzero.
Thus there are exactly $N-2$ sources. Exactly one is a zero-sum source:
the sum of its coordinates is $t+u+w=t+v$, so it is $t=v$.
Every other source is an independent, source-free depth-one state.

Step 3: for $k\ge1$, a zero-sum target has the unique cyclic predecessor
$k$ steps back and the $N-3$ leaves entering the appropriate preceding node;
there are again $N-2$ sources. Repeated targets have one source at every
positive time, and independent targets have none. For $d=1$ the single
target has one source; the zero-sum target stratum does not exist.
At $d=2$, $N-2=1$, so all nonempty fibre sizes coincide, as required.

Equivalently, for every target $b$,
$$
(T^k)^{-1}(b)=(S^k)^{-1}(R^{-k}b).
$$
This follows from $T^k=R^kS^k$ and gives the precise old inverse adapter.
On unordered distinct triples both ordered maps induce Aryapoor's
$\psi_S$; the projective nonblock source family and collapse are directly
source-occupied. Repeated-coordinate cycles are universal Steiner identities.
The raw ordered periods do differ between $S$ and $T$, but only because of
the explicit order-three output rotation. No new independent theorem
mechanism survives.

## Open risks and stopping boundary

No all-size theorem for an arbitrary finite nonprojective Steiner quasigroup
or an arbitrary noncentral rack/braid word is proved. The projective argument
uses binary addition and cannot be moved to those carriers by terminology.
A general quasigroup's local divisibility does not guarantee surjectivity on
a finite periodic spatial ring: our own independent-target fibre is empty
when $d\ge3$. No larger pilot, new scheduler, carrier restriction or external
review is authorized by this deduction. Both controls stop at subtraction.

