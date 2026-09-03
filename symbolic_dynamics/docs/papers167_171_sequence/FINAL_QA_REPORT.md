# Final QA report — P167–P171

**Audit record:** 2026-09-03.  **Scope:** exactly the five final Round-2
packages, with prior round PDFs preserved and checked.  **Decision:**
`PASS_INTERNAL / HOLD_EXTERNAL`.

## Exact author-verifier replay

Each paper-local verifier was run afresh from the final workspace with Python
bytecode disabled.  Every stdout stream matched its retained canonical file
byte for byte.

| paper | verifier | assertions | canonical transcript SHA-256 | batch replay |
|---:|---|---:|---|---|
| P167 | `verify_p167.py` | 12,603,676 | `1e7348f9eab389cffc14582b3cf26ebeec69cb72a6c77dbdb1fb204abd1e1a8c` | exact match / PASS |
| P168 | `verify_p168.py` | 32,754 | `8c0b77d99e976e9666ae658f4af7525ccf185f927948e660e3323a0f6f7f3d74` | exact match / PASS |
| P169 | `verify_p169.py` | 1,217,025 | `e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f` | exact match / PASS |
| P170 | `verify_p170.py` | 481,935 | `985941e0a8b363fcf954d503cf825867e54548dd8fcf416ee105a4cbbac2ba13` | exact match / PASS |
| P171 | `verify_p171.py` | 594,955 | `bc3ba0e2b647ff5c888ad7534ef0088398cc7f58b2b71bde9688e3bc9e11e617` | exact match / PASS |

Total: **14,930,345 exact author assertions** and five of five canonical
transcript matches.  Reviewer-owned lanes are reported separately.

## Ten deterministic source-only builds

Two fresh directories per paper were populated with only `main.tex` and
`references.bib`.  Each completed the declared
`pdflatex / bibtex / pdflatex / pdflatex` sequence with halt-on-error.  Every
cold pair matched internally and every output matched its live `main.pdf`
byte for byte.

| paper | pages | bytes | final PDF SHA-256 | font rows | isolated builds |
|---:|---:|---:|---|---:|---|
| P167 | 4 | 285,799 | `b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9` | 21 | 2/2 exact |
| P168 | 5 | 322,829 | `846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e` | 23 | 2/2 exact |
| P169 | 5 | 392,380 | `419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3` | 28 | 2/2 exact |
| P170 | 4 | 277,277 | `b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034` | 23 | 2/2 exact |
| P171 | 3 | 329,559 | `1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1` | 25 | 2/2 exact |

Total: **10/10 source-only builds**, **21 A4 pages**, **1,607,844 bytes**,
and **120/120 font rows** embedded, subsetted, and Unicode mapped.  Settled
LaTeX and BibTeX logs contain no genuine warning, error, undefined citation
or reference, rerun request, or bad box.

## Preserved PDF rounds

| paper | Round 0 SHA-256 | Round 1 SHA-256 | Round 2/current SHA-256 |
|---:|---|---|---|
| P167 | `81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379` | `b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9` | `b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9` |
| P168 | `846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e` | `846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e` | `846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e` |
| P169 | `df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2` | `419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3` | `419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3` |
| P170 | `b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034` | `b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034` | `b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034` |
| P171 | `1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1` | `1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1` | `1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1` |

For all five papers, `main.pdf` and `main_round2.pdf` are byte-identical.
P167's Round-0 to Round-1 change is the closed proceedings-year repair;
P169's is the closed formal-publication citation repair.  P168, P170, and
P171 are no-change freezes across all rounds.

## PDF, visual, anonymity, and lifecycle QA

All 21 final pages were rasterized at 110 dpi and inspected.  No clipping,
overlap, missing glyph, malformed display, illegible formula/table/reference,
margin excursion, or page-boundary defect was found.  Batch checks also
confirmed:

- A4 media boxes of `595.276 x 841.89 pt` for all five PDFs;
- blank identifying title, author, subject, and keyword metadata fields;
- no encryption, interactive form, or JavaScript;
- exactly one `\author{Anonymous}` declaration in every source and an
  anonymous visible byline;
- no email, affiliation, ORCID, personal acknowledgement, username, or
  workspace path;
- at least one visibly extractable `HOLD_EXTERNAL` token in every PDF; and
- all cited references visibly rendered with no unresolved citation marker.

## Review closure

| review | Critical | Major | Minor | independent assertions | closure |
|---|---:|---:|---:|---:|---|
| Hostile Review A, aggregate | 0 | 0 | 2 | 82,955 | P167/P169 source-metadata findings closed in Round 1 |
| Hostile Review B, aggregate | 0 | 0 | 2 | 15,666,986 | P167/P169 packaging findings closed; five theorem accepts |

No paper has an unresolved review finding.  P168, P170, and P171 passed both
reviews with zero findings.  The reviewer lanes total **15,749,941 exact
assertions** and remain separate from the 14,930,345 author assertions.

## Integrity notes and manifest closure

P167 and P169 deliberately deferred final live pointers and manifests until
the second review had inspected their Round-1 source repairs.  Review B
classified those two conditions as localized packaging findings; README,
build/QA ledgers, round copies, and manifests were then closed without a
further manuscript change.  P168, P170, and P171 needed no theorem or source
repair.

No historical `PINNED_INPUTS.sha256` file exists in this batch.  The explicit
round PDFs remain the historical receipts, and
`HISTORICAL_PIN_VALIDATION_NOTE.md` records their relation to the live tree.

The five final paper-local `SHA256SUMS` files contain **35, 31, 39, 31, and
32** non-self entries and pass **168/168**.  Twelve supporting scouting and
review manifests cover 53 declared entries and pass **53/53**.  The batch
`CANONICAL_PDF_MANIFEST.sha256` covers exactly P167–P171 and passes **5/5**.

## Release boundary

Final QA establishes internal theorem-package and artifact integrity only.
It does not establish novelty, priority, ownership completeness, freedom to
operate, or external readiness.  No upload, posting, circulation, contact,
or submission is authorized.  All five manuscripts remain anonymous
internal accepts under `HOLD_EXTERNAL`.
