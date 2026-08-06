# Derivation package

## 1. Frozen dynamical object

Let \(R=\mathbb Z[1/2]\), \(X_2=\widehat{R^2}\), and

\[
A=\begin{pmatrix}3&1\\1&3\end{pmatrix},\qquad
B=\begin{pmatrix}3&2\\2&4\end{pmatrix}.
\]

For \(M\in GL_2(R)\), define \(\alpha_M=\widehat{M^{\mathsf T}}\). This
transpose convention makes

\[
\alpha_M\circ\alpha_N=\alpha_{MN}.
\]

On \(\Sigma_2\times X_2\), set

\[
F(\omega,x)=(\sigma\omega,\alpha_{M_{\omega_0}}x).
\]

For \(w=w_0\cdots w_{n-1}\), the return matrix is

\[
M_w=M_{w_{n-1}}\cdots M_{w_0}.
\]

A cyclic rotation gives a conjugate matrix in \(GL_2(R)\); a repeated word
gives \(M_{w^r}=M_w^r\). Thus fixed-point data descend to necklaces while
retaining the correct repetition law.

## 2. Expansion and fixed-point index

The eigenvalues of \(A\) are \(4,2\). The eigenvalues of \(B\) are

\[
\beta=\frac{7+\sqrt{17}}2,
\qquad
\gamma=\frac{7-\sqrt{17}}2>1.
\]

Both matrices are symmetric positive definite. Singular values obey

\[
s_{\min}(M_w)\ge\gamma^n>1,
\qquad
\|M_w\|_2\le\beta^n.
\]

Every archimedean eigenvalue of \(M_w\) therefore has modulus greater than
\(1\). If the
eigenvalues are real, positivity of trace and determinant makes both positive;
otherwise they are conjugate. In both cases

\[
D_w=\det(I-M_w)>0.
\]

Since \(\det M_w=8^n\),

\[
D_w=8^n-\operatorname{tr}M_w+1,
\]

and the trace norm bound gives

\[
8^n-2\beta^n+1\le D_w\le8^n+1.
\tag{1}
\]

Dualizing \(I-M_w^{\mathsf T}\) identifies the fixed subgroup with the dual
of its cokernel over \(R\). Smith normal form over the localized PID gives

\[
\#\operatorname{Fix}(\alpha_{M_w})
=|D_w|_\infty|D_w|_2
=\frac{D_w}{2^{\nu_2(D_w)}}.
\tag{2}
\]

## 3. Rational archimedean control

For the torus comparison, the same word has \(D_w\) fixed points. Summing all
based words preserves the noncommutative expansion:

\[
\sum_{|w|=n}M_w=(A+B)^n.
\]

Therefore

\[
N_n^{(\infty)}=2^n+16^n-\operatorname{tr}\bigl((A+B)^n\bigr).
\tag{3}
\]

Writing \(S=A+B\), with \(\operatorname{tr}S=13\) and \(\det S=33\), and using

\[
\log\det(I-zS)
=-\sum_{n\ge1}\frac{\operatorname{tr}(S^n)}n z^n,
\]

gives

\[
Z_\infty(z)
=\frac{\det(I-zS)}{(1-2z)(1-16z)}
=\frac{1-13z+33z^2}{(1-2z)(1-16z)}.
\tag{4}
\]

## 4. Exact mod-\(2\) symbolic classification

Modulo \(2\), write

\[
J=\bar A=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
E=\bar B=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

The relations

\[
J^2=0,\qquad E^2=E,\qquad (EJ)^2=EJ,\qquad
\operatorname{tr}(EJ)=1
\]

give an iff statement.

If a cyclic word contains \(aa\), rotate its product until \(J^2\) is an
adjacent factor. Cyclic trace invariance then gives trace zero modulo \(2\).
If it has no cyclic \(aa\), either it is all \(b\), with reduction \(E\), or,
after compressing each \(b\)-run, its cyclic trace is
\(\operatorname{tr}(EJ)^k=1\). Hence

\[
2\mid D_w
\Longleftrightarrow
\operatorname{tr}M_w\equiv1\pmod2
\Longleftrightarrow
w\text{ is cyclically }aa\text{-free}.
\tag{5}
\]

The number of based length-\(n\) cyclic words with no \(aa\) is

\[
L_n=\operatorname{tr}
\begin{pmatrix}0&1\\1&1\end{pmatrix}^{\!n}
=\varphi^n+(-\varphi^{-1})^n.
\tag{6}
\]

## 5. Congruence tower

For every positive integer \(d\),

\[
2^{-\nu_2(d)}
=1-\sum_{k\ge1}2^{-k}\mathbf1_{2^k\mid d}.
\]

Thus

\[
N_n^{(2)}
=N_n^{(\infty)}
-\sum_{k\ge1}2^{-k}C_{n,k},
\qquad
C_{n,k}=\sum_{\substack{|w|=n\\2^k\mid D_w}}D_w.
\tag{7}
\]

At each fixed \(k\), chronological multiplication modulo \(2^k\) is a finite
monoid recurrence. To retain the integer trace mass, attach to every residue
state \(g\) both its word count and the matrix sum of all integer lifts ending
at \(g\). The code checks these finite-state layer masses against direct word
enumeration. Equation (7) is coefficientwise finite and exact.

## 6. Global correction scale

Let

\[
\Delta_n=N_n^{(\infty)}-N_n^{(2)}.
\]

Only the \(L_n\) words from (6) contribute. On each such word \(D_w\) is even,
so

\[
\frac{D_w}{2}\le D_w-\operatorname{oddpart}(D_w)<D_w.
\]

Using (1), for all sufficiently large \(n\),

\[
\frac12(8^n-2\beta^n+1)L_n
\le\Delta_n\le(8^n+1)L_n.
\tag{8}
\]

It follows that

\[
\lim_{n\to\infty}\Delta_n^{1/n}=8\varphi.
\tag{9}
\]

Let

\[
G(z)=\sum_{n\ge1}\frac{\Delta_n}{n}z^n.
\]

Its radius is exactly \(R=(8\varphi)^{-1}\), and coefficient positivity plus
the lower bound in (8) gives \(G(r)\to+\infty\) as \(r\uparrow R\). Near the
origin,

\[
Z_2(z)=Z_\infty(z)e^{-G(z)}.
\tag{10}
\]

The factor \(e^{-G}\) is analytic and zero-free for \(|z|<R\). The numerator
zeros in (4) have moduli

\[
\frac2{13+\sqrt{37}}\approx0.10481,
\qquad
\frac2{13-\sqrt{37}}\approx0.28913,
\]

both larger than \(R\approx0.07725\). The only divisor of \(Z_\infty\) in
that disk is the simple pole \(z=1/16\). Therefore \(Z_2\) has exactly that
simple pole and no zeros for \(|z|<R\). Its Taylor radius is \(1/16\), but it
has meromorphic continuation across the whole first circle.

Equation (9) does not prove that \(e^{-G}\) has a natural boundary, or even a
nonremovable singularity, at every point of \(|z|=R\). Exponentiation can in
principle regularize a logarithmic singularity. The later boundary remains
open.

## 7. Primitive analytic-type dichotomy

Let \(w\) be a primitive base necklace of length \(\ell\), with

\[
f_w(x)=x^2-t_wx+2^{3\ell}.
\]

If \(t_w\) is even, then \(f_w(x)\equiv x^2\pmod2\). Cayley--Hamilton gives
\(M_w^2\equiv0\pmod2\), and \(\det(I-M_w^r)\) is odd for every \(r\ge1\).
Hence the solenoid and torus return zetas coincide:

\[
\zeta_{\alpha_{M_w}}(u)
=\frac{1-t_wu+2^{3\ell}u^2}
{(1-u)(1-2^{3\ell}u)}.
\tag{11}
\]

If \(t_w\) is odd, then
\(f_w(x)\equiv x(x+1)\pmod2\). Hensel lifting gives one \(2\)-adic unit root
and one root of valuation \(3\ell\). The real eigenvalues have modulus greater
than \(1\). Bell--Miles--Ward Theorem 15 therefore gives a natural boundary
for the return zeta at

\[
|u|=2^{-3\ell}.
\]

After substituting \(u=z^\ell\), the invariant base-orbit subsystem has its
natural boundary at \(|z|=1/8\).

The exact period-five witness is

\[
\begin{array}{c|c|c|c|c}
w&t_w&D_w&\nu_2(D_w)&\#\mathrm{Fix}\\ \hline
\texttt{aabbb}&2734&30035&0&30035\\
\texttt{ababb}&2727&30042&1&15021.
\end{array}
\]

Both words contain two \(a\)'s and three \(b\)'s and are primitive and
nonconjugate. Thus abelianization cannot recover even the analytic type of
their fibre zeta.

For the boundary word, let \(\xi\) be its \(2\)-adic unit eigenvalue. The
other eigenvalue contributes a unit to \(1-\eta^r\), while

\[
\nu_2(\xi-1)=1,
\qquad
\nu_2(\xi+1)=3.
\]

The \(2\)-adic lifting-the-exponent formula yields

\[
\nu_2\det(I-M_w^r)=
\begin{cases}
1,&r\text{ odd},\\
3+\nu_2(r),&r\text{ even}.
\end{cases}
\tag{12}
\]

## 8. Primitive-orbit factorization and scope

Regrouping based periodic words by primitive base necklaces gives the exact
formal identity

\[
Z_F(z)=\prod_{[w]\,\mathrm{primitive}}
\zeta_{\alpha_{M_w}}(z^{|w|}).
\tag{13}
\]

An individual natural-boundary factor in (13) does not imply a natural
boundary for the full infinite product. In fact (10) proves that the full
zeta crosses its first circle, whereas each active primitive factor has its
boundary at the larger radius \(1/8\). No cancellation or convergence claim
outside the proved disk is silently assumed.

## 9. Hilbert--Pólya boundary

The primary pole \(16=2\cdot8\) is the transparent product of base branching
and fibre degree. The secondary scale \(8\varphi\) is the fibre degree times
golden-mean symbolic growth. Neither scale supplies \(\log p\) primitive
periods, von Mangoldt amplitudes, the xi functional equation, or a
self-adjoint operator. These exact theorems therefore close HCS-C14 as a
Hilbert--Pólya candidate while preserving it as an arithmetic-dynamics result.
