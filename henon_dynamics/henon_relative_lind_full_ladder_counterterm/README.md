# HCS-P73: Relative Lind full-ladder counterterm

P72 isolates every scalar-channel singularity of the uniquely normalized
H\'enon packet/Lind relative germ.  P73 resolves the resulting
renormalization problem.  For

    rho_m = 2^(-1/(2m)),
    alpha_(m,k) = rho_m exp(pi i k/m),
    b_(m,k) = c_m (-1)^k/(sqrt(2)m),

the exact partial fraction identity is

    c_m Phi(t^m) = sum_(k=0)^(2m-1) b_(m,k)/(1-t/alpha_(m,k)).

The raw double pole sum is not absolutely summable.  Subtracting the first
`m` Taylor terms from every level-`m` pole (Weierstrass genus `m-1`) changes
no channel sum and makes the complete pole family absolutely normally
convergent on compact subsets of the punctured unit disk.  Its sum is the
exact P72 tail `L(t)=sum_(m>=2)c_m Phi(t^m)` and is independent of pole
ordering.

Writing `w=1+sqrt(2)t`, the normalized counterterm

    K_all(t) = exp(3/2) w^(1/2) exp(-3/(4w)) exp(L(t))

satisfies `K_all(t) C_rel(t)=1` on every compatible branch.  This is exact
analytic renormalization, but the counterterm copies the full scalar-channel
ledger.  It supplies no transfer operator, rational-prime semantics, or
Route-B result.

**Status:** full complex divisor, regularized pole product, absolute normal
convergence, order independence, and exact cancellation PROVED; raw
pole-by-pole ordering REFUTED; operator ownership OPEN; arithmetic advance
NO.  Reproduce with `bash code/run_c73.sh` and see `paper/paper.pdf`.
