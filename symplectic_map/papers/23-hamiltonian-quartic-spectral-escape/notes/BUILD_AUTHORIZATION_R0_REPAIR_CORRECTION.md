# Paper 23 — Deterministic R0 Repair-Build Authorization Correction

Date: 2026-08-25 UTC  
Stage: authorization-contract correction after the consumed failed R0 repair build  
Disposition: corrected authorization frozen for independent review; no build is open

## Purpose, scope, and exact legal effect

This record corrects one internal contradiction in the immutable
`BUILD_AUTHORIZATION_R0_REPAIR.md` and provides the strictly bounded authority
needed for one new corrected invocation after independent review and separate
parent consumption.  It is a correction of authorization only.  It is not a
waiver, a retrospective success finding, a source change, a PDF change, a
review, a build, a retry of either consumed invocation, or permission to use
an old root.

The effective future contract is the conjunction of:

1. the immutable old authorization at
   `notes/BUILD_AUTHORIZATION_R0_REPAIR.md`, SHA-256
   `d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207`,
   25,966 bytes / 428 LF / mode 0644 / root:root / link count one, ending
   exactly and uniquely with `BUILD_AUTHORIZATION_R0_REPAIR`; and
2. this correction, but only after this correction receives the independent
   review and separate parent consumption specified below.

Exactly two old rule families are superseded, and only to the extent stated
in the precedence table and replacement clauses below:

1. the raw PDF date-value requirement in item 4 of the old authorization's
   “PDF validity, metadata, safety, fonts, and visual pagination” contract;
2. the consumed-authority/no-replacement rule following the failed invocation,
   only enough to permit exactly one new corrected invocation under new roots
   after review and parent consumption, together with the mechanical opening,
   inventory, blocker-path, and success-count substitutions that are
   unavoidable consequences of that one new invocation.

Except for those two expressly delimited overrides and their listed mechanical
consequences, every old authorization conjunct is incorporated here by
reference verbatim, as though reproduced in full.  An omitted restatement is
not a deletion, weakening, waiver, or ambiguity: the unchanged old text
controls.  If this correction and the old authorization can be read together,
they must be.  If and only if they directly conflict on one of the two listed
matters, this correction controls on that matter and nowhere else.

## Issuance roots and correction-author opening state

The following are the exact roots under which the sole correction write was
authorized.  They are issuance provenance, not the future build-time roots,
because the mandatory review and parent transition will necessarily change
the two governance-root identities.

| Artifact or field | Exact issuance value |
|---|---|
| `BATCH_06_STATUS.md` SHA-256 | `3da12e60e7bf8a54b2999bb5e6730ec55c517796ad013f029c2bf2bace6bf738` |
| Status bytes / LF / mode / owner / link count | 83,765 / 1,235 / 0644 / root:root / one |
| Issuance gate | `PAPER23_R0_REPAIR_AUTHORIZATION_CORRECTION_OPEN` |
| Paper-23 issuance queue | `R0_REPAIR_BUILD_BLOCKED_AUTHORIZATION_CORRECTION_OPEN` |
| `BATCH_06_IDEA_REPORT.md` SHA-256 | `5deabcaf33e1a576aa2c7274a2db2d34940c328b9e48114af0e5ac7cd10a9ef0` |
| Idea-report bytes / LF / mode / owner / link count | 134,038 / 2,563 / 0644 / root:root / one |
| `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` SHA-256 | `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4` |
| Publication correction bytes / LF / mode / owner / link count | 8,524 / 245 / 0644 / root:root / one |
| Publication correction terminal | `PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS` |

At correction-author opening, the Paper-23 project contained exactly 30
regular files, four child directories, zero symlinks, and zero other
filesystem objects.  Every regular file was a mode-0644 root:root file with
link count one.  The project and its four child directories `experiments/`,
`notes/`, `paper/`, and `refine-logs/` were ordinary mode-0755 root:root
directories and were not symlinks.  This correction path, its future review
path, its future corrected-invocation failure path, and all nine success paths
were absent under both existence and symlink checks.

## Complete 30-file opening ledger

This bytewise-path-sorted ledger is complete.  Every row is immutable through
correction authorship, correction review, parent consumption, and the future
corrected invocation.

| Relative path | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `b37132e282cceeb04a36723d75f48c4af6f3361836067850496cf52b8ad603e8` | 6,015 | 151 | 0644 |
| `experiments/EXPERIMENT_TRACKER.md` | `85724a53e161bfbbb45af305af66454a757771330157694ff5d7f85215ffcb31` | 2,927 | 55 | 0644 |
| `experiments/publication_lock.json` | `6f1830f14413c49cad0945facc7b10c081be1a36d4884e5768205273fce200c4` | 51,578 | 1 | 0644 |
| `experiments/source_lock.json` | `5956a7e6c2e12a9be287b2ead2922e135c4a64da738757a0b55884e16974b248` | 32,889 | 1 | 0644 |
| `notes/BUILD_AUTHORIZATION_R0_REPAIR.md` | `d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207` | 25,966 | 428 | 0644 |
| `notes/BUILD_R0_BLOCKER.md` | `8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384` | 8,900 | 180 | 0644 |
| `notes/BUILD_R0_REPAIR_BLOCKER.md` | `c05d9bb243bd28cd43dee4972f5ee829d01b165b73e7b9bef25a8c4f6940f472` | 11,493 | 223 | 0644 |
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

The only write authorized to this correction author is
`notes/BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION.md` through one
`apply_patch` operation.  No source, root ledger, old authorization, blocker,
review, lock, old root, or other project byte may change; no build or temporary
root may be created.  At this author stop, the required inventory is exactly
31 regular files, four child directories, zero symlinks, and zero other
objects.

## Frozen source, metadata intent, and evidence provenance

The future build input remains exactly the same frozen trio and no other
source or asset:

| Source path | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| `paper/main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 | 1,776 | 0644 |
| `paper/math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 | 0644 |
| `paper/references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 | 99 | 0644 |

The exact opening three lines of frozen `paper/main.tex` are:

```tex
\ifdefined\pdfinfoomitdate
  \pdfinfoomitdate=1
\fi
```

Their bytes have SHA-256
`92bae6ee3706267421b56d22b63d8cf0ade4fa6addb23cd08a5388642a45fba2`.
The same source declares the exact visible title, `\author{Anonymous}`,
`\date{}`, and empty `pdfauthor`, `pdfcreator`, and `pdfproducer` fields.
This is a deliberate deterministic date-suppression contract.  It is not a
defect to repair and must not be edited.

The following evidence is mandatory and immutable:

| Role and path | SHA-256 | Bytes | LF | Required exact unique terminal |
|---|---|---:|---:|---|
| original R0 blocker, `notes/BUILD_R0_BLOCKER.md` | `8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384` | 8,900 | 180 | `R0_BLOCKED` |
| source-repair receipt, `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `a0fe52acf07aed30dc8571b86a48602e74dc7cd15105ea4d69cd701f2e80bbe4` | 15,841 | 222 | `R0_HYPERREF_SOURCE_REPAIR_FROZEN_DUAL_REVIEW_REQUIRED` |
| repaired-source R1 review, `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` | `b8c62343aa9d893d9dcc0bf73e24755d92833c294c4f4a790cd1238c886f2636` | 21,240 | 465 | `PAPER_SOURCE_R1_R0_REPAIR_PASS` |
| repaired-source R2 review, `notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md` | `075b9b6e7cc271f8abec29b08d28509df5ce7c8b6e0951753051d14a6b36c653` | 21,535 | 425 | `PAPER_SOURCE_R2_R0_REPAIR_PASS` |
| consumed repair-build authorization, `notes/BUILD_AUTHORIZATION_R0_REPAIR.md` | `d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207` | 25,966 | 428 | `BUILD_AUTHORIZATION_R0_REPAIR` |
| consumed repair-build blocker, `notes/BUILD_R0_REPAIR_BLOCKER.md` | `c05d9bb243bd28cd43dee4972f5ee829d01b165b73e7b9bef25a8c4f6940f472` | 11,493 | 223 | `R0_REPAIR_BUILD_BLOCKED` |
| publication-lock review correction, root-level `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` | `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4` | 8,524 | 245 | `PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS` |

The consumed failed invocation remains failed.  It built in retained roots
`/tmp/paper23-r0-repair-A.BzlBNd` and
`/tmp/paper23-r0-repair-B.TVRci7`, each an ordinary mode-0700 root:root
directory, and produced exit vectors `0,0,0,0`.  Its pairwise-equal command
logs and final outputs had these exact diagnostic identities:

| Failed-invocation artifact | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `command-1.log` | `1fcbc0319012bbeb4fd526dad9eef6a0ca9e86474e9c092ae766a70a4ef466ce` | 18,124 | 597 |
| `command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 |
| `command-3.log` | `cba30ead0e25a854366d5bf7e9156ffadfb713fd4de7097a43b6f284e1d2db72` | 8,363 | 158 |
| `command-4.log` | `ad3eb1bf23dd06e82b1683ccb3e66c34b142303fa24685f56f268f58368612b0` | 7,254 | 112 |
| `main.aux` | `2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb` | 14,072 | 165 |
| `main.bbl` | `baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9` | 2,881 | 73 |
| `main.blg` | `be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34` | 900 | 46 |
| `main.log` | `ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6` | 27,628 | 700 |
| `main.out` | `14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94` | 6,226 | 28 |
| `main.pdf` | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` | 492,452 | 2,724 |

These are historical diagnostic expectations only.  They neither satisfy a
future check nor authorize reuse.  Fresh corrected-invocation observations
control every acceptance decision.

## Exact old-versus-new precedence table

| Topic | Old effective clause | Corrected effective clause and boundary |
|---|---|---|
| Raw dates | Raw `CreationDate` and `ModDate` must each equal `D:20260825000000Z`. | Both date keys must be wholly absent, as specified in Replacement 1.  `SOURCE_DATE_EPOCH` remains unchanged. |
| Consumed authority | First-root creation consumed the old authorization; no retry or replacement invocation was permitted. | The old invocation remains consumed and failed.  Replacement 2 alone permits one new corrected invocation, but only after an independent correction review passes and a separate parent transition consumes both artifacts. |
| Historical blocker | The old authorization expected `notes/BUILD_R0_REPAIR_BLOCKER.md` absent at its builder opening. | For the corrected invocation that file is required present and immutable as historical evidence.  This is a mechanical consequence of Replacement 2, not a third substantive override. |
| Corrected-invocation failure path | The old failed invocation's sole failure path was `notes/BUILD_R0_REPAIR_BLOCKER.md`. | A future corrected invocation may create only `notes/BUILD_R0_REPAIR_CORRECTION_BLOCKER.md`, ending exactly `R0_REPAIR_CORRECTION_BUILD_BLOCKED`; the old blocker remains untouched.  This is a mechanical consequence of Replacement 2. |
| Inventory arithmetic | The old authorization used a 29-file prebuild and 38-file success state. | Correction author stop is 31/4/0/0; reviewed prebuild is 32/4/0/0; success is 41/4/0/0; corrected-invocation failure with its sole new blocker is 33/4/0/0.  These are mechanical consequences of Replacement 2. |
| Every other contract matter | The old authorization's exact text. | Incorporated verbatim and unchanged. |

No observation from the failed invocation is converted into a pass.  No
source or PDF byte is grandfathered.  The future invocation must reproduce
and revalidate every retained conjunct freshly.

## Replacement 1 — hard PDF date-omission requirement

For the future corrected invocation, old PDF-metadata item 4 is replaced in
full by this hard conjunct:

1. Every build child still receives exactly
   `SOURCE_DATE_EPOCH=1787616000`; the epoch remains
   2026-08-25T00:00:00Z and is recorded as build-environment provenance.
2. `pdfinfo -rawdates main.pdf` must contain no `CreationDate` key and no
   `ModDate` key at all.  A blank value, alternate spelling, differently
   formatted value, duplicate, or hidden occurrence is not absence and fails.
3. Independently decoded PDF metadata must report the creation-date and
   modification-date values as exactly empty.  Every nonzero xref, every
   trailer, every `/Info` dictionary, every object dictionary, and the raw PDF
   bytes must be scanned; `/CreationDate` and `/ModDate` must occur zero times.
4. No metadata stream, XMP packet, annotation, outline, attachment, object,
   visible text, or extracted text may contain either date key, the old raw
   value `D:20260825000000Z`, any alternate build date, or any conflicting
   creation/modification date.  The expected frozen-source result has no
   metadata stream; any stream that carries a date fails.  The document must
   display no date.
5. The title remains exactly “Four-Mode Hamiltonian Product Shears Beyond
   Cubic Collapse: Exact Degree Growth and Quartic Perron Subfamilies”, the
   visible author remains exactly `Anonymous`, and decoded PDF `Author`,
   `Creator`, and `Producer` remain each exactly empty.  All old private-text,
   action, attachment, image, encryption, form, metadata, title, authorship,
   safety, and identity-disclosure checks remain hard conjuncts unchanged.

This replacement aligns acceptance with the frozen source's explicit
`\pdfinfoomitdate=1`.  It does not permit a source edit and does not waive a
metadata check.

## Replacement 2 — one new corrected invocation, and no more

The old no-replacement rule is overridden only as follows:

1. Exactly one distinct future corrected invocation may become authorized,
   and only after the review and parent-consumption gates below.  It is a new
   invocation, not a continuation, retry, resumption, clone, or retrospective
   correction of the failed invocation.
2. Its authority is consumed when its builder first creates either one of its
   two new roots.  After that instant there is no retry, replacement builder,
   second root pair, resumption, or further invocation after either success or
   failure.  A preflight mismatch before root creation requires zero root and
   zero project write.
3. It must create exactly two brand-new private mode-0700 local roots, A and
   B, independently rather than by cloning.  It may create no third root.
   All four prior roots are excluded exactly:

   - `/tmp/paper23-r0-A.DyWKGR`;
   - `/tmp/paper23-r0-B.dsQvTx`;
   - `/tmp/paper23-r0-repair-A.BzlBNd`;
   - `/tmp/paper23-r0-repair-B.TVRci7`.

   None may be read for input, reused, written, copied from, cached from,
   linked to, renamed, or treated as fresh.  The two old diagnostic roots and
   two failed-repair roots remain immutable retained history.
4. `notes/BUILD_R0_REPAIR_BLOCKER.md` remains present at the frozen identity
   above and is required immutable.  The sole possible corrected-invocation
   failure write is
   `notes/BUILD_R0_REPAIR_CORRECTION_BLOCKER.md`, a mode-0644 root:root
   regular file with link count one whose exact unique final nonempty line is
   `R0_REPAIR_CORRECTION_BUILD_BLOCKED`.  On failure, all nine success paths
   must be absent and the resulting project inventory is exactly 33 regular
   files, four child directories, zero links, and zero other objects.  The old
   blocker may never be edited, replaced, removed, or used as the new failure
   path.
5. On success, no new failure blocker exists; the immutable old blocker stays
   present as historical evidence.  Exactly nine success paths are added to
   the 32-file reviewed prebuild, yielding exactly 41 regular files, four
   child directories, zero links, and zero other objects.

No clause here grants a second correction, a source alteration, a second
review authored by the builder, or any action after the one persistence
decision.

## Retained deterministic build and acceptance contract

Subject only to the two replacements above, the future corrected invocation
must satisfy every old authorization conjunct.  For avoidance of doubt, the
following retained requirements are cumulative summaries, not substitutes
for the incorporated verbatim text:

### Frozen inputs, roots, tools, environment, and commands

- The input is exactly the frozen source trio above.  Both fresh roots begin
  with independent mode-0644, link-count-one copies of exactly those three
  files and no other object.  Their inodes are distinct from the project and
  one another.  The project trio, both copied trios, the complete opening
  ledger, correction, review, governance roots, and evidence are hashed before
  and after and remain byte-identical.
- Each of the eight child processes inherits an empty environment populated
  with exactly six pairs and no others:

  ```text
  PATH=/usr/bin:/bin
  SOURCE_DATE_EPOCH=1787616000
  FORCE_SOURCE_DATE=1
  TZ=UTC
  LC_ALL=C
  LANG=C
  ```

- In each root, exactly once and in order, with that root as working
  directory, run:

  1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
  2. `bibtex main`;
  3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`;
  4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.

  There is no retry, fifth pass, second BibTeX run, latexmk, alternate engine
  or option, shell escape, cleanup build, package installation, network,
  source generation/edit, cache use, old-root use, figure generation,
  scientific computation, or external effect.
- Both exit vectors are exactly `0,0,0,0`.  Corresponding source copies, all
  four command logs, and all six final outputs are byte-identical between A
  and B and stable through validation.  Root freshness, canonical paths,
  modes, owners, devices, inodes, inventories, executables, environments,
  commands, working directories, exits, hashes, bytes, LF counts, and every
  direct comparison are recorded.

### Diagnostics, bibliography, bookmark, PDF, fonts, pages, and safety

- Final TeX/BibTeX/AUX/BBL/BLG/LOG/OUT state is closed.  There are exactly
  nine citation commands, nine distinct authorized citation keys, nine final
  AUX citation/bibcite identities, and nine nonduplicate BBL items under
  `plainnat` and `references`, with no missing or tenth key.  The exact set is
  `BergerTuraevHamiltonianMaps`, `BlancVanSantenAffineTriangular`,
  `DangFavreSpectralInterpretations`, `DesertiDegreeGrowthExamples`,
  `ForstnericComplexSymplectic`, `HenonOpenProblems`,
  `KochLomeliStraightLineFlows`, `RangarajanPolynomialSymplectic`, and
  `ShaoSunDimensionFour`.  All remain confined to bounded related work and
  none proves a mathematical claim.
- Final `main.log`, both command-4 logs, `main.blg`, both BibTeX streams, and
  the final state contain zero fatal error, TeX/package/hyperref PDF-string
  warning, BibTeX error/warning, undefined citation/reference, multiply
  defined or changed label, rerun warning, and overfull box.  First-pass
  convergence messages and every underfull box are counted and recorded;
  underfull boxes pass only after fresh visual proof of harmlessness.
- Final `main.out` is syntactically closed and its decoded outline contains
  safe plain `g=9`, including exactly `The restricted boundary at g=9`, with
  no raw math shift, TeX bookmark token, unresolved token, or governance text.
- Both byte-identical PDFs are structurally valid, readable on every page,
  unencrypted, action-safe, attachment-free, form-free, rich-media-free, and
  image-object-free.  They contain no JavaScript, executable action, Launch,
  SubmitForm, ImportData, embedded file, AcroForm, XFA, or private action.
  Every physical page is US Letter with rotation zero.
- Every reported font is embedded, subsetted, and Unicode mapped; zero fonts
  fails.  Title, Anonymous visible author, empty Author/Creator/Producer, and
  corrected date omission must satisfy Replacement 1 exactly.
- Fresh inspection must find exactly 23 physical pages: Abstract on page 1;
  repaired boundary subsection and Section 9 on page 20; Conclusion entirely
  on page 22; References on page 23; no appendix.  The substantive span is
  pages 1--22.  All 23 pages at readable scale, all three tables, and every
  long-display page must be inspected, with no blank page, corruption,
  clipping, collision, crowding, or overflow and with visible mathematical
  `g=9` intact.
- The three pagination judgments remain separate and exact:
  `hard_band_pass=true`, `preferred_band_pass=false`, and
  `planning_target_pass=false`.  The 22--30 hard band passes; the 24--28
  preferred band fails; the 26.00 planning target is missed by 4.00 pages.
- Source, generated text artifacts, logs, PDF text/metadata/outlines/objects,
  annotations, and links contain no unresolved marker, private path, hash,
  byte/LF identity, PASS/BLOCKED token, gate/queue, governance history,
  permission ledger, invocation/log/agent/model/tool identity, lock,
  submission instruction, or identity disclosure.  Every old security and
  private-text check remains hard.

### Strict canonical JSON and atomic success persistence

Before persistence, the accepted-root `main.pdf` must be copied to
`main_round0.pdf` and proved equal by SHA-256 and direct byte comparison.
`BUILD_METADATA_R0.json` and `BUILD_RECEIPT_R0.json` must each be strict
one-line canonical UTF-8 JSON with exactly one terminal LF: no BOM, CR,
invalid UTF-8, duplicate key at any depth, nonfinite number, trailing content,
insignificant whitespace, unordered object key, or noncanonical number.  Every
object is recursively ordered by Unicode code point, arrays retain semantic
order, and `self_identity` is exactly
`{"bytes":null,"sha256":null}`.

Each candidate must independently pass both a strict duplicate-aware Python
parser/canonical serializer and a custom Node recursive-descent parser plus
Unicode-code-point canonical serializer.  Native `JSON.parse`/
`JSON.stringify` alone is insufficient.  Both validators must reject
duplicates at every depth, invalid text, nonfinite numbers, and trailing
content; reproduce the exact candidate bytes; agree on the value tree; and
record runtime identities, adversarial rejections, round trips, and candidate
hashes.

Top-level statuses remain exactly `BUILD_METADATA_R0_REPAIR` for
`BUILD_METADATA_R0.json` and `BUILD_R0_REPAIR_PASS` for
`BUILD_RECEIPT_R0.json`.  Together the JSONs bind all old required evidence
plus this correction's final identity and terminal, its independent review's
identity and terminal, the post-consumption root-ledger identities, the
corrected build-open gate/queue, the complete 30-file opening ledger, the
31-file correction-author stop, the 32-file reviewed prebuild, all four
excluded roots, the new invocation identifier, the new authority/failure
path, every fresh build and validation observation, and the corrected date
omission result.

Only after every conjunct and both independent JSON validations pass may the
future invocation atomically persist, without overwrite, exactly these nine
new mode-0644 regular paths under `paper/`:

1. `BUILD_METADATA_R0.json`;
2. `BUILD_RECEIPT_R0.json`;
3. `main.aux`;
4. `main.bbl`;
5. `main.blg`;
6. `main.log`;
7. `main.out`;
8. `main.pdf`;
9. `main_round0.pdf`.

Persistence is success-only and all-or-nothing.  No success path may exist
before complete validation.  Any partial success paths created during a
failed persistence attempt must be removed by that invocation, leaving all
nine absent and permitting only the new corrected-invocation blocker.  The
six generated outputs come from one declared accepted fresh root, and the two
PDF paths are byte-identical.

## Required independent review and separate parent consumption

This correction does **not** open a build.  It does not itself grant a builder
permission to create even one root.

A fresh distinct reviewer must first perform a read-only audit of this
correction against the full old authorization, full failed-invocation blocker,
frozen source, evidence, root ledgers, complete opening ledger, and path
absences.  The reviewer's sole possible project write is
`notes/INDEPENDENT_BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION_REVIEW.md`.
For a pass, that artifact must bind this correction's final SHA-256, bytes,
LF, mode, owner, link count, and terminal; verify that exactly the two intended
rule families and only their mechanical consequences changed; verify all
incorporated old conjuncts; and end exactly and uniquely with
`BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION_PASS`.  A blocker produces zero
project write.  The reviewer may not compile, create a root, edit source, or
self-author a replacement.

After a passing review, the project must contain exactly 32 regular files,
four child directories, zero symlinks, and zero other objects.  All 30 opening
files and this correction remain immutable; the nine success paths and
`notes/BUILD_R0_REPAIR_CORRECTION_BLOCKER.md` remain absent.

Then and only then, a separate parent transition must validate and consume
the final correction and review.  The parent must:

1. set the current gate to exactly
   `PAPER23_DETERMINISTIC_R0_REPAIR_CORRECTION_BUILD_OPEN`;
2. set the Paper-23 queue to exactly
   `R0_REPAIR_CORRECTION_BUILD_AUTHORIZED`;
3. append the correction and review paths, SHA-256 values, byte/LF counts,
   modes, owners, link counts, and exact unique terminals to both
   `BATCH_06_STATUS.md` and `BATCH_06_IDEA_REPORT.md`; and
4. state that this is the sole new corrected invocation, that all four prior
   roots are excluded, that the old blocker remains immutable, and that the
   new authority is consumed at first fresh-root creation with no retry.

The future builder must hash the actual post-consumption root-ledger bytes,
verify that each binds both final correction and review identities and the
exact gate/queue, and freeze those root-ledger bytes for the entire invocation.
The issuance hashes in this record are provenance only and may not be treated
as post-consumption preconditions.  No builder may act before this separate
transition.

## Success, failure, custody, and prohibited effects

The future corrected invocation has exactly one persistence decision:

- **success:** exactly the nine success paths exist, the new failure blocker
  is absent, the old blocker remains immutable, and the project is exactly
  41 regular files / four child directories / zero symlinks / zero other
  objects;
- **failure after authority consumption:** none of the nine success paths
  remains, only `notes/BUILD_R0_REPAIR_CORRECTION_BLOCKER.md` may be added,
  it ends exactly `R0_REPAIR_CORRECTION_BUILD_BLOCKED`, the old blocker
  remains immutable, and the project is exactly 33/4/0/0; or
- **preflight mismatch before first-root creation:** zero root and zero
  project write, with authority not exercised and the mismatch reported to
  the parent for a new governance decision; the builder cannot repair it.

The corrected builder reports and stops after that decision and performs no
self-review.  This correction author, its reviewer, the parent consumer, and
the future builder have mutually separate custody.  No one may collapse those
roles or infer authority from an old PASS, a clean old PDF, or a retained
root.

This correction grants no source edit, theorem/proof/citation change, old-root
read or mutation, correction self-review, build self-review, R1 build, R1
review, release, finalization, Paper-24 action, submission, upload, public
hosting, repository push, network transport, external messaging, identity
disclosure, browsing, or other external effect.

BUILD_AUTHORIZATION_R0_REPAIR_CORRECTED
