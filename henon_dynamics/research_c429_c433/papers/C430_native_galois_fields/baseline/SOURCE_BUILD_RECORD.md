# C430 source and first-draft build record

Article: **Native Galois fields of small wild cycles**. Anonymous English
mathematics article, `article` 11pt, one-inch margins, ordinary numbered
citations. This is an author drafting/self-review receipt, not an external
peer review, a completed manuscript-review round, or a release seal.

## Mathematical inputs and scope

The approved shared batch plan, its complete C430 section, closed outline
review and admission Section 2 were read. All six arithmetic proof files
below were read completely before drafting; they remain unchanged.
Paths in this table are relative to `../../` (the batch directory).

| Input actually read | Typeset destination |
| --- | --- |
| `continuation_round3/a3_interlevel_contacts/PROOF_SUPPLEMENT.md` | Sections 2–3: exact factor, displacement, prime-value argument and second-layer degree obstruction |
| `continuation_round3/a3_interlevel_contacts/FULL_LOCAL_INERTIA.md` | Section 4: exact level-two multiplier, canonical cluster matching and full native action |
| `continuation_round3/a3_interlevel_contacts/ORIENTED_QUOTIENT_STABILIZATION.md` | Section 5: trace-one resolvent, positive native sign, equality of oriented classes and embedded first fields |
| `continuation_round4/a3_first_quotient_ramification/PROOF_PACKAGE.md` and `SECOND_LAYER_BREAKS.md` | Sections 5–6: disjointness, once-\(p\) cancellation, all early-conductor cases, actual \(L_2\) and compositum filtrations and differents |
| `continuation_round5/a3_eventual_quotient_tower/PROOF_PACKAGE.md` | Section 7: compact-action continuity, canonical translation character, whole-group uniform quotient transfer and algebraic kernel fields |

The complete OM4 proof inputs
`continuation_round4/a1_optimal_cycle_measures/PROOF_PACKAGE.md` and
`continuation_round4/d1_isometric_cycle_limit/PROOF_PACKAGE.md` were also
read. For the final draft, the actual companion C431 Theorem 1.1 and
Sections 5–6 were checked directly in its newly typeset source.
Its title is *Haar limits of optimal wild cycles*; Theorem 1.1 is
*Compact adding-machine limit of the optimal cycles*,
label `thm:compact-adding-machine`. Its first PDF exists locally, SHA256
`989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6`.

C430 Theorem 7.1 restates only the companion's classical compact closure,
full-sequence Hausdorff limit and native infinite adding-machine
conjugacy. The companion includes the finite-contact separation proof
of aperiodicity; weak measure convergence alone is not the input.
Theorem 1.3 uses this dependency, whereas C430 Theorems 1.1–1.2 and
C431's proof are independent of one another. The bibliography identifies
C431 as unpublished and supplies actual relative PDF and source links.

The quantifier is every odd prime. The raw AS representatives are not
claimed equal. The original full fields are not claimed nested, and
the eventual thresholds are not claimed to be \(E_j=j\).
The hypothetical containment calculation is explicitly distinguished
from the actual second-layer breaks. The different is computed in the
integer-normalized field valuation, not from the nonmaximal root order.
The displayed root discriminant and \(p=3\) values are direct symbolic
consequences of the already proved formulas, not experimental evidence.

## Source access and its limits

The complete coordinator source synthesis
`continuation_round4/NOVELTY_CHECK_UNIFORM_LOCAL.md`,
the full `continuation_round4/x2_uniform_local_source_admission/REPORT.md`,
and `continuation_round5/x1_eventual_tower_sources/REPORT.md` were read.
The manuscript's comparisons are restricted to those checked passages.
Drafting-turn public access was read-only; no manuscript was uploaded.

| Bibliography item | Actual access or explicitly inherited check |
| --- | --- |
| Lindahl–Rivera-Letelier | Actual arXiv:1311.4478v3 metadata and HTML Theorem C, its \(q=1\) discussion and Proposition 4.4; issue/DOI metadata agrees with the read source records. The author-version numbering is explicit. |
| Keating, *Extensions of local fields and truncated power series* | Actual arXiv:math/0312391v2 metadata; the detailed Theorem 6.1 and Proposition 5.1 hypothesis checks are inherited from the fully read source audits, not claimed as a new full-paper read on this drafting turn. |
| Keating, *Wintenberger's functor for abelian extensions* | Actual author metadata and publisher record at https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.693/; exact Theorem 1.1/Section 3 comparison follows the fully read source audits. |
| Elder–Keating | Actual arXiv:2503.16830v1 Sections 1–2, including character conventions, Hasse–Arf, Lemma 2.2 and Theorem 2.3 with proof, read in HTML. The perfect-residue-field hypothesis covers the present algebraically closed residue field. |
| Debaisieux | Actual arXiv:2603.03873v2 metadata, including the 22 April 2026 version; the Propositions 2.1–2.3 comparison uses the fully read X1 source audit and coordinator synthesis. No new complete proof read of this preprint is claimed. |
| Conrad | Actual Stanford *Completion of algebraic closure* handout, introduction and Theorem 1.1; the statement about extending the action is checked there and proved as needed in C430. No fixed-field theorem inside the completion is invoked. |
| Stacks, 0BMI | Actual Section 9.22, including the profinite topology, inverse-limit description, open normal subgroup correspondence and proofs. |
| Stacks, 0BWD and 0BWG | Actual statements and proofs of Lemmas 49.12.2–49.12.3; used only for the monogenic different formula. |
| C431 | Actual local Theorem 1.1, Sections 5–6 and existing first PDF; unpublished companion status retained. |

All nine entries are cited. No invented DOI, issue number, author or
publication status is supplied. The read records and primary pages
verify the metadata present in the bibliography; not every cited
publication was re-read in full during drafting. There was no new
exhaustive forward-citation or retraction-database search. These are
bounded-source comparisons, with no worldwide-priority assertion.

## Actual builds and author inspection

The `paper-plan` and `paper-write` instructions and their required writing
reference were read during preparation; `paper-compile` was read in full
before compilation. The approved mathematics-article format supersedes
the skill's ML venue page caps. No installation, mathematical program,
formal evaluator, Git operation, seal or external model API was used.
No figure was added: the required distinctions are explicit equations
and prose, with no proved full-field nesting to depict.

Before the first real build, `main.tex`, `math_commands.tex`,
`references.bib` and `sections/` were copied into the new
`qa/author_build_01/source/`. The actual build command there was:

```sh
env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee ../compile.log
```

This first pipeline did not enable `pipefail`; its pipeline status alone
is therefore not treated as compiler evidence. The retained complete
log itself shows all three pdfLaTeX passes and two BibTeX passes
finishing, and `Latexmk: All targets (main.pdf) are up-to-date`.
Its final TeX/BibTeX logs contain no warning or box notice. The genuine
first PDF, 18 pages and 404875 bytes, remains with that source snapshot.

All source sections and bibliography were self-read. All 18 first-build
pages were actually rendered and visually inspected, without clipped
text, colliding equations, missing glyphs or illegible mathematics.
This found only two bibliography capitalization issues:
`Artin--schreier--witt` and `The Stacks project`. Braces protecting the
proper names were the only source changes after that build.

The corrected source was copied into the separate new
`qa/author_build_02/source/`, then built with:

```sh
set -o pipefail
env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee ../compile.log
```

This invocation returned zero and completed three pdfLaTeX/two BibTeX
passes. Expected first-pass undefined labels and citations resolved;
the final `main.log` and `main.blg` have zero compiler/package warnings,
undefined references/citations, missing characters, overfull or underfull
boxes. No failed compiler invocation occurred.

The corrected PDF is **18 pages, 404880 bytes**, US Letter, PDF 1.5.
The body ends and bibliography starts on page 17; page 18 contains its
last two entries. All 20 listed font resources are embedded subset
Type 1 fonts with Unicode mappings; there are no Type 3 fonts.
Raw creation and modification metadata both equal `D:20260909000000Z`.
The manuscript is anonymous; no identifying PDF author metadata is set.

`pdftotext -layout` and `pdftoppm -r 95 -jpeg -jpegopt quality=82` were
run on both versions, and their outputs are retained under the two
build directories. Extracted text differs only at the two capitalization
corrections. Page renders 1–16 compare byte-identically; changed pages
17–18 were actually viewed again and are readable without overflow.
No `??`, `[?]`, `[VERIFY]`, `TODO` or `FIXME` remains in source/PDF text.
Every section file is included by `main.tex`.

## Frozen round-zero baseline and hashes

`baseline/src/` is the direct source copy of the inspected corrected
first draft. `baseline/main.pdf`, `baseline/main.log` and
`main_round0_original.pdf` preserve that actual first-draft state.
The earlier `qa/author_build_01/` is also retained unchanged; it is not
presented as a manuscript-review revision. The later
`qa/author_build_02/` retains its own genuine build evidence.
Two prospective nonauthor manuscript reviews remain the coordinator's
next step. Earlier mathematical-input checks are not counted as reviews
of this newly typeset manuscript.

| File | SHA256 |
| --- | --- |
| `main.tex` | `64726ac4156c5f58f7012373b0e00497bf36ea3465c7f664d46292749ca39669` |
| `math_commands.tex` | `09ce6cb709b396eef06067e872ed648bc5f4f4295c2c80200e2f4ccc4b298cdd` |
| `references.bib` | `9bb44aae6ffbd524fd24c6567df1bc7ab671fd7f11ea5a62031c35496f1bfcaa` |
| `sections/00_abstract.tex` | `4190fecbf742de602c4a6a1f9add60df97350f4922fe77a0c0bce5e8a63c8189` |
| `sections/01_introduction.tex` | `83859269616b6fc2d58ab8b22729b862c1cb9bbe49ab87ece564567086d2eefb` |
| `sections/02_local_setup.tex` | `6072b59c61c9583e035b9363c63e7889858b9ba127a8fa33024c036672f57ff6` |
| `sections/03_second_layer.tex` | `f65985674292b57f6cbe52ea2c407394e785fb1d9224dbe8829d9990a811204f` |
| `sections/04_full_inertia.tex` | `9f40a4775383c07dd4a4ecc8733f9ffbb235f1215ab26f02be60a62099fd298c` |
| `sections/05_oriented_quotients.tex` | `8cc49232529207fcbec1ff90f73ef9fe5cd5ca8a9e7049785355f47e7034d284` |
| `sections/06_ramification.tex` | `28d77c6548a8e8780ed56750cdea277b536cd2bbb3147a3abc6ef8c0fe3ea77c` |
| `sections/07_eventual_tower.tex` | `4873ac52d5dedee20ec4443d480d86bfdaf306e2dbcbef3d365c5e88a4a19b43` |
| `sections/08_scope.tex` | `026bdee1dd9bc96e3835c6ec038495cbbd4854ed3e178b95f5ee31ba37e999f2` |
| `main.pdf` | `54bc61f0d9c89405047fdf116bbcaf38d9e658c6d401b70862b22659f2574c8e` |
| `qa/author_build_01/source/main.pdf` | `275aea7a19d686856b8e540b5e267ebe4c06d1f500c550eb64d704cb7ec55a4f` |
| `qa/author_build_02/source/main.log` | `7b2cc706dcf7bdbaca4d7c7389162484cf18d078162954edda2ba0dccb6bfc4f` |
| `qa/author_build_02/compile.log` | `bb49cf27e079f7726a81f182227e1109e837618662e7097426ff0f06f81d794c` |

Status: full author draft, source self-review, actual builds and all-page
visual coverage complete; frozen for independent manuscript review.
