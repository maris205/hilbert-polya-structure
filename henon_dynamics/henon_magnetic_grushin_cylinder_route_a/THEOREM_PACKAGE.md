# Theorem package — HCS-C293

Status: **PROVABLE AS STATED** for the Friedrichs realization.

The closed nonnegative form
`q_alpha[u]=integral(|u_x|^2+x^2|(D_theta+alpha)u|^2)`
defines `G_alpha`.  Fourier mode `k` is the line oscillator
`-d_x^2+(k+alpha)^2x^2`, with levels
`lambda_(k,n)=(2n+1)|k+alpha|` when `k+alpha != 0`.

- If `alpha` is not integral, the resolvent is compact and this is the full
  pure-point spectrum.
- If `alpha` is integral, exactly one resonant angular channel is the free
  line Laplacian.  Its absolutely continuous spectrum is `[0,infinity)` with
  a.e. multiplicity two; the orthogonal oscillator sector has compact
  resolvent, all positive integers as embedded eigenvalues, multiplicity
  `2 d_odd(N)`, and the full operator has no singular-continuous spectrum.
- Off integer flux,
  `Tr exp(-tG)=sum_k[2sinh(t|k+alpha|)]^-1`.  At integer flux the
  nonresonant trace is `sum_{m>=1}1/sinh(tm)`.
- At zero flux on the nonresonant sector,
  `Z(s)=2(1-2^-s)zeta(s)^2`, `Re s>1`, and
  `N(L)=2 sum_(j odd) floor(L/j)
       =L log L+(2 gamma+log2-1)L+O(sqrt L)`.

Flux is periodic modulo integers and reflection symmetric.  Irrational flux
has simple levels; rational flux permits finite Diophantine coincidences;
half flux has systematic double pairing.  As flux approaches an integer, one
oscillator frequency collapses and its heat contribution diverges like
`1/(2t dist(alpha,Z))`.

The zeta and divisor formulas are source-local.  They are not target Euler
factors, a target divisor law, functional equation, zero match, or
Hilbert–Pólya construction.
