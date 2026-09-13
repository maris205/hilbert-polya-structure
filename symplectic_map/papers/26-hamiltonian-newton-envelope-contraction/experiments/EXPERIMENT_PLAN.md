# Claim-driven validation plan

## Frozen object of study

Title: Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector Rigidity and Bidirectional Degree Growth

Candidate identifier: planar_newton_envelope_bidirectional_degree_v1

Let K be a field of characteristic zero. Fix a finite, nonempty, collected support
\[
E\subset \mathbf Z_{\ge 2}^{2},\qquad
V(q_1,q_2)=\sum_{(x,y)\in E}c_{x,y}q_1^xq_2^y,\qquad c_{x,y}\ne0,
\]
and
\[
W(p_1,p_2)=\alpha p_1^{e+1}+\beta p_2^{f+1},
\qquad e,f\ge2,\quad \alpha\beta\ne0.
\]
The lower and upper Hamiltonian shears are
\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),
\]
and the map is \(F=T\circ S\). The validation target is the full theorem package for this fixed phase order and the ordinary seed \(\mathbf1=(1,1)^\top\), not an empirical estimate of degree growth.

No numerical or computer-algebra run is part of this source-design stage. The protocols below are exact symbolic checks that a later author or reviewer can execute independently. A computed table is admissible only after its entries have been rederived from the displayed formulas; it cannot replace a proof.

## Dependency graph

The validation order is deliberately one-way.

1. Verify the symplectic formulas and inverse phase order.
2. Verify the exposed-face Hessian determinant certificate.
3. Use that certificate to validate algebraic independence of every leading pair.
4. With cancellation excluded, validate all forward and inverse degree carries and visible blocks.
5. Derive the exact bridge between the forward and inverse recurrences.
6. Derive the projective forward map, its log derivative, and its inverse conjugate.
7. Prove a uniform contraction constant over the finite support, including Newton walls.
8. Classify the eventual selector tail from the unique fixed ray.
9. Derive the interior and wall spectra and the corresponding degree recurrences.
10. Check the two positive fixtures and the boundary counterexamples.

A failure at an earlier item kills every dependent item. In particular, observed degree sequences do not repair an unproved top-form survival claim.

## Protocol P1: symplecticity and inversion

Write the standard symplectic matrix as
\[
J=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix}.
\]
Differentiate the two shears:
\[
DS=\begin{pmatrix}I_2&0\\H_V&I_2\end{pmatrix},\qquad
DT=\begin{pmatrix}I_2&H_W\\0&I_2\end{pmatrix},
\]
where \(H_V\) and \(H_W\) are symmetric Hessians. Multiply \(DS^\top JDS\) and \(DT^\top JDT\) explicitly. The off-diagonal error blocks must reduce respectively to \(H_V-H_V^\top\) and \(H_W^\top-H_W\), hence vanish.

Then compose the subtraction shears
\[
S^{-1}(q,p)=(q,p-\nabla V(q)),\qquad
T^{-1}(q,p)=(q-\nabla W(p),p)
\]
in the reverse order and verify
\[
F^{-1}=S^{-1}\circ T^{-1}.
\]

Acceptance criterion: both matrix identities and both two-sided composition identities hold as polynomial identities. Any altered sign or an inverse written in the forward phase order is a hard failure.

## Protocol P2: arbitrary exposed-face Hessian

For a positive weight \(u=(u_1,u_2)\), let
\[
H(u)=\max_{(x,y)\in E}(xu_1+yu_2),
\qquad
E_u=\{(x,y)\in E:xu_1+yu_2=H(u)\}.
\]
Form the exposed-face polynomial
\[
P_u(X,Y)=\sum_{(x,y)\in E_u}c_{x,y}X^xY^y.
\]
Choose the point \((x_0,y_0)\in E_u\) having minimal \(x\). It is unique: two points of the same exposed face with the same \(x\) also have the same \(y\).

Expand
\[
\det \operatorname{Hess}P_u=P_{XX}P_{YY}-P_{XY}^{2}.
\]
At exponent \(X^{2x_0-2}Y^{2y_0-2}\), equality of the two contributing \(x\)-indices forces both to equal \(x_0\), and hence both \(y\)-indices equal \(y_0\). The coefficient must therefore be exactly
\[
c_{x_0,y_0}^{\,2}x_0y_0(1-x_0-y_0),
\]
which is nonzero in characteristic zero because \(x_0,y_0\ge2\).

Acceptance criterion: the reviewer reconstructs the coefficient from the two Hessian products and confirms that no distinct support pair contributes at that exponent. Sampling only vertex faces is insufficient.

## Protocol P3: top-form survival

For algebraically independent homogeneous forms \(L_1,L_2\), substitute them into the face-gradient pair
\[
\bigl((P_u)_X,(P_u)_Y\bigr).
\]
The nonzero Hessian determinant and the characteristic-zero Jacobian criterion must imply that the face-gradient pair is algebraically independent. Injectivity of the substitution map
\[
K[X,Y]\longrightarrow K[\text{ambient variables}],\qquad
X\mapsto L_1,\quad Y\mapsto L_2
\]
then preserves this independence. Independently verify that nonzero scalar multiples, signs, and the pure-power transform
\[
(L_1,L_2)\mapsto(L_1^e,L_2^f)
\]
also preserve algebraic independence.

Apply these facts to every half-step in both \(F^n\) and \(F^{-n}\). At a Newton wall, use the entire face polynomial \(P_u\); do not select one tied monomial. At each phase record:

- the current degree vector;
- the exposed face;
- the surviving homogeneous leading pair;
- the injective substitution used at the next phase.

Acceptance criterion: induction begins from the coordinate variables and closes in both time directions without a generic-coefficient assumption. A calculation that silently discards a tied face fails.

## Protocol P4: exact degree transports

Define
\[
\mathcal A(u)=
\begin{pmatrix}H(u)-u_1\\H(u)-u_2\end{pmatrix},
\qquad
B=\operatorname{diag}(e,f).
\]
Check the componentwise carry inequalities
\[
H(u)-u_1\ge u_1+2u_2>\max(u_1,u_2),
\]
\[
H(u)-u_2\ge2u_1+u_2>\max(u_1,u_2).
\]

Forward transport:
\[
w^+_{n+1}=\mathcal A(u^+_n),\qquad
u^+_{n+1}=B\,\mathcal A(u^+_n),\qquad u^+_0=\mathbf1.
\]
Verify that after the lower shear the fresh momentum block dominates every old momentum term, and after the upper shear the fresh position block dominates both the carried position and the momentum block. The visible total degree is
\[
\deg(F^n)=\|u^+_n\|_\infty.
\]

Inverse transport:
\[
z^-_{n+1}=Bv^-_n,\qquad
v^-_{n+1}=\mathcal A(Bv^-_n),\qquad v^-_0=\mathbf1.
\]
Verify the analogous two carries in the reversed subtraction phases. The visible total degree is now the final momentum block:
\[
\deg(F^{-n})=\|v^-_n\|_\infty.
\]

Acceptance criterion: the block in which the final maximum is attained is named at each phase; proving only a vector recurrence without visibility is not enough.

## Protocol P5: forward–inverse bridge

Let
\[
c_\star=H(\mathbf1)-1.
\]
Because both components of \(\mathcal A(\mathbf1)\) equal \(c_\star\),
\[
u^+_1=c_\star Bv^-_0.
\]
Use positive homogeneity of \(H\) and \(\mathcal A\) to prove inductively
\[
u^+_{n+1}=c_\star Bv^-_n\qquad(n\ge0).
\]
Then check
\[
c_\star\min(e,f)\deg(F^{-n})
\le \deg(F^{n+1})
\le c_\star\max(e,f)\deg(F^{-n}).
\]

Acceptance criterion: the index shift, seed, and phase order match exactly. The conclusion is \(\lambda_1(F)=\lambda_1(F^{-1})\); the protocol does not assert termwise equality of the two degree sequences.

## Protocol P6: projective contraction

In the chart \(u=(r,1)\), set
\[
\Phi(r)=\max_{(x,y)\in E}(xr+y),\qquad \kappa=e/f.
\]
The forward ratio map is
\[
\phi(r)=\kappa\frac{\Phi(r)-r}{\Phi(r)-1}.
\]
On a chamber selected by \((x,y)\),
\[
\phi_{x,y}(r)=
\kappa\frac{(x-1)r+y}{xr+y-1}.
\]
Differentiate both in \(r\) and in \(t=\log r\). The absolute logarithmic derivative must be
\[
\eta_{x,y}(r)=
\frac{r(x+y-1)}
{((x-1)r+y)(xr+y-1)}.
\]
Verify the strict gap identity
\[
((x-1)r+y)(xr+y-1)-r(x+y-1)
=x(x-1)r^2+2(x-1)(y-1)r+y(y-1)>0.
\]
For each support point, compactify \(r\in(0,\infty)\) by adjoining \(0\) and \(\infty\); \(\eta_{x,y}\) tends to zero at both ends, so its maximum is strictly below one. Take the maximum over finite \(E\). Split an interval at its finitely many Newton walls, integrate the chamberwise derivative bound, and reassemble it using continuity of \(\Phi\).

Acceptance criterion: a single \(q<1\) works globally in log distance. Taking a supremum over an infinite or uncollected support is outside scope.

## Protocol P7: selector and spectral tails

Define the inverse ratio map
\[
\psi(s)=\frac{\Phi(\kappa s)-\kappa s}{\Phi(\kappa s)-1},
\qquad L(s)=\kappa s.
\]
Verify the exact conjugacy
\[
L\circ\psi=\phi\circ L.
\]
By the global log contraction, \(\phi\) has a unique fixed ray and no nontrivial numerical cycle.

Classify:

- If the fixed ray lies inside one chamber, every orbit eventually remains in that chamber.
- If it lies on a wall, the fixed ray stays on the wall, while a strict orbit alternates the two adjacent chambers and converges to the wall.
- At a multiple tie, the extreme adjacent exponents control the two open sides; the full tied face controls a trajectory on the wall.
- Because the contraction is injective and decreasing, an orbit cannot land on the fixed ray after a delay. The ordinary seed lands on it exactly when the fixed ratio is one.

For an interior selector \((x,y)\), form
\[
C_{x,y}=B
\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix}.
\]
Its Perron root is quadratic over \(\mathbf Q\) at worst. On a rational Newton wall let \(w\) be its primitive positive integral direction. Adjacent selector matrices obey
\[
C_-w=C_+w=\mu w.
\]
Since \(\mu\) is both rational and an algebraic integer, verify \(\mu\in\mathbf Z_{>0}\). Thus the two-step Perron root is \(\mu^2\), while the per-step dynamical degree is the integer \(\mu\).

Acceptance criterion: the final statement is the uniform bound
\[
[\mathbf Q(\lambda_1(F)):\mathbf Q]\le2.
\]
No quartic wall bound and no selector-cycle search are retained.

## Protocol P8: recurrence extraction

For \(\xi=(x,y)\), set
\[
A_\xi=\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},
\qquad C_\xi=BA_\xi.
\]
For a forward interior tail, apply Cayley–Hamilton to \(C_\xi\). Each forward state coordinate obeys an order-at-most-two constant-coefficient recurrence. After the selector has stabilized, the visible total degree is a fixed coordinate unless the seed is the fixed ray, where it is geometric from the start.

For the inverse interior tail, reconstruct
\[
D_\xi=A_\xi B=B^{-1}C_\xi B
\]
and verify directly that \(v^-_{n+1}=D_\xi v^-_n\) after selector stabilization. Cayley–Hamilton for \(D_\xi\) has the same trace and determinant as for \(C_\xi\). If \(s_\star\ne1\), verify that \(s_n=v^-_{n,1}/v^-_{n,2}\to s_\star\) makes one inverse coordinate the eventual visible maximum. If \(s_\star=1\), verify that the ordinary seed \(v^-_0=\mathbf1\) is fixed projectively from time zero and the scalar degrees are geometric.

For a strict forward wall tail, choose both parity monodromies \(M_+=C_+C_-\) and \(M_-=C_-C_+\) in the order dictated by the selector word. For the inverse wall tail, first verify that strictness of the ordinary inverse orbit forces \(s_\star\ne1\), and form
\[
N_+=D_+D_-,
\qquad
N_-=D_-D_+.
\]
Check the exact similarities
\[
N_\pm=B^{-1}M_\pm B,
\]
then verify the common values
\[
\tau=\operatorname{tr}(N_+)=\operatorname{tr}(N_-),
\qquad
\Delta=\det(N_+)=\det(N_-).
\]
Convergence to \(s_\star\ne1\) must stabilize the visible inverse coordinate on each parity. Only then may the inverse scalar degree be promoted to
\[
d^-_{n+4}=\tau d^-_{n+2}-\Delta d^-_n.
\]

Acceptance criterion: both time directions have their own state matrices and visible-coordinate argument; the diagonal bridge is checked only as a vector/rate comparison and is not accepted as a scalar-recurrence proof. Every recurrence order is an upper bound, with no minimality assertion.

## Positive fixture F1: one-face quadratic regime

Use
\[
E=\{(2,2)\},\qquad B=\operatorname{diag}(3,2).
\]
Then
\[
A=\begin{pmatrix}1&2\\2&1\end{pmatrix},\qquad
C=BA=\begin{pmatrix}3&6\\4&2\end{pmatrix}.
\]
The characteristic polynomial is
\[
t^2-5t-18,
\]
so
\[
\lambda_1(F)=\frac{5+\sqrt{97}}2.
\]
Also \(c_\star=3\) and
\[
u^+_1=(9,6)^\top,\qquad
v^-_1=(7,8)^\top,\qquad
u^+_2=(63,48)^\top=3B(7,8)^\top.
\]

Acceptance criterion: the fixture confirms a genuinely quadratic interior value and the exact shifted bridge.

## Positive fixture F2: three-support transient to a wall

Use
\[
E=\{(2,8),(4,5),(5,3)\},\qquad
B=\operatorname{diag}(24,11).
\]
The Newton walls are \(r=3/2\) and \(r=2\). In low, middle, and high chambers respectively,
\[
C_{\rm low}=\begin{pmatrix}24&192\\22&77\end{pmatrix},
\quad
C_{\rm mid}=\begin{pmatrix}72&120\\44&44\end{pmatrix},
\quad
C_{\rm high}=\begin{pmatrix}96&72\\55&22\end{pmatrix}.
\]
Starting from \(r_0=1\), verify
\[
r_1=\frac{24}{11}>2,\qquad
r_2=\frac{1548}{781}\in(3/2,2),
\]
\[
r_3=\frac{205176}{102476}
=\frac{51294}{25619}>2.
\]
Prove by interval images that the tail alternates middle, high, middle, high, and so on. For \(w=(2,1)^\top\),
\[
C_{\rm mid}w=C_{\rm high}w=132w.
\]
With the middle-then-high two-step order,
\[
M=C_{\rm high}C_{\rm mid}
=\begin{pmatrix}10080&14688\\4928&7568\end{pmatrix}.
\]
Check
\[
\operatorname{tr}(M)=17648,\qquad
\det(M)=3902976,
\]
and eigenvalues
\[
17424=132^2,\qquad224.
\]

Acceptance criterion: the example is described as a selector alternation converging to a wall, never as a nontrivial projective two-cycle.

## Boundary and mutation suite

Each mutation is a kill test, not an extension claim.

| Mutation | Expected failure |
|---|---|
| Allow an axis exponent, for example \(V=q_1^3+q_1q_2^3\) | A chamber face can have a zero gradient coordinate, so face independence and the two-coordinate carry fail. |
| Allow an exponent equal to one | The strict carry inequalities need not hold. |
| Replace the separated pure-power \(W\) by a mixed Hamiltonian | Diagonal scaling and decreasing projective dynamics can fail; the square based on \((2,2)\) gives an increasing ratio map \((5r+4)/(4r+5)\). |
| Work in positive characteristic | Derivative and Hessian coefficients may vanish. |
| Leave zero coefficients in the declared support | The Newton envelope no longer represents the polynomial actually iterated. |
| Keep a tied wall but replace its face polynomial by one monomial | The cancellation proof is invalid. |
| Change the seed or phase order while retaining the same bridge | The base case and index shift fail. |
| Infer higher dynamical degrees or entropy from total-degree growth | The conclusion exceeds the proved invariant. |
| Call the order-four wall recurrence minimal | Cayley–Hamilton supplies only an upper bound. |

## Final acceptance checklist

A later verification passes only if all of the following are true.

- Every assumption is used at an identified step.
- Face-Hessian nonvanishing is proved for every positive exposed face.
- Algebraic independence is carried through every forward and inverse half-step.
- Degree vectors and visible total-degree blocks are both proved.
- The exact bridge has the correct seed and shift.
- A global, support-uniform log contraction is established across walls.
- The inverse ratio dynamics is conjugate to the forward dynamics.
- Interior and wall tails exhaust all selector behavior.
- The algebraic-degree bound is two, with the wall value integral.
- Both fixtures reproduce all displayed exact integers.
- Every boundary mutation is stated as a limitation, not patched by genericity.

The plan is successful when these symbolic obligations can be checked from the proof package alone and the claims matrix contains no unsupported promotion.
