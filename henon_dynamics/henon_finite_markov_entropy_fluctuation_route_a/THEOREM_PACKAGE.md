# HCS-C361 theorem package: finite Markov entropy and fluctuation symmetry

## 1. Frozen object and conventions

Let \(S=\{0,\ldots,d-1\}\) be finite. For \(i\ne j\), rates satisfy \(q_{ij}>0\) exactly when \(q_{ji}>0\); the resulting undirected support is connected. No self-jumps are recorded. The row generator, acting on column functions, is
\[
 (Lf)(i)=\sum_{j\ne i}q_{ij}(f(j)-f(i)),\qquad
 L_{ij}=q_{ij},\quad L_{ii}=-r_i,\qquad r_i=\sum_{j\ne i}q_{ij}.
\]
Thus there is a unique positive stationary row law \(\pi\) with \(\pi L=0\). An in-arborescence toward root \(i\) has one outgoing edge from every other vertex and every directed path ends at \(i\).

## 2. Main theorem

For every chain above:

1. If
   \[
   \tau_i=\sum_{T\to i}\prod_{(u\to v)\in T}q_{uv},
   \]
   then \(\pi_i=\tau_i/\sum_k\tau_k\).
2. Put \(a_{ij}=\pi_iq_{ij}\), \(J_{ij}=a_{ij}-a_{ji}\), and \(F_{ij}=\log(a_{ij}/a_{ji})\). The stationary entropy-production rate is
   \[
   \sigma=\frac12\sum_{i\ne j}J_{ij}F_{ij}
   =\sum_{i<j}(a_{ij}-a_{ji})\log\frac{a_{ij}}{a_{ji}}\ge0.
   \]
   Equality holds exactly under detailed balance \(a_{ij}=a_{ji}\), and exactly when every oriented graph cycle \(C\) has zero medium affinity
   \[
   \mathcal A(C)=\sum_{(i,j)\in C}\log\frac{q_{ij}}{q_{ji}}=0.
   \]
3. Start the chain in \(\pi\). For a path with successive states \(i_0,\ldots,i_m\), define total entropy
   \[
   \Sigma_T=\log\frac{\pi_{i_0}\prod_{\ell=1}^m q_{i_{\ell-1}i_\ell}}
   {\pi_{i_m}\prod_{\ell=1}^m q_{i_\ell i_{\ell-1}}}.
   \]
   If \(\Theta\) reverses time, define the reversed pushforward law
   \(\mathbb P_\pi^R=\mathbb P_\pi\circ\Theta^{-1}=\mathbb P_\pi\circ\Theta\). Then
   \[
   \frac{d\mathbb P_\pi}{d\mathbb P_\pi^R}=e^{\Sigma_T}.
   \]
   Consequently, for the law \(\mu_T\) of \(\Sigma_T\), every Borel set \(B\), and every real \(\lambda\),
   \[
   \mu_T(B)=\int_{-B}e^{-s}\,\mu_T(ds),\qquad -B=\{-s:s\in B\},
   \mathbb E_\pi e^{-\Sigma_T}=1,\qquad
   \mathbb E_\pi e^{-\lambda\Sigma_T}=\mathbb E_\pi e^{-(1-\lambda)\Sigma_T}.
   \]
   The familiar point formula is asserted only at atoms.
4. For medium entropy \(W_T=\sum\log(q_{ij}/q_{ji})\), Feynman--Kac gives the tilted matrix
   \[
   (L_\lambda)_{ij}=q_{ij}^{1-\lambda}q_{ji}^{\lambda}\ (i\ne j),
   \qquad (L_\lambda)_{ii}=-r_i.
   \]
   Hence \(L_\lambda^{\mathsf T}=L_{1-\lambda}\), and for every complex \(z\) and real \(\lambda\),
   \[
   \det(zI-L_\lambda)=\det(zI-L_{1-\lambda}).
   \]
   The dominant eigenvalue
   \(\psi(\lambda)=\lim_{T\to\infty}T^{-1}\log\mathbb E_\pi e^{-\lambda W_T}\)
   is finite and real analytic and obeys \(\psi(\lambda)=\psi(1-\lambda)\). Total and medium entropy have the same SCGF because their difference is the bounded endpoint term \(\log\pi_{X_0}-\log\pi_{X_T}\).
5. Only under the additional hypothesis that \(W_T/T\) satisfies a full LDP whose rate equals
   \(I(a)=\sup_\lambda\{-\lambda a-\psi(\lambda)\}\) do we infer
   \[
   I(a)-I(-a)=-a.
   \]

## 3. Proof

### Matrix-tree stationary law

Let (M=-L^{\mathsf T}). Its columns sum to zero. Expanding any principal cofactor of (M) by permutations and cancelling terms whose chosen directed edges contain a cycle leaves exactly the products of in-arborescences toward the deleted root. Thus the cofactor vector (τ) satisfies (L^{\mathsf T}\tau=0). Connected bidirected support supplies a positive in-tree to every root, so every (τ_i>0). Irreducibility makes the nullspace one-dimensional; normalizing proves the formula and uniqueness.

### Positivity and all three equality criteria

For (x,y>0), ((x-y)\log(x/y)\ge0), with equality only at (x=y). Applying this to each unordered edge proves (σge0) and shows that equality is equivalent to detailed balance.

If detailed balance holds, multiplying (q_{ij}/q_{ji}=\pi_j/\pi_i) around a cycle telescopes, so every cycle affinity vanishes. Conversely, suppose all cycle affinities vanish. Fix a root (o). For a path (o=i_0,\ldots,i_m=i), put
\[
 h_i=\prod_{\ell=1}^m\frac{q_{i_{\ell-1}i_\ell}}{q_{i_\ell i_{\ell-1}}}.
\]
Two paths give the same value: concatenating one with the reverse of the other decomposes into closed walks, and erasing backtracks and splitting repeated vertices reduces it to simple cycles, all with product one. Therefore (h_j/h_i=q_{ij}/q_{ji}) on each edge. Normalizing (h) gives a probability (ν) with (ν_iq_{ij}=ν_jq_{ji}). It is stationary, hence equals (π). This closes the converse without assuming a cycle basis theorem.

### Finite-time path reversal

Fix a jump count, state skeleton, and holding intervals. The forward density is
\[
 \pi_{i_0}\exp\!\left(-\sum_{\ell=0}^{m}r_{i_\ell}s_\ell\right)
 \prod_{\ell=1}^{m}q_{i_{\ell-1}i_\ell}.
\]
The reversed path has the same holding-time exponential, merely reordered, and jump product with every edge reversed. Bidirectionality makes \(\mathbb P_\pi\) and \(\mathbb P_\pi^R\) mutually absolutely continuous. Their ratio is \(e^{\Sigma_T}\), including the zero-jump case where it is one. Also \(\Sigma_T\circ\Theta=-\Sigma_T\). For bounded measurable \(g\), change variables under \(\Theta\) to obtain
\[
 \mathbb E[g(\Sigma_T)]=\mathbb E[e^{-\Sigma_T}g(-\Sigma_T)].
\]
Indicators, \(g=1\), and \(g(s)=e^{-\lambda s}\) give the three stated finite-time identities.

### Tilt, complete polynomial symmetry, and SCGF

Multiplying every jump \(i\to j\) by \(e^{-\lambda\log(q_{ij}/q_{ji})}\) changes the off-diagonal rate in the backward equation to \(q_{ij}^{1-\lambda}q_{ji}^{\lambda}\), while waiting terms remain \(-r_i\). Entrywise transposition gives \(L_\lambda^{\mathsf T}=L_{1-\lambda}\). A matrix and its transpose have the same full characteristic polynomial, which proves more than equality of their top eigenvalues.

For real \(\lambda\), add a sufficiently large scalar multiple of the identity. The result is an irreducible nonnegative matrix, so Perron--Frobenius gives a simple real dominant eigenvalue; finite-dimensional Feynman--Kac identifies it with
\(\psi(\lambda)=\lim_{T\to\infty}T^{-1}\log\mathbb E e^{-\lambda W_T}\).
The tilted entries are analytic in \(\lambda\); simplicity makes the local Perron branches analytic, and uniqueness joins them into a real-analytic \(\psi\) on \(\mathbb R\). The stationary endpoint correction satisfies
\(|\Sigma_T-W_T|\le 2\max_i|\log\pi_i|\), so it disappears after division by \(T\), including at the logarithmic moment-generating level. Finally, under the explicitly assumed full-LDP Legendre identification, substituting \(\mu=1-\lambda\) gives \(I(-a)=a+I(a)\), which is the stated sign convention. No rate-function conclusion is made without that identification.

## 4. Boundary atlas

- **Singleton:** with the empty-tree weight one, (π=1), (L=0), and every entropy is zero.
- **Two states:** stationarity itself gives (π_0q_{01}=π_1q_{10}); total entropy vanishes pathwise. A nonzero affinity first appears on a three-state cycle. For clockwise rates two and reverse rates one, (π) is uniform, the cycle affinity is (3\log2), and (σ=\log2).
- **Reducible support:** there need not be one positive stationary law or positive rooted tree weight for every root. The theorem applies separately after a closed irreducible class is chosen; arbitrary stationary mixtures require component bookkeeping.
- **One-way edges:** a zero reverse rate can create infinite affinity and singular reversed path measure. It is outside the theorem, not obtained by silently inserting zero into a logarithm.
- **Self transitions:** phantom self-jumps are excluded; diagonal entries encode holding only.

## 5. Scope and ownership

The matrix-tree formula and stochastic fluctuation symmetry are reconstructed from the cited source lineage, with no priority claim. The tilted determinant is only a finite source-model characteristic polynomial. It is not an Euler factor, a target functional equation, a primitive arithmetic-orbit zeta, or a Hilbert--Pólya operator. Route A is rejected at all five gates and Route B is locked.
