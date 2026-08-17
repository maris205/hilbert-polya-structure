# Paper 43 compilation report

Status: `FINAL_WRITER_COMPILE_CANDIDATE_CLEAN`.

Title: **Factors Cannot Resurrect Cycles: Periodic-Ledger Rigidity for the
Squarefree Admissible Shift**.

This report records a writer-only, retrospective rendering of canonical
authority results. It is a publication candidate pending independent approval
and atomic installation. The 158-file research/integration state remained
read-only throughout writing, review, and compilation. No integration code,
experiment, result, evaluation, Route card, root README, Git, mirror, or paper
manifest was changed by this build.

## Deterministic accessibility build

Two independent empty out-of-tree directories were populated from the same
final 19-source state. Each build used this environment and exact 170-byte
ASCII pdfLaTeX input argument, with no trailing newline:

```text
TZ=UTC
SOURCE_DATE_EPOCH=1700000000
FORCE_SOURCE_DATE=1
ENTRY=\pdfglyphtounicode{parenleftbig}{0028}\pdfglyphtounicode{parenrightbig}{0029}\pdfglyphtounicode{parenleftBig}{0028}\pdfglyphtounicode{parenrightBig}{0029}\input{main.tex}
pdflatex -jobname=main -interaction=nonstopmode -halt-on-error "$ENTRY"
bibtex main
pdflatex -jobname=main -interaction=nonstopmode -halt-on-error "$ENTRY"
pdflatex -jobname=main -interaction=nonstopmode -halt-on-error "$ENTRY"
pdflatex -jobname=main -interaction=nonstopmode -halt-on-error "$ENTRY"
```

The exact `ENTRY` byte string has SHA-256
`95281e395a6dd8863500bd198d2f59d6aab950ab136c4329fc2956071f9eed3c`.
The four mappings assign semantic U+0028/U+0029 text to the large-parenthesis
glyphs that pdfTeX otherwise leaves unmapped. They alter no sealed source byte
and no rendered page. Every pdfLaTeX pass used the same argument.

- pdfTeX: `3.141592653-2.6-1.40.22` (TeX Live 2022/dev/Debian);
- BibTeX: `0.99d` (TeX Live 2022/dev/Debian);
- PDF SHA-256:
  `0b7c95926536094e6b30b0b9fb46fa3bf0616b21d7c8c816581faeb4b62f7011`;
- byte size: `483259`;
- format: PDF 1.5, 15 A4 pages;
- metadata: exact title, author `Anonymous Authors`, no host path;
- A/B PDF, final log, bibliography, extracted-text, font, and final-pass
  evidence: byte-identical.

The external evidence bundle is self-excluding and has manifest SHA-256
`bf5ac9753fe77b83b4d1326618b2c117ee675966ceafa7937dd59594b8d32cfa`.
Its principal artifact hashes are:

- final log:
  `4eb5661f3054363fcc0444877a41cb422e904676632cc43554ff90340613ee15`;
- final bibliography:
  `1cac042d27c194e81ed8cbe19c5557a706de11284833a17e81b06eb2aba977f2`;
- final pdfLaTeX stdout:
  `39e2aa1a19ffeead51c564995f58174f0e950015f990c8bb5dc2792e1146bcbe`;
- BibTeX stdout:
  `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9`;
- all captured stderr streams: empty, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- `pdfinfo`:
  `0b4c2e63ae37f61c3dba8261a1d76237bce2d786195ed043cbb07e4f20c55a21`;
- `pdffonts`:
  `ea2781422a87bd9c9074e6c1413440743ae5367b0def6eb7f3596fe8c86e9a55`;
- default text:
  `54c01e8bf8474bfb8bf690adc0d11e0ddb5495f7dceb74c250cf3bc573af778c`;
- layout text:
  `fddfb01877381a7c3fd558277cf3f4ac9a8474ef8cbacf08fada9285469ab645`;
- raw text:
  `67456ca84c1c4b01725c90f5ec3a5b3eb936e731e19732daa08065f807e8adfb`;
- bounding-box XML:
  `0dc5f3ac09b44591773fd2715623a2dd61c4f419614517e158936b292ae6263b`;
- 15-page raster map:
  `e4082957406917fcad36d3d82ca02c5caa99d3b01033f8b02c3b87adf639f6cd`.

## Final log, citation, font, text, and XML QA

Both final logs contain:

- 0 TeX or BibTeX errors;
- 0 package or LaTeX warnings;
- 0 undefined citations or references;
- 0 multiply defined labels;
- 0 overfull boxes;
- 0 underfull boxes;
- 0 rerun requests.

Exactly six bibliography keys are cited, and the final bibliography contains
exactly six resolved entries. The PDF reports 28 font rows; all 28 are
embedded, subset, and equipped with Unicode maps.

Default, layout-preserving, raw, and bounding-box text extractions each have
zero illegal C0/DEL bytes. Form feed is retained only as the standard
`pdftotext` page delimiter and is not classified as illegal. The bounding-box
output is well-formed XML under `xmllint --noout`. Extracted text contains no
unresolved citation/reference, drafting, verification, or host-path marker.
Exactly one `PENDING` occurrence remains: the required
`PENDING_FIRST_ARTIFACT_COMMIT` Stage-A provenance sentinel.

## Page-by-page visual QA

All 15 pages were rasterized and inspected. There is no clipping, overlap,
cutoff, missing object, blank page, defective page break, unreadable label,
table or figure collision, footer collision, or orphaned bibliography entry.
The three figures are pure TikZ. The dense canonical table on page 11, all six
tables, both appendices, and all six bibliography entries remain legible.

The final 15-page raster map is byte-identical to the independently accepted
Round-2 visual candidate. The ToUnicode repair therefore changes only the
machine-readable text layer and not any rendered pixel.

## Writer review and scientific QA

The post-output manuscript completed two bounded review rounds. Round 1 found
zero Critical, zero Major, and two Minor issues; both were repaired. Round 2
returned `CLEAN` at `9.5/10`, with zero Critical, Major, or Minor finding. The
independent PDF audit returned `CLEAN` at `100/100` with zero finding. The
completed improvement log has SHA-256
`8f8993e78e25b5888d2c5e04d118e27082013ee28f987d6e556bccff230d02e0`;
its state JSON has SHA-256
`d81c0965cd9bf0378f1e4bcfd893e658041cdd400c3bc418292ecd483391a393`.

The unique canonical publication block was mechanically extracted as exactly
44 allowed fields. Its extraction JSON has SHA-256
`2352fd577b091bff0cc014918990aeb7d64e46e166b160bfcb837c2ea40be410`.
The strict source-candidate audit passed 27/27 checks with SHA-256
`eadeb45e21c14db9eee95815af4c6a4b94ca86caf370c755080713c6c7bf3c38`.

The block records:

- canonical science SHA-256
  `ae57c6ffb38eb86d43912677eda19574db0ef50f05c25d964d1fcf261fb2422d`;
- main and independent evaluator checks `17/17` and `13/13`;
- CRT controls `16` checked with `0` failures;
- factor-proof obligations `6` checked with `0` failures;
- finite-P0 controls `5` checked with `0` failures, with both empty and
  nonempty controls `PASS`;
- fixed-count coefficients `8` checked, ledger failures `0`, theorem failures
  `0`;
- source resolver `40/40`, with sole retrospective selector survivor
  `SD-C02`;
- main and independent Route checks `23/23` and `24/24`;
- exact output namespace `53`, result ledger `49` entries, and result-ledger
  SHA-256
  `51cd6900505984e0eec391fcd0ff77aedd7747eedd114ec95d2ddf4d273e8a5f`;
- mutation registry `62` classes and `893` instances, zero survivors,
  mutation-ID SHA-256
  `b04cc626b21d4a1df15505a8d2dd9f31f6653879413c9bf05c222abb958eaa76`,
  and registry SHA-256
  `ce9a19990ca79cbd0203c2f42cfab099d754075d78a87438df6bd59551cb1bca`;
- integrity audit `16/16`, SHA-256
  `c4e31e1c48b74bf890e011bae5538bfb98b88dd2f6eb2d36b3021a73a7033021`;
- Run A/B/C byte identity, cold relocated C=A, and normalized State-A/B audit
  byte identity all true; idempotence changed paths `[]`; parent status
  `FINAL`.

The strict Route tuple is
`(A0_FAIL, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`, the verdict
is `ROUTE_A_REJECTED`, and Route B invocation is false. The exact four-field
terminal mapping is:

```text
determinant_comparison       STOP_TRIVIAL_ONE_MINUS_Z_DIVISOR
factor_cycle_creation       STOP_PROXIMAL_PERIODIC_RIGIDITY
literature                  PROCEED_ONLY_AS_INTERNAL_EXACT_CLOSURE
rational_prime_identification STOP_SINGLETON_PRIMITIVE_SUPPORT
```

`STOP_DUPLICATE=LIVE_CONDITIONAL` is an external literature/claim boundary,
not a fifth Route terminal.

The integration chronology is
`RETROSPECTIVE_KNOWN_MATHEMATICS_V6_AUTHORITY_OVERLAY_REPAIR`; this manuscript
is a retrospective post-output rendering. It claims no novelty, priority,
ranking, authorization, preregistration, blindness, selector-independence, or
prospective credit. Stage A remains exact: `source_commit`, `code_commit`, and
`source_lock_code_commit` each equal `PENDING_FIRST_ARTIFACT_COMMIT`, and the
paper manifest is absent.

## Final 19-source publication map

The map is C-sorted by relative path and excludes this report and the
generated PDF. Its serialization has SHA-256
`a973ec0c14546ad13761283be84689b014fe17f1458b7b42d193822cc1f35a4c`.
The self-excluding 17-content writer manifest has SHA-256
`0b0dd9519ed26820ae74d4954c91a111939ede840149a4971d85e23dbff047c1`.
The deterministic research pointer remains SHA-256
`be13e52d83ca7f9f9d59d671bb20df8b826d0d1fa55d3fd71fdf32df2027b67d`.

```text
df2491fa1dc4c7f1ce1c8bb1b1bc435715edcc25d8c9e2e5200b1165b3f2e401  PAPER_PLAN.md
be13e52d83ca7f9f9d59d671bb20df8b826d0d1fa55d3fd71fdf32df2027b67d  RESEARCH_LOCK.json
0b0dd9519ed26820ae74d4954c91a111939ede840149a4971d85e23dbff047c1  SHA256SUMS.txt
7babe4ce222f8ad80ee630477f2d1a949ecc95437e92c5b3b14b604735607b30  WRITER_HANDOFF.md
d917975c5813590f37bd3f99ab47d52bb36952630d7c2439b703847a6934c5ed  abstract.tex
cbb17afce8d573f27ea1c7af4637453527c6709440e935dbb2430314946ec7f6  appendices/A_proof_details.tex
a8889a1a13bcb6a97f45100fa0d067791185195ff8b2cd1c21e7d7e0ec614627  appendices/B_types_provenance.tex
052de746a046816ae956539212186c802569263483a96a881b7e70bff050cf8e  figures/fig1_proof_chain.tex
0b88f6d54c3e70a4a94023954a8e25f034895ed183249fcc16e6c565edcc9b50  figures/fig2_factor_separation.tex
5bac16da402e6f2702d4dfb37877ef7e8546fc3cc74410985008dfb029b0d663  figures/fig3_sharpness.tex
1fef3523cd8fa74c753e788fde78eb260ffdd114fa216fd024ac0670f2f6da79  main.tex
e528cc0e295364f1a18acbcf454ba7a3636087309b00571d6fb583e8b2a7afcf  references.bib
ba8ee54250efc63862eaf7ec57f3715f78bc339fa0e1bac8aec312b18253cb91  sections/1_introduction.tex
6c0d4940874f9d5af020e0f9a9afa82940bfca41168046c60dc0c0668229c544  sections/2_prior_scope.tex
e420f75754b8bde6a57c32fdeb99119ca0fcaca6029ac1f3d469992e9a45064d  sections/3_source_proximality.tex
e8def0418dd13b29f67ca1eeb5b29b69a900edf114c65c64a51b1aec3b3dda53  sections/4_factor_rigidity.tex
8c2bdd35eb2fd7ead8150556f079616fc9ec8d85fa567a67f40994dd0b55a0fc  sections/5_periodic_ledger.tex
4d8a7e786932c3a0d4408e4256dd026fec5ab410056b9cca2f43e821c26d7fcb  sections/6_sharpness_route.tex
19b240a600099edc0115814ebad8be4b2777534842ea37aecd439d8153c380fb  sections/7_limitations_conclusion.tex
```

## Publication boundary

The proposed publication transaction installs exactly the 19 mapped source
paths, this report as `COMPILATION_REPORT.md`, and the verified PDF as
`main.pdf`. It must preserve the frozen 158-file state byte-for-byte and
metadata-for-metadata, produce the exact `AUTHORITY_PUBLICATION_SYNC` overlay,
and pass both static and full integrity audits before it can be declared
complete.

No `.aux`, `.bbl`, `.blg`, `.log`, `.out`, cache, raster, extracted-text, or
build-directory artifact is installed. `PAPER_MANIFEST.sha256` remains absent
in Stage A. Root README registration, Git, mirror, Route provenance, and any
Stage-B action remain outside this writer transaction.
