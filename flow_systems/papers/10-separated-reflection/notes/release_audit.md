# Paper 10 independent final release audit

**Audit date:** 2026-08-14 23:22 CST (UTC+08:00)  
**Audit role:** independent ARS release, reproducibility, citation-closure, and
public-package reviewer  
**Verdict:** **PASS — C0/M0/m0**  
**Open findings:** **0 Critical / 0 Major / 0 Minor**

This verdict applies only to the exact bytes in Section 1.  The audit was
read-only with respect to the locked candidate: clean builds, control
generations, page renders, and Git-index simulation were performed in fresh
temporary directories.  The only project file created by this audit is this
report.

The PASS is an internal scientific and repository-release verdict, not a
journal-submission authorization.  Human declaration confirmations, the
post-batch immutable identity for Paper 9, and the final destination-clone
index check remain explicit external release conditions in Section 8.  They
are not mathematical or manuscript defects in the present candidate.

## 1. Exact release lock

| Artifact | SHA-256 | Result |
|---|---|---|
| `paper/manuscript.tex` | `27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315` | PASS |
| `paper/references.bib` | `201e997ad953ebc1f27bd4c068400be656a1b9b6fbc4a231443ad8c2770e98b1` | PASS |
| `paper/figures/owner_collapse_and_proxy.tex` | `d5be1f45dbf4c5b3c7668d326e416166941dd9dbb7b7d0c64d076a8f41d03421` | PASS |
| `paper/figures/copied_coproduct_ledger.tex` | `e4bceb3b3bb67d6a837014c44d226ce2131ca7cdd4184cdd4aa8da12f8f90291` | PASS |
| `paper/paper.pdf` | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` | PASS |
| `paper/README.md` | `6ffd4dd3ac4e4df27016ee4192652f2e1297e37a92f845d1f6964274bceeb3c7` | PASS |
| project `README.md` | `a60142e1b1eb013d0b8d9dfa22d83afe7ec61efcd5524df4814407634bb0538e` | PASS |
| `results/separated_reflection_controls_manifest.json` | `edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215` | PASS |
| `notes/route_audit.md` | `fded0943eb3c628e90b407c14aece688b1a79f8be4510c02e98010592b9ca4ee` | PASS |
| `notes/citation_audit.md` | `7f33027e9e42b67dd12b65dd1fcd2238fdf0e7419204ecea746fa45f2cd61e35` | ACCEPT |
| `notes/peer_review_round1.md` | `378c20054417b93cd34361a97a2a5f1952c121872d055732ee578d2e3aef03d3` | ACCEPT, C0/M0/m0 |
| `notes/sources/.gitignore` | `6cbf9577be5add7a925718f4047f672fe46d991772fd451f428390aa323b6d3f` | PASS |

The release ledger in `paper/README.md` contains the exact manuscript,
bibliography, two figure-source, and PDF hashes above.  Both final independent
reviews bind the same tuple.  A second hash pass at the end of this audit found
no candidate-byte drift.

## 2. Independent clean build and full-page equivalence

Only `manuscript.tex`, `references.bib`, and the two native TikZ sources were
copied into a newly created directory outside the project.  The documented
build chain was executed explicitly:

```text
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
bibtex paper
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
```

XeTeX `3.141592653-2.6-0.999993` (TeX Live 2022/dev/Debian) and BibTeX `0.99d`
completed successfully.  The clean PDF is 19 A4 pages.  The final pass has:

- zero LaTeX errors or undefined control sequences;
- zero undefined citations or references;
- zero BibTeX or package/LaTeX warnings;
- zero duplicate-label, missing-glyph, or overfull-box diagnostics; and
- four harmless underfull-box notices only.

The clean PDF SHA-256 is
`778a81fe474b7ade2cc339bddaf64909fca20a8970a1c19eafd1554c0bc05c95`.
Its raw container differs from the release PDF by one byte in file size and by
time-dependent creation metadata/font subset identifiers.  Three independent
visible-content checks close that expected container difference:

| Equivalence check | Result |
|---|---|
| `pdftotext -layout` | byte-identical; SHA-256 `6975224f340f1506c766d7f61af45685bace908c56a16d3670cd16f614101cd5` |
| 100-dpi PNG renders, pages 1--19 | **19/19 byte-identical**, mismatches 0 |
| ordered digest of the 19 individual page hashes | `cbf62cccc60fa2bec6758db84bcfed478abab6cf857206d8d20473acb4f956da` |

Representative visual inspection covered pages 1, 8, 12, 14, and 19: the
bilingual abstract; Figure 1 and its owner/direction labels; the separated
Corollaries 6.2 and 6.3 blocks; Figure 2 and the beginning of the Route ledger;
and the end of the bibliography.  No clipping, overlap, missing glyph,
misdirected arrow, broken caption, theorem-heading collision, truncated URL,
or unreadable reference was found.  Mechanical raster equality covers all
other pages.

`pdfinfo` reports 19 unencrypted, unrotated A4 pages, no JavaScript, and the
expected title and author.  `pdffonts` reports eight font records; every record
has `emb=yes`, `sub=yes`, and `uni=yes`.  `pdfimages -list` reports zero image
objects in both the locked release and the clean rebuild, consistent with the
two declared native-vector TikZ figures.

## 3. Citation and retained-source closure

An independent source-level key extraction and the clean BibTeX build agree:

| Citation gate | Result |
|---|---:|
| unique manuscript citation keys | 9 |
| unique bibliography keys | 9 |
| cited keys absent from BibTeX | 0 |
| uncited BibTeX records | 0 |
| final `.aux` `bibcite` records | 9 |
| rendered `.bbl` bibliography items | 9 |
| unresolved citation diagnostics | 0 |

The nine-key sets are identical:
`CagliariMantovani2003`, `Deninger2026`, `FremlinMeasureCh11Dev`,
`HernandezArzusaHernandez2020`, `HoermannCStar2026`, `Pirttimaki2021`,
`Preston2008`, `StacksCoproduct0B1W`, and `Wang2026Packet`.
The final citation audit independently returns `ACCEPT` on this exact tuple.

The load-bearing companion Paper-9 PDF exists and re-hashes to the exact value
cited by Paper 10:
`c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02`.
It is deliberately cited as an unpublished internal-batch artifact without a
false or mutable public URL.

The retained corpus contains 12 local research PDFs and 12 adjacent preflight
sidecars; all 12 sidecars have verdict `PASS`.  The scope checksum ledger
passes 14/14 entries and the domain checksum ledger passes 10/10 entries:

| Retained-source lock | SHA-256 |
|---|---|
| `notes/sources/scope_source_manifest.md` | `38fd6557eba364eff748b35a62ac28bf768b75a259e1e7631099149f67118140` |
| `notes/sources/scope_sources.sha256` | `222c1a6d9552c82890bcc3846245fb4c636eef981a5937b7355d45f5626497aa` |
| `notes/sources/dom-source-manifest.md` | `49e20c34eff26915780f43b5df7d5b6635fa35d6225b63ea476cbeab1c14af21` |
| `notes/sources/dom-sources.sha256` | `34ed23b73f01f5027deaa5084bce250d5f77c1dbcd02c38627c950e5803d13ce` |

These PDFs are verification copies, not public-payload assets.  Citation
reproducibility does not imply redistribution permission.

## 4. Deterministic controls

The complete Paper-10 project was copied into an isolated temporary tree
before running `./experiments/reproduce.sh`.  The locked result directory was
therefore not touched.  The receipt is:

- 24/24 unit tests PASS;
- ten CSV artifacts with exactly 676 data rows;
- locked-result generation PASS and `--verify-only` PASS;
- two independently generated 11-artifact sets byte-identical to each other;
- both fresh sets byte-identical to the locked ten CSVs and manifest;
- manifest SHA-256 in all locations
  `edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215`;
  and
- zero `__pycache__` or `.pyc` artifacts.

The tests also retain the declared no-network, no-randomness, no-fitting,
no-external-dataset, and no-target-zero-data boundary.  These finite controls
are regression/falsification witnesses only and are not credited as proofs of
the infinite or source-specific theorems.

## 5. Stage-10 Route lock

Exactly seven Stage-10 Route-A YAMLs exist and no Stage-10 Route-B YAML exists.
Every Route-A file contains exactly nine frozen A2 validation fields and
`route_b_invocation_allowed: false`.  Five actual/comparison records are
`ROUTE_A_EXPLORATORY`; the two explicitly copied controls are
`ROUTE_A_REJECTED`.  Every record fails A1--A4, and no cross-owner splice is
used to invoke Route B.

| Owner | YAML SHA-256 |
|---|---|
| `DEN-EF-ACTUAL-SEPARATED-REFLECTION-P` | `57bdf64ffcdf66797ba10985082e9bcb42cd64b45bf479a5af8de4d125e123af` |
| `DEN-EF-ACTUAL-CONT-OBS-P` | `a94cc0a8fb48488de0e46bb6f30e845ee3641b5a8517da707e6b1570e212af82` |
| `DEN-EF-ACTUAL-BOREL-MFIN-P` | `be95f98692bab5eb54ef93edab64b0f0bb8bbf7c0131f7021f559c614de94b0d` |
| `DEN-EF-QP-ACTUAL-CONT-CHAR-P` | `9d846ba5577c5424da786a9b28edb471b96a2246ec91cc9d4de5c6767929c146` |
| `DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P` | `f8b9a454c6ebb14163c78ed1e6bd6c188b8a96522fff1c2ba26f3ab45e022ed1` |
| `DEN-EF-COPROD-PRIME-K0-CONTROL` | `5b78ea0199d67457b6963664d42934dde04ee93aa78cf7bd642403f81bc9b6d3` |
| `DEN-EF-COPROD-PRIME-MFIN-CONTROL` | `d38e066923abceae8ebbb382c876b08c562dcff554be465ec5a10d887ccf1aad` |

The tuples and owner classifications agree with the manuscript, project
README, paper README, and Route audit.

## 6. Figure trace and release inventory

The native-figure trace in `paper/README.md` contains two records and satisfies
the strict six-key contract mechanically: two occurrences each of
`artifact_id`, `source_data`, `transformation`, `caption_claim`,
`supported_manuscript_claims`, and `limitations`, with no missing top-level
trace key.  The two registered source hashes match the exact TikZ files and
the release ledger.  Their claim locators and limitations distinguish actual,
proxy, copied, and historical owners.

The top level of `paper/` contains only `README.md`, `manuscript.tex`,
`references.bib`, and `paper.pdf`; the only files below `paper/figures/` are
the two locked TikZ sources.  There is no `.aux`, `.bbl`, `.blg`, `.log`,
`.out`, `.toc`, `.fls`, `.fdb_latexmk`, `.synctex.gz`, Python bytecode, or
cache artifact in the release inventory.

## 7. Public source-PDF exclusion simulation

The local workspace supplied to this audit is not itself a Git worktree, so no
claim is made about a presently fetched destination index.  Instead, a byte
copy of the complete Paper-10 project, including all 12 retained source PDFs,
was placed in a fresh temporary Git repository and staged with `git add -A`.

| Temporary-index check | Result |
|---|---:|
| local `notes/sources/*.pdf` files | 12 |
| PDFs matched by `notes/sources/.gitignore` rule `*.pdf` | 12 |
| retained source PDFs in staged status | **0** |
| retained source PDFs in `git ls-files --stage` | **0** |
| staged preflight sidecars | 12 |
| staged non-PDF source-audit files | 17 |
| staged release `paper/paper.pdf` | 1 |
| staged LaTeX auxiliaries / `.pyc` / `__pycache__` | **0** |

This proves that the local exclusion rule works for a clean Paper-10 payload.
The actual post-fetch/fresh-clone index must nevertheless repeat the two
zero-source-PDF checks immediately before public synchronization, because that
destination index is external state.

## 8. Final decision and external conditions

| Gate | Result |
|---|---|
| Exact candidate and review lock | PASS |
| Explicit clean XeLaTeX/BibTeX build | PASS |
| 19-page layout-text and full-raster identity | PASS |
| Representative visual inspection | PASS |
| Fonts embedded/subset/Unicode; zero images | PASS |
| 9/9 citation and retained-source closure | PASS |
| 24/24 controls and double-fresh reproducibility | PASS |
| Seven Stage-10 Route-A records; zero Route B | PASS |
| Strict six-key figure trace and clean inventory | PASS |
| Temporary public-payload source-PDF exclusion | PASS |

**Final release decision: PASS — C0/M0/m0.**  No mathematical,
methodological, citation, reproducibility, formatting, or package blocker was
found in the exact candidate.

Three disclosed conditions remain external to this verdict:

1. The human author must confirm CRediT roles, funding, competing interests,
   acknowledgments, affiliation wording, venue, license, repository/archive
   identity, and final venue-facing AI disclosure before public or journal
   submission.
2. Paper 9 must receive an immutable public identity only after final batch
   synchronization; that identity must then be added without fabricating or
   backdating a URL, followed by a mechanical re-lock of any changed Paper-10
   bytes.
3. The final fetched destination clone must show zero tracked and zero staged
   `papers/10-separated-reflection/notes/sources/*.pdf` files immediately
   before synchronization.

Any change to a locked manuscript, bibliography, figure, PDF, README, control
manifest, or Route record reopens the affected release gate.
