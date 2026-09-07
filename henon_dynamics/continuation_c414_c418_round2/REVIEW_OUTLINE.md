# Independent review of the C414–C418 manuscript outline

Reviewer: `scout_henon_arithmetic`, current-team nonauthor of
`BATCH_PLAN.md` and `ADMISSION_DECISIONS.md`, both authored by root.
The reviewer authored the cubic research package; this review is **not**
a new independent mathematical review of that package or an admission
self-review. The coordinator's separate cubic proof/source review is
the admission evidence.

Initial verdict: **ONE MINOR PRECISION FIX REQUIRED; NO SUBSTANTIVE
OUTLINE BLOCKER**. The single required wording correction is R1 below.
It requires no new theorem, experiment, full proof review or code run.
The five-paper selection, section plans and release gates otherwise pass.

## Scope and inputs actually read

Read completely: the 211-line batch plan and 127-line continuation
admission decisions. Also read the complete `paper-plan` skill and its
shared writing-principles reference for claim/evidence alignment,
front-loaded scope and complete mathematical exposition. The plan's
standalone anonymous article format and current-team review override
legacy external-model and ICLR examples. No journal was selected, so
there is no venue-specific page-limit or formatting gate to impose.

For exact scope comparison, read the theorem/assumption heads of the
height, full-degree-$2p$, discrete-sine and function-field proof packages;
the cubic theorem's seven templates and all-family quantifiers were
already read in full as its author. Also checked the degree-$2p$
analytic consequence's primitive-root-order restriction, the current
cubic review's admission status, and the function-field review's
affected-revision closure. This was bounded outline verification, not
a new audit of every underlying proof step.

The two continuation proof hashes and the function-field closure hash
match the admission document exactly:

| Input | SHA256 |
|---|---|
| Cubic proof | `d7288267e81a6389f1e71e4999cdc3c1056b754bb22a816b050253422e1f753f` |
| Function-field proof | `a5f10ff4354adb0fa86ffdf6868b9f7c7658e2e95116a62d20142c0308be6ccb` |
| Function-field affected closure | `0880b910fade20f089a2fc710b115d6378d7c17c1a96e4388a17359792bf736c` |

No producer script, reviewer script, sealed diagnostic or PDF build was
run for this outline review. No author source, global state, evaluation,
Git record or frozen research file was edited. This review file is the
only output of the assignment.

## R1 — preserve the two different uniqueness statements

Location: C418 claims–evidence matrix, first row. The initial wording
was “$c=-P^2+C$ uniquely.” The actual theorem and admission record say
that $C$ is unique and $P$ is unique **up to sign**. Without this
qualification the row could be transcribed as uniqueness of $P$ itself.

Required minimum fix: replace the phrase by “$C$ is unique and $P$ is
unique up to sign,” or an equivalent explicit statement. Do not alter
the family, reconstruction rule, proof or already closed review.

Severity: minor mathematical precision. This does not challenge the
theorem or the admission judgment. The affected outline sentence is
the only item requiring recheck before drafting.

## Five separate questions and their evidence

| Paper | Question actually planned | Scope and independence assessment |
|---|---|---|
| C414 | The exact distribution of forward-plus-backward canonical height for all polynomial points of a constant-coefficient finite-field Hénon map | Preserves every prime power, degree at least two, nonzero determinant and unrestricted degree-$d$ polynomial. This is a height Dirichlet series, not ordinary periodic counting. Full pole aggregation, lattice oscillation and the meromorphic boundary have identified proof locations. |
| C415 | The full degree-$2p$ correction family for ordinary geometric fixed points of $H^{-1}\Phi_q$ | Preserves odd $p$, $q=p^e$, $e\ge3$, leading correction coefficient and determinant nonzero, and all lower coefficients. The high/low support partition, mixed perfected tail, semilinearity and descent are explicitly allocated. The inherited analytic consequence is not an extra contract. |
| C416 | Every ordinary rational cycle in the exact discrete-sine polynomial family at all odd degrees | Preserves the exact rational-coefficient integer-valued family, all $\mathbb Q^2$, small radii, signed lifting and no orientation quotient. Bulk clipping, central exceptions, boundary routes and the growing cycle are proof obligations, not just census totals. |
| C417 | Every rational cycle and total coexistence for all monic integral conservative cubics | Preserves all three integer coefficients and the full rational domain. The global secant argument, ninety symbolic cases, proved finite complement, seven templates and unique eleven-point equality locus form one complete question. It does not reuse the nonmonic discrete-sine cubic as its new example. |
| C418 | The entire rational periodic locus for nonconstant polynomial quadratic parameters over arbitrary fields of characteristic not two, with arbitrary nonzero constant determinant | Preserves $k(t)^2$, no perfection/algebraic-closure restriction, the determinant convention, sign-injective reconstruction, all-field graph cases and characteristic-three exceptions. This is not C417 over a renamed coefficient field: the parameter is nonconstant and the branch/offset rigidity and determinant exceptions are different. R1 only clarifies normalization uniqueness. |

Each question has a one-sentence contribution and a claims–evidence
matrix leading into its section plan. Shared integrality or finite-state
tools do not by themselves create extra contracts; the plans deduct
them and identify the separate full-family closure. Prior independent
admission decisions, not this outline review, establish the substantive
research gate.

## Proof placement, sources and artifacts

The shared plan requires full proofs in the article body or an included,
typeset appendix. It does not allow an external proof note, a code link,
a screenshot or a numerical plot to substitute for those proofs.
The paper-specific plans retain the needed proof material:

- C414: disjoint valley forms, exact multiplicities, combined residues,
  every pole and a direct oscillatory counting argument.
- C415: the ordinary/scheme distinction and conversion, both support
  branches, fractional degree estimates, semilinearity and descent;
  the primitive positive $p$-power root restriction is not dropped.
- C416: actual clipped cells, phase labels, signed boundary routing,
  endpoints, no-alias proof and growing-cycle closure, not just totals.
- C417: the finite input ranges, complete exact algorithm and tables,
  short-word interpolation and the full equality locus; the false
  global-three-symbol shortcut is expressly excluded.
- C418: the eight-state edge table, seven-type all-field atlas, sign
  lifts, all overlaps and an explicit common reconstruction for the
  fourteen characteristic-three points.

The cited proof/review paths checked here resolve. Root identified and
corrected the C416 script filename from `bulk_symbolic.py` to
`symbolic_bulk.py` during this review; the corrected source exists in
the old `nonlinear_geometry/` directory. This filename correction
does not require a new execution of that frozen certificate.

Source instructions preserve actual access/version limits and deduct
the relevant predecessors. C412 is identified as a repository result,
not silently upgraded to a journal publication. The plan does not
invent bibliographic entries or assert a global-priority search.
The historical author-status headers in frozen proof packages are
not current admission decisions: the current plan correctly relies
on closed nonauthor reviews and the continuation admission record.

## Five-paper limit and downstream gate separation

The outline contains exactly C414–C418. The positive-word reserve,
independent-clock companion and rejected forward-characteristic
scouts remain outside the manuscript list. Native finite-cycle zetas
in C416–C418 are corollaries of their existing questions, not sixth
papers. C419, Route B and external journal submission are not opened.

Admission, a proof PASS, outline approval, manuscript completeness,
strict pinned Route A evaluation, nonauthor manuscript review,
deterministic double-build equality and every-page visual inspection
are kept separate. The plan requires actual TeX/Bib/PDF review and
affected fixes rather than treating an old proof certificate as a
new manuscript review. It also specifies fresh deterministic builds
and exact release sealing without claiming these have happened.

No source counting exponent, exact zeta or successful build is promoted
to target Euler factors, root numbers, automorphy, target zero/divisor
correspondence or Hilbert–Pólya realization.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

## Closing condition

Once R1 is corrected and that exact sentence is checked, this outline
can be marked **PASS / CLOSED** without reopening the mathematical
reviews. No other required change was found. This conclusion authorizes
only the next manuscript stage under the existing batch plan; it does
not certify any unwritten manuscript, unbuilt PDF or unrun evaluation.

## Affected-revision closure — PASS / CLOSED

The reviewer checked only the two affected outline entries, without
rerunning any proof, certificate, experiment, script or build:

1. C418, claims–evidence matrix, line 168 now says that
   $c=-P^2+C$ has unique $C$ and $P$ unique up to sign. This states the
   two normalization claims correctly. **R1 is CLOSED.**
2. C416, claims–evidence matrix, line 108 now cites
   `symbolic_bulk.py`; the corrected file exists at
   `henon_dynamics/research_c414_c418/nonlinear_geometry/symbolic_bulk.py`.
   No stale `bulk_symbolic.py` reference remains in the batch plan.
   **The filename correction is CLOSED.**

The initial conditional verdict above is superseded by **PASS / CLOSED**
for the five-paper outline. No other required outline correction was
identified in the original bounded review. The accepted inputs are:

| Input | SHA256 at closure |
|---|---|
| `BATCH_PLAN.md` | `dbe8f70b0ee4a31927e1213a196b69025e527dd78452eabd49d8230dc7905f46` |
| `ADMISSION_DECISIONS.md` | `e0339476713a395b6c63bf7482211774016c22634c9d94b45f93c1d8376dc23c` |

Only this review file was changed by the reviewer. Underlying admission
and mathematical reviews remain closed and were not rerun. Manuscript
drafting remains subject to the coordinator's `OUTLINE_FROZEN` handoff;
this closure does not certify any manuscript, PDF or evaluation.
