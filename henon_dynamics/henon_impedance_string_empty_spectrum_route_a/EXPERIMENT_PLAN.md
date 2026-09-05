# Claim-driven finite validation

The primary proof is analytic and precedes executable evidence. Frozen
impedances: 0, 1/3, 1/2, 1, 2, 3, 7. Round-trip times: 1/2, 1, 2.
Time/tau ratios: 0, 1/4, 1, 5/4, 2, 11/4, 3. Space/tau ratios:
1/8, 3/8, 5/8, 7/8. This yields 588 rational transport rows and 7 boundary rows.

The six nontransparent parameters, three times and n=-3 through 3 produce
126 spectral rows. For each time, five trigonometric parameters j/6
(j=1,...,5), three hyperbolic parameters 1/2,1,2 and the critical face yield
27 SL rows. The Green action of f(s)=s²+1 at z=1/2+i is checked for every
parameter/time pair: 21 rows, each storing endpoint and one interior values.

The checker uses repeated crossings, the eigenvalue boundary equation,
direct Green quadrature and differentiated SL boundary values. The producer
uses floor arithmetic, logarithmic spectral parameters, an inhomogeneous
polynomial ODE solution and closed norm expressions. A separate lane uses
11 exact symbolic identities, 27 Rayleigh quotients, 81 Volterra integrals,
81 complex-gauge integrals and 12 finite singular modes.

100-digit arithmetic, 60 stored digits; checks are regression, not intervals.
Semantic mutations repair the payload SHA before checking. Ten YAML attacks
also invoke the real release --write entry; optimized modes must refuse.
No target data, empirical model fitting, GPU training or finite-matrix
substitute for operator completeness is involved.
