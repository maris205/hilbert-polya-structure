# Paper configuration

## Identity

- **Paper ID:** `normalized-algebraic-action-prime-log-certificate-v1`
- **Title:** *Normalized Algebraic Periodic Actions versus Prime Logarithms:
  A Hénon Design Certificate*
- **Author mode:** anonymous finalized local manuscript
- **Article type:** specialist mathematical-dynamics note; theorem plus
  source-locked static implementation audit
- **Format:** 11 pt `article`, one-inch margins, author--year citations
- **Pre-review date:** 2026-08-14
- **Round-1 revision date:** 2026-08-14
- **Finalization date:** 2026-08-14
- **Revision status:** `COMPLETE_LOCAL / FINAL_REVIEW_PASS`; both required
  scientific/provenance repairs and all five Round-1 minor items independently
  verified in Round 2
- **Compiled length:** 13 pages including references and appendices; the
  conclusion ends on page 10

## Central claim configuration

The paper may claim the following and no stronger conclusion:

1. regular finite evaluation of a frozen single-valued
   `Qbar`-rational exact potential on an algebraic periodic orbit gives an
   algebraic one-traversal action at every finite period;
2. Hermite--Lindemann excludes equality of that action with every logarithm
   branch of a nontrivial algebraic number, including positive `log(p)`;
3. algebraic scales, averages, repetitions, real and imaginary parts, and
   modulus retain the direct exclusion, but `log|A|` does not;
4. a stepwise algebraic exact gauge changes the action by the full general
   endpoint expression `chi_n(P_n)-chi_0(P_0)+sum_j C_j`;
5. the identity-map constant-potential control shows that transcendental
   normalization invalidates any map-only arithmetic conclusion;
6. for `H_a(q,p)=(q^2-a-p,q)`, the exact potential
   `G=2q^3/3-pq` and type-1 generating function have opposite signs on the
   graph, every finite periodic point is algebraic, and only `3*A_G` is
   generally certified S-integral;
7. the static outputs audit the implementation and do not prove the
   all-period theorem.

## Mandatory scope language

- The paper is **not** a universal no-go theorem for symplectic or arithmetic
  dynamics.
- It does not exclude `log|A|`, `arg(A)`, multiplier, return-time,
  infinite-place, or adelic clocks.
- It does not exclude multivalued potentials, closed non-exact primitive
  changes, or target-independent transcendental normalizations; each needs a
  new provenance ledger.
- It makes no claim about approximate equality or quantitative separation.
- It does not claim that `A_G` itself is S-integral at places above 3.
- It makes no prime--orbit, zero-data, trace-formula, zeta, determinant,
  compactness, or quantization claim.
- It makes no historical-first claim.

## Evidence policy

| Evidence class | Permitted role |
|---|---|
| Main mathematical proof | All-period algebraicity, logarithmic exclusion, gauge formula, Hénon specialization, and S-integral refinement |
| R020--R023 exact symbolic outputs | Formula and proof-implementation audits only |
| Gauge and target controls | Assumption, endpoint, edge-case, and stop-rule checks |
| Sharp `-1/3` control | Denominator-three boundary |
| JUnit and final manifest | Software and provenance integrity only |

No candidate parameter may be substituted, no candidate periodic point or
candidate action may be computed, and no prime table or Riemann-zero data may
enter the paper package.

## Route configuration

- **Plan decision:** `GO_AS_NARROW_DESIGN_CERTIFICATE`
- **Closed route:**
  `CLOSE_ONLY_THE_NORMALIZED_ALGEBRAIC_ACTION_AS_EXACT_PRIME_LOG_CLOCK`
- **Publication boundary:** `MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED`

## Bibliography policy

Only the 13 records in `references.bib` are cited.  DOI/arXiv and publisher
metadata checks, including the collective author of the 2024 Hénon survey and
the Baker/Masser book-credit correction, are recorded in
`../notes/PAPER_CITATION_AUDIT.md`.  Citations provide context or identify the
classical transcendence input; none substitutes for a paper-specific proof.

## Figure policy

- Regenerate all three figures with
  `python paper/figures/generate_all.py`.
- PDF and SVG are vector masters; PNG is a review rendering.
- The loader refuses a changed source lock, incomplete registry, failed
  proof/control/isolation audit, opened candidate gate, or prime/zero access.
- Figure 2 derives every displayed cell through an explicit ledger that marks
  it either `FROZEN_JSON_DERIVED` or `THEOREM_DEFINED`; the latter is never
  described as a raw computational result.  The 27-cell provenance record is
  `figures/fig2_scope_matrix_provenance.json`.
- Fixed metadata and an SVG hash salt make all nine visual outputs and the
  scope-provenance record byte reproducible.

## Build policy

Run `paper/build.sh`.  It fixes `SOURCE_DATE_EPOCH`, runs BibTeX, and performs
four LaTeX passes.  A valid build has no errors, warnings, overfull/underfull
boxes, undefined citations or references; all fonts are embedded/subset; all
13 pages are visually clean; and a consecutive clean rebuild has the same
SHA-256.
`paper_pre_review.pdf` is the immutable snapshot handed to the Round-1
reviewer.  `paper_round1_revision.pdf` is the author-revised snapshot for a
fresh independent Round 2.  `paper_final.pdf` is the terminal local artifact
and is byte-identical to that independently approved revision.

## Pipeline boundary

Round 1 returned `MINOR_REVISION`; its two required and five minor items were
implemented.  Fresh independent Round 2 returned `PASS — MAY FINALIZE` with
no residual blocking issue.  The local paper and final-integrity stages are
complete.  Repository synchronization remains deferred to the five-paper
batch close under the Session rules.
