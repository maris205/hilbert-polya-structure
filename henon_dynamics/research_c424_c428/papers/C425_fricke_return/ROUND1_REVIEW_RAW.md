# C425 — first actual nonauthor manuscript review

2026-09-09 UTC. Reviewer: current-team arithmetic-lane agent, not the
C425 manuscript author or the coordinator who wrote the original Fricke
proof. This reviewer had also reviewed the earlier proof package. The
present pass separately reads the actual complete manuscript and PDF;
it is not that earlier admission report relabelled as a manuscript round.
No external-model service or human peer review is claimed.

## Verdict

The accepted all-coefficient, all-level line/core classification is
fully transferred into the 12-page article. The proof is self-contained,
the original three-involution clock is maintained, and the source and
execution limits are appropriately explicit. No critical or major
mathematical defect, omitted proof dependency or source-ownership error
was found. One minor but concrete abstract correction is requested below.

**Mathematical must-fix: 0. Source/evidence must-fix: 0. Minor manuscript
corrections requested: 1 (P1).** Recommend adoption of P1, one real revised
build and the scheduled second nonauthor manuscript pass. No numerical
journal score, submission acceptance or completed final-release gate is
asserted. The absence of an executed finite core is not a missing test:
this theorem proves a terminating exhaustive procedure.

## Actual frozen inputs and reading

The reviewer read all twelve active manuscript inputs in full: main,
macros, bibliography and nine section files, including all three tables.
The complete `build.sh`, DRAFT_HANDOFF, SOURCE_AUDIT and BUILD_REPORT
were read. All 614 lines of the actual PDF's extracted text were read,
and all twelve saved renderings of that PDF were separately viewed.
The PDF's metadata, fonts, final engine and bibliography logs, citation
records and byte identity with its baseline/build copy were checked.

The full 272-line frozen proof, frozen question, 131-line original source
audit and 383-line earlier nonauthor review were reread as provenance and
comparison, not as substitutes for the typeset argument. The complete
260-line C421 predecessor proof and its actual title/date entry were
read for the equal-forcing subtraction; neither its code nor certificate
was imported or executed. The route update in the frozen question keeps
the original object while replacing the tentative difference approach
by the accepted maximum-height proof.

Frozen PDF: `papers/C425_fricke_return/main.pdf`, 12 pages, 378216 bytes,
SHA-256 `aa6c4ee4bbc6f55bcf2934caccc927bf36aef872bf230466541c0f3de7b2f207`.
Its `baseline.pdf` and `build_initial_04/main.pdf` are byte-identical by
actual `cmp` checks. The active source hashes agree with DRAFT_HANDOFF:

| Input relative to the manuscript directory | SHA-256 |
| --- | --- |
| `main.tex` | `1d9df3c901777f5993ea4ac586be1b4aa29c4a8c3aa729bfef8d7caffbe4cc8a` |
| `math_commands.tex` | `40878d702da4e1cf18b3effb0a87ebd840790258fd64f9337304f481b926ce97` |
| `references.bib` | `9b35b94a205812d6b9e7ab43e2b6d162206fa94c34e07b7a84bce5b0bc69b7c0` |
| `sections/00_abstract.tex` | `89f057e8a1bdae42d21e6c1696112dc9a64bab18272d9117aec0878797a982e0` |
| `sections/01_introduction.tex` | `53a15a438a71f3ca6666be7ac4f90f425722df1b65cbdb048021bfe949c3313d` |
| `sections/02_phase_lift.tex` | `1ddc3f867112dbdb2aa8eb33bfb9724731f55c331e8b1a1b309ea91bc457bff8` |
| `sections/03_state_graph.tex` | `514d6b7d89c8ec63a588e6e5b2264f92320c66d8501e47972552fb5f5a798a65` |
| `sections/04_height_forcing.tex` | `21844ed7ccb5bd1956410386e9468ce19443e2db20e18304c0a88b2323a3cec5` |
| `sections/05_line_exhaustion.tex` | `8f9890ce3a66df0327be78c7e6987414f18337415e7fcf9e158718c52fb2b56b` |
| `sections/06_effective_classification.tex` | `2432ae11bd4f35d11be1c3785776354f6dfdcb397c677edb0e8848a183a74c02` |
| `sections/07_level_counts.tex` | `1c93670e56816f391123852f7b2b35642ec2cad96cb10447395d9c9006d2c38f` |
| `sections/08_scope.tex` | `795fd2f41be2d98f308292de8bf219e278d9dff6ff265eec144bfcffe392e194` |
| `build.sh` | `81a579a73fe5067a1924aaf6dc991dffc03bb7ec09bccfb1a7f087c45d8018ff` |

Original proof SHA-256:
`4672ce2e12a3e6584cb2bc4df815ea9c4110806d2d96d05a0506cdf79ed10b9c`.
Original source audit SHA-256:
`e1e7f6ce47027eec07069e53eac99506de249e8a4726409daac5227a3ab7f0f8`.
Earlier review SHA-256:
`9c7cea3c7b425141744103ed7cf66546659f3c1bb9d25daae813099259d5c8b5`.
Current manuscript SOURCE_AUDIT SHA-256:
`b51a788f2399684ee9596f68ec8603cdc66b1e661f1aa624335e323e96ef5ee7`.
Current BUILD_REPORT SHA-256:
`41d36ebe607449379b7ae8aca0013dbd3b7677d234b4ea43663f542649790df7`.

## Substantive manuscript checks

1. **Full domain and exact time.** Theorem 1.1 ranges over every ordered
   integer triple and the entire integer lattice, retaining zero
   coordinates and ordinary singular points. The native map is exactly
   `s_z s_y s_x`, rightmost first. Equations (2.1)–(2.3) prove that
   `F^3` on phase zero is this word. The displayed inverse is correct.
   The phase is never forgotten when a lifted return becomes native.
2. **The maximum is genuinely global.** Native triples partition the
   scalar indices, proving (2.6), including intermediate factor updates.
   In Lemma 2.1, integrality first reduces both neighbors to magnitude
   at most two; either value of magnitude two then forces a coordinate
   larger than M. Neither a local maximum nor a reversed forcing word
   is substituted. The manuscript expressly forbids reusing this lemma
   at an arbitrary later large coordinate.
3. **Every state transition is explicit.** Table 2 and Lemma 3.1 agree
   in phase, endpoint and affine parameter. Type I gives `(v,vt+b,c)`;
   Type II has the three listed intermediate triples. These are whole-
   line identities for all integer parameters. Each parametrization
   contains a unit slope, and each edge parameter is an integer
   bijection with displacement bounded by B0.
4. **The omitted-edge cases are exhausted.** Lemma 4.1 treats Type I
   with `|c|>=2`, then the zero case with `|b|>=2`, `|b|=1`, and
   `b=0, |a_(i+2)|>=2`. The respective lower bounds are valid at
   `M>100B0` and `j<=27`; in particular both factors in (4.4) exceed
   `M/2`, and the strict quadratic inequality is justified. Exactly
   27 transitions suffice to repeat a state among 28 visits. No
   unbounded iteration of a deteriorating height estimate is needed.
5. **Affine returns and inverse images close the proof.** The phase
   sum gives `3|ell_C`. The identity/reflection cases fix every
   parameter after at most two graph circuits; a nonzero translation
   cannot contain a periodic point. Equation (5.3) includes every
   intermediate image, and surjectivity on integer parameters proves
   equality of the whole line union with its image. Ambient bijectivity
   then removes every pre-cycle graph tail. This is the essential
   backward-exhaustion step, and it is fully typeset.
6. **Counts concern lines and returns, not automatically periods.**
   Disjoint cycle-state sets give `sum ell_C/3 <= 27`; phase-zero
   returns are at most 54. Coincident lines only decrease the count.
   The text explicitly allows one native orbit to move between distinct
   lines. This correct statement is the reason for abstract correction
   P1 below; no change to Proposition 5.3 is required.
7. **Finite-core exit semantics are correct.** The partial map retains
   only edges remaining in Q_R. Injectivity forces a first repetition
   to be the initial seed, and N_R+1 visited vertices suffice for
   termination. An exit excludes only an orbit wholly in the box, not
   global periodicity of a line point. The invariant line union removes
   entire finite cycles, so the exhaustive union and disjoint output
   lose no point.
8. **All line parameters receive exact labels.** The unit slope proves
   integer saturation of each rational line. Coincidences and every
   integral intersection are decidable by linear equations. For each
   divisor of a certified return, the three coordinate polynomials
   identify exactly its period-dividing parameters. The all-zero and
   nonzero-gcd cases are separated; zero roots, constant gcds and the
   finite rational-root test are covered. The smallest identically
   vanishing divisor gives the generic least period, and the union of
   finite exceptional root sets receives exact individual labels.
9. **Every invariant level remains finite.** Equation (7.2) is checked
   by its displayed expansion. Equation (7.3) is monic quadratic;
   invariant transport and unit-slope reparametrization preserve it.
   Therefore each of at most 27 lines meets a level in at most two
   integer points, while the core has at most N_R points. The ordinary
   cycle-count and zeta identities are consequently legitimate on each
   level. The text correctly refuses an ordinary all-lattice zeta when
   a fixed iterate has infinitely many integer points.
10. **Evidence and ownership remain bounded.** Procedure 6.3 is a
    terminating complete output rule, not a claimed executed census.
    No old C421 certificate is needed for this proof. Nonsharpness,
    impractical possible box size, internal AI-assisted review and the
    absence of target Euler/root-number conclusions are all explicit.

## Fresh bounded primary-source checks

The review reopened all five public primary endpoints, with targeted
reads/finds and no fresh search query. These checks do not constitute
a new full-literature search or full reads of every cited paper.

- **Shin:** read the coefficient/involution setup, Theorems 1.1–1.3,
  height-graph definitions, the displayed zero/plus-one/minus-one
  coordinate identities, and Remark 3.1 in the accepted v3. The last
  remark indeed permits independent coefficients. The manuscript's
  sign conjugacy gives `(-A,B,C,D)` and preserves the ordered word.
  The fixed-word distinction is an inference from the checked scope.
  The arXiv record confirms the cited journal volume/pages, DOI and
  1 June 2026 version date. Embedded graph figures were not separately
  inspected. [Primary v3](https://arxiv.org/html/2308.16614v3),
  [version record](https://arxiv.org/abs/2308.16614v3).
- **Cantat:** read the family setup, Proposition 2.2, Section 3's
  setup/Theorem 3.1 and displayed proof, Proposition 3.2 and proof,
  Corollaries 3.3–3.4 and proofs. The boundary escape neighborhoods
  justify the already-subtracted compact-containment consequence on a
  fixed fibre; they are not an explicit level-independent radius.
  Lines crossing levels do not contradict the absence of invariant
  curves within one fixed surface. [Primary v2](https://arxiv.org/pdf/0711.1727v2).
- **Vishkautsan:** read the abstract, unforced-surface and two-reflection
  setup, residual-periodicity definition and Theorems A–B. This is the
  adjacent local/global observable described in the manuscript, not
  its three-factor integer-locus theorem. No later proof is used.
  [Primary v2](https://arxiv.org/pdf/1504.07099v2).
- **Abboud:** read the version header, abstract and introduction through
  Theorem A and the algebraic-torus discussion. The cited comparison of
  periodic sets of two loxodromic automorphisms is correctly contextual;
  no later effective-height claim is imported.
  [Primary v3](https://arxiv.org/html/2406.11510v3).
- **Planat–Chester–Irwin:** read the publisher front-page metadata,
  abstract and introduction. The article's stated focus on selected
  Painlevé VI solutions supports the restrained contextual sentence;
  later sections were not screened for every potential overlap.
  [Publisher PDF](https://mdpi-res.com/d_attachment/dynamics/dynamics-04-00001/article_deploy/dynamics-04-00001.pdf?version=1704184938).

The bibliography has six cited entries; all five public DOIs are
visible in the actual PDF, and the C421 reference is plainly local and
unpublished. The manuscript's recorded metadata retrieval limits are
not silently upgraded by this review. No worldwide priority,
retraction/interest certification or fresh publisher check for each
entry is claimed. These public works are ownership/context sources,
not omitted steps in the present self-contained proof.

## Requested correction

| ID | Severity | Actual location, defect and precise remedy |
| --- | --- | --- |
| P1 | Minor claim clarity; adopt before second pass | `sections/00_abstract.tex`, lines 13–15, PDF page 1: `identify every large periodic orbit with a whole periodic line` can identify a finite orbit with an infinite line and suggests containment in one line, while Section 5 expressly permits travel between lines. Replace this clause by `place every large periodic orbit in a finite union of whole periodic lines` (or an equivalent containment statement). Theorem 1.1 and Proposition 5.3 are already correct and require no alteration. |

No new computation, theorem or quantitative bound is requested. The
earlier optional observation that invariant preservation makes every
actual graph cycle retained need not be added: the complete affine-return
test is valid as written, and adding that observation would be an
optional simplification rather than repairing a defect.

## Actual PDF/build observations and action boundary

All twelve rendered pages were viewed, including the full three tables,
proof breaks, exact procedure, level formulas and six-entry bibliography.
No clipping, collisions or illegible equation was observed. Page 12
contains references; the complete proof is on pages 1–11, without an
external Markdown-only dependency. All 23 font resources reported by
`pdffonts` are embedded Type 1 fonts; metadata has the anonymous author
and no creation/modification dates. The final engine and BibTeX logs
contain no warning, unresolved reference/citation or over/underfull-box
match. The author faithfully records one failed and three successful
changed-input initial builds; none is a manuscript review or final
identical-input pair.

This review made read-only local/source/PDF/log/hash checks, twelve
page-image views, bounded public primary retrievals and this report
write only. Mathematical programs, symbolic diagnostics, finite-core
enumerations, old certificate reruns, LaTeX builds, manuscript-source
edits, external uploads and Git mutations by this reviewer: **zero**.
The `research-review` skill supplied the claim/evidence discipline;
the batch's assigned nonauthor team review replaces external-model and
ML-venue defaults. Coordinator adjudication, author revision, the second
actual manuscript pass and all final release gates remain distinct.
