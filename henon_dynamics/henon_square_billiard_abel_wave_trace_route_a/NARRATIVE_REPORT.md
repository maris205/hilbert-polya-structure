# C157 narrative report

## Outcome

C157 advances the square-billiard branch from a Gaussian direction transform
to the actual Abel trace of the natural Dirichlet half-wave operator.  Poisson
summation turns the spectral quadrant sum into an exact dual-lattice formula,
and the nonaxis dual vectors reorganize uniquely by primitive billiard
direction and repetition.

## Exact progress

The coefficient of each ordered positive primitive/repetition term is
`2s/pi`, with length `2*sqrt(a^2+b^2)`.  The evidence retains 98 primitive
shells, 239 ordered primitive directions, 161 occupied dual shells, and 373
ordered positive vectors through squared norm 500.  The first fourfold ordered
primitive collision occurs at squared norm 65.

Two complex values in `Re(s)>0` are independently evaluated from the primal
trace and an Epstein-accelerated dual series.  Their differences are
`5.18e-13` and `3.92e-12`, smaller than the rigorous analytic dual truncation
bounds `2.89e-12` and `2.19e-11`.  The deterministic 55-decimal centers are
not interval-arithmetic outputs; the checker uses a `1e-34` comparison margin.

## Boundary repair

The first branch-only narrative was incomplete.  The release now separates
the Weyl `m=0` term, dual-axis `-3/2` branches, interior clean-family `-3/2`
branches, and simple poles of the boundary subtraction at `t in 2Z`.  Axis
branches can coincide with those poles, but their types differ and no
cancellation is claimed.

## Scope

The formula is a genuine source-derived Dirichlet Abel trace and natural
quantization.  It is not an isolated primitive-orbit determinant, a target
trace identity, or an arithmetic factorization.
