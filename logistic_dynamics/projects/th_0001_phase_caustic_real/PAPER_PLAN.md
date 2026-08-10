# Paper plan — TH-0001 on-shell real caustic

**Working title:** An on-shell real caustic in a frozen three-kick Fourier-integral model  
**Type:** short exact-audit / structural-obstruction paper  
**Source freeze:** HP-Dynamics `1b8cc8e`  
**Target:** archive manuscript; no RH claim

## One-sentence contribution

The frozen three-kick phase has a caustic that is attained by the real
stationary canonical relation itself, and an exact rational witness shows a
regular rank-one singularity; therefore a global single reduced phase chart
cannot be silently used for this operator.

## Claims–evidence matrix

| Claim | Evidence | Status | Planned section |
|---|---|---|---|
| Exact frozen phase and clock | Source lock and ordered factorization | Established | §2 |
| On-shell caustic parameterization | Symbolic stationary equations plus (15q_1q_2=1) | Established | §3 |
| Endpoint singularity identity | Jacobian equals (-H_{\rm int}) | Established | §3 |
| Regular rational witness | Six exact kick residuals, rank one, cubic derivative (132) | Established | §4 |
| Route-A boundary | Evaluation tuple and explicit nonclaims | Established | §5 |

## Section outline

### §0 Abstract

State the exact incidence result, the rational witness, and the strict boundary
in one self-contained paragraph.

### §1 Introduction

Motivate why an internal Hessian zero must be tested on the stationary
canonical relation before being called a physical caustic.  State that this is
an A4 audit, not a spectral experiment.

### §2 Frozen ordered FIO

Define (S_a), the three half-integer factors, the stationary equations, and
the internal Hessian.  Freeze clock, normalization, precision, and forbidden
data.

### §3 Exact on-shell incidence

Parameterize the full real nonzero-(t) caustic and prove the endpoint
Jacobian identity.

### §4 Rational rank-one witness

Give the (t=1) trajectory, momenta, six residuals, null direction, and cubic
directional derivative.

### §5 Route-A interpretation and obstruction

Explain the strengthening of OBR-011, report the Route-A tuple, and state why
Route B and determinant/spectrum work remain closed.

### §6 Reproducibility and claim boundary

List commands, exact arithmetic, artifact provenance, and the smallest next
task.

### Appendix A

Record the short algebraic derivations used by the certificate.

## Figure/table policy

No numerical figure or target-data table is appropriate.  The manuscript uses
one compact identity table for the symbolic checks and points to the machine
readable certificate for all exact strings.
