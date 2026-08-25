# C157 paper plan

## Title

An Abel Half-Wave Trace for Square-Billiard Clean Families

## Claims--evidence matrix

| Claim | Derivation | Receipt |
|---|---|---|
| exact Dirichlet Poisson trace | radial transform plus quadrant identity | checker formula lock, SymPy constant |
| primitive clean-family rearrangement | gcd decomposition of nonaxis dual vectors | 161 exact shell rows through norm 500 |
| boundary singularity classification | principal branch and exponential denominator | SymPy branch scaling and pole residue |
| high-precision equality | primal exponential tail and accelerated Epstein dual tail | deterministic complex centers with analytic truncation envelopes and a `1e-34` comparison margin |

## Structure

1. Dirichlet Abel trace and two-dimensional Poisson formula.
2. Primitive directions, repetitions, and multiplicities.
3. Four distinct boundary contributions and exact/numerical certificate.
4. Route-A verdict and declarations.

No external bibliography is needed because the Fourier, Poisson,
Diophantine, and error-bound steps are proved directly in the package.
