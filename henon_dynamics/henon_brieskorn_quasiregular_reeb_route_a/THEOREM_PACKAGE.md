# Theorem package

## 1. Frozen model and normalization

Let (p,q) be odd coprime integers with (3\le p<q), write
(a=(a_0,a_1,a_2)=(2,p,q)), and set

\[
 f(z)=z_0^2+z_1^p+z_2^q,
 \qquad
 \Sigma_{p,q}=f^{-1}(0)\cap S^5.
\]

The origin is the only critical point of (f), so the link is a smooth closed
three-manifold. Freeze

\[
 \alpha=\frac{i}{4\pi}\sum_{j=0}^{2}a_j
 (z_jd\bar z_j-\bar z_jdz_j).
\]

The positive weighted ambient symplectic form (d\alpha), restricted by the
standard contact-type construction, makes (alpha|_{\Sigma_{p,q}}) a contact
form. Define

\[
 R=2\pi i\sum_{j=0}^{2}\frac1{a_j}
 \left(z_j\frac{\partial}{\partial z_j}
 -\bar z_j\frac{\partial}{\partial\bar z_j}\right).
\]

For each coordinate, its contribution to (alpha(R)) is (|z_j|^2), hence
(alpha(R)=1) on (S^5). In ambient notation

\[
 \iota_Rd\alpha=-d\|z\|^2,
 \qquad df(R)=2\pi i f.
\]

Thus (R) is tangent to the link and annihilates (d\alpha) on its tangent
space. It is the Reeb field, with flow

\[
 \Phi_t(z_0,z_1,z_2)=
 (e^{\pi it}z_0,e^{2\pi it/p}z_1,e^{2\pi it/q}z_2).
\]

## 2. Complete orbit and fixed-time theorem

### Theorem 1

Every point of (Sigma_{p,q}) has at least two nonzero coordinates. There are
exactly four orbit types:

| support | locus | primitive period | isotropy in the common circle |
|---|---|---:|---:|
| ({0,1}) | (z_2=0) | (2p) | (q) |
| ({0,2}) | (z_1=0) | (2q) | (p) |
| ({1,2}) | (z_0=0) | (pq) | (2) |
| ({0,1,2}) | principal stratum | (2pq) | (1) |

Each two-coordinate locus is one embedded circle and therefore one exceptional
simple Reeb orbit. The principal locus has a two-dimensional orbit quotient.

For arbitrary real (T), define

\[
 J_T=\{j\in\{0,1,2\}:T/a_j\in\mathbb Z\}.
\]

Then

\[
 \operatorname{Fix}(\Phi_T)=
 \begin{cases}
 \varnothing,&|J_T|<2,\\
 \Sigma_{p,q}\cap\{z_k=0:k\notin J_T\},&|J_T|\ge2.
 \end{cases}
\]

If (|J_T|=2), the fixed set is the corresponding exceptional circle; if
(|J_T|=3), it is the entire link. Every nonempty fixed component is
Morse--Bott, with dimension one or three respectively.

### Proof

A one-coordinate point cannot satisfy (f=0) on the unit sphere. A point is
fixed exactly when every nonzero coordinate has phase one, proving the support
criterion. On a two-coordinate locus with coprime exponents (a_i,a_j), the
moduli are the unique positive solution of
(r^{a_i}=s^{a_j}), (r^2+s^2=1). The phase equation cuts out a connected
one-dimensional subtorus because (gcd(a_i,a_j)=1); hence the locus is one
circle. The primitive period is the lcm of the active weights, giving the table.

At an exceptional circle, the missing-coordinate variation is tangent to both
(f^{-1}(0)) and the sphere to first order, and it spans the two-real-dimensional
contact normal. At a time fixing precisely the two active coordinates,
(d\Phi_T) is the identity on the orbit tangent and a nontrivial rotation on
this missing-coordinate line. Therefore
(ker(d\Phi_T-I)) equals the tangent of the circle. At a common-period return,
(d\Phi_T=I) on the whole link. This is exactly the Morse--Bott kernel condition.

For integer times (1\le T\le2pq), the class counts for one pair are

\[
 \begin{array}{c|ccccc}
 \text{class}&\varnothing&01&02&12&\Sigma_{p,q}\\ \hline
 \text{count}&2pq-p-q&q-1&p-1&1&1.
 \end{array}
\]

These sum to (2pq).

## 3. Transverse return and exceptional indices

Use the ambient missing-coordinate complex-line trivialization along each
exceptional orbit. The linearized return is multiplication by
(e^{2\pi i\rho}), where

\[
 \rho_{01}=\frac{2p}{q},\qquad
 \rho_{02}=\frac{2q}{p},\qquad
 \rho_{12}=\frac{pq}{2}.
\]

Consequently

\[
 \det_{\mathbb R}(I-P)=4\sin^2(\pi\rho),
\]

giving, in order,
(4\sin^2(2\pi p/q)), (4\sin^2(2\pi q/p)), and (4).
Because the displayed fractions are reduced, the first degenerate covers are
(q,p,2). Each first degeneracy occurs at total time (2pq), exactly the
principal return.

For (1\le r<\operatorname{den}(\rho)), the rotation is nondegenerate and the
declared trivialization gives

\[
 \mu_{\mathrm{CZ}}(\gamma^r)=2\lfloor r\rho\rfloor+1.
\]

No CZ value is assigned by this formula at the degenerate cover.

## 4. Seifert quotient and principal RS index

### Theorem 2

The orbit space of the common-period circle action is the Seifert orbifold

\[
 S^2(2,p,q),
\]

and

\[
 \chi_{\mathrm{orb}}
 =2-\left(1-\frac12\right)
    -\left(1-\frac1p\right)
    -\left(1-\frac1q\right)
 =\frac12+\frac1p+\frac1q-1.
\]

In the standard Milnor-fiber capping trivialization, the principal family at
(d=2pq) has Robbin--Salamon index

\[
 \mu_{\mathrm{RS}}
 =2d\left(\frac12+\frac1p+\frac1q-1\right)
 =-2pq+4p+4q.
\]

Both (chi_{\mathrm{orb}}) and (mu_{\mathrm{RS}}) are positive precisely
for ((p,q)=(3,5)), negative for every other allowed pair, and never zero.

### Index normalization and derivation

This is the standard Brieskorn principal-orbit formula, not a fit to the finite
table. In the ambient complex trivialization, the diagonal path over time
([0,d]) contributes

\[
 2d\left(\frac12+\frac1p+\frac1q\right).
\]

Passing to the contact distribution through the hypersurface/Milnor-fiber
capping trivialization removes a complex two-plane normal block.  In the
standard Brieskorn calculation (Kwon--van Koert, Section 5.3, formula (14)
and Proposition 5.9), this block splits into the defining-polynomial line and
a radial/Reeb line.  Since (df(R)=2\pi i f), the first winds (d) times and
contributes (2d), while the second is stationary in that trivialization and
contributes zero.  The Milnor-fiber complex volume trivializes the relevant
determinant line, so the stated capping convention is well defined.
Subtracting the normal-block contribution yields

\[
 2d\left(\sum_j\frac1{a_j}-1\right).
\]

This is the convention used in the cited Brieskorn index literature. It also
equals (2d\chi_{\mathrm{orb}}), independently confirming the stated formula.

For the sign, if (p\ge5), then (q\ge7) and
(1/p+1/q\le1/5+1/7<1/2). If (p=3), positivity requires (q<6), leaving
only (q=5); equality would require the excluded value (q=6).

## 5. Evidence, assumptions, and limits

The finite grid contains 1,003 allowed pairs through (q=101), 5,469,178
integer-time cells, 4,012 orbit-type rows, 3,009 rotation rows, 103,749
nondegenerate CZ cells, and 1,003 invariant rows. The independent checker
reconstructs them all. SymPy separately verifies the normalization,
determinant, lcm/denominator, count, and index identities. This finite work is
only regression evidence; Theorems 1 and 2 are analytic and have no upper
bound on (q).

The package does not compute contact homology. It does not replace the
principal Morse--Bott continuum by an isolated orbit ledger. Integer weights,
periods, and indices provide only a weak arithmetic relation. It constructs no
target arithmetic local data, Euler factor, root number, automorphy statement,
target divisor, target functional equation, target-zero match, or
Hilbert--Pólya operator. Route B is locked.

Route-A result:

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
overall: ROUTE_A_EXPLORATORY
scope: NO_BAD_EULER_OR_ROOT_NUMBER
```

## 6. Sources

- M. Kwon and O. van Koert, *Brieskorn manifolds in contact topology*,
  Bulletin of the London Mathematical Society 48 (2016),
  DOI `10.1112/blms/bdv088`.
- O. van Koert, *Contact homology of Brieskorn manifolds*, Forum Mathematicum
  20 (2008), DOI `10.1515/FORUM.2008.016`.

These sources own the standard Brieskorn contact and index background. This
package claims no literature priority; its contribution is the fully frozen
(Sigma(2,p,q)) theorem, boundary atlas, exact receipt, and Route-A audit.
