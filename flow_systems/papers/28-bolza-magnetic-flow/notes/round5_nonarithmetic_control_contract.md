# P28 Round-5 non-arithmetic genus-two control contract

Date: **2026-08-27**

Status: **`[OPEN] / DESIGN_ONLY_NOT_INSTANTIATED`**.

This document is a pre-execution source and parameter contract.  It does not
name a control surface, claim a non-arithmeticity proof, load control matrices,
or report a comparison result.

## Required source package

Execution is forbidden until one package supplies all of the following:

1. a closed, oriented, constant-curvature `-1`, genus-two surface;
2. explicit torsion-free cocompact Fuchsian matrices and a presentation;
3. a primary or peer-reviewed locator for the representation;
4. a checked polygon/group relation and faithful action certificate;
5. an independent non-arithmeticity certificate using invariant trace-field,
   quaternion-algebra, or an equivalent valid criterion; and
6. a rigorous systole certificate or stronger per-owner primitivity proof.

“Generic metric” is not a substitute.  Arithmeticity is a lattice property in
the constant-curvature setting, and a variable-curvature perturbation would
change the dynamical model rather than instantiate the requested control.

## Matched parameters

The admissible control must keep

```text
genus=2
curvature=-1
area=4*pi
field_b=+1/2,-1/2
base_bundle_degree=+1,-1
tensor_subsequence=N=2m
square_root_connection=L^2=K
source_parameter_E=sqrt(5)
trace_clock=(sqrt(5)/2)*physical_clock
signed_k=+-1,+-2,+-3,+-4
owner_counting=inverse-paired axis; signed k has no owner credit
```

The zero-field theorem, odd powers, arbitrary flat twists, full all-`N`, and
fixed-operator regimes remain separate and open.

## Selection and cutoff firewall

The control may repeat the `L=4` marked-cyclic audit only after its generator
marking is frozen.  Marked length is presentation-dependent, so it cannot be
the sole cross-metric selection rule.  Before inspecting branch outcomes, the
comparison must freeze a common geometric cutoff `Lambda`.  Unless stronger
individual primitivity proofs are supplied, it must satisfy

```text
Lambda < 2 min(sys_Bolza,sys_control).
```

This separates the auditable marked-word census from the metric-comparable
geodesic subset.

## Forbidden inputs and route status

No rational-prime target, prime-ideal target, zeta-zero target, or fixed
operator spectrum may be used to select the control or the cutoff.

```text
GEOMETRY_SELECTED=false
SOURCE_VERIFIED=false
MATRICES_LOADED=false
CENSUS_RUN=false
COMPARISON_RUN=false
FORMAL_ROUTE_A_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
```

The machine-readable version is
`results/round5_nonarithmetic_control_contract.json`.
