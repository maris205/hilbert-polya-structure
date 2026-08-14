# Experiment Report — SD-C29

## Outcome

The exact suite supports

    (A0_ANALYTIC_ARITHMETIC_ORIGIN,
     A1_PASS_ANALYTIC,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

with ROUTE_A_REJECTED, Route B locked, and no target-zero data. The positive
result closes the endogenous-selector obligation: covers of \(1\) in the fixed
integer divisibility source compile to exact all-repetition atom loops without
a prime/color projector table. The negative result is equally exact: every
finite compiler is zeta-conjugate to coordinate projectors, and the canonical
countable realization is boundedly similar to them for \(\eta>1\).

## Raw exact data table

| Artifact | Rows | Exact result |
|---|---:|---|
| incidence inverse | 4 | both inverse orders pass |
| primitive idempotents | 30 | ranks, traces, formulas, similarities pass |
| pair relations | 900 | 900/900 pass |
| cover atoms | 256 | 256/256 evaluator agreements |
| cyclic necklaces | 1016 | 1016/1016 selector agreements |
| digit markers | 80 | 80/80 exponents equal \(r\ell(p)\) |
| power traces | 8 | 8/8 exact atom sums |
| Fredholm/de Rham | 4 | 4/4 exact products or ratios |
| weighted Hilbert | 24 | all theorem formulas and bounds certified |
| bounded similarity | 3 | all \(\eta>1\) certificates pass |
| source mutation | 2 | promoted \(6\) is selected |
| cutoff/relabeling | 30 | 30/30 exact |
| ablations | 13 | decisive failures occur as frozen |
| analysis comparison | 9 | zero claim-bearing failures |
| regression tests | 61 | 61/61 PASS |

These are deterministic exhaustive rows or exact theorem certificates. Means,
standard deviations, stochastic-seed comparisons, and ML performance deltas
do not apply. The machine-readable raw comparison table is
results/analysis_comparison_table.csv.

## Incidence compiler

For a divisibility downset, the core computes the relation-derived incidence
inverse and forms

\[
q_n=Z E_n\mu.
\]

All four two-sided inverse rows pass. Each of the thirty \(q_n\)'s has rank
one, trace one, and the exact kernel

\[
q_n(a,b)=\mathbf 1_{a\mid n\mid b}\mu(b/n).
\]

All 900 pair products satisfy

\[
q_nq_m=\delta_{nm}q_n,
\qquad
\sum_{n\le30}q_n=I.
\]

Every source-derived atom idempotent in the cutoff is oblique rather than
self-adjoint. Nevertheless, the displayed formula already gives an explicit
similarity to the coordinate idempotent \(E_n\).

## Source-derived atoms and necklaces

The candidate core identifies atoms only as covers of the bottom source
element. All 256 classifications agree with a separated post-freeze
trial-division evaluator, with no prime table in the candidate.

For the first four derived atoms, the numbers of cyclic classes and selected
classes are:

| length | all cyclic classes | selected |
|---:|---:|---:|
| 1 | 4 | 4 |
| 2 | 10 | 4 |
| 3 | 24 | 4 |
| 4 | 70 | 4 |
| 5 | 208 | 4 |
| 6 | 700 | 4 |

At every length, exactly the four monochromatic repetitions survive. A source
letter \(p^r\) is a composite and is killed; the temporal word
\(p,p,\ldots,p\) is the \(r\)-fold traversal of the primitive atom loop and
survives. All eighty digit rows retain \(u^{r\ell(p)}\).

## Honest determinants

At the exact rational check point

\[
(s,u,z)=(2,1/2,1/3),
\]

the finite incidence determinant equals the product of its atom factors, and
all eight power traces equal the corresponding atom sums. The finite
gamma-branch de Rham matrices satisfy the chain identity and every local
supertrace identity. Their two ordinary determinants are computed separately,
and their graded ratio is exactly

\[
\frac{\det(I-z\mathcal T_0)}{\det(I-z\mathcal T_1)}
=\prod_p(1-zu^{\ell(p)}p^{-s}).
\]

The ratio is not called an ordinary determinant of an ungraded direct sum.

## Weighted Hilbert realization and similarity ceiling

For \(\eta>1/2\), every source atom has the rank-one realization

\[
q_px=\left(\sum_{k\ge1}\mu(k)x_{pk}\right)(e_1+e_p)
\]

and trace norm

\[
\|q_p\|_1=
\sqrt{(1+p^{-2\eta})\,\frac{\zeta(2\eta)}{\zeta(4\eta)}}.
\]

All twenty-four displayed norm rows lie below the uniform theorem bound.
For \(\eta>1\), the zeta and Möbius operator series converge absolutely and
are inverse, so

\[
q_p=Z_\eta E_pZ_\eta^{-1}.
\]

All three bounded-similarity rows and every finite similarity identity pass.
Thus non-normality exists, but ordinary cyclic traces and determinants cannot
observe it.

## Falsification controls

The exact controls prevent three false interpretations:

1. Promoting \(6\) to a cover of \(1\) makes the compiler select \(6\).
   Therefore it faithfully compiles its source but has no independent
   primality oracle.
2. Scalar Möbius is not the atom predicate: \(\mu(2)=-1\) is not an idempotent
   coefficient and \(\mu(6)=1\) accepts a squarefree composite.
3. Zeta without the Möbius inverse loses cross-orthogonality, while the
   unfiltered two-sided compiler gives trace one to the composite coordinate
   \(4\).

Downset restriction and deterministic source relabeling are exact in all
thirty stability rows. These controls verify implementation correctness while
also exposing the PROVES_TOO_MUCH boundary.

## Key findings

1. **Observation:** 900 pair products and 30 primitive rows pass exactly.
   **Interpretation:** incidence Möbius inversion creates an oblique complete
   primitive family. **Implication:** the finite cyclic observable is a
   coordinate projector table under unitriangular similarity.
2. **Observation:** 256 source labels and 1016 necklace classes pass with no
   classification error. **Interpretation:** atom selection is endogenous and
   precedes cyclic trace. **Implication:** A1_PASS_ANALYTIC is earned.
3. **Observation:** all four determinant rows equal their atom products.
   **Interpretation:** de Rham grading removes stability denominators but not
   incidence similarity. **Implication:** A2 is honest yet scoped.
4. **Observation:** every derived atom projector is oblique, while all
   \(\eta>1\) similarity certificates pass. **Interpretation:** only adjoint
   mixed-Gram geometry remains invisible to ordinary traces. **Implication:**
   repeating an ordinary determinant construction cannot advance the route.
5. **Observation:** the mutated source selects \(6\), and 7 of 11 scalar
   Möbius rows disagree with the atom coefficient. **Interpretation:** cover
   structure, not scalar Möbius values, owns selectivity. **Implication:** every
   follow-up needs diagonal and mutated-source controls.

## Suggested next experiment

Paper28 should freeze the same \(q_p\)'s and test one chiral/adjoint completion:
compute \(q_p^*q_q\), follow its real \(t\)-motion, determine a common Schatten
strip for \(T,T^*,T^*T,TT^*\), and attempt at most one canonical
source-derived regularization. The digit marker, all repetitions, diagonal
control, and mutated-source control remain mandatory. If the singular spectrum
reduces to generic rank-one Gram data or the relative determinant depends on a
chosen reference, stop the incidence route.

## Reproducibility and scope

The canonical runner starts from a fresh paper-local results directory, runs
generator, 61 tests, and analyzer twice under PYTHONHASHSEED=0, compares every
code/generated-result hash, rejects CRLF CSVs and local caches, audits the
strict two-stage pending provenance, and freezes a SHA-256 ledger. It performs
no Git operation.

No analytic continuation, functional equation, critical-line carrier,
target-zero comparison, self-adjoint RH operator, or RH implication is claimed.
