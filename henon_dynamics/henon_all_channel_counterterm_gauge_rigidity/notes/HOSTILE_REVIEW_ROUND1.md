# Hostile review round 1

## Attack 1: the sign of the rigid coefficient is reversed

The raw packet logarithm has `+c_m Phi`, but P74 does not multiply the raw
packet.  It multiplies the P72 relative continuation, whose later-channel
logarithm is `-c_m Phi`.  Since `log W=+d_m Phi+G`, the combined coefficient
is `d_m-c_m`; removability forces `d_m=c_m`.  This sign is replayed in exact
rational arithmetic in both producer and independent checker.

## Attack 2: another channel could cancel the same complex pole

Every pole in channel `m` has modulus `rho_m=2^(-1/(2m))`.  The radii are
strictly increasing, so a pole circle has a unique owner.  Normal convergence
makes the infinite collection of all other channels holomorphic locally.

## Attack 3: meromorphic extension might tolerate a remaining log pole

It cannot.  The logarithm has a simple pole, and the exponential of a
nonzero pole is essential rather than meromorphic.  Thus the coefficient
must vanish exactly.

## Attack 4: the negative boundary coefficient was copied from the positive
boundary without calculation

The paper performs the exact substitution `w=2-u=1+sqrt(2)t` in `H_rel`:

    H_rel(2-w)=3/(4w)-(1/2)log(w)-3/2.

This independently forces `a=3/4` and `beta=1/2` for a nonzero extension.
