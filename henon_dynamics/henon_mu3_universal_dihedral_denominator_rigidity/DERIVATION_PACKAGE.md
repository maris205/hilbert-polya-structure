# HCS-C54 derivation package

## D1. Why an ideal stabilizer preserves both equation lines

The degree-two piece of the homogeneous ideal \((C_n,Q_{n,\rho})\) is
the line \(KQ_{n,\rho}\).  Hence a projective monomial ideal stabilizer
scales the quadric.  In degree three it satisfies

\[
g^*C_n=aC_n+LQ_{n,\rho}
\]

for a scalar \(a\) and a linear form \(L\).  The monomial pullback
\(g^*C_n\) and \(aC_n\) are sums of pure cubes.  Since
\(Q_{n,\rho}\) is squarefree on every edge, \(LQ_{n,\rho}\) has no
pure-cube monomial.  Comparing the coefficient of every \(x_i^3\) gives

\[
g^*C_n=aC_n.
\]

The remaining equality is \(LQ_{n,\rho}=0\).  The polynomial ring is a
domain and \(Q_{n,\rho}\ne0\), so \(L=0\).  This is the step that turns
an ideal stabilizer into a simultaneous equation-line stabilizer.

If a monomial lift has diagonal coefficients \(\lambda_i\), the cubic
identity says \(\lambda_i^3=a\) for every \(i\).  Projectively divide by
\(\lambda_0\).  The normalized coefficients are cube roots of unity, so
the candidate has the form

\[
x_i\longmapsto\rho^{e_i}x_{\sigma(i)},
\qquad e_i\in\mathbf F_3,\qquad e_0=0.
\]

## D2. Edge recurrence and the closure parity

Let \(E_j=\{j,j+1\}\), with indices modulo \(N=2n\), and encode the
quadric coefficient on \(E_j\) by

\[
c_j=\begin{cases}1,&j=N-1,\\0,&0\le j<N-1.
\end{cases}
\]

The quadric support is the \(N\)-cycle, hence \(\sigma\) is a dihedral
permutation.  Write \(g^*Q_{n,\rho}=\beta Q_{n,\rho}\).  On any edge,
the normalized transformed coefficient and the corresponding coefficient of
\(Q_{n,\rho}\) both belong to \(\mu_3\).  Their ratio is \(\beta\), so
\(\beta\in\mu_3\).  Thus \(\beta=\rho^q\) for a unique
\(q\in\mathbf F_3\).  This derives the phase parameter rather than assuming
it.
Comparison at the image of \(E_j\) gives

\[
c_j+e_j+e_{j+1}=q+c_{\sigma(E_j)}\pmod3,
\]

or equivalently

\[
e_{j+1}=q+c_{\sigma(E_j)}-c_j-e_j\pmod3. \tag{D.1}
\]

For fixed support, \(q\), and \(e_0=0\), this recurrence determines all
phases.  Iterating once around the cycle gives

\[
e_N-e_0
=\sum_{j=0}^{N-1}(-1)^{N-1-j}
\bigl(q+c_{\sigma(E_j)}-c_j\bigr).
\]

The alternating sum of the \(q\)-terms vanishes because \(N\) is even.
Let \(j_*\) be the unique edge index with
\(\sigma(E_{j_*})=E_{N-1}\).  The remaining sum is

\[
(-1)^{N-1-j_*}-1.
\]

It vanishes exactly when \(j_*\) is odd.

For a rotation \(\sigma(i)=i+k\), one has
\(j_*=N-1-k\), so \(j_*\) is odd exactly when \(k\) is even.  For a
reflection \(\sigma(i)=k-i\), one has \(j_*=k\), so exactly the odd
reflections survive.  The support count is therefore

\[
n\text{ rotations}+n\text{ reflections}=2n.
\]

For each support, all three values \(q\in\mathbf F_3\) close and give one
normalized phase solution.  Thus the exhaustive count is \(6n\).

## D3. Uniform generators and the dihedral presentation

Let

\[
(rx)_i=\rho^{a_i}x_{i+2},
\qquad a_{N-2}=1,\quad a_{N-1}=2,\quad a_i=0\text{ otherwise},
\]

and

\[
(sx)_i=\rho^{b_i}x_{1-i},
\qquad b_i=1\iff i=1\text{ or }(i\ge2\text{ even}).
\]

The phases cube to one, so both maps preserve \(C_n\).  Edge-by-edge
substitution gives

\[
Q_{n,\rho}(rx)=Q_{n,\rho}(x),
\qquad
Q_{n,\rho}(sx)=\rho Q_{n,\rho}(x).
\]

The support of \(r\) has order \(n\), and phase accumulation gives

\[
r^n=\operatorname{diag}(1,\rho,1,\rho,\ldots,1,\rho)
\]

in \(\operatorname{PGL}_N\).  The displayed diagonal element has order
three, so \(r\) has exact order \(3n\).  Direct phase and support
composition gives

\[
s^2=1,\qquad srs=r^{-1}.
\]

Every element of \(\langle r\rangle\) has rotation support, whereas \(s\)
has reflection support.  Hence \(s\notin\langle r\rangle\).  Since \(r\)
has order \(3n\), the \(6n\) elements
\[
r^k,\quad r^ks,\qquad 0\le k<3n,
\]
are distinct.  They lie in the exhaustive \(6n\)-element list, so the
generated subgroup is the full stabilizer and the presentation is an
isomorphism.

The support kernel consists of

\[
1,\quad r^n,\quad r^{2n},
\]

and is \(C_3\).  The support image has order \(2n\), with the even
rotations and odd reflections of the \(2n\)-cycle, hence is
\(\operatorname{Dih}(C_n)\).

## D4. Semilinear transport and rational points

Let \(\tau(\rho)=\rho^2\) and

\[
(M_nx)_i=\rho^{\eta_i}x_{-i},
\qquad
\eta_i=1\iff i\ne0\text{ is even}.
\]

The HCS-C53 identities

\[
C_n(M_nx)=C_n(x),
\quad
Q_{n,\rho}(M_nx)=\rho Q_{n,\rho^2}(x),
\quad
M_n\tau(M_n)=I
\]

make \(M_n\) an effective quadratic descent datum.  Substitute the explicit
supports and phases of \(r,s\) into

\[
\delta(g)=M_n\tau(g)M_n^{-1}.
\]

After projective phase normalization one obtains

\[
\delta(r)=r^{-1},
\qquad
\delta(s)=rs=sr^{-1}.
\]

These assignments preserve the dihedral relations and square to the identity.
They therefore give effective descent data on the constant \(K\)-group and
its action.

For an arbitrary element,

\[
\delta(r^k)=r^{-k},
\qquad
\delta(r^ks)=r^{1-k}s.
\]

The fixed rotations solve \(2k=0\pmod{3n}\), while the fixed reflections
solve \(2k=1\pmod{3n}\).  If \(n\) is even, the first congruence has the
two solutions \(0,3n/2\), and the second has none.  If \(n\) is odd, the
first has only \(0\), while the second has the unique solution
\((3n+1)/2\).  Thus the rational group scheme has exactly two rational
geometric points in every row.

## D5. Reynolds averaging versus quadratic transfer

On a smooth row, the average

\[
e_{G_n}=\frac1{6n}\sum_{g\in G_n}\Gamma_g
\]

uses all \(6n\) graphs.  Transport permutes those graphs, hence
\(\tau(e_{G_n})=e_{G_n}\).  For the quadratic base-change map \(q\), set

\[
e_{\mathscr G_n}=\frac12q_*e_{G_n}.
\]

Then

\[
q^*e_{\mathscr G_n}
=\frac12(e_{G_n}+\tau e_{G_n})=e_{G_n}.
\]

The coefficient \(1/(6n)\) is group averaging.  The coefficient \(1/2\)
is field transfer.  Neither formula asserts that every graph descends
individually, and neither supplies a Chow object before smoothness and the
relevant motive have been constructed.

## D6. From split traces to a Grothendieck-group identity

Assume \(n\) is packet-admissible and let \(\mathsf V_n\) satisfy the
split trace identity.  Fix a coefficient prime \(\ell\), multiply the trace
relation by \(n\), restrict the three \(\ell\)-adic realizations to
\(G_K\), and take semisimplifications.  This preserves traces,
characteristic polynomials, ranks, and purity; it does not promote HCS-C53 to
a semisimplicity theorem.  Outside a finite set, degree-one primes of \(K\)
lie above split rational primes, and their Frobenius classes are dense.
Chebotarev and Brauer--Nesbitt applied to the semisimplifications

\[
(\operatorname{Res}V_{n,\ell}^{\mathrm{ss}})^{\oplus n}
\quad\text{and}\quad
(\operatorname{Res}E_{n,\ell}^{\mathrm{ss}})^{\oplus4}
\oplus(\operatorname{Res}O_{n,\ell}^{\mathrm{ss}})^{\oplus4}
\]

give

\[
n[\operatorname{Res}V_{n,\ell}^{\mathrm{ss}}]
=4[\operatorname{Res}E_{n,\ell}^{\mathrm{ss}}]
+4[\operatorname{Res}O_{n,\ell}^{\mathrm{ss}}]. \tag{D.2}
\]

The semisimple Grothendieck group is free on irreducible classes.  Since a
pure weight-zero constituent cannot equal a pure weight-one constituent,
the right side has disjoint rails.  Equality (D.2) therefore forces every
multiplicity on each rail to be divisible by \(n\).  In particular,

\[
n\mid4e_n,\qquad n\mid4o_n.
\]

Using \(o_n=2(e_n-3)\), the two divisibilities give

\[
n\mid8e_n,\qquad n\mid8(e_n-3),
\]

and subtraction gives \(n\mid24\).  Checking the seven divisors
\(2,3,4,6,8,12,24\) leaves exactly \(2,4\).

If \(n\mid4\), the direct-copy system

\[
\mathsf E_n^{\oplus4/n}\oplus\mathsf O_n^{\oplus4/n}
\]

matches every power trace.  Since

\[
\operatorname{Log}_0L_p(\mathsf V,u)
=\sum_{m\ge1}\frac{\operatorname{Tr}(F_p^m\mid\mathsf V)}m u^m,
\]

it realizes the complete split-local factor, not only the leading trace.

## D7. Exact \(n=3\) Cayley character

For \(n=3\), the Cayley bidegree \((1,-1)\) has the 27 ambient
monomials

\[
zx_i\quad(0\le i<6),
\qquad
yx_ix_j\quad(0\le i\le j<6).
\]

The seven exact relations are the six equations

\[
\frac{\partial}{\partial x_i}
\bigl(yC_3+zQ_{3,\rho}\bigr)
=3yx_i^2+z\frac{\partial Q_{3,\rho}}{\partial x_i}
\]

and the equation \(yQ_{3,\rho}=0\).  Exact row reduction over
\(\mathbf Q(\rho)\) gives relation rank seven and quotient dimension 20.

If a group element has coordinate matrix \(M_g\) and equation-space matrix
\(A_g\), the residue action on the quotient is polynomial pullback multiplied
by

\[
\frac{\det M_g}{\det A_g}.
\]

Omitting this ratio changes the character.  Exact quotient matrices give

\[
\operatorname{Tr}(r^k\mid H^{2,1})
=(20,-1,-1,2,-1,-1,2,-1,-1)
\]

and reflection trace \(-2\).  Character inner products then give

\[
H^{2,1}=2\varepsilon+2U_1+2U_2+3U_3+2U_4.
\]

The character is real, so adding its conjugate doubles the multiplicities
and yields the odd rail.

For the Fermat rail, the primitive Jacobian ring is

\[
K[x_0,\ldots,x_5]/(x_0^2,\ldots,x_5^2).
\]

The relevant squarefree degrees are \(0,3,6\), the residue factor is
\(\det M_g\), and the packet includes one extra trivial line.  Exact
fixed-monomial traces give

\[
\operatorname{Tr}(r^k\mid\mathsf E_3)
=(23,2,2,-4,2,2,-4,2,2)
\]

and reflection trace \(-1\).  Character inner products give

\[
\mathsf E_3=\mathbf1+2\varepsilon+3U_1+3U_2+U_3+3U_4.
\]

The paired multiplicity ledger has no nonzero sector divisible by three on
both rails.  The orbit block \(U_1\oplus U_2\oplus U_4\) retains the pair
\((3,4)\), so coefficient descent does not change the conclusion.

## D8. Counterpacket and inert-prime boundaries

Fix \(\ell\), a finite coefficient extension \(E_\ell/\mathbf Q_\ell\),
and a common finite set \(S\) containing \(\ell\), ramification, and every
bad prime in scope.  Here the semisimple Grothendieck group is generated by
the finite-dimensional continuous semisimple \(E_\ell\)-representations
arising from the fixed-\(\ell\) compatible-system realizations and their
semisimple subquotients, all unramified outside \(S\); it is not a category
of arbitrary \(G_{\mathbf Q}\)-representations.

Let \(D\) be a virtual class in that category whose trace vanishes at all
but a relative-Dirichlet-density-zero subset of the good rational primes
split in \(K\).  The degree-one prime ideals of \(K\) form a
Dirichlet-density-one set; the exceptional rational primes lift to a
density-zero subset.  After restriction to \(G_K\), Chebotarev and
Brauer--Nesbitt give

\[
\operatorname{Res}(D)=0.
\]

The restriction map on virtual classes is not injective.  If
\(\chi_{K/\mathbf Q}\) is the quadratic character, then

\[
\mathbf1-\chi_{K/\mathbf Q}
\]

is a nonzero element of its kernel.  More generally,
\(U-U\otimes\chi_{K/\mathbf Q}\) lies in the kernel and is nonzero provided
\(U\not\simeq U\otimes\chi_{K/\mathbf Q}\).  Every kernel class
nevertheless has rank zero after
restriction and cannot change a \(K\)-rail rank or source-isotypic
multiplicity.

At an inert prime, \(F_v=F_p^2\).  Thus

\[
P_{K,v}(U^2)
=\prod_i(1-\alpha_i^2U^2)
=P_p(U)P_p(-U),
\]

which is generally not a square.  This is the local algebraic firewall
against promoting the split classification to a global fractional root.
