# Narrative report

The periodic SSH slogan “the edge phase is `w>v`” loses one finite-size
distinction.  For `M` open cells, the characteristic equation is

`U_M(x)+(w/v)U_(M-1)(x)=0`,

where `x=(E^2-v^2-w^2)/(2vw)`.  A pair leaves the trigonometric interval
through `x=-1` only at `w/v=(M+1)/M`.  Thus the interval

`1 < w/v <= (M+1)/M`

is bulk-topological but has no strictly hyperbolic finite-chain pair.  At
the equality the eigenvector is a signed linear taper and the energy is
`v/M`; its nonzero linear taper is the common-`1/kappa` rescaled limit of
the raw hyperbolic vectors.  Above it there is one pair `+-E_edge` with
exact two-ended hyperbolic profiles and an exponential inward-decay bound.

This distinction is finite, sharp, and asymptotically compatible with
bulk--edge intuition: for fixed `r=w/v>1`, the hyperbolic parameter tends
to `log r` and the edge splitting is asymptotic to
`w(1-r^-2)r^-M`.  It is not an exact zero at finite `M` when `v>0`, because
`det T=v^M`.

The periodic theorem has a different finite caveat.  The Bloch loop
`q(k)=v+w exp(ik)` winds counterclockwise once when `w>v`; the continuum
gap-to-zero is `|v-w|`.  The finite sampled gap equals this for even `M`,
but for odd `M` it is
`sqrt(v^2+w^2-2vw cos(pi/M))`.  Thus at `v=w>0` an even ring has a
two-dimensional zero fiber, while an odd ring has the strictly positive gap
`2v sin(pi/(2M))` even though the continuum symbol is gapless.

All singular faces are stated directly.  With `w=0` there are `M`
intracell dimers.  With `v=0` there are `M-1` intercell dimers and two exact
edge zeros.  At the origin the Hamiltonian is zero.  At `v=w>0`, the open
chain is a uniform path and has no zero.  For `M=1`, the open intercell bond
is absent while the periodic bond merges with the intracell bond.

The matrix-cosine/sinc propagator uses entire functions and therefore
survives all those faces.  A separate quench corollary says that positive,
gapped initial and final Bloch Hamiltonians have a continuum mode-amplitude
zero exactly when they lie in opposite phases.  It deliberately does not
promote that statement to every finite ring: a finite zero exists only if
the derived `k*` belongs to that ring's momentum grid.

The result is a substantial exact atlas for a Hermitian chiral quantum
chain, while remaining disjoint from C308's non-Hermitian one-site
Hatano--Nelson skin chain.  The entire result is source-local.  Route A is
rejected, Route B is locked, and no arithmetic or target-spectrum claim is
made.
