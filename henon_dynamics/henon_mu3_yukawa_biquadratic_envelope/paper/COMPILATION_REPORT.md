# HCS-C60 compilation report

Status: **PASS; official final paper build; `PAPER_COMPILED`;
`PAPER_HOSTILE_PASS`; machine layer `PREFREEZE_CODE_RESULTS_PASS` /
`POSTREFRESH_PASS`; formal layer `FORMAL_DOCS_PASS`; project
`NOT_RELEASED`; I60 implementation commit pending.**

## Build

- Engine: pdfLaTeX 1.40.22 (TeX Live 2022/dev/Debian) through latexmk
  4.76.
- Command: `latexmk -C main.tex`, followed by
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
  main.tex`.
- Deterministic environment: `SOURCE_DATE_EPOCH=1786924800`,
  `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
- The raw PDF creation and modification timestamp is fixed at
  `D:20260817000000Z`.
- Exit status: zero.
- Two independent clean builds in distinct temporary directories produced
  byte-identical PDF, stabilized log, bibliography output, and layout text.
- Authoritative integrated path: `paper/main.pdf`.
- Total pages: 26 A4 pages. References begin on page 17; Appendix A begins on
  page 18; the final page is page 26.
- File size: 655516 bytes.
- PDF SHA-256:
  `6a418f2b10a24c072c3097921a54cf60bf1bd73c63ab60d2e434b8ec9c8624c2`.
- Final stabilized external LaTeX log: 48639 bytes; SHA-256:
  `dcb879d4d374bf5364b92249dfcfa8434e9ddc9b8b92f7077352cb988cce94c7`.
- External stabilized `main.bbl`: 2571 bytes; SHA-256:
  `290d839ca0a2773fa7380a619282ba663f224fc51761f4a79abbe0d7b5b1df48`.
- External layout-preserving extracted text: 90755 bytes; SHA-256:
  `4aea5c3b3cdfa247869d07dbe0f0aa41bbf389161835eac48b4fff9202a71c36`.

No conference page limit is asserted. The paper uses a single-column
mathematical-article format. The in-tree PDF named above is the authoritative
paper artifact. The stabilized log, bibliography output, extracted text,
rendered inspection pages, static checks, font inventory, Ghostscript output,
and all other build or review auxiliaries remain external. No claim of
byte-for-byte invariance across arbitrary output paths or TeX installations
is made.

## Paper-source lock and 50-source ledger

- Source count: `50 = 49 TeX + 1 bibliography`.
- Intended live paper count at I60:
  `52 = 50 source + main.pdf + COMPILATION_REPORT.md`.
- Total source size: 106711 bytes in 2497 lines.
- I60 project digest definition: SHA-256 of the 50 `sha256sum` lines below,
  ordered lexicographically by the `paper/` project-relative path and
  including a terminal newline, evaluated from the C60 project root.
- I60 project-relative paper-source SHA-256:
  `84fc29c0c782fbe5a6e818d8606c1f7824575b55985aa4537252cf0e073231b7`.
- Independently hostile-reviewed final candidate aggregate:
  `eb6f958f9d8185cd2a3301d46e53da14e44e4b70e747cd1fdd1c585ad370b12b`.
  This is the SHA-256 of the same ordered digest lines with candidate-relative
  names (`main.tex`, `figures/...`, and `sections/...`) rather than their
  future `paper/` prefixes. The underlying 50 file digests are identical.
- Every source is a regular mode-0644, link-count-one file. The columns below
  are SHA-256, bytes, lines, mode, link count, and future project-relative
  path.

```text
f16995cb629c6c55243ed802705345e6b20f1c901b332d82346e1923a2808b28 | 2135 | 48 | 0644 | 1 | paper/figures/common_preamble.tex
72ae0c7598a4388bed85c1c0f25ad79637e01ac060a9538eafdd0f5ab6b04d36 | 2166 | 44 | 0644 | 1 | paper/figures/fig_fixed_field_diamond.tex
c70dd93d86d71ae1d09bf0d57cc252041da3d4528b0d752e7515f289a35e520a | 4522 | 93 | 0644 | 1 | paper/figures/fig_proof_dependency_dag.tex
9ee3e3cb9bfbd11b24af6ffb3b1f1ffcdd9306bd24646d3191a33fdffde3ee4f | 1563 | 28 | 0644 | 1 | paper/figures/fig_uniqueness_funnel.tex
1fefa7f872355c1c9b471081968ffb22ed8254af81677378b17bd7991cb7a8fe | 198 | 4 | 0644 | 1 | paper/figures/generated/branch_summary_rows.tex
bc1c45853f618cdddee4046bb7349c76688784372f1ff670404d34b9201b7d7d | 1780 | 39 | 0644 | 1 | paper/figures/generated/c60_figure_data.tex
3b3a8c39c5df72bd0b22ab9306c784f47cd50217d627c1a1d0c2e9922568247d | 665 | 13 | 0644 | 1 | paper/figures/generated/collision_rows.tex
92f5235661aa78d0d58eb1cb9091c270c9ff1637c75821c21b94884eb12becd3 | 511 | 7 | 0644 | 1 | paper/figures/generated/dashboard_rows.tex
a0ffaa1424956157babd8e5b42f972a4f1d3d96319ce5668054a3313b4f040df | 1976 | 37 | 0644 | 1 | paper/figures/generated/evidence_rows.tex
c63f86bb042fc0d34a5d655cc3d67da321c30feb7872040e9ea8c1aa4395ddfa | 347 | 7 | 0644 | 1 | paper/figures/generated/global_arithmetic_rows.tex
c5e5587bb9ad23126c73f26d1dee8ed7bdd69741a0e1f0293d04143ff7625a05 | 360 | 5 | 0644 | 1 | paper/figures/generated/invariant_gap_rows.tex
27e9f0b933762acd72811c1de9be60eb00255282d2e70128225939bf38583719 | 531 | 8 | 0644 | 1 | paper/figures/generated/tom140_rows.tex
10d7c0429075277d0c35aa691b08f2c018544b7f885d923fcdb51b4e40c73818 | 534 | 8 | 0644 | 1 | paper/figures/generated/tom206_rows.tex
c84539d3c0fce2a3007d04522e3aaef96ca2d621a6f829cb06a99272cab0bc6d | 6506 | 157 | 0644 | 1 | paper/figures/latex_includes.tex
f85ae3142c54e08254d1be0e034f130a8ae916eaef4790f9d1f50eb07c5d6cd1 | 93 | 2 | 0644 | 1 | paper/figures/paper_calls/fig_fixed_field_diamond.tex
f5969ae3fab74cd6e72ecd69d7e75b577b1976da6ef7935badc560b6c09d4141 | 90 | 2 | 0644 | 1 | paper/figures/paper_calls/fig_proof_dependency_dag.tex
879a9796146a4559e21ad09bf27362ffa2ab0fcaea7ac02f663fab1631a12fc0 | 96 | 2 | 0644 | 1 | paper/figures/paper_calls/fig_uniqueness_funnel.tex
cd896a40b644fe513bd56f46090e21f7be8d662e53ee760fc6b92a359ab8da41 | 96 | 2 | 0644 | 1 | paper/figures/paper_calls/tab_branch_comparison.tex
49b7227a4464e2ef12c870a21aabce3bc4541e6d7da20c412f5a017e3477b398 | 96 | 2 | 0644 | 1 | paper/figures/paper_calls/tab_collision_evidence.tex
86337007c4c3d38eb430b376ea358190c5809f1196a5b53758f53b480a7ee95b | 92 | 2 | 0644 | 1 | paper/figures/paper_calls/tab_evidence_ledger.tex
a02a8bc7adb5dec17998bef797d0df7f8735817f2736bf4b0b01426878e50b90 | 96 | 2 | 0644 | 1 | paper/figures/paper_calls/tab_global_arithmetic.tex
83820d5f0174ae97cfe3fdbbbca74132b1b2ec8e31faa9db6d7f9ec78e667c2a | 88 | 2 | 0644 | 1 | paper/figures/paper_calls/tab_invariant_gap.tex
160b1730b0552c9586c6f6415910100606c8852d8a44e1b6729eda6f225c593f | 96 | 2 | 0644 | 1 | paper/figures/paper_calls/tab_theorem_dashboard.tex
57752b2c1897321a8ab0ab8e2234ce058953ab76901795743cf825c157c16bcd | 94 | 2 | 0644 | 1 | paper/figures/paper_calls/tab_tom140_complete.tex
da68847313cba035682229c3d4e5315d05ff9a8072ee41ff9484a37ee7b86e29 | 95 | 2 | 0644 | 1 | paper/figures/paper_calls/tab_tom206_complete.tex
3a83fc42336332440341e7b165e7d5b219bf2e600484de0bee619b71295b2016 | 628 | 19 | 0644 | 1 | paper/figures/tab_branch_comparison.tex
c4c7a8da0c29b0ccca9e774f091b16b20b1e4078ef881b58fef2c82402ba7593 | 559 | 17 | 0644 | 1 | paper/figures/tab_collision_evidence.tex
1e4221ceacf5bd545f4103e0f20fc1b5253c315d5b7acb816ad41791a25b03f6 | 571 | 16 | 0644 | 1 | paper/figures/tab_evidence_ledger.tex
410dd4f340fe504557b23d5833af5f8ff193281cdf877f7387a029d55236f80b | 459 | 16 | 0644 | 1 | paper/figures/tab_global_arithmetic.tex
399831782015de64be30e557a4ac3fd06de8d24a8da7061cc97c9e8e5b2b6f5b | 614 | 16 | 0644 | 1 | paper/figures/tab_invariant_gap.tex
a96c7c4af6c1dc2d4f4fc326d5fd1a54a52e349934b6e5bdfb2f2ba5fc237a2f | 614 | 18 | 0644 | 1 | paper/figures/tab_theorem_dashboard.tex
08b543086f0f77d5478feea983684899ada886a08a1afd95e4c14a16878d5951 | 555 | 16 | 0644 | 1 | paper/figures/tab_tom140_complete.tex
a37d690f08152b4cbc27a99270c2eb0dfee1914e5648d482df23ed77fa81fb76 | 556 | 16 | 0644 | 1 | paper/figures/tab_tom206_complete.tex
c92e1e9a2a033b998d13f31827a7286859857a46064dc34725247f3ba13c0d3b | 2478 | 82 | 0644 | 1 | paper/main.tex
160f39dcbe495d693f7b4256dd1c79596b2a8b673577f86494a9de1fdbb2dafa | 1094 | 32 | 0644 | 1 | paper/math_commands.tex
0ff39b0142c7ca5313ab74757d5ae47555967bfe297c3eef858a844a750e6ba1 | 2568 | 81 | 0644 | 1 | paper/references.bib
2b40d07a7f33304bd835218c7bf5dffc59ff337984043261f8f2af08667ce36f | 1449 | 20 | 0644 | 1 | paper/sections/0_abstract.tex
8444c29f34ae6946e1e5764a0b73dfa7a0c29bf5c5e3fee2e127f28531a15719 | 8582 | 185 | 0644 | 1 | paper/sections/1_introduction.tex
0e675fdbdd4e49e9ef433f877b310c277375973e9c59d3d32fc222e28a58b45b | 5525 | 143 | 0644 | 1 | paper/sections/2_released_input.tex
a228d508378d5ee861dc2e243295145ca8e090392aaee3f72bf6d0399ef204a5 | 4459 | 119 | 0644 | 1 | paper/sections/3_envelope.tex
bc4b49e1269fa10bfbfdf7b65ce13cc8e77a0cc216120c21c46c3a6c5c3dce6f | 9205 | 213 | 0644 | 1 | paper/sections/4_primitive_generators.tex
21a5efb7cf7199bfb87cf9dc78d4b923a0a254ceb341009d1429de5a7fc511ed | 5155 | 115 | 0644 | 1 | paper/sections/5_uniqueness_zeta.tex
5bf184a6cdbc96007075fc884307c673802d85534b645eb9d37df53267467797 | 5854 | 162 | 0644 | 1 | paper/sections/6_global_arithmetic.tex
4b8e91ec3ddcd1f12ad7a40b913cf990be0042bac9aa6406e694b9f548cf87da | 4015 | 81 | 0644 | 1 | paper/sections/7_local_towers.tex
f14d99852e8164f0c79314fd3ad30d2891373fc29e81208b3991b030c30d3430 | 5668 | 113 | 0644 | 1 | paper/sections/8_reproducibility_scope.tex
404b9ddb4d2bc4a85c851175fd45a735d23090ed024f8bc1ee9175b36da6da76 | 1085 | 19 | 0644 | 1 | paper/sections/9_conclusion.tex
fee7d44b5009ed3bbeb84783361db7cfe1d7fb4d988bcd1adb57453e32a0ad39 | 5560 | 130 | 0644 | 1 | paper/sections/A_group_collision.tex
f8cb1931d532bfdf85eb33576be25450557151d53eb67c4b71c25d72bbf5acc9 | 5629 | 131 | 0644 | 1 | paper/sections/B_carrier_certificates.tex
1e7311d7fdd9c439bac7c4b5ef9a76fc9e67b4ed4ac233cfbf6f4bd03b42e61f | 3519 | 92 | 0644 | 1 | paper/sections/C_arithmetic_ledgers.tex
4ba5284bd3cba3f9b283f83303afac7bad0c9441294c0607aa52d4dda362fbf5 | 5484 | 125 | 0644 | 1 | paper/sections/D_evidence_scope.tex
```

Forty-seven sources are reached by the official build graph. Three are
deliberate dormant source-ledger inputs: the validated optional
global-arithmetic table interface
`paper/figures/generated/global_arithmetic_rows.tex`,
`paper/figures/tab_global_arithmetic.tex`, and
`paper/figures/paper_calls/tab_global_arithmetic.tex`. The manuscript uses
its integrated global-arithmetic table instead of emitting that inactive
interface. These three TeX files are retained as frozen paper-facing interface
sources; they are not generated build auxiliaries. Extraction JSON and its
binding record remain external and are not part of the paper inventory.

No paper-source byte changed during either final clean build. Generator
programs, validation documents, inspection PNGs, standalone smoke PDFs,
LaTeX auxiliaries, and all review records are excluded from the I60 paper
inventory and every future release manifest.

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
- Stale section files: 0; all fourteen files in `paper/sections/` are input by
  `paper/main.tex`.
- Bibliography: 8 entries and 8 cited keys; every entry is cited.
- Figures 1--3 and Tables 1--15 are present. The apparent appendix table
  ordering around pages 18--21 is the stable float order recorded in the
  final PDF; every label and reference resolves.
- Text extraction: PASS, with 1304 layout lines, 11374
  whitespace-delimited tokens, and 90755 bytes.
- Layout-text SHA-256:
  `4aea5c3b3cdfa247869d07dbe0f0aa41bbf389161835eac48b4fff9202a71c36`.
- Residual `TODO`/`FIXME`/`XXX`/`[VERIFY]` markers in extracted PDF: 0.
- Literal `??` or `[?]` placeholders in extracted PDF: 0.
- Anonymous-name, affiliation, email, ORCID, acknowledgement, repository-path,
  `/root`, or `/tmp` leakage in extracted PDF: 0.
- Ghostscript null-device parse: PASS.
- Raster images in the PDF: 0.
- Nonblank pages: 26/26.
- Generated build auxiliaries admitted to `paper/` at I60: 0.

## Exact machine and formal locks

- Machine status: `PREFREEZE_CODE_RESULTS_PASS`.
- Independent post-refresh hostile machine audit: `POSTREFRESH_PASS`.
- Exact gates: G0--G7, 8/8 pass.
- Official refresh: two identical cycles, each 53/53 tests, one atomic
  promotion, cleanup, and mandatory nonmutating replay.
- Payload leaves: 9310; schema leaves: 27.
- Rejected value/type/structural mutations: 9339/9339/14.
- Rejected actual group/resolver/self-consistent-evidence/additional-artifact
  rebounds: 6/4/10/2, or 12 evidence-and-artifact rebounds in total.
- Child snapshot rebind checks: 39.
- Strict-parser invalid/noncanonical cases rejected: 15.
- Machine inventory: 13 code files and 8 result files, or 21 live files;
  the self-excluding scoped machine manifest binds the other 20 entries.
- Payload SHA-256:
  `dca8dbbf269735e78b0435799b0d9c8c9ffad8bdd0470b9262ef64005ff0dead`.
- Certificate SHA-256:
  `d325de1bb0388ccc0c2e81d41fbc6c8fffd692ff777f23647d9e88367d6c2518`.
- Schema-file SHA-256:
  `c7ddb4ff8fa890f9f801d615158c9038299487affa3808f25fe5d73c987791a5`.
- Compact embedded-schema SHA-256:
  `9fe9f8624643ecd83f1ce4eacc9910c413790627dbb35d42fe9262994021303d`.
- Independent-check SHA-256:
  `25bc9c1c656da742359814054b66c05e18a304ca85741776c055152a30a98e44`.
- Group-evidence SHA-256:
  `dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2`.
- Resolvent-evidence SHA-256:
  `f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da`.
- Scoped machine-manifest SHA-256:
  `f8d44a1929b6f873d4f1b4e7317222c0f06e927ba1977f00f493b8fb004cfec7`.
- Group-component aggregate SHA-256:
  `dfd7d16a0128eae7a64906a4449a3022772dbc277abaae8187b6208340302464`.
- Primitive-resolvent component aggregate SHA-256:
  `9ceda190badd260008fcb37788afd5f2a3e3457ca9e1e452f3999df24c12fe97`.
- Group projection SHA-256:
  `77061a473c504925d24cfb2cedc26f7d4bc7057d4ee84615474cfa154323aba0`.
- Resolver evidence-payload SHA-256:
  `eb17676ff10190c0b9f78e8f3fcb90121808fcd2c6a3b5d4dd06bfdc6177bb46`.
- Source-contract SHA-256:
  `4c484b3532c4604b028f45fc157c261149a7a49ca9631bbcf83f8d1efd1cdb90`.
- G0 released-authority rebind SHA-256:
  `0512db556004edde7c19176bbb35375beaeba89301da53902d5c5d98001cb8a8`.
- Producer/checker source SHA-256:
  `0b0dda0eddf0f5ec483cd34ae2c8c285d22b47886d231a126a5849a5162e179b`
  and
  `49b94955cf96862aaefabd5a5988c52b41975e8716a155e1f2ee33af55c7fd46`.
- Official refresh-log SHA-256:
  `5f5d788a1493c16a8eec86ec0cb40bfed2dea72fa2257bddf50eed1be2c43239`.
- Formal-document audit: `FORMAL_DOCS_PASS`.
- Frozen 13-root-Markdown formal aggregate:
  `44b58dc4b43732803dc7b4b04bd0f86673d2161bf95afc9f8f74a77e048bd7a2`.
- `SOURCE_AUDIT.md` SHA-256:
  `50c046c396874e6c0406e92d4ed552fb8b00272d6a0b93d9857c6b4bff13d07f`.
- Neither the 21 protected machine files nor the 13 frozen formal Markdown
  files is rewritten by the paper build or by I60 paper integration.

The scoped machine manifest remains the exact default machine-lane identity.
It is not the pending full-project release manifest. The machine and formal
layers retain their intentional historical `PAPER_PENDING` prose; this report
is the successor paper-state record. Their unchanged bytes do not contradict
the later `PAPER_COMPILED` state recorded here and in the live Route.

## PDF checks

- `pdfinfo` parses the file as an unencrypted PDF 1.5 with 26 A4 pages, no
  forms, no JavaScript, and no suspect objects.
- Title, author, subject, and keyword metadata fields are intentionally blank;
  the rendered author and running-head text is `Anonymous Authors`.
- All 35 fonts are embedded, subsetted Type 1 fonts with Unicode mappings.
- No Type 3 font occurs and no raster image is embedded.
- Ghostscript parsing and complete page-by-page visual/layout inspection pass.
- The independent hostile paper review returned `PAPER_HOSTILE_PASS` with
  zero blockers after rebinding all 50 sources, the PDF, stabilized log,
  layout text, bibliography output, exact machine artifacts, formal package,
  primary-source locators, and visible mathematical claims.
- The theorem dashboard, fixed-field diamond, proof-dependency diagram,
  restricted-uniqueness funnel, Tables 1--15, both complete local branches,
  evidence ledger, and references are legible, unclipped, and
  text-extractable.

## Mathematical and scope checks visible in the paper

- The group has order 51840. The five subgroup orders are
  `|N|=324`, `|H_+|=|H_0|=|H_3|=162`, and `|J|=81`; moreover `N'=J`,
  `N/J` is the Klein four group, every pair of the three order-162 subgroups
  meets in `J` and generates `N`, all relevant cores are trivial, and all
  relevant normalizers are `N`.
- The exhaustive restricted predicate is exactly
  `normalizers_conjugate_in_W AND normalizer_indices_over_subgroups=[2,2]`.
  Among all eleven collision rows, only `[301,303]` qualifies. The `[112,120]`
  near miss has conjugate normalizers but indices `[4,4]`.
- The fixed-field degrees are `[M:Q]=160`, `[F_i:Q]=320`, and `[L:Q]=640`.
  Formal carrier stabilizers and complete noncollision at the split witness
  prime 692717 prove that the evaluated carriers are primitive generators.
- Signatures are `(16,72)` for `M`, `(16,152)` for `F_+` and `F_3`,
  `(0,160)` for `F_0`, and `(0,320)` for `L`.
- The signed discriminant exponent vectors at `(3,5,A,B)` are
  `[308,248,96,80]` for `M`, `[624,496,192,160]` for `F_+` and `F_3`,
  `[632,496,192,160]` for `F_0`, and `[1264,992,384,320]` for `L`.
- The relative discriminant norm exponents at 3 for
  `(F_+/M,F_0/M,F_3/M,L/M)` are `[8,16,8,32]`.
- The complete ToM-140 and ToM-206 local tables are both retained. Every
  relative row is printed; no branch is selected; the relative ramification
  rows have tame `e=2,d=1`; and the `(n,e,f,d)` rows are not promoted as a
  converse classification of individual local fields.
- The V4 rational permutation-character relation proves the displayed zeta
  identity. It is not a finite-G-set isomorphism or an integral permutation
  equivalence.
- The paper claims no expanded characteristic-zero resolvent coefficient
  list, integral basis, maximal order, monogenicity, class number, regulator,
  trace form, decomposition Frobenius, bad Artin Euler factor, epsilon factor,
  root number, Artin holomorphy, automorphy, rational point, Hasse principle,
  weak approximation, Brauer--Manin obstruction, motive, RH, or
  Hilbert--Polya operator.
- `NO_BAD_EULER_OR_ROOT_NUMBER` remains literal.

## I60 release boundary

- Paper compilation status: `PAPER_COMPILED`.
- Independent paper audit status: `PAPER_HOSTILE_PASS`.
- Machine status: `PREFREEZE_CODE_RESULTS_PASS` / `POSTREFRESH_PASS`.
- Formal-document status: `FORMAL_DOCS_PASS`.
- Project release status: `NOT_RELEASED`.
- I60 implementation commit: **pending; no hash is guessed here**.
- Provenance commit: null; pending pre-release policy.
- Full-project release manifest: null; not created; pending.
- Release archive: null; not created; pending.
- Promotion authorization: false.
- C61: contingent and unselected.

This report records the official final paper build and the evidence available
for initial I60 paper integration. It contains neither its own digest nor any
live-Route or archived-Route digest, full-project-manifest digest, or future
implementation, release, or provenance commit identity. Those acyclic
successor identities remain external and may be populated only after the
corresponding artifacts exist.
