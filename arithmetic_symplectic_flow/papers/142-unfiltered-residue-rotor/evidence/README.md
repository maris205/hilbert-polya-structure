# Evidence — ANG-20260915-URR01

**Status:** STOP — NATIVE ARITHMETIC RETURNS; INFINITE TWO-PACKET MULTIPLICITY.

## Frozen inputs and exact method

The [version-1 card](../candidate-card.md) was frozen before this audit.
The input is the full discrete all-integer carrier Y, all nonzero modular
increments, exactly F, unit roof and the complete ordinary unweighted
primitive product. No prime list, prime predicate, unit prefilter or
postselected orbit family is an input.

The reproducible method is entirely in the [paper](../paper.md):

1. Iterate addition to obtain the return equation n divides ka.
2. Divide by g=gcd(n,a), and use the coprime congruence to obtain the least
   period n/g; count cosets to retain g packets.
3. Contrast all nonzero increments of a prime modulus with a proper-divisor
   increment of a composite modulus.
4. Use all n=2k,a=k to exhibit infinitely many genuine two-packets.
5. Take L distinct such packets: the exact finite subproduct is
   (1-exp(-2s))^(-L), which tends to infinity for every real s>0.

There are no numerical inputs, finite orbit tables, cutoff claims,
floating-point precision choices or computational experiments. No empirical
observation is used to support an infinite statement. All formulas and
limits are elementary and proved for the frozen full carrier.

## Evidence boundary

The prime criterion uses the complete distinguished n-fibre, not an
individual packet or the globally unlabelled length set. Its arithmetic
content is native return shortening by divisors, not a static unit filter.
It does not supply a one-prime/one-packet dictionary or a logarithmic clock.

The ordinary-product failure retains all multiplicities. No quotient,
changed roof, weighting, operator or regularized trace is tested as a repair.
Model review and file validation are internal research checks, not
independent human peer review or formal proof-assistant certification.

[Claim ledger](../claim-ledger.md) · [Paper](../paper.md).

The [separate definition-level model check](review.md) independently
verified the stated congruence, multiplicity and product claims, with the
fibre-observation and clock boundaries preserved.
