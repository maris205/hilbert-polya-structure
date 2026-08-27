# All-parameter theorem package

## 1. Setting and notation

Let \(\nu>0\), \(L>0\), \(m\in\mathbb R\), and \(s>3/2\). Write
\(\mathbb T_L=\mathbb R/L\mathbb Z\), \(\kappa_k=2\pi k/L\), and

\[
X_m^s=\{u\in H^s(\mathbb T_L;\mathbb R):L^{-1}\!\int u=m\}.
\]

The Burgers semiflow \(S_t\) uses physical time and solves
\(u_t+u u_x=\nu u_{xx}\). Define

\[
\mathbb P^{s+1}_+=
\{w\in H^{s+1}(\mathbb T_L;\mathbb R):\min w>0\}/\mathbb R_{>0},
\quad
K_t=e^{t(\nu\partial_x^2-m\partial_x)}.
\]

The quotient is only by positive constants. Since \(s+1>5/2\), positivity and all
displayed classical derivatives after positive time are unambiguous; the identities
at time zero hold in the corresponding Sobolev/distributional sense.

## 2. Main theorem

**Theorem (global projective-heat phase portrait).** The map

\[
\Phi_m:\mathbb P^{s+1}_+\longrightarrow X_m^s,
\qquad \Phi_m([w])=m-2\nu\partial_x\log w,
\]

is a smooth bijection, with inverse

\[
u\longmapsto [\exp(-V/(2\nu))],
\qquad V_x=u-m,\quad \int_{\mathbb T_L}V=0.
\]

It gives the autonomous conjugacy

\[
S_t\Phi_m([w])=\Phi_m([K_t w]),\qquad t\ge0. \tag{2.1}
\]

Moreover:

1. \(K_t w(x)=(e^{\nu t\partial_x^2}w)(x-mt)\), preserves strict positivity,
   and produces the unique global Burgers orbit from every \(u_0\in X_m^s\).
   The solution is smooth for every \(t>0\).
2. Every orbit converges to the constant \(m\) in \(H^s\). Consequently the only
   equilibrium, periodic point, or recurrent point is \(u\equiv m\), where recurrence
   means that some \(t_j\to\infty\) satisfies \(S_{t_j}u\to u\) in \(H^s\).
3. Let \(w_0=\sum_{k\in\mathbb Z}a_k e^{i\kappa_kx}\) be any representative of
   \(\Phi_m^{-1}(u_0)\). Then \(a_0>0\). If \(u_0\ne m\), let
   \(r=\min\{|k|:k\ne0,\ a_k\ne0\}\), and let \(r_2>r\) be the next active absolute
   mode, with \(r_2=\infty\) if none exists. With
   \(\eta=\min\{2\nu\kappa_r^2,\nu\kappa_{r_2}^2\}\) and the second term interpreted
   as \(+\infty\) when \(r_2=\infty\),

   \[
   u(x,t)-m=-\frac{2\nu}{a_0}
   \sum_{|k|=r}i\kappa_k a_k
   e^{-\nu\kappa_r^2t}e^{i\kappa_k(x-mt)}
   +O_{H^s}(e^{-\eta t}). \tag{2.2}
   \]

   In particular \(\eta>\nu\kappa_r^2\) and
   \(\lim_{t\to\infty}-t^{-1}\log\|S_tu_0-m\|_{H^s}=\nu\kappa_r^2\).
4. On the complexification of \(H^s\), the generator obtained by linearizing at
   \(m\) has domain \(H^{s+2}\) and complete spectrum

   \[
   \lambda_k=-\nu\kappa_k^2-i m\kappa_k,\qquad k\in\mathbb Z. \tag{2.3}
   \]

   On the tangent space to \(X_m^s\), the \(k=0\) eigenvalue is omitted. On the real
   phase space the nonzero modes occur as conjugate two-dimensional real blocks.

## 3. Proof

For \(u\in X_m^s\), \(u-m\) has a unique zero-mean periodic primitive
\(V\in H^{s+1}\). Sobolev composition gives \(e^{-V/(2\nu)}>0\). Conversely,
\(\partial_x\log w\in H^s\) has zero mean, so \(\Phi_m([w])\in X_m^s\).
The two formulas are inverse because integrating a logarithmic derivative recovers
\(\log w\) up to exactly the positive scalar removed by projectivization. Standard
Sobolev composition also gives smoothness of both coordinate maps.

Let \(w_t=\nu w_{xx}-m w_x\) and \(u=m-2\nu w_x/w\). Differentiating and clearing
\(w^3\) reduces \(u_t+u u_x-\nu u_{xx}\) to zero identically. Conversely the inverse
map sends a Burgers solution to the same projective linear evolution. This proves
(2.1). Translation commutes with heat, giving the displayed formula for \(K_t\).
The periodic heat kernel is strictly positive, so a positive initial representative
stays positive. Analytic heat smoothing and the coordinate map give global
existence and instant smoothing.

For the phase portrait, write

\[
K_tw_0=a_0+\sum_{k\ne0}a_k
e^{-\nu\kappa_k^2t}e^{i\kappa_k(x-mt)}. \tag{3.1}
\]

Positivity of \(w_0\) implies \(a_0=L^{-1}\int w_0>0\). Equation (3.1) converges to
\(a_0\) in \(H^{s+1}\), and the smooth logarithmic derivative therefore converges to
zero in \(H^s\). Hence every Burgers orbit converges to \(m\). An equilibrium or
periodic point is recurrent; if \(S_{t_j}u\to u\) while the full orbit converges to
\(m\), then \(u=m\). This proves the complete recurrence assertion.

For a nonconstant lift, the active positive integers have a least element \(r\).
Separate the \(|k|=r\) terms in (3.1). The remaining linear Fourier tail is
\(O_{H^{s+1}}(e^{-\nu\kappa_{r_2}^2t})\), while expanding
\((a_0+h)^{-1}=a_0^{-1}-a_0^{-2}h+O(h^2)\) makes the first nonlinear correction
\(O_{H^s}(e^{-2\nu\kappa_r^2t})\). Differentiation yields (2.2). The leading real
trigonometric pair is nonzero and translation preserves its \(H^s\) norm, proving
the logarithmic decay limit.

Finally, substituting \(u=m+\varepsilon h\) and retaining order \(\varepsilon\) gives
\(h_t=\nu h_{xx}-m h_x\). Fourier modes diagonalize this sectorial operator, giving
(2.3); compact resolvent on the circle makes the displayed list the complete
spectrum.

## 4. Executable certificate and logical boundary

At \(L=2\pi\), 24 deterministic strictly positive rational trigonometric lifts test:
the cleared-denominator nonlinear identity, Hermitian reality, conservative exact
positivity margins, algebraic drift--heat snapshots, semigroup composition, leading
mode coefficients/exponents, and 408 linear-spectrum cells. An independent checker,
a separate SymPy calculation, byte replay, and semantic mutations audit those rows.

These rows are regression only. The all-parameter result is proved above, not by a
finite census. No determinant, orbit zeta, arithmetic correspondence, target
divisor, functional equation, automorphy result, or Hilbert--Pólya operator is
asserted. The route tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall Route A is rejected and
Route B invocation is false.
