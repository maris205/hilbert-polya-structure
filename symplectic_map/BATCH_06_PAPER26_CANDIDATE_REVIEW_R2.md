# Batch 06 Paper 26 Candidate Review R2

## 1. Review role, frozen scope, and verdict

This is an independent proof-adversarial review of the frozen Paper 26
candidate. The candidate is the following two-dimensional Hamiltonian
product-shear family over a field \(K\) of characteristic zero:

\[
V(q_1,q_2)=\sum_{(x,y)\in E}c_{x,y}q_1^xq_2^y,
\qquad
\varnothing\ne E\subset \mathbf Z_{\ge 2}^2,
\qquad c_{x,y}\in K^\times,
\]

\[
W(p_1,p_2)=\alpha p_1^{e+1}+\beta p_2^{f+1},
\qquad e,f\ge2,
\qquad \alpha,\beta\in K^\times,
\]

\[
S(q,p)=(q,p+\nabla V(q)),
\qquad
T(q,p)=(q+\nabla W(p),p),
\qquad
F=T\circ S.
\]

The review recomputes the support-face algebra, forward and inverse degree
transport, projective contraction, selector-tail classification, spectral
degree, and scalar recurrences. The main conclusion survives, but one
coarse preliminary bound must be strengthened: there is no numerical
projective two-cycle. The logarithmic projective map is a uniform strict
contraction. Consequently the first dynamical degree has algebraic degree
at most two, not merely at most four. When the unique fixed ray is a support
wall, the dynamical degree is in fact a positive integer.

The proof-completeness score is **9.6/10**. The candidate passes after the
precise theorem and nonclaims recorded below are used.

## 2. Literal coordinates, inverses, and symplecticity

The first shear is

\[
\widehat p_1
=p_1+\sum_{(x,y)\in E}x c_{x,y}q_1^{x-1}q_2^y,
\]

\[
\widehat p_2
=p_2+\sum_{(x,y)\in E}y c_{x,y}q_1^xq_2^{y-1}.
\]

The second shear is

\[
q_1'=q_1+(e+1)\alpha\widehat p_1^e,
\qquad
q_2'=q_2+(f+1)\beta\widehat p_2^f,
\qquad
p'=\widehat p.
\]

All displayed derivative scalars are nonzero because \(K\) has
characteristic zero. The inverses are the subtraction shears

\[
S^{-1}(q,p)=(q,p-\nabla V(q)),
\qquad
T^{-1}(q,p)=(q-\nabla W(p),p),
\]

and

\[
F^{-1}=S^{-1}\circ T^{-1}.
\]

Writing \(H_V=\nabla^2V\) and \(H_W=\nabla^2W\), the two Jacobian blocks are

\[
J_S=\begin{pmatrix}I&0\\H_V&I\end{pmatrix},
\qquad
J_T=\begin{pmatrix}I&H_W\\0&I\end{pmatrix}.
\]

Both Hessians are symmetric. Direct multiplication against

\[
\Omega=\begin{pmatrix}0&I\\-I&0\end{pmatrix}
\]

gives \(J_S^{\mathsf T}\Omega J_S=\Omega\) and
\(J_T^{\mathsf T}\Omega J_T=\Omega\). Hence \(S,T,F\) are polynomial
symplectomorphisms. This calculation is independent of the later degree
argument.

## 3. The support-face map

For a positive degree vector \(u=(u_1,u_2)^{\mathsf T}\), define

\[
H(u)=\max_{(x,y)\in E}(xu_1+yu_2)
\]

and

\[
\mathcal A(u)=
\begin{pmatrix}H(u)-u_1\\H(u)-u_2\end{pmatrix}.
\]

Every monomial of \(V\) contains both variables. Subtracting \(u_1\) from
all first-derivative scores and \(u_2\) from all second-derivative scores
does not change the maximizing face. Thus the same exposed face controls
both gradient coordinates, including at a tie.

For a single selected exponent \(\xi=(x,y)\), the corresponding linear
matrix is

\[
A_\xi=
\begin{pmatrix}
x-1&y\\
x&y-1
\end{pmatrix},
\qquad
\mathcal A(u)=A_\xi u
\]

whenever \(\xi\) is active. If several exponents tie, all tied matrices
have the same value on that particular ray because their total scores are
equal.

Since \(x,y\ge2\), for every \(u>0\),

\[
H(u)\ge2u_1+2u_2,
\]

and hence

\[
\mathcal A_1(u)\ge u_1+2u_2>u_1,
\qquad
\mathcal A_2(u)\ge2u_1+u_2>u_2.
\tag{3.1}
\]

This strict componentwise expansion is the source of both carry proofs.

## 4. Extreme-term Hessian certificate

The central noncancellation issue is a support wall, where several monomials
have the same weighted degree. Let

\[
P(X,Y)=\sum_{(x,y)\in E_0}c_{x,y}X^xY^y
\]

be any nonempty exposed-face polynomial, where all points of \(E_0\) lie on
one line

\[
x u_1+y u_2=H
\]

with \(u_1,u_2>0\). Choose the point \((x_0,y_0)\in E_0\) with minimal
\(x_0\). It is unique: two tied points with the same \(x\) must have the
same \(y\), and the support has already been collected.

Consider

\[
\det\nabla^2P=P_{XX}P_{YY}-P_{XY}^2.
\]

The coefficient of

\[
X^{2x_0-2}Y^{2y_0-2}
\]

can only come from pairing \((x_0,y_0)\) with itself. Indeed, any
contributing ordered pair must have first-coordinate sum \(2x_0\), while
both first coordinates are at least \(x_0\). Both must therefore equal
\(x_0\), and uniqueness then fixes both second coordinates as \(y_0\).

The coefficient in \(P_{XX}P_{YY}\) is

\[
c_{x_0,y_0}^2x_0(x_0-1)y_0(y_0-1),
\]

whereas the coefficient in \(P_{XY}^2\) is

\[
c_{x_0,y_0}^2x_0^2y_0^2.
\]

Their difference is exactly

\[
\boxed{
c_{x_0,y_0}^2x_0y_0(1-x_0-y_0).}
\tag{4.1}
\]

It is nonzero in characteristic zero because \(c_{x_0,y_0}\ne0\) and
\(x_0,y_0\ge2\). Therefore

\[
\det\nabla^2P\not\equiv0.
\tag{4.2}
\]

By the characteristic-zero Jacobian criterion, \(P_X\) and \(P_Y\) are
algebraically independent. For completeness, if a nonzero relation
\(R(P_X,P_Y)=0\) existed, differentiating it would make the row
\((R_1(P_X,P_Y),R_2(P_X,P_Y))\) annihilate the Hessian. Over the fraction
field the Hessian is invertible by (4.2), so both substituted partials would
vanish. Taking an irreducible relation of minimal degree and using
characteristic zero rules this out. This is the standard two-variable
Jacobian-criterion implication.

Thus every exposed face, including a multi-monomial wall face, has a
gradient pair that is algebraically independent.

## 5. Highest-form substitution and noncancellation

Let \(Q_1,Q_2\) be polynomials of respective ordinary degrees \(u_1,u_2\),
and let \(L_1,L_2\) be their highest homogeneous forms. Assume \(L_1,L_2\)
are algebraically independent. Substitution

\[
K[X,Y]\longrightarrow K[\text{initial variables}],
\qquad X\mapsto L_1,\quad Y\mapsto L_2,
\]

is then injective.

If \(P\) is the face polynomial selected by \(u\), the highest forms of the
two gradient coordinates are

\[
P_X(L_1,L_2),
\qquad
P_Y(L_1,L_2).
\]

They are nonzero by injectivity. They are also algebraically independent:
\(P_X,P_Y\) are algebraically independent by Section 4, and composing two
injective polynomial-algebra embeddings preserves algebraic independence.

The pure-power phase sends an algebraically independent pair
\((M_1,M_2)\) to \((M_1^e,M_2^f)\), which remains algebraically independent.
Nonzero scalar multiples and the subtraction signs in \(F^{-1}\) do not
change that fact.

Starting with the coordinate variables, this proves inductively that the
highest homogeneous form pair is algebraically independent at every
forward and inverse phase. Consequently:

1. tied face terms cannot erase an entire predicted highest form;
2. arbitrary nonzero coefficient signs are allowed;
3. the subtraction signs in inverse iteration do not create a hidden degree
   drop; and
4. the tropical vectors below are exact ordinary coordinate-degree vectors,
   not upper bounds.

No positivity-semiring argument is needed.

## 6. Exact forward transport and both forward carries

Put

\[
B=\operatorname{diag}(e,f).
\]

Let \(u_n^+\) be the two-vector of position-coordinate degrees after
\(F^n\), and let \(w_n^+\) be the momentum-degree vector at the same full
phase. At \(n=0\), both equal \(\mathbf1=(1,1)^{\mathsf T}\).

At the first \(S\)-phase, (3.1) gives

\[
w_1^+=\mathcal A(u_0^+)>u_0^+=w_0^+,
\]

so the fresh gradient strictly defeats the carried momentum coordinates.
The \(T\)-phase then gives

\[
u_1^+=Bw_1^+>u_0^+,
\]

because \(B\ge2I\).

Inductively, suppose

\[
w_n^+=\mathcal A(u_{n-1}^+),
\qquad
u_n^+=Bw_n^+.
\]

Then \(u_n^+>w_n^+\), and (3.1) gives

\[
\mathcal A(u_n^+)>u_n^+>w_n^+.
\]

This is the next first-phase carry inequality. The second phase satisfies

\[
B\mathcal A(u_n^+)\ge2\mathcal A(u_n^+)>u_n^+,
\]

which is the next second-phase carry inequality. Therefore, for every
\(n\ge0\),

\[
\boxed{
w_{n+1}^+=\mathcal A(u_n^+),
\qquad
u_{n+1}^+=B\mathcal A(u_n^+).}
\tag{6.1}
\]

Moreover \(u_n^+>w_n^+\) componentwise for every \(n\ge1\). Hence the
total degree is visible in the position block:

\[
\boxed{
\deg(F^n)=\lVert u_n^+\rVert_\infty.}
\tag{6.2}
\]

## 7. Exact inverse transport and both inverse carries

For \(F^{-1}=S^{-1}\circ T^{-1}\), let \(v_n^-\) be the momentum-degree
vector after \(F^{-n}\), and let \(z_n^-\) be the position-degree vector at
the same full phase. Initially both are \(\mathbf1\).

The first \(T^{-1}\)-phase has pure fresh degrees \(Bv_0^->z_0^-\), because
\(e,f\ge2\). Its highest forms are nonzero pure powers of independent
momentum variables. The following \(S^{-1}\)-phase has degrees

\[
\mathcal A(Bv_0^-)>Bv_0^->v_0^-.
\]

At a later full inverse phase, suppose

\[
z_n^-=Bv_{n-1}^-,
\qquad
v_n^-=\mathcal A(z_n^-)>z_n^-.
\]

Then the next \(T^{-1}\)-fresh degrees satisfy

\[
Bv_n^-\ge2v_n^->z_n^-,
\]

and the next \(S^{-1}\)-fresh degrees satisfy

\[
\mathcal A(Bv_n^-)>Bv_n^->v_n^-.
\]

Thus both inverse carries close, and

\[
\boxed{
z_{n+1}^-=Bv_n^-,
\qquad
v_{n+1}^-=\mathcal A(Bv_n^-).}
\tag{7.1}
\]

The momentum block strictly dominates the position block at every nonzero
inverse time. Therefore

\[
\boxed{
\deg(F^{-n})=\lVert v_n^-\rVert_\infty.}
\tag{7.2}
\]

## 8. Shifted forward-inverse vector identity

The map \(\mathcal A\) is positively homogeneous. Put

\[
c_0=H(\mathbf1)-1
=\max_{(x,y)\in E}(x+y)-1.
\]

Then

\[
\mathcal A(\mathbf1)=c_0\mathbf1
\]

and the first forward vector is

\[
u_1^+=c_0B\mathbf1=c_0Bv_0^-.
\]

If \(u_{n+1}^+=c_0Bv_n^-\), homogeneity and (6.1)--(7.1) give

\[
\begin{aligned}
u_{n+2}^+
&=B\mathcal A(u_{n+1}^+)\\
&=B\mathcal A(c_0Bv_n^-)\\
&=c_0B\mathcal A(Bv_n^-)\\
&=c_0Bv_{n+1}^-.
\end{aligned}
\]

Hence

\[
\boxed{
u_{n+1}^+=c_0Bv_n^-
\qquad(n\ge0).}
\tag{8.1}
\]

Using (6.2), (7.2), and the elementary diagonal-norm comparison gives

\[
\boxed{
c_0\min(e,f)\deg(F^{-n})
\le \deg(F^{n+1})
\le c_0\max(e,f)\deg(F^{-n}).}
\tag{8.2}
\]

The existence of each exponential degree limit also follows below from the
eventual matrix law; alternatively it follows from submultiplicativity of
degrees. Taking roots in (8.2), with the one-step shift harmless, yields

\[
\boxed{
\lambda_1(F)=\lambda_1(F^{-1}).}
\tag{8.3}
\]

This equality is a theorem of the displayed support architecture. It is not
being inferred from symplecticity alone.

## 9. Forward and inverse projective maps

For \(r=u_1/u_2>0\), define

\[
\Phi(r)=\max_{(x,y)\in E}(xr+y),
\qquad
\kappa=\frac ef.
\]

Equations (6.1) give the forward ratio map

\[
\boxed{
\varphi(r)=
\kappa\frac{\Phi(r)-r}{\Phi(r)-1}.}
\tag{9.1}
\]

For \(s=v_1/v_2\), equations (7.1) give the inverse momentum-ratio map

\[
\boxed{
\psi(s)=
\frac{\Phi(\kappa s)-\kappa s}
     {\Phi(\kappa s)-1}.}
\tag{9.2}
\]

With \(L(s)=\kappa s\), direct substitution gives

\[
\boxed{L\circ\psi=\varphi\circ L.}
\tag{9.3}
\]

At the ordinary forward seed \(r_0^+=1\), numerator and denominator in
(9.1) agree before multiplication by \(\kappa\). Hence

\[
r_1^+=\kappa=L(s_0^-).
\]

The conjugacy then gives

\[
\boxed{r_{n+1}^+=L(s_n^-)}
\]

for all \(n\ge0\), consistently with the stronger vector identity (8.1).

## 10. Strict decrease and the exact logarithmic derivative

On a chamber where \((x,y)\) is active, put

\[
N=(x-1)r+y,
\qquad
D=xr+y-1.
\]

Then

\[
\varphi(r)=\kappa\frac ND
\]

and

\[
\varphi'(r)
=-\kappa\frac{x+y-1}{D^2}<0.
\tag{10.1}
\]

At a support wall, the competing affine functions have the same value
\(\Phi(r)\), so formula (9.1) has the same value from either side. Thus
\(\varphi\) is continuous and strictly decreasing on all of
\((0,\infty)\).

The absolute logarithmic derivative is

\[
\boxed{
\eta_{x,y}(r)
=\left|\frac{d\log\varphi(r)}{d\log r}\right|
=\frac{r(x+y-1)}{((x-1)r+y)(xr+y-1)}.}
\tag{10.2}
\]

The denominator exceeds the numerator by

\[
\begin{aligned}
ND-r(x+y-1)
={}&x(x-1)r^2\\
&+2(x-1)(y-1)r\\
&+y(y-1),
\end{aligned}
\tag{10.3}
\]

which is strictly positive for \(r>0\) and \(x,y\ge2\). Therefore

\[
0<\eta_{x,y}(r)<1.
\tag{10.4}
\]

This pointwise inequality must be upgraded to a uniform one; otherwise a
contraction claim would be incomplete. For each fixed support exponent,
\(\eta_{x,y}\) is continuous on \((0,\infty)\) and tends to zero as
\(r\to0\) or \(r\to\infty\). It therefore extends continuously by zero to
the two-point compactification and attains a maximum strictly below one.
Because \(E\) is finite, there is a common constant

\[
q_E=\max_{(x,y)\in E}\sup_{r>0}\eta_{x,y}(r)<1.
\tag{10.5}
\]

Let

\[
h(t)=\log\varphi(e^t).
\]

The function \(h\) is continuous and piecewise differentiable, with only
finitely many support-wall breakpoints and

\[
|h'(t)|\le q_E
\]

on every differentiability interval. Splitting any segment at those
finitely many breakpoints and applying the mean-value estimate on each piece
gives

\[
\boxed{|h(t)-h(s)|\le q_E|t-s|.}
\tag{10.6}
\]

Thus \(h:\mathbb R\to\mathbb R\) is a global strict contraction.

As a separate range check, on every branch

\[
2N-D=(x-2)r+y+1>0,
\]

and

\[
2D-N=(x+1)r+y-2>0.
\]

Therefore

\[
\frac12<\frac ND<2,
\qquad
\varphi((0,\infty))\subset
\left(\frac\kappa2,2\kappa\right).
\tag{10.7}
\]

The compact-range check agrees with, but is weaker than, the global
logarithmic contraction.

## 11. Unique fixed ray and selector-tail dichotomy

Banach's fixed-point theorem applied to (10.6) gives one and only one fixed
logarithmic ratio \(t_*\), equivalently one and only one positive fixed ray

\[
r_*=e^{t_*},
\qquad
\varphi(r_*)=r_*.
\]

Every ratio orbit converges geometrically to \(r_*\). In particular, a
nontrivial numerical projective two-cycle is impossible. This eliminates
the source of the earlier coarse quartic bound.

Because \(\varphi\) is strictly decreasing,

\[
r<r_*\Longrightarrow \varphi(r)>r_*,
\qquad
r>r_*\Longrightarrow \varphi(r)<r_*.
\tag{11.1}
\]

Unless the orbit starts on the fixed ray, it alternates sides of \(r_*\)
while its logarithmic distance contracts.

There are exactly two tail geometries.

### 11.1 Interior fixed ray

If \(r_*\) lies in the interior of one support chamber, a sufficiently small
neighborhood of \(r_*\) has one active exponent \(\xi\). Every orbit
eventually remains in that neighborhood. The selector is therefore
stationary and

\[
u_{n+1}^+=C_\xi u_n^+,
\qquad
C_\xi=BA_\xi,
\]

for all sufficiently large \(n\).

### 11.2 Wall fixed ray

If \(r_*\) is a support wall, the upper envelope \(\Phi\) has one exposed
affine piece immediately to the left and one immediately to the right.
There may be additional monomials tied exactly at the vertex, but they do not
create additional nearby chambers. An orbit not on the wall eventually
alternates between the two adjacent exposed faces. If it lands on the wall,
it remains there.

Strict injectivity rules out a delayed first landing. If
\(\varphi^N(1)=r_*\), then injectivity and
\(\varphi(r_*)=r_*\) imply successively
\(\varphi^{N-1}(1)=r_*,\ldots,1=r_*\). Thus for the ordinary seed the only
fixed-wall landing case is \(r_*=1\), when the seed was fixed from the
beginning. Otherwise the adjacent selector faces alternate forever while
the numerical ratios converge to the wall.

This is selector alternation, not a numerical ratio two-cycle.

## 12. Spectral conclusion in an interior chamber

For \(\xi=(x,y)\),

\[
C_\xi=
\begin{pmatrix}
e(x-1)&ey\\
fx&f(y-1)
\end{pmatrix}.
\tag{12.1}
\]

It is a strictly positive integer matrix. Its fixed projective ray is its
positive Perron ray, so the asymptotic degree multiplier is

\[
\lambda_1(F)=\rho(C_\xi).
\]

The characteristic polynomial is

\[
t^2-\operatorname{tr}(C_\xi)t+\det(C_\xi),
\]

where

\[
\det(C_\xi)=ef(1-x-y)<0.
\]

Consequently

\[
\boxed{[\mathbb Q(\lambda_1(F)):\mathbb Q]\le2}
\tag{12.2}
\]

in the interior case. The inverse map has the same multiplier by (8.3), or
equivalently because \(A_\xi B\) is similar to \(BA_\xi\) through the
invertible diagonal matrix \(B\).

## 13. Wall matrices share an integer Perron multiplier

Let \(\xi_-=(x_-,y_-)\) and \(\xi_+=(x_+,y_+)\) be the adjacent exposed
faces at a fixed wall \(r_*\). Distinct adjacent affine functions cannot
have the same slope, so \(x_-\ne x_+\), and the wall equation gives

\[
r_*=
\frac{y_+-y_-}{x_--x_+}\in\mathbb Q_{>0}.
\tag{13.1}
\]

Put \(v_*=(r_*,1)^{\mathsf T}\). The wall condition says

\[
x_-r_*+y_-=x_+r_*+y_+=\Phi(r_*).
\]

The fixed-ray equation gives, for either adjacent face,

\[
C_{\xi_\pm}v_*=\mu v_*,
\]

where the second coordinate yields the common value

\[
\mu=f(\Phi(r_*)-1).
\tag{13.2}
\]

Thus both positive integer matrices share the same positive rational
eigenvector and the same eigenvalue. The number \(\mu\) is rational by
(13.1)--(13.2). It is also an eigenvalue of a monic integer characteristic
polynomial, hence an algebraic integer. A rational algebraic integer is an
integer, so

\[
\boxed{\mu\in\mathbb Z_{>0}.}
\tag{13.3}
\]

Because \(v_*>0\), Perron--Frobenius identifies \(\mu\) as the Perron root
of each adjacent matrix.

If the selector alternates, the two-step monodromy is, according to parity,

\[
M_+=C_{\xi_+}C_{\xi_-}
\quad\text{or}\quad
M_-=C_{\xi_-}C_{\xi_+}.
\]

Both are positive and satisfy

\[
M_\pm v_*=\mu^2v_*.
\]

Thus their Perron root is \(\mu^2\), and the per-step dynamical degree is

\[
\boxed{\lambda_1(F)=\mu\in\mathbb Z_{>0}.}
\tag{13.4}
\]

This explicitly closes the apparent square-root loophole. The two-step
Perron root is a perfect square because the adjacent matrices already share
their positive eigenline and eigenvalue.

Combining Sections 12 and 13 gives the uniform theorem

\[
\boxed{[\mathbb Q(\lambda_1(F)):\mathbb Q]\le2.}
\tag{13.5}
\]

## 14. Eventual recurrences

The recurrence statement must distinguish stationary interior selection from
wall alternation.

### 14.1 Interior tail

Once the selector is the fixed face \(\xi\), Cayley--Hamilton gives the vector
recurrence

\[
u_{n+2}^+
=\operatorname{tr}(C_\xi)u_{n+1}^+
-\det(C_\xi)u_n^+.
\tag{14.1}
\]

If \(r_*\ne1\), one position coordinate is eventually strictly larger than
the other, so the total degree is that fixed coordinate and satisfies the
same eventual second-order recurrence.

If \(r_*=1\), the ordinary seed already equals the unique fixed ray. It is
fixed from the first step rather than alternating around itself, and the
degree sequence is geometric. Thus no special fourth-order visibility
claim is needed at \(r_*=1\).

### 14.2 Wall-alternating tail

Assume \(r_*\ne1\), so the ordinary seed is not fixed. Both parity ratios
eventually lie on the same side of the coordinate-visibility wall \(r=1\),
because they converge to \(r_*\ne1\). Hence one position coordinate is the
total-degree coordinate on the entire tail.

The two monodromies \(M_+\) and \(M_-\) have the same trace and determinant:
the equality of traces follows from
\(\operatorname{tr}(AB)=\operatorname{tr}(BA)\), and their determinants are
the same product. Put

\[
\tau=\operatorname{tr}(M_+)=\operatorname{tr}(M_-),
\qquad
\Delta=\det(M_+)=\det(M_-).
\]

Cayley--Hamilton on each parity gives the stride-two second-order recurrence

\[
\boxed{
d_{n+4}=\tau d_{n+2}-\Delta d_n}
\tag{14.2}
\]

for all sufficiently large \(n\). Equivalently, the fully interleaved
sequence has an eventual constant-coefficient recurrence of order at most
four. This recurrence order does not change the algebraic-degree conclusion
\(\lambda_1(F)=\mu\in\mathbb Z\).

The inverse coordinate vectors have the conjugate selector tail and the same
spectral data. Their fixed visible residue subsequences obey the analogous
recurrences. No claim is made that every full scalar recurrence is minimal.

## 15. Hand-checkable witnesses

### 15.1 Interior quadratic witness

Take

\[
V=q_1^2q_2^2,
\qquad
B=\operatorname{diag}(3,2).
\]

There is one support matrix

\[
A=\begin{pmatrix}1&2\\2&1\end{pmatrix},
\qquad
C=BA=\begin{pmatrix}3&6\\4&2\end{pmatrix}.
\]

Its characteristic polynomial is

\[
t^2-5t-18,
\]

so

\[
\lambda_1(F)=\frac{5+\sqrt{97}}2.
\]

Here \(c_0=2+2-1=3\). The first vectors are

\[
u_1^+=B(3,3)^{\mathsf T}=(9,6)^{\mathsf T},
\]

\[
v_1^-=\mathcal A(B\mathbf1)
=\mathcal A(3,2)^{\mathsf T}
=(7,8)^{\mathsf T},
\]

and

\[
u_2^+=B\mathcal A(9,6)^{\mathsf T}
=(63,48)^{\mathsf T}
=3B(7,8)^{\mathsf T}.
\]

This directly checks (8.1) while exhibiting the possible quadratic degree.

### 15.2 Wall-integer witness

Take

\[
V=q_1^3q_2^2+q_1^2q_2^4,
\qquad
B=\operatorname{diag}(7,3).
\]

The two affine scores \(3r+2\) and \(2r+4\) meet at \(r_*=2\), where their
common value is \(8\). Since \(\kappa=7/3\),

\[
\varphi(2)
=\frac73\frac{8-2}{8-1}
=2,
\]

so the support wall is the unique fixed ray.

The adjacent matrices are

\[
C_-=
\begin{pmatrix}7&28\\6&9\end{pmatrix},
\qquad
C_+=
\begin{pmatrix}14&14\\9&3\end{pmatrix}.
\]

Both satisfy

\[
C_-\binom21=21\binom21,
\qquad
C_+\binom21=21\binom21.
\]

Thus the common wall multiplier and the dynamical degree are \(21\).
The ordinary seed uses the \((2,4)\) face first and gives

\[
u_1^+=C_-\mathbf1=(35,15)^{\mathsf T},
\qquad
r_1^+=\frac73>2.
\]

It then alternates strictly across \(2\) while converging to \(2\).
For a two-step check,

\[
C_+C_-=
\begin{pmatrix}
182&518\\81&279
\end{pmatrix},
\]

whose trace is \(461\), determinant is \(8820\), and characteristic
polynomial is

\[
t^2-461t+8820=(t-441)(t-20).
\]

The Perron root \(441=21^2\) confirms the wall-square mechanism by hand.

## 16. Adversarial boundaries and kill conditions

1. **A zero exponent destroys the common-face mechanism.** For example,
   with
   \[
   V=q_1^3+q_1q_2^3
   \]
   and an identity scaling, the fresh ratio expression becomes
   \[
   G(r)=\frac{\max(2r,3)}{r+2},
   \]
   which decreases below \(3/2\) and increases above \(3/2\). The two
   derivative coordinates are no longer controlled by one common
   \(\Phi\)-face.

2. **Allowing exponent one requires a new carry audit.** The projective
   derivative formula may remain decreasing when \(x,y\ge1\), but the
   automatic strict inequalities (3.1) can fail. The theorem should keep
   \(E\subset\mathbf Z_{\ge2}^2\).

3. **A mixed second potential destroys the positive diagonal phase.** If
   both phases use the monomial \(q_1^2q_2^2\), the degree matrix square is
   \[
   \begin{pmatrix}1&2\\2&1\end{pmatrix}^2
   =\begin{pmatrix}5&4\\4&5\end{pmatrix},
   \]
   whose projective map
   \[
   r\longmapsto\frac{5r+4}{4r+5}
   \]
   is increasing. Separation of \(W\) into pure powers is structural.

4. **Positive characteristic is excluded.** Derivative scalars and the
   extreme Hessian coefficient (4.1) can vanish after reduction.

5. **Zero coefficients change the support.** All support coefficients must
   remain nonzero after collecting duplicate exponent pairs. Positivity is
   not required.

6. **The numerical ratio is not eventually periodic in general.** It
   converges to the unique fixed ratio. Only an interior stationary selector
   or a wall-adjacent alternating selector is asserted.

7. **There is no projective numerical two-cycle.** Any statement deriving a
   generic quartic dynamical degree from such a cycle is false under the
   frozen hypotheses. The uniform logarithmic contraction is the decisive
   correction.

8. **The wall integer conclusion is not an interior conclusion.** An
   interior fixed ray can be quadratic, as Section 15.1 shows.

9. **The stride-two recurrence is not a numerical two-cycle statement.** It
   records alternating coefficient matrices around one fixed wall.

10. **No higher-dimensional extension follows.** In three or more degree
    coordinates there is no scalar projective order or one-dimensional
    contraction of the form proved here.

11. **No entropy, inverse-degree sequence identity, or conjugacy
    classification follows.** The exact result is equality of exponential
    forward and inverse degree rates plus the vector shift (8.1).

12. **The ordinary seed matters for the clean shift.** A different initial
    weighting still has the projective contraction, but
    \(\mathcal A(\mathbf1)=c_0\mathbf1\) no longer supplies the same initial
    bridge unless the seed is changed consistently.

13. **External absolute novelty is not certified here.** Locally, the
    theorem is distinct from a single crossed-binomial period-two example,
    from fixed high-dimensional stationary selector matrices, and from an
    unbounded high-dimensional Perron-degree construction. A separate
    literature review is required before any priority wording.

## 17. Exact theorem recommended for Paper 26

The paper-safe headline is:

> For every characteristic-zero Hamiltonian product shear in four variables
> whose first potential has arbitrary finite support in
> \(\mathbf Z_{\ge2}^2\) and whose second potential is a sum of two separated
> pure powers of gradient degrees at least two, the actual forward and inverse
> ordinary coordinate degrees obey the exact piecewise-homogeneous laws
> \(u_{n+1}=B\mathcal A(u_n)\) and
> \(v_{n+1}=\mathcal A(Bv_n)\). Their shifted vectors satisfy
> \(u_{n+1}=c_0Bv_n\), so
> \(\lambda_1(F)=\lambda_1(F^{-1})\). The induced map on positive degree
> ratios is a uniform contraction in logarithmic distance and has a unique
> fixed ray. An interior fixed ray yields a stationary positive
> \(2\times2\) integer selector matrix and a dynamical degree of algebraic
> degree at most two. A fixed support wall yields alternating adjacent
> selector matrices sharing one positive rational ray and one positive
> integer Perron multiplier; the dynamical degree equals that integer.

This statement is stronger and more accurate than a period-at-most-two
numerical-orbit formulation. Selector alternation survives only as a wall
phenomenon around one contracting fixed ray.

## 18. Scores and terminal decision

| Audit item | Score | Decision |
|---|---:|---|
| Literal symplectic map and inverses | 10.0/10 | closed |
| Extreme Hessian coefficient | 10.0/10 | closed |
| Jacobian-criterion independence and noncancellation | 9.5/10 | closed |
| Forward/inverse carries and block visibility | 9.8/10 | closed |
| Shifted vector identity and degree comparison | 10.0/10 | closed |
| Projective and inverse conjugacy | 10.0/10 | closed |
| Uniform finite-support logarithmic contraction | 9.8/10 | closed |
| Fixed-ray selector dichotomy | 9.5/10 | closed |
| Wall integer and interior quadratic spectrum | 9.8/10 | closed |
| Eventual recurrence scoping | 9.3/10 | closed |
| Overall proof completeness | **9.6/10** | **PASS** |

The candidate exceeds the required 9.0 proof-completeness threshold. The
PASS is conditional only on preserving the frozen support, characteristic,
pure-power, ordinary-degree, and nonclaim boundaries stated above.

PAPER26_CANDIDATE_GATE_PASS_R2
