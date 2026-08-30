# Deterministic experiment and audit plan

## Frozen parameter census

Enumerate all 27 triples from the rational beta, increase, and rate grids.
For each tuple compute exact (Z=Y^2) moments through order eight, a
12-factor prefix of the stationary Laplace product, three rational (s)-spot
values, generator moment coefficients (M_m=c_m+d_m\mu), and six steps of a
rational hazard skeleton with (Y_{n+1}-\beta Y_n=1).

## Independent computation

`c246_tcp_aimd_checker.py` independently derives the square-affine recurrence,
perpetuity moments, product coefficients, generator coefficients, reward
integrals, and boundary rows without importing the producer.  SymPy checks the
hazard integral, the (2a/\rho) square completion, exponential Laplace factor,
generator identity, continuous Laplace-generator identity, and Palm reward ratio.  Byte replay compares two fresh
producer outputs.

## Adversarial controls

The mutation suite makes 36 no-op-guarded repaired/stale-hash edits to beta,
the (a) factor, moments, q-product coefficients, occupation wording,
Markov-versus-iid flag, reward skeleton, boundaries, metadata, route tuple,
scope firewall, and unknown keys.  Every changed receipt is rejected.

The q-product and occupation identities are source-local probability
certificates.  They are not arithmetic Euler products, target determinants, or
claims of an iid regeneration structure for positive beta.
