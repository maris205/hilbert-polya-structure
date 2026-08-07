# HCS-C18 breadth-first candidate report

## Search rule

HCS-C17 closed only a final-monodromy-denominator clock.  This round did not
assume that endpoints or multiple cusps repair it.  Candidates were ranked by
structural distance from existing obstructions, source-derived arithmetic,
preservation of genuine chronology, cheap exact falsifiers, and the chance of
a theorem-sized conclusion.

## Candidate screen

Scores are qualitative pre-experiment scores out of ten.

| Candidate | arithmetic | intrinsic dynamics | exact test | plausible delta | principal risk |
|---|---:|---:|---:|---:|---|
| Endpoint action groupoid and projective cocycle | 9 | 9 | 10 | 8 | cusp restriction may be a coboundary; full-boundary trace may be Selberg |
| H\'enon Frobenius--iterate two-axis counts \(N_p(r,n)\) | 9 | 9 | 6 | 9 | extension-field cost and no canonical bivariate Euler law |
| Noncompact \(S\)-arithmetic boundary groupoid | 10 | 8 | 4 | 9 | scalarization may be the old Weil height |
| Squarefree \(\Gamma_0(N)\) multi-cusp scattering | 10 | 7 | 10 | 7 | classical Atkin--Lehner/Huxley factorization |
| Congruence-coset Gauss transfer with Hecke cocycle | 9 | 9 | 7 | 8 | established congruence transfer-operator theory |
| Bianchi class-group cusp channels | 9 | 7 | 5 | 7 | class-group Fourier transform gives Hecke \(L\)-ratios |
| Nonamenable congruence transfer towers | 8 | 9 | 5 | 8 | large existing expander/resonance-gap literature |
| Parabolic H\'enon inducing at \(a=3\) | 5 | 9 | 5 | 7 | section dependence and elliptic islands |
| Fibonacci physical-time composition determinant | 7 | 8 | 7 | 6 | may be another renormalization-clock relabeling |
| H\'enon derivative-representation ladder | 5 | 9 | 9 | 5 | two-dimensional symplectic characters may factor algebraically |
| Equivariant dihedral period tower | 5 | 8 | 7 | 5 | no canonical cross-period induction maps |

## Automatic selection and refinement

The endpoint action groupoid ranked first because it directly changes the
type of the HCS-C17 object and admits an exact, no-fit kill gate.  The first
derivation proved that the cusp-only cocycle is globally gauge-trivial and
that nonzero full-boundary periods are Selberg lengths.  Rather than continue
small endpoint variations, the round then activated the independent
multi-cusp escape in the same trace-closure question.

For squarefree \(\Gamma_0(N)\), the classical tensor formula gives a second
exact gate: all standard scattering matrices lie in one commutative
Atkin--Lehner algebra.  The route was retained because this closes the other
explicit HCS-C17 escape with a theorem, not because the tensor factorization
itself is new.

## Frozen research question

> Can the modular open-scattering arithmetic remain genuinely open and
> chronological after an ordinary trace/Fredholm closure if one retains
> rational endpoints or all squarefree congruence cusp channels?

The answer is no for the rational ordinary-loop clock.  For the bare
squarefree product it is no only conditionally on using spectral-parameter
matrices as successive factors; scattering theory does not supply that time
interpretation.  Off-diagonal open series and projector-resolved path
amplitudes remain nontrivial positive controls, so the conclusion is not a
universal no-go for open kernels.

## Kill criteria met

- the displayed rational endpoint cocycle is an algebraic coboundary in a
  primitive integral gauge, with no analytic conjugacy claim;
- positive reversal-invariant sojourn time cannot be a real additive groupoid
  cocycle;
- the first nonzero action-groupoid loops are hyperbolic and carry exactly
  signed Selberg length;
- the squarefree scattering family has an \(s\)-independent eigenbasis;
- frozen bare spectral-parameter products are permutation-invariant;
- every eigenchannel retains the same shifted completed-zeta quotient divisor.

## Positive branch retained, not promoted

Rank-one endpoint projectors between scattering matrices can distinguish
parameter-to-edge assignments and endpoint paths.  Promotion would require a source-derived path
composition law, primitive/repetition semantics, nuclear operator, and global
divisor.  None is inferred from a finite projected-amplitude witness.

The next major system switch should therefore test the H\'enon
Frobenius--iterate two-axis object, not another small congruence level.
