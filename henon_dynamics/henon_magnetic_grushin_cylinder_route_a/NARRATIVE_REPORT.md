# Narrative report

HCS-C293 changes spectral type under a single flux parameter.  Away from
integer flux, every Fourier sector is a confining oscillator and the full
direct sum has compact resolvent.  At integer flux one angular mode loses its
potential and becomes the free line Laplacian.  The full operator then has
both a multiplicity-two absolutely continuous component and embedded finite-
multiplicity point spectrum, while its singular-continuous part is empty.

The nonresonant sector produces an exact source-side arithmetic-looking
structure: positive integer levels have multiplicity `2 d_odd(N)`, the heat
trace separates, the zeta series is `2(1-2^-s)zeta(s)^2`, and its counting
law is `L log L+(2 gamma+log2-1)L+O(sqrt L)`.  The manuscript derives all of
these from two Fourier–Hermite indices.

The evidence audits 293 cells.  The independent checker reports 2,053
assertions, SymPy 750 identities, two isolated replays are byte exact, and
75/75 hostile mutations are rejected: 54 target the evidence JSON and 21
target the separately parsed evaluation YAML.  The direct heat checker sums the
levels and does not copy the producer's closed hyperbolic-sine trace.

The source zeta earns only weak/partial Route-A labels.  It cannot be read as
target local data, target Euler factors, a target divisor law, functional
equation, zero correspondence, or a Hilbert–Pólya operator.  Overall Route A
is rejected and Route B is disabled.
