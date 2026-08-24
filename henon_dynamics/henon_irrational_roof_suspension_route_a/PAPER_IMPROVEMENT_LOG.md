# C130 paper improvement log

## Method

The compact certificate was reviewed and revised twice after the baseline PDF
compiled.  Reviews were adversarial and claim-focused: theorem scope,
convergence, counterexamples, and Route-A boundaries were checked against the
exact receipt before each edit.  No unsupported experiment or citation was
added.

## Score progression

| Version | Technical-readiness score | Verdict | Retained PDF |
|---|---:|---|---|
| round 0 | 7.0/10 | mathematically promising, boundary underexplained | `paper/main_round0_original.pdf` |
| round 1 | 8.5/10 | core identity rigorous, one requested consequence still implicit | `paper/main_round1.pdf` |
| round 2 | 9.5/10 | compact certificate ready within its strict scope | `paper/main_round2.pdf` |

## Round 1 raw review

> **Score: 7.0/10. Verdict: Almost.**
>
> **Summary.** The draft freezes a clean two-state suspension and reaches the
> requested bivariate and exponential-polynomial determinants.  The
> primitive-root decomposition is correct, and the same-sector period-six
> example prevents an orbit-injectivity overclaim.  The main weakness is that
> the analytic status of the infinite product is described only as “in a
> right half-plane,” whereas the explicit determinant is called entire.
>
> **Strengths.** (1) The matrix calculation is transparent and all-period.
> (2) The rational control changes only the roof.  (3) The strict Route-A
> tuple and arithmetic firewall are visible in the PDF.
>
> **MAJOR 1 — convergence boundary, Section 2.** Name the abscissa `h` by
> `e^-h+e^-sqrt(2)h=1` and state absolute convergence for `Re(s)>h`.
>
> **MAJOR 2 — formal versus analytic identity, Section 2.** Put the trace-log
> formula in the paper, explain why primitive regrouping is absolutely
> convergent there, and state separately that the bivariate product is valid
> in the total-degree completion.  Explicitly deny global convergence of the
> primitive product.
>
> **MINOR — continuation wording.** Say that the explicit exponential
> polynomial is entire and its reciprocal is meromorphic; do not attribute
> global continuation to the raw product.

### Round 1 fixes

1. Added the trace-log identity and absolute primitive-root regrouping.
2. Defined `h` exactly and stated `Re(s)>h` as the convergence domain.
3. Distinguished formal total-degree identity, analytic half-plane product,
   and entire continuation of the explicit determinant.
4. Preserved two pages and a warning-free build.

## Round 2 raw review

> **Score: 8.5/10. Verdict: Almost.**
>
> **Summary.** The convergence and continuation boundary is now precise, and
> the all-period primitive identity is self-contained.  The paper proves
> count-sector injectivity and gives a within-sector collision, but the task's
> stronger clock consequence—absence of a nonzero imaginary period—appears in
> the evidence and theorem package rather than in the PDF itself.
>
> **Strengths.** (1) No theorem cutoff is confused with the period-10 replay.
> (2) Sector separation is not inflated into orbit separation.  (3) The
> rational control exhibits both a concrete collision and a lattice
> polynomial.
>
> **MAJOR — imaginary-period proof, Section 3.** Add the two-coefficient
> argument: a period `iT` forces both `e^-iT=1` and
> `e^-i sqrt(2)T=1`, hence `T=0`.
>
> **MINOR 1 — control isolation.** Repeat immediately before the control that
> only the roof is changed.
>
> **MINOR 2 — validation ownership.** Put the independent checker and SymPy
> check counts in the PDF and identify the hostile suite as repaired-hash.

### Round 2 fixes

1. Added the no-nonzero-imaginary-period statement and proof.
2. Made the roof-only nature of the rational control explicit.
3. Added independent-checker, SymPy, and repaired/stale-hash totals to the
   paper; the final release-hardening counts are recorded below.
4. Recompiled and verified that `main.pdf` is byte-identical to
   `main_round2.pdf`.

## Release-hardening audit after Round 2

- Closed the exact key schemas for the source lock, all-period identity,
  clock-sector statement, progress headline, and Route-A block.
- Added exact checks for the frozen clock and determinant convention, both
  trace headlines, sector injectivity, overall verdict, and progress boundary.
- Expanded the final checker to 139 assertions.
- Expanded the hostile suite to 43 repaired-hash semantic forgeries plus one
  stale-hash case, for 44/44 rejected mutations.
- Moved the evaluator receipt to the v0.1.0 accumulation path and completed
  the missing A2--A4 metric maps.

## Final format review

The final paper has two A4 pages.  Fixed-epoch isolated builds A and B match
the retained PDF byte-for-byte.  All fonts are embedded.  The final log has no
LaTeX/package warning, overfull or underfull box, undefined reference,
undefined citation, multiply-defined label, or badness report.  Both rendered
pages were visually inspected and contain no clipping, collision, truncation,
or broken equation/table layout.

## Remaining limitations (deliberately retained)

- Different primitive necklaces can share one population vector.
- The primitive product converges initially only for `Re(s)>h`; the entire
  object is the explicit determinant, not a globally convergent raw product.
- No target divisor or arithmetic/global analytic structure is compared.
- No natural self-adjoint or quantum lift is constructed.
