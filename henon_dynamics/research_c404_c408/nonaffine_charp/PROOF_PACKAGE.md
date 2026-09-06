# Two short scout lemmas, not retained paper contracts

Status: `PROVABLE_AS_STATED`; selection status: `NOT_RETAINED`. Scope and finite checks are in [SCOUT_REPORT.md](SCOUT_REPORT.md). All fields below have odd characteristic. The derivations here are elementary and do not invoke an unproved proper/affine Lefschetz substitution.

## B. Length-two Witt translation

Let p≥3 be prime, let C_p(X,U)=((X+U)^p−X^p−U^p)/p over Z and reduce its integer coefficients modulo p. The Witt addition law in length two is

\[
(x,y)+_W(u,v)=(x+u,y+v-C_p(x,u)).
\]

It follows by imposing additivity of w₀=x and w₁=xᵖ+py over Z; the resulting polynomial identities persist in characteristic p. Associativity also follows directly from the cocycle identity for C_p. Consequently S_p is translation by e=(1,0), not a non-group mechanism. Iterating the ghost equations over Z gives

\[
m e=\left(m,\frac{m-m^p}{p}\right),\qquad m\in\mathbb Z.
\]

For m=p this reduces to (0,1), and for m=p² to (0,0). Thus S_p^p(x,y)=(x,y+1) and S_p^{p²}=id. Its exact order is p². In particular, an ordinary Artin–Mazur series based on finite geometric fixed-point counts of S_p is undefined in period p².

Let q=pᵃ with a≥1, k∈Z, and F=S_p^k∘Fr_q. Witt addition is defined over F_p, so Fⁿ=S_p^{kn}∘Fr_{qⁿ}. Write Q=qⁿ and c=kn e=(c₀,c₁). The fixed equations are

\[
x^Q+c_0=x,\qquad y^Q+c_1-C_p(x^Q,c_0)=y.
\]

The first equation has Q distinct roots over the algebraic closure; for each, the second has Q distinct roots. Their derivatives in x and y are −1. Hence every n≥1 gives exactly Q² simple fixed points and

\[
Z_F(z)=\exp\left(\sum_{n\ge1}q^{2n}z^n/n\right)=(1-q^2z)^{-1}.
\]

The same calculation proves surjectivity of Fr_q−id on the Witt additive group. Choose b with Fr_q(b)−_W b=−_W(k e). Conjugation by translation τ_b then gives τ_b⁻¹Fτ_b=Fr_q. This explicit conjugacy identifies the classical ownership issue; it is stronger than a resemblance between two zeta formulas.

## C. Markov Dehn twist with Frobenius

Let q be any odd prime power, κ∈F_q\{0,4}, X_κ={x²+y²+z²−xyz=κ}, T(x,y,z)=(y,zy−x,z), and k∈Z. The inverse T⁻¹(x,y,z)=(zx−y,x,z) is polynomial. Direct substitution proves that T preserves X_κ and commutes with Fr_q. Define F=T^k∘Fr_q.

Fix n≥1, Q=qⁿ and m=kn. A fixed point of Fⁿ has z=t∈F_Q. On this fiber,

\[
C_t:\ x^2+y^2-txy=\kappa-t^2,
\qquad A_t=\begin{pmatrix}0&1\\-1&t\end{pmatrix},
\]

and the fixed equation is A_t^m(x^Q,y^Q)^T=(x,y)^T. All m∈Z are valid because det A_t=1. Put Δ=t²−4 and c=κ−t², and let χ=χ_Q, extended by χ(0)=0.

### C.1. Δc≠0

Choose λ,λ⁻¹, the roots of X²−tX+1, in F_{Q²}. Set u=x−λy and v=x−λ⁻¹y. Then uv=c and T acts by (u,v)↦(λu,λ⁻¹v).

If χ(Δ)=1, λ∈F_Q; the fixed equation on u∈G_m is u=λ^m u^Q. It has Q−1 distinct solutions, and v=c/u is determined. If χ(Δ)=−1, λ^Q=λ⁻¹; Frobenius exchanges the two eigen-coordinates. The equations become u=λ^m v^Q and v=λ⁻m u^Q. Eliminating v yields u^{Q+1}=λ^m c, with Q+1 distinct solutions; the second equation then holds automatically. This fiber therefore contributes Q−χ(Δ), independently of m.

### C.2. c=0 (necessarily Δ≠0)

The fiber uv=0 consists of two lines meeting at the origin. In the split case, each preserved line has Q fixed points and the origin is counted twice, giving 2Q−1. In the nonsplit case Frobenius interchanges the lines, so only the origin can be fixed. The contribution is Q+(Q−1)χ(Δ), i.e. the generic expression Q−χ(Δ) plus the correction Qχ(Δ).

### C.3. t=2 and t=−2

Set ε_Q=χ_Q(κ−4), which is nonzero. At t=2 the two disjoint lines are (x−y)²=κ−4. T preserves δ=x−y. The Frobenius-twisted map preserves both branches precisely when ε_Q=1. On a preserved affine line it has form X↦X^Q+b, with Q fixed points; if it exchanges the branches there are none. The total is Q(1+ε_Q).

At t=−2 the two lines are (x+y)²=κ−4. T sends δ=x+y to −δ. The branches are preserved precisely when (−1)^m ε_Q=1; on a preserved line the fixed equation is aX^Q+b=X with a=(−1)^m≠0, again with Q distinct roots. The contribution is Q(1+(−1)^m ε_Q).

### C.4. Summation and reducedness

The identity Σ_{t∈F_Q}χ(t²−4)=−1 follows by counting u²=t²−4: the equation (t−u)(t+u)=4 has Q−1 solutions because 2 and 4 are invertible, whereas the character sum count is Q+Σχ(t²−4). Thus the sum of generic expressions Q−χ(Δ) over all t is Q²+1.

The t=±2 corrections sum to Qε_Q(1+(−1)^m). There are 1+χ_Q(κ) roots of t²=κ in F_Q; their Δ is κ−4, so their correction is Qε_Q(1+χ_Q(κ)). These sets are disjoint since κ∉{0,4}. Therefore

\[
N_n=Q^2+1+Q\varepsilon_Q\bigl(2+(-1)^m+\chi_Q(\kappa)\bigr).
\]

For a∈F_q^× one has χ_{qⁿ}(a)=χ_q(a)ⁿ. Writing ε=χ_q(κ−4), η=χ_q(κ) and m=kn gives

\[
N_n=q^{2n}+1+2(q\varepsilon)^n+
\bigl(q(-1)^k\varepsilon\bigr)^n+(q\varepsilon\eta)^n.
\]

These are counts with no multiplicity. To justify that independently of the fiber presentation, the ambient three fixed equations have Jacobian −I because dFr_Q=0. They have finite support: z has Q choices and on each such fiber the two equations have invertible Q-degree leading coefficient matrix A_t^m. The ambient fixed scheme is therefore finite étale; intersecting it with X_κ gives a quotient of a finite product of algebraically closed fields, hence is reduced. The Gröbner quotient lengths in the finite probe accordingly equal geometric fixed-point counts.

Exponentiating the displayed power-sum formula as a formal series over Q gives

\[
Z_F(z)^{-1}=(1-q^2z)(1-z)(1-q\varepsilon z)^2
\bigl(1-q(-1)^k\varepsilon z\bigr)(1-q\varepsilon\eta z).
\]

This proves precisely the declared family, including every n, every negative or nonnegative k, and all its exceptional conic fibers. It proves nothing about κ=0,4, characteristic 2, hyperbolic words replacing T, or ordinary untwisted hyperbolic periodic-point counts. The assumptions have not been weakened on the basis of the finite checks.
