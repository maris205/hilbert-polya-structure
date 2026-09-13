# Proof Package

## Claim

For fixed integers \(d,n\ge2\), the family

\[
H_{a,c}(x,y)=(a y+x^d+c,x)
\]

has the normalized primitive-point and primitive-cycle covers PC1 and the two
primitive cycle coordinates PC2 defined in RESEARCH_QUESTION.md.

## Status

**SOURCE_LOCKED_V2 / PENDING_INDEPENDENT_R2 / NO_CODE / NO_RESULTS.**

The immutable Round-1 review found no mathematical counterexample and judged
the theorem-level proof sound, but returned `REPAIR_REQUIRED` for lifecycle
and literature-disclosure defects. No Round-2 source-review pass has yet been
issued. The proof imports the established full-centralizer monodromy theorem
for the scalar unicritical family \(z^d+c\). Independent Round-2 review must
check extraction of its exact-period factor, the passage to the geometric
constant field, and the restriction map into the global family.

## Assumptions

- \(d,n\ge2\) are fixed integers.
- The base is \(A=\mathbb Q[a,c]\), with fraction field
  \(K=\mathbb Q(a,c)\).
- Characteristic zero is essential for separability, the Reynolds operator,
  and the geometric-constants step.
- Gao–Ou's scalar theorem supplies the smooth geometrically integral affine
  dynatomic curve for \(z^d+c\).
- The established scalar monodromy theorem supplies
  \(C_n\wr S_r\) on exact-period points, hence \(S_r\) on cycles. The
  exact all-degree source is Morton (1998), Theorem D/Theorem 10;
  Fakhruddin (2014), Theorem 3.2, restates it over every characteristic-zero
  constant field, so taking \(k=\overline{\mathbb Q}\) gives the geometric
  group directly.

No hypothesis is made that every parameter fiber is smooth, reduced, étale,
or an actual-period torsor.

## Notation

Use cyclic indices modulo \(n\) and put

\[
g_i=z_i^d+a z_{i-1}+c-z_{i+1},
\qquad
B_n=A[\mathbf z]/(g_0,\ldots,g_{n-1}).
\]

Put

\[
\nu=\sum_{e\mid n}\mu(n/e)d^e,\qquad r=\nu/n.
\]

Let \(e_n\) be the generic actual-exact-\(n\) idempotent,

\[
E_n=e_n(B_n\otimes_AK),
\]

let \(S\) be the integral closure of \(A\) in \(E_n\), and let

\[
\sigma(z_i)=z_{i+1},\qquad
S_0=S^{\langle\sigma\rangle},\qquad
F=\operatorname{Frac}(S_0).
\]

On \(a=0\), write

\[
D_n=\mathbb Q[c,z]/(\Phi_{d,n}(z,c)).
\]

For derivative traces set

\[
u_i=d z_i^{d-1},\qquad
M_i=\begin{pmatrix}u_i&a\\1&0\end{pmatrix},
\]

\[
\tau=\sum_i z_i,\qquad
\rho=\operatorname{tr}(M_{n-1}\cdots M_0).
\]

## Dependency map

\[
\begin{array}{c}
\text{monic Gröbner basis}\\
\Downarrow\\
B_n/A\text{ finite free of rank }d^n\\
\Downarrow\\
\text{generic étale algebra and actual-period idempotent}\\
\Downarrow\\
\text{Henselian scalar lift}\Rightarrow E_n\text{ one field}\\
\Downarrow\\
\text{excellent normalization + CM + miracle flatness}\\
\Downarrow\\
S/A\text{ finite locally free}\\
\Downarrow\\
\text{unique }a\text{-adic prime, }e=1,\text{ normal comparison}\\
\Downarrow\\
S/aS=D_n,\quad \operatorname{Spec}S\text{ geometrically integral}\\
\Downarrow\\
\text{Reynolds invariants and scalar full-wreath restriction}\\
\Downarrow\\
S_0/aS_0=D_n^{C_n},\quad \operatorname{Mon}=S_r\\
\Downarrow\\
\text{two infinity-word separations}\\
\Downarrow\\
K(\tau)=F=K(\rho)\\
\Downarrow\\
\text{top-wedge characteristic polynomials of degree }r.
\end{array}
\]

## Proof

### Step 1. The cyclic equations are a monic Gröbner basis

Choose any graded monomial order in the variables \(z_0,\ldots,z_{n-1}\),
treating \(A\) as the coefficient ring. Because \(d\ge2\),

\[
\operatorname{LM}(g_i)=z_i^d.
\]

The leading coefficients are \(1\), and the leading monomials are pairwise
coprime. The monic version of Buchberger's product criterion over a
coefficient ring therefore reduces every \(S\)-polynomial to zero. Thus the
\(g_i\) form a monic Gröbner basis.

The standard monomials are exactly

\[
\mathcal B=\left\{\prod_{i=0}^{n-1}z_i^{e_i}:0\le e_i<d\right\}.
\]

Monic division gives existence and uniqueness of the remainder over \(A\).
Consequently \(\mathcal B\) is an \(A\)-basis of \(B_n\), and

\[
\operatorname{rank}_A B_n=d^n.
\]

This is an integral finite-freeness statement. It is not inferred from a
generic point count.

### Step 2. Generic étaleness and the actual-period idempotent

At \(a=0\), the recurrence identifies the full special fixed algebra over
\(\mathbb Q(c)\) with

\[
\mathbb Q(c)[z]/(f_c^n(z)-z),\qquad f_c(z)=z^d+c.
\]

Over the function field \(\mathbb Q(c)\), the dynatomic factors for divisors
of \(n\) are separable and pairwise coprime. Equivalently, the full scalar
fixed polynomial has no repeated root at the generic \(c\). Hence one fiber
of the finite-free discriminant is étale, so

\[
B_n\otimes_AK
\]

is a finite étale \(K\)-algebra.

Over \(\overline K\), its points are the fixed points of \(H^n\). The subset
with actual least period \(n\) is stable under
\(\operatorname{Gal}(\overline K/K)\) and is clopen in this finite discrete
set. It therefore has a unique idempotent \(e_n\). Möbius inversion gives its
cardinality

\[
\nu=\sum_{e\mid n}\mu(n/e)d^e.
\]

Thus \(E_n=e_n(B_n\otimes_AK)\) is finite étale of dimension \(\nu\). At this
stage it could a priori be a product of fields; the next step rules that out.

This construction deliberately occurs only in the generic étale algebra.
Formal-period points on special branch fibers are not removed by defining an
embedded open-and-closed subscheme over all of \(A\).

### Step 3. Henselian lifting makes \(E_n\) one field

Let

\[
R=A_{(a)}=\mathbb Q[c,a]_{(a)}.
\]

This is a DVR with uniformizer \(a\), fraction field \(K\), and residue field
\(k=\mathbb Q(c)\). Let \(R^h\) be its henselization.

The special full fixed algebra is finite étale over \(k\), so finite
freeness and Nakayama's lemma show that \(B_n\otimes_AR\) is finite étale
over \(R\). The scalar exact-period idempotent cuts out

\[
D_n\otimes_{\mathbb Q[c]}k
  =k[z]/(\Phi_{d,n}),
\]

which is a field by the scalar irreducibility theorem. The equivalence
between finite étale algebras over a henselian pair and over its residue
field uniquely lifts this idempotent to a finite étale \(R^h\)-algebra
\(C\).

The ring \(C\) is connected because its residue algebra is a field. A
connected finite étale algebra over the normal local domain \(R^h\) is a
normal domain. Therefore \(C[1/a]\) is a field.

To identify this lift, note that a generic lower-period section satisfies
\(H^e(P)=P\) for some proper divisor \(e\mid n\), and its specialization
still satisfies that closed equation. It therefore cannot specialize to a
scalar point of actual period \(n\). Conversely, every point in the lifted
scalar exact block avoids all such lower-period closed loci. Thus the lifted
idempotent is precisely the base change of the canonical generic
actual-period idempotent, and

\[
E_n\otimes_K\operatorname{Frac}(R^h)\simeq C[1/a].
\]

If \(E_n\) had two nonzero product factors over \(K\), their idempotents
would survive every faithfully flat field extension, contradicting the
field on the right. Thus \(E_n\) is one field of degree \(\nu\) over \(K\).

### Step 4. Excellence makes the normalization finite

The ring \(A\) is a finite-type algebra over the field \(\mathbb Q\), hence
excellent and therefore Nagata. The integral closure

\[
S=\overline A^{\,E_n}
\]

is finite over \(A\).

The ring \(S\) is a normal domain of dimension two. Every local ring of \(S\)
has dimension at most two. Normality gives Serre's \(S_2\) condition, which
in dimension at most two is the Cohen–Macaulay condition.

### Step 5. Miracle flatness makes \(S\) locally free

Let \(\mathfrak q\in\operatorname{Spec}S\) and
\(\mathfrak p=\mathfrak q\cap A\). The finite integral map has zero-dimensional
fibers and

\[
\dim S_{\mathfrak q}=\dim A_{\mathfrak p}.
\]

The local base \(A_{\mathfrak p}\) is regular, while
\(S_{\mathfrak q}\) is Cohen–Macaulay. Miracle flatness applies. Hence \(S\)
is flat over \(A\).

Finite flat modules are finite locally free. Since \(\operatorname{Spec}A\)
is connected and the generic rank is \([E_n:K]=\nu\),

\[
S\text{ is finite locally free of rank }\nu.
\]

No conclusion about smoothness or étaleness of every fiber is drawn.

### Step 6. The unique \(a\)-adic prime and its multiplicity

The Henselian calculation in Step 3 contains more information than
connectedness. The normalization of \(R^h\) in the extended exact-period
field is the finite étale domain \(C\). It has:

- one prime over \(a\);
- ramification index \(e=1\);
- residue field
  \[
  k[z]/(\Phi_{d,n})=\mathbb Q(Y_1(n));
  \]
- residue degree \(f=\nu\).

Descending this valuation statement to \(S\), there is a unique height-one
prime \(P\subset S\) above \((a)\), and

\[
\operatorname{div}_S(a)=P
\]

with coefficient one. The degree identity \(ef=\nu\) leaves no additional
prime or multiplicity.

Because \(S\) is Cohen–Macaulay and \(a\) is a nonzerodivisor,
\(S/aS\) is one-dimensional Cohen–Macaulay and hence satisfies \(S_1\).
The coefficient-one valuation says that its localization at its unique
minimal prime is reduced, i.e. it satisfies \(R_0\). The \(R_0+S_1\)
criterion makes \(S/aS\) reduced. With only one minimal prime it is a
domain, and in particular

\[
aS=P.
\]

This is the required flat special-fiber nilpotent exclusion. It rules out
nilpotents supported at closed points as well as generic multiplicity.

As a redundant rank check, \(S/aS\) is \(\mathbb Q[c]\)-flat of rank
\(\nu\). Any nilradical whose reduced quotient already has rank \(\nu\)
would be \(\mathbb Q[c]\)-torsion; a submodule of the torsion-free module
\(S/aS\) cannot have such torsion. This check agrees with, but does not
replace, the height-one divisor proof.

### Step 7. Finite birational normality gives the exact scalar fiber

The images of the integral orbit coordinates \(z_i\) lie in \(S\). Modulo
\(a\), the recurrence gives

\[
z_i=f_c^i(z_0).
\]

The scalar exact-period relation therefore induces a finite map

\[
D_n=\mathbb Q[c,z]/(\Phi_{d,n})\longrightarrow S/aS.
\]

Both rings are domains. Step 6 identifies their fraction fields with the
same residue field \(\mathbb Q(Y_1(n))\), so the map is birational.

Gao–Ou prove that the affine scalar dynatomic curve is smooth and
geometrically integral in characteristic zero. In particular \(D_n\) is
normal. A finite birational overring of a normal domain inside the same
fraction field equals the normal domain. Hence

\[
\boxed{S/aS\simeq D_n.}
\]

The proof has used Henselian lifting, the unique valuation and ramification
index, Cohen–Macaulay reducedness, and normality. It has not assumed that
normalization commutes with arbitrary base change.

### Step 8. Geometric constants and geometric integrality

Let \(k'\) be the relative algebraic closure of \(\mathbb Q\) in \(E_n\).
Since \(E_n/\mathbb Q\) is finitely generated, \(k'/\mathbb Q\) is finite.
Every element of \(k'\) is integral over \(A\), so \(k'\subset S\). Every
nonzero element of \(k'\) has its inverse in \(k'\subset S\), so it is a unit.

Reduction modulo \(a\) injects \(k'\) into \(\operatorname{Frac}(S/aS)\):
a nonzero constant cannot belong to \(aS\), because it is a unit and \(aS\)
is proper. By Step 7,

\[
k'\hookrightarrow\operatorname{Frac}(D_n).
\]

The geometric integrality of \(D_n\) implies that \(\mathbb Q\) is
algebraically closed in \(\operatorname{Frac}(D_n)\). Therefore
\(k'=\mathbb Q\).

In characteristic zero \(E_n/\mathbb Q\) is geometrically reduced, and the
constant-field conclusion makes it geometrically irreducible. Thus
\(E_n\otimes_{\mathbb Q}\overline{\mathbb Q}\) is a field. Flat base change
preserves the injection \(S\hookrightarrow E_n\), so

\[
S\otimes_{\mathbb Q}\overline{\mathbb Q}
\hookrightarrow
E_n\otimes_{\mathbb Q}\overline{\mathbb Q}
\]

is a domain. Hence \(\operatorname{Spec}S\) is geometrically integral over
\(\mathbb Q\).

### Step 9. Cyclic invariants and arbitrary base change

The shift \(\sigma\) preserves the generic exact-period field and extends
uniquely to \(S\), because normalization is functorial under field
automorphisms. On actual exact-period points its order is exactly \(n\).
Artin's fixed-field theorem gives

\[
[E_n:E_n^{C_n}]=n,\qquad [F:K]=r.
\]

Since \(n\) is invertible in \(A\), the Reynolds idempotent

\[
\mathcal R=\frac1n\sum_{j=0}^{n-1}\sigma^j
\]

has image \(S^{C_n}=S_0\). Thus \(S_0\) is a direct summand of the finite
locally free \(A\)-module \(S\), and is finite locally free. Its generic rank
is \(r\).

The image of an idempotent commutes with arbitrary base change: after
tensoring with any \(A\)-algebra \(A'\), \(\mathcal R\otimes1\) is again the
Reynolds projector and its image is the invariant submodule. Therefore

\[
S_0\otimes_AA'\simeq(S\otimes_AA')^{C_n}.
\]

Taking \(A'=A/(a)\) and using Step 7 gives

\[
\boxed{S_0/aS_0\simeq D_n^{C_n}.}
\]

This is the affine scalar orbit curve \(X_0^{\mathrm{aff}}(n)\). The
statement neither asserts a free action on every special fiber nor identifies
this affine quotient with a smooth projective model.

### Step 10. The finite-étale-open cycle cover has monodromy \(S_r\)

Because both \(E_n/K\) and \(F/K\) are finite separable, and because \(S\)
and \(S_0\) are finite locally free, there is a common dense open

\[
U\subset\operatorname{Spec}A
\]

on which both

\[
W=\operatorname{Spec}S\times_AU\longrightarrow U,
\qquad
V=\operatorname{Spec}S_0\times_AU\longrightarrow U
\]

are finite étale, of degrees \(\nu\) and \(r\), respectively. Step 8 shows
that \(\mathbb Q\) is algebraically closed in \(E_n\), hence also in its
subfield \(F\); therefore both generic covers are geometrically connected.

Choose \(U\) so its intersection \(U_0\) with the scalar line \(a=0\)
contains the common good finite-étale locus of the scalar point and cycle
covers. After base change to \(\overline{\mathbb Q}\), Fakhruddin's
characteristic-zero formulation of Morton's theorem gives scalar point
monodromy

\[
C_n\wr S_r
\]

and hence cycle monodromy \(S_r\) over \(U_0\).

Choose compatible geometric base points. The direction of comparison for
geometric fundamental groups is:

\[
\pi_1((U_0)_{\overline{\mathbb Q}})
\longrightarrow\pi_1(U_{\overline{\mathbb Q}})
\longrightarrow S_r.
\]

Thus the restricted scalar image is a **subgroup of** the global image, not
the other way around. Since the restricted image is already \(S_r\), while
the global cycle action is contained in \(S_r\), the global image equals
\(S_r\).

At point level, the same two inclusions give the full centralizer: the global
action commutes with the defined time shift, so it lies in
\(C_n\wr S_r\), while the scalar restriction supplies that entire subgroup.
This marked-point equality is an auxiliary consequence of the cited scalar
input, not a separate advertised novelty claim. Only the quotient conclusion
\(S_r\) is needed for PC1.

When \(r=1\), the assertion is the tautological group \(S_1\) and supplies no
nontrivial monodromy evidence.

### Step 11. Cyclic invariance of \(\tau\) and \(\rho\)

The sum \(\tau=\sum_i z_i\) is visibly invariant under \(\sigma\).

At the point \((z_i,z_{i-1})\),

\[
DH_{a,c}=
M_i=\begin{pmatrix}d z_i^{d-1}&a\\1&0\end{pmatrix}.
\]

Changing the marked point cyclically rotates the product
\(M_{n-1}\cdots M_0\). Matrix trace is invariant under cyclic rotation, so
\(\rho\) is also \(\sigma\)-invariant. Since the \(z_i\) are integral over
\(A\), both elements lie in \(S_0\).

The sign and order check for \(n=2\) is

\[
\operatorname{tr}(M_1M_0)=u_0u_1+2a.
\]

### Step 12. Infinity branches for the scalar line

Work at \(a=0\) and write

\[
c=-q^{-d},\qquad z_i=q^{-1}v_i,\qquad
\epsilon=q^{d-1}.
\]

The scalar recurrence becomes

\[
v_i^d=1+\epsilon v_{i+1}.
\]

For each word

\[
\boldsymbol\omega=(\omega_0,\ldots,\omega_{n-1})\in\mu_d^n
\]

there is a unique formal branch

\[
v_i=\omega_i(1+\epsilon v_{i+1})^{1/d}
\]

with the binomial root normalized to have constant term \(1\). Primitive
words correspond to exact-period branches, and rotation corresponds to
changing the marked point on the same cycle.

On this branch,

\[
\tau=q^{-1}\left(\sum_i\omega_i+O(\epsilon)\right).
\]

At \(a=0\), the derivative matrices have zero upper-right entry, and direct
multiplication gives

\[
\rho=d^n\prod_i z_i^{d-1}.
\]

Consequently

\[
\rho=d^nq^{-n(d-1)}
\left(\prod_i\omega_i^{d-1}+O(\epsilon)\right)
=d^nq^{-n(d-1)}
\left(\prod_i\omega_i^{-1}+O(\epsilon)\right).
\]

The leading invariants for \(\tau\) and \(\rho\) are therefore the word sum
and inverse word product, respectively.

### Step 13. Separate non-base proofs for \(\tau\) and \(\rho\)

Suppose first that \(d\ge3\), and choose a primitive \(d\)-th root
\(\zeta\). Compare the primitive words

\[
(1,\ldots,1,\zeta)
\quad\text{and}\quad
(1,\ldots,1,\zeta^2).
\]

Their sums are \(n-1+\zeta\) and \(n-1+\zeta^2\), which differ. Their inverse
products are \(\zeta^{-1}\) and \(\zeta^{-2}\), which also differ.

Now suppose \(d=2\) and \(n\ge3\). Compare a word with exactly one \(-1\)
with a word having exactly two adjacent \(-1\)'s. Both words are primitive.
Their sums are \(n-2\) and \(n-4\), and their products are \(-1\) and \(1\).
Thus the leading terms differ separately for both observables.

If an element of \(S_0\) belongs to \(K\), then it is integral over \(A\) and
lies in the integrally closed ring \(A=S_0\cap K\). Its scalar specialization
would have the same value on all branches. The two branch comparisons prove

\[
\tau\notin K,\qquad \rho\notin K
\]

for every case with \(r>1\). This is two proofs: the sum comparison proves
the first assertion and the product comparison proves the second.

The only case with \(r=1\) is \((d,n)=(2,2)\). Indeed, for \(n=2\),
\[
r=\frac{d^2-d}{2},
\]
which is one exactly when \(d=2\). For \(n\ge3\), already in the binary
alphabet the one-minus word and the two-adjacent-minus word are primitive and
not rotations of one another, so there are at least two primitive necklaces;
enlarging the alphabet cannot decrease their number. The exceptional case is
handled in Step 16.

#### Direct scalar prior art and why the uniform argument remains

The preceding branch calculation is a uniform proof route, not a claim that
the scalar generators are new. Morton (1996), Corollary 1 and pp. 322--323,
proves the relevant dynatomic and multiplier-polynomial irreducibility for
\(f(z)=z^d+c\). On p. 336, if
\(K_0=\mathbb Q(c,z)\) with \(\Phi_{d,n}(z,c)=0\), he proves

\[
 K_0^{\langle\sigma\rangle}=\mathbb Q(c,w),\qquad
 w=\prod_{i=0}^{n-1}f'(f^i(z))=\rho|_{a=0}.
\]

Thus Morton already supplies the scalar non-base input, indeed scalar
fixed-field generation, for \(\rho\) for all \(d,n\). In degree two,
Corollary 3 on p. 335 proves the orbit-sum trace polynomial irreducible, and
p. 336 records
\(K_0^{\langle\sigma\rangle}=\mathbb Q(c,t)\) for
\(t=\sum_i f^i(z)=\tau|_{a=0}\). Step 13 is retained because it treats both
observables in one two-parameter-compatible language and supplies the needed
uniform \(\tau\) argument for \(d\ge3\); it is redundant with Morton for
\(\rho\) in every degree and for \(\tau\) when \(d=2\). The residual PC2
work is the two-parameter lift and the integral characteristic-polynomial
packaging, not invention of scalar primitive generators.

### Step 14. Full symmetric monodromy makes each observable primitive

Let \(L/K\) be a Galois closure of \(F/K\). By Step 10,

\[
\operatorname{Gal}(L/K)\simeq S_r
\]

in its action on the \(r\) cycles. A chosen marked cycle has stabilizer
\(S_{r-1}\), and

\[
F=L^{S_{r-1}}.
\]

Every element of \(F\), including \(\tau\) and \(\rho\), is fixed by
\(S_{r-1}\). For \(r\ge2\), \(S_{r-1}\) is a maximal proper subgroup of
\(S_r\). Step 13 says that neither observable is fixed by all of \(S_r\).
Hence each stabilizer is exactly \(S_{r-1}\). Therefore

\[
[K(\tau):K]=r=[K(\rho):K],
\]

and, since both generated fields lie in the degree-\(r\) field \(F\),

\[
\boxed{K(\tau)=F=K(\rho).}
\]

Non-base membership alone would not imply primitivity for a general
monodromy group. The maximal-subgroup argument is indispensable.

### Step 15. Top exterior power and irreducible characteristic polynomials

For \(s\in\{\tau,\rho\}\), multiplication by \(s\) is an \(A\)-linear
endomorphism

\[
m_s:S_0\to S_0.
\]

Since \(S_0\) is finite locally free of rank \(r\), define canonically

\[
\chi_s(T)=\det(T\operatorname{id}-m_s)
\]

as the scalar by which
\(\bigwedge_A^r(T\operatorname{id}-m_s)\) acts on the determinant line
\(\bigwedge_A^rS_0\). This definition requires no global basis.

Over \(K\), Step 14 says \(F=K(s)\). Thus

\[
\omega_s=1\wedge s\wedge\cdots\wedge s^{r-1}
\in\bigwedge_K^rF
\]

is nonzero. The minimal polynomial of \(s\) has degree \(r\), so it equals
\(\chi_s\). Hence \(\chi_s\) is irreducible of degree \(r\) in \(K[T]\), and
also in \(A[T]\) because it is monic and \(A\) is a UFD.

Under the \(r\) embeddings of \(F\) in \(L\), the top wedge \(\omega_s\)
maps to the Vandermonde determinant

\[
\prod_{i<j}(s_i-s_j).
\]

Its square is the discriminant of \(\chi_s\), which is nonzero. This records
generic separability only; it is not a claim that every specialized
polynomial is irreducible or separable.

### Step 16. The explicit \((d,n)=(2,2)\) boundary

For \(d=n=2\),

\[
\nu=2,\qquad r=1.
\]

The two cyclic equations are

\[
z_0^2+(a-1)z_1+c=0,\qquad
z_1^2+(a-1)z_0+c=0.
\]

Subtracting gives

\[
(z_0-z_1)(z_0+z_1-(a-1))=0.
\]

On the generic actual two-cycle block, \(z_0\ne z_1\), so

\[
\tau=z_0+z_1=a-1.
\]

Adding the equations and using this sum yields

\[
z_0z_1=(a-1)^2+c.
\]

With \(u_i=2z_i\), Step 11 gives

\[
\rho=u_0u_1+2a
=4z_0z_1+2a
=4a^2-6a+4+4c.
\]

Both characteristic polynomials are linear. This verifies the boundary but
does not support any nontrivial monodromy inference.

## Imported-source ledger

The proof uses or must disclose the following dynamical results.

1. **Scalar dynatomic geometry:** smoothness and geometric irreducibility of
   the affine exact-period curve for \(z^d+c\), from Gao–Ou.
2. **Scalar point monodromy:** the maximal centralizer
   \(C_n\wr S_r\) for exact-period points of \(z^d+c\). Morton (1998,
   Theorem D/Theorem 10) proves the all-degree product decomposition for
   \(f^b(z)-z\); its exact-period-\(n\) factor is \(C_n\wr S_r\).
   Fakhruddin (2014, Theorem 3.2) gives the same statement over any
   characteristic-zero constant field, which supplies the geometric version.
   Gao (2016, p. 39) is a later independent cross-check, not the primary
   proof.
3. **Formal-period warning:** dynatomic points can specialize to smaller
   actual period at root-of-unity multiplier parameters; Hutz and the
   dynatomic-curve literature supply this boundary.
4. **Direct scalar generator overlap:** Morton (1996), Corollary 1,
   Corollary 3, and pp. 335--336 identify the scalar orbit-shift fixed field
   as generated by the multiplier \(w=\rho|_{a=0}\) for all \(d,n\), and by
   the orbit sum \(t=\tau|_{a=0}\) for \(d=2\). This is an alternate input to
   parts of Step 13 and a mandatory novelty collision, not a new proof claim.

All other steps are proved in this package using standard commutative
algebra, with exact Stacks Project tags recorded in
CITATION_VERIFICATION.md.

The Cantat--Dujardin formal-period trace-spectrum rigidity theorem, the
Endler--Gallas period-four/period-six Hénon carriers, and Zhang's bounded
cyclic-polynomial calculations are collision or adjacency sources, not proof
inputs. They exclude any claim that this package invents trace-spectrum
parameter reconstruction, orbit-sum carriers, low-period stability carriers,
or cyclic-polynomial elimination.

## Corrections and missing-assumption audit

- **Actual versus formal:** repaired by defining \(E_n\) only in the generic
  étale algebra.
- **Normalization versus base change:** repaired by Steps 3 and 6–7.
- **Nilpotents in the scalar fiber:** repaired by the \(e=1\), \(R_0+S_1\)
  argument and the redundant flat-rank check.
- **Geometric versus arithmetic connectedness:** repaired by the constant
  field argument in Step 8.
- **Invariants versus tensor product:** repaired by the Reynolds idempotent
  in Step 9.
- **Monodromy direction:** repaired by the explicit
  \(\pi_1(U_0)\to\pi_1(U)\) inclusion in Step 10.
- **Derivative trace versus field trace:** repaired by the matrix definition
  in Steps 11–12.
- **Non-base versus primitive:** repaired by separating Steps 13 and 14.
- **Basis dependence:** repaired by the determinant line in Step 15.
- **Degree-one exception:** isolated in Step 16.

## Open risks for independent review

The author proof has no known internal algebraic blocker. The independent
Round-2 reviewer must nevertheless check:

1. the application of Morton (1998), Theorem D/Theorem 10, and Fakhruddin
   (2014), Theorem 3.2, to the exact-period factor and geometric constant
   field;
2. Morton (1996), Corollaries 1 and 3 and pp. 335--336, including
   \(w=\rho|_{a=0}\), \(t=\tau|_{a=0}\) in degree two, and the direct scalar
   fixed-field-generation novelty collision;
3. Cantat--Dujardin (2026), Section 3.2 and Theorems A/3.7, including the
   formal-period trace multiset and finite-period parameter-reconstruction
   boundary;
4. the identification of the lifted Henselian idempotent with the generic
   actual-period block;
5. the descent from the Henselian unique prime to
   \(\operatorname{div}_S(a)=P\);
6. the \(R_0+S_1\) nilpotent exclusion;
7. both primitive-word comparisons, including primitivity of the binary
   two-adjacent-minus word;
8. the claim that \((2,2)\) is the only \(r=1\) case;
9. every hash and lifecycle restriction in source_lock.json, including the
   immutable Round-1 review and the corrected planner hashes.

A failure of item 1 blocks the monodromy and PC2 primitivity claims; it may
not be papered over by irreducibility alone.
