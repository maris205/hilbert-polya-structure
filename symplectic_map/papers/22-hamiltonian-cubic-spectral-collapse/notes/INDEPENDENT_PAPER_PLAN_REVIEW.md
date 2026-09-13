# Paper 22 — Independent Paper-Plan Review

## Reviewer identity, scope, and independence

Review date: 2026-08-24 UTC.

I am the fresh independent R2 paper-plan reviewer for Paper 22. In this role I
am distinct from the source-design author, the source-lock author, the
source-design and source-lock reviewers, the two candidate reviewers, the R0
failed-plan author/history, the R1 blocked-plan history, and the R2 repair
author whose stable plan bytes are under review.

This review used no network access, no CAS or symbolic package, no scientific
run, no TeX/Bib/PDF workflow, no manuscript action, no publication-lock
action, no Paper 23 action, and no external effect. I read to EOF:

- `papers/22-hamiltonian-cubic-spectral-collapse/paper/PAPER_PLAN.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/PROOF_PACKAGE.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/experiments/source_lock.json`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`;
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R1.md`;
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R2.md`;
- `BATCH_06_STATUS.md`;
- `BATCH_06_IDEA_REPORT.md`;
- `BATCH_06_PAPER22_PAPER_PLAN_FAILED_R0.md`;
- `BATCH_06_PAPER22_PAPER_PLAN_BLOCKED_R1.md`;
- and the remaining Paper 22 source package files needed to verify inventory,
  citation pool, proof-package alignment, and permission closure.

## Stable identities and immutable plan history

Current canonical plan under review:

- path: `papers/22-hamiltonian-cubic-spectral-collapse/paper/PAPER_PLAN.md`
- SHA-256:
  `2fdfc4eab1bd60e361b144eb8c3c9d0d7c71d37c63ce54145e7e6cca3888e224`
- bytes: `34692`
- LF count: `952`
- encoding/line endings: UTF-8, LF-only, terminal LF present, CR count `0`

Immutable root plan-history records checked directly:

- `BATCH_06_PAPER22_PAPER_PLAN_FAILED_R0.md`
  - SHA-256:
    `7758ce22918de8ee2511611884f861a58d36b37873e114ebbe5534a83a9301f2`
  - bytes `32169`, LF `795`
  - preserved failed-bytes history with CR / escaped-delimiter corruption; no
    review PASS was inferred there
- `BATCH_06_PAPER22_PAPER_PLAN_BLOCKED_R1.md`
  - SHA-256:
    `6a5ae037c6351291132ff1ea22ade36d851b1f861e5d1e88e4501a8fb498f785`
  - bytes `34008`, LF `939`
  - preserved mathematically accepted but permission-blocked history; the R1
    reviewer correctly wrote no review artifact

The current R2 plan prefix through the line immediately preceding
`## Independent Review Handoff and Path-Exact Permissions` hashes to

- `cd19b229837735a08dbb7f64bee6b62af71936c05472ee1c6ea7ec43a0ef2c43`

which matches the independently accepted unchanged R1 mathematical prefix
recorded in `BATCH_06_STATUS.md` and `BATCH_06_IDEA_REPORT.md`.

Candidate-review identities also match exactly:

- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R1.md`
  - SHA-256:
    `8d6cb168b303563cfc3719e176ca9b677b060c91a2527d48f4b49488d827e268`
  - terminal: `PAPER22_CANDIDATE_GATE_PASS_R1`
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R2.md`
  - SHA-256:
    `de7a20a707c5b8926802cb2b5f0db1fd355970a808e908884fa30bbe948b1349`
  - terminal: `PAPER22_CANDIDATE_GATE_PASS_R2`

## Exact project inventory and pre-write path state

Immediately before this review write:

- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`
  did not exist
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/PUBLICATION_STAGE_SCOPE.md`
  did not exist

The Paper 22 project universe at review time is exactly:

- regular files: `14`
- child directories: `4`
- symlinks: `0`

Child directories:

- `experiments`
- `notes`
- `paper`
- `refine-logs`

Regular files:

- `experiments/EXPERIMENT_PLAN.md`
- `experiments/EXPERIMENT_TRACKER.md`
- `experiments/source_lock.json`
- `notes/CITATION_VERIFICATION.md`
- `notes/CLAIMS_EVIDENCE_MATRIX.md`
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`
- `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`
- `notes/NOVELTY_ASSESSMENT.md`
- `notes/PROOF_PACKAGE.md`
- `notes/RESEARCH_QUESTION.md`
- `paper/PAPER_PLAN.md`
- `refine-logs/FINAL_PROPOSAL.md`
- `refine-logs/INITIAL_PROPOSAL.md`
- `refine-logs/REVIEW_SUMMARY.md`

All fourteen are regular files, mode `0644`, and CR-free. No forbidden
`manuscript/`, `publication/`, `build/`, `release/`, `results/`,
`submission/`, `transport/`, `.tex`, `.bib`, or `.pdf` artifact exists in the
Paper 22 tree.

## Independent byte, format, and structure checks

I verified:

- exact title:
  `Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number`
- exact public author line: `Anonymous`
- headline range remains an arbitrary characteristic-zero field `K`,
  `r>=4`, `g>=2r+1`
- exact phase order remains `F=T\circ S`
- UTF-8 / LF-only stable bytes with terminal LF and no CR/BOM/NUL drift
- exactly `57` literal display-math delimiter pairs `\[` / `\]`
- §0 Abstract plus exactly eight numbered main sections §1–§8
- exact page-budget sum `26.5`
- all theorem-critical proofs remain planned in the main body, not an appendix

The R2 permission-tail repair is the only substantive change from accepted R1.
The diff is exactly the expected one: the heading changed to path-exact review
handoff language, the sole review write path is named, the blocker rule is
literal `WRITE NOTHING`, the sole later eligible path is
`notes/PUBLICATION_STAGE_SCOPE.md`, and downstream paths remain closed.

## Independent formula and proof-plan consistency audit

I independently checked that the plan is mathematically aligned with the proof
package and locked theorem:

- the displayed family is exactly the endpoint-spiked product pair
  `V_{r,g}` and `W_{r,g}` with shears `S`, `T`, and `F=T\circ S`
- the support-row story correctly fixes `M`, `A`, `B`, and `C=BA`
- the normalization is exactly
  `x_i=u_i/u_1` for `2<=i<=r` and
  `sigma=sum_{i=2}^r x_i`, excluding `x_1`
- both selector margins, the seed, every cone wall, and the least-parameter
  threshold are explicitly required in the main body
- the carry proof is phase-labelled and uses both carried-coordinate phases
- leading-form survival is required in the polynomial domain, not from degree
  arithmetic alone
- strict last-coordinate visibility is correctly separated as `n>=1`, while
  the exact degree identity is correctly stated for `n>=0`
- Perron--Frobenius is used only after exact visibility closes
- the invariant spaces `U` and `E`, the equal-middle coordinate convention,
  `A_E`, `B_E`, `Q_{m,h}`, `P_{m,h}(t)`, and `P_{m,h}(1)` are copied exactly
- the unit eigenvalue is required to have exact algebraic and geometric
  multiplicity `r-3`
- the cubic is called an annihilator; no universal minimality,
  irreducibility, or “algebraic degree exactly three for every Perron root”
  claim appears
- the `g=2r` statement is limited to the ordinary seed and selected strict
  face
- the formal `r=3`, `m=1` specialization is only a low-mode consistency check
- the coefficient extension is limited to exactly four nonzero coefficients on
  the fixed two supports

I found no formula drift between the plan, the proof package, the source lock,
and the upstream reviewed source materials.

## Citation, anti-claim, and public-separation audit

I verified:

- the citation pool is exactly `S01`–`S06`, with no seventh record
- every source is assigned a context-only role
- no theorem-critical selector, matrix, recurrence, quotient, multiplicity, or
  boundary claim is delegated to a citation
- the zero-figure / zero-experiment / zero-CAS / zero-dataset contract is
  explicit
- the public article is instructed to exclude local project identifiers,
  local paper numbering, filesystem paths, hashes, review verdicts, source or
  publication locks, dashboards, collision matrices, permission history, and
  other governance provenance
- the hard anti-claims cover maximal/necessary cone language, arbitrary
  supports or shear words, positive characteristic, universal irreducibility
  or minimality, global threshold optimality, low-mode novelty inflation,
  entropy/periodic/arithmetic/classification claims, literature firstness, and
  computer-evidence substitution

The public-facing narrative is therefore properly separated from internal
governance and local portfolio machinery.

## Permission and downstream-boundary audit

The repaired tail now passes the exact path-permission checks:

- the potential reviewer's sole writable path at this gate is
  `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`
- any blocker requires literal `WRITE NOTHING`
- the sole passing terminal line is `PAPER_PLAN_PASS`
- a valid `PAPER_PLAN_PASS` has exactly one effect: it makes
  `notes/PUBLICATION_STAGE_SCOPE.md` eligible for one later, separate,
  scope-only author invocation
- the reviewer is not authorized to create that scope file
- neither the plan nor `PAPER_PLAN_PASS` directly authorizes
  `experiments/publication_lock.json`, manuscript prose, TeX, BibTeX, figures,
  code, experiments, datasets, computer algebra or CAS, build, PDF, release,
  transport, submission, upload, repository push, messaging, identity
  disclosure, `Paper23`, or any other external effect

This closes the exact blocker that prevented R1 from writing.

## Verdict

I found no blocker in:

- the current plan's raw-byte identity and stable readback;
- the immutable R0 and R1 root histories and their recorded identities;
- the unchanged accepted mathematical prefix hash;
- the exact `14`-file / `4`-directory / `0`-symlink project universe;
- exact title, Anonymous status, headline range, and phase order;
- UTF-8 / LF-only hygiene and the `57` paired display delimiters;
- section structure and exact `26.5`-page budget;
- theorem transcription against the proof package and source lock;
- selectors, cone walls, carry order, leading-form domain proof, visibility,
  Perron step, invariant splitting, quotient matrix, cubic, `P(1)`, exact
  unit multiplicity, and the bounded `g=2r`, `r=3`, and fixed-support
  coefficient statements as planned;
- the `S01`–`S06` context-only citation boundary;
- zero figures / zero experiments / zero CAS;
- public/governance separation; or
- the repaired path-exact permission tail and downstream closure.

The R2 paper plan is internally consistent, mathematically aligned with the
locked proof package, structurally feasible as a 26.5-page proof-first
article, and permission-correct at its tail. The sole review write is
therefore justified, and the next boundary is scope-only: a later separate
author invocation may create `notes/PUBLICATION_STAGE_SCOPE.md`, and nothing
further is opened here.

PAPER_PLAN_PASS
