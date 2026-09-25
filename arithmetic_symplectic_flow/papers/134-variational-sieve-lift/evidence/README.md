# Evidence — ASFS-20260914-VSL01

**Date:** 2026-09-14  
**Status:** `P0 GEOMETRY ESTABLISHED; A0 SCOPED FAIL — FINITE SOURCE EQUILIBRIUM; PERIOD-6 CONTINUUM CONTROL`

## Source identity and boundary

Ricardo Adonis Caraccioli Abrego, *The Prime Sequence as the Unique Fixed Point
of a Causal Binary Sieve*, Zenodo version 1, 2026-04-29,
DOI 10.5281/zenodo.19894709. The [record](https://zenodo.org/records/19894709)
and linked [TeX source](https://zenodo.org/records/19894709/files/Fluctuation.tex?download=1)
were inspected on 2026-09-14, specifically the definition titled Causal sieve
operator. The record is a preprint source, not a claim of peer-reviewed status.

Its rule on binary candidate sequences gives the polynomial window
G(q)=(1,1,1-q_2) on labels 2,3,4. The real extension, squared residual,
canonical map, and proofs in 134 are separately frozen constructions; they
are not attributed to the source. The source's later externally supplied
von-Mangoldt weights and block prime memory are not part of this candidate.
The local antecedent [050](../../050-causal-binary-sieve-fixed-point-screen/paper.md)
records the complete binary source and its own scope.

## Exact inputs and reproduction

All inputs are in the [version-1 card](../candidate-card.md). The
[paper](../paper.md) supplies the exact gradient, residual Jacobian, inverse
map, symplectic pullback, invariant plane, 2-by-2 recurrence matrix, and
divergent product argument. These explicit algebraic proofs constitute the
mathematical output. There is no numerical integration, orbit search,
precision parameter, source-window sweep, or target-zero comparison.

The cutoff 4 is the frozen object's dimension choice, not a numerical
approximation claimed to prove an infinite model. No N-dependent map or
infinite-coordinate candidate is constructed here. The product obstruction
uses exact arbitrary finite subfamilies from an explicitly established
continuum, without requiring classification of other periodic points.

## Verification and handoff

An independent delegated model audit confirmed the explicit gradient/Hessian,
global inverse and symplecticity, unique equilibrium, exact least period 6,
and the divergent finite-subproduct argument. It emphasized that identity
monodromy is proved only on the two-dimensional tangent plane and that no
full periodic classification is needed or claimed. This is model-assisted
proof checking, not external peer review or a novelty judgment.

The package is checked for existing local Markdown links and matching candidate
ID and status. These documentary checks are distinct from mathematical proof.

**Decision:** `stop`; portfolio `fork`. A0 scoped FAIL; formal A1/A2 and
Route-A coordinates NOT EVALUATED; Route B NOT INVOKED. The periodic and
product calculations are authorized structural prechecks with unchanged
object, unit roof, and full multiplicity.
