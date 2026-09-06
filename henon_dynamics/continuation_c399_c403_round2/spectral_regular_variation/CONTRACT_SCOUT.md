# One retained spectral contract

Date: 2026-09-05. Scope: unfinished C399--C403 research, no C number assigned.

Question: does every positive slowly-varying perturbation of power
coefficients, without arithmetic multiplicativity, have the same normalized
divisibility Gram limit, and in precisely which Schatten ideals?

The [complete proposed proof](PROOF_PACKAGE.md) answers this for every
sigma<1/2 and every positive measurable slowly-varying L with local upper
and lower bounds. With rho=1-2sigma and a(k)=k^(-sigma)L(k),

    rho T_N(a)^*T_N(a)/(N^rho L(N)^2) -> E_sigma in S_q
        exactly for q rho>1,
    E_sigma(m,n)=(mn)^sigma/lcm(m,n).

At and below the threshold the finite-rank approximation error does not
belong to S_q. The proof uses a uniform Potter majorant, positive diagonal
congruence, uniform spectral tails, and singular-value dominated convergence,
including q<1. It includes oscillatory L and normalization by sum |a(k)|^2.

The [source audit](SOURCE_AUDIT.md) credits the entire LCM spectral theorem,
Gram identity, regular-variation tools and earlier multiplicative convergence
results. The proposed increment is one nonmultiplicative universality
theorem with a sharp convergence range, not a new arithmetic spectrum or
separate papers for each ideal. Merely reproducing LCM/Helson spectra was
discarded. No numerical experiment is offered as a substitute for proof.

Independent internal review is pending. A mathematical gap or a directly
owning primary source would change admission; citation-search absence alone
does not admit the contract. No manuscript, formal Route A grade, release
manifest, target-arithmetic success or completed batch is claimed here.
