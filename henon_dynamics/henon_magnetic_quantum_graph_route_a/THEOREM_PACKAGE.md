# Theorem package

Let `C=(2/3)11^T-I_3`, `S=[[0,C],[C,0]]`, and `J=[[0,I_3],[I_3,0]]`.  On the six directed bonds of the theta graph, set

`P_alpha(k)=diag((exp(i(k l_j+alpha_j)/2))_(j=1)^3, (exp(i(k l_j-alpha_j)/2))_(j=1)^3)`

and `U_alpha(k)=P_alpha(k) S P_alpha(k)`.

## Theorem 1 — unitary gauge family

For real `k,alpha`, `U_alpha(k)` is unitary.  A common shift `alpha_j -> alpha_j+c` leaves the matrix exactly unchanged.  Therefore the magnetic parameter space has two gauge-invariant coordinates, for example `(alpha_1-alpha_3,alpha_2-alpha_3)`.  The written `alpha` is a real lift: increasing one `alpha_j` by `2*pi` gives `U_(alpha+2*pi*e_j)=E_j U_alpha E_j`, with `E_j` equal to `-1` on the two orientations of edge `j`.  Hence the unitary equivalence class and determinant, though not the displayed matrix entry by entry, descend to the flux torus.

## Theorem 2 — parameter-changing antiunitary

With `Theta=J K`,

`Theta U_alpha(k) Theta^{-1}=U_{-alpha}(k)^{-1}`.

The minus sign on `alpha` is essential.  At `k=0`, `alpha=(pi/2,0,0)`, the correct defect vanishes, whereas the false fixed-alpha identity has eight nonzero entries and squared Frobenius norm `64/9`.

## Theorem 3 — full Laurent determinant

Let `x_j=exp(i k l_j)`, `q_j=exp(i alpha_j)`,

`X_+=diag(x_j q_j)`, `X_-=diag(x_j/q_j)`.

Then

`D=det(I_3-rho^2 C X_- C X_+)=1-rho^2 T1+rho^4 T2-rho^6(x1x2x3)^2`,

where

`T1=(1/9)sum_i x_i^2+(4/9)sum_(i<j)x_i x_j(q_i/q_j+q_j/q_i)`

and

`T2=(1/9)sum_(i<j)x_i^2x_j^2+(4/9)sum_(i<j)x_i x_j x_k^2(q_i/q_j+q_j/q_i)`

with `k` the complementary index.  The formula is invariant under common scaling of all `q_j` and under `q_j -> q_j^{-1}`.

## Theorem 4 — oriented primitive ledger

For a closed directed walk `p`, let `m_j=N_(+j)-N_(-j)`.  Then `sum_j m_j=0`, and its weight is

`A_p rho^n exp(i k L_p) product_j q_j^m_j`.

The shortest off-diagonal witness `(+i,-j)`, `i!=j`, has amplitude `4/9` and phase `q_i/q_j`; its reverse has `q_j/q_i`.  Individual orientations therefore retain flux sign even though the full determinant is inversion-even.

## Controls and boundary

Zero flux recovers C133 exactly.  Flux `q=(-1,1,1)` changes the `rho^2` coefficient by `16 x1(x2+x3)/9`.  Wrong Kirchhoff normalization destroys unitarity, and a direction-asymmetric reverse length destroys reversal.

The result is exactly `(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`.  It is not a target divisor, arithmetic Euler product, root number, automorphy statement, or Hilbert–Pólya construction.
