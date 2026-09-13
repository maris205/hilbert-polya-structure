# Paper20 final manuscript integrity review R1

Date: 2026-08-22 UTC  
Project: `papers/20-coupled-shear-degree-matrix`  
Role: fresh, read-only final-integrity reviewer

This review was performed after the publication-stage gate.  I authored none
of the frozen source, manuscript, build, lock, authorization, or prior-review
inputs.  No compilation, BibTeX run, experiment, CAS/symbolic or numerical
run, network read, transport, upload, or other external effect was performed.
The only project write made by this review is this note, after all checks below
passed.  Temporary inspection files, where used, were outside the project
tree.

## Frozen identity and lock rehash

The principal byte identities were independently recomputed:

| object | bytes / LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 61,835 / 1,619 | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/main_round1.pdf` | 429,723 / binary | `07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40` |
| `paper/BUILD_RECEIPT_R1.json` | 11,325 / 1 | `0c0ce98b3ee4349d269aaebacf78d89ad237aec4f36595a02d268c2fdf78cc31` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 6,206 / 1 | `d8600e8d50efcda1b694e332a5b4282beb8b6c9ad9b5f302199f6f1aba728d3a` |
| `experiments/source_lock.json` | 11,847 / 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |
| `experiments/publication_lock.json` | 12,382 / 1 | `4559e4947613b70eda65523f83d5c1f369199c77852af3cc1940afa7ecbf0eff` |
| `notes/PUBLICATION_STAGE_SCOPE.md` | 14,472 / 299 | `875c615b00aa98ffc3a290548582762fc321907d19ed338741de58456b2133e2` |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | 9,484 / 213 | `937612e3810c99eda8e9499abaa188b1d5b4d8421c7d8c260188d2d4b1481e02` |

The source lock's ten-file author aggregate was replayed using its prescribed
byte framing and byte-sorted relative POSIX paths.  It independently gives
SHA-256 `3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`,
45,416 bytes, and 873 LF bytes, exactly matching the lock.  Every allowlisted
author file has matching size, LF count, and digest.

`source_lock.json`, `publication_lock.json`, and `BUILD_RECEIPT_R1.json` were
parsed with duplicate-key rejection and nonfinite-number rejection.  Each is
UTF-8, has no BOM, CR, or NUL, exactly one terminal LF, and its byte string is
exactly the recursive Unicode-code-point key-sorted JSON serialization with
`,:` separators.  Self-excluded identity fields are the required null values;
no self-reference or duplicate key was found.

The 57 non-self entries in the publication inventory were independently
rehashed; all exist and every recorded byte count, LF count, and SHA-256
matches.  The two unlisted files are the self-excluded publication lock and
the pre-existing publication-stage review.  The final-integrity note is the
only new project path from this review.  The tree has no symlinks and no
unexpected directory.  Forbidden `code`, `data`, `figures`, `manuscript`,
`results`, `transport`, and `build` directories are absent, including their
paper-local forms.

## Authorization and receipt chain

`notes/SOURCE_PAGEFIX_AUTHORIZATION_R1.md` is byte-bound by the source-revision
receipt and terminates with `SOURCE_PAGEFIX_AUTHOR_STOP`.  The source revision
receipt binds the page-fixed `main.tex`, unchanged notation, bibliography,
plan, and source lock, and records no build, CAS, data, experiment, network,
publication, transport, or upload.  Its pagefix authorization and all source
bindings match the live files.

The four-command deterministic R1 page-fixed build is represented by
`BUILD_RECEIPT_R1.json`, whose live digest is the value above and whose status
is `BUILD_R1_PAGEFIX_PASS`.  Its source bindings, receipt identity, and
persisted candidate PDF binding all match current bytes.  The receipt records
two isolated roots, byte-identical root outputs, no source edits during build,
and no network access.  The two fresh source page-fix reviews terminate with
`PAPER_SOURCE_R1_PAGEFIX_PASS` and `PAPER_SOURCE_R2_PAGEFIX_PASS`; the two
fresh page-fixed build reviews terminate with `BUILD_R1_PAGEFIX_PASS` and
`BUILD_R2_PAGEFIX_PASS`.  The publication-stage scope and lock are unchanged
from their recorded hashes, and the prior publication review terminates with
`PUBLICATION_STAGE_PASS`.

## Static TeX, labels, citations, and proof spine

The source has 67 unique labels (no duplicate labels), and every `ref`,
`eqref`, and `pageref` target resolves to a declared label.  The seven citation
keys used in the source are exactly the seven bibliography keys:
`FriedlandMilnor1989`, `Deserti2018`, `GuedjSibony2002`, `FavreJonsson2011`,
`DangFavre2021`, `Fujioka2023`, and `HenonSurvey2024`.  There are no missing
citation keys or undefined cross-reference diagnostics.

The frozen theorem and proof spine are present and source-consistent:

* algebraically closed characteristic-zero `K`, integer `g\ge5`, and the
  stated potentials `V=q_1^2q_2^2+q_1^g` and
  `W=p_1^2p_2^2+p_2^g`;
* triangular inverses, symmetric-Hessian symplecticity, and the block-Jacobian
  check;
* the phase selectors
  `A_g=((g-1,0),(2,1))` and `B_g=((1,2),(0,g-1))`, with carried-coordinate
  gaps and phase-labelled inequalities;
* the complete-step matrix
  `C_g=B_g A_g=((g+3,2),(2(g-1),g-1))`, rather than an uncorrected half-step
  matrix;
* two-stage half-open cone invariance, simultaneous carried-term induction,
  and coefficientwise no-cancellation in characteristic zero;
* exact recurrence `u_n=C_g^n(1,1)^T`, visibility of total degree through the
  second `q` coordinate, Perron accessibility, and
  `lambda_1(F_g)=rho(C_g)=(sqrt(g)+1)^2`;
* `deg(S)=deg(T)=g-1` and the strict comparison
  `(sqrt(g)+1)^2<(g-1)^2` for `g\ge5`.

The source explicitly limits “non-product” to the displayed coordinate
support and degree comparison.  It does not promote context citations to
proof or priority evidence and does not assert the locked anti-claims:
arbitrary supports/coefficients/words/characteristic, a generic Newton-fan or
all-automorphism classification, entropy equalities, periodic/trace/multiplier
or invariant-curve/centralizer/torus results, arithmetic or effective orbit
results, numerical/CAS certificates, universal product or non-conjugacy
claims, or absolute novelty/firstness/priority.  Occurrences of these terms
are only explicit scope exclusions and hard-stop statements.

## PDF, page, diagnostics, and fonts

Read-only PDF inspection independently reports 23 pages, Letter size, no
encryption, no JavaScript, and metadata `Title: Coupled Hamiltonian Shear
Degree Matrices in A4`, `Author: Anonymous Authors`.  The exact page contract
holds: substantive body through the conclusion ends on page 22, the
`References` heading begins on page 22, and the total is 23 pages; no appendix
or supplementary content is present.

The receipt's final-build diagnostics are independently corroborated by the
retained log and PDF readback: fatal errors 0, undefined citations 0,
undefined references 0, overfull boxes 0, and marker hits `TODO=0`, `FIXME=0`,
`TBD=0`, `VERIFY=0`, `??=0`, `[?]=0`.  The recorded three underfull boxes, one
label-change warning, and four hyperref PDF-string warnings are nonfatal and
explicitly accounted for.  BibTeX warnings are 0.  `pdffonts` reports 25 font
rows; every row is embedded, subset, and Unicode-mapped.

Extracted PDF text contains no draft marker, unresolved-reference marker,
private provenance, digest, local path, dashboard, agent/model name, or
lifecycle token.  The sole raw-PDF `/Root` occurrence is the PDF structural
catalog name, not a filesystem path.  Public identity is anonymous in both
source and metadata: `Anonymous Authors`, empty source date, and the frozen
title only.

## Scientific and external-effect boundary

The publication lock and build/source receipts consistently record zero
scientific experiments, CAS/symbolic runs, numerical runs, datasets, generated
assets, code/data artifacts, and result files.  Permissions remain false for
build, CAS, experiments, network reads, publication, release, submission,
transport, and upload.  No external or scientific effect is implied by this
integrity review.

All final-integrity checks passed.  No blocker was found, and this note does
not authorize source edits, recompilation, experiments, release, submission,
transport, or upload.

FINAL_MANUSCRIPT_INTEGRITY_PASS
