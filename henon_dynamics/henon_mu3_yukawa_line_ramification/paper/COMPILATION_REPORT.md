# HCS-C58 compilation report

Status: **PASS; official final6 paper build; `PAPER_HOSTILE_PASS`; project
`RELEASE_FROZEN` at implementation commit
`55f2b9471475a8becdd97478b248b327a786bce5`; protected machine layer remains
`PREFREEZE_CODE_RESULTS_PASS` / `POSTREFRESH_PASS` and the formal layer remains
`FORMAL_DOCS_PASS`.**

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
- Two consecutive clean builds produced a byte-identical PDF.
- Authoritative integrated path: `paper/main.pdf`.
- Total pages: 28 A4 pages.
- The conclusion is on page 16, Appendix A begins on page 17, and references
  begin on page 27 and continue through page 28.
- File size: 468808 bytes.
- PDF SHA-256:
  `63b84e44fee272f3158ea85eb581321c74609d8c42a37a91a5d80feaa0dbeaa4`.
- Final stabilized external LaTeX log: 42643 bytes; SHA-256:
  `7f868cce5d280790915b5d5f4c5f42b5863cdde8c12328f74092c83c5f4a5602`.
- External stabilized `main.bbl`: 3092 bytes; SHA-256:
  `c00118b386aab9cc90194e2d1636521fa8cd3b16547a8965707e48eba4c219d9`.

No conference page limit is asserted. The paper uses a single-column
mathematical-article format. The in-tree PDF named above is the authoritative
paper artifact. The stabilized log, bibliography build output, extracted
text, raster material, and all other build auxiliaries remain external. No
claim of byte-for-byte invariance across arbitrary output paths or TeX
installations is made.

## Paper-source lock and 17-source ledger

- Source count: `17 = 16 TeX + 1 bibliography`.
- Intended live paper count at I58:
  `19 = 17 source + main.pdf + COMPILATION_REPORT.md`.
- Total source size: 96294 bytes in 2408 lines.
- I58 digest definition: SHA-256 of the `sha256sum` lines below, ordered
  lexicographically by the `paper/` project-relative path (not by the digest
  prefix) and including a terminal newline, evaluated from the C58 project
  root.
- I58 project-relative paper-source SHA-256:
  `b0842e6826ffdaa541dd52db1af7d6b03e66dfd27a0cba861d27de427f828b4e`.
- Independently hostile-reviewed final6 candidate aggregate:
  `60022ff97f45a39984e4240f5a27ff38979e1e0b2163799d6803eb6c1102bd72`.
  This is the SHA-256 of the same ordered digest lines with candidate-relative
  names (`main.tex`, `sections/...`) rather than their future `paper/`
  prefixes. The underlying 17 file digests are identical.

```text
62fc92c3c0ad6a6276c833b5a1f063b35b782bb68cd67d02a3ff824a93d5eb4d  paper/main.tex
857f4a7463e629b7a036d2c56e61fd7942123075c87cd3f9bc5cd675274558b7  paper/math_commands.tex
939e8483364eba4ef432028325bd48384ab40d4b97ec37fb383b6ba576e9a71e  paper/references.bib
9e3324459f8af2b958ccf59023368f23aef1fc9b52aea76d8cf4936972d407ed  paper/sections/0_abstract.tex
0cc9614cbc3dca949a6964f97549d6ba7a40664eb6d0207fc090d6f08c4681ae  paper/sections/1_introduction.tex
92960bd9a89bdecb962bdd92042153119aa74beee7bcb7f9df9779a22210ad14  paper/sections/2_surface_representations_theorem.tex
16ac69fe81d741be66917d81d86dd29a66154fd5bc960ff2c3b139690a779304  paper/sections/3_local_arithmetic_carriers.tex
ad247cf0a40cda0bfc5269bc622fdb8979304e62cc4822373d174e00f0f511a8  paper/sections/4_wild_three.tex
44671043bfe90ffa9b9aec796400cbf1c91f04dc86e85d7f1943b418135e1be5  paper/sections/5_wild_five_tame.tex
14c0b52290414d75f4e412e3da89bdd551aae8d0442b6b1e762a03399b61e8ba  paper/sections/6_conductors_discriminants.tex
ac23c4582343a6a22ba4acd651c0cdfd28803ffbd3670c2761a531c27974ad3c  paper/sections/7_infinity_scope_validation.tex
cb872950da37e86646a2d513b55669a706f18f608500b52beb43a155cf92e9e5  paper/sections/8_conclusion.tex
d9d2ea77f1c93a02fadc84f8c4b0882b26d010fb4ce9c5e7ccdd8f1a538ccb29  paper/sections/A_local_orders_authority.tex
408927c4d31cf062de65e48a50a295f54af6b1119994352f85860a7182ed4156  paper/sections/B_group_tables.tex
52b35bd868bbb3993dd2f191cb73e644463699fc3ce4febdda1127daf27d2a58  paper/sections/C_reflection_geometry.tex
ead36dcb34dac131305ca6b7ffef0fe5e7f24b353eaf2ef88ec2d3f2955829cd  paper/sections/D_exact_certificate.tex
ec5ea5ceea2cfcbe01251d22fc8bae9ebbe9d8ae55a697e41b51f575d8e535ee  paper/sections/E_source_ledger.tex
```

All 17 source MD5 values recorded by latexmk are identical to the final6
source bytes. No paper-source byte changed during the official build.

## Automated checks

- Undefined citations: 0.
- Undefined cross-references: 0.
- pdfTeX warnings: 0.
- LaTeX warnings: 0.
- Package warnings: 0.
- The former pdfTeX font-expansion diagnostic is absent;
  `microtype` records `No font expansion` under `expansion=false`.
- BibTeX warnings: 0 (`warning$ -- 0`).
- Duplicate PDF destinations or multiply defined labels: 0.
- Overfull horizontal or vertical boxes: 0.
- Underfull horizontal or vertical boxes: 0.
- PDF-string warnings: 0.
- Missing-character diagnostics: 0.
- Rerun requests: 0.
- Fatal or engine errors: 0.
- Stale section files: 0; every one of the 14 files in `paper/sections/` is
  input by `paper/main.tex`.
- Static source inventory: 83 label declarations, all unique; 94 reference
  commands with no missing target; 26 literal `\citep`/`\citet` commands over
  exactly 10 bibliography keys; and 129 balanced environment pairs.
- Bibliography: 10 entries, all cited.
- PDF outline: 52 bookmark entries, with no PDF-string warning.
- Text extraction: PASS, with 1380 lines, 12549 whitespace-delimited tokens,
  and 96505 bytes.
- Extracted-text SHA-256:
  `98fcf53d1e906966cff7229c0a4e611bc677c1aaf6af40b6ec971b3e2c08aeb2`.
- Residual `TODO`/`FIXME`/`XXX`/`[VERIFY]` markers in extracted PDF: 0.
- Literal `??` or `[?]` placeholders in extracted PDF: 0.
- Doubled cross-reference wording such as “Equation equation”: 0.
- Rendered literal-TeX residue such as `qquad`: 0.
- Anonymous-name, affiliation, email, repository-path, `/root`, or `/tmp`
  leakage in extracted PDF: 0.
- Ghostscript null-device parse: PASS.
- Generated auxiliaries admitted to `paper/` at I58: 0.

## Exact machine and formal locks

- Machine status: `PREFREEZE_CODE_RESULTS_PASS`.
- Independent post-refresh hostile machine audit: `POSTREFRESH_PASS`.
- Exact gates: G0--G7, 8/8 pass.
- Independent checker status: `PASS_PREFREEZE_CODE_RESULTS`.
- Payload leaves: 1149.
- Rejected systematic rebound mutations: 1199.
- Project-local tests: 45 passing.
- Strict-parser negative cases: 8.
- Machine inventory: 14 code files and 8 result files, or 22 live files;
  the self-excluding scoped machine manifest binds the other 21 entries.
- Payload SHA-256:
  `fba2dfdf71977d8de6c85635eca6572e0b8a0680570f394af9e3e9e8698f732f`.
- Certificate SHA-256:
  `456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee`.
- Schema-file SHA-256:
  `ccbc20eb6e04d00f14cdc0ccf970caebf4d66b4103176515799ddca89639009a`.
- Canonical-schema SHA-256:
  `3aff3873199870c23421dd3986e017d5860366562ebbd6e5fbfafc468c824f54`.
- Independent-check SHA-256:
  `64454700ddaa0bb9ff56c85afa213f038ec6b430bc38ef07e3f22924081d22e9`.
- Independent-replay-summary SHA-256:
  `d5e98eaafedd03b90c851f9082237387f1eddc559a8c37b49b85f0e5ffa897c6`.
- Arithmetic-evidence SHA-256:
  `e374d328a7937c48af93e0b46f54eead5a878f01acc161d8053fe4a10c5f6128`.
- Group-evidence SHA-256:
  `0e0b3fd4927b3a8355037b57b86a1e3cc7efe15832be4f5ca76cb4989b71a1fd`.
- Scoped machine-manifest SHA-256:
  `a18742298722e2bff022b95be8a09806dd774a52ab8e095ebde78924c45ae730`.
- Formal-document audit: `FORMAL_DOCS_PASS`.
- Frozen 13-root-Markdown formal aggregate:
  `7d464a25811362027dfc79d112e9e875306c6d8fc4c824648e1d2bed161d85ef`.
- Project status: `RELEASE_FROZEN`, binding implementation commit
  `55f2b9471475a8becdd97478b248b327a786bce5`.
- Separate provenance commit: `null`; release provenance is external-only and
  no separate provenance commit is promoted.
- The protected 22 machine files and frozen 13-root formal package are not
  rewritten by P58. Their historical `PAPER_PENDING` prose is a layered-state
  record, not the live project release status.
- Release-wide successor: root `FULL_PROJECT_HASHES.sha256`, exactly 56
  entries and self-excluding; its digest is verified and reported externally.
- Frozen Route archive:
  `evaluations/route_a/HCS-C58/20260816T000000Z.yaml`, byte-identical to the
  final live `route_a_evaluation.yaml`; both digests remain external to this
  report.

The 21-entry scoped manifest remains the exact machine-lane identity. The
56-entry successor is the release-wide ledger and does not replace it. P58
does not rewrite any paper source, PDF, code, result, certificate, evidence
artifact, or frozen formal-root Markdown file.

## PDF checks

- `pdfinfo` parses the file as an unencrypted PDF 1.5 with 28 A4 pages, no
  forms, no JavaScript, and no suspect objects.
- Title, author, subject, and keyword metadata fields are intentionally blank;
  the rendered paper title is present and the author/running-head text is
  `Anonymous Authors`.
- All 25 fonts are embedded, subsetted Type 1 fonts with Unicode mappings.
- No Type 3 font occurs.
- Ghostscript parsing and representative visual/layout inspection pass.
- The independent hostile paper review returned `PAPER_HOSTILE_PASS` with
  zero blockers after rebinding all 17 sources, the PDF, stabilized log,
  extracted text, and bibliography output.
- The hero table and filtration diagram are legible. The wild-prime tables,
  reflection geometry, Appendix D artifact map, Appendix E source ledger,
  long digests on pages 24--25, and references on pages 27--28 are complete,
  unclipped, and text-extractable.
- The claim-to-artifact map occurs only in Appendix D.

## Mathematical and scope checks visible in the paper

- The nine-prime surface divided-discriminant envelope is kept distinct from
  the exact eight-prime ramified support of both the degree-27 field and its
  normal closure; the prime 2 belongs only to the surface envelope.
- Section 3 treats the displayed local different sums as computations made
  before, and used later to check, the representation-theoretic conductors.
  No constituent conductor is obtained by splitting a global sum.
- At 3, the paper retains the exhaustive raw subgroup scan and all four
  ordered pairs `(D,I)=(140,140),(142,142),(206,140),(206,142)`. The exact
  ToM `6 x 2, 7, 8` `Fraction` exhaustion gives respectively `(7,-18)`,
  `(1,6)`, and `(7,-18)`, after which Serre's odd-grade inversion test selects
  inertia ToM 140. The surviving pairs are `(140,140)` and `(206,140)`. The
  unresolved decomposition-group order 18 or 36 affects none of the proved
  filtrations, conductors, or discriminants.
- At 5, all raw hits 147/247/295 and the Sylow-normality exclusions remain
  explicit; the resulting filtered inertia is ToM 147 with lower orders
  `(20,5,5,5,1)`.
- `theta36` is the sole certified degree-36 local authority. `delta36` is a
  bounded nonresult and supplies neither a premise nor corroboration at any
  prime.
- At 181, 997, and 2346241, the certified `theta36` double-six partition
  selects tame inertia ToM 6, isomorphic to `C3`, with Artin pair `(6,12)` at
  each prime; this conclusion uses no `delta36` evidence.
- The reflection proof uses four disjoint projective pivot strata, all four
  homogeneous partial derivatives, the `p != 3` Euler bridge, exact Hessian
  and Hensel data, valuation-one transversality, and Picard--Lefschetz. It
  selects root-reflection subgroup ToM 2 and claims no `(e,f)` decomposition
  row.
- The three Saito locators are consistent in the main proof, Appendix C, and
  Appendix E: Proposition 2.3, p. 858; Theorem 3.5, pp. 864--866; and the
  cubic-surface specialization on p. 870. The source ledger distinguishes
  every universal implication from the frozen-instance computation.
- The global Artin/Swan calculation gives
  `N(V6)=3^11 5^7 A^6 B`, `N(V20)=3^35 5^29 A^12 B^5`,
  `Disc(E)=3^46 5^36 A^18 B^6`, and
  `Disc(K)=3^106560 5^80352 A^34560 B^25920`. The proof of the positive sign
  of `Disc(K)` uses the Galois degree 51840 and the even imaginary-place count
  25920.
- At infinity, the subgroup generated by complex conjugation is
  Table-of-Marks subgroup ToM 5, while complex conjugation itself belongs to
  character-table element-class index 17 under CTblLib 1.3.1. The two
  indexing systems are never conflated.
- `NO_BAD_EULER_OR_ROOT_NUMBER` remains an explicit dependency firewall. The
  paper claims no decomposition Frobenius, bad Euler polynomial or factor,
  local epsilon factor, local or global root number, Artin holomorphy,
  automorphy, analytic continuation, or functional equation. Resolving the
  order of the decomposition group at 3 would not by itself authorize any of
  those conclusions.
- The paper makes no rational-point, local-point, weak-approximation,
  Hasse-principle, Brauer--Manin, or all-cubic-surfaces assertion.

## P58 release closure

- Paper compilation status: `PAPER_COMPILED`.
- Independent paper audit status: `PAPER_HOSTILE_PASS`.
- Machine status: `PREFREEZE_CODE_RESULTS_PASS` / `POSTREFRESH_PASS`.
- Formal-document status: `FORMAL_DOCS_PASS`.
- Project release status: `RELEASE_FROZEN`.
- Implementation commit:
  `55f2b9471475a8becdd97478b248b327a786bce5`.
- Separate provenance commit: `null`; P58 provenance remains external-only and
  no separate provenance-commit identity is promoted.
- Release-wide successor: root `FULL_PROJECT_HASHES.sha256`, exactly 56
  entries and self-excluding; its digest is verified and reported externally.
- Frozen Route archive:
  `evaluations/route_a/HCS-C58/20260816T000000Z.yaml`, byte-identical to the
  final live `route_a_evaluation.yaml`; both digests remain external to this
  report.
- Promotion authorization: true.
- P58 rewrites no paper source, PDF, code, result, certificate, evidence, or
  frozen formal-document byte.
- C59--C61 remain contingent and unselected.

This report records the official final6 paper build and P58 release closure.
It contains neither its own digest nor any live-Route, archived-Route,
full-project-manifest, or P58 commit digest. Those acyclic identities are
verified and reported only by external consumers. The frozen formal-package
digest likewise remains external to the 13 Markdown files it covers.
