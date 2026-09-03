# Research question

For the no-loop one-edge preferential-attachment tree, can one prove within a single convention-locked theorem both microscopic hub growth and the macroscopic degree profile?

The microscopic statement asks for every fixed vertex `i` and every integer `r>=1`: an exact all-time rising-factorial moment, a nonnegative martingale, almost-sure and all-finite-`Lp` convergence of `D_i(n)/sqrt(n)`, and a moment-determinate limit law with explicit moments.  The macroscopic statement asks, separately, for `N_k(n)/n` to converge in `L2` to the exact cubic-tail mass `4/[k(k+1)(k+2)]` for each fixed `k`.

The answer is yes.  The proof uses conditional rising-factorial closure for the first scale and a lower-triangular stochastic-approximation recursion with bounded martingale noise for the second.  It does not assert a theorem about the maximum degree, a joint law of all hubs, or another preferential-attachment seed convention.
