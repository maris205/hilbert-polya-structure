# Paper 39 compilation and writer QA report

## Final status

**SUCCESS.** The corrective authority-local manuscript compiles to a 20-page A4 PDF. The
conclusion ends on page 12, references occupy pages 13--14, Appendix A begins on
page 15, and Appendix B ends on page 20.

- PDF: `main.pdf`
- SHA-256: `e407c45483e006effdc4d15e7870d374300a3fb3726b1d9ba49b58194d508617`
- Size: 583,657 bytes
- PDF version: 1.5
- Page size: 595.276 x 841.89 pt (A4)
- Build directory: clean, out of tree at `/tmp/paper39_root_finalbuild.dcyxWR/src`
- Authority-root LaTeX auxiliaries after build: 0

`latexmk` was unavailable. The successful clean sequence was
`pdflatex -> bibtex -> pdflatex -> pdflatex -> pdflatex`, with every TeX pass
using an out-of-tree output directory. Only the resulting PDF was copied into
the authority writer directory.

## Authority FINAL result block

The writer synchronized exactly one integrator-declared authority result block.
These values are finite implementation evidence and do not enlarge the
retrospective theorem domain.

```text
Integrator status: FINAL / CLEAN
main evaluator: 535/535; sha256=041461feaf8d34c9974606b9856be5ba5fc6c26f62c88ba38b041998bfd82394
independent evaluator: 278/278; sha256=21bb9b3f623215875bdf93670165da41ff5c42f7e5ccb25cc19a432f7c048398
science projection: sha256=77a45be483807b81ba61fe0f16b16be20fcd7e6e4ff1f3f74f34d052c6881d93
adversarial mutations: 29/29 rejected by each evaluator; sha256=f5fee0209155d06c8e16aedbf44ed2003f29115ad76b7f06bafe8be8a6d26f56
Route evaluation: 14/14; json_sha256=f0d7f98e06e50b1605642fda3abc47b253103c79119886fa5a5b1b0e5c6b2902
fixed Route YAML: sha256=9cda64c6ddf6bfbb865cb576b1a7475e2ce477c3627102e31862ec4c647ebc4e
analysis summary: sha256=acf6dfefcead90b84eb0f28f43c60bf94ad0512389a7ce50d458d6b08e87560a
integrity audit: 224/224; sha256=3c8aed949d8300e327bc265cd23b982b47397981ac379fef99a6d302360d7ac6
ledger audit: 65/65; sha256=be32c6dcf43050307668d583425c67226e2edbb6231120977448e8b4e778e067
exact result set: 36; sha256=69dcf722a5187dfb576a2a607b72f019cd471273c5090277db8e994e09a382dd
exact text set: 67; sha256=e92eddfec5be91fb74a617ed08c7f532e856cbc08c51d14887eafd9ee39358c5
sealed-state controls: 11/11 rejected; sha256=f12f9890d761e5cffe62f70a743cbc0a4749fe90237aa391033321581197181a
managed outputs: 39
managed aggregate: sha256=ac09cd2c3be39e4d6d6ce754b5648d8a2abf7fd7fb9848db984558ff33dc82b3
experiment report: sha256=86f2184b00e25085c18abeab99ef58815290100c42cb267ea33d16f6439d4dcd
locks: research=24f180a30990c3cd581f0732dabeb641dac9e962b17300883a28f77a3844e43a; prototype=c78ca2e09dd026860533f36b94d538397ec0ba20f40980eb9dadfd2dea011762; dependency=44b432ce9f83986bb0f42fa44a3de23eef5b7910d68b5e234166212a451691dd
paired seal states: A = manifest absent + exact three-field PENDING provenance + Stage-1 note; B = exact self-excluding manifest + identical lowercase nonzero 40-hex provenance triple + metadata-only seal note
reproducibility: fresh A/B, cold C, hidden-provenance clone, dummy sealed State B, and two full-runner passes; normal/hidden audit bytes identical in both legal states; changed_paths=0
census: spine=6/5; expanded=22/28; tags=17; classes=14 (6/6/2); tokens=16 (8/8); registry=6; new/ranked/proposed=0/0/0
```

## Immutable research lock

The nine writer-consumed research snapshots have these final SHA-256 values:

| File | SHA-256 |
|---|---|
| `SOURCE_LOCK.md` | `70456aff0b3afff0fe78336da3af7f2fc47724eb59674bf50bb7de4f1857770b` |
| `MATH_PACKAGE.md` | `9af9b4cc68edf87871b9f3d94b04a1df9a92befa59bb2561394f1b6c990c37e9` |
| `PROOF_PACKAGE.md` | `cc58540cb7a2396b7578f3aa7a76de3fcd7554a9faa5f26a4f98d6334b6da621` |
| `DERIVATION_PACKAGE.md` | `ba3d6686928ebc67a24080a48d759cf6395547216b37aa7eeaffddc1bdfc58ed` |
| `QUANTIFIER_AUDIT.md` | `29653cc74b95b3e4e32382f138c1ac00598a5c92bfbbd3c31d8cf8a9ad244073` |
| `DAG_BRIDGE.json` | `4fa3bb28e6a2371dfb134f4a45ff03c1953ea68764f1decb70c64a9d5423d240` |
| `ROUTE_A_EVALUATION.yaml` | `7bdb90811575a96518c2f67510ef9deb4335e2051c965643f7e3572e806ff6cd` |
| `LITERATURE_AUDIT.md` | `aaca0a1834cc9793873698a07cbf4ddedb73a409eb9bd4dbc72ec4dd857fc781` |
| `DA_REPORT.md` | `ef9aacc4584125853c572802a81e7243a60472ad5c5df17af57dd92d2e1599a3` |

The literature and devil's-advocate hashes supersede their pre-hygiene values.
No other immutable research byte changed during the writer QA rounds.

## Compilation checks

- TeX errors: 0
- Undefined citations: 0
- Undefined references: 0
- Multiply defined labels: 0
- Overfull boxes: 0
- Nonblocking underfull boxes: 1 (`badness 1237`)
- Bibliography entries: 27
- Distinct cited keys: 27
- Uncited bibliography entries: 0
- Fonts: 31, all embedded, subset, and Unicode-mapped
- Raster images: 0; all three figures are vector TikZ
- Abstract length: 192 words
- Provisional result hashes or counts: 0

BibTeX emits one metadata warning: `Hashimoto1989Zeta` has no publisher field.
The verified literature record is intentionally preserved; no publisher was
invented. Proper names and project names were protected for bibliography
rendering without changing factual citation metadata.

## Visual and structural QA

All 20 rendered pages were inspected. In particular:

- Figure 1 shows four nontrivial fibers plus the five exact singleton mappings;
  its five spine-edge IDs appear in a separate readable legend.
- Figure 2 follows the complete proposition and does not split its enumerated
  alternatives.
- Figure 3 has four separated RESET/P37 boxes, routing buses wholly outside the
  boxes, a padded E07/E36_37 connector label, separated metadata boxes, the
  literal `AUXILIARY_NON_DOMAIN_FIREWALL` type, and no failed-`Good` classifier
  role for E22.
- Proposition 4.2 and both enumerated alternatives remain together on page 7.
- Table A.2 renders `FROZEN_ASCENDING_HNN_` and
  `BASS_SERRE_SPLITTING` as an explicit two-line continuation, without splitting
  the final word or obscuring the exact token.
- The authority FINAL table is not interposed inside the adversarial-validity
  argument.
- The corrective evidence block states both legal seal states, reports all
  11/11 mixed-state controls as rejected, and keeps metadata sealing separate
  from the scientific claim.
- Appendix tables are scoped as A.1--A.3 and B.1--B.3, with exact identifiers
  preserved at readable size.
- Bibliography rendering preserves the proper-name capitalization in
  `Ihara--Selberg`, `Wagner`, and `Eden`.
- The conclusion finishes on page 12, satisfying the plan's main-body target.

## Autonomous improvement rounds

Round 1 audited mathematical and claim-boundary fidelity. It corrected the
`N00 -> AUX_CONTRACT_ROOT` projection, separated EXIT classification from
failed-`Good` evidence, described `Good` as a retrospective consolidation of
pre-existing fields, made the nine research snapshots read-only, gave E22 no
classifier role, and completed the 17-edge role labels.

Round 2 audited narrative, typography, and submission readiness. It triggered a
fresh build, removed Figure 1 and Figure 3 collisions, made the E22 type literal,
prevented floats from splitting proofs, rebalanced the trust table, shortened
the abstract to 192 words, protected bibliography names, cross-referenced the
figures and ledgers, introduced appendix-scoped numbering, improved longtable
legibility, and compressed repeated main-text material while retaining the
full source-owned kernels and countermodels in Appendix A.

Both rounds preserved the retrospective claim boundary: 14 classes, 16 tokens,
17 internal tags, 22/28 expanded versus 6/5 structural graphs, class census
6/6/2, token census 8/8, E22 zero credit, four E07/E36_37 RESET fields, an
all-FAIL Route tuple, locked Route B, and an unranked registry handoff with no
Paper-40 authorization.
