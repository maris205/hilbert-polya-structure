# C152 paper improvement log

No external or cross-model reviewer was available or claimed.  These are two
genuine internal theorem/scope audits without numerical scores.

## Round 0 to round 1

The initial proof sketched Möbius interchange and the primitive density but
did not control the absolute transformed sum or state whether `Q(R/d)` used a
real radius.

**Fix:** add the integral bound
`theta_+(4td^2)<=sqrt(pi)/(4d sqrt(t))`, making the absolute `d^-2` sum
explicit; define `Q` for every real radius; derive the scaled inequality used
by exact code; and state `sum mu(d)/d^2=6/pi^2` with its convolution and Basel
justification.

## Round 1 to round 2

The second audit found possible ambiguity between a source direction heat
transform and a Dirichlet spectral heat trace.  It also required exact
collision bookkeeping and a full remainder calculation.

**Fix:** state three nonidentities (wave trace, isolated determinant,
Dirichlet spectral trace), replace “same length source” by “same unit-square
classical geometry,” retain ordered collision multiplicity, and show the
Stieltjes error after `u=sqrt(t)r` is
`O(t^(-1/2)log(1/t))`.

## Final audit

The final PDF is checked against the exact coefficient/count evidence,
independent checker and SymPy paths, replay, repaired-hash mutations, scope
flags, deterministic compilation, embedded fonts, clean logs, extracted text,
and rendered pages.
