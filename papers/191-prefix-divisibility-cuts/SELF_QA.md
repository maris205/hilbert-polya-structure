# P191 author handoff — Round 0

**Decision:** `PASS_INTERNAL / ROUND0_AUTHOR_FREEZE`  
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`

The author-side package contains complete proofs for all advertised totals, a
deterministic anonymous four-page artifact, and a 3,408,240-assertion exact
control.  It does not issue a hostile-review verdict and does not claim
process-separated error provenance.

## Mathematical boundary audit

- The carrier contains positive compositions only; the final endpoint `N` is
  not an internal cut and is never tested.
- Each epoch tests all old parts and endpoints before deleting its failing cuts
  simultaneously.
- Monotone cut containment proves that every recurrent state is fixed; finite
  enumeration is not used in that proof.
- The fixed recurrence gives `A(0)=1`, uses every divisor step into `v`, and
  then sums over the last internal cut `0<=v<N`, leaving the final part
  unconstrained.
- `N=1,2,3` are stated separately and all their compositions are fixed.
- The sharp-clock proof uses the permanently retained first cut and treats
  first/final placement of the unique part two in the equality case.
- The unique witness formula includes both `t=0` and the fixed endpoint
  `t=N-3`.
- In the global fibre recurrence, an edge cannot skip a target cut; each
  nonfinal vertex is required to divide exactly when it belongs to the target.
- The interval formula distinguishes internal target factors `K` from the
  untested final factor `K_*`; the one-part target is covered by the empty
  product.
- Every target, including empty fibres, is checked pointwise against literal
  indegree before image equality or fibre mass is used.

## Source and artifact audit

- the exact citation-key set equals the exact bibliography-key set: five keys
  each;
- all citation contexts are scope-aligned background or subtraction, and all
  five records have verified authoritative metadata;
- OEIS A398023 is explicitly distinguished as the static condition `i | s_i`,
  not the dynamic P191 condition `a_i | s_i`;
- the bounded owner non-hit is never called novelty, priority, or clearance;
- no placeholder, `[VERIFY]`, author identity, affiliation, grant identifier,
  or self-identifying repository link occurs in the manuscript;
- the final log and BibTeX transcript have no warning, bad box, error, or
  unresolved reference;
- the live and immutable Round-0 PDFs are byte-identical A4 files;
- all 28 font rows are embedded, subsetted, and Unicode mapped;
- all four final rasterized pages were inspected at original resolution.

This is internal theorem and artifact QA only.  It is not novelty, priority,
ownership clearance, freedom to operate, external-release authority, or an
independent review.  No external action is authorized.
