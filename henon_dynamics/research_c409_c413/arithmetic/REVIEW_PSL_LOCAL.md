# Independent mathematical review: the wild rational tower at infinity

2026-09-06. This reviewer is not the author of
`../positive_characteristic/WILD_PSL_RATIONAL_PROOF.md`. The complete
542-line proof was read, including its first cover, two global group
lemmas, simultaneous induction, arithmetic descent and final
ramification calculation. The assigned independent emphasis is the
**local** chain, not another literature search or a substitute for the
coordinator's global simple-quotient/Goursat review.

Read version SHA-256:
`7aed6eaa51bd1b9d181d372566b0a50744591f5f2b0cbb9d51f6c720d17abe00`.
Line locators below refer to that version.

## Claim, assumptions and status

The map is $f(X)=X^p+X^{-1}$, with prime $p\geq5$,
$m=(p-1)/2$ and $b=m+1=(p+1)/2$. At height $n$ the geometric
Galois completion $F_n$ at infinity is asserted to have
$$
 e(F_n/k((1/t)))=mp^n,\qquad
 D(F_n/k((1/t)))=p^{n+1}-(m+2),
$$
and
$$
 I_n\simeq(C_p)^n\rtimes C_m,\qquad
 (I_n)_1=\cdots=(I_n)_b=(C_p)^n,\quad (I_n)_{b+1}=1,
$$
with faithful scalar tame action. Here the constants are algebraically
closed and all completion valuations are normalized to have value
group $\mathbb Z$. The arbitrary-field assertion in the overall
theorem refers to the separately treated arithmetic global extension;
the residue-field hypotheses are not silently dropped from the local
lemma.

**Status: PROVABLE AS STATED for this local package.** I found no
required weakening, missing local hypothesis, incorrect pole-difference
estimate, or circular local step. This conclusion follows from the
calculations below, not from the author's stated proof status.
The global group order and regularity require the separate global
review; the genus formula is correct once that global order is known.

No C-number, formal admission, priority certificate, human external
review or manuscript approval is supplied by this file.

## Dependency map actually checked

1. The first-level explicit AS model gives normalized pole valuations
   $-m$ and pairwise pole differences of valuation one.
2. Lemma 3.1 proves that integral parameters split and sufficiently
   close pole parameters have the same nontrivial cyclic AS field.
3. At level $n$, all pole parameters therefore yield one common local
   extension of degree $p$; this determines $e_{n+1}$ before new-level
   closeness is proved.
4. The normalized valuation is then multiplied by $p$ on the old
   field. The difference identity for two new children closes the
   closeness induction in that new normalization.
5. The rational root-path completion independently determines the
   different, using the already established total local index.
6. Closeness bounds all wild ramification numbers from below; the
   exact different forces every one of these bounds to be an equality.
7. The single positive lower graded quotient gives elementary-abelian
   wild inertia and the tame scalar action.

Neither an elementary-abelian wild group nor a guessed unique jump
is used to compute the different. This avoids a possible circular
route to the claimed filtration.

## 1. Initial place and nonpole splitting

In the first model $w^p-w=v^{-b}$, the order $b$ is positive and
prime to $p$. The AS class is nonzero by its pole order. At the place
over $v=0$, the normalized values are
$$
 v_{F_1}(v)=p,\quad v_{F_1}(w)=-b,\quad v_{F_1}(t)=-mp.
$$
For $x_i=v^m+v^{-1}/(w+i)$, the second term has value
$-p+b=-m$, strictly below the value $mp$ of the first term. For
$i\ne j$,
$$
 v_{F_1}(x_i-x_j)=-p+2b=1.
$$
Thus both initial normalized assertions really hold; the pairwise
difference is not inferred merely from equal pole orders.

For an integral parameter $A$, the reduction of
$X^{p+1}-AX+1$ is separable: a root of its derivative $X^p-A$
would make the polynomial equal to $1$. All residue roots exist
because the residue field is algebraically closed, and each lifts
uniquely. Therefore such a parameter gives complete local splitting,
not just absence of ramification. This is the precise input used
both for the support separation and the local compositum.

## 2. Exact AS field of a pole parameter

For $v_K(A)=-m$, the equation
$$s-A^{-1}(1+s^{p+1})=0$$
has a unique root in the maximal ideal, since its derivative at the
residue root zero is one. The equality gives $v_K(s_A)=m$.
Dividing out the $m$th power of a uniformizer, the remaining unit has
an $m$th root by algebraic closedness of the residue field and
$p\nmid m$. Thus $v_A^m=s_A$ with $v_K(v_A)=1$ is justified.

The original root formula with $r=s_A$ then gives all roots over
$$K(w_A),\qquad w_A^p-w_A=v_A^{-b}.$$
Conversely, the generator-recovery formula shows that this is the
splitting field, not a proper containing extension. Its degree is
exactly $p$: an AS coboundary with a pole has pole order divisible
by $p$, whereas $v_A^{-b}$ has pole order $b$. In particular, this
local extension is not trivial or merely bounded above by $p$.

Changing $v_A$ to $\zeta v_A$ with $\zeta^m=1$ scales the right
side by $\zeta^{-b}\in\mathbb F_p^*$. Such multiplication changes
an AS generator by the same nonzero $\mathbb F_p$ scalar and leaves
its field unchanged. The use of the prime field here is valid since
$m\mid p-1$.

## 3. Pole differences and equality of AS classes

For distinct pole parameters $A,B$ with $v_K(A-B)\geq1$, put
$q=v_K(s_A-s_B)$. Since both small roots have value $m$,
$q\geq m>0$. In
$$
 A-B=(s_A-s_B)^p-\frac{s_A-s_B}{s_As_B},
$$
the two terms have values $pq$ and $q-2m$. Their difference is
$(p-1)q+2m>0$, so the second term strictly dominates. Hence
$$
 q=v_K(A-B)+2m\geq2m+1.
$$
The roots $v_A,v_B$ can be chosen with $v_B/v_A$ reducing to one:
their $m$th-power ratio is $s_B/s_A\equiv1$, and every residual
$m$th root can be corrected by an element of $\mu_m$. With this
choice, since $p\nmid m$,
$$
 v_K(v_B/v_A-1)
 =v_K(s_B/s_A-1)
 =q-m\geq m+1=b.
$$
It follows that
$$
 \begin{aligned}
 v_K(v_B^{-b}-v_A^{-b})
 &= -b+v_K\bigl((v_B/v_A)^{-b}-1\bigr)\\
 &\geq0.
 \end{aligned}
$$
There is no lost factor of $p$ in this estimate. In fact $p\nmid b$
as well, although the displayed lower bound suffices.

Every integral element is an AS coboundary **in this completion**:
solve $z^p-z=\overline c$ in the algebraically closed residue field
and lift with derivative $-1$. Therefore the two AS right sides
represent the same class and give exactly the same embedded cyclic
extension. If $A=B$, choose the same small root and $m$th root;
the assertion is immediate and no finite valuation of zero is needed.

## 4. All-height local degree and the new closeness estimate

Fix a place of $L_n$ over infinity. Its $p^n$ pole parameters have
value $-m$ and pairwise differences of value at least one. Section 3
therefore identifies every child splitting field with a single cyclic
degree-$p$ field over $F_n$. All other parameters split already over
$F_n$. Since there is at least one pole, the compositum degree is
exactly $p$, not one. Algebraically closed residues exclude a
nontrivial residue extension, so the ramification index also grows
by precisely $p$.

Now normalize $v=v_{F_{n+1}}$. Its restriction to $F_n$ is
$p v_{F_n}$. Every new pole $u$ has pole parent $A$ with
$v(A)=-pm$. In $A=u^p+u^{-1}$ the first term dominates, yielding
$v(u)=-m$. For two distinct new poles $u,v$ and $h=u-v$,
$$
 A-B=h^p-h/(uv),\qquad v(uv)=-2m=-(p-1).
$$
If $q=v(h)<1$, the right-side term values are
$$pq\quad\text{and}\quad q+(p-1),$$
and their difference is $(p-1)(q-1)<0$. Thus the sum has value
$pq<p$, contradicting either $v(A-B)\geq p$ for distinct parents
or $A-B=0$ for equal parents. The next-level closeness follows.

This uses the new valuation only after the degree-$p$ compositum
has been established. Equal-parent pairs are covered explicitly;
they are not silently excluded from the all-pole assertion.

## 5. Independent computation of the different

In the rational root field along the pole path, $u=1/X$ is a
uniformizer and the base parameter is
$$
 h^{\circ n}(u),\qquad
 h(u)=\frac{u^p}{1+u^{p+1}},\qquad
 h'(u)=-\frac{u^{2p}}{(1+u^{p+1})^2}.
$$
The derivative is nonzero in characteristic $p$; the root completion
is separable and has local degree $p^n$, from the leading order of
$h^{\circ n}$. The chain rule gives
$$
 v_u\bigl((h^{\circ n})'(u)\bigr)
 =\sum_{j=0}^{n-1}2p\,p^j
 =\frac{2p(p^n-1)}{p-1}.
$$
This is the different exponent of the Laurent-series root extension.
The full Galois completion has degree $mp^n$, already established
above. Its relative degree over the root completion is $m$, prime
to $p$. Both residue fields are the same algebraically closed field,
so that extension is tame and its different exponent is $m-1$.
Transitivity gives
$$
 D_n=(m-1)+m\frac{2p(p^n-1)}{p-1}
 =p^{n+1}-(m+2).
$$
No additional ramification outside infinity was omitted: the first
map has no finite critical value, and its sole branch value infinity
is fixed. Composition and Galois closure remain unramified at finite
target places.

## 6. The unique lower jump is forced, not assumed

The pole-root completion has degree $p^n$. Consequently its inertia
orbit has $p^n$ roots and a stabilizer of order $m$. These are exactly
all the poles counted in the subtree. Since wild inertia has order
$p^n$, it intersects that stabilizer trivially and acts regularly
on the pole roots.

Choose $\rho$ with $\rho^m=1/\alpha$ for a pole root $\alpha$;
it is a uniformizer of $F_n$. For nonidentity wild $\sigma$, set
$z=\sigma\rho/\rho$. Then $z\equiv1$ and
$$
 z^m=\alpha/(\sigma\alpha),\qquad
 v(z^m-1)=v(\sigma\alpha-\alpha)+m.
$$
As $p\nmid m$, $v(z-1)=v(z^m-1)$. Thus
$$
 i(\sigma)=v(\sigma\rho-\rho)
 =1+m+v(\sigma\alpha-\alpha)\geq b+1.
$$
Every element outside wild inertia has ramification number one.
Hilbert's formula therefore bounds the different by
$$
 (m-1)p^n+(p^n-1)(b+1)=p^{n+1}-(m+2).
$$
This equals the independently computed different. Each termwise
inequality must be an equality, so every nonidentity wild element
has ramification number exactly $b+1$. The lower filtration is
therefore exactly the claimed one. The jump $b$ is a **lower** jump;
the corresponding positive upper jump would be $b/m$, not $b$.
The manuscript correctly labels its stated filtration as lower.

## 7. Elementary-abelian wild inertia and scalar tame action

With $(I_n)_{b+1}=1$, the map
$$
 \sigma\longmapsto
 \overline{\frac{\sigma\rho-\rho}{\rho^{b+1}}}
$$
identifies $(I_n)_b$ with a finite subgroup of the additive residue
field. The composition law adds the leading coefficients; its kernel
is $(I_n)_{b+1}$. Hence wild inertia is an elementary-abelian group
of order $p^n$, and therefore rank $n$. This does not need a prior
commutativity or exponent-$p$ assumption.

The tame quotient is cyclic of order $m$. Schur–Zassenhaus splits
the inertia extension because $m$ is prime to $p$. If $\chi$ is
the tame uniformizer character, conjugation on the positive graded
quotient multiplies its leading coefficient by $\chi^{b}$ or
$\chi^{-b}$ according to the character convention. These give
isomorphic semidirect descriptions after inverting the cyclic
generator. Since $\gcd(b,m)=1$ and $\mu_m\subset\mathbb F_p^*$,
the action is a faithful scalar action on every vector coordinate,
as claimed. There is no unexamined nonscalar representation here.

Using this different and index in the one-branch-point
Riemann–Hurwitz formula gives exactly the stated genus once the
global group order is supplied. At $n=1$ it reduces to $m^2$, also
matching the genus of $w^p-w=v^{-b}$.

## Precise revision requests and residual scope

**No mandatory mathematical repair was found in the reviewed local
claims.** The following are small, nonblocking manuscript clarifications:

1. Fix `W_n,qquad` in (T1), line 32, to `W_n,\qquad`.
2. At lines 461–465, add that the local root degree $p^n$ proved
   immediately above is what gives a single inertia orbit of all
   $p^n$ pole roots. Their number alone would not establish transitivity.
3. At line 493, name Schur–Zassenhaus rather than only saying that
   the extension splits by coprimality.
4. Keep the algebraically closed residue-field scope visible when
   extracting integral AS coboundaries and unit $m$th roots. Do not
   promote Lemma 3.1 unchanged to arbitrary arithmetic residue fields.
5. Retain the explicit lower-numbering label for the unique jump;
   do not replace it by an unqualified or upper jump in an abstract.

These requests do not change the theorem, introduce extra assumptions
or rescue a failed proof. The main remaining admission questions are
the separately assigned global proof and nearest-owner comparison.
No whole-tower literature check was duplicated here.

As an arithmetic sanity check only, the reviewer also evaluated the
two different expressions and the Hilbert lower-bound expression for
$p=5,7,11,13,17,19$ and $1\leq n\leq6$: all 36 exact identities
agreed, as did the six first-level genus identities. These finite
calculations are not the basis of the all-height proof judgment.

### Author-side typo correction confirmed

After the review, the author fixed request 1. The updated proof hash is
`75d3ff79f0bf877852c19a2a0a38b1fecd3016bd0cb980386eef9b63c0cbacdd`.
The reviewer checked the corrected (T1) display. Reversing only this
single text substitution in a read-only stream reproduces the original
read-version hash, so no mathematical content changed in that update.
