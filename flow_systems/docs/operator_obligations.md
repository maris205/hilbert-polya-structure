# Operator Obligations

This registry records Route-B obligations by **one typed operator**.  Passing
coordinates from different operators or from a scalar identity with no
operator owner may not be combined.  Evidence labels follow
`skills/route-b-evaluator.md`.

## Active operator ledger

| Candidate / operator | B1 definition | B2 self-adjointness | B3 spectral type | B4 arithmetic trace / Weil form | B5 divisor | Current boundary |
|---|---|---|---|---|---|---|
| `DEN-WITT-Z-FIN` / none frozen | required inputs absent — `NOT_TESTABLE` | `NOT_TESTABLE` | `NOT_TESTABLE` | `NOT_TESTABLE` | `NOT_TESTABLE` | Route-B entry unauthorized; first define a source-intrinsic trace-bearing operator. |
| `MOD-GEO` / automorphic Laplacian | natural same-quotient host exists | standard self-adjoint realization exists | correct Selberg host, but wrong target counting/support | no rational-prime trace under frozen clock | no completed-$\xi$ identity | Retained only as exact calibration; Route A is rejected for the rational-prime target, so Route B cannot rescue it. |
| `FF-FROB-SUSP-P1-F2-KOOPMAN-P1` / $A_K=-i\,d/du$ | `B1_COMPLETE_OPERATOR_DEFINITION` — `PROVED` | `B2_SELF_ADJOINT` — `PROVED` | `B3_FAIL` — `PROVED` | not invoked in Paper 5 | not invoked in Paper 5 | Limited early audit stops at Gate C: $\sigma_{\rm p}=(2\pi/\log 2)\mathbb Q$, every point is infinitely degenerate, and $\sigma=\sigma_{\rm ess}=\mathbb R$. |
| `FF-FROB-OPERATOR-OWNERSHIP-P1-F2` / Koopman $A_K$ | `B1_COMPLETE_OPERATOR_DEFINITION` — `PROVED` | `B2_SELF_ADJOINT` — `PROVED` | `B3_FAIL` — `PROVED` | `B4_FAIL` — native Lefschetz trace belongs to $\Phi$, not $A_K$ | `B5_FAIL` — native factor is not completed $\xi$ | Full limited audit: `ROUTE_B_REJECTED`; see the Stage-6 YAML. |
| same parent / étale Frobenius $\Phi$ | finite-dimensional graded $\mathbb Q_\ell$-linear action, not a canonical complex Hilbert operator | no canonical positive complex inner product or self-adjoint HP realization supplied | finite eigenvalue ledger $\{1,2\}$, not a Riemann energy spectrum | exact native Lefschetz trace and graded determinant — `PROVED` | native $1/((1-t)(1-2t))$, not completed $\xi$ | Exact determinant owner and positive control; its credits cannot be transferred to $A_K$. |

## Reusable obligations

| ID | Obligation | Why it is mandatory | Smallest acceptable evidence |
|---|---|---|---|
| `OP-OWN-1` | Name the operator that owns every asserted trace and determinant. | Equal scalar functions can arise from orbit, fixed-point, cohomological, or spectral ledgers with different owners. | One space, action, domain/test class, trace theorem, and determinant convention in a common source lock. |
| `OP-DOM-1` | Specify the full dense domain and boundary conditions before spectral claims. | A formal differential expression is not a closed operator. | Graph domain, boundary traces, closedness/closability, and a core or equivalent theorem. |
| `OP-SA-1` | Prove self-adjointness, not just symmetry or unitarity of a finite approximation. | Real eigenvalues do not imply a self-adjoint infinite operator. | Deficiency/extension theorem, quadratic form, Stone generator, or explicit unitary equivalence. |
| `OP-SPEC-1` | Prove the actual spectral type and multiplicities. | Self-adjointness alone permits dense point spectrum and essential spectrum. | Compact resolvent or another precise target mechanism; spectral projections and essential spectrum audited. |
| `OP-HEAT-1` | Audit compactness and trace ideals before writing a spectral determinant. | Ordinary Fredholm and heat-zeta determinants require trace/compactness hypotheses. | Trace-class/nuclear theorem or an explicitly different regularization with a proved domain. |
| `OP-TRACE-1` | Derive prime-power weights from the same operator. | A native cohomological trace cannot be pasted onto a Koopman generator. | Distributional trace equality with test class, convergence, non-orbit terms, clock, phase, and multiplicity. |
| `OP-WEIL-1` | Tie any Weil-form compression to the same arithmetic/operator ledger. | A post-hoc Hermitian form proves too much and does not certify Hilbert–Pólya. | Intrinsic form/compression whose trace, second moment, and inertia are read from the same prime-power data. |
| `OP-DIV-1` | Prove a global completed-ξ determinant equality. | Finite divisor agreement or a native finite-field determinant is a different target. | Defined determinant, multiplicities, growth, continuation, and zero-free prefactor, globally. |

## Current hard stops

1. A positive component reweighting of the Koopman circle sum is a unitary
   diagonal change and cannot remove its essential spectrum or multiplicity.
2. Deleting the infinite zero eigenspace does not help: every nonzero rational
   frequency also has infinite multiplicity.
3. Adding a finite-dimensional Frobenius block to $A_K$ leaves
   $\sigma_{\mathrm{ess}}(A_K)=\mathbb R$ and the noncompact resolvent intact.
4. The substitution $t=2^{-s}$ creates vertical preimage lattices; it does
   not create additional physical eigenvalues of Frobenius or Koopman time.
5. A genuinely new cohomological flow, anisotropic transfer space, coupling,
   or boundary condition is a new candidate and must restart T0--T7 and
   B1--B5 rather than inherit coordinatewise credits.

## Canonical next theorem

Construct a source-derived Hilbert or trace-space realization in which a
**single** closed operator carries the arithmetic return ledger and its exact
trace/determinant.  Prove its spectral type first; only then test rational-prime
weights, a Weil-form bridge, and a completed-ξ divisor.
