# Theorem package

Fix `A in C^{m x n}` and iterate

`X_{k+1}=X_k(2I_m-AX_k)`, with `X_k in C^{n x m}`.

## Invertible square theorem

If `m=n` and `A` is invertible, put `R_0=I-AX_0`. Then

`R_k=R_0^{2^k}` and `X_k=A^{-1}(I-R_0^{2^k})`.

Consequently `X_k -> A^{-1}` iff `rho(R_0)<1`. For any `rho=rho(R_0)>0`, let `s_*` be the largest Jordan block size among eigenvalues of modulus `rho`. Then for any matrix norm

`||R_k|| = Theta((2^k)^{s_*-1} rho^{2^k})`.

If `rho=0`, termination occurs when `2^k` reaches the nilpotency index. If `rho=1`, semisimple peripheral blocks give bounded nonvanishing residuals, whereas a peripheral block of size greater than one gives polynomially unbounded residuals. If `rho>1`, the residual diverges double-exponentially, with the same Jordan polynomial factor.

## Moore–Penrose iff basin

Let `A^dagger` be the Moore–Penrose inverse and set `P=AA^dagger`, `Q=A^dagger A`. Then

`X_k -> A^dagger`

if and only if

`X_0=QX_0P` and `rho((P-AX_0)|_{Ran A})<1`.

Inside this basin,

`R_k=P-AX_k=R_0^{2^k}` and `X_k=A^dagger-A^dagger R_0^{2^k}`.

For necessity, choose SVD coordinates in which `A=[[Sigma,0],[0,0]]` and write `X=[[B,C],[D,E]]`. The recurrence is

- `B_+=B(2I-Sigma B)`,
- `C_+=(2I-B Sigma)C`,
- `D_+=D(2I-Sigma B)`,
- `E_+=2E-D Sigma C`.

Convergence of `B` to `Sigma^{-1}` forces the compressed residual into the open spectral disk. In that disk, the factors multiplying `C` and `D` approach the identity with a summable error and are all invertible, so their infinite products have invertible limits; convergence to zero therefore forces `C_0=D_0=0`. The last recurrence then gives `E_k=2^kE_0`, so `E_0=0`. This is exactly `X_0=QX_0P`.

## Canonical alpha corridor

For nonzero `A` and real `alpha`, the start `X_0=alpha A*` converges to `A^dagger` iff

`0<alpha<2/sigma_max^2`.

At equality, each maximal-singular-value direction has residual `-1`, whose first square is `1`, so its iterate coefficient becomes and remains zero; smaller directions with strict residual modulus below one converge to their inverse coefficients. Thus equality produces spectral truncation, not `A^dagger`. At `alpha=0`, zero is fixed. For `alpha>2/sigma_max^2` or `alpha<0`, at least one maximal direction diverges. If `A=0`, the canonical start is zero for every alpha and converges trivially; among arbitrary starts, only `X_0=0` converges because `X_k=2^kX_0`.

## Scope

Route-A tuple `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall `ROUTE_A_REJECTED`; Route B locked; scope `NO_BAD_EULER_OR_ROOT_NUMBER`. Exact arithmetic is not a floating-point stability theorem.
