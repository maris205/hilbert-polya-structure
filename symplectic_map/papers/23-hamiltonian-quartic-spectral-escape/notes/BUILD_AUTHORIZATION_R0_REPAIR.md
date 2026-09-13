# Paper 23 — Deterministic R0 Repair-Build Authorization

Date: 2026-08-25 UTC  
Stage: repaired-source deterministic R0 build  
Disposition: exactly one distinct one-shot build invocation is authorized after parent consumption; all source is frozen

## Scope, issuance provenance, and future build-open roots

This note authorizes one distinct build author to perform exactly one local
Paper-23 R0 repair-build invocation. The invocation comprises two fresh
independent builds, the acceptance audit, construction and validation of the
two success JSON candidates, and one success-or-failure persistence decision.
Authority is consumed when the build author first creates either new build
root. It may not be split, resumed by another author, retried after either
success or failure, or reused. A preflight mismatch before root creation grants
no build authority: the author must create no root, write nothing, report the
mismatch, and stop.

The following values describe the authorization author's opening/issuance
state. They are immutable historical provenance, not predicted build-time
root values.

| Issuance artifact or field | Exact issuance value |
|---|---|
| `BATCH_06_STATUS.md` SHA-256 | `2742e8424d2a88ce3137be0aad2b07a9c2ea4b91fb837e0a91603e65352e9271` |
| `BATCH_06_STATUS.md` bytes / LF / mode / owner | 79,107 / 1,171 / 0644 / root:root |
| Issuance gate | `PAPER23_R0_REPAIR_BUILD_AUTHORIZATION_OPEN` |
| Paper-23 issuance queue | `R0_REPAIRED_SOURCE_DUAL_PASS_PENDING_BUILD_AUTHORIZATION` |
| `BATCH_06_IDEA_REPORT.md` SHA-256 | `86dcb1fda46fd2df77633fc56230555250d32000bdbadc7bf4781c60c7646f2c` |
| `BATCH_06_IDEA_REPORT.md` bytes / LF / mode / owner | 123,861 / 2,385 / 0644 / root:root |
| `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` SHA-256 | `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4` |
| Correction bytes / LF / mode / owner | 8,524 / 245 / 0644 / root:root |
| Correction exact terminal line | `PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS` |

Before any builder acts, a separate parent transition must validate and
consume this final authorization. That transition, not the builder, must:

1. set the `BATCH_06_STATUS.md` current gate to exactly
   `PAPER23_DETERMINISTIC_R0_REPAIR_BUILD_OPEN`;
2. set the Paper-23 queue to exactly `R0_REPAIR_BUILD_AUTHORIZED`; and
3. append this note's path, final SHA-256, byte count, LF count, mode, and
   exact terminal line to both `BATCH_06_STATUS.md` and
   `BATCH_06_IDEA_REPORT.md`.

That required transition necessarily changes the issuance-time status and
idea-report hashes above. At invocation start, the builder must instead hash
the actual post-consumption versions of those two roots, record their paths,
SHA-256 values, byte/LF counts, modes, owners, and exact terminal lines,
verify the exact build-open gate and queue, and verify that both roots bind
this note's final identity. Those then-current bytes must remain frozen for
the whole invocation. The issuance hashes are provenance and must never be
mistaken for build-time preconditions. The correction root remains an exact
immutable precondition at the identity above.

The authorization path is
`papers/23-hamiltonian-quartic-spectral-escape/notes/BUILD_AUTHORIZATION_R0_REPAIR.md`.
At build opening the project must contain exactly 29 regular files, four
child directories, zero symlinks, and zero other filesystem objects: the 28
unchanged issuance files below plus this note. This note must be mode 0644,
link count one, and end exactly and uniquely with
`BUILD_AUTHORIZATION_R0_REPAIR`. The builder must bind its final path,
SHA-256, bytes, LF, mode, owner, link count, and terminal before creating a
build root, record those values without writing a success path, and later
place the same binding in both success JSON candidates.

## Complete 28-file issuance ledger and permissions

At issuance the project had exactly 28 regular files, four child directories,
zero symlinks, and zero other objects. Every file was a mode-0644 root:root
regular file with link count one. The following bytewise-path-sorted ledger is
complete; every row is a hard build precondition and remains immutable.

| Relative path | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `b37132e282cceeb04a36723d75f48c4af6f3361836067850496cf52b8ad603e8` | 6,015 | 151 | 0644 |
| `experiments/EXPERIMENT_TRACKER.md` | `85724a53e161bfbbb45af305af66454a757771330157694ff5d7f85215ffcb31` | 2,927 | 55 | 0644 |
| `experiments/publication_lock.json` | `6f1830f14413c49cad0945facc7b10c081be1a36d4884e5768205273fce200c4` | 51,578 | 1 | 0644 |
| `experiments/source_lock.json` | `5956a7e6c2e12a9be287b2ead2922e135c4a64da738757a0b55884e16974b248` | 32,889 | 1 | 0644 |
| `notes/BUILD_R0_BLOCKER.md` | `8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384` | 8,900 | 180 | 0644 |
| `notes/CITATION_VERIFICATION.md` | `fcf71a2364fe6b1624ac99189dd61a6655551928989a75bd2b338cea3d059da6` | 7,269 | 90 | 0644 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `e3d6165b7429880cbe4407c6918ce25d6d8872ee05a48dfe457b5559f4df48c6` | 7,107 | 123 | 0644 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `d491d6fa2fe3ca0d5b03195006f86021f65f6cf56529f592b46730086504b2d9` | 22,954 | 651 | 0644 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` | `b8c62343aa9d893d9dcc0bf73e24755d92833c294c4f4a790cd1238c886f2636` | 21,240 | 465 | 0644 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `aad55320dc0645931be2c0019327cd4255aaa56d77f94cd48e1a3702b10fb9bb` | 30,329 | 785 | 0644 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md` | `075b9b6e7cc271f8abec29b08d28509df5ce7c8b6e0951753051d14a6b36c653` | 21,535 | 425 | 0644 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `0ecfdc71a2de08e37311cb4683e393e397bb8e87854b01eb021a7db7f4d46dec` | 23,481 | 633 | 0644 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `8711ba1e5e6daaef5c008f773cd5a5a0751eb1794b8595befc4c8bd5e4df88fb` | 15,589 | 483 | 0644 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `c6ae173c45d0e8fbe073395abf366a33e3f4b24bf97c1ab97ad39cdb245e356e` | 17,851 | 441 | 0644 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `8828364af81e829ee13201e5e8c63b1b92cb33df462c598ec3b615057545ec8c` | 23,668 | 586 | 0644 |
| `notes/NOVELTY_ASSESSMENT.md` | `3ba35e3a336360e22f054c4821801c9b55e61dd4e9bc50e6aa57150dbca59dca` | 6,992 | 141 | 0644 |
| `notes/PROOF_PACKAGE.md` | `0d0ffb5a7d540c987d37a93ec38c7a7736ac8445f6a82c5096e471ebcc34c040` | 24,560 | 1,184 | 0644 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `fa0aef81669da75eacbe604614d86ae4a18610ef2ce70ba58391a47657f29b31` | 44,575 | 1,269 | 0644 |
| `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `a0fe52acf07aed30dc8571b86a48602e74dc7cd15105ea4d69cd701f2e80bbe4` | 15,841 | 222 | 0644 |
| `notes/RESEARCH_QUESTION.md` | `3cd1e22973e443c47a1672a82431c14c3b86ceba685330234d19085e65acdb5c` | 5,492 | 135 | 0644 |
| `notes/SOURCE_R1_ABSTRACT_INTEGER_REPAIR.md` | `f5bea1184027da2afe9c1cc6810c000b72fb058cc6cb527a30222866b521ef3b` | 8,168 | 136 | 0644 |
| `paper/PAPER_PLAN.md` | `fa7e5a7ea6693b0d8ef10651da317d253f5a1ba199e3b026a3b92c8104b6c974` | 44,881 | 799 | 0644 |
| `paper/main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 | 1,776 | 0644 |
| `paper/math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 | 0644 |
| `paper/references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 | 99 | 0644 |
| `refine-logs/FINAL_PROPOSAL.md` | `aa1221ef198ed1fe8c21da2e24107efb5671cc0f4fb70a7cd657a21c73e1f47b` | 5,531 | 185 | 0644 |
| `refine-logs/INITIAL_PROPOSAL.md` | `485fd5b98e69338aae9a681548ac906e698d98adcd3af8dbf9e42622df9471b4` | 5,158 | 146 | 0644 |
| `refine-logs/REVIEW_SUMMARY.md` | `c02b85e92727134a2cd65789c4034bbef7c047811d3e03314c9e598e5a054bf3` | 4,395 | 101 | 0644 |

The project root and its four child directories `experiments/`, `notes/`,
`paper/`, and `refine-logs/` were ordinary root:root directories, mode 0755,
not symlinks. At issuance each of these paths was absent under both an
existence check and a symlink check:

1. `notes/BUILD_AUTHORIZATION_R0_REPAIR.md`;
2. `notes/BUILD_R0_REPAIR_BLOCKER.md`;
3. `paper/BUILD_METADATA_R0.json`;
4. `paper/BUILD_RECEIPT_R0.json`;
5. `paper/main.aux`;
6. `paper/main.bbl`;
7. `paper/main.blg`;
8. `paper/main.log`;
9. `paper/main.out`;
10. `paper/main.pdf`; and
11. `paper/main_round0.pdf`.

At builder opening, item 1 must be this final note and the other ten paths
must still be absent. All 28 ledger files, directory identities and modes,
the correction root, and the actual post-consumption root-ledger bytes must
remain unchanged throughout the invocation.

## Frozen build input and review provenance

The build input is exactly the following trio and no other source or asset.

| Source path | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| `paper/main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 | 1,776 | 0644 |
| `paper/math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 | 0644 |
| `paper/references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 | 99 | 0644 |

The required immutable blocker, repair, and independent-review evidence is:

| Role and path | SHA-256 | Bytes | LF | Exact unique terminal line |
|---|---|---:|---:|---|
| old blocker, `notes/BUILD_R0_BLOCKER.md` | `8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384` | 8,900 | 180 | `R0_BLOCKED` |
| repair receipt, `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `a0fe52acf07aed30dc8571b86a48602e74dc7cd15105ea4d69cd701f2e80bbe4` | 15,841 | 222 | `R0_HYPERREF_SOURCE_REPAIR_FROZEN_DUAL_REVIEW_REQUIRED` |
| R1 repaired-source review, `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` | `b8c62343aa9d893d9dcc0bf73e24755d92833c294c4f4a790cd1238c886f2636` | 21,240 | 465 | `PAPER_SOURCE_R1_R0_REPAIR_PASS` |
| R2 repaired-source review, `notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md` | `075b9b6e7cc271f8abec29b08d28509df5ce7c8b6e0951753051d14a6b36c653` | 21,535 | 425 | `PAPER_SOURCE_R2_R0_REPAIR_PASS` |

Every identity, count, mode, and required terminal in the frozen-source and
evidence tables immediately above must be verified before first-root creation
and again after validation. The prior
diagnostic roots `/tmp/paper23-r0-A.DyWKGR` and
`/tmp/paper23-r0-B.dsQvTx` are immutable excluded history. They must never be
reused, written, copied from, cached from, linked to, or treated as either
fresh root. Their prior outputs are expectations only; fresh observations
under this invocation control acceptance.

## Exactly two fresh independent builds

The invocation must create exactly two new private local build roots, A and
B. Each must have a unique canonical absolute path, must not have existed
before this invocation, must be created independently rather than cloned,
must be an ordinary directory of mode 0700, and must not be either excluded
diagnostic root. No third build root is authorized. The two roots may not
share any source, log, or output by symlink or hard link.

Before command 1, each root must contain exactly three regular files named
`main.tex`, `math_commands.tex`, and `references.bib`: independent byte
copies from the exact frozen trio. The copies must be mode 0644, link count
one, have distinct inodes from the project and other root, and match all
three frozen identities. No directory, figure, image, asset, lock, project
note, AUX state, format, cache, command log, or other file may initially be
present.

Every one of the eight build child processes must inherit an empty
environment populated with exactly these six pairs and no others:

| Name | Exact value |
|---|---|
| `PATH` | `/usr/bin:/bin` |
| `SOURCE_DATE_EPOCH` | `1787616000` |
| `FORCE_SOURCE_DATE` | `1` |
| `TZ` | `UTC` |
| `LC_ALL` | `C` |
| `LANG` | `C` |

With each root as the exact working directory, run this sequence exactly
once and in order:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
2. `bibtex main`;
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.

A supervising harness may capture merged stdout/stderr as `command-1.log`
through `command-4.log` in the same root, provided it does not alter command,
arguments, environment, working directory, stream bytes, or exit status.
There is no retry, fifth TeX pass, second BibTeX pass, cleanup build, latexmk,
engine substitution, alternate option, shell escape, package installation,
cache use, network access, source generation, source edit, CAS/scientific
computation, figure generation, or external effect. Read-only hashes, strict
JSON validation, and PDF/log inspection required below are allowed.

## Conjunctive acceptance contract

Success requires every conjunct below. No clean PDF, prior diagnostic fact,
waiver, or reviewer judgment compensates for a false, missing, ambiguous, or
unrecorded conjunct.

### Execution, immutability, and two-root determinism

1. The exit vector is exactly `0,0,0,0` in root A and `0,0,0,0` in root B.
2. Hash the project trio immediately before copying and after all work; hash
   each copied trio before command 1 and after command 4 and all validation.
   Every identity remains exactly frozen.
3. After command 4, both roots contain readable nonempty `command-1.log`
   through `command-4.log` and final `main.aux`, `main.bbl`, `main.blg`,
   `main.log`, `main.out`, and `main.pdf`. Read-only identities of all four
   logs and all six outputs are stable from the beginning to the end of
   validation.
4. Corresponding copies of all three sources, four command logs, and six
   final outputs are byte-identical between A and B. Paired command-log
   equality is by command index; different stages need not equal one another.
5. Record exact SHA-256 and byte counts for both copies of all sources, logs,
   and outputs; LF counts for text artifacts; both canonical root paths,
   creation/freshness evidence, modes, ownership and inodes; initial
   inventories; executable resolution and identities; command arrays,
   environments, working directories, and exits.

### AUX, bibliography, OUT, and diagnostic closure

1. The final AUX, references, labels, citations, `plainnat` style, and
   `references` database are closed. The source has exactly nine citation
   commands and nine distinct keys, the AUX has exactly the corresponding
   nine final citation/bibcite identities, and the BBL has exactly nine
   nonduplicate bibliography items, with no missing or tenth key. The exact
   key set is:
   `BergerTuraevHamiltonianMaps`,
   `BlancVanSantenAffineTriangular`,
   `DangFavreSpectralInterpretations`,
   `DesertiDegreeGrowthExamples`,
   `ForstnericComplexSymplectic`,
   `HenonOpenProblems`,
   `KochLomeliStraightLineFlows`,
   `RangarajanPolynomialSymplectic`, and
   `ShaoSunDimensionFour`.
   All nine citations remain confined to the bounded related-work context;
   none is used as proof of a gradient, selector, cone, carry, leading-form,
   visibility, matrix, quartic, irreducibility, kernel, or boundary claim.
2. Final `main.blg` and both command-2 logs have zero BibTeX error and zero
   BibTeX warning. Every citation is defined, every bibliography entry is
   cited, and every cross-reference is resolved.
3. Final `main.out` is syntactically readable and closed. Its decoded outline
   contains the repaired safe plain bookmark text `g=9`, including the exact
   repaired subsection `The restricted boundary at g=9`, and contains no raw
   failed math shift, TeX bookmark token, unresolved token, or private
   governance text.
4. Every command log has zero fatal error. Final `main.log` and both
   command-4 logs have zero LaTeX warning, package warning, hyperref
   PDF-string warning, undefined citation/reference warning,
   multiply-defined-label warning, changed-label/rerun warning, and overfull
   box. First-pass convergence messages must be counted and recorded but must
   be absent from the final state.
5. Count every underfull box separately in each command log and final log,
   recording complete locations and text. Underfull boxes are acceptable only
   when every other conjunct passes and the corresponding rendered region is
   freshly shown visually harmless: no clipping, collision, corruption, or
   overflow. A copied prior count is not evidence.
6. Source, AUX/BBL/BLG/LOG/OUT, logs, extracted text, metadata, and bookmarks
   contain no unresolved or private marker, including `TODO`, `TBD`, `FIXME`,
   `VERIFY`, placeholder/citation-needed text, `??`, unresolved citation or
   reference tokens, gate/queue values, hashes, review/build instructions, or
   private project paths.

### PDF validity, metadata, safety, fonts, and visual pagination

1. Both PDFs are structurally valid and readable on every page, unencrypted,
   and byte-identical. They contain no JavaScript, executable/action script,
   Launch/SubmitForm/ImportData action, attachment, embedded file, form,
   AcroForm, XFA, rich media, or image object. Ordinary internal navigation
   must not expose or execute any private action. Every physical page is US
   Letter with rotation zero.
2. Every reported font is embedded, subsetted, and Unicode mapped; a
   zero-font result fails.
3. The decoded title is exactly “Four-Mode Hamiltonian Product Shears Beyond
   Cubic Collapse: Exact Degree Growth and Quartic Perron Subfamilies”. The
   visible author is exactly `Anonymous`. Decoded PDF `Author`, `Creator`, and
   `Producer` values are each exactly empty.
4. `SOURCE_DATE_EPOCH=1787616000` is 2026-08-25T00:00:00Z. Raw
   `CreationDate` and `ModDate` are each exactly `D:20260825000000Z`, with no
   visible document date and no conflicting metadata date.
5. Visible text, extracted text, metadata, outlines, annotations, links, and
   objects contain no private governance text or action: no project or
   temporary path, hash, byte/LF identity, PASS/BLOCKED token, gate/queue,
   review/build history, permission ledger, invocation identifier, command
   log, author/reviewer/agent/model/tool identity, lock, release/submission
   instruction, or identity disclosure.
6. Fresh inspection must establish exactly 23 physical pages. The Abstract
   starts on physical page 1; the repaired subsection heading starts on page
   20; the Section 9 heading starts on page 20; Conclusion starts and ends on
   page 22; References starts on page 23; and no appendix exists. The
   inclusive substantive Abstract-through-end-of-Conclusion span is therefore
   physical pages 1--22, exactly 22 pages.
7. The frozen acceptance threshold from the open R0 gate is the hard 22--30
   inclusive substantive-page band, which the expected 22-page span satisfies.
   The preferred 24--28 band is not satisfied, and the 26.00-page planning
   target is missed by 4.00 pages. Both JSONs and the handoff must record these
   three statuses separately and honestly: `hard_band_pass=true`,
   `preferred_band_pass=false`, and `planning_target_pass=false` (or exact
   semantically equivalent fields). Preferred/target misses are recorded
   facts, not silently relabeled as passes and not substituted for the frozen
   hard acceptance threshold. Fresh page/boundary observations control; any
   mismatch with the exact 23-page/locus contract fails this invocation.
8. Render and visually inspect every one of all 23 pages at readable scale,
   including all three tables and each page containing a long display. Record
   page-by-page evidence. No page may be blank, corrupt, clipped, crowded past
   its page boundary, or affected by table/formula/text overflow; the repaired
   visible heading must still render mathematically as `g=9`.
9. Before persistence, create `main_round0.pdf` as a byte copy of the accepted
   PDF, then prove it equal to `main.pdf` by SHA-256 and direct byte comparison.

## Strict canonical JSON and success-only persistence

No success path may exist until every preceding conjunct has passed. JSON
candidates and the PDF copy must be staged only after build validation inside
one of the two private roots; no third build root or project staging path is
authorized.

`BUILD_METADATA_R0.json` and `BUILD_RECEIPT_R0.json` must each be strict
one-line canonical UTF-8 JSON:

- no BOM, CR, invalid UTF-8, duplicate key at any depth, nonfinite number,
  trailing content, or insignificant whitespace;
- compact separators, exactly one terminal LF, and no other line break;
- every object key recursively ordered by increasing Unicode code point,
  including every nested `checks` and evidence object; arrays retain semantic
  order and finite numbers use one canonical representation; and
- `self_identity` has exactly the recursively ordered content
  `{"bytes":null,"sha256":null}`. A JSON artifact may not claim a circular
  non-null identity for itself.

The top-level status is exactly `BUILD_METADATA_R0_REPAIR` in
`BUILD_METADATA_R0.json` and exactly `BUILD_R0_REPAIR_PASS` in
`BUILD_RECEIPT_R0.json`.

Each candidate must independently pass (a) a strict duplicate-aware Python
parser/canonical serializer and (b) a custom Node recursive-descent parser and
Unicode-code-point canonical serializer, or two genuinely independent
equivalents. Both must reject duplicate keys at every depth, nonfinite values,
invalid text and trailing content, recursively canonicalize every object,
append one LF, and reproduce the candidate bytes exactly. Native
`JSON.parse`/`JSON.stringify` alone is insufficient. The two value trees must
agree; parser/runtime identities, adversarial rejection tests, round-trip
results, and candidate SHA-256 values must be recorded before persistence.

Together the JSONs must bind, without an unrecorded side ledger:

- this authorization's final identity and terminal; the historical issuance
  roots above; the correction root; both actual post-consumption root-ledger
  identities and terminals; the exact build-open gate/queue; proof that both
  ledgers bind this authorization; and a one-shot invocation identifier;
- the complete 28-file opening ledger, authorization-added 29-file prebuild
  inventory, directory/permission/link/absence checks, and all pre/post
  immutability checkpoints;
- the source trio in the project and both roots before/after; old blocker,
  repair receipt, and both repaired-source reviews with identities and
  terminals; and the exclusion of both old diagnostic roots;
- fresh-root creation/independence evidence, paths, modes, ownership, inodes,
  initial inventories, executable identities, exact environment, commands,
  working directories, exits, source/log/output identities, stability, and
  every A/B byte comparison;
- all AUX/bibliography/OUT/log, warning, underfull/overfull, unresolved-marker,
  PDF validity/security/image/action, metadata/date/title/author, font,
  page/body/band, every-page/table visual, private-text, citation-context, and
  strict-parser checks with observed counts and evidence; and
- the exact granted/denied filesystem authority, chosen persistence source
  root, all-or-nothing decision, and `main.pdf`/`main_round0.pdf` equality.

Only after all conjuncts and both JSON validations pass may the invocation
atomically persist exactly these nine new mode-0644 regular files into
`paper/`, without overwriting any pre-existing path:

1. `BUILD_METADATA_R0.json`;
2. `BUILD_RECEIPT_R0.json`;
3. `main.aux`;
4. `main.bbl`;
5. `main.blg`;
6. `main.log`;
7. `main.out`;
8. `main.pdf`; and
9. `main_round0.pdf`.

The six generated build outputs come from one declared accepted root and
must retain their validated bytes. The two PDF paths are byte-identical.
Persistence is all-or-nothing. If it fails, the builder may remove only
partial success paths created by this invocation, leaving none of the nine.
On success the project has exactly 38 regular files (29 prebuild plus nine),
four child directories, zero symlinks, and zero other objects; all prebuild
files and both post-consumption root ledgers remain byte-identical to their
invocation-start checkpoints; and no repair-build blocker exists. The two
private roots are retained unchanged after the final checkpoint for the
separately authorized independent review.

## Failure rule and handoff

Any false, missing, ambiguous, or unrecorded precondition or acceptance
conjunct is failure. None of the nine success paths may remain. The only
project path a failed invocation may create is
`notes/BUILD_R0_REPAIR_BLOCKER.md`; if created, it must be a standalone
factual record whose exact unique final nonempty line is
`R0_REPAIR_BUILD_BLOCKED`. The old `notes/BUILD_R0_BLOCKER.md` is immutable
and may never be edited, replaced, or deleted. Whether or not the optional
new blocker is written, authority was consumed at first-root creation. No
repair, source edit, second root pair, retry, or replacement invocation is
authorized.

The builder must report and stop after the persistence decision. Its handoff
must include all bound identities, terminals, permissions, inventories,
actual post-consumption root identities and authorization bindings, root
paths, commands/environments/exits, logs/outputs, warnings/boxes, citation and
bibliography closure, PDF security/fonts/metadata/page/body/band/visual facts,
JSON parser results and identities, and either all nine persisted identities
or the sole optional blocker identity. The builder performs no self-review.

A successful build makes a fresh independent R0-repair build review eligible
as the next lifecycle check, but does not authorize the builder to perform it.
This note grants no self-review, source revision, R1 build, R1 review,
release, finalization, Paper-24 action, submission, upload, transport,
repository push, messaging, identity disclosure, browsing, or external
effect.

BUILD_AUTHORIZATION_R0_REPAIR
