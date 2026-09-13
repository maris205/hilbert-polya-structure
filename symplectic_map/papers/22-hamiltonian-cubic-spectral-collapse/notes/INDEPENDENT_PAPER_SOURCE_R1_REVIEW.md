# Paper 22 — Independent Formal Source Review R1

## Reviewer identity, scope, and independence

Review date: 2026-08-24 UTC.

I am the fresh independent Paper 22 formal source reviewer R1. In this role I
authored none of the frozen source trio under review, none of the upstream
Paper 22 author-stop artifacts that governed their creation, and none of the
independent source-design / source-lock / paper-plan / publication-stage /
publication-lock reviews that bound the present gate.

I used no network access, no CAS or symbolic package, no scientific run, no
TeX/BibTeX build, no PDF workflow, no manuscript edit, no source edit, no
Paper 23 action, and no external effect. This file is my sole write.

Before writing, I read to EOF:

- `/root/.codex/skills/paper-write/SKILL.md`;
- `/root/.codex/skills/shared-references/writing-principles.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/paper/main.tex`;
- `papers/22-hamiltonian-cubic-spectral-collapse/paper/math_commands.tex`;
- `papers/22-hamiltonian-cubic-spectral-collapse/paper/references.bib`;
- `papers/22-hamiltonian-cubic-spectral-collapse/paper/PAPER_PLAN.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/PROOF_PACKAGE.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/PUBLICATION_STAGE_SCOPE.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/CITATION_VERIFICATION.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/CLAIMS_EVIDENCE_MATRIX.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`;
- `papers/22-hamiltonian-cubic-spectral-collapse/experiments/publication_lock.json`;
- `BATCH_06_STATUS.md`;
- `BATCH_06_IDEA_REPORT.md`;
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R1.md`; and
- `BATCH_06_PAPER22_CANDIDATE_REVIEW_R2.md`.

## Required adversary coordination

Per the source-review contract, I was not permitted to write PASS until a
separate fresh read-only adversary sent a direct
`READONLY_ADVERSARY_CLEAR` message and its stated source identities matched my
stable read of the trio. That message was received directly from
`/root/paper22_source_readonly_adversary` and reported:

- `paper/main.tex` SHA-256
  `9e71dca521e61000d6d850c8ca090ef36a9164e50e5ec94bab033adc2f17a78e`,
  `69218` bytes, `1921` LF;
- `paper/math_commands.tex` SHA-256
  `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c`,
  `330` bytes, `11` LF; and
- `paper/references.bib` SHA-256
  `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d`,
  `1928` bytes, `55` LF.

Those three identities match my own recomputation exactly. The adversary also
cleared the theorem chain, structure, citation boundary, metadata firewall,
and static-source hygiene without reporting any CRITICAL or MAJOR blocker.

## Revalidated live gate and pre-write state

Immediately before this write, I rechecked the live project state:

- `BATCH_06_STATUS.md` still records the current gate as
  `PAPER22_FORMAL_SOURCE_R1_REVIEW_OPEN`;
- the review path
  `papers/22-hamiltonian-cubic-spectral-collapse/notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md`
  did not exist;
- the Paper 22 project universe was exactly `22` regular files, `4` child
  directories, and `0` symlinks; and
- the four child directories remained exactly:
  `experiments`, `notes`, `paper`, and `refine-logs`.

No source drift, root-gate drift, inventory drift, or premature build/release
artifact appeared between my completed audit and the adversary clear.

## Stable source identities

I recomputed the frozen source trio immediately before writing:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `9e71dca521e61000d6d850c8ca090ef36a9164e50e5ec94bab033adc2f17a78e` | 69218 | 1921 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1928 | 55 |

All three files are UTF-8, LF-only, BOM-free, CR-free, NUL-free, and end in a
single terminal LF.

## Conjunctive audit

### 1. Public identity, metadata, and no-leakage audit

I verified all identity and metadata requirements exactly:

- source title is exactly
  `Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number`;
- `\title{...}` matches the frozen publication-stage title exactly;
- visible source author is exactly `Anonymous`;
- `\date{}` is exactly empty;
- `\hypersetup{...}` binds
  `pdftitle={Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number}`,
  `pdfauthor={}`, `pdfcreator={}`, and `pdfproducer={}`;
- no author footnote, affiliation, email, ORCID, acknowledgment, funding,
  grant number, corresponding-author marker, or hidden identity field appears.

I scanned the source trio for forbidden leakage and found none:

- no real-name or pseudonymous identity;
- no local path, project number, review token, hash, byte count, dashboard
  state, governance history, permission ledger, or PASS token;
- no reviewer / agent / model identity;
- no submission venue or external-effect authority;
- no comments in `main.tex` at all, and therefore no comment-channel leakage;
- no forbidden metadata or BibTeX-comment leakage.

This clears the exact public identity and firewall contract.

### 2. Article structure, abstract, contributions, proof placement, and zero-asset audit

The source structure matches the locked publication contract exactly:

- exactly one `abstract` environment;
- exactly eight numbered `\section{...}` headings;
- section titles match the frozen ordered list:
  1. `Introduction and bounded positioning`
  2. `The family, polynomial inverses, and symplectic geometry`
  3. `Gradient supports and the two strict selectors`
  4. `Seed containment and strict cone invariance`
  5. `Carried coordinates and leading-form survival`
  6. `Last-coordinate visibility, exact degrees, and Perron growth`
  7. `Unit modes, the equal-middle quotient, and cubic recurrence`
  8. `Sharp boundary, low-mode consistency, fixed-support coefficients, limitations, and conclusion`
- the headline theorem appears before bounded context in the introduction;
- the introduction contains exactly three explicit falsifiable contribution
  bullets;
- the proof roadmap is present in the fixed twelve-step order;
- theorem-critical arguments remain in the main body and are not deferred to an
  appendix;
- there is no appendix;
- there are exactly three `table` environments and zero `figure` environments;
- there are zero generated assets, plots, diagrams, experiments, datasets, or
  empirical tables in the public source.

The three public tables are the exact permitted mathematical-role tables:

1. gradient support-row ledger;
2. selector/cone proof ledger; and
3. three-dimensional invariant ledger.

The abstract is self-contained and citation-free. It states the theorem,
explains the mechanism, records strict visibility for `n>=1` with the tied
`n=0` case separated, gives the degree and Perron identities, records the
three-dimensional quotient collapse, and bounds the `g=2r` statement to the
ordinary seed and chosen strict selected face.

### 3. Independent theorem-chain replay

I independently rederived the complete locked theorem chain and found the
source mathematically aligned with the proof package and all frozen upstream
contracts.

Field, parameters, and maps:

- `K` is an arbitrary characteristic-zero field;
- `r>=4`, `g>=2r+1`;
- `h=g-1`, `m=r-2`;
- `V_{r,g}(q)=\prod_i q_i^2+q_1^g`;
- `W_{r,g}(p)=\prod_i p_i^2+p_r^g`;
- `S(q,p)=(q,p+\nabla V_{r,g}(q))`;
- `T(q,p)=(q+\nabla W_{r,g}(p),p)`;
- `F_{r,g}=T\circ S`.

Gradients, inverses, and symplecticity:

- the displayed gradients match the literal derivative formulas;
- subtraction inverses are stated exactly;
- the block Jacobians use symmetric Hessians and correctly prove preservation
  of `\omega=\sum_i dq_i\wedge dp_i`.

Literal support rows and matrices:

- the mixed score is exactly `2\sum_j u_j-u_i`;
- `M=2\mathbf1\mathbf1^{\mathsf T}-I_r`;
- only two rows compete: the first `V` row and the last `W` row;
- `A` is `M` with row 1 replaced by `he_1^{\mathsf T}`;
- `B` is `M` with row `r` replaced by `he_r^{\mathsf T}`;
- the complete-step matrix is exactly `C=BA`, never `AB`.

Cone normalization and selectors:

- ratios are defined only as `x_i=u_i/u_1` for `2<=i<=r`;
- `\sigma=\sum_{i=2}^r x_i`, excluding `x_1`;
- the cone is always called the
  `explicit sufficient invariant selector cone`;
- the first selector margin is
  `u_1(h-1-2\sigma)>0`;
- the second selector acts on `v=Au`, never directly on `u`;
- the exact reduced second margin is
  `(2h-4m)\sigma-(h+1)x_r-4m-2`;
- both sign cases are retained with the locked strict lower bounds
  `((h+1)(h-2m-3))/2` and `(2m+1)(h-2m-3)`.

Seed and all cone walls:

- the seed satisfies `\sigma(\one)=m+1<(h-1)/2`;
- middle lower walls use the exact strict expression
  `(h-1-2\sigma)+(x_i-1)>0`;
- the last lower wall retains both exact lower bounds
  `((h+2)(h-2m-3))/2` and `2(m+1)(h-2m-3)`;
- the height wall proves
  `(h-2m-3)(h+4m^2+4m+2)>0`;
- the least-parameter audit correctly records `h=2m+4` and decisive factor
  `h-2m-3=1`.

Carried coordinates and leading forms:

- both half-step carry comparisons are proved in the actual phase order;
- `C-I_r>0`, `A\one>\one`, and nonnegative nonzero rows of `A` are used
  correctly;
- leading-form survival is proved in the polynomial domain using
  `\LH(fg)=\LH(f)\LH(g)\neq0` and strict degree uniqueness;
- the source does not replace this with a positivity-of-coefficients shortcut.

Visibility and exact degree:

- `C-A>0` is proved entrywise;
- strict last-versus-first and last-versus-middle comparisons are carried out;
- strict visibility is asserted only for `n>=1`;
- the tied `n=0` case is preserved separately;
- the exact degree identity is stated exactly for `n>=0`:
  `\degt(F_{r,g}^n)=e_r^{\mathsf T}C^n\one`;
- the Perron statement is correctly an algebraic-degree statement:
  `\lambda_1(F_{r,g})=\rho(C)`.

Invariant splitting, quotient, cubic, and multiplicity:

- `U={z_1=z_r=0,\ \sum_{i=2}^{r-1}z_i=0}`;
- `\dim U=r-3`;
- `A|_U=B|_U=-I_U` and `C|_U=I_U`;
- `E={(a,b,\ldots,b,c)^{\mathsf T}}` in the exact equal-middle coordinate
  convention;
- `K^r=U\oplus E`;
- the locked matrices `A_E`, `B_E`, and
  `Q_{m,h}` are copied and used exactly;
- the trace, principal-minor sum, and determinant are the locked invariants;
- `\chi_C(t)=(t-1)^{r-3}P_{m,h}(t)`;
- `P_{m,h}(1)=-4m(m+1)(h+1)^2\neq0`;
- the eigenvalue `1` has exact algebraic and geometric multiplicity `r-3`;
- the scalar recurrence is correctly presented as a cubic annihilator with
  exact coefficients `T_0`, `S_0`, `D_0` and initial values `d_0=1`,
  `d_1=h(2m+3)`.

Boundary and bounded extensions:

- the `g=2r` discussion is bounded to the ordinary seed and selected strict
  face;
- the source does not promote it to a global failure or optimality theorem;
- the formal `r=3` substitution is clearly marked as
  `formal low-mode consistency` only;
- the four-nonzero-coefficient corollary is limited to the two fixed supports
  and characteristic zero, with no vanished coefficient, added monomial,
  changed support, changed shear word, or positive-characteristic extension.

I found no theorem-critical drift, no anti-claim breach, and no wording that
promotes a bounded statement into a stronger one.

### 4. Exact citation audit

The citation boundary passes exactly:

- cited keys are exactly:
  `BlancVanSanten2021`,
  `ShaoSun2025`,
  `Deserti2016`,
  `DangFavre2021`,
  `Rangarajan2002`, and
  `FujiokaKogawaLiShudo2023`;
- `references.bib` contains exactly those six entries and no seventh;
- there are no uncited bibliography entries and no missing cited keys;
- the related context is used only for bounded positioning, not as proof;
- no local predecessor citation is invented;
- no priority, firstness, or exhaustive-literature claim is made.

The BibTeX metadata match the verified pool:

- `BlancVanSanten2021` with DOI `10.1017/etds.2021.90`;
- `ShaoSun2025`;
- `Deserti2016`;
- `DangFavre2021` with DOI `10.4007/annals.2021.194.1.5`;
- `Rangarajan2002`; and
- `FujiokaKogawaLiShudo2023`.

### 5. Static LaTeX audit without compilation

I performed a static source audit only, with no compilation.

The source trio passes:

- UTF-8 decode;
- LF-only endings;
- no BOM;
- no CR;
- no NUL;
- one terminal LF in each file.

`main.tex` passes:

- balanced `\begin{...}` / `\end{...}` environment counts;
- balanced braces;
- exactly `121` labels with no duplicates;
- `98` references/cross-references with no missing target;
- exact citation closure to the six-key bibliography;
- zero comments;
- zero `TODO`, `FIXME`, `XXX`, `TBD`, `VERIFY`, `placeholder`, or `??` markers;
- zero `figure` environments;
- zero `\includegraphics`;
- zero `\appendix`;
- zero `\include{...}`;
- only one external source include: `\input{math_commands}`;
- no shell-escape or external-write commands such as `\write18`.

The theorem/proof environment surface is consistent with a main-body
proof-first article:

- `theorem`: 6
- `lemma`: 2
- `proposition`: 5
- `corollary`: 2
- `definition`: 1
- `proof`: 12

### 6. Source mass, reverse-outline credibility, and page-band audit

Without building, I cannot certify physical page count, and I explicitly do
not claim to do so. I did audit source mass and structural density for
credibility against the frozen target:

- `detex` visible word count, run from the paper directory so that
  `\input{math_commands}` resolves, is `6620` words;
- the draft contains substantial theorem/proof mass across §§2–8 and does not
  pad with governance text, figures, appendices, or decorative assets;
- the introduction front-loads the payoff, the theorem, the three
  contributions, the bounded context, and the twelve-step roadmap;
- the remaining sections each carry the exact proof branch locked in the plan.

This is a credible proof-first source for the frozen `24–28` preferred and
`22–30` hard substantive page band, while leaving actual physical page count to
a later authorized build gate.

### 7. Permission boundary and lifecycle audit

This review uses the sole authorized write path at the present gate:

- allowed write path: `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md`;
- source edits remain unauthorized;
- build, auxiliary files, PDF, release, Paper 23, and every external effect
  remain unauthorized;
- no automatic build or downstream transition is implied by this PASS artifact
  itself.

Pre-write Paper 22 inventory was exactly:

- regular files: `22`
- child directories: `4`
- symlinks: `0`

The pre-write regular-file universe was:

- `experiments/EXPERIMENT_PLAN.md`
- `experiments/EXPERIMENT_TRACKER.md`
- `experiments/publication_lock.json`
- `experiments/source_lock.json`
- `notes/CITATION_VERIFICATION.md`
- `notes/CLAIMS_EVIDENCE_MATRIX.md`
- `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md`
- `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md`
- `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`
- `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md`
- `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md`
- `notes/NOVELTY_ASSESSMENT.md`
- `notes/PROOF_PACKAGE.md`
- `notes/PUBLICATION_STAGE_SCOPE.md`
- `notes/RESEARCH_QUESTION.md`
- `paper/PAPER_PLAN.md`
- `paper/main.tex`
- `paper/math_commands.tex`
- `paper/references.bib`
- `refine-logs/FINAL_PROPOSAL.md`
- `refine-logs/INITIAL_PROPOSAL.md`
- `refine-logs/REVIEW_SUMMARY.md`

After this sole review write, the post-review inventory is exactly:

- regular files: `23`
- child directories: `4`
- symlinks: `0`

with this file added and no other path modified.

## Verdict

I found no blocker in:

- live gate and stable pre-write inventory;
- exact frozen identities of the public source trio;
- required adversary coordination and identity match;
- anonymous title/author/date/PDF metadata contract;
- no-leakage firewall across source and bibliography;
- exact one-abstract / eight-section / three-table / zero-figure / zero-appendix structure;
- theorem-critical proof placement in the main body;
- full theorem chain from gradients through selectors, cone walls, carry,
  leading forms, visibility, splitting, quotient algebra, cubic, multiplicity,
  boundary, and fixed-support corollary;
- exact six-key context-only bibliography;
- static LaTeX hygiene and reference closure;
- credible source mass for the frozen page band, without claiming a build; and
- present permission boundary and no-downstream-authority closure.

This formal source review therefore passes.

PAPER_SOURCE_R1_PASS
