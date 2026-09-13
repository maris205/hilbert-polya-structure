# Research question and theorem target

## Frozen identity

Title: Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector Rigidity and Bidirectional Degree Growth

Candidate identifier: planar_newton_envelope_bidirectional_degree_v1

## Primary question

Consider a planar position Hamiltonian with an arbitrary finite positive interior Newton support and a separated pure-power momentum Hamiltonian. For the product of their Hamiltonian shears:

1. can every potential top-degree cancellation, including cancellation on a Newton wall, be excluded for all nonzero coefficients;
2. can forward and inverse ordinary degree growth be transported by exact finite-dimensional vector recurrences and then yield separately proved scalar tail recurrences;
3. does the induced projective Newton-envelope map force a rigid selector tail rather than higher-period selector behavior; and
4. what uniform arithmetic restriction follows for the first dynamical degree?

The desired answer is a single proof chain. It should not rely on experiments, generic coefficients, an assumed stable selector, or a separate inverse asymptotic estimate.

## Map class

Work over a field \(K\) of characteristic zero. Let
\[
E\subset\mathbf Z_{\ge2}^{2}
\]
be finite and nonempty. The support is collected: every listed exponent has one nonzero combined coefficient. Set
\[
V(q_1,q_2)=\sum_{(x,y)\in E}c_{x,y}q_1^xq_2^y,
\qquad c_{x,y}\in K^\times,
\]
and
\[
W(p_1,p_2)=\alpha p_1^{e+1}+\beta p_2^{f+1},
\qquad e,f\ge2,\quad \alpha,\beta\in K^\times.
\]
On \(\mathbf A^4_K\) with coordinates \((q_1,q_2,p_1,p_2)\), define
\[
S(q,p)=(q,p+\nabla V(q)),\qquad
T(q,p)=(q+\nabla W(p),p),\qquad F=T\circ S.
\]

The phase order, the use of ordinary total degree, and the initial coordinate-degree vector \(\mathbf1=(1,1)^\top\) are part of the target. Changing any of them may preserve some contraction phenomena, but it changes the exact forward–inverse bridge.

## Main theorem target

Define the Newton support function and its gradient-degree transform by
\[
H(u_1,u_2)=\max_{(x,y)\in E}(xu_1+yu_2),
\]
\[
\mathcal A(u)=
\begin{pmatrix}H(u)-u_1\\H(u)-u_2\end{pmatrix},
\qquad
B=\operatorname{diag}(e,f).
\]
Starting from \(u^+_0=v^-_0=\mathbf1\), define
\[
u^+_{n+1}=B\mathcal A(u^+_n),\qquad
v^-_{n+1}=\mathcal A(Bv^-_n).
\]
The theorem should establish all of the following under exactly the displayed hypotheses.

### Exact cancellation-free degree transport

Every positive exposed face of \(V\) has a face-gradient pair with algebraically independent coordinates. Consequently the leading forms survive every forward and inverse shear, even when the current degree ray lies on a Newton wall. The ordinary degrees are exactly
\[
\deg(F^n)=\|u^+_n\|_\infty,\qquad
\deg(F^{-n})=\|v^-_n\|_\infty.
\]

### Exact bidirectional bridge

With
\[
c_\star=H(\mathbf1)-1,
\]
positive homogeneity gives
\[
u^+_{n+1}=c_\star Bv^-_n\qquad(n\ge0).
\]
Thus
\[
c_\star\min(e,f)\deg(F^{-n})
\le\deg(F^{n+1})
\le c_\star\max(e,f)\deg(F^{-n}),
\]
and
\[
\lambda_1(F)=\lambda_1(F^{-1}).
\]

### Selector rigidity

In the positive projective coordinate \(r=u_1/u_2\), set
\[
\Phi(r)=\max_{(x,y)\in E}(xr+y),\qquad\kappa=e/f.
\]
The forward recurrence induces
\[
\phi(r)=\kappa\frac{\Phi(r)-r}{\Phi(r)-1}.
\]
It is a strict global contraction in logarithmic distance. It has a unique fixed ray and no nontrivial numerical periodic orbit. If the fixed ray lies in a Newton chamber, the selector is eventually stationary. If it lies on a Newton wall, the fixed trajectory stays on the entire tied face while every strict trajectory alternates the two adjacent chambers and converges to the wall. Multiple ties are treated by the full face on the wall and the two extreme adjacent exponents off it.

The inverse projective map
\[
\psi(s)=\frac{\Phi(\kappa s)-\kappa s}{\Phi(\kappa s)-1}
\]
is conjugate to \(\phi\) by \(L(s)=\kappa s\).

### Arithmetic and recurrence consequences

For an interior fixed selector \((x,y)\), the relevant matrix is
\[
C_{x,y}=B
\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},
\]
so the Perron value has algebraic degree at most two. On a wall, the adjacent matrices have a common primitive positive integral ray with a common positive integer multiplier \(\mu\); the two-step Perron root is \(\mu^2\), and the per-step dynamical degree is \(\mu\). Hence throughout the class
\[
[\mathbf Q(\lambda_1(F)):\mathbf Q]\le2.
\]

For \(\xi=(x,y)\), put
\[
A_\xi=\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},
\qquad C_\xi=BA_\xi.
\]
Forward interior coordinate degrees eventually satisfy the order-at-most-two Cayley–Hamilton recurrence of \(C_\xi\). Inverse interior states use their own matrices
\[
D_\xi=A_\xi B=B^{-1}C_\xi B.
\]
If the inverse fixed ratio \(s_\star\ne1\), its visible maximum coordinate stabilizes; if \(s_\star=1\), the ordinary inverse seed is fixed from time zero and its degree sequence is geometric. In a strict wall tail, the forward and inverse parity products are treated separately. The inverse products \(N_+=D_+D_-\) and \(N_-=D_-D_+\) are similar to the corresponding forward products, have common trace and determinant, and give
\[
d^-_{n+4}=\tau d^-_{n+2}-\Delta d^-_n
\]
after parity-wise visible-coordinate stabilization. All recurrence orders are upper bounds. The exact bridge proves vector/rate comparison, not the inverse scalar recurrence.

## Why the arbitrary-face step is central

The Newton envelope alone predicts a max-plus degree vector, but it does not prove that the predicted top form survives polynomial composition. A wall is the dangerous case because several support monomials contribute at the same weight. The required coefficient-uniform certificate is:

For every positive exposed face polynomial
\[
P(X,Y)=\sum_{(x,y)\in E_u}c_{x,y}X^xY^y,
\]
choose its unique minimal-\(x\) exponent \((x_0,y_0)\). The coefficient of
\[
X^{2x_0-2}Y^{2y_0-2}
\]
in \(\det\operatorname{Hess}P\) is
\[
c_{x_0,y_0}^{\,2}x_0y_0(1-x_0-y_0)\ne0.
\]
The characteristic-zero Jacobian criterion then makes \(P_X,P_Y\) algebraically independent. This one local certificate drives the global leading-form induction in both time directions.

## Scope boundaries

The theorem does not cover:

- support points on either coordinate axis or with an exponent below two;
- zero coefficients or positive characteristic;
- a mixed momentum Hamiltonian \(W\);
- uncollected support with canceled coefficients;
- dimension at least three;
- a different phase order or an arbitrary seed in the exact bridge statement.

It also makes no assertion about:

- higher dynamical degrees, entropy equalities, compactifications, or integrability;
- periodic or arithmetic point orbits;
- classification or nonconjugacy of polynomial symplectomorphisms;
- genericity, sharpness of the support hypothesis, or minimal recurrence order;
- global literature priority.

The reason for each boundary is mathematical, not cosmetic. Axis terms can make one face-gradient coordinate vanish and destroy the two-coordinate carry. Exponent one can also destroy strict carries. Mixed \(W\) destroys the diagonal rescaling behind the decreasing map. Positive characteristic can annihilate the derivative and Hessian coefficients.

## Portfolio separation

Within the local Papers 20–25 corpus, the nearest results have different centers:

- Paper 20 treats a stationary two-mode quadratic matrix regime.
- Paper 21 treats a fixed three-mode cubic recurrence.
- Paper 22 treats arbitrary-mode cubic endpoint collapse with a common unit sector.
- Paper 23 treats a fixed four-mode quartic escape construction.
- Paper 24 treats a special two-term wall criterion, forced selector period two, and conditional finite selector words.
- Paper 25 treats support-rank bounds, stationary sharp constructions, unbounded Perron degree, and scalar minimality.

This project does not reuse those headline claims. Its center is the conjunction of arbitrary finite interior Newton support, coefficient-uniform exposed-face survival, a global projective contraction, a complete interior/wall selector classification, an exact forward–inverse bridge, and a uniform quadratic arithmetic cap. The special wall monodromy resembles Paper 24 locally, so the present theorem must foreground why contraction forbids arbitrary selector cycles and why the wall per-step value is integral.

## Strongest defensible novelty wording

Local-only wording:

> Within the audited local Papers 1–25 corpus, no prior project proves the combined statement that arbitrary finite positive interior Newton support in a planar Hamiltonian product shear yields coefficient-uniform wall-safe degree transport, globally contractive Newton-envelope selector dynamics, an exact forward–inverse degree bridge, and a uniform quadratic bound for the first dynamical degree.

This sentence is a portfolio distinction, not a global priority claim. External novelty verification is required before any submission uses “first,” “new,” or an exhaustive related-work statement.

## Deliverable test

A 22–30 page proof-first manuscript is warranted only if:

1. the arbitrary-face Hessian lemma is presented before all degree recurrences;
2. forward and inverse top-form inductions are both explicit;
3. every carry names the visible coordinate block;
4. the log contraction is uniform across the finite support and patched continuously across walls;
5. wall selector alternation is distinguished from a projective two-cycle;
6. the exact bridge proves equality of exponential rates without termwise equality or an unsupported scalar-recurrence transfer;
7. inverse scalar tails are proved from \(D_\xi=B^{-1}C_\xi B\), the \(s_\star=1\) seed case, and both strict-wall parity products;
8. the one-face quadratic and three-support wall fixtures are reproduced exactly; and
9. all excluded regimes and anti-claims remain visible.
