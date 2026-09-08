# P7: full-domain orbit bound from the resolved anticanonical pencil

2026-09-08 UTC. Author-complete proof package; independent review and any
admission decision belong to the coordinator. This addresses the unchanged
[P7 contract](../../continuation_round7/charp_scout/FROZEN_CONTRACTS.md#p7--finite-field-q-painlevé-i-uniform-native-periods),
not a new conjecture. The conjecture, dynamical charts and monodromy integral
are owned by Joshi–Roffelsen. The argument below adds an algebraic
pole-index and fibre-integrality argument; it does not assume their
conjectured discriminant formula or identify a dynamical fibre with a
spectral quotient.

## 1. Statement and proof dependencies

Let $k=\mathbb F_q$, let $s,t_0\in k^*$, and put
$r=\operatorname{ord}(s)$. Apply exactly the seven native branches of P7,
including $t\mapsto st$, on all torus states and all four exceptional
affine lines over phases $t\in t_0\langle s\rangle$. Then every state has
a least native period $\ell$, and

$$
r\mid\ell,\qquad \frac{\ell}{r}\le q+1+2\sqrt q. \tag{1}
$$

The main stronger geometric assertion proved below is this: at each fixed
nonzero phase $t$, the source integral $I_r$ extends to a morphism
$f_t:S_{t,s}\to\mathbb P^1$ on an explicitly constructed smooth rational
surface. Its infinity fibre is $rD$, where $D$ is a reduced eight-component
anticanonical cycle. Every finite geometric fibre is integral and reduced
of arithmetic genus one and is contained entirely in the original
initial-value space $U_{t,s}$.

The dependencies are: elementary blowup intersection theory; adjunction
for an integral Cartier curve on a smooth surface; the source's proved
integral construction, with the reduction step made explicit in Section 5;
normalization of projective curves; Riemann–Roch in genus zero; and Hasse's
theorem. No theorem about complex period maps or classification of
positive-characteristic Halphen surfaces is used.

All geometric arguments through Section 6 may be made over $\bar k$.
Every construction and the map itself descend to $k$, since all centres
and coefficients are defined over $k$.

## 2. A compactification of exactly the state space

Start with $\mathbb P^1_x\times\mathbb P^1_y$. Write $H_x$ and $H_y$
for pullbacks of the classes of $x=\text{constant}$ and
$y=\text{constant}$, respectively. Make the following eight blowups.
The indices label total exceptional classes, not strict transforms.
Centres on disjoint parts of the surface may be blown up in either order.

| Class | Centre |
| --- | --- |
| $E_1$ | $(x,y)=(\infty,1)$ |
| $E_2$ | $(0,\infty)$ |
| $E_3$ | On $E_2$, at $xy=t$ |
| $E_4$ | $(0,0)$ |
| $E_5$ | Intersection of the first exceptional curve over $(0,0)$ with the strict transform of $y=0$ |
| $E_6$ | On $E_5$, at $x^2/y=t$ |
| $E_7$ | $(\infty,\infty)$ |
| $E_8$ | On $E_7$, at $y/x=s$ |

For example, the coordinates just before the $E_3,E_6,E_8$ blowups are,
respectively,

$$
(x,y)=(uv,u^{-1}),\quad(uv,u^2v),\quad((uv)^{-1},u^{-1}),
$$

with centre $(u,v)=(0,t),(0,t),(0,s)$. The $E_1$ blowup is an ordinary
smooth-boundary blowup with centre $x^{-1}=0,y=1$.

Denote the resulting projective smooth surface by $S=S_{t,s}$. Its Picard
group has the free basis $H_x,H_y,E_1,\ldots,E_8$, with

$$
H_x^2=H_y^2=0,\quad H_xH_y=1,\quad
E_iE_j=-\delta_{ij},\quad H_xE_i=H_yE_i=0.
$$

The following are actual irreducible curves on $S$:

$$
\begin{array}{ll}
D_1=H_x-E_1-E_7,&D_2=E_7-E_8,\\
D_3=H_y-E_2-E_7,&D_4=E_2-E_3,\\
D_5=H_x-E_2-E_4,&D_6=E_4-E_5,\\
D_7=E_5-E_6,&D_8=H_y-E_4-E_5.
\end{array} \tag{2}
$$

They form a transverse cycle in the order displayed: each has square
$-2$, consecutive curves meet once, including $D_8,D_1$, and all other
intersections vanish. Indeed these are the boundary curves after the four
corner blowups, followed by the four smooth-boundary blowups. None of the
latter centres is a node, since $s,t\ne0$. In particular

$$
D:=\sum_{i=1}^8D_i=2H_x+2H_y-\sum_{i=1}^8E_i=-K_S,
\qquad D^2=0,\qquad DD_i=0. \tag{3}
$$

Put $U=S\setminus D$. It consists, as a disjoint decomposition of points,
of the torus and the four accessible exceptional curves
$E_1,E_3,E_6,E_8$ minus their respective single boundary point. Those
four curves are affine lines with the following neighbourhood coordinates:

$$
\begin{array}{lll}
L_1:&x=u^{-1},&y=1+uv,\\
L_2:&x=u(t+uv),&y=u^{-1},\\
L_3:&x=u(t+uv),&y=u^2(t+uv),\\
L_4:&x=[u(s+uv)]^{-1},&y=u^{-1}.
\end{array} \tag{4}
$$

Here $L_j$ is $u=0$ with $v\in\mathbb A^1$. Thus (4) reproduces the
source charts and the exact P7 state encoding, including $v=0$ on every
line. In particular no intermediate exceptional component has accidentally
been counted as an additional ordinary state: those components occur in
$D$ in (2).

### 2.1. Regularity of the native evolution, including every line point

On the torus write

$$
X=\frac{st}{sx-y},\qquad Y=\frac{sx}{y},\qquad T=st. \tag{5}
$$

The map takes $U_{t,s}$ to $U_{T,s}$. The following formulas explicitly
extend it near each missing torus divisor or accessible line. In the target
chart $(a,b)$ the formulas (4) use phase $T$ rather than $t$.

* On the torus near $sx-y=0$, use target $L_1$ coordinates
  $a=(sx-y)/(st)$ and $b=st/y$.
* On input $L_1$, set $A=1+uv$, $B=s-uA$. Target $L_2$ coordinates are

  $$a=\frac{uA}{s},\qquad
  b=\frac{s^2t(A^2-sv)}{A^2B}.$$

* On input $L_2$, set $A=t+uv$, $B=su^2A-1$. Target $L_3$ coordinates are

  $$a=\frac{uAB}{t},\qquad
  b=\frac{st^2(-v+2suA^2-s^2u^3A^3)}{A^2B^3}.$$

* On input $L_3$, set $A=t+uv$. Target $L_4$ coordinates are

  $$a=u/s,\qquad b=s(sv-A)/t.$$

* On input $L_4$, set $A=s+uv$. Target $L_1$ coordinates are

  $$a=-v/(stA),\qquad b=stu.$$

All displayed denominators are units at the relevant input line: the
values of $A,B$ there are among $1,s,t,-1$. These rational identities,
obtained by substituting (4) into (5), therefore prove that the forward map
$F_t:U_{t,s}\to U_{st,s}$ is a morphism. This check uses no division by
$2$ or $3$. Evaluating at $u=0$ gives exactly the P7 branches. In the
last row $v\ne0$ gives $(X,Y)=(-s^2t/v,1)$, and $v=0$ gives the
target point $(a,b)=(0,0)$ on $L_1$.

For completeness, the state map is bijective over any field. Given an
output phase $T$, the preceding phase is $t=T/s$, and the unique input is:

| Output | Input at phase $T/s$ |
| --- | --- |
| Torus $(X,Y)$, $Y\ne1$ | Torus $(TY/[sX(Y-1)],\ T/[X(Y-1)])$ |
| Torus $(X,1)$ | $L_4$ coordinate $v=-sT/X$ |
| $L_1$ coordinate $W\ne0$ | Torus $(T/(sW),T/W)$ |
| $L_1$ coordinate $0$ | $L_4$ coordinate $0$ |
| $L_2$ coordinate $W$ | $L_1$ coordinate $(1-W/T)/s$ |
| $L_3$ coordinate $W$ | $L_2$ coordinate $W/s$ |
| $L_4$ coordinate $W$ | $L_3$ coordinate $T(W+s)/s^3$ |

Substitution in the seven forward branches verifies every row. The torus
coordinates in the first row are nonzero. Thus over $k$ every state on the
finite phase-union is periodic, not merely eventually periodic.

## 3. Two elementary surface lemmas

### Lemma 3.1. Every integral curve disjoint from $D$ has class $dD$

Work over an algebraically closed field and let $Z$ be an integral curve
disjoint from $D$. Write its integral divisor class as

$$Z=aH_x+bH_y-\sum_{i=1}^8m_iE_i.$$

The eight equations $ZD_i=0$ from (2) give, for some integers $u,v$,

$$
\begin{split}
a&=2u,\quad b=u+v,\quad m_1=2v-u,\\
m_2=m_3&=v,\quad m_4=m_5=m_6=u,\quad m_7=m_8=2u-v.
\end{split} \tag{6}
$$

For clarity, before solving these equations they read

$$
b-m_1-m_7=0,\ m_7-m_8=0,\ a-m_2-m_7=0,\ m_2-m_3=0,
$$
$$
b-m_2-m_4=0,\ m_4-m_5=0,\ m_5-m_6=0,\ a-m_4-m_5=0.
$$

Using the intersection form, (6) yields

$$Z^2=-8(u-v)^2.$$

Adjunction and $ZK_S=-ZD=0$ give

$$p_a(Z)=1+\frac{Z^2+ZK_S}{2}=1-4(u-v)^2.$$

An integral proper curve over an algebraically closed field has
$p_a(Z)=\dim H^1(Z,\mathcal O_Z)\ge0$. Consequently $u=v=d$ and the
class of $Z$ is $dD$. This is linear equivalence, not just numerical
equivalence, because the displayed classes are a free Picard basis.
Finally $d>0$: intersect with an ample class, using that both $Z$ and
$D$ are nonzero effective divisors. This proves the lemma.

### Lemma 3.2. Poles of a nonconstant function on $U$ are uniform

Let $g\in\Gamma(U,\mathcal O_U)$ be nonconstant. Its polar divisor on
$S$ is an effective divisor $P=\sum n_iD_i$. It is nonzero, since a
global regular function on the projective integral surface $S$ is constant.

Choose a constant $c$ over the algebraically closed field such that the
effective zero divisor $C$ of $g-c$ contains none of the $D_i$. Only
finitely many constants are forbidden: a forbidden value must be the
constant residue of $g$ on a component where it has no pole. The polar
divisor of $g-c$ is still $P$, so $C\sim P$ and

$$PD_i=CD_i\ge0.$$

But $PD=0$ by (3). Summing these eight nonnegative integers gives zero;
hence $PD_i=0$ for all $i$. The intersection matrix of the cycle is
minus the graph Laplacian of an eight-cycle, with kernel spanned by the
all-ones vector. Explicitly its equations are
$-2n_i+n_{i-1}+n_{i+1}=0$ cyclically, so successive differences are
equal and therefore zero. Thus

$$P=mD\quad\text{for one integer }m>0. \tag{7}$$

Moreover $CD_i=0$ and $C$ has no common component with $D$; positivity
of local intersection multiplicities implies $C\cap D=\varnothing$.
The two sections with zero divisors $C$ and $mD$ consequently have no
common zero. They define a morphism $g:S\to\mathbb P^1$ with infinity
fibre $mD$. Every finite fibre has class $mD$ and is disjoint from $D$.
Indeed subtracting any finite constant does not change the order $-m$
along any $D_i$, and its zero divisor again has zero intersection with
every $D_i$ and no common component.

The two lemmas hold in arbitrary characteristic. In particular, the
appearance of an integer square in adjunction is an intersection-number
calculation in $\mathbb Z$, not a reduction of the number $4$ modulo the
characteristic.

## 4. The coefficient obstruction: $s^m=1$ for every pole order $mD$

### Lemma 4.1. Minimal-pole divisibility

For any nonconstant $g\in\Gamma(U,\mathcal O_U)$ with polar divisor
$mD$, one has $s^m=1$. Hence, when $s$ has exact order $r$, $r\mid m$.

**Proof.** Restriction to the torus is a Laurent polynomial
$g=\sum c_{a,b}x^ay^b$. Consider first the toric surface obtained by the
four corner blowups $E_2,E_4,E_5,E_7$, before the four smooth-boundary
blowups $E_1,E_3,E_6,E_8$. These latter blowups do not change the
valuation at a generic toric boundary point. The eight toric valuations
of $x^ay^b$ have primitive vectors

$$
(1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(1,2),(-1,-1).
$$

Every valuation of $g$ is at least $-m$. Distinct monomials of equal
valuation remain distinct characters on the associated toric divisor,
so there is no cancellation of an entire leading Laurent polynomial.
The exponents therefore lie in

$$
m\Delta=\operatorname{conv}\{(-m,0),(0,m),(m,0),(m,-m)\}. \tag{8}
$$

For example, the eight inequalities are
$-m\le a\le m$, $-m\le b\le m$,
$a-b\ge-m$, $a+b\ge-m$, $a+2b\ge-m$, and $a+b\le m$;
their intersection is (8).

Let the four vertex coefficients be

$$
A=[x^{-m}]g,\quad B=[y^m]g,\quad
C=[x^m]g,\quad E=[(x/y)^m]g. \tag{9}
$$

Here $B\ne0$. Indeed $g$ has exact pole order $m$ on the strict
transform of $y=\infty$, while (8) has just one exponent with
$b=m$, namely $(0,m)$.

We record carefully why a smooth-boundary blowup imposes a face-root
condition. In local coordinates $(u,v)$ with boundary $u=0$ and
centre $(0,v_0)$, write $g=u^{-m}h(u,v)$ with $h$ regular near the
centre. If the blowup creates an accessible exceptional curve, regularity
of $g$ along its generic point implies that $h$ has multiplicity at least
$m$ at the centre. Restricting $h$ to $u=0$ therefore gives a function
with a zero of order at least $m$ at $v_0$. This is a statement in the
local ring, with no differentiation or division by factorials.

Apply this to the four smooth-boundary blowups. The relevant face
polynomial has degree at most $m$ after multiplication by a unit at the
centre. Its endpoint coefficients are as follows:

| Blowup | Boundary coordinate and face expression | Root condition |
| --- | --- | --- |
| $E_1$ | $u=1/x$, $z=1/y$; coefficient of $u^{-m}$ is a polynomial in $z$ with constant $C$ and top coefficient $E$ | Root $z=1$ of multiplicity at least $m$ |
| $E_3$ | $x=uv$, $y=u^{-1}$; coefficient of $u^{-m}$ is $v^{-m}$ times a polynomial with constant $A$ and top coefficient $B$ | Root $v=t$ of multiplicity at least $m$ |
| $E_6$ | $x=uv$, $y=u^2v$; coefficient of $u^{-m}$ is $v^{-m}$ times a polynomial with constant $A$ and top coefficient $E$ | Root $v=t$ of multiplicity at least $m$ |
| $E_8$ | $x=(uv)^{-1}$, $y=u^{-1}$; coefficient of $u^{-m}$ is $v^{-m}$ times a polynomial with constant $C$ and top coefficient $B$ | Root $v=s$ of multiplicity at least $m$ |

Consequently, including the possibility of an initially zero face
polynomial, comparison with a scalar multiple of $(z-z_0)^m$ gives

$$
C=(-1)^mE,\qquad A=(-t)^mB,\qquad
A=(-t)^mE,\qquad C=(-s)^mB. \tag{10}
$$

As $t\ne0$ and $B\ne0$, the middle two equations give $B=E\ne0$.
The first and last then yield $(-1)^mB=(-s)^mB$, so $s^m=1$.
All of this holds in characteristics two and three as written. ∎

## 5. The source integral exists with exact polar divisor $rD$

This is the one nontrivial dynamical input already proved by the source.
For explicit reproducibility, set $w=1$ in its matrix and write

$$
A(z)=A_0+zA_1+z^2A_2,
$$

$$
A_0=\begin{pmatrix}
t+x-xy&-x\\
t+x-ty-2xy+xy^2&x(y-1)
\end{pmatrix},\quad
A_1=\begin{pmatrix}
y-x+x/y-1-t/x&1\\
y-2x-1+xy+x/y-t/x&1
\end{pmatrix},\quad
A_2=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

Define

$$
I_{r,t}(x,y)=\operatorname{Tr}\bigl(A(s^{r-1})\cdots A(s)A(1)\bigr)
-(t^r+1). \tag{11}
$$

The source proves that this is a Laurent polynomial with coefficients in
$R=\mathbb Z[s]/(\Phi_r(s))$ and satisfies

$$I_{r,st}(F_t(x,y))=I_{r,t}(x,y). \tag{12}$$

This is Theorem 3.1 and its proof, not the source's genus conjecture.
See [Joshi–Roffelsen v2, Section 3.1](https://arxiv.org/html/2508.18578v2#S3.SS1).

### 5.1. Why (11)–(12) remain valid in every allowed characteristic

Here $p\nmid r$, because $r\mid q-1$. An element of exact order $r$
in $k^*$ is a zero of $\Phi_r$ modulo $p$: the factors
$\Phi_d$, $d\mid r$, of $X^r-1$ remain pairwise coprime since
$X^r-1$ is separable. Thus there is a specialization $R\to k$ sending
the cyclotomic parameter to the chosen $s$.

There are no integer denominators in (11). For the identity (12), insert
the rational functions (5) and clear only powers of $x,y,t,s$ and
$sx-y$; the phase parameters $s,t$ are units on the allowed domain.
The resulting numerator belongs to
an integral polynomial/Laurent ring over $R$. It vanishes in its fraction
field by the source theorem, and therefore vanishes in that ring itself.
Specialization consequently preserves (12) as an identity of rational
functions over $k$. No inference from smoothness in characteristic zero
is being made.

For comparison with the source's Lax proof, the identity comes from cyclic
trace invariance of $A(s^{r-1}z)\cdots A(z)$ and telescoping its Lax
compatibility identity. The constant and highest trace coefficients are
$t^r$ and $1$, respectively, and the middle coefficient is (11).
Thus the use of (12) is algebraic, not analytic.

### 5.2. Extension across the four accessible lines

The rational function $I_{r,t}$ is regular on the torus. The generic point
of $L_4$ reaches the torus after one forward step; the generic points of
$L_3,L_2,L_1$ do so after two, three and four steps, respectively. This
follows either from the seven branches or the formulas in Section 2.1:
each intermediate map between line coordinates is affine with nonzero
slope, and the last map is torus-valued for nonzero coordinate.

Those forward maps are morphisms. Repeated use of (12) therefore expresses
$I_{r,t}$ near the generic point of each accessible line as the pullback
of a regular Laurent function on a target torus. Hence $I_{r,t}$ has no
pole along any of those lines. Every other irreducible curve in $U$
meets the torus, so it has no pole there either. Since $U$ is smooth and
therefore normal, the absence of a codimension-one pole implies

$$I_{r,t}\in\Gamma(U,\mathcal O_U). \tag{13}$$

This includes the finitely many special line points: they cannot support
an isolated pole of a rational function on a normal surface. By equality
of regular functions on a dense open, (12) also holds at every point of
$U$ after this extension.

### 5.3. Exact pole order and nonconstancy

At the generic point of $x=0$, with $y$ finite and nonzero,

$$
A(z)=-\frac{tz}{x}V+O(1),\qquad
V=\begin{pmatrix}1&0\\1&0\end{pmatrix},\qquad V^2=V,\quad\operatorname{Tr}V=1.
$$

The order-$x^{-r}$ coefficient of the matrix product in (11) is therefore
$(-1)^r s^{r(r-1)/2}t^rV$. Since the product of all $r$ roots of
$X^r-1$ is $(-1)^{r-1}$,

$$(-1)^r s^{r(r-1)/2}=-1.$$

Consequently

$$I_{r,t}=-t^r x^{-r}+O(x^{-(r-1)}). \tag{14}$$

As $t\ne0$, this leading coefficient never vanishes in any allowed
characteristic. In particular $I_{r,t}$ is nonconstant, and its pole on
the strict transform of $x=0$, namely $D_5$, has exact order $r$.
Combining (13), (14) and Lemma 3.2 proves that its full polar divisor is
exactly $rD$. Thus it defines the asserted morphism

$$f_t:S\longrightarrow\mathbb P^1,\qquad f_t^{-1}(\infty)=rD. \tag{15}$$

## 6. Every finite geometric fibre is integral and reduced

Fix an arbitrary $c\in\bar k$. Lemma 3.2 says that the fibre divisor
$C_c=f_t^{-1}(c)$ is effective of class $rD$ and is disjoint from $D$.
Write its irreducible decomposition over $\bar k$ as

$$C_c=\sum_{j=1}^h n_jZ_j,\qquad n_j\ge1.$$

Lemma 3.1 gives $Z_j\sim d_jD$ with integer $d_j>0$. The linear
equivalence supplies a rational function $g_j$ with divisor
$Z_j-d_jD$. Since $Z_j$ is disjoint from $D$, its polar divisor is
exactly $d_jD$ and $g_j$ is nonconstant and regular on $U$.
Lemma 4.1 now forces $r\mid d_j$ for each $j$.

Comparing classes yields

$$\sum_{j=1}^h n_jd_j=r.$$

Every summand is a positive multiple of $r$. Thus necessarily $h=1$,
$n_1=1$ and $d_1=r$. This proves geometric irreducibility and generic
reducedness of every finite fibre. A fibre of a morphism from a smooth
surface to a smooth curve is an effective Cartier divisor. It has no
embedded associated points; equivalently, locally its defining principal
ideal has only the height-one factors of its divisor. Multiplicity one on
the unique component therefore makes the entire fibre reduced. Hence
$C_c$ is geometrically integral as a scheme.

Adjunction gives

$$
p_a(C_c)=1+\frac{(rD)^2+(rD)K_S}{2}=1. \tag{16}
$$

This proves the claimed assertion for every finite fibre, not merely the
generic fibre. It rules out the proposed dangerous reducible and
nonreduced finite strata, including any component-permutation issue.
It does not require a section of the fibration, connected-fibre descent,
a translation law, an exclusion of quasi-elliptic fibrations, or the
source's proposed equation for singular values.

## 7. Rational-point bounds, including singular fibres

Let $c\in k$ and suppose $C=C_c$ contains a state $P\in U(k)$.
The curve $C$ is projective and geometrically integral, has arithmetic
genus one, and is entirely contained in $U$.

If $C$ is smooth, the point $P$ makes it an elliptic curve over $k$,
and Hasse's theorem gives

$$\#C(k)\le q+1+2\sqrt q. \tag{17}$$

One primary exposition valid for every finite field is
[Sutherland, 18.783, Spring 2021, Theorem 7.3](https://math.mit.edu/classes/18.783/2021/LectureNotes7.pdf),
whose proof is in Sections 7.1–7.2 and imposes no odd-characteristic
restriction on this theorem.

If $C$ is singular, let $\nu:\widetilde C\to C$ be its normalization.
Over the perfect field $k$, $\widetilde C$ is smooth projective and
geometrically integral. The normalization exact sequence, after base
change to $\bar k$, gives

$$
1=p_a(C)=g(\widetilde C)+\sum_{Q\in\operatorname{Sing}(C_{\bar k})}\delta_Q.
$$

Every singular point of a reduced curve contributes a positive integer
$\delta_Q$. Thus in this case $g(\widetilde C)=0$ and there is exactly
one geometric singular point, with total $\delta=1$. These are the usual
normalization and delta-invariant facts; see the
[Stacks Project's delta-invariant section](https://stacks.math.columbia.edu/tag/0C3Q)
and [genus comparison](https://stacks.math.columbia.edu/tag/0CE0).

Always $\#\widetilde C(k)\le q+1$: if it has a $k$-point, genus-zero
Riemann–Roch identifies it with $\mathbb P^1_k$, while otherwise its
point count is zero. Normalization is an isomorphism over the smooth
locus, so each smooth $k$-point lifts uniquely to a $k$-point of
$\widetilde C$. There is at most one remaining rational point, namely
the singular point. Therefore

$$\#C(k)\le\#\widetilde C(k)+1\le q+2\le q+1+2\sqrt q. \tag{18}$$

No assumption about split nodes, cusps, a smooth rational orbit point, or
characteristic greater than three is needed for (18).

## 8. Return to the unchanged native clock

The seven-branch map is a bijection on the finite phase-union by Section
2.1, so every state has a least native period $\ell$. Since its phase
after $n$ steps is $s^nt$, returning the state forces $s^n=1$ and thus
$r\mid\ell$.

Fix a starting phase $t$. The $r$-step map $G=F_{s^{r-1}t}\circ\cdots
\circ F_t$ is a bijection of $U_{t,s}(k)$ and preserves $I_{r,t}$ by
(12). The starting point belongs to a finite fibre, since (13) gives a
finite value at every ordinary state. Its least period under $G$ is
exactly $\ell/r$: the smallest positive multiple of $r$ giving a native
return is $\ell$ itself.

All these $\ell/r$ distinct points lie in the same $C_c(k)$. Applying
(17) or (18) proves (1). This completes the author proof of the original
all-field, all-parameter, all-seven-branch P7 upper bound.

## 9. Scope, novelty boundary and receipt

The source's monodromy integral, state space and target conjecture are
prior ownership. The general connection between roots of unity and
Halphen pencils is also prior ownership. This package supplies a concrete
algebraic divisibility calculation and an all-finite-fibre argument for
this resolved surface; it does not claim these ingredients individually
are new mathematical techniques. The coordinator must separately assess
whether the complete finite-field delta is already in the literature or
is merely a short classical corollary.

The proof establishes the upper-bound part 1.2.A only. It does not prove
the bin-distribution assertion 1.2.B, the explicit singular-fibre
discriminant in source Conjecture 3.6, a general spectral–dynamical
isomorphism, an automorphy statement, or any target Euler factor.

The initial generic-fibre and singular-stratum obligations in
[the frozen attempt](FROZEN_ATTEMPT.md) are discharged here by a stronger
arithmetic-genus-one and finite-fibre-integrality route. In particular,
the proof does not need to claim that the geometric generic fibre is
smooth in every characteristic. This is an improvement in proof route,
not a restriction of the original orbit contract.

Execution receipt: zero mathematical programs, zero enumerations, zero
diagnostic reruns, zero GPUs, zero external-model calls, zero saved source
PDFs, zero Git writes. All calculations above are hand derivations.
Only files in this delegate's authorized directory were edited. The
independent reviewer must check the argument before the coordinator
changes any global status.
