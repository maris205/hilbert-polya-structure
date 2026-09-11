# Bounded source and internal-collision subtraction

Scope: the single CTM literal in [INTAKE.md](INTAKE.md). This is a negative
author boundary, not novelty clearance. No external contact, upload or
specialist response was solicited. There is no independent literature review.

## 1. Exact public searches and the primary source actually read

The three inputs below each contain exactly three web queries. The matching
output JSON is the actual complete tool-returned text, not a reconstructed
search-result summary. A search result is not a source-body read.

| Input and complete return | Scope and purpose |
|---|---|
| `sources/matrix_search_input.json` / `matrix_search_output.json` | Literal `"A^T A^2"`, matrix transpose/cubic dynamics and finite-field cubic functional graphs; unrestricted search domains. |
| `sources/cubic_search_input.json` / `cubic_search_output.json` | Exact Konyagin title plus two expanded matrix/cubic expressions; unrestricted domains. |
| `sources/recent_search_input.json` / `recent_search_output.json` | Three arXiv-domain queries; the first requests recency 183 days, the other two are unrestricted in time. |

The exact nine query strings, domain restrictions and recency value are in
those input files. The recency query returned older items too. Its presence
does not establish six-month coverage, an exhaustive recent survey or a
verified absence of a CTM owner. Nonprimary search hits, including forums,
aggregators and bibliographic lists, were discovery noise and are not used
to support any theorem or ownership conclusion.

The sole downloaded external primary work used here is Sergei V. Konyagin,
Florian Luca, Bernard Mans, Luke Mathieson, Min Sha and Igor E. Shparlinski,
*Functional Graphs of Polynomials over Finite Fields*. The downloaded
author PDF identifies itself as arXiv:1307.2718v3, 26 May 2015. Retrieved
arXiv/publisher metadata reports *Journal of Combinatorial Theory, Series B*
116 (2016), 87–122, DOI 10.1016/j.jctb.2015.07.003. The journal text itself
was not separately read. [Author preprint](https://arxiv.org/abs/1307.2718),
[publisher DOI](https://doi.org/10.1016/j.jctb.2015.07.003).

The successful curl invocation, response headers, complete stdout/stderr and
exit are in `commands/primary_pdf_download/`; pdftotext is separately captured
in `commands/primary_text_extract/`. Physical PDF/text copies were made and
pinned before the primary body read in `history/primary_before_read/`.
The exact author-PDF SHA256 is
`3b30fb5a93a3038841346a126b66244ab3ba877bf01ef7b0df49933433aee036`;
the extracted-text SHA256 is
`c67662765d36c1606de356a14547155dfa6daea9474abf84ad45577e587efef8`.

**Actual read limit:** extracted text lines 1–195, exactly as captured in
`commands/primary_body_read/`. This includes the abstract, introduction and
the beginning of the first theorem's proof, not the entire paper and not
a completed independent verification of that theorem. Only the introduction
is used: finite-field functional graphs encode periods and preperiods, and
monomial mechanisms should not simply be substituted for general polynomial
graphs. No numeric theorem from the paper is imported into CTM.

The local structural-preflight source is physically copied with its hash.
The actual command produced `sources/konyagin.preflight.json` with verdict
`UNAVAILABLE` because pypdf is absent. Consequently the cited read limit is
in extracted-text lines, not a claim of validated original-page anchors,
page-count integrity, complete visual inspection or a PDF-read PASS.

**Source-verification outcome:** title/authors/arXiv identity are supported
by the downloaded header; journal reference is retrieved metadata; used
introductory context is supported by the stated body range; CTM ownership,
priority and the completeness of current coverage are **not established**.
No statement that the CTM cubic factors are globally unsolved in the
literature is made. The narrower statement is that this desk did not prove
their full temporal structure or matrix lifts.

## 2. Internal originals and precise read limits

Before source reading, physical control copies included AGENTS, STATE,
the linked batch PIPELINE, current Git receipt, the exact old Git receipt,
project skill, full HISTORY/caveats and current theorem/artifact contracts.
The workflow and inherited problem/review controls were separately copied
before reading. Their manifests bind before/copy/after bytes. Mandatory
central summaries are status/context, not substitutes for the below proofs.

All paths in the next table are relative to this lane's physical `history/`
directory. The original paths are preserved under each snapshot group and
recorded exactly in its `PIN_MANIFEST.json`.

| Physical group and original | Actual body read used in this desk | Collision conclusion and limit |
|---|---|---|
| `recent/.../finite_systems_twenty_sixth/{INTAKE,PROOF_PACKAGE}.md` | Both complete documents. | ASC fixed-skew linearization, EMD missing axes and UTR exact-old are closed boundary inputs, not directions to repair. |
| `recent/.../finite_systems_twenty_seventh/{INTAKE,PROOF_PACKAGE,HANDOFF}.md` | All three complete documents. | SRT exact P112 and conservative gcd-flow missing all-size theorem remain negative; no inherited finite box is promoted. |
| `recent/.../PROBLEM_ANCHOR.md` | Complete. | Current two-axis/fresh-value contract; no new admission from a summary. |
| `matrix_originals/.../papers172_176_sequence/scouting/fresh_nonlinear_algebra/{SCOUT_AND_KILL_LEDGER,COLLISION_FIREWALL}.md` | Both complete documents. | Matrix-word/Gram/transpose/scalar-collapse combinations are a crowded prior lane; primitive multiplication/coordinate change earns no freshness. |
| `matrix_originals/.../finite_systems_twentieth/PROOF_AND_ADAPTERS.md` | Complete. | Prior transpose–Gram/collapse adapters are subtracted; CTM is not declared a new exception just because its literal word differs. |
| `matrix_originals/.../papers122_126_sequence/scouting/algebraic/SCOUT.md` | Physically copied; only rg fragments, no separate body read. | Discovery pointer only; no complete theorem or gate acceptance imported. |
| `nearby_originals_v2/.../papers127_131_sequence/scouting/algebraic/SCOUT.md` | Lines 1–160, captured in `scalar_matrix_original_read`. | In particular X01 is the additive rule `A^T+A^2` over F2, not CTM's multiplicative rule over odd fields. The excerpt is an old negative ledger, not a full new review. |
| `nearby_originals_v2/.../algebra_third/SOURCE_AND_COLLISION_NOTES.md` | Complete document (the command requests lines 1–160). | Existing matrix-mechanism crowding; no invented `INTAKE.md`, whose attempted copy really failed. |
| `nearby_originals_v2/papers/102-cyclic-group-algebra-involution-norm-dynamics/main.tex` | Lines 1–190. This covers its collapse and Fourier proof blocks, not the whole manuscript. | Commutative involution-norm collapse is spent. General noncommuting CTM is not shown conjugate to it, and that absence of an adapter is not owner clearance. |
| `nearby_originals_v2/papers/103-double-adjugate-matrix-dynamics/main.tex` | Lines 1–190. This covers its Jacobi identity and iterate proof blocks; a later proof is only partly exposed. | Its determinant-dependent scalar iterate mechanism is distinct from CTM's moving trace/skew recurrence. Merely having `d'=d^3` cannot import its temporal result. |
| `nearby_originals_v2/papers/150-zero-totalized-lyness-finite-fields/main.tex` | Lines 1–170, definitions and statements, not all proofs. | Literal zero-totalized Lyness map is not CTM. A historical ledger's informal trace-reduced label is not treated as the manuscript's definition. |

The four explicit content searches and their exact regexes are durable under
`discovery/`. Their scopes exclude many snapshots/reviews and are not the
whole repository. The three v1 scopes were also actually flawed as recorded
in [SCOPE_FAILURE.md](SCOPE_FAILURE.md). Search misses cannot certify either
exact-literal freshness or absence of a theorem-level adapter.

## 3. What is subtracted, and what remains missing

CTM's entry coordinates are an invertible bookkeeping change. Determinant
multiplicativity, Cayley–Hamilton, scalar cube-root choices, linear-system
inversion and finite-field quadratic-form counts receive zero novelty credit.
The singular sector becomes a symmetric rank-at-most-one matrix followed
by ordinary cubing; that power mechanism is also zero credit.

The author deductions in PROOF_PACKAGE.md do establish a full-carrier
one-step decoder, including every singular kernel branch, and an independent
zero-target count. They do not give a complete all-q invertible temporal
theorem. The determinant-one/skew-k trace factor is onto the specific family
`s -> s^3+(k^2-3)s`; it is not “every cubic polynomial”, an equivalence with
the matrix map, or a reason to announce a hard/unsolved problem.

After collision subtraction there is no defensible fresh two-axis package
ready for a candidate gate. This remains **HOLD_PROOF_SOURCE / NO_PROMOTION**,
with no paper number or reserve. No added finite census is recommended.

## 4. Exact historical Git-control mapping

The launch-time current Git receipt was physically copied with SHA256
`2f6998d2986831fa8776e31e9d336497e6ab37b114d1b13ef94879f3e2271c24`.
The separate historical bytes with SHA256
`af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da`
are copied under `history/controls/.../qa/central_lifecycle_p209_a/`.

The original live path for those older bytes is
`docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md`. Root's actual prior
recovery receipt, physically copied in `history/git_recovery/` and fully
read in `commands/git_recovery_read/`, binds them to Git commit
`f8ee398cb7b0ddd5d1e5890543034a001cd2bc26`, tree
`79d5256492bd29647cb739d71282e631f944fe6f`, with actual git-show and stdin
cmp exits zero. `history/git_provenance/` preserves root's explanatory
README. This desk did not rerun Git or claim a new at-time copy at the old
launch; it verifies only that exact documented path/hash alias. Other live
path changes are not silently refreshed into historical evidence.
