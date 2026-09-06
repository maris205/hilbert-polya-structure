# Wild rational inverse towers with simple projective monodromy

2026-09-06. Scout proof package, not an admission record or manuscript.
The classical first-level Serre/Abhyankar cover is explicitly deducted
from the proposed increment. No candidate number is assigned here.

## Claim and status

**Status: PROVABLE AS STATED, subject to independent review of this
written proof and the separate source-ownership screen.**

**Selection status: REJECT_SUBSTANCE for a separate batch paper;
retain as a companion mathematical note.** On 2026-09-06, the coordinator
accepted the author and independent source-reviewer's assessment after
independent global and local mathematical review found no gap. Deducting
the classical first cover and general composition machinery leaves a
short map-specific AS stability calculation closely related to the
cubic tower's local method. This selection decision does not retract
the theorem, assert an exact prior owner of every displayed formula,
or authorize a separate paper slot. No candidate number is assigned.

Let $p\geq5$ be a prime, let $k$ be any field of characteristic $p$,
and let $t$ be transcendental over $k$. Put

$$
f(X)=X^p+X^{-1},\qquad d=p+1,\qquad
m=\frac{p-1}{2},\qquad b=m+1=\frac{p+1}{2},
$$

and let $L_n$ be the splitting field over $k(t)$ of the generic
equation $f^{\circ n}(X)=t$. Its inverse-image tree has $d^n$ vertices
at height $n$. Let $G=\operatorname{PSL}_2(\mathbb F_p)$ in its natural
degree-$d$ action, and define the full iterated permutation wreath groups

$$
W_1=G,\qquad W_{n+1}=G^{d^n}\rtimes W_n.
$$

Then, with compatible tree labeling, for every $n\geq1$,

$$
\operatorname{Gal}(L_n/k(t))=W_n,\qquad
|W_n|=\left(\frac{p(p^2-1)}2\right)^{((p+1)^n-1)/p}.
\tag{T1}
$$

The extension is regular over $k$: its arithmetic and geometric
monodromy groups coincide. After extension of constants to an
algebraic closure, the only branch point is $t=\infty$, and its
ramification index and different exponent are

$$
e_n=m p^n,\qquad D_n=p^{n+1}-(m+2).
\tag{T2}
$$

More precisely, geometric inertia has the form

$$
I_n\simeq(\mathbb Z/p\mathbb Z)^n\rtimes C_m,
\tag{T3}
$$

where $C_m$ acts by faithful scalar multiplication through the subgroup
of order $m$ in $\mathbb F_p^*$. Its lower ramification filtration is

$$
(I_n)_0=I_n,\quad (I_n)_1=\cdots=(I_n)_b
  \simeq(\mathbb Z/p\mathbb Z)^n,\quad (I_n)_{b+1}=1.
\tag{T4}
$$

The smooth projective geometric curve with function field $L_n$ has
genus

$$
g_n=1+\frac{|W_n|}{2m}
       \left(1-\frac{m+2}{p^n}\right).
\tag{T5}
$$

In particular $g_1=m^2$. The clock here is generic inverse-image
height, not ordinary forward period or finite-field extension degree.
No Artin--Mazur zeta, target Euler divisor, or Hilbert--Pólya claim is
deduced from this inverse-tower theorem.

## Scope and difference from the characteristic-three cubic

This is a different rational map, all primes $p\geq5$, and a simple
nonabelian first monodromy group. The cubic polynomial's sibling sign
constraints and mixed Kummer/AS global character-rank proof are absent.
This proof uses a leaf stabilizer having no simple-group quotient,
exact ramification-support separation, and Goursat independence of the
simple factors. Those abstract independence mechanisms are classical
machinery, not a new general composition theorem. The local compositum
has degree only $p$, established here through the explicit local model.

The first-level group, projective action and explicit Serre-type
Artin--Schreier curve are classical input reconstructed below for an
auditable normalization; none is counted as a newly discovered object.

A further ownership deduction is required. König--Neftin--Rosenberg,
*Polynomial compositions with large monodromy groups and applications
to arithmetic dynamics* ([arXiv:2401.17872v2](https://arxiv.org/abs/2401.17872v2)),
Corollary 4.6 and its field formulation 4.6.B, supply a general
composition-factor upgrade from minimal steps, nondiagonal adjacent
kernels, and distinct prefix Galois closures. Their paper has a standing
characteristic-zero convention. Its finite-group/Galois argument adapts
directly to this separable tower; it is not quoted here as a literally
characteristic-free published statement. Once the local degrees below
and the height-two kernel are known, this classical upgrade also yields
the full groups within the stated wreath upper bound.

Accordingly, Sections 2 and 4 retain a self-contained special-case proof
but are not claimed as new generic Goursat theory. The possible residual
contribution is the map-specific all-height wild local calculation and
its complete consequences. Whether that residual is substantial enough
for a paper is an independent selection judgment, not implied by the
correctness of the theorem. The separate source audit records that gate.

## Dependency map

1. Section 1 reconstructs the classical first cover and its local
   normalization. It also gives the full-wreath upper bound.
2. Section 2 proves two elementary finite-group/field lemmas without
   assuming anything about a later dynamical level.
3. Section 3 proves a complete local splitting and stability lemma.
4. Section 4 simultaneously inducts the actual monodromy, ramification
   index, and closeness of the pole roots. Global independence uses
   only the preceding level's already-proved group.
5. Sections 5--6 descend arithmetic equality and compute the different,
   filtration and genus from the established local index.

## 1. The classical first-level model

Over $k(v)$ let $w$ satisfy

$$w^p-w=v^{-b},\qquad t=v^{mp}+v^{-m}=f(v^m).\tag{1.1}$$

The AS equation is irreducible: its right side has a pole of order
$b$, with $p\nmid b$, whereas a nonintegral expression $h^p-h$ has
pole order divisible by $p$. This argument works after any constant
extension. Thus the degree of $M=k(v,w)$ over $k(t)$ is

$$p\,m(p+1)=|G|.\tag{1.2}$$

The rational map in $v$ in (1.1) is separable, as its derivative is
$-m v^{-m-1}\ne0$; its degree is $m(p+1)$.

Write $r=v^m$. The $p+1$ roots of $X^{p+1}-tX+1$ in $M$ are

$$
r,\qquad x_i=r(w+i)^{p-1}
             =r+\frac{v^{-1}}{w+i}\quad(i\in\mathbb F_p).
\tag{1.3}
$$

For verification, one can adjoin $u$ with $u^2=v$. Then
$r=u^{p-1}$ and $w^p-w=u^{-(p+1)}$. Both $u$ and $uw$ solve

$$Z^{p^2}-tZ^p+Z=0.$$

Their $\mathbb F_p$-linear combinations give (1.3) after taking
$(p-1)$st powers. They are linearly independent because $w$ is not
constant. The second equality in (1.3) also follows immediately from
$w^p=w+v^{-b}$ and $b=m+1$. The roots are distinct.

Conversely, the roots in (1.3) recover both generators:

$$
v=\frac1{x_1-r}-\frac1{x_0-r},\qquad
w=\frac1{v(x_0-r)}.
\tag{1.4}
$$

Hence $M$ is exactly the splitting field, not an auxiliary larger
field. For a matrix
$\begin{pmatrix}a&c\\e&h\end{pmatrix}\in\operatorname{SL}_2(\mathbb F_p)$,
the transformations

$$
v\longmapsto v(a+cw)^2,\qquad
w\longmapsto\frac{e+hw}{a+cw}
\tag{1.5}
$$

preserve the AS equation. They preserve $t$, because the new value of
$v^m$ is one of the roots in (1.3). Their kernel is precisely
$\{\pm I\}$, as can be seen first from the fractional linear action on
the transcendental element $w$. The resulting $|G|$ automorphisms,
together with (1.2), identify the first group with $G$ in its natural
projective action. These automorphisms are defined over $\mathbb F_p$,
so the first result is arithmetic as well as geometric over every $k$.

At a place above $v=0$ over algebraically closed constants, (1.1) gives

$$
v_{L_1}(v)=p,\quad v_{L_1}(w)=-b,\quad
v_{L_1}(t)=-mp.
$$

The root $r$ has positive valuation $mp$. The other $p$ roots have
valuation $-m$, and, for $i\ne j$,

$$
x_i-x_j=\frac{v^{-1}(j-i)}{(w+i)(w+j)},\qquad
v_{L_1}(x_i-x_j)=-p+2b=1.
\tag{1.6}
$$

This initializes the local induction below. At a finite target value,
the polynomial $X^{p+1}-tX+1$ and its derivative $X^p-t$ have no common
root: simultaneous vanishing would give $1=0$. The cover is therefore
unramified over every finite target. Since $f(\infty)=\infty$, every
iterate and its Galois closure are unramified away from $\infty$.

At all heights there is a compatible embedding of the actual Galois
tree group into $W_n$. To make this bound explicit, for each vertex
$\alpha$ choose a copy of the first splitting field by the parameter
embedding $t\mapsto\alpha$. A Galois automorphism carrying $\alpha$ to
$\beta$ compares this copy with the chosen copy over $\beta$ by an
element of the first group $G$. Thus every local transition lies in
$G$, not merely in $\operatorname{Sym}_{p+1}$ or $\operatorname{PGL}_2$.
These choices give the full-wreath upper bound over both $k$ and
$\overline k$.

## 2. Two elementary global-independence lemmas

### Lemma 2.1. No simple quotient of a leaf stabilizer

Let $H_n$ be a leaf stabilizer in $W_n$. There is no surjective
homomorphism $H_n\to G$.

**Proof.** The point stabilizer $B$ in the natural action of $G$ is a
Borel group of order $pm$. It is solvable, so the assertion holds for
$H_1=B$, since $G$ is nonabelian simple for $p\geq5$.

For a leaf at height $n+1$ with parent $\alpha$, the standard wreath
coordinates give

$$
H_{n+1}=\left(B\times\prod_{\beta\ne\alpha}G_\beta\right)
                    \rtimes H_n.
\tag{2.1}
$$

The group $H_n$ fixes $\alpha$ and permutes the other height-$n$
vertices without singleton orbits. Indeed, for any other vertex take
its first divergence from $\alpha$; the point stabilizer in the local
copy of $G$ is transitive on the other $p$ children, and moves the
divergent vertex while fixing $\alpha$.

Suppose $\phi:H_{n+1}\to G$ were onto. The selected factor $B$ is
normal and solvable in $H_{n+1}$, so its image is a solvable normal
subgroup of the nonabelian simple group $G$, hence trivial. On each
$G_\beta$, the restriction is either trivial or an isomorphism onto
$G$. If it were nontrivial for one factor, it would be nontrivial for
every conjugate factor in its $H_n$-orbit. That orbit has at least two
members, but their images commute, since the corresponding direct
factors commute. Two copies of the whole nonabelian group $G$ cannot
commute elementwise inside $G$. Thus every $G_\beta$ is killed.

The surjection would factor through $H_n$, contradicting induction.
This proves the lemma. $\square$

### Lemma 2.2. Distinct simple Galois fields are jointly independent

Let $E_1,\ldots,E_s$ be pairwise distinct Galois extensions of a field
$K$, in one algebraic closure, all with group the same finite
nonabelian simple group $G$. Their compositum has group $G^s$ over $K$.

**Proof.** Induct on $s$. If $E_s$ met the previous compositum
nontrivially, simplicity would force $E_s$ to be contained in it.
By induction its Galois group is $G^{s-1}$, so restriction would give
a surjection $G^{s-1}\to G$. Every factor has trivial or full image,
and two full images would commute, which is impossible. Exactly one
factor survives. The field of its kernel is the corresponding $E_i$,
forcing $E_s=E_i$, contrary to the hypothesis. Thus the intersection
is trivial and the full direct product follows. $\square$

This is the elementary Goursat/simple-factor mechanism, not a claim
that pairwise disjointness suffices for arbitrary abelian extensions.

## 3. A complete local splitting and stability lemma

For this section let $k$ be algebraically closed, and let $K=k((\pi))$
have its normalized valuation $v_K$.

### Lemma 3.1. Finite parameters split; tight pole parameters share one AS field

For $A\in K$:

1. If $v_K(A)\geq0$, the equation $f(X)=A$ splits completely in $K$.
2. If $v_K(A)=-m$, its splitting field over $K$ is cyclic of degree
   $p$. It is given by an AS equation with pole order $b$.
3. If $v_K(A)=v_K(B)=-m$ and $v_K(A-B)\geq1$, the two splitting
   fields in part 2 are the same inside an algebraic closure of $K$.

**Proof.** For part 1, reduce $X^{p+1}-AX+1$ modulo $\pi$.
The reduction is separable for the same derivative calculation as in
Section 1. It has all $p+1$ roots over the algebraically closed residue
field, and Hensel's lemma lifts every root to $K$.

For part 2, there is a unique small root $s_A\in\pi k[[\pi]]$ of
$f(s_A)=A$. Apply Hensel's lemma to

$$s-A^{-1}(1+s^{p+1})=0$$

at zero. The equation gives $v_K(s_A)=m$. As $p\nmid m$ and the
residue field is algebraically closed, $s_A$ has an $m$th root
$v_A\in K$ with $v_K(v_A)=1$. The model (1.3) shows that the full
splitting field is

$$K(w_A),\qquad w_A^p-w_A=v_A^{-b}.\tag{3.1}$$

This equation is irreducible since $b<p$ and $p\nmid b$; its right
side has pole order $b$. Formula (1.4) shows again that it is exactly
the splitting field. Replacing $v_A$ by another $m$th root scales the
AS right side by an element of $\mathbb F_p^*$, which leaves that
cyclic extension unchanged.

For part 3, the identity

$$f(s_A)-f(s_B)=(s_A-s_B)^p-\frac{s_A-s_B}{s_As_B}\tag{3.2}$$

shows

$$v_K(s_A-s_B)=v_K(A-B)+2m\geq2m+1.$$

Indeed $v_K(s_A-s_B)\geq m>0$, so in (3.2) the second term has
strictly smaller valuation than the first. Choose the $m$th roots
so that $v_B/v_A$ has residue one. Hensel's lemma for an $m$th power
then gives

$$v_K(v_B/v_A-1)\geq m+1=b.$$

Consequently

$$v_K(v_B^{-b}-v_A^{-b})\geq0.\tag{3.3}$$

Every integral element of $K$ is an AS coboundary: solve its residue
equation in $k$ and apply Hensel's lemma, whose derivative is $-1$.
Thus (3.3) makes the two AS classes equal, and their splitting fields
coincide. $\square$

The equality is local, not global. Globally the corresponding simple
extensions will be independent, as proved next.

## 4. Simultaneous all-height induction over algebraically closed constants

Work over algebraically closed $k$. In addition to $G_n=W_n$, maintain
the following two assertions at every place above $t=\infty$:

$$
e_n=mp^n;\qquad
v_{L_n}(\alpha)=-m\ \text{for each pole root }\alpha,
\tag{4.1}
$$

and

$$
v_{L_n}(\alpha-\beta)\geq1
\quad\text{for all distinct pole roots at height }n.
\tag{4.2}
$$

The base case is Section 1. Because the extension is Galois, the
calculation at its displayed place propagates to all conjugate places.

### Step 4A. Every individual factor stays full after base change

Assume the assertions through height $n$. For a height-$n$ root
$\alpha$, let $E_\alpha/k(\alpha)$ be the splitting field of
$f(X)-\alpha$. It has group $G$, by the first-level theorem.

The extension $L_n/k(\alpha)$ is Galois and its group is the leaf
stabilizer $H_n$. The intersection $E_\alpha\cap L_n$ is Galois over
$k(\alpha)$. By simplicity of $G$, it is either $k(\alpha)$ or all
of $E_\alpha$. The second possibility would make $G$ a quotient of
$H_n$, contradicting Lemma 2.1. Therefore

$$
E_\alpha\cap L_n=k(\alpha),\qquad
\operatorname{Gal}(L_nE_\alpha/L_n)=G.
\tag{4.3}
$$

This proves the base-change assertion before invoking any new global
kernel or any next-level group.

### Step 4B. Exact ramification supports distinguish the factors

At a place $Q$ of $L_n$ above $\infty$, Lemma 3.1 and (4.1) imply
that $L_nE_\alpha/L_n$ ramifies at $Q$ if and only if $\alpha$ has
a pole there. At a nonpole it splits completely locally; at a pole
its local degree is exactly $p$.

The set $S_Q$ of pole roots is an embedded full $p$-ary subtree at
height $n$ inside the $d$-ary inverse tree. At every pole parent,
precisely $p$ children are poles and one is a small zero; no child of
a finite parent is a pole. It follows that $|S_Q|=p^n$.

The orbit of $S_Q$ under the already-proved $W_n$ consists of all
embedded full $p$-ary subtrees of height $n$. This follows inductively
because $G$ is transitive on the one omitted child and the lower
wreath coordinates act independently on the retained subtrees.

For any distinct leaves $\alpha,\beta$, one such subtree contains
$\alpha$ but not $\beta$: retain their common path, and at the first
divergence omit the child leading to $\beta$. Extend all retained
vertices by any choices of $p$ children. Thus some conjugate place
$Q'$ has $\alpha\in S_{Q'}$ and $\beta\notin S_{Q'}$.

At $Q'$ the first factor is ramified and the second is split, so
$L_nE_\alpha\ne L_nE_\beta$. Lemma 2.2 now proves their simultaneous
linear disjointness. Therefore the new kernel is the entire
$G^{d^n}$. Together with the wreath upper bound, this gives

$$\operatorname{Gal}(L_{n+1}/k(t))=W_{n+1}.\tag{4.4}$$

### Step 4C. The local compositum has degree only one copy of $p$

Fix a place $Q$ above $\infty$. By (4.2) all its pole parameters
meet Lemma 3.1(3). Their child splitting fields in the completion are
the same cyclic degree-$p$ extension. All nonpole parameters split
there. Hence the whole local compositum has degree exactly $p$,
not $p^{d^n}$, and

$$e_{n+1}=p e_n=mp^{n+1}.\tag{4.5}$$

Let $u$ be any pole root at height $n+1$ with pole parent $A$.
The valuation on $L_n$ is multiplied by $p$ in this completion, so
$v(A)=-pm$. In $f(u)=u^p+u^{-1}$ the first term dominates for a
pole $u$, giving $v(u)=-m$.

For two pole children $u,v$, their parents $A,B$ are poles, and
$v(A-B)\geq p$ if $A\ne B$ by the previous-level closeness. If they
coincide, treat the right side as zero. With $h=u-v$,

$$A-B=h^p-\frac{h}{uv},\qquad v(uv)=-2m=-(p-1).\tag{4.6}$$

If $v(h)<1$, the first term in (4.6) has strictly smaller valuation
than the second, and their sum has valuation $p\,v(h)<p$. This
contradicts the parent bound, or contradicts a zero right side.
Thus $v(u-v)\geq1$. Equations (4.1)--(4.2) close at height $n+1$.
The simultaneous induction proves the geometric part of (T1)--(T2).

## 5. Arithmetic equality and absence of new constants

For an arbitrary field $k$ of characteristic $p$, Section 1 gives an
arithmetic full-wreath upper bound $G_n^{\mathrm{arith}}\subseteq W_n$.
Extension of constants to an algebraic closure gives the geometric
subgroup, already proved to be all of $W_n$. Thus

$$W_n=G_n^{\mathrm{geom}}\subseteq G_n^{\mathrm{arith}}\subseteq W_n.$$

The two groups are equal. Equivalently, the degree does not drop after
any algebraic constant extension. Since the original splitting field
is separable over $k(t)$, this also gives regularity over $k$; in
particular there is no hidden arithmetic constant-field extension.

## 6. Different exponent, full inertia filtration and genus

Work again over algebraically closed constants. In the root field at
the pole path, put $u=1/X$. The local map at infinity is

$$h(u)=\frac{u^p}{1+u^{p+1}},\qquad
h'(u)=-\frac{u^{2p}}{(1+u^{p+1})^2}.\tag{6.1}$$

The local degree of $h^{\circ n}$ is $p^n$. The derivative criterion
for the different in a separable extension of Laurent-series fields,
or the transitivity formula applied to the root tower, gives its
different exponent

$$d_n^{\mathrm{root}}=2p(1+p+\cdots+p^{n-1})
                  =\frac{2p(p^n-1)}{p-1}.\tag{6.2}$$

The Galois completion has degree $mp^n$ over the base and contains
that root completion of degree $p^n$. Its relative degree over the
root completion is $m$, so this relative extension is tame and has
different exponent $m-1$. The transitivity formula yields

$$
D_n=(m-1)+m d_n^{\mathrm{root}}
    =p^{n+1}-(m+2).
\tag{6.3}
$$

For completeness, this also determines the entire lower filtration.
Let $P_n$ be wild inertia; it has order $p^n$, and the tame quotient
has order $m$. The local root degree $p^n$ established immediately above
means that a pole root has an inertia orbit of size $p^n$. There are
exactly $p^n$ pole roots in total, so this is one orbit containing all
of them, with stabilizer of order $m$. Thus $P_n$ acts freely and
transitively on these roots.

Choose a pole root $\alpha$ and choose an $m$th root $\rho$ of
$1/\alpha$ in the completion. It exists by Hensel's lemma and has
valuation one. For $1\ne\sigma\in P_n$, the distinct pole roots
$\sigma\alpha$ and $\alpha$ satisfy (4.2), while
$\sigma\rho/\rho$ has residue one. As $p\nmid m$,

$$
v(\sigma\rho-\rho)
 =m+1+v(\sigma\alpha-\alpha)\geq m+2=b+1.
\tag{6.4}
$$

Every element outside $P_n$ has ramification number one. Hilbert's
different formula and (6.4) therefore give the lower bound

$$
\sum_{1\ne\sigma\in I_n}v(\sigma\rho-\rho)
\geq (m-1)p^n+(p^n-1)(b+1)
=p^{n+1}-(m+2).
$$

The bound equals the exact different (6.3), so equality holds for
every nontrivial wild element in (6.4). This proves (T4). The standard
embedding of a positive lower ramification graded quotient into the
additive residue field shows that $P_n=(I_n)_b/(I_n)_{b+1}$ is
elementary abelian, of rank $n$. The tame quotient is cyclic of order
$m$, and Schur--Zassenhaus splits the inertia extension because
$\gcd(m,p)=1$. Its action on that graded quotient is
the $b$th power of the tame character (up to reversing the chosen
generator). Since $\gcd(b,m)=1$ and the $m$th roots of unity lie in
$\mathbb F_p$, this is faithful scalar multiplication. Thus (T3)
follows with its stated action. The jump $b$ in (T4) is in lower
numbering; the corresponding positive upper jump is $b/m$.

Finally the only branch point is infinity. Riemann--Hurwitz for the
Galois cover gives

$$
2g_n-2=|W_n|\left(-2+\frac{D_n}{e_n}\right)
       =\frac{|W_n|}{m}\left(1-\frac{m+2}{p^n}\right),
$$

which is (T5). $\square$

## Induction-dependency and non-overclaim audit

- The initial simple group is classical and proved here only to fix
  normalization and the exact local model.
- Lemma 2.1 uses only an abstract full wreath group already established
  at height $n$; it does not assume a new kernel at height $n+1$.
- Fullness of each base-changed factor is proved before any use of
  its distinct ramification support.
- Ramification at a pole is not guessed from the pole divisor: it is
  established by the nonzero AS class in Lemma 3.1.
- Distinguishing places uses only the previous $W_n$ action.
- Pairwise field distinction implies joint independence here because
  the factor group is nonabelian simple, not for arbitrary groups.
- Local equality of AS fields is consistent with global independence;
  the normalization in (4.5) is multiplied by exactly $p$ before
  proving the next closeness statement.
- The genus calculation uses the proved index, not a guessed inertia
  order, and the elementary-abelian inertia assertion is deduced only
  after the exact different is known.
- No assertion for $p=3$ or $p=2$ follows from the simple-group lemma.
  No such parameter is included in the theorem.
- No claim of literature priority, formal batch admission, finite-target
  specialization surjectivity, or full ordinary periodic counts is made.

## Remaining review tasks

The proof is complete as written, but non-author review should focus
on Lemma 2.1, the exact local splitting-field equality in Lemma 3.1,
the pole-support orbit argument, and the all-field wreath upper bound.
The separate bounded source screen must examine whether this precise
wild rational all-height realization already appears in the
Serre/Abhyankar or later iterated-monodromy literature. Small exact
checks will be supporting diagnostics, not a substitute for these
arguments or that source distinction.
