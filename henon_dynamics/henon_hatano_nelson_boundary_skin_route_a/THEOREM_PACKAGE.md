# HCS-C308 theorem package

Frozen obstruction identifier: `HEN-O292`.

## Exact model and conventions

Let `N>=2`.  Under open boundary conditions (OBC), `H_N(t_R,t_L)` is the real `N` by `N` matrix

`(H_N)_{j,j+1}=t_R`, `(H_N)_{j+1,j}=t_L` for `1<=j<N`,

with all other entries zero and `t_R,t_L>=0`.  Evolution means `i d psi/dt=H_N psi`.  The periodic chain (PBC) is stated for `N>=3`: with `(C v)_j=v_{j+1 mod N}`, set `H_N^per=t_R C+t_L C^{-1}`.  At `N=2`, `C=C^{-1}` and the two oriented neighbors coincide; that double-edge convention is recorded separately and is not silently identified with the standard oriented ring.

For positive hoppings define

`g=sqrt(t_R t_L)`, `q=sqrt(t_L/t_R)`, `D=diag(1,q,...,q^(N-1))`,

and let `A_N` be path adjacency.  Write `theta_m=m pi/(N+1)` and

`S_{jm}=sqrt(2/(N+1)) sin(j m pi/(N+1))`, `1<=j,m<=N`.

## Theorem (complete finite-chain boundary/skin atlas)

1. **Positive OBC similarity and spectrum.** If `t_R,t_L>0`,

   `D^{-1} H_N D=g A_N`.

   Hence `P_0=1`, `P_1=z`, `P_N=zP_{N-1}-t_Rt_L P_{N-2}`, and

   `det(zI-H_N)=g^N U_N(z/(2g))`.

   The spectrum is simple and real:

   `E_m=2g cos(theta_m)`, `m=1,...,N`.

2. **Canonical left/right basis and the skin distinction.** With `R=DS` and `L^T=S^T D^{-1}`,

   `H_N R=R diag(E_m)`, `L^T H_N=diag(E_m)L^T`, `L^T R=I`.

   Thus `R_{jm}=q^(j-1)S_{jm}` and `L^T_{mj}=q^(-(j-1))S_{jm}`.  The ordinary right amplitude has an exponential envelope toward the left when `q<1` and toward the right when `q>1`.  In contrast, its canonical pointwise biorthogonal density is

   `L^T_{mj}R_{jm}=S_{jm}^2`,

   independent of `q`.  These are different objects; this theorem never calls the latter skin-localized.

3. **Exact conditioning, propagation, and resolvent.** In the canonical sine gauge `R=DS`,

   `kappa_2(R)=kappa_2(D)=max(q,q^{-1})^(N-1)`.

   Arbitrary column rescalings change an eigenvector-matrix condition number, so this equality is explicitly gauge-specific.  For real time,

   `exp(-itH_N)=D S diag(exp(-itE_m)) S^T D^{-1}`,

   and, off the spectrum,

   `(zI-H_N)^{-1}=D(zI-gA_N)^{-1}D^{-1}`.

   In particular `||exp(-itH_N)||_2<=kappa_2(D)` and

   `||(zI-H_N)^{-1}||_2<=kappa_2(D)/dist(z,sigma(H_N))`.

   With `x=z/(2g)`, its entries are

   `[(zI-H_N)^{-1}]_{ij}=q^(i-j) U_{min(i,j)-1}(x) U_{N-max(i,j)}(x)/(g U_N(x))`.

4. **PBC Fourier ellipse.** For `N>=3`, the unitary Fourier basis diagonalizes `C`, so `H_N^per` is normal and

   `E_m^per=t_R exp(i k_m)+t_L exp(-i k_m)` with `k_m=2 pi m/N`.

   Equivalently, `Re E=(t_R+t_L)cos k_m` and `Im E=(t_R-t_L)sin k_m`.  These are finitely many points on the ellipse, not the whole ellipse at finite `N`; they become dense along it only as `N` grows.

5. **All degenerate hopping faces.** On `t_R=t_L=t>0`, `D=I` and both boundary matrices are Hermitian, with no right-amplitude bias.  If exactly one hopping is positive, OBC is a scalar multiple of the upper or lower shift: it is a single nilpotent `N`-Jordan block, `H^N=0`, `H^(N-1)!=0`, and `rank(H^k)=N-k`.  Its propagator and resolvent truncate:

   `exp(-itH)=sum_{k=0}^{N-1}(-itH)^k/k!`,

   `(zI-H)^{-1}=sum_{k=0}^{N-1}H^k/z^(k+1)` for `z!=0`.

   On the same one-sided axis, PBC is a nonzero scalar multiple of `C` or `C^{-1}` and remains unitarily diagonalizable with `N` distinct roots on a circle.  If both hoppings vanish, both matrices are zero with eigenspace dimension `N`, not one Jordan block.

6. **Orientation and singular boundary limit.** Swapping `t_R,t_L` transposes OBC, keeps its eigenvalues, sends `q` to `q^{-1}`, and flips the right-amplitude edge.  It complex-conjugates the PBC ellipse.  At fixed `N`, taking one positive hopping to zero collapses all positive-OBC eigenvalues and makes the canonical eigenbasis conditioning diverge; its OBC limit is defective.  The corresponding PBC limit retains a Fourier eigenbasis and a spectral circle.  This is a boundary-condition-sensitive singular limit, not a claimed topological invariant.

## Proof

For adjacent OBC sites, `D_j^{-1}t_R D_{j+1}=t_R q=g` and `D_{j+1}^{-1}t_LD_j=t_L/q=g`, proving the similarity.  Laplace expansion along the last row gives the continuant recurrence.  The defining recurrence `U_N(x)=2xU_{N-1}(x)-U_{N-2}(x)` with `x=z/(2g)` supplies the Chebyshev form.  The discrete sine transform is orthogonal and diagonalizes `A_N`, proving the spectrum and `R,L` identities.

Because right multiplication by the orthogonal `S` preserves singular values, the singular values of `R=DS` are exactly the diagonal entries of `D`; their extreme ratio is the stated condition number.  Functional calculus of the similar symmetric core proves the exponential and resolvent formulas.  The tridiagonal inverse continuant formula gives the displayed entry expression, and submultiplicativity plus the spectral theorem for `gA_N` gives the two norm bounds.

For PBC, Fourier vectors are eigenvectors of the unitary cyclic shift.  Substitution yields the ellipse parametrization and normality.  On a one-sided OBC axis the shift ranks are read directly from its surviving super- or subdiagonals, establishing one Jordan chain of length `N`; on the ring, `C^N=I`, so the Fourier eigenvalues are distinct roots.  The remaining boundary statements follow by direct substitution.

## Evidence boundary and Route A

The analytic proof covers all stated `N` and parameter faces.  The 123 finite evidence rows are regression witnesses only: 40 positive-OBC continuants/condition numbers, 21 determinant-log-derivative resolvent traces, 18 one-sided Jordan/PBC cases, 36 PBC power traces, and 8 semantic boundary faces.  Independent recomputation, a separate SymPy lane, isolated double replay, and repaired-hash hostile mutations protect the artifact; none upgrades a finite table into a theorem.

Route-A tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  Overall: `ROUTE_A_REJECTED`; Route B is locked.  Exact finite determinants and a similarity to a symmetric source matrix do not construct arithmetic local data, a target Euler product, a functional equation, target zeros, or a same-clock self-adjoint Hilbert--Polya operator.

## Explicit nonclaims

No disorder localization, interaction effect, topological invariant, topological edge mode, thermodynamic-limit theorem, or literature priority is claimed.  “Skin” here means the exact exponential envelope of the canonical finite-chain right amplitudes.  The work remains inside `NO_BAD_EULER_OR_ROOT_NUMBER`.
