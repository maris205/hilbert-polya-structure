# Paper 13 Publication-Stage Expansion Scope

## State, purpose, and non-self-authorization

- Candidate: `henon_primitive_cycle_cover_v1`
- Date: 2026-08-16 UTC
- Current state: `PUBLICATION_STAGE_LOCKED / PENDING_INDEPENDENT_PUBLICATION_REVIEW / NO_DRAFT / NO_BUILD`
- Prepared target: an anonymous, proof-first, independently reviewed draft
- Current draft authorization: `false`
- Current build authorization: `false`
- Finalization authorization: `false`
- Submission authorization: `false`
- Author-identity release: `false`
- Required next verdict: `PUBLICATION_STAGE_PASS`

This scope expands the already passed result-aware proof-to-writing handoff
only far enough to prepare an anonymous draft, deterministic draft builds,
two bounded independent manuscript reviews with at most one revision cycle,
and a terminal integrity receipt for the anonymous draft.  It does not
self-authorize any of those actions.  A fresh, role-separated publication
reviewer must first rehash the exact bindings, repeat the complete plan audit,
and write the sole gate-review file
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` with the exact verdict
`PUBLICATION_STAGE_PASS`.  Until that verdict exists against unchanged bytes,
no draft source, diagram, build output, manuscript review, revision, or draft
integrity artifact may be created.

A pass activates only the stage-gated paths and roles enumerated below.  It
does not create a submission-ready or identity-bearing artifact.  In
particular, `paper/main.pdf` remains an anonymous reviewed draft; neither it
nor a later `DRAFT_INTEGRITY_PASS` is a finalization or submission verdict.

## Exact frozen-input receipt

The publication-lock author directly rehashed the following closed input set
and read no project artifact outside it.  The bytes and hashes below are the
only author-side inputs to this expansion.

| Project-relative path | SHA-256 | Bytes |
|---|---|---:|
| `experiments/manuscript_lock.json` | `488c257f377de1cbc94855041c3e7930cbab3fdf1d390a310684a8fc9b0344cd` | 9154 |
| `notes/RESULT_AWARE_MANUSCRIPT_SCOPE.md` | `265fd1539d4957a78422c641c9508a432d769389fe7f78fb3cc5fdbf7c8b0307` | 16992 |
| `notes/RESEARCH_QUESTION.md` | `18ccf35df9b0f3b73636044c9400f3d79e8f213af365fb33504fa3524f6fd287` | 12301 |
| `notes/PROOF_PACKAGE.md` | `9b1fd6a4e262d7b4dc0df4456e58b1af3b78be63a58014860679d992f71dd6d9` | 25766 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `21537ed1ed04abf7e3e1dc7d089a105fc36eb5815d164e1cae840f8c56464890` | 13041 |
| `notes/CITATION_VERIFICATION.md` | `08d310cb4c5b8e14810bf06e79e988ecf28b9ef2825868b7f7edfeccdce0e71b` | 27784 |
| `notes/NOVELTY_ASSESSMENT.md` | `bde37eb93989989d2c55c81b13c6919a9ba367c6f2d7ca2320335fd0df155c6a` | 20383 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e` | 15344 |
| `results/INDEPENDENT_RESULT_REVIEW.json` | `a5d1d3df1ed5e6e34d16aa50b86f5028c4ea86a655492794f0c58d8febcae23a` | 4462 |
| `notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md` | `3df02be2a4a629d9eeab89b9fe3cd30dc47892729603205d308ab6b9f5320e98` | 15574 |
| `paper/PAPER_PLAN.md` | `3dd625590a16e0fe64f475e5913a3d5f1b9eac9b2883e136f389c049ae5d0911` | 39066 |

The plan has 822 lines and ends in one newline.  The three M5 transition
artifacts are bound separately: the result-aware scope, canonical manuscript
lock, and independent `RESULT_AWARE_HANDOFF_PASS` review have the exact
hashes printed above.  The theorem authority remains the exact proof package
plus the exact independent R2 `SOURCE_LOCK_PASS`.  The R2 review binds source
lock SHA-256
`11d51aae93f4230a06046de7c3c8331a7e00169b69295d335435f470f9ff9469`.
Because `experiments/source_lock.json` was not in the publication-lock
author's closed input set, that source-lock hash is an indirect governance
binding here, not a claim of author-side rehash.  The independent publication
reviewer receives reviewer-only authority to rehash that exact source-lock
path before passing the gate.

## Zero-write plan-review receipt

A fresh plan reviewer returned the message verdict `PLAN_REVIEW_PASS` against
the exact plan hash, 39066-byte size, and 822-line count above.  The review
was deliberately zero-write: there is no plan-review file, path, or hash to
bind.  This receipt is therefore explicitly unattested by a durable review
artifact and may not be represented as one.  The reviewer reported that all
of the following checks passed:

1. exact safe title and one-sentence contribution;
2. PC1 as the dominant theorem and PC2 as its narrower subordinate layer;
3. C1--C20 mapping to source-proof authority, with a complete machine-proof
   firewall;
4. all sixteen proof bridges in order, including the main-text chain through
   the unique prime, (e=1), (R_0+S_1), and finite birational normality;
5. the correctly directed special-line-to-global monodromy inclusion;
6. separate non-base proofs for \(\tau\) and \(\rho\);
7. the exact \((d,n)=(2,2)\) boundary;
8. direct and adjacent prior-art collision handling without priority claims;
9. `RESULT_PASS` confined to bounded implementation consistency;
10. the mandatory same-family/correlated-error paragraph exactly once in
    Section 8 and nowhere in the abstract, claims, proofs, figures, tables,
    or novelty discussion;
11. zero experimental figures or result tables and at most one later-
    authorized definition-only diagram;
12. eight sections plus Appendices A--C, a 24.5-page working budget,
    citation controls, anonymity, and absence of public workflow jargon; and
13. continued closure of all later source, figure, build, finalization, and
    submission permissions.

A historical end-of-file blank-normalization observation was reported as
nonblocking; the current exact bytes and final newline are the binding.  The
forthcoming independent publication reviewer must not rely on this message
receipt.  It must reperform every check above directly on the bound plan and
record the results in its durable review.

## Authority hierarchy and machine firewall

1. The sole theorem authority is `notes/PROOF_PACKAGE.md` at SHA-256
   `9b1fd6a4e262d7b4dc0df4456e58b1af3b78be63a58014860679d992f71dd6d9`
   conjoined with `SOURCE_LOCK_PASS` in
   `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` at SHA-256
   `83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e`,
   which binds source lock SHA-256
   `11d51aae93f4230a06046de7c3c8331a7e00169b69295d335435f470f9ff9469`.
2. The research question, claims matrix, citation verification, novelty
   assessment, M5 scope and lock, handoff review, stable paper plan, this
   scope, and the publication lock constrain presentation and permissions.
   None enlarges the theorem.
3. `results/INDEPENDENT_RESULT_REVIEW.json` has verdict `RESULT_PASS` only
   for `BOUNDED_IMPLEMENTATION_CONSISTENCY_ONLY`: registered count one, no
   rerun, zero reviewer scientific recomputations, no machine-proof
   authority, and no proof or scientific-truth claim.
4. R100 must never be rerun.  No publication role may invoke, import, or
   recompute either implementation route, a runtime adjudicator, or any
   scientific engine.  No path under `code/`, `preexecution/`, or `runtime/`
   is manuscript evidence or a publication-stage input.  Under `results/`,
   only the exact independent result review is readable.
5. The independent result review may be mentioned only in the one mandatory
   Section 8 paragraph below as bounded implementation consistency.  It may
   not support a theorem premise, proof step, formula, abstract, contribution,
   figure, table, scientific conclusion, novelty statement, or priority
   statement.  Raw Q/R or runtime paths, hashes, values, certificates, and
   summaries are prohibited public content.

## Exact closed read authority

Every list below is path-exact, closed, and non-transitive.  A directory name
does not grant directory access.  A path, hash, citation, embedded record,
manifest entry, bibliography field, generated summary, tool, or subagent
cannot expand a list.  Symlinks, path aliases, `..`, absolute-path escapes,
network retrieval, and transitive citation fetching are prohibited.

### Gate reviewer, before `PUBLICATION_STAGE_PASS`

The fresh publication reviewer may read exactly:

1. `notes/PUBLICATION_STAGE_SCOPE.md`;
2. `experiments/publication_lock.json`;
3. `experiments/manuscript_lock.json`;
4. `notes/RESULT_AWARE_MANUSCRIPT_SCOPE.md`;
5. `notes/RESEARCH_QUESTION.md`;
6. `notes/PROOF_PACKAGE.md`;
7. `notes/CLAIMS_EVIDENCE_MATRIX.md`;
8. `notes/CITATION_VERIFICATION.md`;
9. `notes/NOVELTY_ASSESSMENT.md`;
10. `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md`;
11. `results/INDEPENDENT_RESULT_REVIEW.json`;
12. `notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md`;
13. `paper/PAPER_PLAN.md`; and
14. `experiments/source_lock.json`, for governance rehash only.

Its sole write is `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`.  It may
perform byte hashing, strict JSON validation, line/byte counting, path-safety
checks, and plan/source-scope comparison, but no scientific recomputation.

### Draft author, after `PUBLICATION_STAGE_PASS`

The anonymous draft author may read exactly the eleven direct frozen inputs
in the receipt table, this scope, `experiments/publication_lock.json`, and
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`.  It may also reread the
draft-source paths it is actively authoring.  It may not read
`experiments/source_lock.json`; its hash is governance, not manuscript
content.  Bibliography records must be reconstructed only from the locked
`notes/CITATION_VERIFICATION.md`; no web or external metadata lookup is
authorized.

### Optional diagram author

The diagram author may read exactly `paper/PAPER_PLAN.md`, this scope,
`experiments/publication_lock.json`,
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`, and `paper/main.tex`.  It may
not read results, code, runtime, build logs, or any external asset.

### Deterministic builder

The builder may read exactly `paper/main.tex`, `paper/references.bib`, the
optional `paper/figures/architecture.tex`, this scope,
`experiments/publication_lock.json`,
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md`, and the ten exact generated
build-output paths listed below.  A missing optional diagram or not-yet-
generated output is valid.  Generated outputs may be read only for build,
warning, metadata, hash, and reproducibility checks.

### Manuscript reviewers and one revision author

The Round-1 reviewer may read the post-pass draft-author set, the three
possible draft-source paths, the exact Round-0 build outputs, and the
Round-0 build receipt.  The revision author may additionally read
`notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md`.  The Round-2 reviewer may
additionally read the Round-1 review, the revision receipt, and the exact
Round-1 build outputs.  Each reviewer has only its named review write path
and may not edit manuscript bytes.

### Draft-integrity roles

After `MANUSCRIPT_REVIEW_PASS` in Round 2, the manifest author and independent
draft-integrity reviewer may read exactly the pre-existing paths enumerated
in the lock's `integrity_roles` allowlist.  That list excludes the reviewer-
only source lock and the integrity review's own not-yet-written output.  The
manifest author writes only
`paper/DRAFT_ARTIFACT_MANIFEST.json`; the independent integrity reviewer
writes only `notes/INDEPENDENT_DRAFT_INTEGRITY_REVIEW.md`.  Neither role may
rerun R100, recompute science, edit the manuscript, release identity, or
submit anything.

## Exact closed write authority

The following paths are the complete publication-stage write universe.  A
path is usable only at its stated gate; the list grants no directory-wide
authority.

### Lock preparation and gate review

- `notes/PUBLICATION_STAGE_SCOPE.md` -- publication-lock author only; frozen
  once its hash is placed in the canonical lock.
- `experiments/publication_lock.json` -- publication-lock author only;
  self-hash excluded and frozen after author stop.
- `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` -- fresh publication
  reviewer only, and only while all bound bytes are stable.

### Draft sources after `PUBLICATION_STAGE_PASS`

- `paper/main.tex`;
- `paper/references.bib`; and
- optional `paper/figures/architecture.tex`.

No `paper/math_commands.tex`, section split, style file, class file, build
script, data file, image, supplementary source, acknowledgment file, or
other draft path is authorized.  All macros stay in `paper/main.tex`.

### Deterministic draft-build outputs

- `paper/main.aux`;
- `paper/main.bbl`;
- `paper/main.blg`;
- `paper/main.log`;
- `paper/main.out`;
- `paper/main.pdf`;
- `paper/main_round0.pdf`;
- `paper/main_round1.pdf`;
- `paper/BUILD_RECEIPT_R0.json`; and
- `paper/BUILD_RECEIPT_R1.json`.

No `.toc`, `.fls`, `.fdb_latexmk`, SyncTeX, index, glossary, Biber, shell-
escape, cache, temporary image, or unlisted build output is authorized.  The
builder may delete or overwrite only the exact derived paths in this list
while performing a clean deterministic rebuild; source and governance paths
may never be removed by the builder.

### Bounded review, revision, and draft integrity

- `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md` -- fresh Round-1 reviewer only;
- `notes/MANUSCRIPT_REVISION_R1.md` -- revision author only;
- `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md` -- fresh Round-2 reviewer only;
- `paper/DRAFT_ARTIFACT_MANIFEST.json` -- manifest author only after the
  Round-2 pass; and
- `notes/INDEPENDENT_DRAFT_INTEGRITY_REVIEW.md` -- independent integrity
  reviewer only.

There is at most one manuscript revision cycle under this lock.  Round 2 must
return exact verdict `MANUSCRIPT_REVIEW_PASS` on the revised Round-1 bytes.
If Round 2 finds a required change, the stage fails closed and a new explicit
expansion is required; no unreviewed Round-2 patch is authorized.

## Stage order and activation rules

1. **P0 -- publication gate.**  Current state is no draft and no build.  The
   gate reviewer rehashes all 14 reviewer inputs, validates canonical JSON,
   repeats the zero-write plan-review criteria, and either writes
   `PUBLICATION_STAGE_PASS` or authorizes nothing.
2. **P1 -- proof-first source draft.**  After the pass, the author writes
   Sections 2--6 and Appendices A--C first, then Section 7, and only then the
   Abstract, Section 1, and Section 8.  The author stops and reports exact
   source hashes before any build begins.
3. **P2 -- deterministic Round-0 build.**  The builder performs the fixed
   build protocol below, verifies a byte-identical clean rebuild, preserves
   the result as `paper/main_round0.pdf`, and writes the canonical Round-0
   receipt.  A failed or nondeterministic build blocks review.
4. **P3 -- independent Round-1 review and one repair.**  The reviewer writes
   the complete review without editing the draft.  The revision author then
   changes only authorized sources, writes the exact revision receipt, and
   stops.  The builder repeats the deterministic protocol, preserves
   `paper/main_round1.pdf`, and writes the Round-1 receipt.
5. **P4 -- independent Round-2 review.**  A fresh reviewer binds the revised
   source and Round-1 PDF hashes and returns `MANUSCRIPT_REVIEW_PASS` only if
   every proof, scope, citation, anonymity, visual, and build check passes.
   Any other disposition stops the locked stage.
6. **P5 -- anonymous-draft integrity.**  The manifest binds all authoritative
   source, diagram-if-present, review, revision, build, and PDF bytes.  A
   role-separated reviewer rehashes the closed inventory and may return
   `DRAFT_INTEGRITY_PASS`.  That verdict certifies only the integrity of the
   anonymous reviewed draft and does not authorize finalization or submission.

## Deterministic build contract

The article uses pdfLaTeX plus BibTeX, not `latexmk`, Biber, shell escape, or
networked tooling.  From the exact `paper/` working directory, each clean
build uses `TZ=UTC`, `SOURCE_DATE_EPOCH=1786838400`, and
`FORCE_SOURCE_DATE=1`, then runs, in order:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
2. `bibtex main`;
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.

`main.tex` must suppress variable PDF dates and trailer identifiers, contain
no table of contents or package that creates an unlisted side file, use no
shell escape, and set the public PDF title to the exact safe title.  PDF
Author, Subject, Keywords, CreationDate, and ModDate must be empty or absent;
Creator and Producer may contain only fixed tool identifiers.  The build must
have zero undefined references, zero undefined citations, zero missing
glyphs, zero overfull boxes above 10 pt, embedded fonts, 24--25 pages of
mathematical content excluding references as planned, and no local path,
identity, hash, workflow identifier, or unresolved drafting marker in the
PDF text or metadata.

Each receipt is strict canonical JSON with source and output hashes, byte
sizes, page count, tool versions, command sequence, environment values,
warning counts, font and metadata checks, and the hash from a second clean
build.  The two clean PDF hashes must be identical.  The receipt is build
integrity only, never mathematical evidence.

## Proof, story, and boundary contract

The public title is exactly *Normalized Primitive-Cycle Covers in a
Degenerating Hénon Family*.  The article is a format-neutral specialist
mathematics paper with eight numbered sections and Appendices A--C.  Its
one-sentence contribution and What/Why/So-What structure are those frozen in
the plan.  PC1 is the theorem spine.  PC2 is explicitly narrower after
Morton's scalar generator results and remains subordinate in the abstract,
Introduction, page allocation, conclusion, and review criteria.

The manuscript must expose the following sixteen bridges in this order:

1. monic coefficient-ring cyclic Groebner basis and the rank-(d^n) basis;
2. generic etaleness and the generic actual-period idempotent;
3. Henselian connected lifting and identification of one field (E_n);
4. excellence, Nagata finiteness, and finite normalization;
5. normal-surface Cohen--Macaulayness and miracle flatness;
6. the unique (a)-adic prime, (e=1), residue degree, multiplicity-one
   divisor, and (R_0+S_1) nilpotent exclusion;
7. finite birational comparison and the exact scalar fiber;
8. constants and geometric integrality;
9. Reynolds invariants, rank, arbitrary base change, and affine quotient;
10. scalar-line-to-global monodromy with the direction
    \(\pi_1(U_0)\to\pi_1(U)\) and the time-shift centralizer bound;
11. cyclic invariance and the ordered pointwise derivative-return trace;
12. scalar infinity branches with the word sum and inverse product derived
    independently;
13. separate non-base proofs for \(\tau\) and \(\rho\), including all degree
    cases and excluding (r=1);
14. the full-(S_r) maximal-stabilizer step applied separately;
15. determinant-line characteristic polynomials, nonzero top wedge,
    Vandermonde, and generic discriminant; and
16. the direct degree-one boundary derivation.

Bridges 6--7 and 10 must remain visible in the main text.  The exact boundary
record is

\[
\nu=2,\qquad r=1,\qquad \tau=a-1,
\]

\[
z_0z_1=(a-1)^2+c,\qquad
\rho=4a^2-6a+4+4c.
\]

Both multiplication polynomials are linear there; the case supplies neither
a non-base assertion nor nontrivial monodromy evidence.  The twelve frozen
anti-claims remain global: no formal-to-actual promotion on every fiber; no
everywhere embedded primitive subscheme; no automatic normalization/base-
change compatibility; no every-fiber smoothness, reducedness, etaleness, or
free torsor; no projective interpretation of the affine quotient; no reversed
monodromy inclusion; no primitivity from non-base behavior alone; no field-
trace or determinant reinterpretation of \(\rho\); no non-base or nontrivial-
monodromy claim at (r=1); no extension to arbitrary Hénon maps; no machine
or finite-case proof; and no novelty credit for occupied scalar generators
or formal trace-spectrum rigidity.

The direct prior-art boundaries remain mandatory: Gao--Ou for scalar
geometry; Morton (1998) and Fakhruddin for scalar geometric wreath monodromy;
Morton (1996) with the bounded 2011 corrigendum scope for scalar generators;
Cantat--Dujardin for formal-period trace-spectrum parameter reconstruction;
Endler--Gallas for low-period Hénon carriers; and Zhang for bounded-period
cyclic-polynomial computation.  Do not use `first`, `previously unknown`,
`no prior work`, `method novelty`, a universal absence claim, or language
that resolves the preserved novelty dissent.

## Mandatory same-family paragraph

The following paragraph must appear verbatim exactly once in Section 8 and
nowhere in the abstract, claims, proofs, equations, figures, tables, or
novelty positioning:

> Separately from the proof, a preregistered, seedless exact audit compared
> two independently implemented bounded routes in a single sealed run. An
> independent integrity review returned `RESULT_PASS` only for bounded
> implementation consistency. This computation is neither a proof nor a
> validation of the theorems, which rest on the mathematical argument and
> its independent source review. All available reviews used one model
> family, so correlated-error risk remains and no cross-model validation is
> claimed.

## Figure cap and exact caption contract

The default is figure-free.  At most one optional diagram is authorized, and
only at `paper/figures/architecture.tex`.  It must be a self-contained TikZ
definition-and-theorem architecture inserted into `paper/main.tex`; it may
not read or encode experimental, result, runtime, audit, certificate, or
numerical data.  It contains only the generic/integral/scalar-fiber rows, the
marked-point/cycle columns, the generic clopen-idempotent extraction, the
(C_n)-fixed-subring relations, reduction modulo (a), and the theorem's
dense-open (S_r) annotation with (S_1) trivial.  It uses vector strokes,
grayscale-safe styling, at most one colorblind-safe blue accent, and no
decorative title or evidentiary badge.

If present, its caption in `paper/main.tex` is exactly:

> **Figure 1. Definition-and-theorem architecture of the normalized
> primitive-cycle cover.** The generic actual-period field \(E_n\) is cut
> out only after passing to the generic finite-etale algebra
> \(B_n\otimes_AK\); \(S\) is the integral closure of \(A\) in \(E_n\), and
> \(S_0=S^{C_n}\). The theorem identifies the scalar fibers as
> \(S/aS\simeq D_n\) and \(S_0/aS_0\simeq D_n^{C_n}\) and gives geometric
> cycle monodromy \(S_r\) on a common dense finite-etale open. The diagram
> records definitions and theorem organization only; it is not evidence
> for any claim.

No second figure, plot, table, standalone diagram PDF, PNG, SVG, external
asset, or machine-evidence display is authorized.  If the exact contract is
not met, the diagram is omitted.

## Independent publication-review contract

The reviewer must be fresh and must not have authored this scope, the
canonical publication lock, the M5 scope/lock, the stable plan, or any future
draft.  Before returning `PUBLICATION_STAGE_PASS`, it must:

1. bind the exact SHA-256 and byte count of this scope, the canonical
   publication lock, all eleven direct frozen inputs, and the reviewer-only
   source-lock governance path;
2. strictly validate JSON for canonical encoding, duplicate keys, nonfinite
   values, path safety, self-hash exclusion, and closed non-transitive lists;
3. verify the M5 scope/lock/handoff-review triad and exact
   `RESULT_AWARE_HANDOFF_PASS` without promoting its authority;
4. reperform all thirteen zero-write plan-review criteria, bind the exact
   39066-byte/822-line plan, and explicitly state that no durable prior plan-
   review artifact exists;
5. verify PC1/PC2 hierarchy, C1--C20 mapping, all sixteen ordered bridges,
   the twelve anti-claims, exact \((2,2)\) formulas, citation collisions,
   priority prohibitions, and the same-family paragraph contract;
6. verify that R100 remains one-shot and sealed, that no rerun or scientific
   recomputation is authorized, and that `RESULT_PASS` remains bounded
   implementation consistency only;
7. verify every role-specific read list, every exact write path, the one-
   diagram cap, the exclusion of `paper/math_commands.tex`, and the
   deterministic two-build protocol;
8. verify anonymous public prose and metadata, no identity release, no
   submission, and no finalization; and
9. rehash both author artifacts after author stop immediately before issuing
   the verdict.

Any drift, omission, malformed JSON, scope promotion, path expansion,
unreviewed plan criterion, theorem/machine conflation, priority language,
identity exposure, or self-signature blocks the pass and authorizes no later
write.  This transition is fail-closed.

## Terminal exclusions

This scope does not authorize a camera-ready paper, author disclosure,
acknowledgments, funding text, institutional metadata, repository release,
preprint upload, journal or conference submission, supplementary archive,
public announcement, email, external message, or any write outside the exact
paths above.  Those actions require a new, explicit authority after a valid
`DRAFT_INTEGRITY_PASS` and are not implied by it.
