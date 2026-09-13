# Final proof-first proposal

## Frozen identity

Title: Newton-Envelope Contraction for Planar Hamiltonian Product Shears: Selector Rigidity and Bidirectional Degree Growth

Candidate identifier: planar_newton_envelope_bidirectional_degree_v1

## One-sentence contribution

For planar Hamiltonian product shears with arbitrary finite collected support in \(\mathbf Z_{\ge2}^{2}\) and separated pure-power momentum Hamiltonian, prove coefficient-uniform wall-safe degree transport, global Newton-envelope log contraction, an exhaustive interior/wall selector tail, and an exact forward–inverse bridge, yielding a uniform quadratic bound for the first dynamical degree and an integer value on walls.

## Problem anchor

Tropical degree calculations for polynomial compositions are only predictions until top-form cancellation is excluded. The difficulty is concentrated on exposed Newton faces, where several monomials tie. Once exactness is established, the resulting recurrence is nonlinear and piecewise integral; a priori it could switch selectors indefinitely. Finally, forward and inverse compositions place the same two nonlinear operations in opposite orders.

The proposal resolves these three issues in one chain:

\[
\text{face Hessian}
\Longrightarrow
\text{leading-form independence}
\Longrightarrow
\text{exact degree transports}
\Longrightarrow
\text{projective contraction}
\Longrightarrow
\text{selector and spectral rigidity},
\]
with positive homogeneity supplying an exact bridge between the two time directions.

## Final assumptions

- \(K\) has characteristic zero.
- \(E\subset\mathbf Z_{\ge2}^{2}\) is finite and nonempty.
- Support coefficients are collected and all nonzero.
- \(V(q)=\sum_Ec_{x,y}q_1^xq_2^y\).
- \(W(p)=\alpha p_1^{e+1}+\beta p_2^{f+1}\), with \(e,f\ge2\) and \(\alpha\beta\ne0\).
- \(F=T\circ S\), where \(S\) is the lower \(V\)-shear and \(T\) the upper \(W\)-shear.
- Ordinary total degree and the ordinary coordinate seed \(\mathbf1\) are used.

Every assumption has a named proof role. No genericity or sign condition on the nonzero coefficients is used.

## Main theorem package

### Structural part

The shears are polynomial symplectomorphisms because their Jacobian error blocks are the skew parts of Hessians. Their inverses are subtraction shears in reverse phase order.

### Cancellation part

For every positive exposed face polynomial \(P\), the unique minimal-\(x\) face point \((x_0,y_0)\) produces the uncancellable coefficient
\[
c_{x_0,y_0}^{\,2}x_0y_0(1-x_0-y_0)
\]
in \(\det\operatorname{Hess}P\). The determinant is nonzero. The characteristic-zero Jacobian criterion makes \(P_X,P_Y\) algebraically independent. Injective substitution and separated pure powers propagate independence through every forward and inverse half-step.

### Exact degree part

With
\[
H(u)=\max_E(xu_1+yu_2),\qquad
\mathcal A(u)=(H(u)-u_1,H(u)-u_2)^\top,
\]
and \(B=\operatorname{diag}(e,f)\), the exact states are
\[
u^+_{n+1}=B\mathcal A(u^+_n),\qquad
v^-_{n+1}=\mathcal A(Bv^-_n).
\]
Strict carry inequalities show that the final position block is visible forward and the final momentum block is visible backward:
\[
\deg(F^n)=\|u^+_n\|_\infty,\qquad
\deg(F^{-n})=\|v^-_n\|_\infty.
\]

### Bidirectional part

For \(c_\star=H(\mathbf1)-1\),
\[
u^+_{n+1}=c_\star Bv^-_n.
\]
This gives two-sided constant-factor degree comparison and
\[
\lambda_1(F)=\lambda_1(F^{-1}).
\]
The exact vector identity, rather than abstract invertibility, is the contribution.

### Projective part

The forward ratio map
\[
\phi(r)=\frac ef\frac{\Phi(r)-r}{\Phi(r)-1},
\qquad
\Phi(r)=\max_E(xr+y),
\]
has chamberwise logarithmic slope
\[
\eta_{x,y}(r)
=
\frac{r(x+y-1)}
{((x-1)r+y)(xr+y-1)}.
\]
Its denominator exceeds its numerator by
\[
x(x-1)r^2+2(x-1)(y-1)r+y(y-1)>0.
\]
For each finite branch, compactification at zero and infinity makes the supremum strictly below one. A finite maximum gives one global constant; continuity and interval splitting pass it across Newton walls.

The inverse ratio map
\[
\psi(s)=\frac{\Phi((e/f)s)-(e/f)s}{\Phi((e/f)s)-1}
\]
is conjugate to \(\phi\) by \(L(s)=(e/f)s\).

### Selector and arithmetic part

The contraction has one fixed ray and no nontrivial numerical periodic orbit.

- Interior fixed ray: eventually one selector matrix \(C_{x,y}\) acts, so \(\lambda_1\) is quadratic over \(\mathbf Q\) at worst.
- Wall fixed ray: a strict orbit alternates adjacent selectors while converging; a wall orbit uses the entire tied face. The adjacent integral matrices share a primitive rational ray and one positive integer multiplier \(\mu\), so the two-step Perron root is \(\mu^2\) and \(\lambda_1=\mu\).

Thus
\[
[\mathbf Q(\lambda_1(F)):\mathbf Q]\le2.
\]

### Recurrence part

For \(\xi=(x,y)\), write
\[
A_\xi=\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},
\qquad C_\xi=BA_\xi.
\]
Forward interior coordinate tails use \(C_\xi\), while inverse interior tails use
\[
D_\xi=A_\xi B=B^{-1}C_\xi B.
\]
Cayley–Hamilton and eventual visible-coordinate stabilization give scalar degree recurrences of order at most two. The inverse proof separately treats \(s_\star\ne1\) and the ordinary fixed-seed case \(s_\star=1\), where the degree sequence is geometric.

In a strict wall tail, the two forward parity products \(M_+=C_+C_-\), \(M_-=C_-C_+\) and the two inverse products \(N_+=D_+D_-\), \(N_-=D_-D_+\) satisfy
\[
N_\pm=B^{-1}M_\pm B.
\]
They have one common trace \(\tau\) and determinant \(\Delta\). After the inverse visible maximum stabilizes on each parity,
\[
d^-_{n+4}=\tau d^-_{n+2}-\Delta d^-_n.
\]
Thus the forward and inverse scalar degree tails have order at most two in an interior regime and at most four in a strict wall regime. These are upper bounds. The exact bridge supplies vector and exponential-rate comparison, but it is not the scalar-recurrence proof.

## Exact fixtures

### Interior quadratic witness

\[
E=\{(2,2)\},\quad B=\operatorname{diag}(3,2),\quad
C=\begin{pmatrix}3&6\\4&2\end{pmatrix}.
\]
Then
\[
\lambda_1=\frac{5+\sqrt{97}}2.
\]
The small-index bridge check is
\[
u^+_1=(9,6),\quad v^-_1=(7,8),\quad
u^+_2=(63,48)=3Bv^-_1.
\]

### Transient wall witness

\[
E=\{(2,8),(4,5),(5,3)\},\qquad
B=\operatorname{diag}(24,11).
\]
The walls are \(3/2\) and \(2\), and the selector prefix is
\[
\text{low},\text{ high},\text{ middle},\text{ high},\ldots
\]
with
\[
r_1=24/11,\quad r_2=1548/781,\quad
r_3=51294/25619.
\]
Middle and high selectors share \(w=(2,1)\) with multiplier \(132\). Their monodromy has trace \(17648\), determinant \(3902976\), and eigenvalues \(17424=132^2\) and \(224\).

## Planned 26-page proof architecture

The allocation below counts mathematical content pages and excludes references.

| Component | Pages | Mathematical purpose |
|---|---:|---|
| Abstract | 0.5 | State the exact map class, contraction, bridge, and quadratic cap. |
| 1. Introduction and local positioning | 2.5 | Explain the cancellation/projectivization/bidirectionality problem without global priority language. |
| 2. Setup, symplecticity, and inverse phases | 2.5 | Freeze assumptions, maps, degrees, and block notation. |
| 3. Exposed-face Hessian and algebraic independence | 4.0 | Prove the minimal-\(x\) coefficient and substitution lemmas. |
| 4. Forward/inverse top forms, carries, and bridge | 4.5 | Establish exact recurrences, visibility, and rate equality. |
| 5. Projective formulas and uniform log contraction | 4.0 | Derive branch slopes, uniformity, wall patching, and inverse conjugacy. |
| 6. Selector-tail classification | 2.5 | Interior, wall, multiple tie, injectivity, and no-cycle statements. |
| 7. Spectra and degree recurrences | 3.0 | Quadratic interior, integer wall, and Cayley–Hamilton laws. |
| 8. Fixtures, boundaries, and conclusion | 2.5 | Exact examples, failed extensions, and theorem scope. |
| Total | 26.0 | Proof-first body |

The face-Hessian and bidirectional induction sections must not be compressed into appendices; they are the theorem's validity core.

## Exposition rules

1. State the full map and all support restrictions before the headline theorem.
2. Use “exposed face” on a tie; never replace it with “chosen monomial.”
3. Distinguish coordinate-degree vectors from the total degree of the four-coordinate map.
4. Name the visible block after every half-step.
5. State the bridge with its shift and ordinary-seed hypothesis every time it is used.
6. Use “selector alternation converging to a fixed wall ray,” never “projective two-cycle.”
7. State recurrence orders as upper bounds.
8. Put excluded cases next to the theorem, not only in a closing discussion.
9. Keep bibliography comparisons contextual until external novelty verification is complete.

## Local portfolio position

The closest local collision is Paper 24's special two-term wall monodromy. The final proposal separates itself by proving a global contraction for arbitrary finite interior support, using the full wall face, excluding nontrivial ratio cycles, and coupling the tail to inverse growth.

The next closest collision is Paper 25's support-rank and unbounded Perron-degree program. The final proposal concerns a narrower planar separated family and proves rigidity: the arbitrary number of planar support points does not increase the Perron algebraic degree beyond two.

The theorem should not claim novelty for \(2\times2\) Perron formulas, Cayley–Hamilton, or two-step monodromy in isolation.

## Literature boundary

The current citation ledger reuses locally frozen primary metadata for algebraic entropy, cluster and tropical recurrences, polynomial symplectomorphisms, triangular polynomial automorphisms, and spectral dynamical-degree context. These sources are not proof dependencies. A later external claim-level search must verify whether the exact conjunction of arbitrary-face survival, global envelope contraction, and a bidirectional bridge already appears.

## Success and kill criteria

The proposal succeeds if a reader can derive every claimed degree from the displayed polynomial leading forms and can reconstruct both fixtures by hand.

It is killed by:

- one in-scope face with zero Hessian determinant;
- one in-scope wall cancellation;
- failure of a support-uniform contraction constant;
- an unclassified in-scope selector tail;
- an in-scope Perron value of degree above two;
- or a primary source proving the same combined theorem.

The source-design proof audit finds no mathematical killer. The external novelty condition remains deliberately unresolved.
