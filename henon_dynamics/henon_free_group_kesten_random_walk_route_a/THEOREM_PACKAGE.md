# Theorem package

## Frozen model

Let \(F_d=\langle a_1,\ldots,a_d\rangle\), \(d\ge2\), put \(D=2d\), and at each integer time right-multiply by one of \(a_i^{\pm1}\) uniformly.  Its Cayley graph is the \(D\)-regular tree.  The operator is exactly
\[
(Pf)(v)=D^{-1}\sum_{w\sim v}f(w)
\]
on \(\ell^2(T_D)\), and the walk starts at the identity \(o\).

## Complete theorem

Put \(\rho=2\sqrt{D-1}/D\), \(R_n=|X_n|\), and \(C_m=(m+1)^{-1}\binom{2m}{m}\).

1. The full operator \(P\) is purely absolutely continuous, with spectrum \([-\rho,\rho]\).  Its root spectral density is
   \[
   k_D(x)=\frac{\sqrt{4(D-1)-D^2x^2}}{2\pi(1-x^2)}\mathbf1_{|x|<\rho}.
   \]
   With \(\sqrt{z^2-\rho^2}\sim z\), its root resolvent is
   \[
   G_o(z)=\frac{D\sqrt{z^2-\rho^2}-(D-2)z}{2(z^2-1)}.
   \]
2. The radial chain jumps \(0\to1\) surely and, from every \(r\ge1\), jumps up with \(p=(D-1)/D\) and down with \(q=1/D\).
3. Odd returns vanish and for \(n\ge1\),
   \[
   \mathbb P_o(X_{2n}=o)=D^{-2n}\sum_{k=1}^n
   \frac{k}{2n-k}\binom{2n-k}{n}D^k(D-1)^{n-k}.
   \]
4. The first return law is
   \[
   \mathbb P_o(\tau_o^+=2k)=\frac{C_{k-1}(D-1)^{k-1}}{D^{2k-1}},
   \qquad \mathbb P_o(\tau_o^+<\infty)=\frac1{D-1}.
   \]
5. Almost surely \(R_n/n\to(D-2)/D\), and
   \[
   \frac{R_n-(D-2)n/D}{\sqrt n}\Longrightarrow
   N\!\left(0,\frac{4(D-1)}{D^2}\right).
   \]
6. At \(d=1\), \(F_1\cong\mathbb Z\): the spectral density is \([\pi\sqrt{1-x^2}]^{-1}\) on \((-1,1)\), the walk is recurrent, \(u_{2n}=4^{-n}\binom{2n}{n}\), \(R_n/n\to0\) a.s., and \(R_n/\sqrt n\Rightarrow|N(0,1)|\).

## Proof closure

### Root resolvent

The forward-tree cavity value satisfies
\[
h=[z-(D-1)h/D^2]^{-1},\qquad G_o=[z-h/D]^{-1}.
\]
Selecting the solution \(h\sim z^{-1}\) gives the stated \(G_o\).  Stieltjes inversion gives \(k_D\); the apparent poles at \(\pm1\) cancel, and \(zG_o(z)\to1\), so there is no missing mass or exterior atom.

### Full pure-AC spectrum

The normalized sphere indicators give a radial Jacobi matrix with first coupling \(D^{-1/2}\) and all later couplings \(a=\sqrt{D-1}/D\).  For each vertex, split its child values into their mean and zero-sum subspace.  Every zero-sum sibling vector, extended constantly and normalized on successive descendant layers, generates the free half-line Jacobi matrix with coupling \(a\).  Recursive mean/zero-sum splitting on finite rooted truncations proves completeness, hence
\[
P\cong J_0\oplus\bigoplus J_{\mathrm{free}}.
\]
The root is cyclic for \(J_0\), whose complete measure was just found; the sine transform makes every free block multiplication by \(2a\cos\theta\).  Thus all blocks, and therefore \(P\), are purely AC on the asserted interval.

### Exact returns

A length-\(2n\) radial return is a Dyck path.  If it has \(k\) irreducible excursions, Lagrange inversion for \(C(t)=1+tC(t)^2\) gives
\[
[t^{n-k}]C(t)^k=\frac{k}{2n-k}\binom{2n-k}{n}.
\]
Its \(k\) rises from zero have \(D\) choices; the other \(n-k\) rises have \(D-1\), while falls are forced.  This proves the return formula.  One irreducible excursion leaves \(C_{k-1}\) interior Dyck paths and has word count \(DC_{k-1}(D-1)^{k-1}\).  Summing its probability with the Catalan generating function gives \(q/p=1/(D-1)\).

### Escape laws without a last-return stopping-time error

Take i.i.d. \(\xi_i\in\{-1,1\}\) with probabilities \(q,p\), and define
\[
\widehat R_{n+1}=\widehat R_n+\xi_{n+1}
+2\mathbf1_{\{\widehat R_n=0,\xi_{n+1}=-1\}}.
\]
This is the radial chain.  From one, gambler's ruin gives return probability \(q/p<1\); strong Markov therefore makes the number of zero visits finite a.s.  Hence
\[
\widehat R_n=\sum_{i=1}^n\xi_i+2B_n,
\qquad B_n\uparrow B_\infty<\infty\quad\text{a.s.}
\]
The correction disappears on both \(n\) and \(\sqrt n\) scales, so the i.i.d. SLLN and CLT yield the stated constants.

## Boundary and evidence status

For \(D=2\), Fourier transform on \(\mathbb Z\) gives the arcsine law and \(R_n\stackrel d=|S_n|\), closing the critical boundary.  The 1,997 exact finite rows and 237 SymPy identities are regression receipts only; all infinite claims are analytic.  No primitive-arithmetic-orbit, zeta, target determinant, Euler-factor, root-number, target-zero, or Route-B claim is made.
