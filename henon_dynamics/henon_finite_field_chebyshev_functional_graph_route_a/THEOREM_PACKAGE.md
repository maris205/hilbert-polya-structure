# Theorem package

## 1. Frozen definitions

Let `q=p^r` be a prime power.  Define the non-normalized Chebyshev/Dickson first-kind polynomials by

\[
T_0(X)=2,\qquad T_1(X)=X,\qquad T_d(X)=XT_{d-1}(X)-T_{d-2}(X).
\]

They satisfy `T_d(z+z^{-1})=z^d+z^{-d}` in every characteristic.  In `F_{q^2}^*` put

\[
G_-:=\mathbb F_q^*,\qquad G_+:=\{z:z^{q+1}=1\},\qquad
\eta(z):=z+z^{-1}.
\]

Thus `|G_-|=q-1`, `|G_+|=q+1`, and `G_-∩G_+` has order `e=gcd(2,q-1)`.

For positive integers `u|q-1`, `v|q+1`, define the glued inversion-quotient count

\[
\mathcal Q_q(u,v)=\frac{u+\gcd(2,u)}2+\frac{v+\gcd(2,v)}2
-1-\mathbf1_{\{q\text{ odd},\ 2\mid u,\ 2\mid v\}}. \tag{1}
\]

The last two terms subtract the common `+1` branch and, when present on both sides, the common `-1` branch.

## 2. Exact graph theorem

**Theorem.** For every prime power `q` and integer `d>=1`, take disjoint copies of the functional graphs of `z↦z^d` on `G_-` and `G_+`.  In each copy identify `z~z^{-1}`.  Then identify the two images of every point of `G_-∩G_+`.  The induced map on the resulting quotient is conjugate through `eta` to `T_d:F_q→F_q`.

Consequently this quotient is the complete labeled functional graph, including all regular in-trees and the exceptional folded trees at the one characteristic-two branch or the two odd-characteristic branches.

**Proof.** For `x∈F_q`, the roots of `Z^2-xZ+1` are inverse to one another.  If a root lies in `F_q`, both lie in `G_-`; otherwise Frobenius exchanges them, so `z^q=z^{-1}` and both lie in `G_+`.  Hence `eta:G_-∪G_+→F_q` is onto and its fibers are exactly inversion fibers, except that the two cover copies of the intersection must be glued.  The defining identity gives `eta(z^d)=T_d(eta(z))`, so the bijection intertwines the maps and every directed edge. ∎

## 3. Periodic and fixed ledgers

Write

\[
q-1=a_-b_-,\qquad q+1=a_+b_+,
\]

where `(a_\pm,d)=1` and every prime of `b_\pm` divides `d`.  The periodic population is

\[
P=\mathcal Q_q(a_-,a_+). \tag{2}
\]

For `D=d^n` and `N∈{q-1,q+1}`, set

\[
s_N(D)=\gcd(D-1,N)+\gcd(D+1,N)-\gcd(D-1,D+1,N),
\]

\[
i_N(D)=1+\mathbf1_{\{2\mid N,\ D\text{ odd}\}}.
\]

The first number counts the union of `z^D=z` and `z^D=z^{-1}` on the cyclic cover; the second counts its inversion-fixed elements.  Therefore

\[
F_n:=|\operatorname{Fix}(T_d^n)|=
\frac{s_{q-1}(D)+i_{q-1}(D)}2+
\frac{s_{q+1}(D)+i_{q+1}(D)}2-
1-\mathbf1_{\{q\text{ odd},\ D\text{ odd}\}}. \tag{3}
\]

Möbius inversion gives exact-period points and cycles,

\[
E_m=\sum_{e\mid m}\mu(m/e)F_e,\qquad C_m=E_m/m, \tag{4}
\]

and hence the finite source zeta

\[
\zeta_{T_d}(t)=\exp\!\left(\sum_{n\ge1}F_n\frac{t^n}{n}\right)
=\prod_{m\ge1}(1-t^m)^{-C_m}. \tag{5}
\]

## 4. Complete tree, tail and image data

On a cover `C_{a_\sigma}×C_{b_\sigma}`, the first factor is periodic and the second is killed by a power of `d`.  This proves (2) and, together with the graph theorem, describes every local tree before and after inversion folding and branch gluing.

The number of field points with tail at most `j` is

\[
H_j=\mathcal Q_q\!\left(a_-\gcd(d^j,b_-),
a_+\gcd(d^j,b_+)\right). \tag{6}
\]

Thus exact tail zero has size `H_0=P`, exact tail `j>=1` has size `H_j-H_{j-1}`, and the height is the least `h` for which both `b_-|d^h` and `b_+|d^h`.

The `j`th image has cover subgroup orders

\[
m_\pm(j)=\frac{q\pm1}{\gcd(d^j,q\pm1)},
\]

so its exact size is

\[
R_j=|\operatorname{im}T_d^j|=\mathcal Q_q(m_-(j),m_+(j)). \tag{7}
\]

These ranks stabilize at `P`.

## 5. Full-function Koopman Jordan atlas

Let `U:C^{F_q}→C^{F_q}` be `(Uf)(x)=f(T_d(x))`.  Distinct rows of `U^j` are indexed by distinct image values, so `rank(U^j)=R_j`.  The number of zero Jordan blocks of exact size `j` is therefore

\[
Z_j=R_{j-1}-2R_j+R_{j+1}. \tag{8}
\]

The recurrent quotient is the permutation on the cycles counted by (4).  Hence

\[
\det(\lambda I-U)=\lambda^{q-P}\prod_{m\ge1}(\lambda^m-1)^{C_m}. \tag{9}
\]

For `d=1` this is the identity map.  The separate degree-zero polynomial `T_0=2` is constant (zero in characteristic two): one fixed point, `q-1` exact-tail-one points, zeta `(1-t)^{-1}`, ranks `(q,1,1,...)`, and a diagonalizable composition operator with eigenvalues `1,0^{q-1}`.

## 6. Proof and claim boundary

Equations (2), (6) and (7) follow because periodicity, killed `d`-primary components and images are subgroup conditions on each cyclic cover, after which (1) performs the exact inversion quotient and branch gluing.  Equation (3) is Burnside on the union of the two signed kernels, followed by the same branch correction.  Equations (4), (5), (8) and (9) are finite cycle and Jordan identities.

This proves the theorem for every prime power, including characteristic two; there is no weakening to prime fields or odd characteristic.  The finite composition matrix is canonical but generally nonnormal, with no self-adjoint realization, so the evaluator grade is only `A4_FORMAL_HINT` and the overall verdict remains `ROUTE_A_EXPLORATORY`.  It gives finite source dynamics only.  It does not provide arithmetic local data, bad Euler factors, root numbers, automorphy, a target divisor or functional equation, or a Hilbert–Pólya operator.
