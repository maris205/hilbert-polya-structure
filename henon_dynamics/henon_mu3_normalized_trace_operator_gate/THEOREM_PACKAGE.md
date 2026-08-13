# HCS-C47 theorem package

## 1. Graded Galois-sector algebra

For a split prime \(p\), put \(d_p=(p-1)/2\) and let \([a]\) run over
\(\mathbf F_p^\times/\{\pm1\}\).  The sector dimensions are

\[
d_0=(p+2)/3,
\qquad d_1=d_2=(p-1)/3.
\]

Let \(\mathcal H_{a,k}\) be the sector Hilbert space on which the unitary
\(T_{a,k}\) acts.  For every \([a]\), define

\[
\begin{aligned}
\mathcal H_{p,[a]}^+
 &=\mathcal H_{a,0}^{\oplus2}\oplus
   \mathcal H_{-a,0}^{\oplus2},\\
W_{p,[a]}^+
 &=T_{a,0}^{\oplus2}\oplus T_{-a,0}^{\oplus2},
\end{aligned}
\]

and let the negative space and operator contain one copy of each of

\[
T_{a,1},T_{a,2},T_{-a,1},T_{-a,2}.
\]

Thus \(\mathcal H_{p,[a]}^-\) is the direct sum of the four corresponding
sector spaces and \(W_{p,[a]}^-\) is the direct sum of these four operators.
Including both \(a\) and \(-a\) makes the construction independent of the
representative of \([a]\).  Sum over all real Galois classes and put

\[
\mathcal H_p^\pm=\bigoplus_{[a]}\mathcal H_{p,[a]}^\pm,
\qquad
W_p^\pm=\bigoplus_{[a]}W_{p,[a]}^\pm,
\qquad
W_p=W_p^+\oplus W_p^-.
\]

Let \(\Gamma_p=+I\oplus-I\).  On

\[
\mathcal M_p=B(\mathcal H_p^+)\oplus B(\mathcal H_p^-)
\]

put the positive field-degree-normalized trace

\[
\tau_p(A_+\oplus A_-)
=d_p^{-1}(\operatorname{Tr}A_++\operatorname{Tr}A_-), \tag{1}
\]

and the associated supertrace

\[
\operatorname{str}_p(A)=\tau_p(\Gamma_pA). \tag{2}
\]

The trace is faithful and positive, but it is not a tracial state:
\(\tau_p(I)\ne1\).

Then

\[
\tau_p(I)=\frac{8p+4}{3}, \tag{3}
\]

and the C45 normalized chronological moments satisfy

\[
\boxed{\operatorname{str}_p(W_p^n)=c_{p,n}}. \tag{4}
\]

Consequently, on \(|z|<1\),

\[
G_p(z)=\exp\operatorname{str}_p\Log_0(I-zW_p). \tag{5}
\]

The fractional C46 divisor orders are normalized projection dimensions in
this algebra; they are no longer required to be integers.

## 2. Exact Schatten threshold

Let

\[
\mathcal M=\prod_{p\equiv1\ (3)}\mathcal M_p,
\qquad
\mathcal H=\bigoplus_p(\mathcal H_p^+\oplus\mathcal H_p^-),
\qquad
X_s=\bigoplus_pp^{-s}W_p. \tag{6}
\]

For a positive element \(A=(A_p)_p\), define
\(\tau(A)=\sum_p\tau_p(A_p)\).  This is a faithful normal semifinite trace on
\(\mathcal M\).  Put \(\Gamma=\bigoplus_p\Gamma_p\).  For every \(q>0\),
since every \(W_p\) is unitary,

\[
\tau(|X_s|^q)
=\sum_{p\equiv1\ (3)}\frac{8p+4}{3}p^{-q\sigma},
\qquad \sigma=\operatorname{Re}s. \tag{7}
\]

The prime series gives the sharp equivalence

\[
\boxed{X_s\in L^q(\mathcal M,\tau)
\Longleftrightarrow q\sigma>2}. \tag{8}
\]

Indeed, for \(q\sigma>2\) the summand in (7) is dominated by a constant
multiple of \(p^{-(q\sigma-1)}\), whose sum converges even over all positive
integers.  If \(q\sigma\le2\), it dominates a constant multiple of \(1/p\);
the Euler--Dirichlet theorem gives
\(\sum_{p\equiv1\ (3)}p^{-1}=\infty\).

In particular:

\[
\begin{array}{c|c}
\text{class}&\text{half-plane}\\ \hline
L^1&\sigma>2\\
L^2&\sigma>1\\
L^3&\sigma>2/3\\
L^4&\sigma>1/2
\end{array} \tag{9}
\]

As a bounded operator on \(\mathcal H\), \(X_s\) is compact exactly for
\(\sigma>0\); it is bounded and noncompact for \(\sigma=0\), and unbounded
for \(\sigma<0\).  The grading does not improve positive Schatten
summability, because \(|\Gamma X_s|=|X_s|\).

## 3. Fourth-order regularized graded determinant

The functional \(\operatorname{str}(A)=\tau(\Gamma A)\) is used globally only
when \(A\in L^1(\mathcal M,\tau)\).  For \(\sigma>1/2\), one has
\(X_s\in L^4\) and

\[
\|X_s\|=7^{-\sigma}<1.
\]

Let \(X_s^\pm\) be the two graded restrictions and let \(\tau_\pm\) be the
corresponding restrictions of \(\tau\).  Define

\[
\det_{4,\tau_\pm}(I-X_s^\pm)
=\exp\!\left(-\sum_{n\ge4}
 \frac{\tau_\pm((X_s^\pm)^n)}n\right)
\]

and

\[
\det_{4,\tau,\rm gr}(I-X_s)
=\frac{\det_{4,\tau_+}(I-X_s^+)}
       {\det_{4,\tau_-}(I-X_s^-)}
=\exp\!\left(-\sum_{n\ge4}
 \frac{\operatorname{str}(X_s^n)}n\right). \tag{10}
\]

This is legitimate because \(X_s^4\in L^1\) and, for \(n\ge4\),

\[
\big|\operatorname{str}(X_s^n)\big|
\le \tau(|X_s|^n)
\le \|X_s\|^{n-4}\tau(|X_s|^4).
\]

The same estimate is uniform on compact subsets of \(\sigma>1/2\), so the
series is locally normally convergent and defines a holomorphic, nonzero
graded regularized determinant.  Put

\[
\ell_n(s)=\sum_pc_{p,n}p^{-ns},\qquad n=1,2,3. \tag{11}
\]

The first-moment identity and the uniform H\'enon moment bound give normal
convergence of \(\ell_1,\ell_2,\ell_3\) respectively on
\(\sigma>0,\sigma>1/2,\sigma>1/3\).  On \(\sigma>1/2\) they are therefore
all holomorphic.  Outside the individual positive \(L^n\) domains, these are
convergent sums of **local** supertraces; they are not applications of the
global semifinite trace to the non-\(L^1\) operators \(X_s^n\).  Therefore

\[
\boxed{
\mathcal G(s)=
\exp\!\left(-\ell_1(s)-\frac{\ell_2(s)}2-\frac{\ell_3(s)}3\right)
\det_{4,\tau,\rm gr}(I-X_s)}. \tag{12}
\]

This is an exact equality of canonical logarithms, not a fitted
renormalization.  Order four is the smallest fixed integer Schatten order
valid on the whole half-plane \(\sigma>1/2\).  Since every \(c_{p,n}\) is
rational, normal convergence also gives
\[
\mathcal G(\overline s)=\overline{\mathcal G(s)}
\qquad(\operatorname{Re}s>1/2).
\]
The exponential counterterm in (12) is holomorphic and nowhere zero on this
domain, so it does not insert a hidden divisor.

## 4. Ordinary and positive determinant boundaries

On \(\sigma>2\), \(X_s\in L^1(\mathcal M,\tau)\), and (5)--(12) reduce to
the unregularized \(\tau\)-trace-associated graded determinant ratio.  On
\(1/2<\sigma\le2\), that unregularized \(\tau\)-determinant does not exist.

This is not the classical Fredholm determinant on the underlying Hilbert
space.  Indeed,

\[
\dim(\mathcal H_p^+\oplus\mathcal H_p^-)
=d_p\,\tau_p(I)
=\frac{(p-1)(4p+2)}3.
\]

Consequently, for the canonical Hilbert trace,

\[
\operatorname{Tr}_{\mathcal H}(|X_s|^q)
=\sum_p\frac{(p-1)(4p+2)}3p^{-q\sigma},
\qquad
X_s\in S^q(\mathcal H)\Longleftrightarrow q\sigma>3.
\]

The classical trace-class threshold is therefore \(\sigma>3\), and its
graded trace has moments \(C_{p,n}=d_pc_{p,n}\): it recovers the ordinary
Galois norm, not the normalized C45 root.

Where the positive Fuglede--Kadison determinant (or its semifinite relative
version on \(I+L^1\)) is defined, it uses \(\tau(\log|A|)\) and therefore
retains only modulus data.  In particular, on the ordinary domain its graded
ratio gives the modulus of the analytic determinant ratio, not its phase.
On the \(L^4\) domain an additional fourth-order regularization would first be
required.  The object in (12) is the explicitly defined graded analytic
regularized determinant, not an unregularized positive Fuglede--Kadison
determinant.

## 5. Scope

The theorem proves an operator-category realization of the C45 germ.  It does
not prove:

- a classical Fredholm determinant for the normalized C45 root;
- meromorphic continuation across \(\sigma=1/2\);
- a functional equation, Gamma factor, or Riemann divisor;
- a self-adjoint Hilbert--Pólya generator.

The three low-order counterterms are essential and must remain visible.
