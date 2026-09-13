# Paper30 backup probe: explicit wild covers of nonadditive Hénon maps

Date: 2026-09-06. Status: AUTHOR_FIRST_LEMMAS_ONLY, NOT_A_SELECTED_CANDIDATE.
This is a separate bounded test of portfolio question W while the quantum
candidate is independently assessed. It contributes nothing to that candidate's
page count. No full classification, novelty score or long-paper capacity is
claimed. All assertions labeled proved below are author proofs pending an
independent check. The applicable proof-writer workflow is proof-first, with
no numerical experiments or new formal paper project.

## 1. Assumptions, object and a necessary distinction

Let $K$ be algebraically closed of characteristic $p>0$, $A=K[x,y]$, and
$$
H_P(x,y)=(P(x)-y,x),\qquad \sigma=H_P^*,\qquad \deg P\ge2.
$$
This is a polynomial symplectic automorphism in every characteristic.
Put $\wp(u)=u^p-u$ and $Q_{\rm AS}=A/\wp(A)$ as an additive
$\mathbb F_p$-vector space, not a $K$-vector-space quotient or algebra.

For a nonzero class $[g]$, the cover $z^p-z=g$ has a lift commuting with
the specified deck translations exactly when
$\sigma g-g=\wp(u)$ for a polynomial $u$. An arbitrary lift of the same
connected cover may instead conjugate the deck generator, and its criterion
is $\sigma g-jg=\wp(u)$ for some $j\in\mathbb F_p^*$.
Thus portfolio W's phrase “can lift” must be read as **deck-equivariant
lifting** when its criterion is $\sigma[g]=[g]$. Without that qualification
the two conditions differ for odd $p$.

To justify this distinction, a lift sends the fiber coordinate to $jz+u$
if its action on deck translations is multiplication by $j$. Indeed the
difference of that image and $jz$ is invariant under all translations and
hence belongs to the base ring. Substitution yields the displayed criterion.
Conversely the displayed formula defines a lift, whose inverse is obtained
using $H_P^{-1}$ and division by $j$. For connected degree-$p$ covers every
automorphism of the deck group has this form. This is ordinary
Artin–Schreier theory, not a proposed new theorem.

The broader question of classifying all invariant or finite-orbit classes
in $Q_{\rm AS}$ remains OPEN in this probe.

## 2. Two elementary reduction lemmas

**Lemma 1 — PROVABLE AS STATED.** If $u\in K(x,y)$ and $\wp(u)\in A$,
then $u\in A$. If $\wp(u)\in K[x]$ for polynomial $u$, then $u\in K[x]$.
No polynomial $a xy+f(x)$ with $a\ne0$ belongs to $\wp(A)$.

**Proof.** At a finite prime divisor where $u$ has negative valuation,
$v(u^p-u)=pv(u)<0$, contradicting polynomiality. The factorial normal
ring $K[x,y]$ is the intersection of its height-one valuation rings inside
its fraction field, so $u$ is polynomial. If $\deg_yu=s>0$, then
$\deg_y\wp(u)=ps\ge p$, since its leading $y$ coefficient is the nonzero
$p$th power of the leading coefficient of $u$. It cannot equal a polynomial
of $y$ degree zero or one. This proves both remaining assertions. In
particular the map $a\mapsto[a xy]$ is injective as an additive map.

**Lemma 2 — PROVABLE AS STATED.** Modulo $\wp(K[x])$, each univariate
polynomial has a unique representative with zero constant and only powers
$x^m$ with $p\nmid m$. Reduce a term $c x^{pm}$ to $c^{1/p}x^m$ and
repeat, combining terms on the same Frobenius chain.

**Proof.** The replacement subtracts $\wp(c^{1/p}x^m)$ and lowers the
positive degree. Constants belong to $\wp(K)$ because $K$ is algebraically
closed. The process terminates. A nonzero reduced polynomial cannot be
$\wp(v)$ for nonconstant $v$, whose largest degree is divisible by $p$;
and a constant $v$ cannot produce a nonzero reduced polynomial. Uniqueness
follows by subtraction. This is the standard Artin–Schreier normal form.

## 3. Exact classification only within the bilinear slice

For $a\in K$ and $j\in\mathbb F_p^*$, direct substitution gives
$$
\sigma(a xy)-j a xy=a xP(x)-(1+j)a xy.                 \tag{1}
$$
By Lemmas 1–2, a nonzero bilinear class $[a xy]$ is a $j$-eigenclass if
and only if $j=-1$ and the univariate reduced form of $a xP(x)$ is zero.
This is a necessary and sufficient statement **within this slice**, not
the assertion that every eigenclass has such a representative.

In particular take $q=p^r>2$, $c\in K$ and
$$
P(x)=x^{q-1}+c.                                       \tag{2}
$$
The degree $q-1$ is prime to $p$ and at least two, so the leading term is
not additive. Lemma 2 reduces $a xP(x)$ to
$$
(a^{1/q}+ac)x.
$$
Consequently the exact bilinear $(-1)$-eigenspace is
$$
E_c=\{[a xy]: a^q c^q+a=0\}.                         \tag{3}
$$
When $c=0$, this space is zero. When $c\ne0$, the polynomial in $a$ in
(3) has degree $q$ and derivative one, so it has exactly $q$ distinct
roots in $K$. It is additive and $\mathbb F_p$-linear, so $E_c$ has
dimension $r$ over $\mathbb F_p$. Injectivity of $a\mapsto[a xy]$ ensures
that these are distinct nontrivial classes, not coboundary representatives.

For $p=2$, these are genuine $\sigma$-invariant classes. For odd $p$, their
eigenvalue is $-1$, so they are $\sigma^2$-invariant and each is carried by
$\sigma$ to its negative. This does not assert that $Q_{\rm AS}^{\sigma}$
vanishes or that $E_c$ exhausts $Q_{\rm AS}^{\sigma^2}$.

## 4. A connected degree-$q$ cover and the actual lift

Assume now $c\ne0$ in (2). Choose $t\in K^*$ with
$t^{q-1}=-1/c$ and put $\alpha=t^q$. Thus $\alpha c=-t$.
Define the surface and map
$$
Y:\quad z^q-z=\alpha xy,
$$
$$
\widetilde H(x,y,z)=
(x^{q-1}+c-y,\ x,\ -z+t x).                           \tag{4}
$$

**Claim — PROVABLE AS STATED.** Projection $Y\to\mathbb A^2$ is a
connected finite étale cover of degree $q$, with deck group
$(\mathbb F_q,+)$. Formula (4) is a polynomial automorphism of $Y$
lifting the specified Hénon map. It conjugates deck translation by $b$
to translation by $-b$; its square commutes with every deck translation.

**Proof.** The defining polynomial is monic of degree $q$ in $z$ and
has derivative $-1$, proving finite freeness and étaleness. For connectedness,
use the valuation $v(y)=-1$ of $K(x)(y)$, with $v(K(x)^*)=0$.
At any extension of this valuation to a field containing a root $z$,
the equation forces $v(z)<0$ and $qv(z)=-1$. With the extension still
normalized on the base, its ramification index is divisible by $q$.
The degree of the root field is at least that index and at most $q$;
it is therefore $q$. The polynomial is irreducible and the surface is
integral. The $q$ translations by roots of $b^q-b=0$ supply its full deck
group, since their number equals the degree.

For preservation, compute using $t^q=\alpha$ and $-t=\alpha c$:
$$
(-z+t x)^q-(-z+t x)
=-(z^q-z)+\alpha x^q-t x
=\alpha x(x^{q-1}+c-y).
$$
This is the required equation on the image. Its inverse is polynomial:
$$
(x',y',z')\longmapsto
(y',\ (y')^{q-1}+c-x',\ t y'-z').
$$
Finally applying (4) after $z\mapsto z+b$ changes its last coordinate
by $-b$, proving the stated deck action.

For $b\in\mathbb F_q$, the polynomial
$w_b=\sum_{i=0}^{r-1}(bz)^{p^i}$ satisfies
$w_b^p-w_b=b(z^q-z)=b\alpha xy$. Thus the degree-$p$ character subcovers
of this explicit cover realize precisely the slice in (3): the set of
coefficients is $\alpha\mathbb F_q$, which is exactly its $q$ roots.
For a nonzero $b$ these subcovers are connected by Lemma 1.

## 5. What this first probe does and does not establish

This refutes a possible blanket heuristic that a nonadditive, prime-to-$p$
Hénon map cannot preserve any nontrivial wild cover. It also distinguishes
deck-equivariant invariance from a lift which inverts the deck group.
For example $p=3$, $q=3$, $P=x^2+c$, $c\ne0$, already gives a quadratic
Hénon lift; its nonzero displayed degree-three character classes are
anti-invariant for $H$ and invariant for $H^2$.

These are short explicit results. The surface $xy=\alpha^{-1}(z^q-z)$
is a Danielewski-type surface, and its elementary shift in $z$ produces
a polynomial shear because the change in $z^q-z$ is divisible by $x$.
Nothing here establishes newness of that construction or a complete
classification of covers. The currently proved slice and lift alone must
not be expanded into a 22–30-page paper.

The genuine next feasibility question would be whether, for this fixed
nonadditive family, every finite-orbit Artin–Schreier class can be classified,
or whether a further independent mechanism produces classes outside (3).
At present neither a completeness theorem nor an effective global search
bound is proved. Characteristic-zero Paper29 cannot simply be cited to close
this Frobenius quotient problem.

## 6. Bounded primary-source context and verification boundary

The [Stacks Project, §59.63](https://stacks.math.columbia.edu/tag/0A3J)
gives the Artin–Schreier sequence and the vanishing of higher quasi-coherent
étale cohomology used for its affine interpretation. This is standard
background; the elementary calculations above do not claim that theory.

Leuenberger–Regeta, [*Automorphism groups of Danielewski surfaces*,
§3](https://arxiv.org/html/1710.06045), explicitly write the elementary
fiber shifts on $xy=P(z)$. Their stated base field is $\mathbb C$; this
probe does not apply their characteristic-zero group-classification theorem
in characteristic $p$. It instead proves (4) by direct substitution. The
known elementary formula is a strong reason not to advertise the lift
itself as a new general automorphism construction.

The bounded searches “Henon Artin-Schreier”, “Hénon étale cover positive
characteristic”, and “Danielewski Hénon characteristic” did not locate a
complete theorem for the specific invariant-class problem. This is not a
deep novelty check. Crachiola's *On automorphisms of Danielewski surfaces*
was also located; its advertised family has $x^ny=z^2+h(x)z$, $n\ge2$,
so it must not be silently substituted for the surface in (4).

No numerical run supports these statements: the evidence consists of the
written proofs, still requiring an independent mathematical check. There
is no Route A/B claim, source/publication lock, manuscript or external effect.
