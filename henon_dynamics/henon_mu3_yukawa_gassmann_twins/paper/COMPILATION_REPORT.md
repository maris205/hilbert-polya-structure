# HCS-C59 compilation report

Status: **PASS; official final paper build; `PAPER_HOSTILE_PASS`; machine
layer `PREFREEZE_CODE_RESULTS_PASS` / `POSTREFRESH_PASS`; formal layer
`FORMAL_DOCS_PASS`; project `NOT_RELEASED`; I59 implementation commit
pending.**

## Build

- Engine: pdfLaTeX 1.40.22 (TeX Live 2022/dev/Debian) through latexmk 4.76.
- Command: `latexmk -C main.tex`, followed by
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
  main.tex`.
- Deterministic environment: `SOURCE_DATE_EPOCH=1786838400`,
  `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
- The raw PDF creation and modification timestamp is fixed at
  `D:20260816000000Z`.
- Exit status: zero.
- Two independent clean builds produced byte-identical PDF, stabilized log,
  bibliography output, and layout text.
- Authoritative integrated path: `paper/main.pdf`.
- Total pages: 27 A4 pages.
- Section 8 and Appendix A begin on page 18; references begin on page 26 and
  continue through page 27.
- File size: 503969 bytes.
- PDF SHA-256:
  `b0cfaf636cbc42613590a87b4e972d5ed47d82369a42f7c19257e7f1738a982a`.
- Final stabilized external LaTeX log: 43229 bytes; SHA-256:
  `7960319b25ca2a2e527538b0439d460bb2564910eb63034c9b0b4a3f60208d7f`.
- External stabilized `main.bbl`: 3372 bytes; SHA-256:
  `85e82cfc1a1597dc1d8fa13b8e0f7b2f36a3ab98c05b6dda384a2c3ed6fa7008`.
- External layout-preserving extracted text: 87196 bytes; SHA-256:
  `0204133c1fdde51005ebe596ff5fc8798aca92367a022f3f12a1378d4ea4ad50`.

No conference page limit is asserted. The paper uses a single-column
mathematical-article format. The in-tree PDF named above is the authoritative
paper artifact. The stabilized log, bibliography build output, extracted
text, improvement log, static audit, raster checks, and all other build or
review auxiliaries remain external. No claim of byte-for-byte invariance
across arbitrary output paths or TeX installations is made.

## Paper-source lock and 25-source ledger

- Source count: `25 = 24 TeX + 1 bibliography`.
- Intended live paper count at I59:
  `27 = 25 source + main.pdf + COMPILATION_REPORT.md`.
- Total source size: 96008 bytes in 2321 lines.
- I59 digest definition: SHA-256 of the `sha256sum` lines below, ordered
  lexicographically by the `paper/` project-relative path (not by the digest
  prefix) and including a terminal newline, evaluated from the C59 project
  root.
- I59 project-relative paper-source SHA-256:
  `184dbbdb1a5a732098e9926fb226eceea19690fb9e180285e904601818be22ed`.
- Independently hostile-reviewed final candidate aggregate:
  `125bc22581cd9b35a50c361be007b5b91cdc99ff490cf6165b7ab1fe0df766d3`.
  This is the SHA-256 of the same ordered digest lines with candidate-relative
  names (`main.tex`, `figures/...`, and `sections/...`) rather than their
  future `paper/` prefixes. The underlying 25 file digests are identical.

```text
98a21e7553e78b6775ee30662aac7c5e92a3e4c3e876b71b164b45a511cbc115  paper/figures/c59_figure_data.tex
fb192c26407c16694e443679f182e61a5fa5916bd62cb8cb214af09d5d3c78b6  paper/figures/figure_proof_dependency.tex
4e30138c7a6df525f0df0c08161e1895135d44d970e87d2ac60d7cb86b8fd4e8  paper/figures/latex_includes.tex
e1f3761e585b4936a451b5d76da3cde62cddf887ce3979a82d31481d68b0bfc1  paper/figures/proof_dependency_tikz.tex
8d23d234ef9f7863cb21eae6ef05763ea6285a5575396251a14dac5e337605b3  paper/figures/table_hero_comparison.tex
ab144dbe3f532d0736e0a4eb97b9bc77e564a9abbe6ff83113a2bda8ae03f115  paper/figures/table_local_tom140.tex
b0b59aae3656c79f2354e5991dc240a40cd30c79c7634baa56861e9acfb0c9ae  paper/figures/table_local_tom206.tex
1663f9120d7f96a7e3d3d20cdd8ef1573b57fa4f942b71e44b4fe501e0db0ce0  paper/main.tex
376ab609edef45149aef4e0dc5edca2a3dc9c57a9c44546cd82c3e48814e7bf4  paper/math_commands.tex
37e41c5dc49066e8d7b8d767218326816d2cb2ecbdfa1b1dd2e72e890ca0e1d4  paper/references.bib
4a5fc8897cd55607317123226c9a34bc3978c71f5dce794c975cc04120dbe8d2  paper/sections/0_abstract.tex
e08a6acb2f5422d80a332cdd2f581410e43bae4c644d99b4e2ffabfd71250a14  paper/sections/1_introduction.tex
a3eb7e96d603e0009cc406d9127ded6687aac62e67111866a6a0e75cbe9b832b  paper/sections/2_prior_input_definitions.tex
12d4edd25d664a4d1972906c0f7fd464855d764525c89c1a303b0e3f7b828036  paper/sections/3_primitive_resolvents.tex
bddaeee11d03576ebedd2d422a1d8caa51500096c7306243b4617e3bfb5e1f54  paper/sections/4_gassmann_fields.tex
c91e9794a44d10b77fa492c7aa8f13695c75e21de865cbcdf5395588c2fe2a73  paper/sections/5_global_arithmetic.tex
5232c30b2872896f300266abc28a0afc3cb550df52f171797f42300000869c2d  paper/sections/6_local_branches.tex
da2e9edebc7531b50c7f4f4eba510cfa4b8eb06ee337650e51a038810257799d  paper/sections/7_reproducibility.tex
61f759ccc6fd86172f9c2a9609dba1059d5168abba0da3938b4d50a983737337  paper/sections/8_scope_conclusion.tex
311f806f6515625ce61a95752845f462cebf0585093a50aaa0c2f0bbc5b3cfc7  paper/sections/A_split_graph_certificate.tex
fb6618820ad99747072981d8da45354e4ae84e0e7cd7b8ade22d452a5b73cc3c  paper/sections/B_gassmann_audit.tex
6824d83d218781b941306e4459d2e03da36620360394350447973e18d174baea  paper/sections/C_global_ledger.tex
1769a4b283cd774c5ae143c03eae866b681d678f787070ac1fc82a9477ad8bea  paper/sections/D_local_ledger.tex
0fcbc4e14f91a0d64bbe91414e9488c94ff639a9a0c0ae76e01795fbcc779ecb  paper/sections/E_reproducibility_ledger.tex
f8cfffe0f93b003cc49a4d41d9494f33520e1a5b4c63d6f43ac5f84b314e5381  paper/sections/F_source_scope_ledger.tex
```

No paper-source byte changed during either final clean build. The external
`PAPER_IMPROVEMENT_LOG.md` and `STATIC_AUDIT.md` are process records, not
paper-facing source files, and are excluded from the I59 paper inventory and
every release manifest.

## Automated checks

- Undefined citations: 0.
- Undefined cross-references: 0.
- pdfTeX warnings: 0.
- LaTeX warnings: 0.
- Package warnings: 0.
- BibTeX warnings: 0 (`warning$ -- 0`).
- Duplicate PDF destinations or multiply defined labels: 0.
- Overfull horizontal or vertical boxes: 0.
- Underfull horizontal or vertical boxes: 0.
- PDF-string warnings: 0.
- Missing-character diagnostics: 0.
- Rerun requests: 0.
- Fatal or engine errors: 0.
- Stale section files: 0; all 15 files in `paper/sections/` are input by
  `paper/main.tex`. Six figure/table sources are reached by the build graph;
  `paper/figures/latex_includes.tex` is the exact release-ledger convenience
  include for those inputs and is intentionally not itself input by
  `paper/main.tex`.
- Static source inventory: 68 label declarations, all unique; 78 literal
  reference commands resolving to 87 targets; 28 citation commands over
  exactly 11 bibliography keys; and 118 balanced environment pairs.
- Bibliography: 11 entries, all cited.
- Tables 1--10 and Figure 1 are present and numbered continuously.
- Text extraction: PASS, with 1273 lines, 11193 whitespace-delimited tokens,
  and 87196 bytes.
- Layout-text SHA-256:
  `0204133c1fdde51005ebe596ff5fc8798aca92367a022f3f12a1378d4ea4ad50`.
- Residual `TODO`/`FIXME`/`XXX`/`[VERIFY]` markers in extracted PDF: 0.
- Literal `??` or `[?]` placeholders in extracted PDF: 0.
- Anonymous-name, affiliation, address, email, ORCID, acknowledgement,
  repository-path, `/root`, or `/tmp` leakage in extracted PDF: 0.
- Ghostscript null-device parse: PASS.
- Raster images in the PDF: 0.
- Nonblank pages: 27/27.
- Generated auxiliaries admitted to `paper/` at I59: 0.

## Exact machine and formal locks

- Machine status: `PREFREEZE_CODE_RESULTS_PASS`.
- Independent post-refresh hostile machine audit: `POSTREFRESH_PASS`.
- Exact gates: G0--G7, 8/8 pass.
- Independent checker status: `PASS_PREFREEZE_CODE_RESULTS`.
- Payload leaves: 10412.
- Rejected systematic certificate mutations: 20894.
- Rejected self-consistent evidence rebounds: 8.
- Project-local tests: 48 passing.
- Strict-parser negative cases: 15.
- Machine inventory: 13 code files and 8 result files, or 21 live files;
  the self-excluding scoped machine manifest binds the other 20 entries.
- Payload SHA-256:
  `a6428addfb14f00f3ed45781d9ba0944be177cfb7c257c958e7fa538fcaf366b`.
- Payload-shape SHA-256:
  `788aa5e58d51f0d4edfa7a4e58de5748bd5a1ad1d28445d91045d5dd72c850d2`.
- Certificate SHA-256:
  `3c4c756d912d49653353503701f5b8be412d0da53383ac9c9830b6e7a953ed9a`.
- Schema-file SHA-256:
  `07a817bb2eade24862f0cf4dca8d1d0248eb4f473a137c07bd0200efeea8c6b4`.
- Canonical-schema SHA-256:
  `b049dbd8f69d57eef38babbdc6da78a07ef0baf60939e8ea516ca35af96e8795`.
- Independent-check SHA-256:
  `271d0123b170bef1317b63e97e3f679179b6e794185b78facd571150ba2123d3`.
- Independent-replay-summary SHA-256:
  `6c659e70e4e3c0e6a4209371faef5e3663926f95b98fdf807b676c729956025b`.
- Group-evidence SHA-256:
  `0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958`.
- Resolvent-evidence SHA-256:
  `667e0eeb04e5724b620bf513f9556a321dfd39f9215396ed1840ca83879ec6a6`.
- Scoped machine-manifest SHA-256:
  `c4145ea23b57b1adcd8cfddb18c41c703e93ca8a6f84eeecb9457e0f4e046dda`.
- Formal-document audit: `FORMAL_DOCS_PASS`.
- Frozen 13-root-Markdown formal aggregate:
  `4772e25d5191ccf961d9408c5a91b717ca9d610fa12457cdf6c4025718d4c6bb`.
- Incoming pre-paper Route SHA-256:
  `026a5f6d69be8588a60fb3aae10823f589d6befd26dc1f72a2d84d9c890f9925`.
- Incoming pre-paper Batch SHA-256:
  `19797e7209f9551b967018323f930569d4fda9ca1f3b4e8e5106ac4bfb1d93f2`.
- Neither the 21 protected machine files nor the 13 frozen formal Markdown
  files is rewritten by the paper build or by I59 paper integration.

The scoped machine manifest remains the exact machine-lane identity. It is
not the pending full-project release manifest. The machine and formal layers
may retain their intentional historical `PAPER_PENDING` prose; this report
is the successor paper-state record. The incoming Route and Batch digests
record the pre-paper handoff and are expected to acquire new external digests
when their I59 paper-state prose is updated.

## PDF checks

- `pdfinfo` parses the file as an unencrypted PDF 1.5 with 27 A4 pages, no
  forms, no JavaScript, and no suspect objects.
- Title, author, subject, and keyword metadata fields are intentionally blank;
  the rendered author/running-head text is `Anonymous Authors`.
- All 30 fonts are embedded, subsetted Type 1 fonts with Unicode mappings.
- No Type 3 font occurs and no raster image is embedded.
- Ghostscript parsing and complete page-by-page visual/layout inspection pass.
- The independent hostile paper review returned `PAPER_HOSTILE_PASS` with
  zero blockers after rebinding all 25 sources, the PDF, stabilized log,
  layout text, bibliography output, exact machine artifacts, formal package,
  primary-source locators, and visible mathematical claims.
- The five-clause integrated theorem is uninterrupted by floats. The hero
  table, proof-dependency diagram, Tables 1--10, both local-branch tables,
  exact artifact ledgers, thirty-leaf scope ledger, and references are
  complete, legible, unclipped, and text-extractable.

## Mathematical and scope checks visible in the paper

- The exact 20-term cubic surface agrees term-for-term and in order with the
  released C56 coefficient carrier. The C56 and C58 commits, certificates,
  full-project manifests, and the promoted C59 evidence hashes are exact.
- The characteristic-zero roots `d_i` and `alpha_i=L*d_i` are distinguished
  from their reductions modulo 692717: paper label `i` corresponds to
  zero-based resolver-array index `i-1`.
- The six exact subgroup generators, subgroup invariants, and the complete
  `27+27` and `81` support arrays agree element-for-element with the promoted
  carriers. The support stabilizers are exactly `H_+` and `H_-`; both
  split-prime orbit products have 320 distinct values and the certified
  modular coefficient hashes.
- The certified degree-10 line-intersection graph is explicitly distinguished
  from the conventional 16-regular skew-line Schlaefli complement; both have
  the same full 51840-element automorphism group in the released labelling.
- The paper claims exact monic integral product-form minimal polynomials but
  prints no expanded characteristic-zero degree-320 coefficient list.
- The complete 350-class character grouping, eleven collision buckets,
  unique index-320 minimum, full permutation-character equality, trivial
  cores, common normal closure, field nonisomorphism, and Dedekind-zeta
  equality agree with the promoted certificate.
- Both fields have signature `(16,152)`, signed discriminant
  `+3^624*5^496*A^192*B^160`, and the exact eight-prime ramified support.
- Every ToM-140 and ToM-206 `(n,e,f,d)` row, multiplicity, factor count,
  degree total 320, different total 624, subgroup chain, and local separator
  agrees with G5/G6. Both decomposition-group branches remain retained and
  unselected.
- In the ToM-140 branch, `F_+` has eight degree-one factors and `F_-` has
  none. In the ToM-206 branch, `F_+` has four unramified quadratic factors
  and `F_-` has no degree-two factor. This proves nonisomorphic finite etale
  `Q_3`-algebras in either retained branch and therefore nonisomorphic adele
  rings; the `(n,e,f,d)` tuples are not promoted as complete classifications
  of the individual high-degree completions.
- All thirty promoted Boolean-false scope leaves occur exactly once in the
  source ledger. `NO_BAD_EULER_OR_ROOT_NUMBER` remains literal: the paper
  claims no decomposition Frobenius, bad Artin Euler factor, epsilon factor,
  root number, Artin holomorphy, automorphy, analytic continuation, or
  functional equation.
- The paper also claims no integral permutation equivalence, ring-of-integers
  or class-number equality, integral basis, monogenicity,
  polynomial/field-discriminant equality, rational point, Hasse principle,
  weak approximation, Brauer--Manin obstruction, motive, RH, or
  Hilbert--Polya operator.

## I59 release boundary

- Paper compilation status: `PAPER_COMPILED`.
- Independent paper audit status: `PAPER_HOSTILE_PASS`.
- Machine status: `PREFREEZE_CODE_RESULTS_PASS` / `POSTREFRESH_PASS`.
- Formal-document status: `FORMAL_DOCS_PASS`.
- Project release status: `NOT_RELEASED`.
- I59 implementation commit: **pending; no hash is guessed here**.
- Full-project release manifest: not created; pending.
- Release archive: not created; pending.
- Promotion authorization: false.

This report records the official final paper build and the evidence available
for initial I59 paper integration. It contains neither its own digest nor any
I59 live-Route digest, archived-Route digest, full-project-manifest digest, or
I59/P59 commit identity. Those acyclic successor identities remain external
and may be populated only after the corresponding artifacts exist.
