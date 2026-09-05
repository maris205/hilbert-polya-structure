# Paper plan — P204

Title: **Two-step dynamics and flagged fibres of previous-smaller distances**.
One-sentence contribution: On the full inversion-sequence box, recomputing
strict previous-smaller distances twice decodes exactly the original zero
and ascent sets, giving an explicit recurrent involution and every-target
fibre formula for both phases at all times at least two.

Type/format: anonymous, self-contained short mathematics note; no submission
venue selected and no external release authorized. Target length about four
pages in total, including title, abstract and references, at most five if
needed to keep the complete proofs readable. No
empirical ML benchmark, trained model, GPU experiment or decorative figure
is relevant. The ordinary conference defaults of the generic writing skills
do not replace this project's established short-note format.

## Claims/evidence and section plan

| Claim | Deductive evidence | Finite pressure, never the proof | Section |
|---|---|---|---|
| Literal closure and zero barriers | Author proof §1 | all $E_n$, $n\le8$ | 1–2 |
| First-image one-or-rise inequality | Previous-smaller index comparison, including ties | direct strict scans | 2 |
| Exact $P^2$ endpoint and core involution | Author proof §§2,4 | endpoint/core checks and independent graph walks | 2 |
| Sharp height in all boundary sizes | $002$ and zero-prepended $0122$ | graph depths | 2 |
| Fixed/recurrent/two-cycle census | Weighted two-state recurrence; isolated positive positions | exact complete core/graph enumeration | 2 |
| Every-target fibres for $t\ge2$ | Endpoint mask, decreasing segments, signed cut product | all targets at $t=2,3,4,5$; independent last-value DP | 3 |
| Static primitives are owned | Three verified primary references and candidate source gate | strict/weak tie and classical statistic adapter controls | 1,4 |

1. **The map and scope.** Define the factorial carrier and synchronous strict
   update; state the endpoint/fibre takeaway. Position strict nearest-smaller
   computation versus weak Cartesian parent-distance and classical inversion
   statistics. Two concrete contributions are temporal decoding and evaluated
   post-collapse fibres; the Fibonacci census is not a third novelty claim.
2. **Two-step decoding and recurrence.** Define local block indices carefully.
   Prove one-or-rise, the exact decoder, core surjectivity, recurrence and
   sharp tail. Derive the Fibonacci count with correct initial indices.
3. **Every target after two steps.** State the full signed cut formula before
   proving it; show noncore fibres vanish and the zero target has one source.
   Retain global upper bounds $r+j$, not just local block lengths. Include a
   short numerical two-letter block example to expose the global-flag issue.
4. **Verification and limitations.** Give the exact author test scope, separate
   deductive results from finite tests, and exclude $t=1$, first-image and
   maximum-fibre claims. Explain the classical descent/record interpretation
   and retain OWNER_AMBER/HOLD_EXTERNAL in the package.

All proofs stay in the main body. Files are modular (`sections/01_setup.tex`
through `04_scope.tex` plus `00_abstract.tex`); common notation is in
`math_commands.tex`. The abstract begins with the exact two-step result and
mentions the uniform height and all-$t\ge2$ scope. No one-page generic related
work filler is added to this four-page note. There is no comparable prior
numeric bound for this literal map to place in a misleading comparison table.
The sources are compared by their actual operation/statistic scope in prose.

## Citation plan and owner boundary

- Berkman–Schieber–Vishkin (1993): strict static nearest-smaller values.
- Park–Amir–Landau–Park (CPM 2019): weak parent-distance convention;
  the tie example $011$ distinguishes its one-shot literal from ours.
- Lin–Kim (JCTA 2018; checked author preprint 2016): classical ASC/DES and
  ZERO/record statistics, not ownership of the present iteration theorem.

Use publisher/institutional metadata and retrieved DOI BibTeX, not guessed
entries. Read limits and version differences go in `SOURCE_AUDIT.md`.
Internal P134/P185 map and mechanism subtraction is documented there without
making a public-priority or self-identifying external citation claim.

## Review status and skill adaptation

The process-separated candidate gate accepted only the contract above.
It is not outline or manuscript acceptance. The generic skills' old GPT-5.4
MCP endpoint is unavailable, and no external model/upload is authorized.
Current-model process-separated outline/draft review is used under the
project workflow, with actual feedback recorded when received. The required
two manuscript reviews are still pending; no placeholder PASS is issued.
Figures are omitted because the mathematical decoder and cut example are
more compact and fully explanatory. No source file existed to overwrite.

Actual outline review: `/root/batch197_fosp_gate` read this plan, narrative,
candidate gate and both canonical count records, without supplying a new
lemma or editing the manuscript. Its
[report](../../docs/papers204_208_sequence/outline_reviews/p204/OUTLINE_REVIEW.md)
is `GO_TO_DRAFT / NO_CHANGE_TO_MATHEMATICAL_SCOPE_OR_SECTION_ORDER`.
The sole production clarification, that the four-page target/five-page cap
includes all front matter and references, is implemented above. This is an
outline review only; formal A/B and PDF acceptance remain pending.
