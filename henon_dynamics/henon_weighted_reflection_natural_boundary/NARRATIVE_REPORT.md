# HCS-P76 narrative report

P72 saw only the positive roots in the unweighted fiber.  The weighted
channel formula exposes much more geometry.  Channel `m` has `2m` roots on
the circle of radius

    rho_m(q)=(1+q^(2m))^(-1/(2m)).

For every positive `q`, these radii are strictly increasing and tend to
`L(q)=min(1,q^(-1))`.  Since the channel coefficient never vanishes and
different channels have different moduli, every listed root is an
exponential essential singularity.  The angular mesh has gap `pi/m`, so the
roots accumulate at every point of `|z|=L(q)`.  No meromorphic continuation
can cross even a small arc of that circle.

This is a genuine global analytic theorem, but only for the exact
unrenormalized packet continuation.  P73-style all-channel subtraction can
remove a prescribed divisor and therefore changes the object.  The result
does not construct an operator or attach rational-prime semantics.  It sets
up P77's narrower ownership test: an acceptable operator must be specified
independently of the function it is asked to reproduce.
