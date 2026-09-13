# Self-contained proof package

## 1. Setting, notation, and theorem

Let \(K\) be a field of characteristic zero. Let
\[
E\subset\mathbf Z_{\ge2}^{2}
\]
be finite and nonempty. The support is collected, meaning that each exponent in \(E\) has one nonzero combined coefficient. Write
\[
V(q_1,q_2)=\sum_{(x,y)\in E}c_{x,y}q_1^xq_2^y,
\qquad c_{x,y}\in K^\times,
\]
and
\[
W(p_1,p_2)=\alpha p_1^{e+1}+\beta p_2^{f+1},
\qquad e,f\ge2,\quad\alpha,\beta\in K^\times.
\]
On affine four-space with position \(q=(q_1,q_2)\) and momentum \(p=(p_1,p_2)\), define
\[
S(q,p)=(q,p+\nabla V(q)),
\]
\[
T(q,p)=(q+\nabla W(p),p),
\]
\[
F=T\circ S.
\]
All degrees below are ordinary total degrees in the four initial coordinate variables.

For \(u=(u_1,u_2)\in\mathbf R_{>0}^{2}\), define
\[
H(u)=\max_{(x,y)\in E}(xu_1+yu_2),
\]
\[
\mathcal A(u)=
\begin{pmatrix}H(u)-u_1\\H(u)-u_2\end{pmatrix},
\qquad
B=\begin{pmatrix}e&0\\0&f\end{pmatrix}.
\]
The function \(H\) and the map \(\mathcal A\) are positively homogeneous:
\[
H(cu)=cH(u),\qquad
\mathcal A(cu)=c\mathcal A(u)\qquad(c>0).
\]

Let \(\mathbf1=(1,1)^\top\). Define the forward and inverse degree states by
\[
u^+_0=\mathbf1,\qquad
u^+_{n+1}=B\mathcal A(u^+_n),
\tag{1.1}
\]
\[
v^-_0=\mathbf1,\qquad
v^-_{n+1}=\mathcal A(Bv^-_n).
\tag{1.2}
\]

The theorem proved below is the following.

### Theorem 1.1

Under the displayed hypotheses:

1. \(F\) is a polynomial symplectomorphism and
   \[
   F^{-1}=S^{-1}\circ T^{-1},
   \]
   where the inverse shears use subtraction.
2. No leading-form cancellation occurs in any forward or inverse iterate, including on Newton walls, and
   \[
   \deg(F^n)=\|u^+_n\|_\infty,\qquad
   \deg(F^{-n})=\|v^-_n\|_\infty.
   \tag{1.3}
   \]
3. If \(c_\star=H(\mathbf1)-1\), then for all \(n\ge0\),
   \[
   u^+_{n+1}=c_\star Bv^-_n.
   \tag{1.4}
   \]
   Consequently
   \[
   \lambda_1(F)=\lambda_1(F^{-1}).
   \tag{1.5}
   \]
4. The projectivization of (1.1) is a strict contraction in logarithmic distance. It has a unique fixed ray. The selector tail is eventually stationary if that ray is in a Newton chamber, and it is fixed on the wall or alternates the two adjacent chambers if that ray lies on a Newton wall.
5. The first dynamical degree satisfies
   \[
   [\mathbf Q(\lambda_1(F)):\mathbf Q]\le2.
   \tag{1.6}
   \]
   In the wall case, \(\lambda_1(F)\) is a positive integer.
6. Each forward or inverse interior degree tail satisfies a constant-coefficient recurrence of order at most two. Each strict forward or inverse wall-alternating tail satisfies a constant-coefficient recurrence of order at most four; a fixed-ray tail is geometric.

The proof is organized so that cancellation control precedes the tropical recurrences.

## 2. Symplectic structure and inverses

Use the standard symplectic matrix
\[
J=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix}.
\]
Let \(H_V(q)\) and \(H_W(p)\) denote the Hessian matrices of \(V\) and \(W\). Both are symmetric.

The derivative of the lower shear is
\[
DS=\begin{pmatrix}I_2&0\\H_V&I_2\end{pmatrix}.
\]
First multiply
\[
JDS=
\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix}
\begin{pmatrix}I_2&0\\H_V&I_2\end{pmatrix}
=
\begin{pmatrix}H_V&I_2\\-I_2&0\end{pmatrix}.
\]
Then
\[
DS^\top JDS
=
\begin{pmatrix}I_2&H_V^\top\\0&I_2\end{pmatrix}
\begin{pmatrix}H_V&I_2\\-I_2&0\end{pmatrix}
=
\begin{pmatrix}H_V-H_V^\top&I_2\\-I_2&0\end{pmatrix}
=J.
\]

The derivative of the upper shear is
\[
DT=\begin{pmatrix}I_2&H_W\\0&I_2\end{pmatrix}.
\]
Similarly,
\[
JDT=
\begin{pmatrix}0&I_2\\-I_2&-H_W\end{pmatrix},
\]
and
\[
DT^\top JDT
=
\begin{pmatrix}I_2&0\\H_W^\top&I_2\end{pmatrix}
\begin{pmatrix}0&I_2\\-I_2&-H_W\end{pmatrix}
=
\begin{pmatrix}0&I_2\\-I_2&H_W^\top-H_W\end{pmatrix}
=J.
\]
Thus \(S\), \(T\), and \(F=T\circ S\) are symplectic polynomial maps.

The inverse formulas are direct:
\[
S^{-1}(q,p)=(q,p-\nabla V(q)),
\]
\[
T^{-1}(q,p)=(q-\nabla W(p),p).
\]
Indeed each shear fixes the variables on which its added gradient depends. Since \(F=T\circ S\), inversion reverses the phases:
\[
F^{-1}=S^{-1}\circ T^{-1}.
\tag{2.1}
\]
This order will be essential in the inverse degree recurrence.

## 3. The exposed-face Hessian certificate

For \(u\in\mathbf R_{>0}^{2}\), define the exposed support
\[
E_u=\{(x,y)\in E:xu_1+yu_2=H(u)\}
\]
and the face polynomial
\[
P_u(X,Y)=\sum_{(x,y)\in E_u}c_{x,y}X^xY^y.
\]

### Lemma 3.1: unique minimal-\(x\) point

Every positive exposed face \(E_u\) has a unique point with minimal first coordinate.

#### Proof

Existence follows from finiteness. Suppose \((x,y)\) and \((x,y')\) both lie on \(E_u\). Then
\[
xu_1+yu_2=xu_1+y'u_2.
\]
Since \(u_2>0\), this implies \(y=y'\). Therefore two distinct face points cannot have the same first coordinate. In particular the point with minimal first coordinate is unique. \(\square\)

Let this point be \((x_0,y_0)\), and abbreviate \(c_0=c_{x_0,y_0}\).

### Lemma 3.2: nonzero face-Hessian determinant

For every \(u>0\),
\[
\det\operatorname{Hess}P_u\ne0.
\]
More precisely, the coefficient of
\[
X^{2x_0-2}Y^{2y_0-2}
\]
in \(\det\operatorname{Hess}P_u\) is
\[
c_0^2x_0y_0(1-x_0-y_0).
\tag{3.1}
\]

#### Proof

Expand
\[
\det\operatorname{Hess}P_u
=(P_u)_{XX}(P_u)_{YY}-(P_u)_{XY}^{2}.
\tag{3.2}
\]
A contribution to the target exponent from an ordered pair of face points
\[
(x_a,y_a),(x_b,y_b)
\]
requires
\[
x_a+x_b-2=2x_0-2,
\]
or
\[
x_a+x_b=2x_0.
\tag{3.3}
\]
By minimality, \(x_a,x_b\ge x_0\). Equality (3.3) forces
\[
x_a=x_b=x_0.
\]
Lemma 3.1 then forces
\[
y_a=y_b=y_0.
\]
Thus only the self-pair of the minimal-\(x\) monomial contributes.

Its contribution from the first product in (3.2) is
\[
c_0^2x_0(x_0-1)y_0(y_0-1),
\]
while its contribution from the second product is
\[
c_0^2x_0^2y_0^2.
\]
The difference is
\[
c_0^2x_0y_0
\bigl((x_0-1)(y_0-1)-x_0y_0\bigr)
=c_0^2x_0y_0(1-x_0-y_0).
\]
Because \(c_0\ne0\), \(x_0,y_0\ge2\), and \(K\) has characteristic zero, this coefficient is nonzero. Hence the determinant polynomial is nonzero. \(\square\)

The proof works for a one-point face and for an arbitrary tied face. It does not use positivity of the coefficients, only their nonvanishing after collection.

## 4. Algebraic independence and substitution

We now convert the Hessian certificate into a cancellation certificate.

### Lemma 4.1: characteristic-zero Jacobian criterion in two variables

If \(R,S\in K[X,Y]\) and
\[
\det\frac{\partial(R,S)}{\partial(X,Y)}\ne0,
\]
then \(R,S\) are algebraically independent over \(K\).

#### Proof

If \(R,S\) were algebraically dependent, the subfield \(K(R,S)\) would have transcendence degree at most one. In characteristic zero, the Kähler differentials \(dR,dS\) would then be linearly dependent over \(K(X,Y)\). Their wedge would vanish:
\[
dR\wedge dS
=
\det\frac{\partial(R,S)}{\partial(X,Y)}
dX\wedge dY
=0,
\]
contrary to the hypothesis. \(\square\)

Applying this to
\[
R=(P_u)_X,\qquad S=(P_u)_Y,
\]
whose Jacobian determinant is \(\det\operatorname{Hess}P_u\), gives:

### Corollary 4.2

For every positive exposed face, the pair
\[
\bigl((P_u)_X,(P_u)_Y\bigr)
\]
is algebraically independent.

### Lemma 4.3: injective substitution

If \(L_1,L_2\) are algebraically independent elements of a polynomial ring \(A\) over \(K\), then
\[
\sigma:K[X,Y]\longrightarrow A,\qquad
\sigma(X)=L_1,\quad\sigma(Y)=L_2
\]
is injective.

#### Proof

The kernel consists exactly of polynomial relations between \(L_1,L_2\). Algebraic independence says that no nonzero relation exists. \(\square\)

### Lemma 4.4: face gradients survive substitution

If \(L_1,L_2\) are algebraically independent, then
\[
\bigl((P_u)_X(L_1,L_2),(P_u)_Y(L_1,L_2)\bigr)
\]
is algebraically independent.

#### Proof

Suppose a polynomial \(Q(U,V)\) vanishes after substitution:
\[
Q\bigl((P_u)_X(L_1,L_2),(P_u)_Y(L_1,L_2)\bigr)=0.
\]
By injectivity in Lemma 4.3,
\[
Q\bigl((P_u)_X(X,Y),(P_u)_Y(X,Y)\bigr)=0
\]
in \(K[X,Y]\). Corollary 4.2 then implies \(Q=0\). \(\square\)

### Lemma 4.5: pure powers preserve independence

If \(L_1,L_2\) are algebraically independent and \(a,b\ge1\), then \(L_1^a,L_2^b\) are algebraically independent. Nonzero scalar multiples and sign changes also preserve independence.

#### Proof

The map
\[
K[U,V]\longrightarrow K[X,Y],\qquad U\mapsto X^a,\quad V\mapsto Y^b
\]
is injective because distinct monomials \(U^iV^j\) map to distinct monomials \(X^{ai}Y^{bj}\). Compose it with the injective substitution \(X\mapsto L_1,Y\mapsto L_2\). Multiplication by nonzero scalars and signs is an automorphism of the polynomial ring in the two generated elements. \(\square\)

These lemmas are coefficient-uniform. There is no genericity exception.

## 5. Weighted top forms of the gradient

Let \(Q_1,Q_2\) be polynomials in the initial coordinates. Suppose their ordinary homogeneous leading forms are \(L_1,L_2\), with
\[
\deg Q_1=u_1,\qquad\deg Q_2=u_2,
\]
and suppose \(L_1,L_2\) are algebraically independent.

For a monomial \(Q_1^xQ_2^y\), the expected top ordinary degree is
\[
xu_1+yu_2.
\]
Because \(L_1,L_2\) are algebraically independent, distinct monomials in them cannot cancel in a nonzero polynomial. Therefore the leading homogeneous part of \(V(Q_1,Q_2)\) is
\[
P_u(L_1,L_2),
\]
where \(P_u\) is the entire exposed face, not an arbitrarily chosen tied monomial.

Differentiating \(V\) before substitution gives
\[
V_{q_1}(Q_1,Q_2)
=\sum_{(x,y)\in E}c_{x,y}xQ_1^{x-1}Q_2^y.
\]
Its highest possible degree is
\[
H(u)-u_1.
\]
Its leading homogeneous form is
\[
(P_u)_X(L_1,L_2).
\tag{5.1}
\]
Similarly,
\[
\deg V_{q_2}(Q_1,Q_2)=H(u)-u_2,
\]
with leading form
\[
(P_u)_Y(L_1,L_2).
\tag{5.2}
\]
Corollary 4.2 and Lemma 4.4 show simultaneously that neither form vanishes and that the pair (5.1)–(5.2) is algebraically independent.

Thus the exact gradient-degree transform is
\[
u\longmapsto\mathcal A(u).
\tag{5.3}
\]
Equations (5.1)–(5.3) remain valid on every Newton wall because they use the full face.

## 6. Carry inequalities

The support condition \(E\subset\mathbf Z_{\ge2}^{2}\) gives a uniform carry estimate. For every \((x,y)\in E\),
\[
xu_1+yu_2\ge2u_1+2u_2,
\]
so
\[
H(u)-u_1\ge u_1+2u_2>\max(u_1,u_2),
\tag{6.1}
\]
\[
H(u)-u_2\ge2u_1+u_2>\max(u_1,u_2).
\tag{6.2}
\]
In particular, each component of \(\mathcal A(u)\) strictly exceeds every component of \(u\).

Set
\[
A=(A_1,A_2)^\top=\mathcal A(u).
\]
The same lower bound for \(H\) gives the cross-component inequalities
\[
2A_1-A_2=H(u)-2u_1+u_2\ge3u_2>0,
\tag{6.3}
\]
\[
2A_2-A_1=H(u)+u_1-2u_2\ge3u_1>0.
\tag{6.4}
\]
Because \(e,f\ge2\) and \(A_1,A_2>0\),
\[
eA_1\ge2A_1>A_2,\qquad eA_1>A_1,
\]
\[
fA_2\ge2A_2>A_1,\qquad fA_2>A_2.
\]
Thus each component of \(BA=B\mathcal A(u)\) is strictly larger than both components of \(\mathcal A(u)\), and therefore larger than every component of \(u\).

These strict inequalities do two different jobs:

1. they prevent an old coordinate block from tying a fresh gradient block;
2. they identify the block in which the total degree of the full four-coordinate map is visible.

## 7. Forward leading-form induction and visibility

We track the state after each full forward iterate. At time \(n\), let the position block have degree vector \(u^+_n\). For \(n\ge1\), let the momentum block inherited from the preceding lower phase have degree vector \(w^+_n\). The inductive invariants are:

- the two position leading forms are algebraically independent;
- the position block strictly dominates the momentum block componentwise in the strong sense that every position degree exceeds every momentum degree;
- after the next lower phase, the new momentum leading pair is algebraically independent and has degree vector \(\mathcal A(u^+_n)\).

At \(n=0\), the position leading pair is \((q_1,q_2)\), hence algebraically independent. Both position and momentum coordinate degrees equal one.

Apply \(S\). The new momentum block is
\[
p+\nabla V(q).
\]
By (6.1)–(6.2), both gradient degrees exceed one, so the old \(p\) terms cannot affect the top forms. Section 5 gives
\[
w^+_1=\mathcal A(u^+_0),
\]
and the new momentum leading pair is algebraically independent.

Apply \(T\). Since
\[
\nabla W(p)
=
\bigl(\alpha(e+1)p_1^e,\ \beta(f+1)p_2^f\bigr),
\]
the new position degree vector is
\[
u^+_1=Bw^+_1=B\mathcal A(u^+_0).
\]
The new leading pair is a nonzero scalar multiple of
\[
\bigl((L^p_1)^e,(L^p_2)^f\bigr),
\]
where \(L^p_1,L^p_2\) are the momentum leading forms after \(S\). Lemma 4.5 makes this pair algebraically independent. The pure-power degrees strictly exceed all momentum degrees, while Section 6 shows that they also exceed the old position degrees. Thus the fresh position block is visible.

For the induction step, assume the invariants at full time \(n\). In the next lower phase, Section 5 gives a new algebraically independent momentum leading pair of degree
\[
w^+_{n+1}=\mathcal A(u^+_n).
\tag{7.1}
\]
Equations (6.1)–(6.2) show that each of these fresh degrees exceeds every old position degree, and hence every old momentum degree. No carry can tie it.

The upper phase then gives the algebraically independent position leading pair and degree vector
\[
u^+_{n+1}=Bw^+_{n+1}
=B\mathcal A(u^+_n).
\tag{7.2}
\]
Each new position degree exceeds every new momentum degree, so the position block is visible after the full iterate. Therefore
\[
\deg(F^n)=\max(u^+_{n,1},u^+_{n,2})
=\|u^+_n\|_\infty.
\tag{7.3}
\]

This proves the forward recurrence, top-form survival, and block visibility simultaneously.

## 8. Inverse leading-form induction and visibility

The inverse phases occur in the order
\[
T^{-1}:\quad(q,p)\mapsto(q-\nabla W(p),p),
\]
then
\[
S^{-1}:\quad(q,p)\mapsto(q,p-\nabla V(q)).
\]

At full inverse time \(n\), let the momentum degree vector be \(v^-_n\). After the next \(T^{-1}\) phase, let the fresh position degree vector be \(z^-_{n+1}\).

At \(n=0\), the momentum leading pair \((p_1,p_2)\) is algebraically independent and both blocks have coordinate degrees one.

Apply \(T^{-1}\). The subtraction sign changes only nonzero scalar factors in the top forms. The pure powers of the momentum leading pair survive by Lemma 4.5, and
\[
z^-_1=Bv^-_0.
\]
Since \(e,f\ge2\), the corresponding coordinate contributions dominate the initial position coordinates.

Apply \(S^{-1}\). Section 5, now applied to the fresh position leading pair, gives a momentum gradient leading pair with degree
\[
v^-_1=\mathcal A(z^-_1)
=\mathcal A(Bv^-_0).
\]
Each component of \(v^-_1\) exceeds every component of \(z^-_1\), by (6.1)–(6.2), so the gradient dominates the old momentum block. Its pair is algebraically independent, and the final momentum block is visible.

Assume now that at full inverse time \(n\):

- the momentum leading pair is algebraically independent;
- every momentum degree exceeds every current position degree;
- the momentum degree vector is \(v^-_n\).

The next \(T^{-1}\) phase produces
\[
z^-_{n+1}=Bv^-_n.
\tag{8.1}
\]
Although a diagonal scaling need not preserve a global component ordering for an arbitrary vector, it dominates the old position block here: each old position degree is smaller than every component of \(v^-_n\), and each component of \(Bv^-_n\) is at least twice the corresponding positive momentum degree.

The next \(S^{-1}\) phase produces
\[
v^-_{n+1}
=\mathcal A(z^-_{n+1})
=\mathcal A(Bv^-_n).
\tag{8.2}
\]
Both components exceed every component of \(z^-_{n+1}\), which in turn includes a component exceeding the maximum old momentum degree. Hence the fresh momentum block dominates all carried terms. Sections 4–5 again give algebraic independence of its leading pair, with signs harmless.

Thus, after every full inverse iterate, the momentum block is visible:
\[
\deg(F^{-n})=\|v^-_n\|_\infty.
\tag{8.3}
\]

This completes the bidirectional cancellation and visibility proof.

## 9. The exact forward–inverse bridge

Set
\[
c_\star=H(\mathbf1)-1.
\]
Because both coordinates of \(\mathbf1\) are one,
\[
\mathcal A(\mathbf1)
=
\begin{pmatrix}H(\mathbf1)-1\\H(\mathbf1)-1\end{pmatrix}
=c_\star\mathbf1.
\]
The base step is therefore
\[
u^+_1
=B\mathcal A(\mathbf1)
=c_\star B\mathbf1
=c_\star Bv^-_0.
\tag{9.1}
\]

Suppose
\[
u^+_{n+1}=c_\star Bv^-_n.
\]
Positive homogeneity gives
\[
\begin{aligned}
u^+_{n+2}
&=B\mathcal A(u^+_{n+1})\\
&=B\mathcal A(c_\star Bv^-_n)\\
&=c_\star B\mathcal A(Bv^-_n)\\
&=c_\star Bv^-_{n+1}.
\end{aligned}
\]
By induction,
\[
u^+_{n+1}=c_\star Bv^-_n
\qquad(n\ge0).
\tag{9.2}
\]

For every positive vector \(v\),
\[
\min(e,f)\|v\|_\infty
\le\|Bv\|_\infty
\le\max(e,f)\|v\|_\infty.
\]
Combining this with (7.3), (8.3), and (9.2) yields
\[
c_\star\min(e,f)\deg(F^{-n})
\le\deg(F^{n+1})
\le c_\star\max(e,f)\deg(F^{-n}).
\tag{9.3}
\]
Taking \(n\)-th roots and using that fixed positive multiplicative constants and the one-step shift do not change an exponential rate gives
\[
\lambda_1(F)=\lambda_1(F^{-1}).
\tag{9.4}
\]

Equation (9.2), not merely (9.4), is the new exact structural relation. It is tied to the ordinary seed and the phase order fixed in Section 1.

## 10. Forward projectivization

Write a positive ray as \(u=(r,1)\), where \(r>0\), and set
\[
\Phi(r)=H(r,1)=\max_{(x,y)\in E}(xr+y),
\qquad
\kappa=e/f.
\]
Then
\[
\mathcal A(r,1)
=
\begin{pmatrix}\Phi(r)-r\\\Phi(r)-1\end{pmatrix}.
\]
After multiplication by \(B\), the new ratio is
\[
\phi(r)
=
\kappa\frac{\Phi(r)-r}{\Phi(r)-1}.
\tag{10.1}
\]
The denominator and numerator are positive. Indeed every active \((x,y)\) has \(x,y\ge2\), so
\[
\Phi(r)-r\ge r+2>0,\qquad
\Phi(r)-1\ge2r+1>0.
\]

On a chamber where \((x,y)\) realizes \(\Phi(r)\),
\[
\Phi(r)=xr+y,
\]
and
\[
\phi_{x,y}(r)
=
\kappa\frac{(x-1)r+y}{xr+y-1}.
\tag{10.2}
\]
Differentiate:
\[
\phi'_{x,y}(r)
=
\kappa
\frac{(x-1)(xr+y-1)-x((x-1)r+y)}
{(xr+y-1)^2}.
\]
The numerator simplifies to
\[
(x-1)(y-1)-xy=1-x-y.
\]
Thus
\[
\phi'_{x,y}(r)
=
-\kappa\frac{x+y-1}{(xr+y-1)^2}<0.
\tag{10.3}
\]
Every chamber branch is strictly decreasing. Since \(\Phi\) is continuous and adjacent formulas agree at a wall, \(\phi\) is continuous and strictly decreasing on all of \((0,\infty)\).

## 11. Uniform contraction in logarithmic distance

Let
\[
t=\log r,\qquad h(t)=\log\phi(e^t).
\]
On the chamber selected by \((x,y)\), the chain rule and (10.2)–(10.3) give
\[
\left|h'(t)\right|
=
\left|\frac{r\phi'_{x,y}(r)}{\phi_{x,y}(r)}\right|
=
\frac{r(x+y-1)}
{((x-1)r+y)(xr+y-1)}
=:\eta_{x,y}(r).
\tag{11.1}
\]

The denominator exceeds the numerator by
\[
\begin{aligned}
&((x-1)r+y)(xr+y-1)-r(x+y-1)\\
&\quad=
x(x-1)r^2+2(x-1)(y-1)r+y(y-1).
\end{aligned}
\tag{11.2}
\]
Every coefficient on the last line is positive for \(x,y\ge2\), and \(r>0\). Hence
\[
0<\eta_{x,y}(r)<1.
\tag{11.3}
\]

Pointwise strictness is not yet a uniform contraction. We now make it uniform.

For fixed \((x,y)\), the rational function \(\eta_{x,y}\) is continuous on \((0,\infty)\). Moreover,
\[
\lim_{r\to0}\eta_{x,y}(r)=0,\qquad
\lim_{r\to\infty}\eta_{x,y}(r)=0.
\]
Extend it by zero to the two endpoints of the compactified interval \([0,\infty]\). It attains a maximum
\[
q_{x,y}<1.
\]
Because \(E\) is finite,
\[
q=\max_{(x,y)\in E}q_{x,y}<1.
\tag{11.4}
\]

It remains to cross walls. Let \(t<t'\). The compact interval \([t,t']\) meets only finitely many Newton walls. Partition it at those walls. On each open subinterval, \(h\) is differentiable and \(|h'|\le q\). Continuity at the endpoints gives
\[
|h(t')-h(t)|
\le\sum_j q\,|I_j|
=q|t'-t|.
\tag{11.5}
\]
Thus \(h:\mathbf R\to\mathbf R\) is a global strict contraction.

Since \(\mathbf R\) is complete, Banach's fixed-point theorem gives a unique \(t_\star\in\mathbf R\) with
\[
h(t_\star)=t_\star.
\]
Equivalently, \(\phi\) has a unique positive fixed ray
\[
r_\star=e^{t_\star}.
\tag{11.6}
\]
Every positive orbit converges to it at the uniform geometric rate \(q\) in log distance. A strict contraction has no nontrivial periodic orbit.

## 12. Inverse projective conjugacy

Write the inverse momentum state as \(v=(s,1)\). The intermediate position vector \(Bv\) has ratio
\[
\kappa s.
\]
Applying \(\mathcal A\) gives the inverse ratio map
\[
\psi(s)
=
\frac{\Phi(\kappa s)-\kappa s}
{\Phi(\kappa s)-1}.
\tag{12.1}
\]
Let
\[
L(s)=\kappa s.
\]
Then
\[
\begin{aligned}
(L\circ\psi)(s)
&=\kappa
\frac{\Phi(\kappa s)-\kappa s}
{\Phi(\kappa s)-1}\\
&=\phi(\kappa s)\\
&=(\phi\circ L)(s).
\end{aligned}
\tag{12.2}
\]
Therefore
\[
L\circ\psi=\phi\circ L.
\tag{12.3}
\]
The inverse projective dynamics is linearly conjugate to the forward projective dynamics. It has the corresponding unique fixed ray and the same selector-tail classification after the rescaling.

## 13. Selector-tail classification

Newton walls are the finitely many positive ratios at which two or more affine functions \(xr+y\) tie for the maximum. Their complement is a finite union of open chambers.

### Proposition 13.1: interior fixed ray

If \(r_\star\) lies in an open Newton chamber, every positive orbit eventually remains in that chamber.

#### Proof

The fixed ray has positive distance in log coordinate from the finite wall set. Every orbit converges to \(t_\star\), so it eventually enters a smaller wall-free neighborhood of \(t_\star\) and never leaves it. \(\square\)

### Proposition 13.2: wall fixed ray

Suppose \(r_\star\) lies on a Newton wall.

1. The trajectory starting at \(r_\star\) remains on the wall.
2. Every other trajectory eventually alternates the two chambers adjacent to the wall and converges to \(r_\star\).
3. No trajectory lands on the wall after a positive delay unless it started there.

#### Proof

The first statement is the fixed-point identity.

Because \(h\) is strictly decreasing,
\[
t<t_\star\implies h(t)>h(t_\star)=t_\star,
\]
and
\[
t>t_\star\implies h(t)<t_\star.
\]
Thus every strict orbit crosses from one side of \(t_\star\) to the other at each step. Convergence and finiteness of the wall set imply that, after a finite transient, the only chambers visited are the two adjacent to \(t_\star\).

Finally, if \(h(t)=t_\star=h(t_\star)\), strict monotonicity gives \(t=t_\star\). Hence delayed landing is impossible. \(\square\)

If several support points tie on the fixed wall, the proof is unchanged. The two open sides are controlled by the extreme adjacent exponents in the upper envelope. A trajectory exactly on the wall uses the full face polynomial in the leading-form proof. It is incorrect to select one tied monomial on the wall.

For the ordinary seed \(r_0=1\), a wall or interior fixed ray is hit exactly when \(r_\star=1\). If \(r_\star=1\), the seed is fixed from time zero. Otherwise injectivity rules out any later hit.

The “period two” visible in a strict wall selector word is therefore combinatorial alternation, not a nontrivial period-two projective orbit.

## 14. Interior spectrum

Suppose the fixed ray lies in the chamber selected by \((x,y)\). On that chamber,
\[
\mathcal A(u)
=
\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix}u.
\]
Set
\[
A_{x,y}=
\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},
\qquad
C_{x,y}=BA_{x,y}
=
\begin{pmatrix}
e(x-1)&ey\\
fx&f(y-1)
\end{pmatrix}.
\tag{14.1}
\]
Every entry is a positive integer. By Proposition 13.1, for some \(N\),
\[
u^+_{n+1}=C_{x,y}u^+_n\qquad(n\ge N).
\tag{14.2}
\]
The fixed ray is a positive eigenvector of \(C_{x,y}\). Perron–Frobenius identifies its eigenvalue with the spectral radius
\[
\rho(C_{x,y}).
\]
Transient factors do not change exponential growth, so
\[
\lambda_1(F)=\rho(C_{x,y}).
\tag{14.3}
\]
The characteristic polynomial is
\[
t^2-\operatorname{tr}(C_{x,y})t+\det(C_{x,y}),
\]
with integer coefficients. Hence
\[
[\mathbf Q(\lambda_1(F)):\mathbf Q]\le2.
\tag{14.4}
\]

## 15. Wall spectrum and integrality

Suppose the unique fixed ray lies on a Newton wall. The wall has rational slope because it is defined by equality of two integer affine functions:
\[
x_-r+y_-=x_+r+y_+.
\]
Choose its primitive positive integer direction
\[
w=(a,b)^\top,\qquad\gcd(a,b)=1.
\]

For every support point \((x,y)\) on the tied face,
\[
H(w)=xa+yb.
\]
Therefore
\[
A_{x,y}w
=
\begin{pmatrix}H(w)-a\\H(w)-b\end{pmatrix}
\tag{15.1}
\]
is independent of the chosen tied support point. Multiplication by \(B\) gives the same vector for all adjacent selector matrices:
\[
C_-w=C_+w.
\tag{15.2}
\]

Because \(w\) is the fixed projective ray, this common vector is parallel to \(w\). Thus
\[
C_-w=C_+w=\mu w
\tag{15.3}
\]
for a positive rational number \(\mu\). In fact \(\mu\) is an integer. One proof is that \(C_-w\) and \(w\) are integral and \(w\) is primitive: choose integers \(m,n\) with \(ma+nb=1\), and apply \(m\) and \(n\) to the two coordinate identities in (15.3). Equivalently, \(\mu\) is a rational eigenvalue of an integer matrix, hence a rational algebraic integer and therefore an integer.

For a strict wall orbit, the selector matrices alternate. Let
\[
M=C_+C_-
\]
for one parity; the reverse product controls the other parity. Equation (15.3) gives
\[
Mw=\mu^2w.
\]
The matrix \(M\) is positive, so its positive eigenvector \(w\) corresponds to its Perron root:
\[
\rho(M)=\mu^2.
\]
The growth is measured per single iterate, hence
\[
\lambda_1(F)=\sqrt{\rho(M)}=\mu\in\mathbf Z_{>0}.
\tag{15.4}
\]
If the ordinary seed lies exactly on the fixed wall, each selected face produces the same vector on \(w\), and the same geometric multiplier \(\mu\) applies without alternation.

At a multiple tie, (15.1) holds for every tied exponent, so the same integer multiplier conclusion remains valid.

Combining (14.4) and (15.4) proves the uniform bound
\[
[\mathbf Q(\lambda_1(F)):\mathbf Q]\le2.
\]

## 16. Degree recurrences

### Forward interior tail

For \(n\ge N\), equation (14.2) and Cayley–Hamilton give
\[
C_{x,y}^2
-\operatorname{tr}(C_{x,y})C_{x,y}
+\det(C_{x,y})I_2=0.
\]
Every coordinate \(a_n\) of \(u^+_n\) therefore satisfies
\[
a_{n+2}
=\operatorname{tr}(C_{x,y})a_{n+1}
-\det(C_{x,y})a_n.
\tag{16.1}
\]

If \(r_\star\ne1\), convergence implies that eventually the same coordinate of \(u^+_n\) is larger, so \(\deg(F^n)\) itself obeys (16.1). If \(r_\star=1\), the ordinary seed is the fixed ray from time zero and both coordinates grow geometrically with the Perron multiplier. Thus the forward degree tail has recurrence order at most two in every interior case.

### Forward strict wall tail

For one parity, the state advances by \(M=C_+C_-\); for the other, by \(\widetilde M=C_-C_+\). These two \(2\times2\) products have the same trace and determinant:
\[
\operatorname{tr}(C_+C_-)=\operatorname{tr}(C_-C_+),
\]
\[
\det(C_+C_-)=\det(C_-C_+).
\]
Each parity coordinate therefore satisfies the same Cayley–Hamilton recurrence. As in the interior case, the fixed ray cannot be \(r_\star=1\) for a strict orbit from the ordinary seed; hence the visible maximum is eventually a fixed coordinate. The full forward degree tail obeys
\[
d_{n+4}
=\operatorname{tr}(M)d_{n+2}
-\det(M)d_n.
\tag{16.2}
\]
This is an order-at-most-four recurrence. No minimality is asserted.

### Inverse selector matrices

The inverse scalar recurrence requires its own proof. The bridge (9.2) compares vectors after a diagonal rescaling, but it does not turn a recurrence for
\[
\max(e v^-_{n,1},f v^-_{n,2})
\]
into one for
\[
d^-_n=\deg(F^{-n})=\max(v^-_{n,1},v^-_{n,2}).
\]

For an active exponent \(\xi=(x,y)\), write
\[
A_\xi=\begin{pmatrix}x-1&y\\x&y-1\end{pmatrix},
\qquad C_\xi=BA_\xi,
\]
and define the inverse chamber matrix
\[
D_\xi=A_\xi B.
\]
Since \(B\) is invertible,
\[
D_\xi=B^{-1}C_\xi B.
\tag{16.3}
\]
Thus \(D_\xi\) is similar to \(C_\xi\), but the inverse recurrence is obtained directly from (8.2): whenever the ratio of \(Bv^-_n\) lies in the chamber selected by \(\xi\),
\[
v^-_{n+1}=D_\xi v^-_n.
\tag{16.4}
\]
The selector is determined by the ratio of \(Bv^-_n\), not by replacing the inverse state with a forward state.

### Inverse interior tail

Let \(s_n=v^-_{n,1}/v^-_{n,2}\). By the conjugacy in Section 12,
\[
s_\star=\frac{r_\star}{\kappa},
\qquad \kappa=e/f,
\]
is the unique inverse fixed ratio, and \(s_n\to s_\star\). Suppose \(r_\star\) lies in the chamber selected by \(\xi\). Then the ratio of \(Bv^-_n\) converges to \(r_\star\), so for some threshold \(n_{\mathrm{int}}\),
\[
v^-_{n+1}=D_\xi v^-_n\qquad(n\ge n_{\mathrm{int}}).
\tag{16.5}
\]
Similarity (16.3) gives
\[
\operatorname{tr}(D_\xi)=\operatorname{tr}(C_\xi),
\qquad
\det(D_\xi)=\det(C_\xi).
\]
Cayley–Hamilton therefore gives
\[
D_\xi^2-\operatorname{tr}(C_\xi)D_\xi+\det(C_\xi)I_2=0.
\]
Each inverse state coordinate \(b_n\) satisfies
\[
b_{n+2}=\operatorname{tr}(C_\xi)b_{n+1}-\det(C_\xi)b_n
\qquad(n\ge n_{\mathrm{int}}).
\tag{16.6}
\]

If \(s_\star\ne1\), convergence gives an index after which \(s_n-1\) has the fixed sign of \(s_\star-1\). Hence the same coordinate of \(v^-_n\) realizes the visible maximum (8.3), and \(d^-_n\) obeys (16.6).

If \(s_\star=1\), the ordinary inverse seed \(v^-_0=\mathbf1\) already lies on the unique inverse fixed ray. It is fixed projectively from time zero. In the interior chamber, \(D_\xi\mathbf1=\nu\mathbf1\) for its positive fixed-ray multiplier \(\nu\), so
\[
v^-_n=\nu^n\mathbf1,\qquad d^-_n=\nu^n.
\tag{16.7}
\]
This geometric sequence has recurrence order one, hence order at most two. These two cases exhaust the inverse interior tail.

### Inverse fixed-wall and strict-wall tails

If \(\kappa s_\star=r_\star\) lies on a Newton wall and \(s_\star=1\), the ordinary inverse seed is again fixed from time zero. Because \(v^-_n\) remains on the inverse ray \(s=1\), the intermediate vector \(Bv^-_n\) stays on the tied Newton ray \(r=r_\star\). The full tied face therefore gives one homogeneous degree vector on that Newton ray, so \(v^-_n=\nu^n\mathbf1\) and the inverse degree sequence is geometric.

Now suppose the ordinary inverse orbit is strict. Then necessarily \(s_\star\ne1\): if \(s_\star=1\), the seed \(s_0=1\) would be the fixed ratio from time zero. The decreasing inverse contraction makes a strict orbit alternate the two adjacent selectors after a finite transient. Label them so that a step with \(D_-\) followed by a step with \(D_+\) has the two-step product
\[
N_+=D_+D_-,
\]
while the opposite parity has
\[
N_-=D_-D_+.
\]
Define the forward parity products with the same step order:
\[
M_+=C_+C_-,
\qquad
M_-=C_-C_+.
\]
Using (16.3) twice gives the exact similarities
\[
N_+=B^{-1}M_+B,\qquad N_-=B^{-1}M_-B.
\tag{16.8}
\]
Consequently
\[
\tau=\operatorname{tr}(N_+)=\operatorname{tr}(M_+)
=\operatorname{tr}(M_-)=\operatorname{tr}(N_-),
\]
and
\[
\Delta=\det(N_+)=\det(M_+)=\det(M_-)=\det(N_-).
\tag{16.9}
\]
The equality of the two middle traces is cyclicity of trace, and the determinant equality is multiplicativity.

Cayley–Hamilton applied separately to \(N_+\) and \(N_-\) gives
\[
N_\pm^2-\tau N_\pm+\Delta I_2=0.
\tag{16.10}
\]
Hence every coordinate on either parity subsequence obeys the same stride-two recurrence.

It remains to pass from coordinates to the visible scalar degree. Since \(s_n\to s_\star\ne1\), choose a neighborhood of \(s_\star\) disjoint from \(1\). Both parity subsequences eventually lie in that neighborhood. On each parity, the same coordinate of \(v^-_n\) therefore realizes
\[
d^-_n=\max(v^-_{n,1},v^-_{n,2}).
\]
Applying (16.10) to that coordinate on each parity gives, for all sufficiently large \(n\),
\[
d^-_{n+4}=\tau d^-_{n+2}-\Delta d^-_n.
\tag{16.11}
\]
This is an order-at-most-four recurrence. No minimality is asserted.

The bridge (9.2) remains the exact vector identity that proves the constant-factor comparison and equality of forward and inverse exponential rates. Equations (16.3)–(16.11), not the bridge, prove the inverse scalar recurrences.

## 17. Fixture I: one-face quadratic value

Take
\[
E=\{(2,2)\},\qquad B=\operatorname{diag}(3,2).
\]
The envelope has one branch, and
\[
A=
\begin{pmatrix}1&2\\2&1\end{pmatrix}.
\]
Thus
\[
C=BA
=
\begin{pmatrix}3&6\\4&2\end{pmatrix}.
\]
Its trace is \(5\) and determinant is
\[
3\cdot2-6\cdot4=-18.
\]
Hence its characteristic polynomial is
\[
t^2-5t-18
\]
with roots
\[
\frac{5\pm\sqrt{97}}2.
\]
The Perron root is
\[
\lambda_1(F)=\frac{5+\sqrt{97}}2,
\]
which is genuinely quadratic.

The exact bridge is visible at small indices. Here
\[
H(\mathbf1)=4,\qquad c_\star=3.
\]
Forward:
\[
\mathcal A(1,1)=(3,3)^\top,
\]
\[
u^+_1=B(3,3)^\top=(9,6)^\top.
\]
Inverse:
\[
Bv^-_0=(3,2)^\top,
\]
\[
H(3,2)=2\cdot3+2\cdot2=10,
\]
\[
v^-_1=\mathcal A(3,2)=(7,8)^\top.
\]
Then
\[
u^+_2
=B\mathcal A(9,6).
\]
Since \(H(9,6)=30\),
\[
\mathcal A(9,6)=(21,24)^\top,
\]
and
\[
u^+_2=(63,48)^\top.
\]
On the other hand,
\[
c_\star Bv^-_1
=3\operatorname{diag}(3,2)(7,8)^\top
=(63,48)^\top.
\]
This verifies the shift, scalar, and diagonal scaling in (9.2).

## 18. Fixture II: three-support transient and wall tail

Take
\[
E=\{(2,8),(4,5),(5,3)\},
\qquad
B=\operatorname{diag}(24,11).
\]
The three affine envelope functions are
\[
2r+8,\qquad4r+5,\qquad5r+3.
\]
The first two tie at
\[
2r+8=4r+5\iff r=3/2.
\]
The last two tie at
\[
4r+5=5r+3\iff r=2.
\]
Thus the low, middle, and high selectors are respectively
\[
(2,8),\quad(4,5),\quad(5,3).
\]

Their matrices are
\[
C_{\rm low}
=
\begin{pmatrix}24&192\\22&77\end{pmatrix},
\]
\[
C_{\rm mid}
=
\begin{pmatrix}72&120\\44&44\end{pmatrix},
\]
\[
C_{\rm high}
=
\begin{pmatrix}96&72\\55&22\end{pmatrix}.
\]

Start from \(u^+_0=(1,1)^\top\), so the low selector is active. Then
\[
u^+_1=C_{\rm low}(1,1)^\top
=(216,99)^\top,
\]
and
\[
r_1=\frac{216}{99}=\frac{24}{11}>2.
\]
The high selector is next:
\[
u^+_2
=C_{\rm high}(216,99)^\top
=(27864,14058)^\top.
\]
Dividing numerator and denominator by \(18\) gives
\[
r_2=\frac{1548}{781}.
\]
Since
\[
\frac32<\frac{1548}{781}<2,
\]
the middle selector is next. Applying it gives a ratio
\[
r_3
=\frac{205176}{102476}
=\frac{51294}{25619}>2.
\]
Thus the initial selector word is
\[
\text{low},\ \text{high},\ \text{middle},\ \text{high}.
\]

We now prove the tail, rather than extrapolating it from these values. On the middle chamber,
\[
\phi_{\rm mid}(r)
=
\frac{24}{11}\frac{3r+5}{4r+4}.
\]
It is decreasing. At \(r=2\) it equals \(2\), and at \(r=3/2\) it is strictly greater than \(2\). Hence
\[
\phi_{\rm mid}\bigl((3/2,2)\bigr)\subset(2,\infty).
\tag{18.1}
\]
On the high chamber,
\[
\phi_{\rm high}(r)
=
\frac{24}{11}\frac{4r+3}{5r+2}.
\]
It is decreasing, equals \(2\) at \(r=2\), and tends to
\[
\frac{96}{55}
\]
as \(r\to\infty\). Since
\[
\frac{96}{55}>\frac32,
\]
we have
\[
\phi_{\rm high}\bigl((2,\infty)\bigr)
\subset(3/2,2).
\tag{18.2}
\]
Equations (18.1)–(18.2) prove that the tail alternates middle, high, middle, high indefinitely while converging to \(r=2\).

Let
\[
w=(2,1)^\top.
\]
Direct multiplication gives
\[
C_{\rm mid}w
=
\begin{pmatrix}72&120\\44&44\end{pmatrix}
\begin{pmatrix}2\\1\end{pmatrix}
=
\begin{pmatrix}264\\132\end{pmatrix}
=132w,
\]
and
\[
C_{\rm high}w
=
\begin{pmatrix}96&72\\55&22\end{pmatrix}
\begin{pmatrix}2\\1\end{pmatrix}
=
\begin{pmatrix}264\\132\end{pmatrix}
=132w.
\]
For the middle-then-high two-step order,
\[
M=C_{\rm high}C_{\rm mid}
=
\begin{pmatrix}
10080&14688\\
4928&7568
\end{pmatrix}.
\]
Its trace is
\[
10080+7568=17648.
\]
Its determinant is
\[
10080\cdot7568-14688\cdot4928
=3902976.
\]
The two integers
\[
17424=132^2,\qquad224
\]
have sum \(17648\) and product \(3902976\). They are therefore the eigenvalues of \(M\). The Perron root is \(17424\), and the per-step dynamical degree is
\[
\sqrt{17424}=132.
\]

This is an explicit transient followed by selector alternation toward a fixed wall. It is not a numerical period-two orbit.

## 19. Counterexamples, failed extensions, and anti-claims

The hypotheses are frozen because each supports a named proof step.

### 19.1 Axis support

If axis exponents are allowed, the face-Hessian certificate and two-coordinate independence can fail. For example,
\[
V(q_1,q_2)=q_1^3+q_1q_2^3
\]
has a chamber face \(P=X^3\). Its gradient pair is
\[
(3X^2,0),
\]
which is not algebraically independent, and \(\det\operatorname{Hess}P=0\). The uniform two-coordinate carry also fails because one derivative direction may be absent. This example is used only to show failure of the present proof mechanism; no universal statement about axis-support dynamics is made.

### 19.2 Exponent one

If \(x=1\) or \(y=1\), the inequalities in Section 6 lose a full copy of a coordinate degree. Strict domination of all carried blocks is no longer automatic. The theorem makes no optimality claim about the threshold two.

### 19.3 Mixed momentum Hamiltonian

The separated form of \(W\) makes the upper leading transform diagonal:
\[
(L_1,L_2)\mapsto(L_1^e,L_2^f).
\]
A mixed \(W\) replaces \(B\) by another Newton transform and can destroy both the simple conjugacy and decreasing projective dynamics. For instance, a positive mixed leading matrix can induce
\[
r\longmapsto\frac{5r+4}{4r+5},
\]
whose derivative is positive. The contraction theorem is not extended to that setting.

### 19.4 Positive characteristic

The coefficient in (3.1) contains
\[
x_0y_0(1-x_0-y_0).
\]
It can vanish modulo the characteristic even when the coefficient \(c_0\) is nonzero. Pure-power derivatives can also vanish. Characteristic zero is essential to the present proof.

### 19.5 Uncollected support

If duplicate exponents with canceling coefficients are kept in \(E\), the envelope records a monomial absent from the actual polynomial. Support must be formed after coefficient collection.

### 19.6 Different seed or phase order

Contraction of the forward ratio map applies to every positive ray, but the exact bridge (9.2) uses
\[
\mathcal A(\mathbf1)=c_\star\mathbf1
\]
and the order \(F=T\circ S\). A new seed or reversed forward order requires a new base identity and possibly a different shift.

### 19.7 Dimension at least three

The proof uses a one-dimensional projective coordinate and the fact that a continuous decreasing contraction alternates across a wall point. In higher projective dimension, neither the total order nor the two-side wall classification survives automatically.

### 19.8 No genericity patch

All coefficients on the collected support are arbitrary nonzero elements. It would weaken the theorem to replace the face-Hessian proof by “generic coefficients avoid cancellation.” Conversely, the present argument does not cover coefficients that vanish after specialization without recollecting the support.

### 19.9 Invariants not computed

The proof computes ordinary degree growth and the first dynamical degree of this affine polynomial automorphism. It does not compute:

- higher dynamical degrees;
- topological or measure-theoretic entropy;
- a compactification action;
- integrability or nonintegrability;
- periodic or arithmetic point orbits.

No equality involving those invariants should be inferred.

### 19.10 No classification or priority claim

The theorem does not classify polynomial symplectomorphisms, prove nonconjugacy, or assert a globally first result. The current literature boundary is local and requires external novelty verification.

### 19.11 No recurrence minimality

Equations (16.1)–(16.2) and (16.6)–(16.11) give recurrence orders at most two and at most four. Special traces, determinants, initial states, or a fixed wall ray may lower the minimal order.

### 19.12 No nontrivial wall cycle

A wall-alternating selector word does not imply a period-two ratio orbit. Global log contraction rules out every nontrivial numerical cycle. The alternating ratios converge to the unique fixed wall ray.

## 20. Proof dependency audit

The theorem's logic is now closed:

1. Symmetric Hessians prove symplecticity; reversed subtraction phases give the inverse.
2. The unique minimal-\(x\) face monomial gives a nonzero Hessian-determinant coefficient.
3. The Jacobian criterion gives algebraic independence of the full face-gradient pair.
4. Injective substitution and pure powers propagate that independence through every half-step.
5. Support exponents at least two give strict forward and inverse carries and identify the visible block.
6. Exact degree transports follow without genericity.
7. Homogeneity and the ordinary seed give the shifted forward–inverse bridge.
8. The projective branch formula gives a positive strict logarithmic derivative gap.
9. Compactification of each of finitely many branches makes the contraction uniform; continuity patches walls.
10. The unique fixed ray gives the exhaustive selector-tail classification.
11. A stationary positive \(2\times2\) matrix gives an interior quadratic value.
12. A primitive rational wall ray gives an integer common multiplier.
13. Cayley–Hamilton for the forward matrices \(C_\xi\), the separately derived inverse matrices \(D_\xi=B^{-1}C_\xi B\), and both forward/inverse parity products yields the stated scalar recurrence upper bounds after visible-coordinate stabilization; the bridge is not used as a scalar-recurrence proof.
14. The two fixtures test the interior and wall branches with exact arithmetic.

No later step is used to justify an earlier one, and no empirical observation is used in the chain.
