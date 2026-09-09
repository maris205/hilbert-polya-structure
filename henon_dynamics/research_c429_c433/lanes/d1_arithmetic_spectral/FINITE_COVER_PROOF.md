# D1-FC proof supplement: finite algebraic holonomy rigidity and sharpness

2026-09-09 UTC. Author proof; no paper admission. The coordinator-assigned
independent checker examined §§3–7 and closed its one mathematical
correction after readback: the residue-field/Frobenius hypothesis in §7.
Its final review file is being prepared; no broader review is claimed.
The frozen original question is in [REPORT.md](REPORT.md).

## 1. Claim, assumptions, notation, and status

**Status: PROVABLE AS STATED** for the finite-cover classification below.
The proposed positive finite-cover label mechanism is therefore refuted.
The elementary consequences and sharpness examples are not separate papers.

Let $K$ be a number field, $X=\mathbb A_K^2$, and $H$ a polynomial
conjugate over $K$ of a nonempty composition of maps

$$
h_i(x,y)=(y,P_i(y)-a_i x),\qquad a_i\in K^*,\quad \deg P_i\ge2.
$$

Fix this entire $H$ as one native tick. Let $m\ge1$. A finite normal
cover means a finite morphism $\pi:Y\to X$ from a normal scheme of finite
type, with finitely many nonempty components, all dominating $X$. Let
$G\in\operatorname{Aut}_K(Y)$ satisfy $\pi G=H^m\pi$. For $m=1$,
$G$ is a one-tick lift; for general $m$ it represents $m$ original ticks.

**Theorem FC.** There is a nonzero finite étale $K$-algebra $A$ and a
$K$-automorphism $\tau$ of $T=\operatorname{Spec}A$ such that, over $X$,

$$
(Y,G)\simeq(X\times_K T,\ H^m\times\tau).                 \tag{FC}
$$

Conversely every such pair gives a cover with the stated properties.
Morphisms of covers commuting with the dynamics correspond exactly to
morphisms of finite étale $K$-schemes commuting with $\tau$. In particular
a geometrically connected cover has degree one.

If $L/K(x,y)$ is any finite field extension and a $K$-automorphism $\sigma$
of $L$ extends $(H^m)^*$, then $L=K'(x,y)$ for a finite extension $K'/K$;
$K'$ is the relative algebraic closure of $K$ in $L$. Thus permitting a
field lift or a birational lift on a finite normal model adds no covers.

For a compatible tower in which every finite level is equivariant under
the specified lift (or an iterate), every level and transition is constant.
This assertion does **not** include an infinite extension with no cofinal
system of finite dynamically invariant subextensions; Section 7 constructs
exactly that escape.

## 2. Strategy and dependency map

1. The classical no-periodic-affine-curve property of Hénon maps excludes
   invariant divisorial branch support. Section 3 gives a direct pole-order
   reconstruction, credited to the existing theorem rather than claimed new.
2. Purity of branch applies to a finite generically separable morphism from
   a normal surface to the regular plane and removes possible residual
   codimension-two branching.
3. Finite étale covers of affine space in characteristic zero are constant.
   Galois descent then classifies the lifts and their morphisms.
4. The product action gives exact holonomy and primitive/repetition formulas.
5. Artin–Schreier and infinite Kummer examples delimit the actual scope.

The nontrivial classical inputs are stated with source scopes in Section 8.
No target zeta, trace regularization, infinite determinant, prime owner or
automorphic theorem is used.

## 3. Classical no-periodic-curve input, reconstructed on the native factors

Work first over an algebraically closed field. Suppose a nonempty finite
union $C$ of irreducible affine curves is preserved by $H^m$. Conjugating
transports this assertion, so take $H=h_s\cdots h_1$ in the displayed form.
Use $sm$ phases, repeating the factors, and let $C_j$ be the image of $C$
under the first $j$ factors. Thus $C_{sm}=C_0$. Keep separate copies when
the same curve reappears. Each factor is an isomorphism $C_j\to C_{j+1}$.

Normalize each component of every $C_j$ and complete it to its smooth
projective curve. Each factor extends to an isomorphism of these complete
normalizations: an isomorphism of function fields of nonsingular complete
curves determines an isomorphism. The finite sets of points omitted from
the affine normalizations are carried bijectively to one another. A point
is omitted precisely when at least one coordinate has a pole: otherwise
the finite normalization over the affine curve extends that point into
the affine normalization. Such points exist because a positive-dimensional
affine curve cannot be complete.

Across this finite set of phase-marked boundary points, define the
nonnegative pole orders $u$ and $v$ of $x$ and $y$, respectively. If a
coordinate is identically zero its pole order is defined to be zero.
Since each factor has first coordinate $y$, the multiset of all $x$ pole
orders equals the multiset of all $y$ pole orders, with their phase and
boundary-point multiplicities. Let their common maximum be $M$. We have
$M>0$ because some boundary point has a coordinate pole.

Choose a point with $y$ pole order $M$ and let its next factor have degree
$d\ge2$. The term $P_i(y)$ has pole order $dM$ with nonzero leading
coefficient, while $a_i x$ has pole order at most $M$. These orders differ,
so cancellation of the leading pole is impossible. The next $y$ coordinate
has pole order exactly $dM>M$, contradicting maximality. Therefore $C$
does not exist. In particular no affine curve is periodic under any
positive iterate of $H$.

This is a reconstruction of the source-owned no-curve theorem, not an
independent increment. The argument uses neither a complex absolute value
nor characteristic zero; it also explains why the branch-support step
survives in positive characteristic.

## 4. Proof of Theorem FC

### Step 1. The branch support is invariant

In characteristic zero each component of the finite dominant cover is
generically separable, so the étale locus is dense. The non-étale locus
of $\pi$ is closed in $Y$, and its image $B$ is closed in $X$ because
$\pi$ is finite. The commuting square with the two isomorphisms $G$ and
$H^m$ preserves the property of being étale, hence $H^m(B)=B$.

The union of the one-dimensional components of $B_{\overline K}$ would
be a finite invariant union of affine curves. Section 3 excludes it.
Thus $\pi$ is unramified over every codimension-one point of $X$.
Equivalently, at every codimension-one point of every normal source
component the finite map is unramified; finite dominant maps between these
surfaces preserve codimension at such points.

### Step 2. Purity excludes a hidden finite branch set

Apply purity of branch locus to every source point over a closed point of
$X$. The local rings of $Y$ are normal; those of $X$ are regular; the
map is finite, hence quasi-finite; source and target local dimensions
agree; and every codimension-one specialization is unramified by Step 1.
These are precisely the hypotheses of Stacks Tag 0BMB. The map is étale
at such points. At codimension one it was already étale (an unramified
finite torsion-free algebra over a DVR is flat); at generic points it is
separable and hence étale. Therefore $\pi$ is finite étale everywhere.

Normality and regularity are used here. An isolated branch set is not
discarded merely because it has no curves.

### Step 3. Descent gives constant covers and constant lifts

The classical equivalence between finite étale covers of $\mathbb A_K^2$
and finite étale $K$-schemes gives $Y\simeq X\times T$. One way to see
the geometric assertion in the present number-field case is to embed
$\overline K$ into $\mathbb C$: a finite étale complex cover analytifies
to a finite topological covering of the contractible space $\mathbb C^2$.
Every connected component has degree one; a finite degree-one morphism
to a normal variety is an isomorphism. Descent records the finite Galois
permutation of these components and gives $T$ over $K$.

Over $\overline K$, a lift $G$ above $H^m$ sends each connected sheet
$X_{\overline K}$ to one sheet. Its first coordinate is prescribed by
$\pi G=H^m\pi$, and its sheet permutation is constant on the connected
plane. Being defined over $K$ is exactly the condition that this
permutation commute with the absolute Galois action on the sheet set.
It therefore descends to a unique $\tau\in\operatorname{Aut}_K(T)$.
The same component argument proves the assertion about morphisms and
uniqueness up to isomorphism. Conversely the product construction is
finite étale and normal and satisfies the commuting square. This proves FC.

### Step 4. Field lifts and towers

Let $R=K[x,y]$. The integral closure $B$ of $R$ in $L$ is finite over $R$
because $R$ is an excellent finitely generated algebra over a field.
If $b\in B$ satisfies a monic relation with coefficients in $R$, applying
$\sigma$ gives a monic relation for $\sigma(b)$ with coefficients in
$(H^m)^*R=R$. Hence $\sigma(B)\subset B$; applying $\sigma^{-1}$ proves
equality. The field lift therefore extends to an automorphism of the
normalization, to which FC applies. Connectedness makes $A=K'$ a field.

Every element of $K'(x,y)$ algebraic over $K$ lies in $K'$, because $K'$
is algebraically closed in its purely transcendental extension. This
identifies the constants intrinsically. No Galois assumption on $L/F$
was needed.

For a compatible tower, apply FC level by level; its full-faithfulness
forces all transition maps to come from the constants. Thus an inverse
limit of finite equivariant sheet systems remains independent of the
phase point. If a union of finite invariant fields is used instead,
it is $K_\infty(x,y)$, where $K_\infty$ is their union of constant fields.
There is no assertion about a tower whose finite levels are permuted
out of themselves by every iterate of the lift.

## 5. Exact native holonomy, primitive trajectories, and spectral boundary

Take $m=1$ and let $S=T(\overline K)$, with permutation $\tau$.
For every primitive orbit $c$ of $H$ of length $n$, the return on its
fiber is $\tau^n$. Changing the starting point conjugates the return by
one transport; here the global product trivialization makes the same
permutation visible everywhere. Consequently every conjugacy-class
function of the fiber return is identical for all length-$n$ trajectories.

For a particular $\tau$-cycle of length $r$, the product of this cycle
and $c$ has $nr$ points. A point returns after $q$ ticks precisely when
$n\mid q$ and $r\mid q$. It therefore decomposes into

$$
\gcd(n,r)\text{ primitive lifted cycles, each of length }
\operatorname{lcm}(n,r).                                      \tag{1}
$$

These are ordinary primitive cycles, not scheme lengths or a quotient
by reversal. If $b_r$ is the number of $\tau$-cycles of length $r$,
then $F_n=\#\operatorname{Fix}(H^n)$ and $\widetilde F_n$ satisfy

$$
\widetilde F_n=F_n\sum_{r\mid n}r b_r.                        \tag{2}
$$

The $F_n$ are finite: a positive-dimensional fixed locus of $H^n$ would
contain a prohibited invariant curve, and the whole plane cannot be
fixed because the dynamical degree exceeds one. Counting here is reduced
geometric-point counting. If an ordinary dynamical zeta is desired, the
formal consequence is

$$
\zeta_G(z)=\prod_{r\ge1}\zeta_{H^r}(z^r)^{b_r}.              \tag{3}
$$

Indeed insert (2) into $\log\zeta_G(z)=\sum_n\widetilde F_nz^n/n$
and put $n=rk$. The finite product (3) is a consequence, not the research
mechanism or a new determinant reconstruction. No target Euler factors
are identified by it.

For any $H$-invariant measure for which a Koopman space is defined, the
product cover with uniform sheet measure gives the exact tensor action
$U_G=U_H\otimes U_\tau$ (using pullback Koopman conventions on both
factors). Arithmetic Galois acts only on the finite sheet factor and
commutes with $U_\tau$. Thus this cover cannot create state-dependent
arithmetic holonomy by choosing a different operator completion.
No claim that an arbitrary desired trace exists is made.

For an iterate-only lift and a primitive $H$-orbit of length $n$, the
$H^m$ return has $\gcd(n,m)$ subcycles of length
$n/\gcd(n,m)$ in block ticks. Its holonomy is
$\tau^{n/\gcd(n,m)}$, again length-only. Every block is exactly $m$
original ticks; a one-tick lift is not inferred.

At a finite place where a chosen product model extends étale, arithmetic
Frobenius acts on the constant sheet set by a permutation $\phi_v$ that
commutes with $\tau$. Every mixed sheet trace is
$\operatorname{Tr}(U_\tau^nU_{\phi_v}^r)$, independent of the base point.
For reduced geometric equalizers, whenever the base equalizer is finite,

$$
\#\{G^n(y)=\Phi_v^r(y)\}
=\#\{H^n(x)=\Phi_v^r(x)\}\,
  \#\{s\in S:\tau^n s=\phi_v^r s\}.                         \tag{4}
$$

Equation (4) concerns the reductions of this constant characteristic-zero
cover, not all covers newly available in characteristic $p$. The two
clocks remain separate. Base-point arithmetic and different residue
degrees are not erased; the **additional cover label** is constant.
The sheet equalizer in (4) is the permutation trace of
$U_\tau^nU_{\phi_v}^{-r}$; the sign of the Frobenius exponent is fixed
by the displayed equalizer, not silently changed to a fixed-point count.

## 6. A genuine positive-characteristic boundary

For any prime $p$, over an algebraic closure of $\mathbb F_p$, set

$$
H(u,v)=(v,v^p-u),\qquad
\pi(u,v)=(u^p-u,v^p-v).
$$

The two coordinate Artin–Schreier equations make $\pi$ finite of degree
$p^2$. Its derivative is $-I$, so it is étale. Its source is the connected
normal affine plane, and the degree exceeds one. Direct substitution gives

$$
\pi H(u,v)=(v^p-v,v^{p^2}-v^p-u^p+u)=H\pi(u,v).
$$

Thus the full characteristic-zero conclusion is false in characteristic
$p$, even with smooth source and a one-tick lift. On the geometric deck
group $\mathbb F_p^2$, the lifted $H$ acts by
$\left(\begin{smallmatrix}0&1\\-1&1\end{smallmatrix}\right)$.
This is a classical additive/Artin–Schreier construction, not a claim of
new source ownership. The example isolates the failed step: affine space
is no longer geometrically étale simply connected. No claim about the
quadratic one-variable PC424-L transfer problem follows from it.

## 7. An infinite-ramification sharpness witness with orbit-sensitive arithmetic

This section is an exact boundary example for the tower quantifier, not
an extension of FC to a new analytic operator class.

Fix a coordinate $f=x$, or transport this marked coordinate along a
polynomial conjugacy, and write $f_j=f\circ H^j$ for every $j\in\mathbb Z$.
Each $f_j$ is irreducible in $\overline K[x,y]$: an automorphism sends the
irreducible polynomial $x$ to an irreducible polynomial. Their zero
divisors are pairwise distinct, since equality would make one affine
curve periodic. The choice $(H,f)$ is declared data; no canonical divisor
on an unmarked conjugacy class is asserted.

For any nonempty finite set $J\subset\mathbb Z$, the square class of
$\prod_{j\in J}f_j$ is nontrivial. Its valuation at the prime divisor
$f_k=0$, for $k\in J$, is one. Thus the classes $[f_j]$ are linearly
independent over $\mathbb F_2$ in
$\overline K(x,y)^*/\overline K(x,y)^{*2}$.

Elementary Kummer theory now gives

$$
L_\infty=\overline K(x,y)(\sqrt{f_j}:j\in\mathbb Z),\qquad
\operatorname{Gal}(L_\infty/\overline K(x,y))
\simeq\prod_{j\in\mathbb Z}\mathbb Z/2\mathbb Z.              \tag{5}
$$

For completeness the finite Kummer step follows inductively. In an
extension generated by independent square roots, the sign-change
automorphisms have the products of subsets of the roots as their common
one-dimensional eigenspaces. If an element of the base field becomes a
square, its square root is changed only by signs under this Galois group
and lies in one such eigenspace; its square class was therefore a product
of the previous classes. The new odd valuation rules this out. Every new
root doubles the degree. Passing through finite subsets proves (5).

The assignments $\sigma|_{\overline K(x,y)}=H^*$ and
$\sigma(\sqrt{f_j})=\sqrt{f_{j+1}}$ define an automorphism of
$L_\infty$, with inverse the reverse shift. They respect the defining
quadratic relations and the independent monomial bases. However, no
nontrivial finite intermediate extension is stable under any $\sigma^m$,
$m\ge1$. In the character module
$\bigoplus_{j\in\mathbb Z}\mathbb F_2 e_j$, such an extension would
give a finite-dimensional shift-$m$ invariant subspace. A nonzero
finite-support vector has an extreme support index which translates
without bound under repeated shifts. Its translates cannot belong to a
fixed finite-dimensional subspace, whose elements have support in one
fixed finite union. This proves the claim and also follows from FC.

There is an explicit native-orbit/Frobenius interaction, without clock
identification. Work at a reduction of odd characteristic $p$ for which
$H$ remains of Hénon type, and fix a finite field $\mathbb F_q$ containing
all reduced coefficients of $H$ and $f$, where $q$ is a power of $p$.
Let $P\in\mathbb F_q^2$ have native least period $n$ and assume
$f_j(P)\ne0$ for all $j$. The entire orbit and all its $f_j$ values then
lie in $\mathbb F_q$. On every finite Kummer stage the
geometric fibre at $P$ is étale and consists of independent choices
$t_j^2=f_j(P)$. The inverse-limit fibre consists of all such root sequences;
the lifted $n$-tick return shifts indices by $n$. Its fixed fibre therefore
has exactly $2^n$ points, the $n$-periodic root sequences.

The $q$-power arithmetic Frobenius fixes $P$, commutes with the lifted
native map, and sends each root to

$$
t_j^q=\chi_q(f_j(P))\,t_j,
$$

where $\chi_q$ is the quadratic character of $\mathbb F_q^*$. In the complex permutation
representation on this finite fixed fibre, choose reference roots and
take the product of the $n$ relative signs. The resulting one-dimensional
character line is independent of the reference choice as a line, and
Frobenius acts on it with eigenvalue

$$
\epsilon(c)=\chi_q\!\left(\prod_{j=0}^{n-1}f_j(P)\right).
                                                                    \tag{6}
$$

The product is unchanged by cyclic re-rooting of the primitive trajectory.
It depends on the actual trajectory, not merely its length. As a hand
control, use $H(x,y)=(y,y^2+3-3x)$ at $p=7$. The points $(1,1)$ and
$(3,3)$ are two different native fixed points, both avoiding $f=0$.
Their eigenvalues (6) are $+1$ and $-1$, since the nonzero squares modulo
$7$ are $1,2,4$. No enumeration or mathematical program was used.

This does **not** construct a finite dynamically invariant cover of the
whole plane, and it does not contradict FC. It uses infinitely many
ramification divisors, no nontrivial finite invariant geometric stage,
and periodic-point-dependent fixed fibres. There is no constructed global
trace-class operator or limiting determinant. Formula (6) is the familiar
multiplicative quadratic cocycle for the marked observable $f$; assigning
it target Euler weights or calling it a prime-owner theorem is unjustified.

## 8. Sources, closest ownership, and open risks

1. Bedford–Smillie, *Polynomial diffeomorphisms of $\mathbb C^2$: currents,
   equilibrium measure and hyperbolicity*, Invent. Math. 103 (1991),
   69–99, Proposition 4.2, is the original credited no-invariant-curve
   owner. [Publisher metadata](https://link.springer.com/article/10.1007/BF01239509)
   was accessed; the author-list PDF link failed, so a fresh original-body
   read is not claimed.
2. Dujardin–Favre, *The dynamical Manin–Mumford problem for plane polynomial
   automorphisms*, JEMS 19 (2017), 3421–3465, DOI 10.4171/JEMS/743:
   [publisher PDF](https://ems.press/content/serial-article-files/32251?nt=1).
   Published Proposition 1.9 states the no-curve theorem and credits [1].
   The introduction and targeted proposition text were accessed, not the
   complete 45-page proof corpus; subsequent PDF find/range calls failed.
3. Cantat–Dujardin, *Holomorphically conjugate polynomial automorphisms of
   $\mathbb C^2$ are polynomially conjugate*, first published
   2024-09-26, [DOI 10.1112/blms.13164](https://doi.org/10.1112/blms.13164),
   Section 3(a), Theorem B and its complete displayed proof, were read.
   The proper holomorphic semiconjugacy theorem already uses the same
   invariant-ramification/no-curve mechanism when the source is
   $\mathbb C^2$. Arbitrary normal source surfaces in FC are not literally
   its theorem statement; purity supplies the straightforward extension.
4. [Stacks, Tag 0BMB](https://stacks.math.columbia.edu/tag/0BMB),
   Lemma 58.21.4, purity of branch locus: full statement/hypotheses and
   opening proof read. [Tag 0BTX](https://stacks.math.columbia.edu/tag/0BTX),
   Lemma 58.14.3: arithmetic/geometric fundamental-group exact sequence,
   statement and proof read.
5. Chernousov–Gille–Reichstein, *Reduction of structure for torsors over
   semilocal rings*, [author/institution-hosted text](https://www.math.uni-bielefeld.de/lag/man/274.pdf),
   Section 8, opening paragraphs, explicitly gives the constant finite
   étale-cover assertion for affine space in characteristic zero, with
   its SGA1 attribution. Title/abstract and the complete relevant opening
   body were read. No theorem about general reductive torsors is imported.

**Ownership judgment.** FC is a complete reusable scoped obstruction,
not a tautological missing-target-bridge statement. Nonetheless its main
geometric idea is already present in [3]; the added normal-source, descent,
primitive-count and tower formulations are short consequences of classical
tools. Sections 6–7 are sharpness/control constructions, not evidence of
a new global spectral theorem. A substantial independent-paper increment
has not been established. Search non-hits are not novelty evidence.

**Remaining risks/boundaries.** The independent check's residue-field
correction is closed; its final archived report remains pending.
Characteristic-$p$ classification, nonnormal finite
schemes, covers of parameter or periodic-point loci, nonalgebraic covers
of invariant fractals, general infinite-monodromy sheaves, and infinite
extensions lacking finite invariant stages are not excluded by FC.
The infinite Kummer witness addresses existence and its exact fixed-fibre
character only; its global analytic trace problem remains unformulated.

No changes to old/shared packages, no mathematical execution, and no target
Euler/root-number/automorphy/Hilbert–Pólya claim: `NO_BAD_EULER_OR_ROOT_NUMBER`.
