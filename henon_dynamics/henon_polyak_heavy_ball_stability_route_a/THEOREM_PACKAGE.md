# Theorem package

For `f(x)=x^T A x/2-b^T x`, `0<m I<=A<=L I`, and real `alpha,beta`, the error
mode at eigenvalue `lambda` has polynomial

`r^2-(1+beta-alpha lambda)r+beta`.

The package proves in one classification:

1. Robust convergence for the whole spectral interval holds exactly when
   `-1<beta<1` and `0<alpha<2(1+beta)/L`, including negative momentum.
2. The exact mode radius is `sqrt(beta)` on the complex plateau and otherwise
   `(|a|+sqrt(a^2-4beta))/2`; the interval supremum occurs at an endpoint.
3. For `m<L`, the unique minimax real constant parameters are
   `alpha*=4/(sqrt(L)+sqrt(m))^2`, `beta*=q^2`,
   `q=(sqrt(L)-sqrt(m))/(sqrt(L)+sqrt(m))`.
4. At both minimax endpoints the blocks are defective.  Generic convergence
   is `O(k q^k)` with root factor `q`, not a uniform `C q^k` bound.
5. For `m=L`, `alpha=1/m,beta=0` annihilate the error in one step and the phase
   state in two.
6. The full characteristic polynomial, trace, determinant and identity
   `M^T J M=beta J` hold in every dimension.
7. At `beta=1`, fixed-A elliptic blocks have finite order exactly when all
   rotation angles are rational multiples of `2 pi`; a nontrivial continuous
   spectral interval has no uniform finite order.  The `beta=-1,alpha=0`
   swap is the other full-state finite-order case.

The finite certificate is a convention and hostile-regression ledger.  The
all-real theorem follows from the algebraic proof.
