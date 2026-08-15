# Proof Package

## Claim

For every integer $q\ge2$, let

$$
G_q=\operatorname{Cent}_{\mathrm{GL}_2(\mathbb Z/q\mathbb Z)}(A),
\qquad
X_q=\mathrm{CV}_q,
\qquad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
$$

Use the Paper-10 torsor isomorphism to identify $X_q$ with the left regular
$G_q$-set and write $a_q=A\in G_q$ and
$\phi_q(x)=a_qx$.  Put

$$
n_q=|G_q|,
\qquad
r_q=\operatorname{ord}(a_q),
\qquad
m_q=n_q/r_q,
\qquad
\mathbf u_q=[G_q/\{e\}]\in B(G_q).
$$

More generally, for a finite abelian group $C$, an element $a\in C$, and a
finite $C$-set $X=\coprod_K n_K(C/K)$, put
$H=\langle a\rangle$ and $d_K=[H:H\cap K]$.  The proof first establishes
the full information-loss hierarchy for this general object and then
specializes it to the regular Paper-10 torsor.

Then:

1. the point-order rational Burnside zeta is
   $(1-t^{r_q})^{-\mathbf u_q/r_q}$;
2. the orbit-order integral Burnside zeta is
   $(1-t)^{-\mathbf u_q}$;
3. cardinality and orbifold reduction yield, respectively,

   $$
   (1-t^{r_q})^{-m_q},\quad
   (1-t^{r_q})^{-1/r_q},\quad
   (1-t)^{-n_q},\quad
   (1-t)^{-1};
   $$

4. the 2013 $G_q$-permutation zeta is the actual finite permutation
   $(X_q,\phi_q)$, whose $(\mathbb Z\times G_q)$-stabilizer is
   $\langle(1,a_q^{-1})\rangle$ and whose irreducible triple is
   $(\{e\},1,a_q^{-1})$;
5. the enhanced Burnside class is
   $\widehat X_{\{e\},1,a_q,1}$, but its enhanced orbifold zeta is
   $(1-t)^{-1}$;
6. the action groupoid $G_q\ltimes X_q$ is equivalent to the terminal
   groupoid and the endofunctor induced by $\phi_q$ is naturally isomorphic
   to identity;
7. each of the $m_q$ source cycles shortens by $1/r_q$ and all $m_q$ glue to
   the quotient fixed point; and
8. these facts retain source/order/twist data in definition-dependent ways,
   but do not produce an intrinsic modulus or prime clock.  The same formulas
   hold for composite $q$, and the frozen values include
   $r_2=r_4=3$ and $r_6=r_9=12$.
9. in the general finite $C$-set, the source zeta is
   $\prod_K(1-t^{d_K})^{-n_K[C:HK]}$, the coarse quotient zeta is
   $(1-t)^{-\sum_Kn_K}$, the point-order Burnside exact class is
   $P_m^C=\sum_{d_K=m}n_K[C/K]$, and the $C$-permutation stabilizer on
   $C/K$ is $\langle0\times K,(1,a^{-1})\rangle$;
10. the effective action
    $C_6/C_2\sqcup C_6/C_3$ with generator $a\in C_6$ has source periods
    $3$ and $2$ but no period-$6$ factor, while its quotient and five inertia
    sectors are static.

## Status

**PROVABLE AS STATED**.

The theorem is a specialization and comparison of existing definitions.  It
does not prove that every possible equivariant, orbifold, stacky, weighted,
or representation-valued construction fails.

Terminal classification supported by the proof:

`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /`
`A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

## Assumptions

- Paper 10's terminal theorem is used as a bound upstream fact:
  $G_q$ is finite abelian and $X_q$ is a free transitive $G_q$-set.
- The action is left multiplication.  The base-point identification sends
  $e\in G_q$ to $e_1\in X_q$.
- The point-order rational Burnside zeta is the 2008 construction based on
  the fixed-point equivariant Lefschetz class.  The orbit-order integral
  Burnside zeta is the distinct 2015 construction based on fixed
  $G$-orbits; the 2015 paper discusses both Lefschetz sequences.  They are
  never treated as one invariant.
- The $G$-permutation zeta uses Gusein-Zade (2013) and therefore all twisted
  values $L^G(g\phi^m)$, not only $L^G(\phi^m)$.
- The enhanced class and enhanced orbifold zeta use
  Ebeling--Gusein-Zade (2018).
- The quotient-stack conclusion applies only to invariants that are Morita
  invariant and invariant under $2$-isomorphism of the induced endomorphism.
- No numerical value of $s$, $\log q$, or $q^{-s}$ is introduced.

## Notation

- $B(G)=K_0(\mathrm{f.}\,G\text{-sets})$ is the Burnside ring.
- $K_0(\mathrm{f.}\,G\text{-perm})$ is the Grothendieck ring of finite
  $G$-permutations, equivalently finite $(\mathbb Z\times G)$-sets.
- $\kappa_G:B(G)\to\mathbb Z$ is the cardinality homomorphism.
- $\Phi_G:B(G)\to\mathbb Z$ is the additive orbifold homomorphism of
  abelian groups.  For abelian $G$, $\Phi_G([G/H])=|H|$.  It is not a ring
  homomorphism for the Cartesian Burnside product: if
  $\mathbf u=[G/1]$ and $G$ is nontrivial, then
  $\mathbf u^2=|G|\mathbf u$ but
  $\Phi_G(\mathbf u^2)=|G|\ne1=\Phi_G(\mathbf u)^2$.
- For an additive map $\psi:B(G)\to R$, $\psi_*$ denotes exponent reduction:

  $$
  \psi_*\!\left(\prod_{m\ge1}(1-t^m)^{-s_m/m}\right)
  =\prod_{m\ge1}(1-t^m)^{-\psi(s_m)/m}.
  $$

  This notation does not claim that $\psi$ preserves Burnside
  multiplication, the pre-$\lambda$ structure, or the power structure.  For
  $\Phi_G$, it agrees with the 2015
  definition obtained from the orbifold Lefschetz sequence.  Marks are
  applied only to $L^G(\phi^m)$ or $s_m^G$, not naively to Burnside powers.
- $L^G$ counts fixed points as a virtual finite $G$-set.
- $\widetilde L^G$ counts setwise fixed $G$-orbits decorated by orbit type.
- $s_m^G$ and $\widetilde s_m^G$ are defined by divisor inversion:

  $$
  L^G(\phi^k)=\sum_{m\mid k}s_m^G,
  \qquad
  \widetilde L^G(\phi^k)=\sum_{m\mid k}\widetilde s_m^G.
  $$

- $\mathcal G_q=G_q\ltimes X_q$ is the left action groupoid.

## Proof Strategy

First compute every fixed-point and fixed-orbit sequence directly on a
regular finite group.  Divisor inversion gives both 2015 zetas without a
topological approximation.  Next compute all $g$-twisted fixed-point sets;
these identify the stronger 2013 $(\mathbb Z\times G_q)$-set.  Then apply the
two scalar maps and the fixed-sector definition of the enhanced orbifold
zeta.  Finally identify the action groupoid with a point and use elementary
orbit intersection formulas to recover shortening and gluing.

## Dependency Map

1. The general orbit-type hierarchy depends on the unique decomposition of a
   finite abelian $C$-set into $C/K$ and on orbit--stabilizer.
2. Uniform source period depends only on regularity and the order of $a_q$.
3. The two Burnside zetas depend on the two distinct Lefschetz sequences and
   divisor inversion.
4. The four scalar formulas depend on
   $\kappa_q(\mathbf u_q)=n_q$ and
   $\Phi_q(\mathbf u_q)=1$.
5. The $G$-permutation triple depends on the full family
   $L^{G_q}(g\phi_q^m)$ and the stabilizer of the base point.
6. The enhanced class depends on the classification of irreducible enhanced
   $G$-sets; its orbifold image depends on freeness.
7. The stack conclusion depends on free transitivity and centrality of
   $a_q$ in the abelian group $G_q$.
8. Shortening/gluing depends on the intersection of the $\phi_q$-orbit with
   the unique $G_q$-orbit.
9. The Route-A decision depends on the exact reductions, varying coefficient
   categories, period collisions, and composite controls.

## Proof

### Step 0. General finite abelian $C$-set hierarchy

Let $C$ be finite abelian, let $a\in C$, put $H=\langle a\rangle$, and
write

$$
X\simeq\coprod_{K\le C}n_K(C/K).
$$

Fix one copy of $C/K$.  Translation by $a^j$ fixes a coset $cK$ if and only
if

$$
a^jcK=cK,
$$

which, because $C$ is abelian, is equivalent to $a^j\in K$.  The least
positive such $j$ is the order of $a$ in $H/(H\cap K)$, namely

$$
d_K=[H:H\cap K].
$$

All points in $C/K$ have this period.  The number of translation cycles in
one copy is

$$
\frac{[C:K]}{d_K}
=\frac{|C|\,|H\cap K|}{|K|\,|H|}
=\frac{|C|}{|HK|}
=[C:HK].
$$

Therefore the ordinary source zeta is

$$
\zeta_{X,\phi_a}(t)
=\prod_{K\le C}(1-t^{d_K})^{-n_K[C:HK]}.
$$

Each copy of $C/K$ is one $C$-orbit.  On the quotient $X/C$, translation by
$a\in C$ is identity.  Hence

$$
\zeta_{X/C,\bar\phi_a}(t)
=(1-t)^{-\sum_Kn_K}.
$$

The points of exact period $m$, regarded as a $C$-set, are precisely the
copies whose $d_K$ equals $m$.  Thus the point-order Burnside exact class is

$$
P_m^C=\sum_{d_K=m}n_K[C/K].
$$

Since every $d_K$ depends on $a$ only through $H=\langle a\rangle$, this
entire untwisted sequence cannot distinguish two generators of the same
cyclic subgroup.  The point-order zeta is

$$
\zeta_{\mathrm{pt}}^C(t)
=\prod_{m\ge1}(1-t^m)^{-P_m^C/m}.
$$

By contrast, every $C$-orbit is setwise fixed, so

$$
\widetilde P_1^C=[X]=\sum_Kn_K[C/K],
\qquad
\widetilde P_m^C=0\quad(m>1),
$$

and

$$
\widetilde\zeta_{\mathrm{orbset}}^C(t)=(1-t)^{-[X]}.
$$

For abelian $C$, the additive orbifold homomorphism sends $[C/K]$ to $|K|$.
Only its additivity on exact-period classes is used here.  It follows that

$$
\Phi_{C,*}(\zeta_{\mathrm{pt}}^C)
=\prod_K(1-t^{d_K})^{-n_K|K|/d_K}
$$

and

$$
\Phi_{C,*}(\widetilde\zeta_{\mathrm{orbset}}^C)
=(1-t)^{-\sum_Kn_K|K|}.
$$

Now give $C/K$ the $(\mathbb Z\times C)$-action

$$
(j,c)\cdot xK=ca^jxK.
$$

The stabilizer of the base coset $K$ consists of the pairs with
$ca^j\in K$.  It is exactly

$$
\widehat K_a
=\langle\{0\}\times K,(1,a^{-1})\rangle.
$$

Thus the $C$-permutation invariant records $a^{-1}K$ on that orbit.  Across
all orbit types with $n_K>0$, two elements give the same recorded cosets
exactly modulo

$$
N=\bigcap_{n_K>0}K,
$$

which is the kernel of the $C$-action on $X$.  Hence the labelled invariant
recovers $a$ exactly when the action is effective, $N=1$.

Finally,

$$
[C/K\,/C]\simeq BK.
$$

The action endomorphism induced by $a$ is $2$-isomorphic to identity.  Since
$K$ is abelian, the inertia of $BK$ is indexed by its $|K|$ elements, but
each sector has identity dynamics.  Therefore

$$
[X/C]\simeq\coprod_Kn_KBK
$$

retains isotropy-sector multiplicity without retaining a nontrivial quotient
period.

For the frozen structural counterexample, take $C=C_6$, let $a$ generate
$C$, and let $X=C/C_2\sqcup C/C_3$.  The action kernel is
$C_2\cap C_3=1$, so it is effective and the pair of recorded twist cosets
recovers $a$.  Nevertheless

$$
d_{C_2}=[C_6:C_2]=3,
\qquad
d_{C_3}=[C_6:C_3]=2,
$$

and $[C:C_2H]=[C:C_3H]=1$.  Consequently

$$
\zeta_{X,\phi_a}(t)=(1-t^3)^{-1}(1-t^2)^{-1},
$$

with no period-$6$ factor, whereas

$$
\zeta_{X/C,\bar\phi_a}(t)=(1-t)^{-2}.
$$

The orbifold reductions are

$$
(1-t^3)^{-2/3}(1-t^2)^{-3/2}
$$

and $(1-t)^{-5}$, and the quotient stack is
$BC_2\sqcup BC_3$ with $2+3=5$ static inertia sectors.  This completes the
general hierarchy and the counterexample.

### Step 1. Source-cycle structure

Fix $q\ge2$ and abbreviate $G=G_q$, $X=X_q$, $a=a_q$, $r=r_q$,
$n=n_q$, and $m=m_q$.

Under the torsor identification, $X=G$ and

$$
\phi^k(x)=a^kx.
$$

If $\phi^k(x)=x$ for one $x\in G$, cancellation gives $a^k=e$.  Conversely,
$a^k=e$ makes $\phi^k$ identity on all of $X$.  Therefore every point has
exact period $r$, and $X$ is the disjoint union of

$$
m=\frac nr
$$

cycles of length $r$.  This proves that the ordinary source zeta is

$$
\zeta_{\phi}(t)=(1-t^r)^{-m}.
$$

### Step 2. Point-order Burnside zeta

The fixed set of $\phi^k$ is either all of the regular $G$-set or empty:

$$
\operatorname{Fix}(\phi^k)
=\begin{cases}
X,&r\mid k,\\
\varnothing,&r\nmid k.
\end{cases}
$$

For a finite discrete $G$-set, the equivariant Lefschetz class is its fixed
set with the induced action.  Hence

$$
L^G(\phi^k)
=\begin{cases}
\mathbf u,&r\mid k,\\
0,&r\nmid k,
\end{cases}
\qquad
\mathbf u=[G/\{e\}].
$$

The exact-period classes are uniquely determined by divisor inversion.  The
choice

$$
s_r^G=\mathbf u,
\qquad
s_d^G=0\quad(d\ne r)
$$

has precisely the displayed divisor sums, so uniqueness proves it is the
entire sequence.  The point-order rational Burnside zeta is therefore

$$
\zeta_{\mathrm{pt}}^G(t)
=\prod_{d\ge1}(1-t^d)^{-s_d^G/d}
=(1-t^r)^{-\mathbf u/r}.
$$

The coefficient $\mathbf u/r$ generally lies only in
$B(G)\otimes\mathbb Q$.  Moreover the formula depends on $a$ only through
$r$.  If $a,b\in G$ have the same order, their untwisted point-order
sequences and zetas coincide.  Thus this invariant does not retain the
distinguished element $a$.

### Step 3. Orbit-order integral Burnside zeta

There is exactly one $G$-orbit in $X$, namely $X$ itself.  Every
$G$-equivariant map sends a $G$-orbit into a $G$-orbit, so this unique orbit
is setwise fixed by every $\phi^k$.  Its orbit type is $G/\{e\}$.  Hence

$$
\widetilde L^G(\phi^k)=\mathbf u
\qquad(k\ge1).
$$

Divisor inversion now gives

$$
\widetilde s_1^G=\mathbf u,
\qquad
\widetilde s_d^G=0\quad(d>1).
$$

Therefore

$$
\widetilde\zeta_{\mathrm{orbset}}^G(t)
=\prod_{d\ge1}(1-t^d)^{-\widetilde s_d^G/d}
=(1-t)^{-\mathbf u}.
$$

This lies over the integral Burnside ring and retains the regular orbit type,
but its sole dynamical support is $d=1$.

### Step 4. Burnside marks and the four scalar reductions

For a subgroup $K\le G$, a point of $G/\{e\}$ is fixed by $K$ exactly when
every element of $K$ is identity.  Thus

$$
\mu_K(\mathbf u)=
\begin{cases}
n,&K=\{e\},\\
0,&K\ne\{e\}.
\end{cases}
$$

In particular $\kappa_G(\mathbf u)=n$.  Because $G$ is abelian, the
additive orbifold homomorphism satisfies
$\Phi_G([G/H])=|H|$, so $\Phi_G(\mathbf u)=1$.

Apply $\kappa_G$ and the additive map $\Phi_G$ to the exact-period classes
before forming
the scalar products.  Equivalently, use the exponent-reduction notation
fixed above.  This gives

$$
\kappa_{G,*}(\zeta_{\mathrm{pt}}^G)
=(1-t^r)^{-n/r}
=(1-t^r)^{-m},
$$

$$
\Phi_{G,*}(\zeta_{\mathrm{pt}}^G)
=(1-t^r)^{-1/r},
$$

$$
\kappa_{G,*}(\widetilde\zeta_{\mathrm{orbset}}^G)
=(1-t)^{-n},
$$

and

$$
\Phi_{G,*}(\widetilde\zeta_{\mathrm{orbset}}^G)
=(1-t)^{-1}.
$$

The first is exactly the ordinary source zeta and has multiplicity $m$.  The
second retains support $r$ but has fractional exponent $1/r$.  The third has
multiplicity $n$ at period one.  The fourth has unit multiplicity but period
one.  None of these four standard outputs has both source support $r$ and
unit exponent.

### Step 5. The stronger 2013 $G$-permutation zeta

For $g\in G$ and $k\ge1$,

$$
(g\phi^k)(x)=ga^kx.
$$

This translation fixes one point if and only if $ga^k=e$, and then it fixes
every point.  Therefore

$$
L^G(g\phi^k)
=\begin{cases}
\mathbf u,&g=a^{-k},\\
0,&g\ne a^{-k}.
\end{cases}
$$

The 2013 invariant is the unique virtual $G$-permutation reproducing all
these twisted Lefschetz classes.  The actual permutation $(X,\phi)$ does so,
so uniqueness identifies it with the invariant.

Equivalently, give $X$ the $(\mathbb Z\times G)$-action

$$
(k,g)\cdot x=ga^kx.
$$

At the base point $e\in G$, the stabilizer condition is
$ga^k=e$, or $g=a^{-k}$.  Hence

$$
\operatorname{Stab}_{\mathbb Z\times G}(e)
=\{(k,a^{-k}):k\in\mathbb Z\}
=\langle(1,a^{-1})\rangle.
$$

In the irreducible classification by $(H,d,\alpha)$, the intersection with
$\{0\}\times G$ is trivial, the least positive $\mathbb Z$-coordinate is
$d=1$, and the twist is $a^{-1}$.  Thus the triple is

$$
(\{e\},1,a^{-1}).
$$

Because the regular $G$-action is faithful, this twist recovers $a$.  For a
non-effective action with kernel $K$, the same reasoning would recover only
$a^{-1}K$; this proof makes no assertion beyond the effective regular case.

### Step 6. The enhanced Burnside class

An irreducible enhanced $G$-set is classified by
$(H,k,\bar h,\bar\alpha)$, where $H$ is the point isotropy, $k$ is the period
of the induced permutation on the orbit set, $\bar h\in N_G(H)/H$ is the
return twist, and $\bar\alpha$ is an isotropy character.

For the regular torsor, $H=\{e\}$.  There is one $G$-orbit, so $k=1$.
The return map on that orbit is translation by $a$, and the trivial group has
only the trivial character.  Therefore

$$
[X,\phi,1]=\widehat X_{\{e\},1,a,1}.
$$

Since $G$ is abelian, conjugation does not identify different twists.  The
enhanced class therefore retains the exact labelled $a$.

For its enhanced orbifold zeta, consider the fixed sector $X^g$ for each
$g\in G$.  Freeness gives

$$
X^g=\varnothing\quad(g\ne e),
\qquad
X^e=X.
$$

The only isotropy character value is $1$.  The centralizer of $e$ is $G$,
and $X/G$ is one point.  The induced map on that point is identity.  Hence
all nonidentity factors are $1$ and the identity-sector factor is

$$
\zeta^{\mathrm{enh,orb}}(t)=(1-t)^{-1}.
$$

Thus the enhanced carrier retains $a$, but this particular orbifold image
does not.

### Step 7. Action groupoid and quotient stack

The action groupoid $\mathcal G=G\ltimes X$ has objects $x\in X$ and a
morphism labelled $g\in G$ from $x$ to $gx$.  Because the action is
transitive, any two objects are isomorphic.  Because it is free, every object
has trivial automorphism group.  Choosing one object therefore gives a fully
faithful and essentially surjective functor from the terminal groupoid to
$\mathcal G$.  Hence

$$
\mathcal G\simeq *.
$$

The inertia objects are pairs $(x,g)$ with $gx=x$.  Freeness forces $g=e$,
so there are no nonidentity twisted sectors.

The $G$-equivariant map $\phi(x)=ax$ induces an endofunctor $F_a$ of
$\mathcal G$.  Define a component

$$
\eta_x:x\longrightarrow ax
$$

to be the groupoid arrow labelled $a$.  For an arrow labelled $g$ from $x$
to $gx$, naturality requires

$$
g\circ a=a\circ g.
$$

This holds because $G$ is abelian.  Therefore

$$
\eta:\operatorname{Id}_{\mathcal G}\Longrightarrow F_a
$$

is a natural isomorphism.  It follows formally that a quotient-stack
invariant respecting Morita equivalence and $2$-isomorphism of endomorphisms
must equal its value on identity acting on one point.  Presentation-sensitive
Burnside or $G$-permutation data are not covered by this statement.

### Step 8. Shortening and gluing

For any $x\in X$,

$$
\mathcal O_G(x)=X,
\qquad
|\mathcal O_G(x)|=n,
$$

whereas

$$
|\mathcal O_\phi(x)|=r.
$$

Since the latter orbit is contained in $X$,

$$
|\mathcal O_\phi(x)\cap\mathcal O_G(x)|=r.
$$

Zegowitz's finite-group quotient formulas therefore say that the source
orbit shortens by $1/r$ and that

$$
\frac{|\mathcal O_G(x)|}
{|\mathcal O_\phi(x)\cap\mathcal O_G(x)|}
=\frac nr=m
$$

source cycles glue to one quotient orbit.  This quotient orbit has length
$r/r=1$.

### Step 9. No intrinsic modulus or prime clock in the audited outputs

The only nontrivial dynamical support retained by the point-order series is
$r_q$.  It is not the modulus: the frozen exact values contain

$$
r_2=r_4=3,
\qquad
r_6=r_9=12.
$$

The 2013 and enhanced carriers retain $a_q$, but only as elements of the
separately labelled, varying groups $G_q$ and the separately varying rings
$K_0(\mathrm{f.}\,G_q\text{-perm})$ and $\widehat B(G_q)$.  The construction
provides no canonical comparison that converts these labels into one common
return-time observable.

The orbit-order/orbifold/stack outputs with unit multiplicity have period
$1$.  Replacing their formal variable by $q^{-s}$ supplies $q$ from outside.
For the source-period output, producing a unit factor at $q^{-s}$ would
require both a $q$-dependent variable substitution and a $q$-dependent
normalization of the exponent.  Neither is generated by an iterate or fixed
sector.

Finally, every step above used only that $X_q$ is a regular $G_q$-torsor and
$a_q\in G_q$.  Paper 10 proved this for every $q\ge2$, not just primes.
Therefore composites satisfy the same formulas.  No prime selector is
present.  This proves the scoped A0 conclusion.

## Corrections or Missing Assumptions

- The phrase “equivariant zeta retains the clock” is too ambiguous.  It is
  corrected to three separate statements: the point-order series retains
  $r_q$; the orbit-order series retains orbit type but only period one; the
  $G$-permutation/enhanced carriers retain the twist $a_q$ in a fixed
  effective labelled group.
- The statement “stacky refinements retain stabilizers” is not useful on the
  cyclic torsor without qualification: all point stabilizers are trivial.
  Presentation-sensitive Burnside data retain the free orbit type, whereas
  the Morita quotient stack is a point.
- No statement about all stacky zetas is justified.  The proved statement is
  conditional on Morita and $2$-isomorphism invariance.

## Open Risks

- Power-structure notation in a later manuscript must distinguish the
  rational point-order factor from the integral orbit-order factor.
- The inverse in the 2013 stabilizer triple is convention-sensitive.  With
  the frozen left action $(k,g)x=ga^kx$, the twist is $a^{-1}$; the enhanced
  return map itself is $a$.
- The four scalar reductions must not be described as exhaustive among all
  homomorphisms or all representation-valued refinements.
- Walton and Miles remain scope boundaries only; no theorem from either is
  used to extend the finite-set construction.
