# HCS-P72: Relative Lind essential-singularity ladder

P71's unique counterterm cancels the first positive entropy boundary, but it
does not globalize the relative germ. The exact regrouping

    log Z_orb(t,1) = sum_{m>=1} c_m Phi(t^m),
    c_m = (1/m) product_{p|m, p odd} (1-p),
    Phi(x) = 2x/(1-2x^2),

has `c_m != 0` for every `m`. After the `m=1` P71 cancellation, the relative
continuation has an exponential essential singularity at

    rho_m = 2^(-1/(2m)),  m >= 2,

and `rho_m` increases to one. Hence this relative object cannot be a
meromorphic finite-state or holomorphic trace-class Fredholm determinant on
the unit disk. A punctured-domain infinite-rank realization remains open.

**Status:** regrouping, continuation formula, and infinite ladder PROVED;
unit-disk meromorphic determinant REFUTED for this germ; arithmetic advance
NO; Route B not authorized. Reproduce with `bash code/run_c72.sh` and see
`paper/paper.pdf`.
