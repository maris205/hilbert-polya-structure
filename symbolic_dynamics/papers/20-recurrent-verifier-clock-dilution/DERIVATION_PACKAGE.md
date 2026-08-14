# DERIVATION PACKAGE — SD-C22

## 1. Expanded recurrent verifier

For every input \(n\ge2\), retain the explicit Paper 19 states
\(I_n,T_{n,d},Q_{n,d,q},R_{n,k}\). Multiplication and order determine:

\[
I_n\to T_{n,2},
\]

\[
T_{n,d}\to
\begin{cases}
I_n,&d^2>n,\\
Q_{n,d,2},&d^2\le n,
\end{cases}
\]

\[
Q_{n,d,q}\to
\begin{cases}
Q_{n,d,q+1},&dq<n,\\
R_{n,1},&dq=n,\\
T_{n,d+1},&dq>n.
\end{cases}
\]

The terminal acceptance edge is redirected to \(I_n\) uniformly, not after a
prime lookup. Accepted inputs form vertex-disjoint cycles; rejected inputs
enter one-way rays.

## 2. Exact length

Let \(p\) be prime and \(m=\lfloor\sqrt p\rfloor\). For each
\(2\le d\le m\), quotient search visits \(q=2,\ldots,\lceil p/d\rceil\).
The edge segment from \(T_{p,d}\) to \(T_{p,d+1}\) therefore has
\(\lceil p/d\rceil\) edges. Adding the input and terminal-return edges gives

\[
\ell(p)=2+\sum_{d=2}^{m}\left\lceil\frac p d\right\rceil.
\]

Because \(p/d\) is nonintegral in this range,
\(\lceil p/d\rceil=1+\lfloor p/d\rfloor\). Therefore

\[
p(H_m-1)+2\le\ell(p)\le p(H_m-1)+m+1,
\]

and

\[
\ell(p)=\frac12p\log p+(\gamma-1)p+O(\sqrt p).
\]

## 3. Weighted cyclic block

Give a cycle of length \(\ell\) nonnegative roofs
\(\tau_0,\ldots,\tau_{\ell-1}\) with total \(T\). Its weighted cyclic shift
obeys

\[
B_s^\ell=e^{-sT}I.
\]

Consequently

\[
\operatorname{spec}(B_s)=
\left\{\exp\left(\frac{-sT+2\pi i k}{\ell}\right):
0\le k<\ell\right\},
\]

its singular values are \(e^{-\sigma\tau_j}\), and

\[
\det(I-zB_s)=1-z^\ell e^{-sT}.
\]

For \(T=\log p\), these become the prime-cycle formulas used by the exact
suite.

## 4. Distribution-free compactness obstruction

On every prime cycle choose an edge of minimum roof. Then

\[
0\le\min_{e\in\Gamma_p}\tau(e)
\le\frac{\log p}{\ell(p)}\longrightarrow0.
\]

The corresponding source basis vectors are orthonormal and their image norms
tend to one. Every compact operator sends this sequence to a norm-null
sequence after compact subtraction, so

\[
\|L_s\|_{\mathrm{ess}}=1
\qquad(\operatorname{Re}s>0).
\]

Moreover, for every \(q>0\), Jensen gives

\[
\sum_{e\in\Gamma_p}e^{-q\sigma\tau(e)}
\ge\ell(p)p^{-q\sigma/\ell(p)}.
\]

The right-hand side does not tend to zero, hence the direct sum belongs to no
finite Schatten class.

## 5. Essential unit circle

Every prime block has eigenvalue radius
\(r_p=p^{-\sigma/\ell(p)}\to1\). Its \(\ell(p)\) eigenvalue phases form an
equally spaced grid. For each \(\omega\) on the unit circle, select normalized
block eigenvectors whose eigenvalues approach \(\omega\). Distinct block
vectors are orthogonal and weakly null, giving a singular Weyl sequence.
Thus the unit circle lies in the essential approximate spectrum and
\(I-zL_s\) is non-Fredholm whenever \(|z|=1\).

## 6. Orbit product versus Fredholm determinant

The combinatorial primitive product is

\[
D_{\rm orb}^{\rm raw}(s,z)
=\prod_p(1-z^{\ell(p)}p^{-s}).
\]

It converges normally for \(\operatorname{Re}s>1\), \(|z|\le1\), and at
\(z=1\) equals \(\zeta(s)^{-1}\). This does not define
\(\det(I-zL_s)\): the whole operator is noncompact and not trace class.

The raw block power trace is

\[
\operatorname{tr}(B_{p,s}^r)=
\begin{cases}
\ell(p)p^{-sr/\ell(p)},&\ell(p)\mid r,\\
0,&\ell(p)\nmid r.
\end{cases}
\]

## 7. First-return collapse

Choose one input vertex \(I_p\) from each accepted cycle. The first-return
operator is

\[
R_s\delta_{I_p}=p^{-s}\delta_{I_p}.
\]

It is trace class for \(\operatorname{Re}s>1\) and unitarily identical to the
Paper 04 prime-loop operator. Its ordinary return-step factor is
\(1-zp^{-s}\), not the raw \(1-z^{\ell(p)}p^{-s}\). Equality at \(z=1\)
forgets graph-step time; retaining \(z^{\ell(p)}\) on the induced loop restores
the raw marker but not the ordinary return convention.

## 8. Universal control and state subdivision

Any total decider may expose its finite configuration chain and close accepted
chains with exact total roof \(\log n\). A uniformly prescribed padding of
\(n^2\) idle states leaves the accepted support unchanged but forces
\(\ell(n)/\log n\to\infty\). The same noncompactness follows for squares,
powers of two, Fibonacci numbers, seeded hashes, or any other infinite
decidable support.

Conversely, contracting every accepted computation to one loop recovers a
diagonal compiler. Compactness of the one-step vertex adjacency is therefore
unstable under unbounded source-clock-preserving state subdivision even though
the unmarked orbit Euler factor is unchanged.

## 9. Claim boundary

The result is proved for vertex-disjoint finite accepted cycles, nonnegative
exact-clock roofs, and the natural counting \(\ell^2\)-space. It does not
settle overlapping recurrent grammars, signed or homological cancellation,
quotient spaces deleting the finite-cycle modes, anisotropic completions, or
nonordinary determinants. Those possibilities require a new source lock and
cannot repair A2 of SD-C22.
