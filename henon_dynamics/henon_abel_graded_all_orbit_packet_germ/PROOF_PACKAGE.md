# Proof package

## 1. Source object

Let \(H_6(q,p)=(1-6q^2-p,q)\) and restrict it to the certified four-state
survivor with adjacency matrix

\[
A=\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.
\]

For a primitive orbit \(\gamma\), write \(m(\gamma)\) for its symbolic
period, \(M_\gamma\in SL_2\) for its return derivative, and
\(\lambda_\gamma\) for the signed unstable multiplier.  Put
\(\Lambda_\gamma=|\lambda_\gamma|>1\),
\(t_\gamma=\lambda_\gamma+\lambda_\gamma^{-1}\) and
\(F_\gamma=\mathbb Q(t_\gamma)\).  HCS-P46 and HCS-P49 give, for every
\(n>2\),

\[
\beta_{\gamma,n}=
\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma)
\in\mathcal O_{F_\gamma}.
\]

Let

\[
D_{\gamma,n}=\sum_{\mathfrak q}
v_{\mathfrak q}(\beta_{\gamma,n})[\gamma,n,\mathfrak q]
\]

be its effective prime-ideal divisor.

## 2. Universal tagged Banach space

Let \(\mathscr A\) be the countable set of all triples
\((\gamma,n,\mathfrak q)\), where \(\gamma\) is primitive, \(n>2\), and
\(\mathfrak q\subset\mathcal O_{F_\gamma}\) is a nonzero prime ideal.  If
\(\mathfrak q\mid p\) has residue degree \(f_{\mathfrak q}\), assign weight

\[
w(\gamma,n,\mathfrak q)=f_{\mathfrak q}\log p.
\]

Define

\[
\mathcal B_{\rm tag}=\ell^1(\mathscr A,w).
\]

The ideal-norm formula gives the exact packet identity

\[
\|D_{\gamma,n}\|_{\rm tag}
=\sum_{\mathfrak q}v_{\mathfrak q}(\beta_{\gamma,n})
 f_{\mathfrak q}\log p
=\log\left|N_{F_\gamma/\mathbb Q}\beta_{\gamma,n}\right|.
\tag{2.1}
\]

## 3. Uniform conjugate-height bound

Use the integral coordinates \(x_i=6q_i\).  Every period-\(m\) conjugate
fixed point satisfies

\[
x_i^2+x_{i-1}+x_{i+1}-6=0.
\tag{3.1}
\]

If \(M=\max_i|x_i|\), choosing an index attaining the maximum gives

\[
M^2\le6+2M,
\qquad M\le1+\sqrt7.
\tag{3.2}
\]

The derivative step is

\[
J_i=\begin{pmatrix}-2x_i&-1\\1&0\end{pmatrix},
\]

so in the infinity norm

\[
\|J_i\|_\infty\le C_0:=3+2\sqrt7.
\tag{3.3}
\]

Consequently every conjugate return trace obeys

\[
|\sigma(t_\gamma)|\le2C_0^m.
\tag{3.4}
\]

The period-\(m\) fixed algebra is finite free of rank \(2^m\).  Hence

\[
[F_\gamma:\mathbb Q]\le2^m.
\tag{3.5}
\]

Every embedding \(\sigma:F_\gamma\hookrightarrow\mathbb C\) extends to the
residue field of the corresponding geometric fixed point, so the conjugate
coordinates still satisfy (3.1).  Extend it further to the multiplier field
and choose the reciprocal root \(\mu\) with \(|\mu|\ge1\).
The characteristic equation and (3.4) give

\[
|\mu|\le1+|\sigma(t_\gamma)|\le3C_0^m.
\tag{3.6}
\]

Cyclotomic reciprocity now yields

\[
|\sigma(\beta_{\gamma,n})|
\le\left(\sqrt{|\mu|}+\frac1{\sqrt{|\mu|}}\right)^{\varphi(n)}
\le\left(2\sqrt3\,C_0^{m/2}\right)^n.
\tag{3.7}
\]

Multiplying over at most \(2^m\) embeddings proves

\[
\log\left|N_{F_\gamma/\mathbb Q}\beta_{\gamma,n}\right|
\le2^m n\left(\log(2\sqrt3)+\frac m2\log C_0\right).
\tag{3.8}
\]

This deliberately crude inequality is uniform over every primitive orbit.

## 4. Orbit and pressure envelopes

The period-\(m\) marked-point count is

\[
N_m=\operatorname{tr}(A^m)
=\varphi^m+(-\varphi^{-1})^m+i^m+(-i)^m.
\tag{4.1}
\]

For \(m\ge1\), \(N_m\le3\varphi^m\).  Therefore the number of primitive
period-\(m\) orbits is also at most \(3\varphi^m\).

Let \(h_*\) be the certified Bowen-pressure root and set

\[
\widehat\ell_\gamma=h_*\log|\Lambda_\gamma|.
\]

The uniform unstable expansion gives

\[
\widehat\ell_\gamma\ge h_*m\log J_*,
\qquad J_*=\frac{\sqrt{17}+\sqrt{13}}2.
\tag{4.2}
\]

## 5. All-orbit convergence theorem

Define

\[
\mathcal G(s,u)=
\sum_{\gamma\ {\rm primitive}}e^{-s\widehat\ell_\gamma}
\sum_{n\ge3}u^nD_{\gamma,n}.
\tag{5.1}
\]

For \(r=|u|<1\) and \(\sigma=\Re s\), (2.1), (3.8), (4.1), and (4.2)
give

\[
\begin{aligned}
\|\mathcal G(s,u)\|_{\rm tag}
&\le3\sum_{m\ge1}\varphi^m e^{-\sigma h_*m\log J_*}2^m
\left(a+bm\right)\sum_{n\ge3}nr^n\\
&\le\frac{3r}{(1-r)^2}
\sum_{m\ge1}(a+bm)
\left(2\varphi e^{-\sigma h_*\log J_*}\right)^m,
\end{aligned}
\tag{5.2}
\]

where \(a=\log(2\sqrt3)\) and \(b=\frac12\log C_0\).  The last series
converges under the sufficient condition

\[
\sigma>\sigma_0:=\frac{\log(2\varphi)}{h_*\log J_*}.
\tag{5.3}
\]

On compact subsets of \(|u|<1,\Re s>\sigma_0\), the same majorant is
uniform.  Each summand is jointly holomorphic, so the Banach-valued
Weierstrass theorem proves that \(\mathcal G\) is jointly holomorphic there.

Since \(h_*\ge0.277980\), the source-locked, fully numerical safe condition
is

\[
\Re s>
\frac{\log(2\varphi)}{0.277980\log J_*}
=3.125206884004728\ldots .
\tag{5.4}
\]

## 6. Continuous rational norm pushforward

Let

\[
\mathcal B_{\rm rat}=\ell^1(\{p\text{ prime}\},\log p)
\]

and define on basis vectors

\[
\nu[\gamma,n,\mathfrak q]=f_{\mathfrak q}[p].
\tag{6.1}
\]

For every finitely supported complex vector \(c\), the triangle inequality
gives

\[
\|\nu c\|_{\rm rat}\le\|c\|_{\rm tag}.
\tag{6.2}
\]

Equality holds on each weighted basis vector, so \(\|\nu\|=1\).  Equality
also holds on every positive packet divisor.  Thus \(\nu\) extends uniquely
and continuously to \(\mathcal B_{\rm tag}\), and normal convergence permits
termwise pushforward of (5.1).  HCS-P50 proves that \(\nu\) is not injective;
continuity is not promoted to lossless identification.

## 7. Exact Abel-boundary obstruction

Take the primitive period-four orbit with

\[
L_4=289+24\sqrt{145}>1,
\qquad N_{\mathbb Q(\sqrt{145})/\mathbb Q}(L_4)=1.
\]

Flatters' Theorem 1.4 gives a primitive rational prime divisor of

\[
\Delta_n=N(L_4^n-1)
\]

for every \(n>12\).  If \(p\) is such a divisor, the factorization

\[
L_4^n-1=\prod_{d\mid n}\Phi_d(L_4)
\]

if \(p\) divided \(N(\Phi_d(L_4))\) for a proper divisor \(d<n\), it would
divide \(N(L_4^d-1)=\Delta_d\), contradicting primitivity.  Therefore
\(p\mid N(\Phi_n(L_4))\).  In this reciprocal quadratic case,

\[
N(\Phi_n(L_4))=\beta_{\gamma_4,n}^2.
\]

Therefore \(p\mid\beta_{\gamma_4,n}\), and

\[
\|D_{\gamma_4,n}\|_{\rm tag}
=\log|\beta_{\gamma_4,n}|\ge\log2
\qquad(n>12).
\tag{7.1}
\]

The fixed-orbit estimate (3.8) is \(O(n)\), so
\(\sum_{n\ge3}u^nD_{\gamma_4,n}\) converges for \(|u|<1\).  Equation
(7.1) shows that its terms fail to tend to zero when \(|u|=1\).  The two
bounds give
\(\limsup_n\|D_{\gamma_4,n}\|_{\rm tag}^{1/n}=1\), so the Banach
Cauchy--Hadamard formula proves radius exactly one.  Multiplying by the
fixed nonzero pressure factor
\(e^{-s\widehat\ell_{\gamma_4}}\) cannot repair this divergence.

## 8. Claim ceiling

The proof constructs an all-orbit analytic germ and a continuous rational
pushforward.  It does not produce a Fredholm determinant, analytic
continuation, a value at \(u=1\), a von-Mangoldt trace identity, a functional
equation, or a self-adjoint operator.  The next theorem must renormalize or
extract the Abel boundary without deleting the source-native tags.
