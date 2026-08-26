# C188 source audit

## Primary source lock

1. Sergei Sergeev, “Max algebraic powers of irreducible matrices in the
   periodic regime: An application of cyclic classes,” *Linear Algebra and its
   Applications* 431(8) (2009), 1325–1339.
   DOI: <https://doi.org/10.1016/j.laa.2009.04.027>.
   Author manuscript: arXiv:0903.3960.

   The introduction states the classical cyclicity theorem in the needed
   strength: for an irreducible matrix, the ultimate period of the matrix-power
   sequence equals the cyclicity of the critical graph.  The paper develops
   cyclic classes, periodic powers, ultimate spans and attraction cones.  This
   is the ownership source for the exact minimal ultimate period `gamma`; the
   package does not relabel that theorem as new.

2. Sergei Sergeev and Hans Schneider, “CSR expansions of matrix powers in max
   algebra,” *Transactions of the American Mathematical Society* 364(11)
   (2012), 5969–5994.
   DOI: <https://doi.org/10.1090/S0002-9947-2012-05605-4>.
   Author manuscript: arXiv:0912.2534.

   This is the ownership source for `C S^t R` products, their periodic
   structure, the ultimate CSR expansion, and the reducible multiple-term,
   multiple-growth-rate boundary.  The irreducible normalized specialization
   used here is `B^t=C S^t R` after a matrix-dependent transient.

Both DOI/title/author/journal records were checked against publisher or
official arXiv metadata on 2026-08-26.  The journal paper and arXiv title of the
first item differ; both identifiers are recorded rather than silently merged.

The sources primarily write max algebra in max-times notation on nonnegative
numbers.  The logarithm sends max-times multiplication to max-plus addition and
the zero element to `-inf`, while leaving maximum unchanged.  It preserves the
support digraph, critical cycles, component cyclicities, matrix powers and CSR
identities.  We use this exact semiring isomorphism, then restrict the resulting
real max-plus theorem to the rational-weight subfamily; no theorem is imported
across a nonequivalent convention.

## Exact convention

- Semiring: `Q_max = Q union {-inf}`, `x plus y=max(x,y)`,
  `x times y=x+y`.
- Source-notation translation: logarithmic max-times/max-plus isomorphism.
- Support edge: `i -> j` iff `a_ij` is finite.
- Irreducible: the support digraph is strongly connected.
- Spectral radius: maximum directed-cycle mean `lambda(A)`.
- Normalization: subtract `lambda(A)` from every finite entry.
- Critical graph: union of all cycles attaining `lambda(A)`.
- Component cyclicity: gcd of all cycle lengths in that critical SCC.
- Critical cyclicity `gamma`: lcm of component cyclicities.
- Clock: one max-plus matrix multiplication.

The lcm is essential when the critical graph has several SCCs.  The finite
census includes a two-cycle plus three-cycle critical graph with
`gamma=lcm(2,3)=6` inside an irreducible support.

## Ownership boundary

Classical/source-owned:

- existence of a finite periodicity transient;
- equality of the minimal ultimate matrix-power period and `gamma`;
- cyclic-class/attraction-cone/ultimate-span theory;
- CSR products and ultimate CSR expansions.

Package derivations and integration:

- `T=min{t:B^(t+gamma)=B^t}` by semigroup propagation;
- exact period strata from divisor-indexed attraction cones;
- the phase-indexed column-cone formulation used in the Route-A audit;
- the explicit fixed-support family `B_m` proving the absence of a
  weight-independent dimension/support transient bound;
- executable cross-checks and adversarial scope enforcement.

The 177-matrix census is regression evidence only.  It is not presented as a
finite proof of either classical all-matrix theorem and not as a
literature-wide novelty certificate.

## Reducible boundary

The diagonal reducible matrix `diag(0,1)` has component growth rates zero and
one.  After normalization by the larger rate its powers contain a `-t` entry,
so no single normalized periodic matrix sequence results.  General reducible
behavior may require several CSR terms and growth rates.  This example is a
boundary witness, not a claim that no reducible matrix can be periodic.
