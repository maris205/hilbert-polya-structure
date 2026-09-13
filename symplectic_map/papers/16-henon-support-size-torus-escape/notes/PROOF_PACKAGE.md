# Proof Package

## Status and scope

This is the complete source-stage proof package for **Support Size and
Finite-Rank Torus Escape for Generalized Hénon Maps**.  It fixes every
mathematical convention needed for independent checking.  It is not a
manuscript, a source lock, or an authorization to submit.

Throughout, \(K\) is a field of characteristic zero,

\[
1\le e_1<\cdots<e_s=d,
\qquad
a,c,b_1,\ldots,b_s\in K^*,
\]

and

\[
P(X)=c+\sum_{j=1}^s b_jX^{e_j},
\qquad
H(x,y)=(P(x)+ay,x).
\]

Let \(\Gamma\le K^*\) have finite rank \(r\), where

\[
r=\dim_{\mathbb Q}(\Gamma\otimes_{\mathbb Z}\mathbb Q).
\]

No finite-generation hypothesis is imposed.  For \(m\ge0\), put

\[
T_m(H,\Gamma)=
\{Q\in\Gamma^2:H^i(Q)\in\Gamma^2\text{ for }0\le i\le m\}.
\]

The coefficient \(a\ne0\) makes \(H\) invertible, with

\[
H^{-1}(X,Y)=\left(Y,\frac{X-P(Y)}a\right).
\]

## Quantitative unit-equation input and the field bridge

For \(q\ge2\) and \(R\ge0\), set

\[
\mathcal A(q,R)=(8q)^{4q^4(q+R+1)}.
\]

The sole external theorem used in the proofs below is the explicit
nondegenerate unit-equation bound of Amoroso--Viada, Theorem 6.2: if
\(G\le(\overline K^*)^q\) has rank at most \(R\), then the equation

\[
\alpha_1X_1+\cdots+\alpha_qX_q=1,
\qquad \alpha_i\in\overline K^*,
\]

has at most \(\mathcal A(q,R)\) solutions in \(G\) for which no nonempty
proper subsum on the left vanishes.

The published theorem is stated over an algebraically closed field.  To use
it for the arbitrary characteristic-zero field \(K\) above, choose an
algebraic closure \(\overline K\) and regard \(K^*\), \(\Gamma\), and every
coefficient as lying in \(\overline K^*\).  The abstract group \(\Gamma\)
has the same rank after this inclusion; likewise, every homomorphic image
used below has rank no larger than the stated rank.  The solutions defined
over \(K\) inject into the solutions over \(\overline K\).  Thus the
algebraically closed theorem supplies an upper bound for the original
solution set.  No descent assertion is being used.

## Lemma 1: a sparse polynomial cannot hit the torus too often

For \(2\le q\le s+1\), define

\[
\mathcal S_q(d,r)
=d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr),
\qquad
\mathcal S_*=
\max_{2\le q\le s+1}\mathcal S_q(d,r).
\]

> **Sparse-image lemma.**  Let
> \[
> F(X)=\sum_{\ell=1}^q f_\ell X^{m_\ell}\in K[X]
> \]
> have \(q\ge2\) nonzero terms, distinct exponents
> \(0\le m_1<\cdots<m_q\le d\), and let \(\lambda\in K^*\).  Then
> \[
> \#\{(t,u)\in\Gamma^2:\lambda u=F(t)\}
> \le \mathcal S_q(d,r).
> \]

### Proof

Normalize the equation as

\[
\sum_{\ell=1}^q
\frac{f_\ell}{\lambda}\,t^{m_\ell}u^{-1}=1.
\]

The variable tuple

\[
\bigl(t^{m_1}u^{-1},\ldots,t^{m_q}u^{-1}\bigr)
\]

lies in the image of the homomorphism

\[
\Gamma^2\longrightarrow(K^*)^q,
\qquad
(t,u)\longmapsto
\bigl(t^{m_1}u^{-1},\ldots,t^{m_q}u^{-1}\bigr).
\]

That image has rank at most \(2r\).  Amoroso--Viada therefore gives at most
\(\mathcal A(q,2r)\) nondegenerate image tuples.  From the ratio of any two
coordinates one obtains

\[
t^{m_j-m_i}=X_j/X_i.
\]

Because \(1\le m_j-m_i\le d\), this equation has at most \(d\) roots in a
characteristic-zero field.  Once \(t\) is fixed, the original equation fixes
\(u\).  The nondegenerate contribution is consequently at most
\(d\mathcal A(q,2r)\).

For a degenerate solution, some nonempty proper subset \(I\subset[q]\)
satisfies

\[
\sum_{\ell\in I} f_\ell t^{m_\ell}u^{-1}=0.
\]

A singleton cannot vanish because \(f_\ell,t,u\ne0\).  Hence
\(2\le |I|\le q-1\), and there are

\[
2^q-q-2
\]

possible subsets.  For each one, \(t\) is a nonzero root of the nonzero
polynomial

\[
F_I(X)=\sum_{\ell\in I}f_\ell X^{m_\ell},
\]

which has at most \(d\) roots.  Again \(u\) is then unique.  A union bound
gives at most \(d(2^q-q-2)\) degenerate pairs and proves the lemma. \(\square\)

### Torsion audit

Finite rank includes arbitrary torsion.  The Amoroso--Viada theorem is
formulated in terms of rank and does not require the torsion subgroup to be
finite.  The only fiber estimate above is the elementary fact that a
nonzero polynomial of degree at most \(d\) has at most \(d\) roots in
characteristic zero.  Thus infinite torsion creates no omitted fiber.

## Theorem PC1: two-transition finiteness for support size at least two

For nonempty \(J\subseteq[s]\), write

\[
e_{\max J}=\max_{j\in J}e_j,
\qquad
e_{\min J}=\min_{j\in J}e_j,
\qquad
B_J(X)=\sum_{j\in J}b_jX^{e_j}.
\]

Define, by the two displayed subset sums,

\[
\boxed{
\begin{aligned}
\mathcal M(\mathbf e)
={}&2(2^s-1)\\
&+\sum_{\substack{J\subseteq[s]\\|J|\ge2}}
  (e_{\max J}-e_{\min J})
+\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}.
\end{aligned}}
\]

> **PC1.**  If \(s\ge2\), then
> \[
> \boxed{
> \#T_2(H,\Gamma)
> \le
> d\mathcal A(s+2,3r)+\mathcal M(\mathbf e)\mathcal S_*.
> }
> \]

### Proof: the first local equation

Write a point and its first two images as

\[
Q=(v,u),
\qquad
H(Q)=(z,v),
\qquad
H^2(Q)=(w,z).
\]

Membership in \(T_2\) means

\[
u,v,z,w\in\Gamma,
\]

and the two recurrence equations are

\[
z=c+\sum_{j=1}^s b_jv^{e_j}+au,
\qquad
w=c+\sum_{j=1}^s b_jz^{e_j}+av.
\]

Normalize the first one as

\[
Z+U+\sum_{j=1}^sM_j=1,
\]

where the notation is fixed once and for all by

\[
Z=\frac zc,
\qquad
U=-\frac{au}{c},
\qquad
M_j=-\frac{b_jv^{e_j}}c.
\]

The variable tuple

\[
(z,u,v^{e_1},\ldots,v^{e_s})
\]

lies in a homomorphic image of \(\Gamma^3\), of rank at most \(3r\).
The coefficients \(1/c,-a/c,-b_j/c\) are fixed coefficients of the linear
equation; they are not adjoined to the variable group.  If the normalized
equation is nondegenerate, Amoroso--Viada gives at most
\(\mathcal A(s+2,3r)\) variable tuples.  Each tuple has at most \(d\)
preimages \(v\): the common values \(v^{e_j}\) determine a power of \(v\),
whose kernel has size at most \(d\).  Then \(u\) is already a coordinate of
the tuple and \(Q=(v,u)\) is fixed.  Hence

\[
\#\{Q\in T_2:\text{first local equation nondegenerate}\}
\le d\mathcal A(s+2,3r).
\]

### Proof: exhaustive degeneracy audit

Suppose now that the normalized equation is degenerate.  Choose one
nonempty proper vanishing subsum.  Its set of monomial labels is denoted
\(J\subseteq[s]\).  According to whether that subsum contains \(Z\) and
\(U\), there are exactly four types.

#### Type GZ: \(Z\) in, \(U\) out

Here \(J\ne\varnothing\), and the vanishing subsum together with its
complement gives

\[
z=B_J(v),
\qquad
-au=c+B_{J^c}(v).
\]

The two polynomials on the right have respectively

\[
|J|
\quad\text{and}\quad
1+s-|J|
\]

terms, whose sum is \(s+1\ge3\).  Thus one has at least two terms.  If
\(J=[s]\), use \(z=B_J(v)\), which has \(s\ge2\) terms.  If \(|J|=1\), use
\(-au=c+B_{J^c}(v)\), which has \(s\ge2\) terms.  The remaining cases may
use either multi-term side.  Lemma 1, with input \(v\) and output \(z\) or
\(u\), bounds the graph by \(\mathcal S_*\).  Once \(v\) is known, both
\(z\) and \(u\) are fixed, so imposing the second recurrence can only
remove points.  There are \(2^s-1\) labels \(J\).

#### Type GU: \(Z\) out, \(U\) in

Again \(J\ne\varnothing\), and

\[
au=-B_J(v),
\qquad
z=c+B_{J^c}(v).
\]

The same term counts \(|J|\) and \(1+s-|J|\) apply.  In particular, the
endpoint cases \(J=[s]\) and \(|J|=1\) are covered exactly as above.
Lemma 1 gives at most \(\mathcal S_*\) points for each of the
\(2^s-1\) labels.

#### Type R0: neither \(Z\) nor \(U\) in

Now \(|J|\ge2\) and

\[
B_J(v)=0.
\]

After factoring \(X^{e_{\min J}}\), the remaining nonzero polynomial has
degree \(e_{\max J}-e_{\min J}\) and nonzero constant term.  Since
\(v\in\Gamma\subset K^*\), there are at most

\[
e_{\max J}-e_{\min J}
\]

possible values \(v=\rho\).

#### Type R1: both \(Z\) and \(U\) in

The chosen subsum cannot contain all the \(M_j\), because it is proper.
Put \(J\) equal to the nonempty complementary set of monomial indices.
The complementary equation is

\[
c+B_J(v)=0.
\]

This nonzero polynomial has degree \(e_{\max J}\), so it has at most
\(e_{\max J}\) possible values \(v=\rho\).

### Proof: closing every root fiber at the second step

Both root types leave \(u\), hence \(z\), potentially free after \(v=\rho\)
is fixed.  The second recurrence supplies

\[
w=(c+a\rho)+\sum_{j=1}^s b_jz^{e_j}.
\]

If \(c+a\rho\ne0\), the right side has \(s+1\) distinct nonzero terms.  If
\(c+a\rho=0\), the constant term disappears but the right side still has
exactly \(s\ge2\) distinct nonzero terms.  Lemma 1, with input \(z\), output
\(w\), and \(\lambda=1\), therefore gives at most \(\mathcal S_*\) pairs
\((z,w)\).  For fixed \(v=\rho\) and \(z\), the first recurrence uniquely
recovers

\[
u=\frac{z-P(\rho)}a.
\]

Thus every allowed root contributes at most \(\mathcal S_*\) points of
\(T_2\).

Summing the two graph families and the two root families gives

\[
\begin{aligned}
\#T_2
\le{}&d\mathcal A(s+2,3r)\\
&+\Biggl[
2(2^s-1)
+\sum_{\substack{J\subseteq[s]\\|J|\ge2}}
(e_{\max J}-e_{\min J})
+\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}
\Biggr]\mathcal S_*,
\end{aligned}
\]

which is PC1.

A point can have several vanishing proper subsums.  The proof chooses any
one and then unions over every possible label.  Therefore simultaneous
zero subsums are deliberately overcounted, never omitted; disjointness of
the four displayed families is neither asserted nor needed. \(\square\)

## Checks on the component budget

The subset sums, not a closed form, define \(\mathcal M(\mathbf e)\).  The
following identities are useful independent checks.  Since a subset with
largest index \(k\) can contain any subset of \([k-1]\),

\[
\sum_{\varnothing\ne J\subseteq[s]}e_{\max J}
=\sum_{k=1}^s2^{k-1}e_k.
\]

Separating maxima and minima in the spread sum gives

\[
\sum_{\substack{J\subseteq[s]\\|J|\ge2}}
(e_{\max J}-e_{\min J})
=\sum_{k=1}^s
(2^{k-1}-2^{s-k})e_k.
\]

Consequently

\[
\mathcal M(\mathbf e)
=2^{s+1}-2+\sum_{k=1}^s(2^k-2^{s-k})e_k.
\]

Using only \(e_{\max J}-e_{\min J}\le d\) and
\(e_{\max J}\le d\) gives the cruder checksum

\[
\mathcal M(\mathbf e)
\le2(2^s-1)+d(2^{s+1}-s-2).
\]

## Theorem PC2: sharpness of the two-transition window

> **PC2.**  For every prescribed support
> \(1\le e_1<\cdots<e_s\) with \(s\ge2\), there are rational nonzero
> coefficients and a rank-one subgroup for which \(T_1\) is infinite.

### Proof

Take

\[
K=\mathbb Q,
\qquad
a=1,
\qquad
b_1=\cdots=b_s=1,
\qquad
c=-s,
\qquad
\Gamma=\langle2\rangle.
\]

Then \(P(1)=0\).  For every \(n\ge0\),

\[
Q_n=(1,2^n)\in\Gamma^2,
\qquad
H(Q_n)=(2^n,1)\in\Gamma^2.
\]

The points \(Q_n\) are distinct, so \(T_1\) is infinite.  Together with
PC1, this proves that two transitions are the shortest coefficient-uniform
finite window for every support size \(s\ge2\). \(\square\)

If the field contains all roots of unity, the same construction with
\(\Gamma=\mu_\infty\) also produces a rank-zero example.  This observation
does not replace the rational rank-one headline.

## Theorem PC3: the fully absorbed support-one result

Now let \(s=1\), so

\[
P(X)=c+bX^d,
\qquad
H(x,y)=(bx^d+ay+c,x),
\qquad d\ge2.
\]

> **PC3.**  For every finite-rank \(\Gamma\le K^*\),
> \[
> \#T_4(H,\Gamma)
> \le4d\mathcal A(3,3r)+81d^2.
> \]
> For every \(d\ge2\), a number-field, rank-one example has infinite
> \(T_3\).

### Proof of the upper bound: local labels

Write the scalar recurrence

\[
x_{i+1}=bx_i^d+ax_{i-1}+c,
\qquad
H^i(x_0,x_{-1})=(x_i,x_{i-1}).
\]

There are four local equations for a point of \(T_4\), at
\(i=0,1,2,3\).  Normalizing any one of them gives

\[
\frac{x_{i+1}}c-\frac bcx_i^d-\frac acx_{i-1}=1,
\]

has three variable terms, and the corresponding tuple

\[
(x_{i+1},x_i^d,x_{i-1})
\]

lies in an image of \(\Gamma^3\) of rank at most \(3r\).  If that local
three-term unit equation is nondegenerate, Amoroso--Viada gives at most
\(\mathcal A(3,3r)\) tuples and the power fiber gives at most \(d\)
choices for \(x_i\).  Since \(a\ne0\), the recovered local state determines
the initial state by forward or inverse iteration.  Unioning over the four
indices contributes at most

\[
4d\mathcal A(3,3r).
\]

It remains to count points for which all four local equations are
degenerate.  Put

\[
\alpha=-c/a.
\]

The only possible vanishing proper subsums give at least one of the three
labels

\[
\begin{array}{lll}
A_i:&x_{i-1}=\alpha,&x_{i+1}=bx_i^d,\\
B_i:&bx_i^d=-c,&x_{i+1}=ax_{i-1},\\
C_i:&bx_i^d=-ax_{i-1},&x_{i+1}=c.
\end{array}
\]

Singletons cannot vanish.  If several pair subsums vanish, assign any one
label; the eventual union over words handles the overlap.

### The nine adjacent transitions

At a fixed index put \(u=x_{i-1}\) and \(v=x_i\).  Direct substitution for
two adjacent labels gives:

| word | necessary conditions on \(u,v\) | bound or status |
|---|---|---:|
| \(AA\) | \(u=\alpha,\ v=\alpha\) | \(1\) |
| \(AB\) | \(u=\alpha,\ b^{d+1}v^{d^2}=-c\) | \(d^2\) |
| \(AC\) | \(u=\alpha,\ b^{d+1}v^{d^2}=-av\) | \(d^2-1\) |
| \(BA\) | \(v=\alpha,\ b\alpha^d=-c\) | \(u\) free |
| \(BB\) | \(v^d=-c/b,\ u^d=-c/(ba^d)\) | \(d^2\) |
| \(BC\) | \(v^d=-c/b,\ u^d=-v/(ba^{d-1})\) | \(d^2\) |
| \(CA\) | \(v=\alpha,\ u=-b\alpha^d/a\) | \(1\) |
| \(CB\) | \(bc^d=-c,\ u=-bv^d/a\) | \(v\) free |
| \(CC\) | \(v=-bc^d/a,\ u=-bv^d/a\) | \(1\) |

Thus only \(BA\) and \(CB\) can remain free after two labels.

For \(BA\), compatibility requires \(b\alpha^d=-c\), and the coordinate
chain is

\[
t,\ \alpha,\ at,\ ba^dt^d.
\]

The third label imposes respectively

\[
\begin{array}{lll}
BAA:&at=\alpha,&\le1,\\
BAB:&b^{d+1}a^{d^2}t^{d^2}=-c,&\le d^2,\\
BAC:&b^{d+1}a^{d^2}t^{d^2}=-a^2t,&\le d^2-1.
\end{array}
\]

So every \(BA\)-branch closes by the third label.

For \(CB\), compatibility is

\[
bc^d=-c,
\qquad\text{equivalently}\qquad bc^{d-1}=-1,
\]

and the chain is

\[
-bt^d/a,\ t,\ c,\ at.
\]

The next label gives

\[
\begin{array}{lll}
CBA:&c=\alpha,&\text{free only if }a=-1,\\
CBB:&ba^dt^d=-c,&\le d,\\
CBC:&ba^dt^d=-ac,&\le d.
\end{array}
\]

Only \(CBA\) can survive freely.  Under its compatibility conditions
\(a=-1\) and \(bc^{d-1}=-1\), its chain is

\[
bt^d,\ t,\ c,\ -t,\ b(-t)^d.
\]

The fourth label imposes

\[
\begin{array}{lll}
CBAA:&-t=c,&\le1,\\
CBAB:&b^{d+1}(-t)^{d^2}=-c,&\le d^2,\\
CBAC:&b^{d+1}(-t)^{d^2}=-t,&\le d^2-1.
\end{array}
\]

It follows that every word of four labels has at most \(d^2\) initial
states.  There are \(3^4=81\) words.  Unioning over them gives the
degenerate contribution \(81d^2\), including every simultaneous-label
point, and proves the upper bound.

### Proof of support-one sharpness

Choose \(c\) with \(c^{d-1}=-1\), and set

\[
K=\mathbb Q(c),
\qquad
b=1,
\qquad
a=-1,
\qquad
\Gamma=\langle2,c,-1\rangle.
\]

The elements \(c\) and \(-1\) are torsion, so \(\Gamma\) has rank one.
For \(t=2^n\), let \(Q_t=(t,t^d)\).  With the scalar convention above,
the orbit segment is

\[
x_{-1},x_0,x_1,x_2,x_3
=t^d,\ t,\ c,\ -t,\ (-t)^d.
\]

Indeed,

\[
t^d-t^d+c=c,
\qquad
c^d-t+c=-t,
\qquad
(-t)^d-c+c=(-t)^d,
\]

where \(c^d=-c\).  Thus \(Q_t,H(Q_t),H^2(Q_t),H^3(Q_t)\) all lie in
\(\Gamma^2\), and the distinct values \(t=2^n\) make \(T_3\) infinite.
This completes PC3. \(\square\)

## Essential-assumption counterexamples

### The constant term cannot vanish

Let \(d\ge2\), \(P(X)=X^d+X\), \(a=-1\), and let \(\Gamma\) be any
infinite subgroup.  Then

\[
(t,t^d)\longmapsto(t,t)\longmapsto(t^d,t)
\]

for every \(t\in\Gamma\).  Hence \(T_2\) is infinite when \(c=0\), even
with two nonconstant monomials.

### The Hénon coefficient cannot vanish

Take \(P(X)=-1+X+X^2\), so \(P(1)=1\), and put \(a=0\).  Then

\[
(1,t)\longmapsto(1,1)\longmapsto(1,1)
\]

for every \(t\) in an infinite subgroup.  The initial second coordinate is
forgotten, so \(T_2\) is infinite.  This is also why the theorem is stated
for Hénon automorphisms, not triangular degenerations.

### Support size one is genuinely different

The free chain \(CBA\) above yields infinite \(T_3\), so PC1 cannot be
extended to \(s=1\).  PC3 gives the exact replacement window.

## Absorption and proof provenance

PC3 reproduces the full support-one proof so that the present theorem
package is logically standalone.  Its local predecessor is identified by
terminal-review SHA-256
`9cfb8b2cb492dc6bea84231a81c8f7b7c698eea5299a357d066339180b14260d`
and PDF SHA-256
`4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414`.
That project is absorbed provenance only and must not be submitted in
parallel with a later Paper16 manuscript.

## Proof nonclaims

Nothing above proves positive-characteristic finiteness, optimality of the
constants, effective enumeration, height bounds, affine-conjugacy
invariance, a periodic-point classification, or a classification of free
chains after dropping \(a\ne0\) or \(c\ne0\).  Coefficients are never
assumed to lie in \(\Gamma\), and addition is never performed inside
\(\Gamma\).
