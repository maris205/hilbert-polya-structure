# Proof Package

## Claim

Let $d\ge2$, put $r=d-1$, and fix arbitrary positive integers
$$
\mathbf n=(n_1,\ldots,n_r).
$$
For the extended generalized Hénon family
$$
H_{b,p}(x,y)=(p(x)+by,x),
\qquad
(b,p)\in\mathcal B_d:=\mathbf A^1_b\times\mathcal P_d^{\mathrm{cm}},
$$
consider $r$ labelled, pairwise-disjoint, simple cycles of exact respective periods $n_i$. On the unique irreducible marked component containing the polynomial boundary $b=0$, the map formed by the Jacobian parameter and the marked traces is dominant and generically étale. Its critical scheme restricts scheme-theoretically to the polynomial multiplier critical scheme at every simple scalar tuple.

The precise theorem is stated below after the incidence notation is fixed.

## Status

**PROVABLE AS STATED**

This status applies to the repaired and frozen theorem in this document. The earlier informal formulation required the corrections recorded under “Corrections already incorporated.”

## Assumptions

- The ground field is $\mathbf C$.
- The degree satisfies $d\ge2$.
- The polynomial is monic and centered:
  $$
  p(z)=z^d+\sum_{k=0}^{d-2}a_kz^k.
  $$
- Each $n_i$ is a positive integer; repetitions among the $n_i$ are allowed.
- Marked cycles are exact, pairwise disjoint, and simple.
- Scheme-theoretic ramification is asserted only on the simple scalar locus, where the marked incidence is étale over the parameter base.
- The arbitrary-period multiplier-independence and marked-polynomial irreducibility input is [Gorbovickis, Theorem 1.6, Definition/Remark 1.4, Lemma 1.5, and Lemma 2.1](https://arxiv.org/html/1305.0867).

## Notation

- $R_d=\mathbf C[b,a_0,\ldots,a_{d-2}]$ is the coordinate ring of $\mathcal B_d$.
- $H=H_{b,p}$ when the parameters are understood.
- For a point $z$ of exact period $n$, its cycle is $\{z,H(z),\ldots,H^{n-1}(z)\}$.
- A periodic point is **simple** when
  $$
  \det(D_zH^n-I)\ne0.
  $$
- $\widetilde{\mathcal X}_{\mathbf n}^{\circ}$ is the point-marked simple exact disjoint incidence. Its points are
  $$
  (b,p,z_1,\ldots,z_r)
  $$
  with $H^{n_i}(z_i)=z_i$ and the three open conditions above.
- The finite group
  $$
  G_{\mathbf n}=\prod_{i=1}^{r}\mathbf Z/n_i\mathbf Z
  $$
  moves each point marking around its exact cycle. Its action on $\widetilde{\mathcal X}_{\mathbf n}^{\circ}$ is free.
- The cycle-marked incidence is
  $$
  \mathcal X_{\mathbf n}^{\circ}
  =\widetilde{\mathcal X}_{\mathbf n}^{\circ}/G_{\mathbf n}.
  $$
- $\mathcal S_{\mathbf n}=(\mathcal X_{\mathbf n}^{\circ})_{b=0}$ is the scalar marked locus.
- $\mathcal C_{\mathbf n}$ is the unique irreducible component of $\mathcal X_{\mathbf n}^{\circ}$ containing $\mathcal S_{\mathbf n}$.
- The trace functions are
  $$
  \rho_i=\operatorname{tr}(D_{z_i}H^{n_i}).
  $$
  They are invariant under cyclic shifts, so they descend from the point-marked cover to the cycle-marked quotient.
- Put
  $$
  T=\mathbf A^1_t\times\mathbf A^r_{q_1,\ldots,q_r},
  \qquad
  \Psi=(-b,\rho_1,\ldots,\rho_r):\mathcal C_{\mathbf n}\to T.
  $$
- On $\mathcal S_{\mathbf n}$, $\lambda_i$ denotes the one-variable multiplier of the corresponding polynomial cycle, and
  $$
  \Lambda=(\lambda_1,\ldots,\lambda_r):\mathcal S_{\mathbf n}\to\mathbf A^r.
  $$

## Exact theorem

### Theorem A: marked trace coordinates and scalar-boundary ramification

For every $d\ge2$ and every $\mathbf n\in\mathbf Z_{>0}^{d-1}$, the following assertions hold.

1. **Marked scalar component.** The scalar cycle-marked locus $\mathcal S_{\mathbf n}$ is nonempty and irreducible. It is contained in a unique irreducible component $\mathcal C_{\mathbf n}$ of $\mathcal X_{\mathbf n}^{\circ}$. The natural map
   $$
   \pi:\mathcal C_{\mathbf n}\longrightarrow\mathcal B_d
   $$
   is étale and dominant. Moreover,
   $$
   (\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}
   $$
   scheme-theoretically inside the simple exact disjoint incidence.

2. **Coordinate map.** The morphism
   $$
   \Psi=(-b,\rho_1,\ldots,\rho_r):\mathcal C_{\mathbf n}\to T
   $$
   is étale at some scalar point and hence is dominant and generically étale. Consequently,
   $$
   \rho_1,\ldots,\rho_r
   $$
   are algebraically independent over $\mathbf C(b)$ in $\mathbf C(\mathcal C_{\mathbf n})$.

3. **Safe fixed-$b$ specialization.** There is a nonempty Zariski-open set $U\subset\mathbf G_m$ such that, for every $b_0\in U$, the whole-fiber map
   $$
   \rho_{b_0}:
   (\mathcal C_{\mathbf n})_{b_0}\longrightarrow\mathbf A^r,
   \qquad
   x\longmapsto(\rho_1(x),\ldots,\rho_r(x)),
   $$
   is dominant. For each $b_0\in U$, at least one irreducible component of the reduced fiber $(\mathcal C_{\mathbf n})_{b_0,\mathrm{red}}$ maps dominantly and generically étale to $\mathbf A^r$. No irreducibility of the specialized fiber is asserted.

4. **Completed local form.** For every scalar point $s\in\mathcal S_{\mathbf n}$ and centered coefficient coordinates $u=(u_0,\ldots,u_{d-2})$ based at $\pi(s)$, there are compatible isomorphisms
   $$
   \widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
   \simeq\mathbf C[[b,u_0,\ldots,u_{d-2}]],
   \qquad
   \widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
   \simeq\mathbf C[[u_0,\ldots,u_{d-2}]],
   $$
   under which
   $$
   \rho_i(b,u)=\lambda_i(u)+bG_i(b,u)
   $$
   for a unique $G_i\in\mathbf C[[b,u]]$.

5. **Fitting-scheme restriction.** Define
   $$
   \mathcal R_H
   =V\!\left(\operatorname{Fitt}_0
   \Omega_{\mathcal C_{\mathbf n}/T}\right)
   $$
   and
   $$
   \mathcal R_{\mathrm{poly}}
   =V\!\left(\operatorname{Fitt}_0
   \Omega_{\mathcal S_{\mathbf n}/\mathbf A^r}\right).
   $$
   Then
   $$
   \mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
   =\mathcal R_{\mathrm{poly}}
   $$
   as closed subschemes of $\mathcal S_{\mathbf n}$. In completed local coordinates, if $J_H$ and $J_{\mathrm{poly}}$ are local Jacobian determinants, then
   $$
   J_H\bmod b=\pm J_{\mathrm{poly}}.
   $$
   Hence scheme multiplicities agree along every irreducible component of the boundary ramification scheme. For $d>2$, no closed-point numerical intersection multiplicity is asserted without a proper transverse slice.

### Auxiliary Lemma B: finite-free universal ordered loops

For $n\ge1$, let
$$
A_n=
R_d[x_0,\ldots,x_{n-1}]
\Big/
\left(p(x_j)+b x_{j-1}-x_{j+1}:j\in\mathbf Z/n\mathbf Z\right).
$$
Then $A_n$ is finite free over $R_d$ of rank $d^n$, with basis
$$
\mathscr B_n=
\left\{x_0^{e_0}\cdots x_{n-1}^{e_{n-1}}:
0\le e_j<d\right\}.
$$
It represents the full ordered $n$-loop incidence and is scheme-isomorphic to the full incidence of points fixed by $H^n$. For $r$ independent point markings, the fiber-product algebra is finite free of rank
$$
d^{n_1+\cdots+n_r}.
$$

Lemma B is not used to claim irreducibility of the full incidence. Its algebra includes lower-period loops, collisions between markings, and nonsimple or nonreduced fibers.

## Proof strategy

The proof is a reduction to the polynomial boundary followed by formal and scheme-theoretic base change.

1. Use monic Gröbner reduction to establish the optional finite-free description of the full loop incidence.
2. Apply the Jacobian criterion to the orbit equations to show that the simple marked incidence is étale over $\mathcal B_d$.
3. Identify its scalar fiber with the arbitrary-period polynomial marked incidence.
4. Import Gorbovickis's irreducibility and full-rank polynomial multiplier point.
5. Use regularity to place the full scalar locus in one unique total component.
6. Compute $DH_{0,p}^n$ and use the block-triangular differential of $\Psi$ to obtain étaleness at the scalar test point.
7. Spread a dense open subset of the étale locus over the $b$-line, without assuming specialized-fiber irreducibility.
8. Use formal étaleness for the completed local expansion.
9. Use the Cartesian boundary square, base change for Kähler differentials, and base change for Fitting ideals to identify the critical schemes exactly.

## Dependency map

1. Theorem A(1) depends on Lemmas 2, 3, 4, and 5 below.
2. Theorem A(2) depends on Lemmas 4, 6, and 7.
3. Theorem A(3) depends on Theorem A(2), Chevalley constructibility, and base change of the étale locus.
4. Theorem A(4) depends on Theorem A(1), formal étaleness, and Lemma 6.
5. Theorem A(5) depends on Theorem A(1), the Cartesian boundary square, base change of differentials and Fitting ideals, and the local determinant calculation.
6. Auxiliary Lemma B depends only on a monic Gröbner-basis argument over $R_d$ and a functorial identification with $H^n$-fixed points.
7. No conclusion about full-incidence irreducibility depends on Lemma B.

## Proof

### Lemma 1. The universal ordered-loop algebra is finite free

For $j\in\mathbf Z/n\mathbf Z$, set
$$
F_j=p(x_j)+b x_{j-1}-x_{j+1}.
$$
Treat $b,a_0,\ldots,a_{d-2}$ as coefficients and choose any monomial order in the variables $x_0,\ldots,x_{n-1}$ that refines total $x$-degree. Because
$$
p(x_j)=x_j^d+\sum_{k=0}^{d-2}a_kx_j^k
$$
and $d\ge2$, the leading monomial of $F_j$ is $x_j^d$, with leading coefficient $1$. For distinct $j,k$, the monomials $x_j^d$ and $x_k^d$ are relatively prime.

The monic pairwise-coprime leading-monomial criterion for Buchberger reduction remains valid over a commutative coefficient ring: every $S$-polynomial of $F_j,F_k$ reduces to zero because the least common multiple of their leading monomials is their product and both leading coefficients are units. Hence $(F_0,\ldots,F_{n-1})$ is a monic Gröbner basis over $R_d$.

Division by this basis expresses every polynomial as an $R_d$-linear combination of monomials not divisible by any $x_j^d$, namely the monomials in $\mathscr B_n$. To prove independence, suppose that a nonzero $R_d$-linear combination of monomials in $\mathscr B_n$ lies in the ideal $(F_0,\ldots,F_{n-1})$. Its leading monomial is a standard monomial. The defining property of a Gröbner basis would require that leading monomial to be divisible by some $x_j^d$, a contradiction. Thus $\mathscr B_n$ is an $R_d$-basis and $A_n$ is finite free of rank $d^n$.

The cyclic coincidences cause no exception. When $n=1$, the single relation is
$$
p(x_0)+(b-1)x_0,
$$
whose leading monomial is $x_0^d$. When $n=2$, the two relations are
$$
p(x_0)+(b-1)x_1,
\qquad
p(x_1)+(b-1)x_0,
$$
with leading monomials $x_0^d$ and $x_1^d$.

The recurrence
$$
x_{j+1}=p(x_j)+b x_{j-1}
$$
means that
$$
H(x_j,x_{j-1})=(x_{j+1},x_j).
$$
Therefore a cyclic solution gives a fixed point $(x_0,x_{n-1})$ of $H^n$. Conversely, a fixed point of $H^n$ yields its cyclic sequence of first coordinates. These constructions are polynomial and inverse on points over every $R_d$-algebra, so the two represented functors, and hence the two schemes, are isomorphic.

For several independent point markings, the coordinate algebra is
$$
A_{n_1}\otimes_{R_d}\cdots\otimes_{R_d}A_{n_r}.
$$
The tensor products of the displayed bases form an $R_d$-basis of rank $d^{\sum_i n_i}$. This proves Auxiliary Lemma B. $\square$

**Limitation of Lemma 1.** A finite-free full incidence can be reducible. The basis calculation neither selects exact period nor separates distinct cycles. Passing to the exact, disjoint, and simple locus removes closed subsets from a finite scheme; the resulting open morphism is étale and quasi-finite but need not remain finite over all of $\mathcal B_d$. No irreducibility claim will be derived from this lemma.

### Lemma 2. The simple point-marked incidence is étale over the parameter base

In the ambient space
$$
\mathcal B_d\times(\mathbf A^2)^r,
$$
the full point-marked incidence is cut out by the $2r$ coordinate equations
$$
H^{n_i}(z_i)-z_i=0,
\qquad 1\le i\le r.
$$
The derivative of these equations with respect to the $2r$ orbit coordinates is block diagonal. Its $i$-th block is
$$
D_{z_i}H^{n_i}-I_2.
$$
On the simple locus every block is invertible. The relative Jacobian criterion therefore makes the projection
$$
\widetilde{\mathcal X}_{\mathbf n}^{\circ}\to\mathcal B_d
$$
étale. Exactness and pairwise disjointness are open conditions: lower period is detected by finitely many equations $H^m(z_i)=z_i$ for proper divisors $m\mid n_i$, and cycle collision is detected by finitely many equations $H^q(z_i)=H^{q'}(z_j)$.

On an exact cycle, a nontrivial cyclic shift cannot fix the point marking. Thus $G_{\mathbf n}$ acts freely. In characteristic zero the finite free quotient is finite étale, and étaleness over $\mathcal B_d$ descends to
$$
\mathcal X_{\mathbf n}^{\circ}\to\mathcal B_d.
$$
In particular, $\mathcal X_{\mathbf n}^{\circ}$ is smooth of pure dimension
$$
\dim\mathcal B_d=d.
$$
$\square$

### Lemma 3. Identification of the scalar fiber

At $b=0$,
$$
H_{0,p}(x,y)=(p(x),x).
$$
Induction gives, for every $n\ge1$,
$$
H_{0,p}^n(x,y)=\bigl(p^n(x),p^{n-1}(x)\bigr).
$$
The fixed-point equations are therefore
$$
p^n(x)=x,
\qquad
y=p^{n-1}(x).
$$
They identify the scalar fixed-point incidence scheme with the one-variable polynomial fixed-point incidence. Minimal periods agree: if $x$ has minimal polynomial period $m\mid n$, then
$$
p^{n-1}(x)=p^{m-1}(x)
$$
and the lifted pair has minimal $H_{0,p}$-period $m$; the converse follows by projecting to the first coordinate. Orbit disjointness also agrees under this lift.

Differentiating the formula for $H_{0,p}^n$ gives
$$
D_{(x,y)}H_{0,p}^n
=
\begin{pmatrix}
(p^n)'(x)&0\\
(p^{n-1})'(x)&0
\end{pmatrix}.
$$
If $\lambda=(p^n)'(x)$, then
$$
\operatorname{tr}(D H_{0,p}^n)=\lambda
$$
and
$$
\det(DH_{0,p}^n-I)=
\det
\begin{pmatrix}
\lambda-1&0\\
*&-1
\end{pmatrix}
=1-\lambda.
$$
Thus scalar simplicity is exactly polynomial-cycle simplicity, and the Hénon trace restricts exactly to the polynomial multiplier. The same identifications hold after the free cyclic quotients. $\square$

### Lemma 4. The scalar marked locus is irreducible and has a full-rank multiplier point

Gorbovickis defines the marked polynomial space $M^d_{\mathbf n}$ using nonmultiple periodic points of minimal periods $n_i$ lying on distinct cycles. Definition/Remark 1.4 makes it irreducible, and Lemma 1.5 shows that it is independent of the initial polynomial and markings. Its simple exact disjoint locus is a nonempty Zariski-open subset and is therefore irreducible. The free finite cyclic quotient remains irreducible. By Lemma 3 this quotient is $\mathcal S_{\mathbf n}$.

Gorbovickis's Theorem 1.6 applies for every $d\ge2$, every $k\le d-1$, and every positive period vector. With $k=r=d-1$ and all coefficient directions selected, Lemma 2.1 supplies nonzero periodic points of exact periods $n_i$ for
$$
p_0(z)=z^d
$$
such that
$$
\det\left(\frac{\partial\lambda_i}{\partial a_j}\right)_{1\le i\le r,\,0\le j\le d-2}\ne0.
$$
The theorem's proof observes that these points lie on distinct cycles. At every nonzero exact $n_i$-periodic point of $z^d$,
$$
(p_0^{n_i})'(x)=d^{n_i}x^{d^{n_i}-1}=d^{n_i}\ne1,
$$
so the selected cycles are simple. Passing through the finite étale cyclic quotient preserves the full-rank differential. $\square$

### Lemma 5. A unique total component contains the full scalar locus

By Lemma 2, $\mathcal X_{\mathbf n}^{\circ}$ is regular. At every point of a regular scheme the local ring is a domain, so two distinct irreducible components cannot meet. Thus the irreducible components of this finite-type regular scheme are pairwise disjoint open-and-closed subsets.

The irreducible set $\mathcal S_{\mathbf n}$ cannot meet two disjoint open-and-closed components. Hence it is contained in one component, denoted $\mathcal C_{\mathbf n}$. Since every scalar point belongs to $\mathcal S_{\mathbf n}$ by Lemma 3, no other component of $\mathcal X_{\mathbf n}^{\circ}$ meets $b=0$. Because the projection is étale, the scalar fiber is reduced. Consequently,
$$
(\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}
$$
scheme-theoretically.

The restriction $\pi:\mathcal C_{\mathbf n}\to\mathcal B_d$ is étale. An étale morphism is open; its image is a nonempty open subset of the irreducible base $\mathcal B_d$, so the image is dense. Thus $\pi$ is dominant. This proves Theorem A(1). $\square$

The reduced closure of the corresponding point-marked component in the full finite-free incidence of Lemma 1 is finite over $\mathcal B_d$. This observation is useful for global bookkeeping but is not needed to prove uniqueness or irreducibility of $\mathcal C_{\mathbf n}$.

### Lemma 6. Boundary traces and the block differential

At every point,
$$
DH_{b,p}=
\begin{pmatrix}
p'(x)&b\\
1&0
\end{pmatrix},
\qquad
\det DH_{b,p}=-b.
$$
Multiplicativity of the determinant along an $n_i$-cycle therefore gives
$$
\det(DH_{b,p}^{n_i})=(-b)^{n_i}.
$$
Thus trace together with the known determinant records the unordered eigenvalue pair; it does not select an eigenvalue branch.

Let $s\in\mathcal S_{\mathbf n}$ be the full-rank scalar point from Lemma 4. Since $\pi$ is étale, centered coefficient coordinates
$$
u=(a_0,\ldots,a_{d-2})
$$
together with $b$ are local coordinates on $\mathcal C_{\mathbf n}$ at $s$. By Lemma 3,
$$
\rho_i(0,u)=\lambda_i(u).
$$
With target coordinates ordered as $t,q_1,\ldots,q_r$, the differential is
$$
D\Psi=
\begin{pmatrix}
-1&0&\cdots&0\\
\partial_b\rho_1&&&\\
\vdots&&\left(\partial_{u_j}\rho_i\right)&\\
\partial_b\rho_r&&&
\end{pmatrix}.
$$
Therefore
$$
\det D\Psi
=\pm\det\left(\partial_{u_j}\rho_i\right),
$$
and at $b=0$,
$$
\det D\Psi(s)
=\pm\det\left(\partial_{u_j}\lambda_i\right)(s)\ne0.
$$
Thus $\Psi$ is étale at $s$. $\square$

### Lemma 7. Dominance, generic étaleness, and algebraic independence

Both $\mathcal C_{\mathbf n}$ and $T$ are irreducible of dimension $d$. Lemma 6 shows that the image of $\Psi$ contains a Euclidean and hence Zariski-dense neighborhood of $\Psi(s)$; equivalently, the image has dimension $d$. Thus $\Psi$ is dominant. Since it is étale at one point, its étale locus is a nonempty Zariski-open subset. It is consequently generically étale.

Dominance makes the pullback
$$
\mathbf C[t,q_1,\ldots,q_r]
\longrightarrow \mathbf C(\mathcal C_{\mathbf n})
$$
injective. Substituting $t=-b$ and $q_i=\rho_i$ shows that $b,\rho_1,\ldots,\rho_r$ are algebraically independent over $\mathbf C$. If a nonzero relation with coefficients in $\mathbf C(b)$ existed among the $\rho_i$, clearing denominators would give a nonzero polynomial relation over $\mathbf C$ among $b,\rho_1,\ldots,\rho_r$, a contradiction. This proves Theorem A(2). $\square$

### Lemma 8. Safe spreading to fixed nonzero $b$

Let $E\subset\mathcal C_{\mathbf n}$ be the étale locus of $\Psi$. It is nonempty, open, and dense. The restricted morphism
$$
\Psi|_E:E\longrightarrow T
$$
is étale and is therefore an open map. Set
$$
V=\Psi(E).
$$
Then $V$ is a nonempty open subset of the irreducible variety $T$, hence is dense. The projection
$$
\operatorname{pr}_t:T=\mathbf A^1_t\times\mathbf A^r\longrightarrow\mathbf A^1_t
$$
is also open. Consequently $\operatorname{pr}_t(V)$ is a nonempty open subset of $\mathbf A^1_t$, and for every $t_0\in\operatorname{pr}_t(V)$ the fiber $V_{t_0}$ is a nonempty open, hence dense, subset of $\mathbf A^r$. After the change $t=-b$, set
$$
U=\{-t:t\in\operatorname{pr}_t(V)\}\cap\mathbf G_m.
$$
Because a nonempty open subset of $\mathbf A^1$ cannot be supported only at $0$, $U$ is nonempty and Zariski open in $\mathbf G_m$.

Fix $b_0\in U$. For every point of the dense open set $V_{-b_0}\subset\mathbf A^r$, the definition $V\subset\Psi(E)$ supplies a preimage in $E_{b_0}$. Hence the image of the whole fiber $(\mathcal C_{\mathbf n})_{b_0}$ contains $V_{-b_0}$ and is dense: the fiber trace map is dominant.

The reduced fiber has finitely many irreducible components. The closures of their images form a finite collection of closed subsets whose union is $\mathbf A^r$. Since $\mathbf A^r$ is irreducible, at least one component, call it $D_{b_0}$, has dense image. Moreover, $E\cap D_{b_0}$ contains a nonempty open subset after choosing such a dominating component from the components whose étale-locus images cover a dense subset. Base-changing the étale map
$$
E\to T
$$
along $\{-b_0\}\times\mathbf A^r\hookrightarrow T$ shows that
$$
E_{b_0}\to\mathbf A^r
$$
is étale. Thus the trace map on $D_{b_0}$ is dominant and generically étale.

This proves Theorem A(3) without assuming that $(\mathcal C_{\mathbf n})_{b_0}$ is irreducible. $\square$

### Lemma 9. Completed local trace expansion

Fix $s\in\mathcal S_{\mathbf n}$. The map
$$
\pi:\mathcal C_{\mathbf n}\to\mathcal B_d
$$
is étale at $s$, and both residue fields are $\mathbf C$. Formal étaleness therefore identifies completed local rings:
$$
\widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
\simeq
\widehat{\mathcal O}_{\mathcal B_d,\pi(s)}
\simeq\mathbf C[[b,u_0,\ldots,u_{d-2}]].
$$
This is the standard completed-local property of étale morphisms; the relevant official Stacks Project discussions are [Tag 02GH](https://stacks.math.columbia.edu/tag/02GH) and [Tag 0257](https://stacks.math.columbia.edu/tag/0257).

By Theorem A(1), the scalar fiber is cut out scheme-theoretically by $b$. Hence
$$
\widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
\simeq\mathbf C[[u_0,\ldots,u_{d-2}]].
$$
Choose the unique formal continuations of the simple polynomial cycles over $\mathbf C[[u]]$ and let $\lambda_i(u)$ be their multiplier germs. Lemma 3 gives
$$
\rho_i(0,u)=\lambda_i(u).
$$
Therefore $\rho_i-\lambda_i$ lies in the principal ideal $(b)$ of $\mathbf C[[b,u]]$. Since $b$ is a non-zero-divisor, there is a unique $G_i\in\mathbf C[[b,u]]$ satisfying
$$
\rho_i=\lambda_i+bG_i.
$$
This proves Theorem A(4). $\square$

### Lemma 10. Exact base change of the critical Fitting scheme

Let
$$
T_0=\{t=0\}\times\mathbf A^r\subset T.
$$
Because $t\circ\Psi=-b$ and the entire simple scalar fiber of $\mathcal C_{\mathbf n}$ is $\mathcal S_{\mathbf n}$, the square
$$
\begin{array}{ccc}
\mathcal S_{\mathbf n}&\longrightarrow&\mathcal C_{\mathbf n}\\
\downarrow\Lambda&&\downarrow\Psi\\
T_0&\longrightarrow&T
\end{array}
$$
is Cartesian.

Relative Kähler differentials commute with base change, yielding
$$
\Omega_{\mathcal C_{\mathbf n}/T}
\otimes_{\mathcal O_{\mathcal C_{\mathbf n}}}
\mathcal O_{\mathcal S_{\mathbf n}}
\simeq
\Omega_{\mathcal S_{\mathbf n}/T_0}.
$$
Zeroth Fitting ideals of finitely presented modules commute with arbitrary base change. The exact official references are [Stacks Project, Tag 07Z6, Lemma 15.8.4](https://stacks.math.columbia.edu/tag/07Z6) for Fitting ideals under base change and [Tag 0C3I](https://stacks.math.columbia.edu/tag/0C3I) for the scheme-level construction. Consequently,
$$
\operatorname{Fitt}_0\Omega_{\mathcal C_{\mathbf n}/T}
\cdot\mathcal O_{\mathcal S_{\mathbf n}}
=
\operatorname{Fitt}_0\Omega_{\mathcal S_{\mathbf n}/T_0}.
$$
Identifying $T_0$ with $\mathbf A^r$ gives
$$
\mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
=\mathcal R_{\mathrm{poly}}
$$
as schemes.

For the local determinant form, use the coordinates of Lemma 9. The differential matrix is block triangular as in Lemma 6. Since
$$
\rho_i=\lambda_i+bG_i,
$$
we have
$$
\frac{\partial\rho_i}{\partial u_j}\bmod b
=\frac{\partial\lambda_i}{\partial u_j}.
$$
Thus
$$
J_H\bmod b=\pm J_{\mathrm{poly}}.
$$
This proves the scheme equality in Theorem A(5). $\square$

### Lemma 11. What multiplicity is preserved

The schemes $\mathcal C_{\mathbf n}$ and $\mathcal S_{\mathbf n}$ are smooth and irreducible. The determinant of each differential is a regular section of the corresponding determinant line bundle. Generic étaleness of $\Psi$ shows that the Hénon determinant section is not identically zero, while the full-rank scalar point supplied by Gorbovickis shows that the polynomial determinant section is not identically zero. Consequently, $\mathcal R_H$ and $\mathcal R_{\mathrm{poly}}$ are effective Cartier divisors when their determinant sections vanish somewhere, and are empty otherwise. No nonemptiness of $\mathcal R_{\mathrm{poly}}$ is imported from Gorbovickis.

The congruence $J_H\bmod b=\pm J_{\mathrm{poly}}$ shows that the scalar divisor $(b=0)$ is not a component of $(J_H=0)$. If $\mathcal R_{\mathrm{poly}}$ is empty, the multiplicity assertion is vacuous. Otherwise, let $Z$ be any irreducible component of $\mathcal R_{\mathrm{poly}}$, with generic point $\eta_Z$. The proper intersection multiplicity of the two Cartier divisors at that generic point is
$$
\operatorname{length}_{\mathcal O_{\mathcal C_{\mathbf n},\eta_Z}}
\frac{\mathcal O_{\mathcal C_{\mathbf n},\eta_Z}}{(b,J_H)}
=
\operatorname{length}_{\mathcal O_{\mathcal S_{\mathbf n},\eta_Z}}
\frac{\mathcal O_{\mathcal S_{\mathbf n},\eta_Z}}{(J_{\mathrm{poly}})}.
$$
This is precisely the component multiplicity encoded by the scheme restriction.

For every such $Z$, when $d>2$, $\dim\mathcal S_{\mathbf n}=d-1$ and $Z$ has dimension $d-2>0$. The local quotient at an arbitrary closed point is then not Artinian, so no pointwise numerical intersection multiplicity follows. A compatible transverse slice could produce such a number, but no slicing theorem is part of Theorem A. This completes Theorem A(5). $\square$

### Lemma 12. Residual normal-form quotient and the injectivity obstruction

For $\beta\in\mu_{d-1}$, the diagonal map
$$
L_\beta(x,y)=(\beta x,\beta y)
$$
satisfies
$$
L_\beta^{-1}\circ H_{b,p}\circ L_\beta
=H_{b,p_\beta},
\qquad
p_\beta(z)=\beta^{-1}p(\beta z).
$$
The condition $\beta^{d-1}=1$ makes $p_\beta$ monic and centered. Conjugacy transports the labelled cycles and preserves $b$ and all traces. The action preserves $\mathcal S_{\mathbf n}$ and therefore, by uniqueness in Theorem A(1), preserves $\mathcal C_{\mathbf n}$.

For a generic centered polynomial and generic marked tuple, the stabilizer is trivial. Hence a generic fiber of $\Psi$ on the normal-form cover contains at least the $d-1$ points of a $\mu_{d-1}$-orbit when $d>2$. The theorem cannot imply global injectivity or birationality on this cover. At points with nontrivial stabilizer, passing to a coarse quotient can create quotient singularities; the completed-local theorem should remain on the normal-form cover unless a stack formulation or a stabilizer-free open is used. $\square$

Combining Lemmas 1--12 proves Auxiliary Lemma B and every part of Theorem A. $\blacksquare$

## Frozen anti-claim ledger

The following A1--A20 ledger is frozen verbatim across all ten source-design files.

- **A1.** No irreducibility claim for the full marked Hénon incidence.
- **A2.** No irreducibility claim for any or every specialized fixed-$b$ fiber.
- **A3.** No local-coordinate claim for every nonzero $b$.
- **A4.** No conclusion at any prescribed nonzero fiber, including $b=-1$.
- **A5.** No global injectivity, birationality, or reconstruction claim on the monic-centered normal-form cover.
- **A6.** No claim that every irreducible component of a general fixed-$b$ fiber dominates or is generically étale.
- **A7.** No reducedness or smoothness claim for either critical/Fitting scheme.
- **A8.** No transversality or normal-crossings claim for the boundary intersection.
- **A9.** No global, nonsimple, or compactified Fitting-scheme equality beyond the simple scalar locus.
- **A10.** No closed-point numerical intersection multiplicity without a separately justified proper transverse slice; the theorem preserves generic multiplicities along boundary components.
- **A11.** No individual eigenvalue branch is a coordinate: $\det(DH_{b,p}^{n_i})=(-b)^{n_i}$, so trace records only the unordered eigenvalue pair once the determinant is known.
- **A12.** No interpretation of finite-free rank $d^n$ as an exact-cycle count.
- **A13.** The fiber $b=0$ is only the polynomial/proof boundary; $H_{0,p}$ is not a Hénon automorphism.
- **A14.** No positive-characteristic extension.
- **A15.** No extension to multi-factor or composed generalized Hénon maps.
- **A16.** Point-marked fibers contain cyclic-shift copies; passage to cycle markings removes only those shifts, not residual $\mu_{d-1}$ ambiguity.
- **A17.** No naive coarse $\mu_{d-1}$-quotient completed-local claim near stabilizers; stack or quotient-singularity analysis is required.
- **A18.** No claim that the simple exact open is finite or proper over all of $\mathcal B_d$, no uniform all-fiber degree, and no all-fiber reconstruction.
- **A19.** No absolute-priority or “first ever” claim.
- **A20.** No computational, CAS, numerical, empirical, or experimental evidence or result.

## Corrections already incorporated

1. The degree range is $d\ge2$, not merely $d\ge3$.
2. The incidence is defined using exact, disjoint, simple marked cycles; point and cycle markings are distinguished explicitly.
3. Only the unique component through the irreducible scalar marked locus is used.
4. Fixed-$b$ specialization is asserted on a nonempty open $U\subset\mathbf G_m$, not for every nonzero $b$.
5. Because a specialized fiber can be reducible, the theorem guarantees at least one dominant generically étale component of the reduced fiber, not every component.
6. The Fitting equality is on the simple scalar locus; it is not extended across nonsimple boundary points.
7. Multiplicity means multiplicity along components of the scheme-theoretic boundary intersection, not an automatic closed-point number in dimension greater than two.
8. The residual $\mu_{d-1}$ quotient is recorded, and global injectivity is explicitly excluded.
9. The finite-free loop lemma is not used as an irreducibility argument.

## Open risks

- **No proof risk on the frozen theorem:** every substantive step is either proved above or reduced to the precisely scoped Gorbovickis result.
- **Presentation risk:** calling the selected functions “multipliers” without saying “trace plus known determinant” could suggest chosen eigenvalue branches. The paper should use “marked traces” in theorem statements.
- **Boundary-scope risk:** a global compactified critical-cycle assertion would need new lci, reducedness, and component-control arguments. It is outside the theorem.
- **Special-fiber risk:** no argument identifies the exceptional finite set of $b$-values. In particular, the theorem does not settle a preassigned conservative or symplectic fiber.
- **Coarse-moduli risk:** quotient points with nontrivial $\mu_{d-1}$ stabilizers require separate local analysis.
- **Standalone risk:** the paper must present the scheme-theoretic ramification theorem and exact marked-component construction as central contributions. A note containing only the openness transfer from $b=0$ would be too slight.
