# C417 author handoff

Status at 2026-09-07 02:26 UTC: **COMPLETE AUTHOR MANUSCRIPT AND PDF;
READY FOR NONAUTHOR MANUSCRIPT REVIEW**. This is not the final
deterministic release, a formal Route A evaluation, or a manuscript
review PASS.

## Deliverable and exact mathematical contract

- [main.tex](main.tex), shared macros, ten included section files
  (abstract, eight main sections, complete certificate appendix), and
  [references.bib](references.bib): 1,246 source lines in total.
- [main.pdf](main.pdf): **17 pages**, 392,206 bytes, copied from the
  actual author output in build_author/main.pdf.
- [Citation audit](CITATION_AUDIT.md): exactly five cited entries,
  including C412 explicitly as a non-journal repository manuscript.
- Complete extracted [PDF text](build_author/main.txt), all three
  actual compile transcripts, final engine log and BibTeX artifacts
  remain in build_author/.

The unchanged theorem is for all a,b,c in Z, leading coefficient +1,
H_f(x,y)=(y,f(y)−x), determinant +1, all Q², ordinary iteration,
unit-weight points and no reversal quotient. It gives all seven
word/coefficient templates, least periods 1,2,3,4,6, per-cycle three
symbols, sharp total eleven points and the entire integer-translation
equality locus. The ordinary finite-cycle zeta is only a corollary.

## Proof placement

| Obligation | Actual manuscript location |
|---|---|
| Entire periodic-set finiteness before taking its global extrema | Section 3, Lemma 3.1 and normalization (5) |
| Integral secant slope/root and the bound by twice the diameter | Lemma 3.2, equations (6)–(8) |
| Empty, one-symbol, diameter-one and affine-root/parabolic cases | Section 3 and Lemma 3.3 |
| Complete large alphabet, reflection and strict no-cancellation threshold | Section 4, Lemmas 4.1–4.2 |
| All ninety symbolic graphs and every endpoint-using pattern | Proposition 4.3, Tables 3–4, Appendix A.3 |
| Four global coordinate values coexist; endpoint filter is only necessary | Remark 4.4 and the paragraph immediately following |
| Complete finite input ranges and fourteen diameter rows | Section 5, equations (13)–(17), Table 5 |
| Full traversal, exact range loops, maxima/equality updates, period and symbol counts | Appendix A.1–A.3; no code link substitutes for it |
| Seven templates, reciprocal lemma, six-word exhaustion and all converses | Table 1 and full Section 6 |
| Unique maximizing graph, every translated equality coefficient and eleven explicit points | Section 7, equations (18)–(19) |
| Primary-source deductions, non-journal predecessor, and source/target limits | Sections 2 and 8; CITATION_AUDIT.md |

All tables and proofs are typeset. No diagram was needed. There is no
coefficient experiment, new candidate, sixth paper or altered contract.

## Frozen research inputs

The author read the complete proof, source audit, nonauthor review and
producer code without executing the frozen code. The historical author
status in the frozen proof is superseded by the separate admission
review; it was not silently rewritten.

| Input under ../../cubic_arithmetic/ | SHA256 checked during drafting |
|---|---|
| PROOF_PACKAGE.md | d7288267e81a6389f1e71e4999cdc3c1056b754bb22a816b050253422e1f753f |
| SOURCE_AUDIT.md | 88ef8a0a48eca376c1c4749e11142519b9268901199888699640f7d6b81545d7 |
| REVIEW_CUBIC_ROOT.md | f924db223d9cf050232084712db7c87e7e94301440c80d630579393e225aa5c2 |

The previous independent checker reconstructed all finite tables by
a different periodic-vertex isolation method. Its accepted receipt is
in that review. No producer, author cross-check, independent checker,
old mathematical script or previous batch build was rerun during
this manuscript task. The appendix is a readable transcription of
the exact finite procedure, not a newly claimed execution.

## Actual author build

Working directory: this C417 manuscript directory.
The build_author/ directory was newly created for this task; no old
directory was cleaned. Each of three invocations used bash pipefail and:

    SOURCE_DATE_EPOCH=1788739200 FORCE_SOURCE_DATE=1 TZ=UTC \
      latexmk -pdf -outdir=build_author -interaction=nonstopmode \
      -halt-on-error -file-line-error main.tex 2>&1 \
      | tee build_author/compile_attemptN.log

Here N was actually 1, 2 and 3, respectively. All three invocations
exited **0**. The first fresh invocation ran LaTeX/BibTeX to stable
references and produced a 17-page PDF. Its four underfull boxes were
in the source-comparison table; ragged-right paragraph columns removed
them in attempt 2. PDF-text inspection then prompted three compound-word
line-break repairs, a six-cycle parameter line break, and a clearer
distinct-pair explanation; attempt 3 compiled those affected inputs.
No additional author build was run after the final checks.

Environment reported by the actual logs: latexmk 4.76, pdfTeX
3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian, LaTeX2e
2021-11-15 patch level 1, BibTeX 0.99d. The final PDF is letter
size, PDF 1.5, unencrypted, with anonymous visible author block and
no identifying author metadata. The metadata time reported by
pdfinfo is 7 September 2026 08:00 CST; the requested fixed epoch
and build variables are recorded above without claiming a two-build
byte comparison.

## Checks actually completed

- Read all actual TeX and Bib files; checked the final affected edits.
  The ten section files are all included by main.tex; no orphaned
  section source is present.
- Read the full 17-page extracted PDF text, then reread the final
  affected front-matter/template passages. The bounds, signs, ordinary
  orientation counts and every table were checked against the frozen
  proof and independent review.
- Final main.log and main.blg contain **zero** warning, underfull,
  overfull, undefined-reference, undefined-citation or error matches.
  The final no-match ripgrep status is 1, its normal no-match result,
  not a compilation failure. Earlier transient reference warnings
  remain honestly in the first complete transcript.
- PDF-text marker check found no unresolved-reference/citation markers,
  TODO/FIXME/XXX or verification placeholders. All five citation keys
  match the five bibliography entries; no unused entry was retained.
- All **20** listed font objects are embedded Type 1 fonts; no Type 3
  font is listed.
- Actually viewed rendered pages **2, 3, 7, 15 and 16**, covering the
  template/comparison/symbolic tables and both main enumeration
  listings. No clipping or overlap was found. These are selected-page
  author checks, **not** the required final every-page visual review.
  The five rendered images are retained in build_author/visual-*.png.

## Output identities at this handoff

| Artifact | SHA256 |
|---|---|
| main.pdf and build_author/main.pdf | 0615b9fb914114f8acc8aa37631a1c946862f3e245529334b62f6f64e2c21313 |
| build_author/main.log | ef5d78d70996e12020a570679ddeb2aa55f58a4bc44f18f3bcfdad642097fb4d |
| build_author/main.txt | 291983798334a7dc6a6073ad585235f6af3e0b214fea33aaf73c04dc4a776890 |

These are author-output identities, not final release hashes.
The main body including limitations ends on page 13; Appendix A is
pages 14–16; references are on page 17. No page quota or journal
submission format was imposed.

## Scope of completion and pending gates

No unresolved author-side mathematical or citation issue was identified.
The exact finite certificate remains a computational part of the proof,
not a hand-classified or proof-assistant certificate. Global-priority
uncertainty remains explicit.

The coordinator still owns nonauthor manuscript adjudication, formal
pinned evaluation, two fresh final deterministic builds, every final
page's visual inspection, the release ledger/manifest, global indexes
and Git integration. No such gate is marked complete here.

The writing skills influenced the explicit claim/evidence map,
front-loaded all-family theorem, complete in-PDF proof dependency
chain and source-access limitations. Their legacy conference page
quotas and external-model defaults were overridden by the frozen
anonymous-article/current-team batch instructions.
NO_BAD_EULER_OR_ROOT_NUMBER remains unconditional.
