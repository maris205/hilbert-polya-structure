# Paper 8 independent final release audit

**Audit date:** 2026-08-14 18:05 CST (UTC+08:00)  
**Audit role:** independent ARS integrity, formatting, reproducibility, and
public-package reviewer  
**Verdict:** **PASS**  
**Open findings:** **0 Critical / 0 Major / 0 Minor**

This verdict attaches only to the exact byte locks below.  Any change to the
manuscript, bibliography, native figure sources, release PDF, release READMEs,
control manifest, or Stage-8 Route records reopens the affected audit surface.
The public Git synchronization must repeat the zero-source-PDF index check in
the actual clone immediately before commit; the local package simulation in
Section 8 already passes that rule.

## 1. Exact final release lock

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa` |
| `paper/references.bib` | `a0d3300c8f7cc093db47e8339adcc079f3d2a993d68d862a37e8d1d79cf0f35e` |
| `paper/figures/owner_map.tex` | `b1978bcd5f37cb470096f36b3f05c7a5bc4abf30001b417d8eda5094bd54a34d` |
| `paper/figures/character_filter.tex` | `6405ba10b414dfebc5d25811d26b71f3cccccd07f554ce56ee83af55061e72a7` |
| `paper/paper.pdf` | `fad0f602edf4d2300b91bd7b356e363da3ab776c645288a14f39ae171aea262a` |
| `paper/README.md` | `b81badeaf10747d819b8422843834e931f2e54ff6551f3a4b3465b4f5f658dcf` |
| project `README.md` | `2f50c26a67f3c1ecd6c641b6947ed45599768c978fa2397a2fe27ddfb1dd285b` |
| `results/isotropy_trace_manifest.json` | `20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07` |
| `notes/stage8_summary_zh.md` | `4aede4aaac2161350786a1c29991565c569d0d3bd41ad6769ba6ec5a2c618771` |
| `notes/peer_review_round1.md` | `02bb7301376aa5b3644a6796c62b870b36b6f6825b085f47ee121bc5ab17b4a7` |
| `notes/citation_audit.md` | `69a27c8b8d450c180d294714aa18c6715220bdf8b8aef92724576dd0ecf18fbf` |
| `notes/sources/.gitignore` | `0e1f5f5c4eed19b8f2cb1463087d8b93d34dfcc855101a746c7c2fa94ec26c84` |
| `notes/sources/README.md` | `0e092f6dee031c1615079985cf490fcdf489af053c8a70e0c65d048e8e302762` |

The final independent manuscript review and citation audit both return
`ACCEPT` on these same manuscript, bibliography, figure, and PDF bytes.  No
review decision was transferred across a byte change.

## 2. Clean-room LaTeX rebuild

The four release sources (`manuscript.tex`, `references.bib`, and the two TikZ
files) were copied to a newly created directory outside the release tree.  The
document was rebuilt there using the documented sequence:

```text
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex paper
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
```

The final pass completed successfully.  It contains:

- zero undefined citations or references;
- zero BibTeX warnings;
- zero LaTeX errors or undefined control sequences;
- zero overfull boxes;
- zero missing-glyph messages; and
- exactly two retained underfull boxes: badness 10000 at source lines 93--95
  and badness 1038 at lines 148--149.

The clean rebuild has 19 A4 pages and SHA-256
`90b0514a2407a740effd4447ac6ad88ffee851385337ce555e84fdf5a938c32a`.
Its raw PDF hash differs from the release PDF because `xdvipdfmx` writes the
build time into the container (`CreationDate` and dependent container bytes).
This is not visible-content drift:

| Equivalence test | Result |
|---|---|
| default `pdftotext` | byte-identical; SHA-256 `1dd6a3a3730912aa6d23b4b3ec3fde74ed16a2a34d546389f0a23f4efac61c5d` |
| `pdftotext -layout` | byte-identical; SHA-256 `333a501f499b42d141269bee7048f350a5f8442b65dd27921af7fa4ad7433e91` |
| 120-dpi PNG raster, pages 1--19 | `19/19` page files byte-identical by `cmp` |

The release-to-rebuild page-raster locks are:

| Page | SHA-256 | Page | SHA-256 |
|---:|---|---:|---|
| 1 | `132ce48336d156fd0962f9c5ad715bd2f3fb956eabe33538762174193cba9585` | 11 | `093a0254eeef282e57b1515f79867e9316b0a195e809a6c` |
| 2 | `af52c6270b534b137cdb18b9b67aba21b41a001055353c548673a5c4c13814e6` | 12 | `bfa4eec887529f1eb8d640d4b2902e3d87de586f51605954568d01c49cce4109` |
| 3 | `ff38764aa388876bfc9a05cc13afece9f42efb8e413592198f2a68cdadcbc6b4` | 13 | `1ae3101554d8854e410607edddd0f1dc8b5bd7b246c83bd6cb5da3a439d0b2da` |
| 4 | `2feab3a7ae823658a424484dbca5de8874ae149630e69b0d1655215c9792f475` | 14 | `4cc03e912b5adb92ee24b6c79558cf6928c73cc44843dc72d7fcadedae34f5c0` |
| 5 | `b355bb2deeb789c703f43d3b77d3c28f364b4c934388b3c9ae33a373c608e88a` | 15 | `bdf6eebe45b30a64c02f2b30c6eaf9c4772bfc2438525ab3a305a2cba1e690f8` |
| 6 | `8d6f0ef78fbdaaaa91de5331381fd841cb5e59b0966a38fd764be94e05d180eb` | 16 | `c6782bcd6abec3ca2322107f0c5ce1651b570542538bf71c79b26be5e3e6f2f4` |
| 7 | `ee1bf7b7358fb561133e7946a980ef3e5a184ed823d3702333cbe58fce55376d` | 17 | `c62a84767d25597915c3ba938c5c706381766217c1405c17e262616943f9a7ef` |
| 8 | `2b959f740d7571a8e0a8f1f488ae759e8e27bb9ef09963a5a081b7476c0e5059` | 18 | `d7469c4d1cbf4598ad8172ae3b400dc5b5eae8b25319a24ed7aab3d50befdc40` |
| 9 | `8dc6a7e1c0174f912345146efb0c110e3d992b7b0cb3032f7cd963ab40679210` | 19 | `2f111a327cc1ddd76c2852daeba37f0e6aea20c0ca68286047cb3214e91269f1` |
| 10 | `19e7bfbabb64cff873407855a71ada66d149409fab7c3a4aa8d9fa92788ba3c6` |  |  |

## 3. PDF metadata, fonts, text, and layout

`pdfinfo` reports the expected title, author `Liang Wang`, subject, and
keywords; 19 pages; A4 media size; zero rotation; no encryption, form,
JavaScript, or suspect flag; and PDF version 1.5.  The release PDF is 191,048
bytes.

`pdffonts` reports seven used font subsets.  Every row has `emb=yes`,
`sub=yes`, and `uni=yes`.  The used families are TeX Gyre Termes regular,
bold, and italic; TeX Gyre Termes Math; Noto Serif CJK regular and bold; and
TeX Gyre Cursor.

All 19 release pages were rendered and visually inspected.  No clipped text,
equation, table rule, figure edge, footer, URL, or bibliography line was found,
and no text/figure collision was found.  Detailed checks included:

- page 1: title, author metadata, email, English abstract/formula, independent
  Simplified-Chinese abstract, and page footer;
- pages 4, 6, 11, 13--15: all six tables, long identifiers, theorem blocks,
  formulas, and Route tuples;
- pages 7 and 9: both native TikZ figures, captions, colour labels, equations,
  and surrounding text;
- pages 16--17: appendices, dense formulas, declarations, and AI/source
  disclosures; and
- pages 18--19: all 14 rendered bibliography entries and long URLs.

The 19/19 release-to-clean-build raster equality, clean no-overfull log, and
two independent text-layer comparisons provide the mechanical all-page
cross-check.  The visual inspection is a human-readable rendering check, not a
formal proof that every possible PDF viewer renders fonts identically.

## 4. Citation and source integrity

The source contains 14 unique citation keys and the bibliography contains the
same 14 unique records.  There are zero cited-but-missing keys, zero
bibliography-only records, zero duplicate keys, and zero unresolved citations
in the final build.  The final citation audit independently verifies all 14
manifestations, locators, and metadata records and records no remaining
citation or claim-strength finding.

The abstract hierarchy and main claims agree across the English and
Simplified-Chinese abstracts:

- packet completion/bridge: `NOT_TESTABLE`;
- fixed chosen one-orbit normal extension: `REFUTED`; and
- positive-time coefficient-one scalar Radon ledger: `PASS`.

The manuscript contains the required data/code, ethics/consent, author
contribution, competing-interest, funding, generative-AI, source/citation, and
acknowledgment declarations.  It does not claim a determinant, A3/A4 credit,
Route B, a global all-prime operator, or a Hilbert--Polya construction.

Theoretical-paper failure-mode audit:

| ARS failure mode | Final status | Evidence |
|---|---|---|
| implementation bug | CLEAR | 18 tests pass in an isolated copy; manifest verifies code and active-lock hashes |
| hallucinated citation | CLEAR | 14/14 key closure plus independent manifestation/locator audit |
| hallucinated experimental result | CLEAR | no empirical result is claimed; every finite control is regenerated from disclosed deterministic code |
| shortcut reliance | CLEAR / not applicable | no learned model or performance generalization; generic-clock and copied/composite falsifiers are disclosed |
| bug reframed as insight | CLEAR | theorem ownership is symbolic; controls are explicitly denied proof credit |
| methodology fabrication | CLEAR | reproduction entry point, code, tests, CSVs, hashes, and domains agree |
| early frame-lock | CLEAR | packet/local/scalar owners and stop conditions remain separate throughout both abstracts, theorem tables, and Route records |

No professional plagiarism service or proprietary full-corpus similarity
database was used by this release audit.  Its originality assurance is limited
to the documented source/claim audit and search-bounded novelty record; a venue
may still require an iThenticate/Turnitin-style submission check.

## 5. Deterministic control package

The complete `code/`, `experiments/`, `results/`, and required lock files were
copied to a second temporary tree before execution.  Running
`./experiments/reproduce.sh` there gave:

- `18/18` unit tests passing;
- nine CSV artifacts with 129 data rows;
- manifest, active-lock, artifact, and implementation hash verification;
- two fresh generations byte-identical to one another and to the locked
  artifacts;
- no network, randomness, fitting, external dataset, or target-zero input;
  and
- no `__pycache__` directory or `.pyc` file.

The regenerated manifest retains SHA-256
`20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07`.
The actual release tree contains no LaTeX auxiliary, log, synchronization,
Python bytecode, or cache artifact.  Its `paper/` directory contains only the
six files expected by the release inventory: `README.md`, `manuscript.tex`,
`references.bib`, `paper.pdf`, and the two native TikZ files.

## 6. Stage-8 Route lock

All five YAML files parse successfully.  Their `candidate_id` matches the
directory name, every `overall_verdict` is `ROUTE_A_EXPLORATORY`, every
`route_b_invocation_allowed` value is Boolean `false`, and every record has
`A2_FAIL / A3_FAIL / A4_FAIL`.  There is no Paper-8 Route-B YAML.

| Record | Exact tuple | YAML SHA-256 |
|---|---|---|
| `DEN-EF-PACKET-ACTION-GRPD-P` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `28da284cd0f1be601ded15a24281a5b07937df1fd29ba8551cbf2ab9f6f9d0ee` |
| `DEN-EF-ORBIT-ACTION-GRPD` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `17defc7c1ec088e4aab5b256ec4ee19a6df126d1d3c76b86f191d3c76f5b77b9` |
| `DEN-EF-ORBIT-GRPD-REG-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)` | `51903590ba183daa54029c7977c1a0ba5c2550cf6e685d18ec2a9bb64d5fa333` |
| `DEN-EF-ORBIT-GRPD-TRIVCHAR-TRACE` | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `ddade81079ca04fcb652b0fe2810e081775afdb674c83d72c5c0844e61077e1d` |
| `DEN-EF-GRPD-TIME-RETURN-POS` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `d42df1d6dd699665e918efac61d24a38b500c4d7a3e771ef87761fd89616c22a` |

The YAML tuples agree exactly with the manuscript, Route audit, project
README, and Chinese stage summary.  No coordinate is spliced across owners.

## 7. README and inventory consistency

Both release READMEs point to the canonical `paper/paper.pdf`, state 19 pages,
record the exact release PDF and control-manifest hashes, document the
XeLaTeX--BibTeX build, describe the two harmless underfull boxes, and preserve
the packet/local/scalar claim hierarchy.  Their five release-file hashes match
the files on disk.  Neither README authorizes redistribution of retained
source PDFs.

The `paper/` release inventory has no obsolete `manuscript.pdf` and no build
auxiliaries.  The only manuscript figures are the two audited native TikZ
sources; the manuscript imports no external raster or vector figure.

## 8. Public source-PDF exclusion gate

The retained source directory contains 19 local research PDFs and 19
same-stem preflight sidecars.  Citation reproducibility does not grant
redistribution permission.  The directory-level `.gitignore` contains the
default rule `*.pdf`, and `sources/README.md`, the project README, and the paper
README all state the local-only policy.

An independent temporary Git repository was initialized around a byte copy of
the complete Paper-8 project.  After `git add 8-isotropy-trace`:

| Check | Result |
|---|---:|
| local `notes/sources/*.pdf` files | 19 |
| ignored source PDFs reported by Git | 19 |
| source PDFs in `git diff --cached --name-only` | **0** |
| source PDFs in `git ls-files` | **0** |
| staged preflight JSON sidecars | 19 |
| staged source-directory non-PDF audit files | 25 |
| staged build auxiliaries / `.pyc` / `__pycache__` | **0** |

This closes the citation audit's public-package condition for the package as
constructed.  Because the working research directory itself is not a Git
worktree, the actual GitHub synchronization must run the same two zero-count
commands in the fetched destination clone before commit.  If either command
finds a source PDF, this verdict automatically changes to **REVISE** until the
PDF is removed from the public index or an exact-manifestation redistribution
licence is documented.

## 9. Final decision and disclosed limits

**Release decision: PASS.**  The exact release is reproducible at the visible
and extracted-text levels, all 19 pages are stable and legible, fonts are
embedded, citations close, controls reproduce, Route records agree, and the
public-package simulation excludes every retained source PDF.

Disclosed limits are narrow and non-blocking:

1. raw PDF bytes are time-dependent even though both text extractions and all
   19 raster pages are byte-identical;
2. PDF visual review cannot guarantee identical rendering in every third-party
   viewer, although embedded Unicode fonts and clean rasterization strongly
   reduce that risk;
3. no proprietary plagiarism database was available; and
4. the destination Git index is external state and must be rechecked after
   the actual fetch/sync, immediately before commit.
