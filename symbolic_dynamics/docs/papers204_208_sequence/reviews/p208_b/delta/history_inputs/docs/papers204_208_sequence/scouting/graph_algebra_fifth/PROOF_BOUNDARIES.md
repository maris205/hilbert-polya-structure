# Fifth scout proof boundaries

2026-09-05 UTC. Author: batch197_fifth_scout.
Status for the proposed all-parameter, two-axis admission of every row:
**NOT CURRENTLY JUSTIFIED / NO_PROMOTION**.
The corrected statements below are **PROVABLE AFTER WEAKENING**.
They are scout deductions, not a manuscript contract or independent review.

## Assumptions and notation

All groups below are finite, with identity $e$; multiplication is ordered
as written. Symmetric groups act by composition $(gh)(i)=g(h(i))$.
A field $K$ may be arbitrary in the XCY identities; the literal finite
carriers use $K=\mathbb F_p$. XCY indices belong to $\mathbb Z/4\mathbb Z$.
Cross and dot products are the coordinate polynomial operations in $K^3$;
no Euclidean positivity or division by a norm is assumed.

For a finite self-map $F$, a state's tail is its least time to a periodic
point; $H(F)$ is the maximum tail. An inverse fibre is the full source set
over a specified target, including empty fibres. Pilot values of these
quantities are not all-parameter theorems.

## Strategy and dependency map

1. GHD: solve the two target equations exactly; the complete inverse is a
   classical square-root problem. This requires only group cancellation.
2. TQP: compute one conjugacy invariant. It does not reconstruct an orbit.
3. XCY: derive the double-cross identity; derive determinant feedback;
   embed the two-step map in a monomial system. A zero coordinate then
   propagates on the four-cycle. No nonzero determinant division is used.
4. DCP: prove the canonical representative convention and analyze only
   the closed affine/quadratic strata.
5. UOP: count ordered representations by set intersection; derive a dense
   source collapse and the abelian control. These are static facts.
6. WPP: use the quotient derivation and product rule; the unit ratio is
   only a partial coordinate. Analyze characteristic two separately.

## 1. GHD: full classical inverse adapter

The literal is $F(g,h)=(gh,g^{-1}h)$ on $G^2$.

**Corrected claim.** For every target $(u,v)\in G^2$ there is a bijection
$$
 \{g\in G:g^2=uv^{-1}\}\longrightarrow F^{-1}(u,v),
 \qquad g\longmapsto(g,g^{-1}u).
$$

**Proof.** Step 1: a source satisfies
$uv^{-1}=gh(h^{-1}g)=g^2$ and $h=g^{-1}u$.

Step 2: conversely, $g^2=uv^{-1}$ implies $u=g^2v$. Setting
$h=g^{-1}u$ gives $gh=u$ and $g^{-1}h=g^{-2}u=v$.
The maps are inverse because the first source coordinate recovers $g$.

Step 3: if $r_2(w)=|\{g:g^2=w\}|$, then every target fibre has size
$r_2(uv^{-1})$. Let $Q=\{g^2:g\in G\}$. For each $v$ the eligible targets
are exactly $(wv,v)$ with $w\in Q$, so $|\operatorname{im}F|=|G||Q|$.
The maximum fibre is $\max_w r_2(w)$ and its complete target set is obtained
by pulling back the maximizing $w$ under $(u,v)\mapsto uv^{-1}$.

For $G=S_n$, write $a_\ell$ for the number of $\ell$-cycles in $uv^{-1}$.
The classical permutation-root formula gives
$$
 r_2(uv^{-1})=\prod_{\ell\ge1}Q_\ell(a_\ell),
$$
where, for even $\ell$,
$$
 Q_\ell(a)=
 \begin{cases}
 0,&a\text{ odd},\\
 a!\ell^{a/2}/(2^{a/2}(a/2)!),&a\text{ even},
 \end{cases}
$$
and, for odd $\ell$,
$$
 Q_\ell(a)=\sum_{j=0}^{\lfloor a/2\rfloor}
 \frac{a!\ell^j}{2^j j!(a-2j)!}.
$$
Empty cycle classes contribute one. This is the $m=2$ specialization of
Leaños–Moreno–Rivera-Martínez, Theorem 1, not a new counting result.
The explicit adapter deducts the whole one-step inverse axis. It does not
supply an all-$G$ temporal theorem. In an abelian group the literal is an
ordinary linear group endomorphism with coefficient matrix
$\left(\begin{smallmatrix}1&1\\-1&1\end{smallmatrix}\right)$; that control
is not a linearization of the noncommutative carrier.

**Open risk.** No all-$S_n$ sharp tail, recurrent atlas or independent
remaining second axis has been proved. The permutation-root formula
does not count roots inside an arbitrary subgroup by Cayley embedding.

## 2. TQP: a conjugacy invariant, not an atlas

The literal is $F(g,h)=(g^2h,gh^2)$ on $G^2$.

**Corrected claim.** If $d=gh^{-1}$ and $(u,v)=F(g,h)$, then
$uv^{-1}=g d g^{-1}$. Thus the conjugacy class of $gh^{-1}$ is invariant.

**Proof.** Direct ordered cancellation gives
$$
 uv^{-1}=g^2h(h^{-2}g^{-1})=g^2h^{-1}g^{-1}
          =g(gh^{-1})g^{-1}.
$$
This uses neither commutativity nor nilpotency. It supplies no deterministic
update for $d$ alone because the conjugator $g$ is still needed.
On abelian groups the system is the classical linear group endomorphism
with matrix $\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)$.

**Open risk.** The noncommutative full-carrier clock, all cycle lengths and
target-resolved inverse remain unproved. The old involution-restricted
mutual sandwich $(aba,bab)$ is a different literal; no conjugacy to that
old product-cubing system is asserted.

## 3. XCY: exact two-step monomial restriction and zero basin

Let $F(u)_i=u_i\times u_{i+1}$ and
$d_i(u)=\det(u_i,u_{i+1},u_{i+2})$.

**Corrected claims.** Over every field, including characteristic two,
$$
 F^2(u)_i=d_i(u)u_{i+1},\qquad
 d_i(F(u))=d_i(u)d_{i+1}(u).
 \tag{X1}
$$
The full two-step map embeds bijectively onto an invariant subvariety of
a monomial self-map on $K^{16}$. If any $d_i(u)=0$, then $F^5(u)=0$.
This zero-basin bound is sharp over every field. If all $d_i(u)\ne0$,
the orbit never reaches zero; hence the basin of zero is exactly the
set with at least one zero cyclic determinant.

**Proof.** Step 1: the vector triple-product identity, obtained by expanding
the coordinate determinants, is
$A\times(B\times C)=B(A\cdot C)-C(A\cdot B)$.
Set $A=a\times b$, $B=b$, $C=c$; then
$$
 (a\times b)\times(b\times c)=b\det(a,b,c),
$$
because $(a\times b)\cdot b=0$. These are integral polynomial identities
and remain valid in every characteristic.

Step 2: applying this identity to $(b,c,d)$ and taking the dot product
with $a\times b$ gives
$$
 \det(a\times b,b\times c,c\times d)
 =\det(a,b,c)\det(b,c,d).
$$
This proves both identities in (X1), with no nonsingularity assumption.

Step 3: define the injective graph embedding
$$
 \iota(u)=(d_0(u),\ldots,d_3(u),u_0,\ldots,u_3).
$$
On independent coordinates $(z_0,\ldots,z_3,w_0,\ldots,w_3)$, with each
$w_i\in K^3$, define
$$
 \mathcal M(z,w)=
 \big((z_i z_{i+1}^2z_{i+2})_{i=0}^3,\,
      (z_iw_{i+1})_{i=0}^3\big).
$$
Every scalar coordinate is a monomial. Applying (X1) twice proves
$\mathcal M\circ\iota=\iota\circ F^2$. Thus the graph of the four
determinant equations is invariant and the restriction there is conjugate
to $F^2$. This is not a claim that the full $F$ is conjugate to an
unrestricted monomial map, or that $\iota$ is onto $K^{16}$.
The determinant factor itself is $z_i\mapsto z_i z_{i+1}$.

Step 4: if $d_i(u)=0$, then $F^2(u)_i=0$. A zero at position $i$ forces
zeros at $i$ and $i-1$ in the next step. Three more steps cover the four
positions, proving $F^5(u)=0$. If every initial determinant is nonzero,
the determinant identity preserves that property at every time, and a
zero state is impossible. This also proves the exact basin criterion.

Step 5: for a sharp witness take standard coordinate vectors and
$$
 u=(e_3,e_2,e_2+e_3,e_1).
$$
Its four determinants are $(0,1,-1,-1)$, and direct (X1) gives
$$
 F^2(u)=(0,e_2+e_3,-e_1,-e_3),\quad
 F^3(u)=(0,-e_2+e_3,-e_2,0),\quad
 F^4(u)=(0,e_1,0,0),\quad F^5(u)=0.
$$
The fourth state is nonzero in every field. Since a state that reaches
zero cannot previously lie on another cycle, its tail is exactly five.

**Deduction boundary.** The double-cross determinant/scaled-shift engine
lies on the occupied adjugate/monomial surface. The all-zero support
propagation is the elementary four-cycle support clock. The small
$p=2,3$ period-eight cores do not establish such a core for every prime.
No full one-step target inverse, uniform extremal fibre or all-$q$
nonzero recurrent count has been proved. Merely naming the invariant
determinant variety does not produce the missing enumerative result.

## 4. DCP: canonical convention and low-degree strata only

A state is the unique polynomial $f$ of degree $<p$ representing a function
$\mathbb F_p\to\mathbb F_p$. The update is the degree-$<p$ representative
of $f'\circ f$ modulo $X^p-X$.

**Corrected claim.** This is a well-defined finite self-map only with the
specified canonical differentiation convention. Its affine stratum enters
zero in at most two steps. For odd $p$, the degree-at-most-two stratum is
invariant and obeys
$$
 aX^2+bX+c\longmapsto
 2a^2X^2+2abX+(2ac+b).
$$

**Proof.** Step 1: evaluation on $\mathbb F_p$ is injective on polynomials
of degree $<p$, since a nonzero such polynomial has fewer than $p$ roots.
The coefficient space and function space both have $p^p$ elements;
evaluation is therefore bijective and fixes the canonical representative.

Step 2: differentiation is not an operation on arbitrary representatives
modulo $X^p-X$, whose derivative is $-1$ rather than zero in this quotient.
Applying it first to the unique representative removes that ambiguity.

Step 3: for $f=a+bX$, the derivative is the constant $b$, which maps to
zero next. For a quadratic in odd characteristic,
$f'=2aX+b$ and $f'\circ f=2af+b$, giving the displayed formula without
any reduction of degree.

**Open risk.** The quadratic scalar/multiplier recurrence controls only
that invariant stratum. At $p=5$ the full carrier already includes degrees
three and four and has height twelve. No all-prime temporal spine or
all-target decoder is proved. Old canonical advection $f\mapsto ff'$
is not this composition literal; both share the representative caution.

## 5. UOP: ordered unique products, static facts only

For $S\subseteq G$, let $r_S(z)=|\{(a,b)\in S^2:ab=z\}|$ and
$F(S)=\{z:r_S(z)=1\}$. Diagonal pairs are included.

**Corrected claim.** For every $z$,
$$
 r_S(z)=|S\cap zS^{-1}|\ge 2|S|-|G|.
$$
In particular, if $|S|>(|G|+1)/2$, then $F(S)=\varnothing$.
The empty set is fixed and $F(\{a\})=\{a^2\}$.

**Proof.** Once $a$ is chosen, the only possible partner is $b=a^{-1}z$.
The condition $b\in S$ is equivalent to $a\in zS^{-1}$.
Both intersected subsets have size $|S|$, so inclusion-exclusion in $G$
gives the lower bound. Under the displayed density assumption the
integer lower bound is at least two for every $z$. The empty and
singleton statements follow directly from the count.

If $G$ is abelian, each off-diagonal ordered representation is paired
with the distinct representation $(b,a)$. Consequently a unique product
must come from exactly one diagonal square and no off-diagonal pair.
This is not the old unordered-distinct UPR rule: in an elementary
abelian two-group, $S=\{e,a\}$ with $a\ne e$ gives $F(S)=\varnothing$,
whereas UPR outputs $\{a\}$ in additive notation.

**Open risk.** This literal distinction and static density test provide
no all-group recurrent atlas or complete inverse. The group-ring square
coefficient at $z$ is exactly $r_S(z)$, but replacing a coefficient by the
predicate that it equals one is nonlinear; ordinary subset multiplication
or a parity-linear map is not an asserted conjugacy.

## 6. WPP: unit-ratio limitation and characteristic-two closure

For $R_p=\mathbb F_p[X]/(X^p)$ set
$F(f,g)=(f'g-fg',fg)$ on the whole $R_p^2$.

**Corrected claim.** Formal differentiation induces a derivation of $R_p$.
If $f,g$ are units, the output coordinate ratio is
$$
 \frac{f'g-fg'}{fg}=\frac{f'}f-\frac{g'}g
                  =\frac{(f/g)'}{f/g}.
$$
For $p=2$, all states reach a fixed point in at most two steps, and the
bound is sharp. Its fixed points are $(0,0),(1,X),(1,1+X)$.

**Proof.** Step 1: the derivative of $X^ph$ equals $X^ph'$ in characteristic
$p$, so the ideal $(X^p)$ is stable under differentiation. The product
rule descends. Inverting units and differentiating $gg^{-1}=1$ proves
the ratio identity.

Step 2: at $p=2$, write $f=a+bX$ and $g=c+dX$ and put
$w=bc+ad$, $z=ac$. In $R_2$,
$$
 F(f,g)=(w,z+wX),\qquad F^2(f,g)=(w,wz+wX).
$$
If $w=0$ the second state is $(0,0)$; if $w=1$ the first state is already
fixed. The only possible fixed points in the first image are exactly
the three listed states, and direct substitution verifies each.
The source $(1,1)$ maps to $(0,1)$ and then $(0,0)$, so its tail is two.

**Open risk.** Even with unit inputs, the next first coordinate can be a
nonunit; for example $f=g$ gives zero. The displayed ratio is not a
global coordinate conjugacy and cannot erase the nonunit strata.
Characteristic two alone is not an all-prime family theorem.
No all-prime recurrent/inverse package is currently justified.

## Final mathematical disposition

All six literals remain **NO_PROMOTION**, with zero reserves. GHD has a
complete but classical inverse axis; XCY has a precise occupied temporal
reduction and a shallow support clock. TQP, DCP, UOP and WPP do not have
the required all-parameter conjunction. None is rescued by enlarging its
fixed initial enumeration box. Correct lemmas above are retained as
negative scouting evidence, not relabelled as eligible papers.
