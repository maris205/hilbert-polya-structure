# Hostile audit

## Mathematical attacks

1. **Divide by `d_i-1` at a circle.** Rejected.  Circle clocks are defined as
   infinity, their scales are constant, and an all-circle product is a
   stationary flat torus.
2. **Choose one minimizer from a tie.** Rejected.  `I` contains every first
   clock; both curvature residues and the blowup product use the full tied
   dimension `D`.
3. **Call every finite unnormalized singularity finite in normalized time.**
   Rejected.  The endpoint integral is finite exactly for `D<n`; when `D=n`,
   the normalizer has a logarithmically nonintegrable pole.
4. **Call full collapse possible with a flat factor.** Rejected.  A flat clock
   is infinite, so any finite first collapse leaves that factor outside `I`.
5. **Infer Einstein from one factor.** Scoped.  One curved factor is Einstein;
   for a product, full collapse requires all positive Ricci ratios
   `(d_i-1)/a_i` to agree.  All-flat data are separately Ricci-flat.
6. **Claim Type I from scalar curvature alone.** Rejected.  The exact
   `|Rm|^2` residue and a full pointed parabolic-flow limit are proved.
7. **Continue through `T` by allowing negative scales.** Rejected.  The owner
   stops at the positive-metric boundary; no surgery is claimed.

## Release attacks

Fifty-one semantic fields were altered and their payload hashes repaired.
The independent checker rejected all fifty-one.  These include exact
top-level, nested, and row key sets; required-key drops; empty or truncated
factor vectors; a wrong positive tail; a spurious `+inf` tail; a wrong
collapse endpoint; collision/nonclaim tampering; exact case mapping; and a
duplicate/drop-replace attack on every major row family.  A fifty-second trial
changed content without repairing the hash and was also rejected.  Fresh
replay is byte-identical.  The checker contains no producer import.

The Route-A carrier is parsed with a duplicate-key-safe YAML loader.  Exact
schema and nested key sets, axis/tuple/overall consistency, artifact paths,
and the false Route-B lock are checked.  Five embedded carrier attacks cover
duplicate top-level, cutoff and axis keys, tuple disagreement, and YAML
anchor/alias use; all are rejected.

## Collision attacks

- C185 shares only the broad word “flow”; its matrix-sorting orbit and
  isospectral commutator mechanism are absent here.
- C277/C283 own linear heat semigroups.  This paper contains no heat trace,
  zeta, determinant, or Schatten result.
- C133 owns Kirchhoff quantum-graph scattering.  No graph, bond map, or
  unitary propagator appears here.
- C270 studies static sub-Riemannian geodesics, not evolving curvature.

The exact Ricci-flow/product-sphere keyword scan against both registries and
prior release headlines returned no collision through C280.

## Final firewall

All arithmetic scope flags are false.  The tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_REJECTED`; Route B remains disabled.
