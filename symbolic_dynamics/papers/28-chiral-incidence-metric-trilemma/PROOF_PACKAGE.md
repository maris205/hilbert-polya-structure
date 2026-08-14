# Proof package — Paper 28 / SD-C30

## 1. Operator setting

Fix \(\eta>1\) and

\[
\mathcal H_\eta
=\left\{x=(x_n)_{n\ge1}:
\sum_{n\ge1}n^{2\eta}|x_n|^2<\infty\right\}.
\]

The divisibility zeta and Möbius operators are denoted by \(Z\) and
\(M=Z^{-1}\). They are bounded and boundedly invertible in this range.
For the coordinate idempotent \(E_n\), set

\[
q_n=ZE_nM.
\]

Then \(q_nq_m=\delta_{nm}q_n\). The cover atoms of the unmutated
divisibility poset are the primes. With \(A\) the atom set, define

\[
D_s^A=\sum_{p\in A}p^{-s}E_p,
\qquad
T_s=\sum_{p\in A}p^{-s}q_p=ZD_s^AM.
\]

Let \(J\) be the coordinate conjugation in normalized orthonormal
coordinates. For an operator whose matrix is source-real, define the
complex-linear reflection

\[
X^\sharp=JX^*J.
\]

In unnormalized source coordinates this is
\(W_\eta^{-1}X^{\mathsf T}W_\eta\), where
\(W_\eta=\operatorname{diag}(n^{2\eta})\). The map \(\sharp\) is an
isometry on every Schatten ideal and reverses products.

Define the holomorphic reflected block

\[
\mathcal B_s=
\begin{pmatrix}
0&T_s\\
T_{1-s}^{\sharp}&0
\end{pmatrix}.
\]

All critical-line theorems below use the arithmetic specialization
\(u=1\). If the inherited digit marker is retained as
\[
T_s(u)=\sum_pu^{\ell(p)}p^{-s}q_p,
\]
then \(r\) repetitions of atom \(p\) carry \(u^{r\ell(p)}\). For
\(|u|<1\), this additional decay changes the Schatten domain. The
resulting family is not a continuation argument for the \(u=1\)
operator.

## 2. Schatten threshold and critical self-adjointness

### Theorem 2.1 — exact Schatten criterion

For every \(q\ge1\),

\[
T_s\in\mathcal S_q
\quad\Longleftrightarrow\quad
\sum_{p\in A}p^{-q\Re s}<\infty.
\]

For the prime atom set this is equivalent to \(q\Re s>1\).

#### Proof

Since \(T_s=ZD_s^AZ^{-1}\), the ideal property gives
\[
D_s^A\in\mathcal S_q\Longrightarrow T_s\in\mathcal S_q.
\]
Conversely \(D_s^A=Z^{-1}T_sZ\), so the reverse implication follows
from the same property. Relative to the normalized coordinate basis,
\(D_s^A\) is diagonal with singular values \(p^{-\Re s}\). This proves
the sum criterion.

For primes, the sum converges when \(q\Re s>1\) by comparison with the
integer Dirichlet series. At equality it is Euler's divergent prime
harmonic series. Below equality its terms eventually dominate \(1/p\).
∎

### Theorem 2.2 — common reflected strip

For every \(q\ge1\),

\[
\mathcal B_s\in\mathcal S_q
\quad\Longleftrightarrow\quad
\frac1q<\Re s<1-\frac1q.
\]

This strip is nonempty exactly for \(q>2\). Hence \(q=3\) is the first
integer order admitting the critical line, and

\[
\mathcal B_{1/2+it}\in\bigcap_{q>2}\mathcal S_q,
\qquad
\mathcal B_{1/2+it}\notin\mathcal S_2.
\]

#### Proof

For a block operator \(B=\bigl(\begin{smallmatrix}0&A\\C&0\end{smallmatrix}\bigr)\),
\[
B^*B=\operatorname{diag}(C^*C,A^*A).
\]
Therefore \(B\in\mathcal S_q\) iff \(A,C\in\mathcal S_q\). By
Theorem 2.1 and the isometry of \(\sharp\), the two conditions are
\(q\Re s>1\) and \(q(1-\Re s)>1\). Solving gives the open strip.
At \(\Re s=1/2\), these inequalities hold precisely for \(q>2\).
The failure at \(q=2\) is exact, not a missing estimate. ∎

### Proposition 2.3 — critical-line self-adjointness

For real \(t\),

\[
\mathcal B_{1/2+it}=\mathcal B_{1/2+it}^*.
\]

#### Proof

The incidence idempotents are source-real. Thus
\[
T_s^*=\sum_p p^{-\overline s}q_p^*.
\]
When \(s=1/2+it\), \(\overline s=1-s\), and the definition of the
holomorphic reflection gives \(T_{1-s}^{\sharp}=T_s^*\). The two
off-diagonal blocks are adjoints. ∎

### Scope corollary

The proposition produces a compact self-adjoint operator for each \(t\),
but the operator itself depends on \(t\). It is not a fixed operator
whose eigenvalue parameter is \(t\). This distinction is logically
independent of self-adjointness and forces the strict A3 failure.

## 3. Exact native Gram geometry

In source coordinates,

\[
q_n=u_nv_n^{\mathsf T},
\qquad
u_n(a)=\mathbf1_{a\mid n},
\qquad
v_n(b)=\mu(b/n)\mathbf1_{n\mid b}.
\]

Set

\[
G_{pq}=\operatorname{Tr}(q_pq_q^\sharp),
\qquad
C_\eta=\sum_{k\ge1}\frac{\mu(k)^2}{k^{2\eta}}
=\frac{\zeta(2\eta)}{\zeta(4\eta)}.
\]

### Theorem 3.1 — closed Gram formulas

For primes \(p,q\),

\[
G_{pp}=C_\eta(1+p^{-2\eta}),
\]

and for \(p\ne q\),

\[
G_{pq}
=C_\eta
\frac{(pq)^{-2\eta}}
{(1+p^{-2\eta})(1+q^{-2\eta})}>0.
\]

#### Proof

The weighted rank-one contraction is

\[
G_{pq}
=
\left(\sum_a u_p(a)u_q(a)a^{2\eta}\right)
\left(\sum_b v_p(b)v_q(b)b^{-2\eta}\right).
\]

For \(p=q\), the primal sum is \(1+p^{2\eta}\), while the dual
sum is
\[
\sum_{b:p\mid b}\mu(b/p)^2b^{-2\eta}
=p^{-2\eta}C_\eta.
\]
Their product gives the diagonal formula.

For distinct primes, the only common divisor in the primal sum is \(1\).
A nonzero dual summand has \(b=pqk\), with \(k\) squarefree and
coprime to \(pq\). Both Möbius factors change sign, so their product is
\(+1\). Hence the dual sum is
\[
(pq)^{-2\eta}
\sum_{\substack{k\ {\rm squarefree}\\(k,pq)=1}}k^{-2\eta}
=C_\eta
\frac{(pq)^{-2\eta}}
{(1+p^{-2\eta})(1+q^{-2\eta})}.
\]
This is strictly positive. ∎

### Proposition 3.2 — exact finite two/three-atom trace

For a finite atom set \(F\) and \(s=1/2+it\),

\[
\operatorname{Tr}\mathcal B_s^2
=2\sum_{p\in F}\frac{G_{pp}}p
+4\sum_{\substack{p<q\\p,q\in F}}
\frac{G_{pq}}{\sqrt{pq}}
\cos\left(t\log\frac qp\right).
\]

For two atoms this has one cosine; for three atoms it has the three
pair frequencies.

#### Proof

Since the two diagonal blocks of \(\mathcal B_s^2\) have the same trace,
\[
\operatorname{Tr}\mathcal B_s^2
=2\operatorname{Tr}(T_sT_s^*)
=2\sum_{p,q\in F}
p^{-1/2-it}q^{-1/2+it}G_{pq}.
\]
The Gram matrix is real symmetric. Pairing \((p,q)\) with \((q,p)\)
gives the cosine identity. ∎

### Proposition 3.3 — the infinite second trace does not exist

On the critical line, \(\mathcal B_s^2\notin\mathcal S_1\). More
specifically, the diagonal cutoff contribution diverges:

\[
\sum_p\frac{2G_{pp}}p
\ge2C_\eta\sum_p\frac1p=\infty.
\]

Therefore every displayed \(B^2\) trace is a finite-cutoff diagnostic;
it is not the trace of the countable operator.

## 4. The first honest regularized determinant

On \(1/3<\Re s<2/3\), define

\[
\det{}_3(I-z\mathcal B_s).
\]

### Proposition 4.1 — deletion ledger

Near \(z=0\),

\[
\log\det{}_3(I-z\mathcal B_s)
=-\sum_{m\ge3}\frac{z^m}{m}
\operatorname{Tr}(\mathcal B_s^m).
\]

Powers \(1,2\) are deleted by the regularization. Every odd block trace
vanishes, so the first visible term is

\[
-\frac{z^4}{4}\operatorname{Tr}(\mathcal B_s^4).
\]

#### Proof

This is the standard third modified Fredholm determinant expansion.
Odd powers of an off-diagonal block operator remain off diagonal and
have zero trace whenever they are trace class. Since
\(\mathcal B_s\in\mathcal S_3\), every power \(m\ge3\) is trace class.
∎

### Theorem 4.2 — exact fourth-moment motion

For distinct primes \(p,q\), the cosine coefficient at frequency
\(2\log(q/p)\) in
\(\operatorname{Tr}\mathcal B_{1/2+it}^{4}\) equals

\[
\frac{4G_{pq}^2}{pq}>0.
\]

Consequently the native compact self-adjoint spectrum genuinely varies
with \(t\), and \(\det_3(I-z\mathcal B_{1/2+it})\) is nonconstant in
\(t\) as an analytic germ in \(z\).

#### Proof

Write \(a_p=p^{-1/2-it}\). Then

\[
T_sT_s^*=\sum_{p,q}a_p\overline{a_q}\,q_pq_q^*
\]

and

\[
\operatorname{Tr}\mathcal B_s^4
=2\operatorname{Tr}\bigl((T_sT_s^*)^2\bigr).
\]

In the square, the tuple \((p,q,p,q)\) contributes

\[
a_p^2\overline{a_q}^{\,2}
\operatorname{Tr}\bigl((q_pq_q^*)^2\bigr).
\]

The operator \(q_pq_q^*\) has rank at most one, so

\[
\operatorname{Tr}\bigl((q_pq_q^*)^2\bigr)
=\operatorname{Tr}(q_pq_q^*)^2=G_{pq}^2.
\]

Pairing with the conjugate tuple yields a cosine. The outer factor \(2\)
gives \(4G_{pq}^2/(pq)\).

It remains to rule out cancellation. A second four-index term at this
frequency would require a quotient of two products of two primes to
equal \(q^2/p^2\). Unique factorization forces the numerator multiset
to be \(\{q,q\}\) and the denominator multiset to be \(\{p,p\}\).
Thus the coefficient is isolated.

Finally, prime cutoffs converge uniformly in \(\mathcal S_4\) for all
real \(t\), because the diagonal tail has \(t\)-independent
\(\ell^4\) norm and bounded similarity preserves it. The fourth trace
moment is continuous on bounded subsets of \(\mathcal S_4\), so the
finite Fourier coefficient passes to the countable limit. ∎

## 5. Positive metric rigidity

### Theorem 5.1 — full-family metric classification

Let \(q_n=ZE_nZ^{-1}\), and let \(G\) be bounded, positive, and
boundedly invertible. Then

\[
Gq_n=q_n^*G\quad\hbox{for every }n
\]

if and only if

\[
Z^*GZ=D
\]

for a positive bounded diagonal \(D\) with bounded inverse.
Equivalently,

\[
G=Z^{-*}DZ^{-1}.
\]

#### Proof

Multiply \(GZE_nZ^{-1}=Z^{-*}E_nZ^*G\) on the left by \(Z^*\)
and on the right by \(Z\). With \(K=Z^*GZ\), the condition becomes

\[
KE_n=E_nK\quad\hbox{for every }n.
\]

The joint commutant of all coordinate projections is the diagonal
algebra. Positivity and bounded invertibility transfer between \(G\)
and \(K\) under bounded congruence. The converse follows by reversing
the calculation. ∎

### Theorem 5.2 — active-family metric classification

If \(Gq_p=q_p^*G\) is required only for active atoms \(p\in A\), then
\(K=Z^*GZ\) has no coupling between any active coordinate and another
coordinate, is diagonal on the active sector, and may have an arbitrary
positive block on the dormant complement.

#### Proof

The condition is \(KE_p=E_pK\) for every \(p\in A\). Commutation with
a rank-one coordinate projection annihilates its row and column away
from the diagonal. Applying this to every active coordinate gives the
stated decomposition. ∎

### Corollary 5.3 — Hellinger/Löwdin atom collapse

Let \(S=G^{1/2}\), \(K=Z^*GZ\), and

\[
U=SZK^{-1/2}.
\]

Then \(U\) is unitary and

\[
ST_sS^{-1}=UD_s^AU^*.
\]

Thus every positive common orthogonalizing metric makes the active
family a set of mutually orthogonal coordinate atoms.

#### Proof

\[
U^*U=K^{-1/2}Z^*GZK^{-1/2}=I.
\]
By Theorem 5.2, \(K\) commutes with \(D_s^A\). Conjugating \(T_s\)
and inserting \(K^{1/2}K^{-1/2}\) gives the displayed identity. ∎

### Corollary 5.4 — phase-free regularized product

In the orthogonalized atom basis, the reflected double is a direct sum
of blocks

\[
\begin{pmatrix}
0&p^{-s}\\p^{-(1-s)}&0
\end{pmatrix},
\]

each of which squares to \(p^{-1}I_2\). Therefore

\[
\det{}_3(I-z\widehat{\mathcal B}_s)
=\prod_p
\left(1-\frac{z^2}{p}\right)
\exp\left(\frac{z^2}{p}\right).
\]

The product converges and is independent of \(s,t\).

#### Proof

The block eigenvalues are \(\pm p^{-1/2}\). In the third modified
determinant the linear exponential corrections cancel between the pair,
while the quadratic corrections combine to \(\exp(z^2/p)\). The
logarithm of each factor is \(O(p^{-2})\), proving convergence.
Neither the eigenvalues nor the product retains a phase. ∎

## 6. Logical conclusion

The native completion has an honest \(\mathcal S_3\) determinant and
real fourth-moment motion. Exact non-arithmetic controls show that the
motion is generic oblique-incidence geometry. Every positive completion
that removes the obliqueness simultaneously diagonalizes the active
atoms and erases the motion. These statements prove a scoped canonical
completion trilemma; they do not prove that every imaginable indefinite,
unbounded, or non-source-natural completion collapses.
