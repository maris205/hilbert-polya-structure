# Final QA report — P157–P161

**Audit date:** 2026-09-02 UTC.  **Scope:** the five live final Round-2
packages only, with Round-0 and Round-1 PDFs checked for preservation.
**Decision:** `PASS_INTERNAL / HOLD_EXTERNAL`.

The retired BST candidate is not a live P160 package and is excluded from all
five-paper totals below.  Its historical evidence is recorded separately in
`STAGE2_REPORT.md` and the retirement ledgers.

## Exact author-verifier replay

Each paper-local author verifier was executed afresh from the final workspace
with Python bytecode disabled.  Every fresh stdout matched its retained
`verification_output.txt` byte for byte.  The paper-local final-QA passes had
already obtained two matching fresh runs per verifier; this batch pass adds a
fresh cross-paper replay.

| paper | verifier | assertions | transcript SHA-256 | batch replay |
|---:|---|---:|---|---|
| P157 | `verify_p157.py` | 2,563,880 | `f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1` | exact match / PASS |
| P158 | `verify_p158.py` | 77,530 | `3e69dfb7d0653c140f2945a6fe4888afc569756a25acf20c1e7eaf2d9f432f0d` | exact match / PASS |
| P159 | `verify_p159.py` | 3,167,525 | `363d77a151dfa0b1d6b4ded84700d01dd249ed242573bff98fa38d490a1d4879` | exact match / PASS |
| P160 | `verify_p160.py` | 3,462,895 | `3e1b83ff586795fc80fc01882d545fff270f9106471145b39c0f0ca51bd3a778` | exact match / PASS |
| P161 | `verify_p161.py` | 1,317,843 | `26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c` | exact match / PASS |

Live total: **10,589,673 exact author assertions**; five of five transcript
gates pass.  The larger independent hostile-review assertion lanes remain
supporting falsification evidence and are not added to this author total.

## Ten deterministic source-only builds

Two fresh directories per paper were populated with only `main.tex` and
`references.bib`.  Each completed the declared
`pdflatex / bibtex / pdflatex / pdflatex / pdflatex` settling sequence with
halt-on-error.  Every cold-build pair matched internally and each output
matched its live `main.pdf` byte for byte.

| paper | pages | bytes | final PDF SHA-256 | font rows | isolated builds |
|---:|---:|---:|---|---:|---|
| P157 | 4 | 349,380 | `6b0c1fb81c065a9213df4cb4af7b731e25e02e3306e6220a154899166e9129dd` | 26 | 2/2 exact |
| P158 | 4 | 371,703 | `2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5` | 28 | 2/2 exact |
| P159 | 5 | 363,444 | `72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d` | 27 | 2/2 exact |
| P160 | 4 | 316,629 | `ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352` | 23 | 2/2 exact |
| P161 | 4 | 304,462 | `1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214` | 21 | 2/2 exact |

Total: **10/10 source-only builds**, **21 A4 pages**, **1,705,618 bytes**,
and **125/125 font rows** embedded, subsetted, and Unicode mapped.

The ten settled-log scans contain zero LaTeX/package/pdfTeX warning, TeX
error, overfull or underfull box, undefined reference or citation, or rerun
request.  BibTeX diagnostics are zero.  All five final PDFs report A4 media
boxes of `595.276 x 841.89 pt`.

## Preserved PDF rounds

| paper | Round 0 SHA-256 | Round 1 SHA-256 | Round 2/current SHA-256 |
|---:|---|---|---|
| P157 | `4188a459ad233e8a6a55d5706648617e833ea0f7771d324a368352182a2f9c0d` | `f054f639f4c9ba9d462c183f417597390223b18ca3f74ba5907c39637ba4743e` | `6b0c1fb81c065a9213df4cb4af7b731e25e02e3306e6220a154899166e9129dd` |
| P158 | `bbe961298aa62adc54d34f15cc546ff3f14d7d4d29fd90dee2dcc6e2fff2e892` | `2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5` | `2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5` |
| P159 | `bba68d57e9f46cda2996db072b703ff0b18e5d19c7edab2a53ef24d3032c8602` | `72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d` | `72c0ca96d3afde550b05677e61454ba5c9fcdb819c6332c92baaa0045fe4b05d` |
| P160 | `2be90261ae3b636aa8db684597896f7e7d549363879936b3f6539877577f7d08` | `3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03` | `ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352` |
| P161 | `b0e241883509857362f59688b6ea18422959b07862681cabe13bedfe0d1f79c0` | `1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214` | `1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214` |

For all five papers, `main.pdf` and `main_round2.pdf` are byte-identical.
Round-0 and Round-1 artifacts remain present at their recorded hashes.

P160 Review B accepted Round 1 with **0 Critical / 0 Major / 0 Minor** and
requested no change.  Its Round-2/current difference is exactly the visible
sentence `This artifact remains HOLD_EXTERNAL`, added for cross-batch
lifecycle consistency during final-QA preparation.  It is a post-review
status consistency edit, not a Review-B finding and not a change to a theorem,
proof, source subtraction, bibliography, verifier, or transcript.

## PDF, visual, anonymity, and lifecycle QA

The five paper-local final-QA passes rasterized and inspected all **21** final
pages at 144 dpi.  They report no clipping, overlap, missing object, malformed
glyph, illegible formula/table/reference, margin excursion, or page-boundary
defect.  Batch checks reconfirmed:

- blank identifying values in PDF title, author, subject, and keyword
  metadata;
- exactly one anonymous source author per manuscript and an anonymous visible
  byline;
- no unresolved citation marker, placeholder, email, affiliation, ORCID,
  personal acknowledgement, funding statement, username, or machine path;
- one visibly extractable `HOLD_EXTERNAL` token in each of the five PDFs;
- no encryption, form, JavaScript, or embedded-file release hazard.

## Review closure

The following counts cover the **five live papers only**.

| review | Critical | Major | Minor | closure |
|---|---:|---:|---:|---|
| Hostile Review A, aggregate | 0 | 2 | 5 | all seven findings closed in Round 1 |
| Hostile Review B, aggregate | 0 | 0 | 2 | both findings closed in Round 2 |

Review-A repairs comprised P157's two attribution/scope wording items,
P158's boundary separator and independent sequential-update coverage,
P160's every-weight witness and enlarged classical rectangle/symbol source
subtraction, and P161's build-warning repair.  P159 Review A returned zero
findings.  Review-B findings were only P157's reproducible microtype warning
and P159's stale lifecycle sentence; both are closed.  P158, P160, and P161
Review B returned zero findings, with P160 specifically **0/0/0**.

The retired BST manuscript's `1 Critical` direct-owner kill is historical and
is deliberately excluded from these live review aggregates.

## Manifest closure

The five final paper-local `SHA256SUMS` files contain, respectively, **37,
30, 33, 42, and 33** non-self entries: **175/175** checksum checks pass.  The
batch `CANONICAL_PDF_MANIFEST.sha256` covers exactly the five live
`main.pdf` files and passes **5/5**.  The retired BST PDF is not in that
manifest.

## Release boundary

Final QA establishes internal theorem-package and artifact integrity only.  It
does not establish novelty, priority, ownership completeness, or external
readiness.  No upload, posting, circulation, author or specialist contact, or
submission is authorized.  All five live manuscripts remain anonymous
internal accepts under `HOLD_EXTERNAL`.
