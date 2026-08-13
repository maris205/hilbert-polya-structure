# SD-C12 Frozen Experiment Plan

## Object and parity

Use only the entropy-adjacent tensor-atom relative quotient. Odd entropy
ranks p_(2n-1) are plus/super-even and occur in the numerator; even ranks
p_(2n) are minus/super-odd and occur in the denominator:

\[
R(s,z)=\prod_n\frac{1-zp_{2n-1}^{-s}}{1-zp_{2n}^{-s}},
\qquad H(s,z)=R(s,z)R(1-s,z).
\]

Primary z=1. No target-zero data or parameter fitting is allowed.

## Must-run tests

1. Audit paired l1 sums at N=16,64,256,1024,4096,16384 pairs for
   sigma=0.1,0.25,0.5,1 and four frozen complex points.
2. Record observed Cauchy increments and rigorous disjoint-interval tail
   bounds.
3. Verify exact opaque finite-prefix product and trace-log coefficients
   through repetition 10.
4. Verify H(s,z)=H(1-s,z), positive center curvature, and critical-line
   motion without performing a root census.
5. Certify zero-free strips from local-factor margins, especially
   0<Re(s)<1 at z=1.
6. Test offsets 1,2,3; orientation permutations; 32 random bounded-block
   pairings; shuffled/composite/consecutive/random inventories.
7. Test zero-sum and all-positive finite-block patterns.
8. Distinguish fixed super-parity a^r-b^r from repetition holonomy
   a^r+(-1)^r b^r.

## Stop gates

- A fixed negative rank sector triggers STOP_POSITIVE_EULER_ORIENTATION.
- A proved zero-free primary strip triggers STOP_DIVISOR.
- Bounded-local and nonprime controls passing triggers
  STOP_SCOPED / PROVES_TOO_MUCH.
- Route B remains false without a fixed self-adjoint generator.
