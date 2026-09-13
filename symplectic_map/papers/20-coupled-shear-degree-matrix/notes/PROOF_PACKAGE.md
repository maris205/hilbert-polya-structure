# Paper20 — Theorem, Lemmas, and Proof Package

This is the formal proof design for the fixed four-dimensional family in
`RESEARCH_QUESTION.md`. It deliberately does not assert a generic Newton-fan
theorem.

## 1. Setup and phase notation

Let \(K\) be algebraically closed with \(\operatorname{char}K=0\), let
\(g\ge5\), and put
\[
 V=q_1^2q_2^2+q_1^g,
 \qquad W=p_1^2p_2^2+p_2^g.
\]
Write
\[
 S(q,p)=(q,p+\nabla V(q)),
 \qquad T(q,p)=(q+\nabla W(p),p),
 \qquad F=T\circ S.
\]
Writing \(\widehat p=p+\nabla V(q)\), the coordinate formula used in every
selector check is
\[
\begin{aligned}
\widehat p_1&=p_1+2q_1q_2^2+gq_1^{g-1},&
\widehat p_2&=p_2+2q_1^2q_2,\\
F_1&=q_1+2\widehat p_1\widehat p_2^2,&
F_2&=q_2+2\widehat p_1^2\widehat p_2+g\widehat p_2^{g-1},\\
F_3&=\widehat p_1,&F_4&=\widehat p_2.
\end{aligned}
\]
For the coordinate polynomials of \(F^n\), set
\[
 u_n=(\deg q_{1,n},\deg q_{2,n})^{\mathsf T},
 \qquad q_{i,n}=q_i\circ F^n.
\]
When applying the \((n+1)\)-st step, let \(v_{n+1}\) be the degree vector of the
intermediate \(p\)-coordinates after \(S\), before \(T\). Thus \(v_{n+1}\)
is not the same phase as \(u_n\). The initial vectors are
\(u_0=(1,1)^{\mathsf T}\) and the carried initial \(p\)-coordinates also have
degree one.

The face rows are fixed by the actual monomials:
\[
 A=\begin{pmatrix}g-1&0\\2&1\end{pmatrix},
 \qquad B=\begin{pmatrix}1&2\\0&g-1\end{pmatrix}.
\]
They are Newton-face exponent rows (gradient monomial degree minus the
coordinate degree), not arbitrary Jacobian matrices. The first row of \(A\)
selects \(q_1^g\), the second selects \(q_1^2q_2^2\); the first row of \(B\)
selects \(p_1^2p_2^2\), the second selects \(p_2^g\).

Define
\[
 C=BA=\begin{pmatrix}g+3&2\\2(g-1)&g-1\end{pmatrix},
 \qquad
 \mathcal C=\left\{u=(u_1,u_2)>0:1\le u_2/u_1<(g-2)/2\right\}.
\]

## 2. Lemmas

### Lemma 1 (canonical shears)

Both \(S\) and \(T\) are polynomial automorphisms and preserve
\(\omega=dq_1\wedge dp_1+dq_2\wedge dp_2\). Their inverses are
\[
 S^{-1}(q,p)=(q,p-\nabla V(q)),\qquad
 T^{-1}(q,p)=(q-\nabla W(p),p).
\]

**Proof.** For \(S\),
\[
 S^*\omega=\sum_i dq_i\wedge d(p_i+\partial_iV)
 =\omega+\sum_{i,j}\partial_{ij}V\,dq_i\wedge dq_j=\omega,
\]
because the Hessian is symmetric and the last sum cancels pairwise. The proof
for \(T\) is identical with \(q,p,W\) interchanged. The inverse formulas are
immediate triangular polynomial maps. \(\square\)

### Lemma 2 (the \(S\)-face selectors)

If \(u\in\mathcal C\), then the gradient terms in the first shear have exact
degree vector \(Au\), and they strictly dominate the carried \(p\)-vector
whenever the latter is the preceding intermediate vector.

**Proof.** The two nonzero gradient coordinates are
\[
 \partial_{q_1}V=2q_1q_2^2+gq_1^{g-1},
 \qquad \partial_{q_2}V=2q_1^2q_2.
\]
For the first coordinate, the two candidate degrees are
\(u_1+2u_2\) and \((g-1)u_1\). Since
\(u_2/u_1<(g-2)/2\),
\[
 u_1+2u_2<(g-1)u_1.
\]
The second coordinate has degree \(2u_1+u_2\). Hence the selected vector is
\(Au=((g-1)u_1,2u_1+u_2)^{\mathsf T}\). At the initial step this dominates the
carried degree-one vector because \(g\ge5\). At later steps, the preceding
intermediate vector is \(Au_{n-1}\), while \(u_n\) is componentwise larger
than \(u_{n-1}\) (Lemma 4 below), so monotonicity of the nonnegative matrix
\(A\) gives \(Au_n>Au_{n-1}\) componentwise. \(\square\)

### Lemma 3 (the \(T\)-face selectors)

If \(u\in\mathcal C\) and \(v=Au\), then the gradient terms in the second
shear have exact degree vector \(Bv\), and they strictly dominate the carried
\(q\)-vector.

**Proof.** We have
\[
 \partial_{p_1}W=2p_1p_2^2,
 \qquad \partial_{p_2}W=2p_1^2p_2+gp_2^{g-1}.
\]
The first coordinate has degree \(v_1+2v_2\), which is larger than \(u_1\)
because \(v_1=(g-1)u_1\) and \(v_2=2u_1+u_2\). For the second coordinate,
the claimed face \(gp_2^{g-1}\) dominates the cross term precisely when
\[
 (g-1)v_2>2v_1+v_2
 \quad\Longleftrightarrow\quad
 \frac{v_2}{v_1}>\frac2{g-2}.
\]
But
\[
 \frac{v_2}{v_1}=\frac{2+u_2/u_1}{g-1}
 \ge\frac3{g-1}>\frac2{g-2}
\]
for \(g>4\). The selected vector is therefore
\(Bv=(v_1+2v_2,(g-1)v_2)^{\mathsf T}\). Its carried-coordinate gaps are
\[
 v_1+2v_2-u_1=(g+2)u_1+2u_2>0,
 \qquad
 (g-1)v_2-u_2=2(g-1)u_1+(g-2)u_2>0.
\]
\(\square\)

### Lemma 4 (two-phase cone invariance)

For \(u\in\mathcal C\), \(Cu\in\mathcal C\), and \(Cu>u\) componentwise.

**Proof.** Put \(r=u_2/u_1\) and \(R=(g-2)/2\). The new ratio is
\[
 f_g(r)=\frac{(g-1)(2+r)}{g+3+2r}.
\]
The denominator is positive and
\[
 f_g(1)=\frac{3(g-1)}{g+5}>1.
\]
At the upper endpoint,
\[
 f_g(R)=\frac{(g-1)(g+2)}{2(2g+1)}<\frac{g-2}{2}=R,
\]
because the difference after clearing positive denominators is \(g(g-4)>0\).
The fractional-linear map has positive derivative
\( (g-1)(g-1)/(g+3+2r)^2\), so these endpoint inequalities imply
\(1\le f_g(r)<R\) for \(1\le r<R\). Finally,
\[
 (Cu)_1-u_1=(g+2)u_1+2u_2>0,
\]
\[
 (Cu)_2-u_2=2(g-1)u_1+(g-2)u_2>0.
\]
This is a two-phase statement: after the \(S\)-phase the second selector is
evaluated on \(v=Au\); after the \(T\)-phase the full state returns to the
\(q\)-phase. No single strict cone \(\{Au>v,Bv>u\}\) is asserted, since
the completed step necessarily has the equality \(v_{n+1}=Au_n\). \(\square\)

### Lemma 5 (no cancellation)

For the displayed positive integer coefficients, every selected leading
monomial has a positive coefficient in every iterate, and no selected degree
can cancel with a competing term.

**Proof.** Starting from coordinate monomials with coefficient one, both
shears use additions and multiplication by the positive integers \(2\) and
\(g\). Thus all coefficients in all iterated coordinate polynomials are
nonnegative integers. Lemmas 2 and 3 give strict degree gaps between the
selected monomial and every competitor, so a cancellation at the selected
degree is impossible. The characteristic-zero hypothesis ensures these
positive integers remain nonzero in \(K\). \(\square\)

### Lemma 6 (exact recurrence and observable degree)

For every \(n\ge0\), with \(v_{n+1}\) the intermediate vector,
\[
 v_{n+1}=Au_n,\qquad u_{n+1}=Bv_{n+1}=Cu_n.
\]
For \(n\ge1\), \(\deg(F^n)=u_{n,2}=e_2^{\mathsf T}u_n\).

**Proof.** The first two identities are Lemmas 2 and 3. Induction starts at
\(u_0=(1,1)\), and Lemma 4 keeps the selectors valid. The second component of
\(u_n\) is strictly larger than the first for \(n\ge1\). Moreover,
\(u_n\) dominates the preceding intermediate vector \(Au_{n-1}\) componentwise
by the explicit inequalities
\[
 (Cu)_1-(Au)_1=4u_1+2u_2>0,
 \qquad
 (Cu)_2-(Au)_2=(2g-4)u_1+(g-2)u_2>0,
\]
Since the final \(p\)-coordinates are \(v_n=Au_{n-1}\), these same inequalities
put both \(p\)-degrees below the corresponding \(q\)-degrees. Together with
\(u_{n,2}>u_{n,1}\) for \(n\ge1\), every coordinate of \(F^n\) has degree at
most \(u_{n,2}\), while \(q_{2,n}\) has exactly that degree. \(\square\)

### Lemma 7 (Perron calculation)

The matrix \(C\) is positive and has eigenvalues
\[
 \lambda_\pm=g+1\pm2\sqrt g=(\sqrt g\pm1)^2.
\]
Thus \(\rho(C)=(\sqrt g+1)^2\).

**Proof.** Its trace is \(2g+2\), determinant is \((g-1)^2\), and the
discriminant is \(16g\). Positivity gives a simple Perron root and a positive
eigenvector. \(\square\)

## 3. Headline theorem

**Theorem (asymmetric coupled-shear degree matrix).** For every integer
\(g\ge5\), the map \(F_g\) above is a symplectic polynomial automorphism of
\(\mathbb A^4_K\). Its iterated degrees satisfy
\[
 \deg(F_g^n)=e_2^{\mathsf T}C_g^n\binom11\quad(n\ge1),
\]
and its first dynamical degree is
\[
 \lambda_1(F_g)=(\sqrt g+1)^2.
\]
Each elementary shear has degree \(g-1\), whereas
\[
 \lambda_1(F_g)<(g-1)^2.
\]
The support hypergraph on \(\{1,2\}\) is connected through the mixed
monomials, so the displayed map is not a product with respect to the given
coordinate split. The theorem does not assert non-conjugacy to every possible
product coordinate system.

**Proof.** Lemma 1 gives symplectic polynomial automorphisms. Lemmas 2–5 give
the exact two-phase recurrence for all iterates, and Lemma 6 identifies the
observable total degree. Lemma 7 and Perron–Frobenius yield the limit. The
individual shear degree is \(g-1\) because the pure power in each selected
gradient has that degree and all other displayed gradient terms have degree at
most three. Finally,
\[
 (g-1)^2-(\sqrt g+1)^2
 =\sqrt g(\sqrt g-2)(\sqrt g+1)^2>0
\]
for \(g>4\). \(\square\)

## 4. Matrix-phase warning

The complete one-step degree matrix on the stacked phase vector is
\[
 \widehat M_g=\begin{pmatrix}C_g&0\\A_g&0\end{pmatrix},
\]
not \(\begin{pmatrix}0&B_g\\A_g&0\end{pmatrix}\). The latter records two
half-steps and its spectral radius must be interpreted with a square or period
correction. The nonzero spectrum of \(\widehat M_g\) is the spectrum of
\(C_g\). Any later extension with multiple selector phases must use an
explicit phase-lift and a period-product root.

## 5. Proof gates before any manuscript claim

`G1` literal monomial selector inequalities are written for every \(g\ge5\).
`G2` carried-coordinate domination is checked at \(n=0\) and inductively.
`G3` positivity/no-cancellation is stated over characteristic zero, not inferred
from a numerical sample. `G4` the degree functional \(e_2\) sees the Perron
class. `G5` the support graph remains connected. Failure of any gate is a
design STOP, not an invitation to widen the family.
