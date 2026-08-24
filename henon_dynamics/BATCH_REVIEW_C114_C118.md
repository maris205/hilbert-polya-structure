# Batch review: HCS-C114--HCS-C118

Date: 2026-08-24

System family: Route-A dynamics variants under the frozen scope firewall
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **continue exploratory Route A; keep Route B unauthorized**.

## Completed paper outputs

1. **C114 -- local jet Koopman operator.**  The order-four local algebra has
   dimension 15.  Its pullback has trace \(129/16\), determinant \(2^{-20}\),
   five exact graded blocks, and a strictly degree-raising nonlinear part of
   nilpotency index four.  This is the strongest operator-first result of the
   round, but it is only a finite local quotient at one fixed point.
2. **C115 -- rational McMillan/QRT dynamics.**  The invariant, inverse,
   reversor, determinant-one identity, three valid complex fixed points, and
   one real primitive two-cycle are exact.  The two cleared-denominator roots
   at \(x=\pm i\) are forward poles and are explicitly rejected.  The local
   polynomial \(\det(I-zP_2)=(1+z)^2\) is not called a transfer determinant.
3. **C116 -- Lozi nonsmooth pruning.**  All 510 rooted binary words through
   length eight are tested with exact branch inequalities.  The rooted strict
   counts are \((2,4,2,8,22,40,58,128)\), producing 37 primitive necklaces
   and a 240-state/240-edge finite cycle atlas.  The result is explicitly
   bounded to powers at most eight.
4. **C117 -- Markov-switching tangent moments.**  The source convention
   (old environment \(i\) to new environment \(j\), then apply \(F_j\)) is
   frozen.  Exact conditional first- and second-moment operators have
   dimensions 4 and 6.  Their determinant-polynomial coefficients and a
   rank-one stationary average-versus-square gap are independently recovered.
5. **C118 -- damped conformally symplectic dimer.**  The map satisfies
   \(J^T\Omega J=\Omega/2\), \(\det J=1/4\), an exact inverse, and an exact
   one-form identity.  A synchronous primitive two-cycle splits into
   longitudinal and transverse two-step factors with traces \(-59/4\) and
   \(-13\); an uncoupled control isolates the trace shift \(7/4\).  Tangent
   monodromy is not promoted to an A2 transfer owner.

## Uniform release audit

All five packages pass their deterministic producer, checker that does not
import the producer, independent SymPy reconstruction, canonical replay, and
hostile mutation suite.  Mutation rejection totals are 13/13, 12/12, 12/12,
12/12, and 12/12.  Each content-addressed manifest closes at 26/26 files with
matching evidence and PDF hashes.

For every paper, two fresh fixed-date isolated LaTeX builds are byte-identical
to one another and to the checked-in PDF.  All five PDFs have two pages, all
fonts are embedded, and the final logs contain no LaTeX/package warning,
overfull or underfull box, undefined reference, multiply-defined label, or
citation warning.  A rendered ten-page contact audit found no clipping,
truncation, or visibly broken formula/table layout.

## Integrity and failure-mode audit

- **Implementation bugs as discoveries:** mitigated by independently written
  validators, exact symbolic reconstruction, canonical evidence replay, and
  hostile mutations that alter both conclusions and boundary fields.
- **Hallucinated or irreproducible results:** mitigated by rational arithmetic,
  deterministic JSON receipts, matching content hashes, and isolated builds;
  no numerical tolerance or random seed is needed.
- **Pipeline frame lock:** mitigated by five materially different systems
  (local polynomial jet, birational reversible, nonsmooth piecewise-linear,
  stochastic switching, and damped coupled variational dynamics).
- **Shortcut-to-global-theorem risk:** finite prefixes and local monodromies
  are labelled with maximum order, local quotient, or low-period scope.  No
  complete coding, compactness/nuclearity, or Fredholm ownership is inferred.
- **Methodology or review fabrication:** no external reviewer, acceptance
  score, literature novelty result, or citation is claimed.  Improvement logs
  distinguish internal prose passes from preserved release snapshots.
- **Forbidden arithmetic promotion:** Euler factors, root numbers, automorphy,
  Hilbert--P\'olya, and Route B occur only in nonclaim/firewall statements.

## Route-A assessment

The strongest global tuple remains

```text
(A0_NOT_ADDRESSED, A1_WEAK, A2_CERTIFIED_PREFIX,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

C114 demonstrates that an operator-first finite local quotient can be fully
owned and audited; C116 supplies the widest new exact orbit prefix.  Neither
is yet a source-native global analytic operator with a proved trace identity
or compactness/nuclearity estimate.  C115 and C118 intentionally fail A2,
while C117 certifies only finite tangent moments.  The correct overall status
therefore remains `ROUTE_A_EXPLORATORY`.

## Next gate

Continue the user's diversity strategy, but require at least one C119--C123
candidate to connect a source-defined global function space, an explicitly
defined action, and a proved trace law.  Coefficient matching alone cannot
advance A2, and no arithmetic or Route-B work is authorized by this round.
