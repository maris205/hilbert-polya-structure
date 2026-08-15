# Independent Manuscript Review — Round 2

Review date: 2026-08-15 UTC  
Candidate: `cat_prime_shell_multiplicity_obstruction_v1`  
Manuscript: *A Multiplicity Audit for Prime-Torsion Euler Products of the Cat Map*  
Reviewer role: fresh independent Round-2 mathematical, scope, provenance, reproducibility, figure, and publication-readiness reviewer  
Verdict: **PASS**  
Disposition: **MAY_FINALIZE**  
Confidence: **5/5** for mathematics, revision closure, and local artifact integrity; **4/5** for literature completeness because this review was intentionally offline  
Overall score: **85/100 (8.5/10)**

## Executive decision

All four bounded Round-1 findings are closed, and I found no Critical,
Major, or Minor regression.  The final manuscript claim namespace C1--C9
now agrees one-to-one with the final claim manifest; the reader-facing
manuscript contains no numerical novelty score or project-internal
``Paper 9/Paper 10'' wording; Figure 3 uses standalone follow-up wording and
reproduces deterministically; and the revised plan correctly describes
Figure 1's multiplicity axis as linear.

The scientific core also passes a fresh end-to-end regression.  The
split/inert/binary/ramified orbit theorem is correct, the raw-return and
external orbit-label constructions remain distinct, the scalar denominator
obstruction stays inside its stated fixed nonzero and (z)-independent
scope, the zero/equal/fractional/selector boundaries are exact, and the
global convergence claims stop at the proved safe strips.  Direct prior-art
collisions and the low-novelty specialized-note positioning remain explicit.

The exact source and PDF reviewed below may therefore be finalized without
another scientific or editorial revision.  Any change to the manuscript,
PDF, figures, bibliography, claim map, or upstream evidence after this
review would create a new snapshot and would require a new integrity check.

## Exact Round-2 bindings

Every requested principal digest was independently recomputed:

| Object | SHA-256 | Round-2 result |
|---|---|---|
| Round-1 independent review | `dc34ea65a091680e3a2e0f89b15f804f45b3a7be7ae11502d82c668ec6d58ed8` | PASS |
| Round-1 author response | `2cb3da5c9af34b12cb8a4e6f6c7c5b7c8299a95628f5d1126742dcc7be110934` | PASS |
| revised `paper/manuscript.tex` | `fb54cb9273c89ad5f76a9485d67a815555050b3c71e630e47d367b043ae6e26c` | PASS |
| revised `paper/manuscript.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` | PASS |
| `paper/paper_round1_revision.pdf` | `96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6` | PASS, byte-identical to live PDF |
| historical `paper/paper_pre_review.pdf` | `9b63f190e7c751c27682d1a9cc9246f0153edddfec61d4539c573ab70070d51c` | PASS, retained unchanged |
| Round-1 revision integrity record | `40df4fe0e893f3ae308fa609c34b39cc74be044a1ca03866d28c7f12f4e337dd` | PASS |
| revised `PAPER_PLAN.md` | `41a1e6e9356c3820c3890fca232b60302673c1a28a83d8ba26f932eec5f73e3e` | PASS |
| final `paper/CLAIM_MANIFEST.json` | `8dd511a2775460bcd9d33a925df60c780fd946f46ca015c3bf6f41b6fa80ccc8` | PASS |
| revised `paper/FIGURE_PACKAGE.json` | `477e63151c7b203d3199b5e98122f1b2df315910ec05f1c262cadb3044a4032c` | PASS |
| revised 24-path framed asset tree | `0526235c1b3581aba830e054d1f883fd677cb7a752180bb8a0eeb0dbab7a862e` | PASS, independently reconstructed |

The 24-path tree was recomputed from the exact lexicographically ordered
allowlist in `FIGURE_PACKAGE.json`, using its unsigned-64-bit big-endian
path/content framing.  It has 24 distinct paths and reproduces the frozen
revision digest exactly.

## Round-1 finding closure

### M1 — final claim map: CLOSED

Appendix B contains exactly nine rows, C1 through C9, with no X1/X2 row.
They agree one-to-one with the final `CLAIM_MANIFEST.json`:

| Final ID | Manuscript authority | Final-manifest source locator |
|---|---|---:|
| C1 | prime-shell orbit theorem and proof | 172 |
| C2 | raw-return and orbit-label products | 348 |
| C3 | fixed nonzero scalar obstruction | 412 |
| C4 | equal-weight repetition identity | 454 |
| C5 | fractional prime/composite identities | 474 |
| C6 | selector discard cost | 517 |
| C7 | safe convergence strips | 552 |
| C8 | registered exact audit | 627 |
| C9 | outside-theorem escape boundary | 604 |

The source-lock-era `CLAIMS_EVIDENCE_MATRIX.md` and planning table retain an
older planning namespace.  Round 1 explicitly recorded the remapping, and
the live publication namespace is unambiguous in both Appendix B and the
final claim manifest.  I therefore treat the older numbering as historical
provenance, not as a surviving M1 defect.

### M2 — numerical novelty self-score: CLOSED

The revised source and extracted PDF contain no `2.5--3/10`, `3/10`, or
reader-facing numerical novelty score.  The manuscript instead calls the
contribution deliberately modest, primarily diagnostic, and a low-novelty
negative audit.  The numerical calibration remains only in internal
planning/source-lock material, where it is appropriately identified as a
route-selection diagnostic.  Direct collisions with Gaspari and
Baake--Neumärker--Roberts remain prominent.

### M3 — standalone manuscript and Figure 3: CLOSED

The reader-facing manuscript and extracted PDF contain no project-internal
`Paper 9` or `Paper 10` reference.  The prose uses ``the present audit'' and
``follow-up work.''  Figure 3 visibly reads `UNTESTED / follow-up route`, and
its footer says that the follow-up centralizer route is not opened.  Its PDF
metadata is anonymous and standalone.

An isolated copy of the complete figure package was regenerated through the
supplied orchestrator.  Its two internal render passes were byte-identical
for all nine PDF/SVG/PNG outputs, and every regenerated output matched the
frozen package.  In particular:

- Figure 3 PDF: `2b0a72db9d8cea6d901a8f2e03d6f2a17c49a4d2a2cd217e36ccbf148d4806b4`;
- figure manifest: `23468908fb020e80677e7a5b8e8686c2d14edbec2dc1e74f06973940c12adb8e`;
- determinism audit: `a6aab23da51635f07e68104507a5ab55f49d64abdf33f70205e5317478b71129`.

Internal generator module names and schemas may retain the project number;
they are not present in publication-visible text or metadata and are not a
standalone-submission defect.

### M4 — Figure 1 axis contract: CLOSED

The revised plan now specifies a ``compact linear axis.''  The generator and
rendered Figure 1 use a linear axis with the exact frozen multiplicities
(1,2,4,6,24).  No plotted value or scientific axis implementation changed.

## Mathematical and scope regression

### Prime-shell arithmetic

The proof at manuscript lines 172--289 exhausts all prime cases.  In the
split case both eigenvalues have common order (	au_pmid p-1), every
nonzero vector has exact period (	au_p), and
(m_p=(p+1)h_p).  In the inert case multiplication by the norm-one root in
(mathbb F_{p^2}) gives common exact period (	au_pmid p+1) and
(m_p=(p-1)h_p).  Neither argument assumes maximal matrix order.

The binary Cayley--Hamilton argument gives one length-three orbit.  At five,
(A=-I+N), (N^2=0), and (operatorname{rank}N=1): the four nonzero
kernel vectors have exact period two, while the twenty remaining vectors
have exact period ten.  Thus the two/two cycle split and (m_5=4) are
correct.  The consequence (m_pge p-1) for odd primes and uniqueness of
the binary one-orbit shell follows.

### Product semantics and mechanism boundary

The fixed-point/Birkhoff construction correctly gives

\[
  Z_{\mathrm{raw},p}(s)
  =\prod_{\gamma\in\Gamma_p}(1-p^{-s|\gamma|})^{-1},
\]

including the separate length-two and length-ten factors at five.  The
externally assigned one-time orbit label is separately defined and gives
((1-p^{-s})^{-m_p}), with logarithmic repeat coefficient (m_p/r).
No step identifies the two objects.

The scalar theorem is valid exactly as scoped: after clearing denominators,
a finite product with every fixed (w_\gamma\ne0) has polynomial degree
(m_p>1) for odd (p), whereas (1-z) has degree one.  If zeros are
allowed, equality holds exactly for the multiset ({1,0,\ldots,0}).
Equal weights give (m_p^{1-r}), and fractional outer exponents work only
because complete orbit masses sum to one.  The Jordan-totient extension is
a symbolic finite-permutation identity and selects no composite input.

### Global claims and open mechanisms

The first logarithmic repetition together with (m_pge p-1) proves the
stated divergence/nonabsolute-convergence region through
(Re s=2).  The elementary upper bound (m_ple p^2-1) proves absolute
convergence only for (Re s>3).  The gap, exact abscissa, continuation,
functional equation, and zeros remain unclaimed.

Matrix, numerator, alternating, Fredholm, transfer, cohomological, enriched
selector, and centralizer mechanisms remain outside the theorem.  The
centralizer sentence uses the full finite-field linear centralizer (hence
the displayed (mathbb F_{p^2}^{\times}) in the inert case) and asserts no
quotient theorem.  A future symplectic-centralizer study must distinguish
the (\mathrm{SL}_2=\mathrm{Sp}_2) centralizer, but that future ambient-group
choice is not a defect in this manuscript's explicit nonclaim.

## Results, citations, originality, and disclosure

The strict result manifest passes a fresh read-only check: all ten listed
non-self evidence hashes match, and the live `results/` directory is exactly
the nine-file final inventory.  The unique lifecycle remains one registered
exact audit and one registered run, with zero candidate numerical runs.  The
five development-seen rows, 203 nonzero points, 37 cycles, and 12/12 exact
controls agree across manuscript, official reports, raw result, and claim
manifest.  They are consistently described as finite falsification controls,
not as all-prime or analytic evidence.

Mechanical citation closure is 11 cited keys, 11 BibTeX entries, and 11
generated bibliography items, with no missing or unused key and no BibTeX
warning.  The strongest arithmetic and product collisions are cited at the
claim sites.  No live URL resolution was repeated in this offline review;
metadata authority remains the independently reviewed citation ledger at
`ae25c56d17703ee00b8168eba33bbec77c688e72c8fb6ac520214e523241b808`.

The bound project-local originality manifest matches the revised manuscript.
A fresh conservative prose comparison found no copied abstract, paragraph,
caption, or table text against Papers 1--8 or the proposal.  Shared formulas
for the inherited cat matrix and its (p=5) Jordan calculation are
mathematical identities, not evidence of copied prose.  This remains a local
heuristic check, not an external plagiarism certificate.

The PDF metadata names `Anonymous Authors`.  Source and extracted PDF reveal
no author identity, affiliation, email, ORCID, acknowledgment, grant,
repository link, or filesystem path.  The manuscript's explicit disclosure
sentence does not itself identify an author.

## Independent build, font, figure, and visual QA

I copied the complete paper tree into two separate temporary directories and
ran the frozen build script independently in both.  Both builds produced the
same 15-page, 536,506-byte PDF at
`96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6`,
byte-identical to each other, the live `manuscript.pdf`, and
`paper_round1_revision.pdf`.  The two terminal LaTeX logs and BibTeX logs
were also pairwise byte-identical.

Post-build checks found:

- zero LaTeX, package, BibTeX, undefined-reference, undefined-citation,
  overfull, or underfull warning;
- 37/37 reported font objects embedded and subset, with no Type-3 font;
- zero raster image objects in the manuscript PDF;
- no `??`, `[?]`, `[VERIFY]`, placeholder, or TODO marker in extracted text;
- all three included figure masters present as vector PDF assets; and
- 15/15 rendered pages visually inspected.

The visual pass covered every theorem ending, equation, table, reference,
long provenance digest, and all three figures.  No overlap, clipping, missing
glyph, corrupt asset, or unresolved marker appears.  In particular, the
repaired Appendix-B C1--C9 table is legible with no stale X1/X2 row, Figure
3's standalone centralizer card/footer is clear, and Figure 1 visibly uses
the linear multiplicity scale described by the revised plan.

## Immutability and independence statement

Before and after review, I compared a sorted SHA-256 inventory of every file
under `code/`, `results/`, `experiments/`, and `notes/`; the inventories are
byte-identical.  The source lock, proof package, raw result, strict result
manifest, independent result review, and historical pre-review PDF retain
their recorded hashes.  I did not run the candidate or tests, enumerate a
new prime or composite shell, compute a centralizer, evaluate numerical
(s), (p^{-s}), or (log p), access prime or Riemann-zero data, or use the
network.  Apart from this Round-2 report, I changed no file.

## Findings and score

- **Critical findings:** none.
- **Major findings:** none.
- **Minor findings:** none.
- **Nonblocking provenance note:** the planning/source-lock claim IDs are a
  documented historical namespace; the final publication namespace is the
  C1--C9 map in Appendix B and `CLAIM_MANIFEST.json`.

The score remains limited by inherent originality and venue reach, not by an
unresolved defect.  Most orbit arithmetic is classical and the denominator
degree argument is elementary, so the work is best positioned as a
specialized negative technical note or companion audit.  Within that stated
role, its mathematical rigor, evidence firewall, reproducibility, and scope
discipline are excellent.

| Dimension | Score | Round-2 assessment |
|---|---:|---|
| Originality (20%) | 35 | Deliberately modest; direct collisions are fully disclosed. |
| Methodological rigor (25%) | 98 | Exhaustive exact proof with sharp mechanism boundaries. |
| Evidence sufficiency (25%) | 99 | One-shot exact controls, strict manifests, deterministic figures and builds. |
| Argument coherence (15%) | 97 | Arithmetic, semantics, obstruction, repair, and nonclaims form a clean chain. |
| Writing quality (15%) | 96 | Standalone, precise, and publication-ready after M1--M4 closure. |
| **Weighted total** | **85** | **PASS; specialized-note significance, terminal technical readiness.** |

## Final verdict

**PASS — MAY_FINALIZE.**  The exact revised source at
`fb54cb9273c89ad5f76a9485d67a815555050b3c71e630e47d367b043ae6e26c`
and exact revised PDF at
`96a560712ae7fb34e1d0ecfcd59e9b2c210ad61fe8ee0537c3a5ff5c860b4cd6`
have passed fresh independent Round-2 review.  No further manuscript,
figure, citation, source, code, experiment, or result change is required.
Finalization may copy and bind this reviewed PDF; it must not silently
substitute a changed source or rebuilt artifact.
