# HCS-C20 derivation package

## 1. Frozen input

Work over (K=\mathbb Q(\sigma)), put

\[
a=\sigma^2-2\sigma,
\]

and let (P(\sigma,x)) be the adopted monic septic certified in HCS-C19.
Its smooth projective normalization (C) is geometrically integral of genus
three.  The exact inputs used here are:

1. the seven geometric roots of (P) carry one Galois-invariant simple
   seven-cycle;
2. an ordered edge ((x_i,x_{i-1})) advances by
   \(\tau(x,y)=(a-x^2-y,x)\);
3. the scalar deck involution is
   \(J(x,y)=(x,a-x^2-y)\), with
   \(J\tau J=\tau^{-1}\);
4. the scalar discriminant is
   \[
   \operatorname{Disc}_xP=(4\sigma-9)^2Q_6(\sigma)^3;
   \]
5. (Q_6) is squarefree and irreducible, and its six roots each support
   three scalar ramification points of index two;
6. the scalar normalization is unramified at the ordinary node
   \(\sigma=9/4\) and at all seven infinity branches.

No finite-prime or Riemann data enter the geometric proof.

## 2. Exact dihedral monodromy

Let (G_{\rm geom}) be the geometric monodromy of the degree-seven cover
(C\to\mathbb P^1_\sigma).  The neighbor relation is defined over (K), so
every element of (G_{\rm geom}) preserves the seven-cycle.  Hence

\[
G_{\rm geom}\leq\operatorname{Aut}(C_7)\cong D_7.
\]

Geometric integrality makes this action transitive.  A transitive subgroup of
(D_7) is either its rotation subgroup (C_7) or all of (D_7).  The
discriminant square class is

\[
[\operatorname{Disc}_xP]=[Q_6]
\quad\text{in}\quad
\overline{\mathbb Q}(\sigma)^\times/
\overline{\mathbb Q}(\sigma)^{\times2}.
\]

It is nontrivial because (Q_6) has six simple zeros.  Thus geometric
monodromy contains an odd permutation.  Every seven-cycle is even, so the
rotation subgroup lies in (A_7).  Therefore

\[
\boxed{G_{\rm geom}=D_7.}
\]

The formulas for \(\tau\) and (J) are rational over (K).  Starting from an
ordered adjacent pair, the recurrence reconstructs every coordinate in the
cycle.  The ordered-edge field is therefore the full splitting field (L) of
(P).  It has degree 14 over (K), with 14 explicit deck transformations,
so the arithmetic group is also (D_7).

## 3. Branch locus and genus of the splitting curve

Let (E) be the smooth projective curve with function field (L).  The six
roots of (Q_6) have scalar inertia cycle type (2^3 1), hence reflection
inertia in (D_7).  The scalar cover is unramified after normalization at
\(\sigma=9/4\) and infinity.  Faithfulness of the seven-vertex action implies
that the Galois closure cannot acquire inertia where every scalar sheet was
unramified.  Thus the six (Q_6)-roots are the complete branch locus of
\(E\to\mathbb P^1_\sigma\).

Above each branch value a regular (D_7)-cover has (14/2=7) points, each of
ramification index two.  Riemann--Hurwitz gives

\[
2g(E)-2=14(-2)+6\cdot7=14,
\qquad
\boxed{g(E)=8}.
\]

## 4. Quadratic extension over the scalar quotient

The marked-coordinate field is

\[
M=K(C)=L^{\langle J\rangle}.
\]

Rotations are even and reflections odd in the seven-vertex action.  The
unique sign quadratic subfield of the splitting field is therefore

\[
L^{\langle\tau\rangle}
=K(\sqrt{\operatorname{Disc}_xP})
=K(\sqrt{Q_6}).
\]

Since \(\langle J\rangle\cap\langle\tau\rangle=1\), compositum degrees give

\[
\boxed{L=M(\sqrt{Q_6(\sigma)}).}
\]

This also proves directly that the two-neighbor quadratic does not split over
(M).  A norm parity check is useful: if (Q_6=g^2) in (M), then
\(Q_6^7=N_{M/K}(g)^2\), impossible at any simple zero of (Q_6).

At a root \(\alpha\) of (Q_6), the scalar fiber consists of three points
with (v(\sigma-\alpha)=2) and one point with valuation one.  Thus
\(v(Q_6)=2,2,2,1\); exactly the last point ramifies in (E\to C).  Its
coordinate modulo (Q_6) is

\[
u(\sigma)=-\frac{
160\sigma^5-760\sigma^4+412\sigma^3+1120\sigma^2
-111\sigma+166}{4}.
\]

Exact reduction gives

\[
P(\sigma,u)\equiv0\pmod{Q_6}
\]

and

\[
P_x(\sigma,u)\equiv
2(8\sigma^4-36\sigma^3+16\sigma^2+39\sigma+37)
\pmod{Q_6}.
\]

The resultant of the last quartic with (Q_6), including the displayed
factor 2, is (2^{42}\), so this root is simple.

At the finite node,

\[
Q_6(9/4)=-7/64,
\]

so neither normalization branch ramifies in the quadratic extension.  At
infinity, (t=1/\sigma) is a uniformizer on every scalar branch and

\[
Q_6=t^{-6}(64-448t+848t^2+\cdots),
\]

which has even valuation and square leading unit.  Hence the complete branch
divisor of (E\to C) is the single closed degree-six divisor

\[
\mathcal B_J=
\sum_{Q_6(\alpha)=0}[(\alpha,u(\alpha))].
\]

The quadratic Riemann--Hurwitz check is

\[
2g(E)-2=2(2g(C)-2)+6=14.
\]

## 5. The genus-two sign quotient

Put

\[
B=E/\langle\tau\rangle.
\]

The preceding sign-subfield calculation gives the explicit model

\[
\boxed{B:\quad w^2=Q_6(\sigma).}
\]

Because (Q_6) is squarefree of degree six, (g(B)=2).  Its leading
coefficient (64=8^2) gives two rational points at infinity.  Every inertia
group of (E\to\mathbb P^1\) is a reflection and has trivial intersection
with \(\langle\tau\rangle\).  Consequently

\[
\boxed{E\to B\text{ is an unramified cyclic cover of degree }7.}
\]

The genus check becomes

\[
2g(E)-2=7(2g(B)-2)=14.
\]

## 6. Jacobian decomposition

For (G=D_7), (H=\langle J\rangle), and (N=\langle\tau\rangle\), the
rational permutation characters satisfy

\[
\mathbb Q[G/1]\oplus2\mathbb Q[G/G]
\cong
\mathbb Q[G/N]\oplus2\mathbb Q[G/H].
\]

At the identity both sides have character 16; at a nonidentity rotation both
have character 2; and at a reflection both have character 2.  The associated
idempotent relation yields

\[
\operatorname{Jac}(E)\times\operatorname{Jac}(E/G)^2
\sim_{\mathbb Q}
\operatorname{Jac}(E/N)\times\operatorname{Jac}(E/H)^2.
\]

Since (E/G=\mathbb P^1\), (E/N=B\), and (E/H=C\),

\[
\boxed{
\operatorname{Jac}(E)
\sim_{\mathbb Q}
\operatorname{Jac}(B)\times\operatorname{Jac}(C)^2.
}
\]

This is an isogeny statement.  A polarized product decomposition is not
claimed.

## 7. The Hénon Hecke correspondence and real multiplication

Let (q:E\to C\) and define the unnormalized push-pull operator

\[
A=q_*\tau^*q^*\in\operatorname{End}_{\mathbb Q}(\operatorname{Jac}(C)).
\]

On (V=H^1(E,\mathbb Q)), (q^*H^1(C)=V^H\) and
\(q^*q_*=1+J\).  For (v\in V^H\),

\[
q^*A(q^*)^{-1}v
=(1+J)\tau v
=(\tau+\tau^{-1})v.
\]

Put (X=\tau+\tau^{-1}\).  On every nontrivial rotation eigenspace,

\[
1+\tau+\cdots+\tau^6=0.
\]

Using
\(\tau^2+\tau^{-2}=X^2-2\) and
\(\tau^3+\tau^{-3}=X^3-3X\) gives

\[
X^3+X^2-2X-1=0.
\]

There is no rotation-fixed vector in (V^H\), because such a vector would be
(D_7)-invariant and (H^1(E/D_7)=H^1(\mathbb P^1)=0\).

To prove minimality, write the rational representation as

\[
H^1(E,\mathbb Q)\cong\varepsilon^4\oplus W^2,
\]

where \(\varepsilon\) is the reflection sign representation and (W) is the
six-dimensional rational irreducible whose complexification is the sum of the
three nontrivial two-dimensional dihedral representations.  On (W^H\), the
three distinct eigenvalues are

\[
\zeta_7^k+\zeta_7^{-k},\qquad k=1,2,3,
\]

each occurring twice on (H^1(C)).  Thus

\[
\chi_A(T)=(T^3+T^2-2T-1)^2,
\qquad
\mu_A(T)=T^3+T^2-2T-1.
\]

The transpose correspondence replaces \(\tau\) by \(\tau^{-1}\), which is
conjugate by (J) and hence acts identically after push-pull.  Therefore (A)
is Rosati self-adjoint.  Since the irreducible cubic has discriminant 49,

\[
\boxed{
\mathbb Q[A]\cong\mathbb Q(\zeta_7+\zeta_7^{-1})
\hookrightarrow\operatorname{End}_{\mathbb Q}^0(\operatorname{Jac}(C)).
}
\]

If the normalized idempotent (e_H=(1+J)/2\) is used instead, then
\(e_H\tau e_H=A/2\) on (H^1(C)) and its polynomial is
\(8T^3+4T^2-4T-1\).  Mixing these normalizations is an error.

## 8. Arithmetic factorization

Let

\[
F=\mathbb Q(\theta),\qquad
\theta^3+\theta^2-2\theta-1=0.
\]

At every prime of good reduction where the correspondence extends, the
Frobenius action commutes with (F\), (H^1(C)) has rank two over (F\), and

\[
L_{C,p}(T)=
\operatorname{Norm}_{F/\mathbb Q}(1-a_pT+pT^2)
\]

for an algebraic integer (a_p\in\mathcal O_F\).

For the three HCS-C19 branch-corrected rows, exact reduction in
\(\mathbb Z[\theta]\) gives

\[
\begin{array}{c|c}
p&a_p\\ \hline
5&-4+\theta+2\theta^2\\
11&-4+\theta^2\\
13&-2+\theta+\theta^2.
\end{array}
\]

These are exact norm identities.

For (B:w^2=Q_6\), good reduction is elementary at (p=5,11,13\), since
\(\operatorname{Disc}(Q_6)=2^{63}\cdot97\).  Direct counts over
\(\mathbb F_p\) and \(\mathbb F_{p^2}\) give

\[
\begin{array}{c|c|c}
p&(N_1,N_2)&L_{B,p}(T)\\ \hline
5&(8,30)&1+2T+4T^2+10T^3+25T^4\\
11&(14,120)&1+2T+T^2+22T^3+121T^4\\
13&(10,178)&1-4T+12T^2-52T^3+169T^4.
\end{array}
\]

The selected-prime theorem in
[SELECTED_PRIME_GOOD_REDUCTION.md](SELECTED_PRIME_GOOD_REDUCTION.md)
closes the normalization caveat at exactly \(p=5,11,13\).  Its proof has
four independent components:

1. a nontrivial vertical inertia group in the unramified \(C_7\)-cover
   \(E\to B\) would force \(\mu_7\) into the constant field \(\mathbb F_p\),
   contradicting \(p\not\equiv1\pmod7\);
2. purity extends the cover finite étale over the smooth model of \(B\), and
   the tame reflection quotient gives smooth proper models of \(E\) and
   \(C\);
3. monicity on the affine and infinity charts identifies the smooth quotient
   with the total-space normalization of the projective plane septic; and
4. irreducible specializations modulo each selected prime make the special
   comparison finite birational, while exact node and infinity screens prove
   the correction \(A_{p,r}+7+\epsilon_{p,r}\).

The resulting genuine scalar counts are

\[
\begin{array}{c|c}
p&(N_1,N_2,N_3)\\ \hline
5&(9,39,147)\\
11&(19,167,1171)\\
13&(16,242,2131).
\end{array}
\]

The Jacobian isogeny therefore implies

\[
\boxed{L_{E,p}=L_{B,p}L_{C,p}^2}
\]

as an identity of genuine Hasse--Weil local factors at all three displayed
primes.  No blanket good-reduction statement is made outside this set.

## 9. General fixed-period collapse

The same representation argument applies to any connected (D_\ell)-Galois
cover of \(\mathbb P^1\), for odd prime \(\ell\), with six reflection branch
values.  The rotation quotient has genus two, the Galois curve has genus
\(\ell+1\), and the reflection quotient has genus \((\ell-1)/2\).  Moreover,

\[
\operatorname{Jac}(E)\sim
\operatorname{Jac}(B)\times\operatorname{Jac}(C)^2,
\]

while the reflection quotient has real multiplication by
\(\mathbb Q(\zeta_\ell+\zeta_\ell^{-1})\).  Thus ordinary cohomology of the
oriented lift supplies no eigenvalues beyond the sign quotient and two scalar
copies.  Chronology is visible only in the equivariant decomposition.

This is a classical dihedral/Prym mechanism, here used as a scoped obstruction
to treating fixed-period orientation as a new ordinary zeta spectrum.

## 10. Route-A boundary

The exact output strengthens A1 and A4 evidence but does not change the
tuple:

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).
\]

The period label remains (n=7\), no cross-period primitive law or Fredholm
determinant exists, and the finite-dimensional Rosati-self-adjoint
correspondence is not a Hilbert--Pólya operator.
