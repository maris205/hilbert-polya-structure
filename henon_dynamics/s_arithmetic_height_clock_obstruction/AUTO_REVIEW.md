# Adversarial review record

## Scope

Three adversarial passes reviewed this project from complementary angles:

1. mathematical validity and theorem scope;
2. code, numerical precision, and artifact integrity;
3. Route-A positioning, evidence coverage, and prior art.

This record distinguishes theorem proofs from computations and distinguishes
changes made in the project-level Markdown from residual issues in files that
were outside this revision's write scope.

## Consolidated verdict

The central calculations survive review when stated narrowly:

- the quaternion algebra and selected split places are consistent;
- the displayed projective $S$-unit centralizer has a rank-two clock;
- primitive nonzero lattice directions obey the expected gcd repetition law;
- continued fractions give a primitive near-wall sequence;
- the real-only one-flat class product fails a necessary convergence
  condition;
- the normalized Weil height supplies the displayed proper scalarization and
  geometry-of-numbers asymptotic;
- a bounded function of one fixed Hecke operator does not change the $T^2$
  Weyl order of the full compact-surface baseline.

These facts support an explicit arithmetic example with scoped Route-A
obstructions. They do not support a general no-go theorem, a global
prime-geodesic theorem, a new higher-rank zeta theory, or a Hilbert--Pólya
operator.

## Audit 1: mathematics and theorem scope

### Findings retained

- The Hilbert-symbol calculation, anisotropic arithmetic-lattice conclusion,
  $S$-unit basis, joint real/tree lengths, irrationality argument, continued-
  fraction construction, Weil-height factor $2$, lattice constants, and
  bounded-perturbation Weyl argument are correct in their intended setting.
- The one-flat divergence statement is correctly scoped to ordinary finite,
  nonzero product convergence for the real specialization.
- The two-variable product converges in the stated positive region, although a
  published proof should state the uniform geometric-tail estimate and local
  uniformity used for differentiation.

### Resolved in the project-level Markdown

- The positioning is now “explicit arithmetic example with scoped Route-A
  obstructions” and “scoped Route-A assessment.”
- The flat is described as the centralizer quotient of the minimum flat; its
  orbifold image may be immersed and may have a finite Weyl quotient.
- The primitive rule explicitly excludes $(m,n)=(0,0)$.
- The height discussion specifies normalized local height and defines the
  eigenvalue ratio up to inversion.
- The proof/computation boundary is explicit throughout the project-level
  documentation.

### Resolved by the concurrent manuscript pass

The parent workflow separately revised the paper and `DERIVATION_PACKAGE.md`;
those files were not edited in this Markdown-only pass. The concurrent changes

- removed the derivation package's pseudo-LaTeX and control bytes;
- restricted the real invariant-length formula to an
  orientation-preserving hyperbolic element with positive norm;
- added the projective scalar and reduced-trace argument to the centralizer
  proof;
- proved regularity for nonzero pairs and identified the Weyl inversion as the
  only further conjugacy relation;
- qualified the flat as an immersed periodic flat with a possible finite Weyl
  quotient; and
- defined the orientation-preserving arithmetic orbifold, normalized Hecke
  operator, compact-resolvent statement, and eigenvalue-counting convention.

The mathematical audit found no remaining critical error in the core theorem
chain after those corrections. The conclusions remain restricted to the
explicit centralizer and bounded fixed-Hecke baseline.

## Audit 2: code, precision, and artifact integrity

### Original findings

- Binary64 logarithms with a fixed boundary epsilon did not justify calling
  the finite transcendental-boundary counts exact.
- The original independent checker admitted vacuous passes for empty sample or
  near-wall arrays and an empty hash manifest, omitted several schema and
  JSON/CSV consistency checks, and did not guard the zero input of its
  $13$-adic valuation helper.
- The hash manifest covered only selected generated result files. It was an
  integrity convenience, not authentication and not provenance for code,
  documentation, the paper, or evaluation records.
- The reported finite values were nevertheless rechecked at high precision.
  The nearest inspected box boundary was about
  $8.62\times10^{-4}$ away, and the nearest inspected height boundary was
  about $3.75\times10^{-3}$ away, so the published finite decisions were
  robust to the original binary64 rounding.

### Implemented remediation

The companion code-review pass implemented and validated the code/result
changes. The producer now uses exact `Fraction` algebra together with 80-digit
`Decimal` evaluation for logarithms, near-wall selection, finite boundary
decisions, and its numerical value of $\pi$. It records conservative positive
boundary gaps and no longer uses a fixed binary64 epsilon.

The checker now enforces required inputs, schemas, nonempty and duplicate-free
records, the exact four-file manifest key set, digest syntax, the six frozen
sample coordinates, JSON/CSV agreement, and full rederivation of model,
generator, clock, sample, near-wall, and count fields. Its independent
numerical path uses 120-digit `Decimal` arithmetic and a separate computation
of $\pi$. The valuation helper rejects zero, and mutation tests exercise the
formerly vacuous paths.

The default generated output is byte-reproducible. The independent checker
reports $16/16$ grouped checks with no errors, all eleven tests pass, and a
custom near-wall cutoff of $400$ also passes. These are software-validation
facts, not additional mathematical theorems.

### Residual numerical and provenance limits

- Finite `Decimal` precision plus a second higher-precision recount and
  positive margins is strong reproducibility evidence, but it is not a formal
  transcendence or interval-arithmetic proof.
- Some serialized diagnostics may be converted to binary floats for JSON
  presentation; decisions should continue to be made before that conversion.
- The four-artifact hash manifest is not a signature. Git or a release
  manifest must provide provenance for code, documentation, paper, evaluation
  YAML, and the independent-check output.
- Passing computational checks does not verify the centralizer, periodic-flat,
  Weil-height, or Weyl theorems; those depend on the written proofs.

## Audit 3: Route-A positioning and source boundary

### Findings retained

- The negative conclusion is justified only for the displayed real-only
  one-flat specialization, the isolated-orbit interpretation, and the full
  compact-surface baseline with a bounded fixed-prime Hecke perturbation.
- Earlier wording overstated “exact” finite counts and gave too much weight to
  a title-based novelty gap.
- Sixteen checker flags were not sixteen independent validations of the
  mathematical theorem package.
- The source-commit identifier did not bind all project documentation, paper,
  and evaluation artifacts because those files were untracked in the audited
  checkout.
- The initial route-review report did not locate the local prior-work PDF;
  the parent audit subsequently verified that it is present at
  `henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`
  and had been included in the source review.

### Resolved in the project-level Markdown

- Novelty language is now explicitly search-bounded and modest.
- Nguyen-Thi Dang and Jialun Li's published work on periodic tori in Weyl
  chambers (DOI `10.4171/CMH/594`, preprint arXiv:2305.17070, with related
  predecessor arXiv:2202.08323) is included as directly relevant prior art.
- Unsupported fallback claims were removed.
- The 2026 Hecke--Ruelle item remains labeled as an announced overlap risk,
  not as a verified published theorem.
- The local prior-work PDF path and its role as the foundational Hénon
  baseline are now stated explicitly.
- Claims that preprints were cited or labeled in the manuscript were removed.

### Residual Route-A and release issues

- The hardened computation is frozen at commit `24553c8`; the complete
  package must still be committed, tag-bound, and verified against the
  top-level release manifest before push.
- The parent manuscript pass narrowed the title and prose to match the scoped
  worked-example positioning.
- No global determinant, functional equation, continuation theorem, divisor
  identity, or height-compatible self-adjoint operator is supplied.
- A future scattering or unbounded-operator direction requires a fresh
  construction and source audit; it is not an outcome of this project.

## Resolution ledger

| Issue | Status after this pass |
|---|---|
| Pseudo/mangled LaTeX in authorized project Markdown | resolved |
| Control characters in authorized project Markdown | resolved after byte-level lint |
| Overbroad Route-A and novelty positioning | resolved in project Markdown |
| Exact-count wording | replaced by high-precision reproducible numerical wording |
| Proof versus computation distinction | added |
| Dang--Li periodic-flat prior art | added |
| Unsupported fallback discussion | removed |
| Initially unlocated local prior-work PDF | resolved; present and audited at the repository path above |
| `DERIVATION_PACKAGE.md` corruption | resolved by concurrent parent manuscript pass; not edited here |
| Overbroad invariant real-length hypothesis | resolved by concurrent parent manuscript pass |
| Full project provenance/source freeze | release manifest added; final commit/tag/push still required |
| Global higher-rank determinant or Hilbert--Pólya operator | not supplied and not claimed |

## Final assessment

The defensible result is a worked quaternionic $S$-arithmetic example with a
proved joint clock, a proved near-wall obstruction for one rank-one
specialization, a proved height identity and one-flat counting asymptotic, and
a scoped bounded-Hecke Weyl assessment. The numerical artifacts support
reproducibility but do not replace the proofs. Remaining manuscript and
release-provenance issues should be closed before presenting the package as a
final source-frozen paper. The remaining release actions are recorded in
`REPOSITORY_UPDATE.md`.
