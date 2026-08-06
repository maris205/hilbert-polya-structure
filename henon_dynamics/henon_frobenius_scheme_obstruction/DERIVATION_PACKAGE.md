# Derivation package

## Target

Determine whether the Paper-5 area-preserving Hénon recurrence supports a
nontrivial fixed-period Frobenius zeta mechanism, and identify exactly what
arithmetic/dynamical information survives if it does not.

## Status

- cyclic periodic scheme and finite-flat rank: **PROVED**;
- good-prime and étale criteria: **PROVED**;
- fixed-\(n\) Frobenius permutation determinant: **PROVED**;
- loss of nilpotent multiplicity: **PROVED**;
- insufficiency of rectangular counts: **PROVED by finite control**;
- fixed-\(n\) local rationality as distinctive Route-A evidence:
  **REFUTED / SCOPED NO-GO**;
- global Artin, joint-action, and positive-dimensional mechanisms:
  **OPEN and not tested by this obstruction**;
- higher-period Galois-tower novelty: **OPEN, with period five duplicated by
  prior work**.

## Invariant object

Work over

\[
B=\mathbb Z[A,A^{-1}]
\]

with

\[
H_A(q,p)=(1-Aq^2-p,q).
\]

For each chronological period \(n\), the invariant object is the affine fixed
scheme

\[
\mathcal X_n=\operatorname{Fix}(H_A^n).
\]

At a finite-field fiber the chronology-preserving representation is generated
by the commuting permutations \(H_A\) and Frobenius on
\(\mathcal X_n(\overline{\mathbb F}_p)_{\rm red}\).

## Assumptions

1. \(A\) is invertible for the uniform quadratic family.
2. Ordinary Hasse--Weil point counts mean morphisms from
   \(\operatorname{Spec}\mathbb F_{p^r}\); they do not carry local Artin
   length.
3. A fiber is called `etale_good(a,n)` only when it is degree-good and every
   geometric fixed point is transverse.
4. Exact-period set formulas are used only on reduced fibers; scheme-level
   dynatomic multiplicities require separate hypotheses.
5. The period-two splitting is asserted over \(\mathbb Q(A)\), equivalently
   away from its branch collision at \(A=3\), not at every specialization.

## Notation

\[
X_{a,n}=\operatorname{Fix}(H_a^n),\qquad
S_{a,p,n}=X_{a,n}(\overline{\mathbb F}_p)_{\rm red},
\]

\[
N_{a,p}(r,n)=\#X_{a,n}(\mathbb F_{p^r}),
\]

\[
T_{a,p,n}(r,s)=
\operatorname{Tr}(F_p^rH_a^{-s}\mid\mathbb Q_\ell[S_{a,p,n}]).
\]

Here \(F_p:x\mapsto x^p\) is arithmetic Frobenius.  Switching to geometric
Frobenius inverts \(F_p\) and correspondingly reverses the joint-action
convention.

## Strategy

1. Replace iterated bivariate expressions by the exact cyclic recurrence.
2. Use a monic Gröbner basis to prove uniform finite flatness.
3. Separate coefficient-goodness, étaleness, support cardinality, and local
   length.
4. Apply the zero-dimensional Frobenius trace formula directly.
5. Test whether ordinary rectangular counts retain the joint action.
6. Audit the first nontrivial Galois case against primary literature before
   claiming novelty.

## Map from assumptions to claims

| Assumption/input | Derived claim |
|---|---|
| \(A\in B^\times\) | monic leading terms \(x_i^2\) |
| pairwise-coprime leading monomials | finite free rank \(2^n\) |
| transverse fixed points | finite étale fiber |
| finite reduced geometric support | Frobenius is a finite permutation |
| finite permutation | cyclotomic local zeta and periodic \(r\)-sequence |
| ordinary field-valued points | nilpotents are invisible |
| only \(s=0\) joint traces retained | relative chronology can be lost |

## Main derivation

Write

\[
H_A^i(x_0,x_{-1})=(x_i,x_{i-1}).
\]

Then

\[
x_{i+1}+x_{i-1}+Ax_i^2-1=0.
\]

With neighbors counted as a multiset modulo \(n\), define

\[
f_i=Ax_i^2+x_{i-1}+x_{i+1}-1.
\]

Thus

\[
\mathcal X_n\simeq
\operatorname{Spec}B[x_0,\ldots,x_{n-1}]/(f_0,\ldots,f_{n-1}).
\]

Scheme-theoretically, the forward map sends \((q,p)\) to
\(x_i=\pi_1H_A^i(q,p)\), and its inverse sends a cyclic tuple to
\((x_0,x_{n-1})\).  For \(n=1\) the inverse is
\(x_0\mapsto(x_0,x_0)\); for \(n=2\) it is
\((x_0,x_1)\mapsto(x_0,x_1)\).  The recurrence identities verify both
compositions on coordinate rings.

The multiset convention gives the necessary exceptional formulas

\[
n=1:\quad Ax_0^2+2x_0-1,
\]

\[
n=2:\quad
Ax_0^2+2x_1-1,
\quad
Ax_1^2+2x_0-1.
\]

Divide each equation by the unit \(A\).  Under any degree-compatible term
order its leading monomial is \(x_i^2\).  The leading monomials are pairwise
coprime, so the monic Buchberger product criterion applies over \(B\).  The
standard monomials are

\[
x_0^{e_0}\cdots x_{n-1}^{e_{n-1}},\qquad e_i\in\{0,1\}.
\]

Therefore

\[
\boxed{\mathcal X_n\to\operatorname{Spec}B
\text{ is finite flat of rank }2^n.}
\]

For an integer \(a\ne0\), every prime \(p\nmid a\) is degree-good and the
fiber has scheme length \(2^n\).  Reducedness is an additional condition.  If
\(J_n=(\partial f_i/\partial x_j)\) and

\[
M_n=DH_a(H_a^{n-1}x)\cdots DH_a(x),
\]

then the cyclic Hill identity gives

\[
\det J_n=(-1)^{n+1}\det(I-M_n).
\]

Hence the degree-good fiber is étale exactly when all periodic points have no
multiplier 1.  A prime \(p\mid a\) is outside
\(\operatorname{Spec}\mathbb Z[A,A^{-1}]\); direct reduction of the original,
uninverted \(\mathbb Z[A]\)-family instead gives

\[
H_0(q,p)=(1-p,q),\qquad H_0^4=I,
\]

so \(X_{a,4}\) becomes \(\mathbb A^2\); such primes are genuine degree-drop
cells.  Every **degree-good** characteristic-two fiber (\(a\ne0\)) is
non-étale: there
\(DH_a=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), whose
every power has eigenvalue \(1\).  This is intentionally not extended to
\(a=0\), where some fixed schemes are empty (hence étale) while
\(X_{0,4}=\mathbb A^2\).

For any finite zero-dimensional fiber, write the Frobenius orbits on its
reduced geometric support with lengths \(d\) and multiplicities \(c_d\).
Direct finite-set algebra gives

\[
N_{a,p}(r,n)=\sum_{d\mid r}d c_d,
\]

\[
Z_{a,p,n}(u)
=\exp\left(\sum_{r\ge1}N_{a,p}(r,n)\frac{u^r}{r}\right)
=\prod_d(1-u^d)^{-c_d}
=\det(I-uF_p\mid\mathbb Q_\ell[S_{a,p,n}])^{-1}.
\]

Every eigenvalue is a root of unity and only \(H_c^0\) occurs.  The same
formula applies to a nonreduced finite fiber; nilpotents do not add
eigenvalues.  The separately labelled nonstandard statistic used in the
certificate is
\[
N^{\mathrm{len}}(r)=
\sum_{x\in X(\mathbb F_{p^r})}
\ell(\mathcal O_{X_{\overline{\mathbb F}_p},x}).
\]
An orbit of degree \(d\) and geometric local length \(m\) contributes
\((1-u^d)^{-m}\), so this too remains a weighted finite-permutation product.

Finally, ordinary counts retain only

\[
N(r,n)=T(r,0;n).
\]

On the reversible pair of five-cycles
\(\{\pm1\}\times\mathbb Z/5\), set
\(H(\varepsilon,i)=(\varepsilon,i+1)\),
\(R(\varepsilon,i)=(-\varepsilon,-i)\), and
\(F_c(\varepsilon,i)=(\varepsilon,i+\varepsilon c)\).  The choices
\(c=1,2\) both commute with \(H\) and \(R\), have identical ordinary
fixed-count sequences, and have different \(T(r,s)\).  Thus the original
two-index table is not a complete invariant even among matched reversible
joint actions.

## Remarks

- If the characteristic-zero finite algebra is reduced and decomposes as
  \(\prod_i K_i\), its global arithmetic zeta is, away from finitely many
  primes, \(\prod_i\zeta_{K_i}(s)\).  Such factors can have nontrivial global
  zeros and can contain \(\zeta(s)\); the obstruction is therefore to
  **novelty and discriminating power**, not to every global RH connection.
- For \(a=6\), \(n=1\) gives \(\mathbb Q(\sqrt7)\), with
  \(\zeta_{\mathbb Q(\sqrt7)}=\zeta L(\chi_{28})\), while the primitive
  period-two branch gives \(\mathbb Q(\sqrt3)\), with character \(\chi_{12}\).
  These inherited classical factors are not a new Hénon encoding of the
  Riemann divisor.
- The reversor \(R(q,p)=(p,q)\) satisfies \(RH_aR=H_a^{-1}\), so Galois
  centralizes a dihedral action on exact-period points.  This constraint must
  be built into every control.

## Boundaries

This package does **not** prove that every fixed-\(a\) characteristic-zero
fiber is reduced for all \(n\).  It neither rules out the zeros of classical
global Artin factors nor identifies a new Riemann divisor, an
analytic continuation beyond classical Artin factors, a transfer operator, or
a self-adjoint lift.  It does not transfer projective-morphism dynatomic
theorems verbatim to the birational compactification of a Hénon map.

## Open risks

1. A positive-dimensional parameter quotient may have nontrivial \(H^1\), but
   its canonicity and relation to RH are entirely open.
2. Higher-period Galois images may contain new dihedral-centralizer
   obstructions, but low-period elimination alone is heavily covered by prior
   work.
3. Scheme-theoretic formal period in characteristic dividing \(n\) can differ
   from primitive set period.
4. A full higher-rank zeta requires twisted, nonrectangular subgroup data and
   analytic hypotheses absent from the global algebraic-closure phase space.
