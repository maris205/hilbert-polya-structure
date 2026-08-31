# Theorem package

## Frozen notation

Use additive notation (T_d(x)=dx) on (G=\bigoplus_i C_{n_i}). For (d\ge1), factor (n_i=a_i b_i) by placing in (b_i) exactly the prime-power factors whose primes divide (d). Put (A=\bigoplus_i C_{a_i}), (B=\bigoplus_i C_{b_i}), (K_j=\prod_i\gcd(d^j,b_i)), and
\[
R_j=|A|\prod_i\frac{b_i}{\gcd(d^j,b_i)}.
\]

## Main theorem

1. Chinese remaindering conjugates (T_d) to (T_d|_A\times T_d|_B). The first factor is an automorphism and the second reaches zero after
   \[
   h=\max_{p\mid d}\left\lceil\frac{\max_i v_p(b_i)}{v_p(d)}\right\rceil.
   \]
2. The periodic set is exactly (A\times\{0\}). Every periodic vertex carries the same rooted in-tree, namely the tree of (b\mapsto db) on (B); its exact depth-(j) population is (K_j-K_{j-1}), (K_0=1).
3. For every (n\ge1),
   \[
   F_n=|\operatorname{Fix}(T_d^n)|=\prod_i\gcd(d^n-1,a_i).
   \]
   Exact-period points and cycles are
   \[
   P_m=\sum_{e\mid m}\mu(m/e)F_e,\qquad C_m=P_m/m.
   \]
   Consequently
   \[
   \zeta_{T_d}(t)=\exp\!\left(\sum_{n\ge1}F_n\frac{t^n}{n}\right)
   =\prod_{m\ge1}(1-t^m)^{-C_m}.
   \]
4. On all complex functions (U f=f\circ T_d), (operatorname{rank}U^j=R_j). The number of zero Jordan blocks of exact size (j) is
   \[
   Z_j=R_{j-1}-2R_j+R_{j+1}.
   \]
   The full characteristic polynomial is
   \[
   \det(\lambda I-U)=\lambda^{|G|-|A|}\prod_m(\lambda^m-1)^{C_m}.
   \]
5. For (d=0), (T_0) is constant at the identity: one fixed point, (|G|-1) vertices at tail one, zeta ((1-t)^{-1}), and a diagonalizable Koopman operator with eigenvalues (1,0^{|G|-1}).

## Proof boundary

The formulas are source-dynamical. They do not provide arithmetic local data, bad Euler factors, root numbers, automorphy, a target divisor or functional equation, or a Hilbert–Pólya operator.
