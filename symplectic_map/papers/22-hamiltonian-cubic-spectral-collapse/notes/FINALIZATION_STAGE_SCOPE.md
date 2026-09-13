# Paper 22 Finalization Stage Scope

Date: 2026-08-24 UTC

Project: `papers/22-hamiltonian-cubic-spectral-collapse`

Public title: **Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number**

## 1. Authority and exact opening state

The fresh independent build R2 review is
`notes/INDEPENDENT_BUILD_R2_R1_REVIEW.md`, SHA-256
`55b461472be87451a05dbff06eee5bfa2a5890f5d0d4984c89e5c8c01301b7ad`,
25,497 bytes, 408 LF, ending exactly `BUILD_R2_R1_PASS`. This scope
freezes the exact after-R2 project universe and defines a local-only,
five-role finalization protocol. Its creation does not copy a PDF, compile or
render source, create a release manifest or terminal receipt, clean temporary
evidence, perform a terminal review, or produce any external effect.

The two root ledgers at opening are separately frozen as follows:

| Root ledger | SHA-256 | Bytes | LF | Required live state |
|---|---|---:|---:|---|
| `BATCH_06_STATUS.md` | `eef237f68d04019ecd541efeb12750386d9057dfa9845af50b73f5879ab260f4` | 38,477 | 594 | gate `PAPER22_FINALIZATION_GOVERNANCE_OPEN`; Paper 22 queue `BUILD_R2_R1_PASS_PENDING_FINALIZATION_GOVERNANCE` |
| `BATCH_06_IDEA_REPORT.md` | `e1faae9ad2a55fc0ca5d807f9ac9e2ed8dea4b69a639200ccd6d140b362125d5` | 48,919 | 956 | append-only through the Paper 22 independent build R2 PASS addendum |

The finalization-governance author may write exactly this file and then
`experiments/finalization_lock.json`, in that order, validate them read-only,
and stop. The stable identity of this scope is computed before the lock is
written. This scope binds the future lock only by its safe path, role, order,
schema, strict-canonical contract, and self-exclusion rule; it cannot bind
future bytes. The lock must bind this completed scope externally and must
leave its own hash and byte count null.

Source or bibliography edits, manuscript revision, build commands, PDF
copying, manifest or receipt authoring, rendering, cleanup, creation of a
later-stage path, ledger edits, scientific or CAS execution, network access,
submission, upload, public hosting, repository push, external messaging,
identity disclosure, Paper 23 work, and every other external effect are
unauthorized in this role.

## 2. Exact frozen project universe F45

`F45` is the complete project universe immediately before this scope was
created: 45 regular non-symlink files; exactly four child directories
(`experiments`, `notes`, `paper`, `refine-logs`); zero symlinks; and zero
other filesystem entry types. Paths are unique safe project-relative paths
in lexicographic byte order. LF counts byte `0a`, including in PDFs.

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `914542c082f3bc65c47db822c6d7d3bceca8b55041117548b10b1cef96cc2873` | 5812 | 146 |
| `experiments/EXPERIMENT_TRACKER.md` | `07c147aaa323bb7d445d3fb669a9c75b896a006f53aed1d8f11e3e0637d35f4c` | 3318 | 63 |
| `experiments/publication_lock.json` | `3d7eb3c7ef143a17c1ccdb82ece985a05c916b78c1ebe0591bca8af3c05ce6cd` | 34222 | 1 |
| `experiments/source_lock.json` | `6f79231121f78e1c6b55da148c5710c2005e0ae36f92b0771740d127a253ad88` | 32258 | 1 |
| `notes/BUILD_AUTHORIZATION_R0_REPAIR.md` | `8095586065f3f997125b29231ffcff28be1d099ecd01bedc22eb75b7809ee6ca` | 21642 | 389 |
| `notes/BUILD_AUTHORIZATION_R1.md` | `cc64d8e294dce01d0e2e4dbc24a15007222dde04998c5598fee0eb5e35f7a634` | 19746 | 353 |
| `notes/BUILD_R0_BLOCKER.md` | `5242052c625add4ba084d5542faae221e6b1a1cb6d81b773b9295d968afbc7fd` | 5873 | 145 |
| `notes/CITATION_VERIFICATION.md` | `d2b89b3313d54e612c3aa6e1e0a454c034d312268fd431217638417d90afa2bc` | 4916 | 65 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `b1184e0dffd4ccd633e9ced15c227e5bad3e9074627fd7442bd78896c1f48416` | 6915 | 94 |
| `notes/INDEPENDENT_BUILD_R1_R0_REPAIR_REVIEW.md` | `cc1d6f222ab500c10040c28f24bf3207fe5b0d645dc7a695e1406eb997e5f868` | 24176 | 195 |
| `notes/INDEPENDENT_BUILD_R2_R1_REVIEW.md` | `55b461472be87451a05dbff06eee5bfa2a5890f5d0d4984c89e5c8c01301b7ad` | 25497 | 408 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `20c7e7b49a2f698b509026bd025e5dd3ebf000ff6d3fa343466867e755d3951c` | 10683 | 248 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` | `6c02368dd361192628d4b79898b0a5fd9b273344d56e60179f52cb66dcc6d925` | 21489 | 582 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `d38343539db88d1eeda555c464657e408df6ab58aa6ad7a811cd262f53038750` | 17056 | 424 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md` | `8699472ce07744617c7407d051f84c2cca577c4d5e4ad4f9a0aa6f911ca1b0d5` | 26796 | 891 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `21a35057011098de88b03518cbb4e24a27ee1cb998303e526fcd128188c99fa8` | 17031 | 350 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `65bfe3d7e24c6f9f4ec6a826f2d29a387c0105e208f4990226a4d22242f24512` | 16536 | 388 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `a8dd5800afbf1b950453bd8fef7538b8c4a97e8a971d4db5e0c4705aa9917e56` | 12590 | 390 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `1fa152bdf1cf83a852b7e585e1e3aac402d06534c447a881e7506f082594846f` | 16605 | 521 |
| `notes/NOVELTY_ASSESSMENT.md` | `dbd33f68af27f0ba57982e5bb6f2dde8d01099188e2d240e0319199ee52b2699` | 7486 | 140 |
| `notes/PROOF_PACKAGE.md` | `2d290cbc316b42be8c978a527d9fa24751c992f532747067aeaf64d79eef6846` | 23639 | 951 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `49b17a22be1a774f5befbce67f54d1770d8277bd179a4a7ec728e4f55a59eeeb` | 21397 | 561 |
| `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `0587269d6e5fcd4461a4749b6846d459c096d698dd460d2f4abf291463934ed5` | 7553 | 189 |
| `notes/R1_REVISION_WINDOW_NO_CHANGE.md` | `4da8ff908be280bb9140eaf23ab60a726794ca9d6e2b95a4b2356fda8d350df3` | 2729 | 68 |
| `notes/RESEARCH_QUESTION.md` | `fc2269c6abe58b077b1c0b33bf07f93661f59a2ca72733330b9d67c38cb63175` | 5266 | 138 |
| `paper/BUILD_METADATA_R0.json` | `10797a9079fea64629a852dbf6644302a35ef2a96e8b05573eae9799f865345c` | 65981 | 1 |
| `paper/BUILD_METADATA_R1.json` | `ba621d379d805d4f7d9aae9b4233a02c79cf578605ad2a2d498d8b3613037af3` | 75469 | 1 |
| `paper/BUILD_RECEIPT_R0.json` | `4e7810b9ac2ad628503634539f0997a418aa4f583c9557ef6a5c41146b95dcec` | 66318 | 1 |
| `paper/BUILD_RECEIPT_R1.json` | `1a84c8af9e1f5ce74c0a7fb0a40c765885da43578561c78b0dc21c88790db966` | 75628 | 1 |
| `paper/PAPER_PLAN.md` | `2fdfc4eab1bd60e361b144eb8c3c9d0d7c71d37c63ce54145e7e6cca3888e224` | 34692 | 952 |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | `a77154a2150e74af115cb2ced4767f9617bafdb22267373b8128ebed09c3208d` | 3967 | 1 |
| `paper/main.aux` | `22a3bcd35b0aa9b87d6a4e40fe9f0cdc422fee366cf72e848be149486e5bcfb2` | 17245 | 191 |
| `paper/main.bbl` | `13faf55051bd94bf0cacdf4cae3b6476b77c417657bd8184b6f2446b1c28c3aa` | 1738 | 45 |
| `paper/main.blg` | `911285900fa9c373c657edd562d9cc284cd702194ab99094be5870613ef15f92` | 896 | 46 |
| `paper/main.log` | `3f8a5951bda82725d0731f0fd17d4e6b506ed2084e48bb7a9663b69ab5924cb0` | 27869 | 712 |
| `paper/main.out` | `c732b3ddb9511976c30b5b00e10709c77c022636e419de173c10db9ce172093a` | 8604 | 36 |
| `paper/main.pdf` | `5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7` | 471647 | 2649 |
| `paper/main.tex` | `926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1` | 69241 | 1921 |
| `paper/main_round0.pdf` | `5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7` | 471647 | 2649 |
| `paper/main_round1.pdf` | `5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7` | 471647 | 2649 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1928 | 55 |
| `refine-logs/FINAL_PROPOSAL.md` | `f58efbf336df21ab32296fc3c022be2200d4a0c7679e935652a405600c182679` | 5764 | 162 |
| `refine-logs/INITIAL_PROPOSAL.md` | `1d23119b72630a34446a0a331e1f3be5bf8e8362385c88b63c7f568aa411097d` | 4052 | 124 |
| `refine-logs/REVIEW_SUMMARY.md` | `96ee47f7cfa3f5324521335ebba6b6a21e009631fd0d668a3de7061dcf8a934d` | 3234 | 80 |

## 3. Authoritative source, build, and review chain

The authoritative terminal source is exactly the repaired trio:

| Source | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1` | 69,241 | 1,921 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1,928 | 55 |

The authoritative source-design and publication lineage, in order, is the
independent source-design review ending `SOURCE_DESIGN_PASS`; the source lock;
the independent source-lock review ending `SOURCE_LOCK_PASS`; the paper-plan
review ending `PAPER_PLAN_PASS`; the publication scope; the independent
publication-stage review ending `PUBLICATION_STAGE_PASS`; the publication
lock; and the independent publication-lock review ending
`PUBLICATION_LOCK_PASS`. The later source lineage is, in order, initial source
`PAPER_SOURCE_R1_PASS`; the historical first R0 hyperref blocker ending
exactly `R0_BLOCKED`; the one-line hyperref repair ledger ending
`SOURCE_REPAIR_FROZEN_DUAL_REVIEW_REQUIRED`; and two independent repaired-
source passes ending `PAPER_SOURCE_R1_R0_REPAIR_PASS` and
`PAPER_SOURCE_R2_R0_REPAIR_PASS`. The initial source review remains valid
historical evidence for its bound pre-repair bytes but cannot substitute for
either repaired-source review.

The accepted build lineage, in order, is the R0-repair authorization ending
`BUILD_AUTHORIZATION_R0_REPAIR`; R0 metadata status
`BUILD_METADATA_R0_REPAIR`; R0 receipt status `BUILD_R0_REPAIR_PASS`; the
fresh build review ending `BUILD_R1_R0_REPAIR_PASS`; the no-op revision
ledger ending `R1_REVISION_WINDOW_NO_CHANGE`; the strict-canonical no-op
source receipt, schema `PAPER22_SOURCE_REVISION_RECEIPT_R1_NO_OP_V1` and
status `R1_NO_OP_REVISION_PASS`; the R1 authorization ending
`BUILD_AUTHORIZATION_R1`; R1 metadata, schema
`PAPER22_BUILD_METADATA_R1_NO_OP_V1` and status
`BUILD_METADATA_R1_NO_OP`; R1 receipt, schema
`PAPER22_BUILD_RECEIPT_R1_NO_OP_V1` and status `BUILD_R1_NO_OP_PASS`; and
the final independent build review ending `BUILD_R2_R1_PASS`. The lock must
record every exact identity in that chain; no later object may promote the
historical blocker into a pass or replace an exact terminal/status token.

The current outputs and every accepted R0-repair/R1 comparator agree. In
particular,
`paper/main.pdf == paper/main_round0.pdf == paper/main_round1.pdf` byte for
byte at SHA-256
`5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7`,
471,647 bytes and 2,649 LF.

## 4. Frozen temporary-evidence universe E216

A no-follow rescan of `/tmp` found exactly ten live top-level paths whose
basename begins `paper22`: eight directories and two ordinary files. Their
complete nested universe is `E216`: 216 nodes comprising 201 regular files
and 15 directories, zero symlinks, zero special entries, and 72,033,301
regular-file bytes. The exact top-level paths are:

- `/tmp/paper22-prebuild28-manifest.txt`
- `/tmp/paper22-r0-A.PIwA2V`
- `/tmp/paper22-r0-B.xwtGZQ`
- `/tmp/paper22-r0-postbuild37-manifest.txt`
- `/tmp/paper22-r0-repair-A.0zGVu9`
- `/tmp/paper22-r0-repair-B.FwYPpz`
- `/tmp/paper22-r0-repair-validation.Y4OsGc`
- `/tmp/paper22-r1-noop-A.JMXTHF`
- `/tmp/paper22-r1-noop-B.lEctAm`
- `/tmp/paper22-r1-review.Nb23X3`

The finalization lock records every one of the 216 nodes with its literal and
top-relative path, type, mode, owner/group numeric IDs, device, inode, link
count and stat size; every regular file additionally has SHA-256, byte, and
LF identity. It also records top-level and aggregate counts and a
deterministic inventory framing hash. That complete lock inventory, not this
summary alone, governs later audit and cleanup.

The R2 review scratch `/tmp/paper22-r2-review-render.W0WPDx` is absent. The
removed R1 `r1-staging` and `validation-renders` descendants are absent from
both retained R1 roots. Literal names containing `XXXXXX`, including old
mktemp templates and the future terminal-root templates, are assertions that
must remain absent; they are not objects and never become cleanup targets.
No temporary evidence may be cleaned by the first four finalization roles.

## 5. Monotone project universes and closed stage paths

Every gate must enumerate and rehash the live universe rather than infer it.
The only permitted monotone project sequence is:

- `F45`: the 45 frozen inputs above;
- `G47 = F45 + {notes/FINALIZATION_STAGE_SCOPE.md,
  experiments/finalization_lock.json}`;
- `P48 = G47 + {notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md}`;
- `R50 = P48 + {paper/main_release_candidate.pdf,
  paper/FINAL_RELEASE_MANIFEST.json}`;
- `Q51 = R50 + {paper/TERMINAL_REBUILD_RECEIPT.json}`;
- `T52 = Q51 + {paper/reviews/final_integrity_review.md}`.

The project has four directories through `Q51`. `paper/reviews` is the only
permitted new directory, and it may be created only by the sole terminal
reviewer after all audits and authorized cleanup pass. No stage may precreate
a later path, skip a predecessor, modify an earlier byte, retain an unlisted
project artifact, follow a symlink, or use a hard link as a copy.

## 6. Five distinct and temporally fenced roles

1. **Finalization-governance author (G47).** Reads exact `F45`, the two
   frozen root ledgers, and `E216`; writes this scope and the lock in order;
   performs read-only validation; stops.
2. **Independent finalization reviewer (P48).** Is fresh, distinct from the
   governance author, and authored none of `F45` or the governance pair.
   Reads and rehashes exact `G47`, both root ledgers, and all live temporary
   evidence. On success writes only
   `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md`, ending exactly
   `FINALIZATION_STAGE_PASS`; on any blocker writes nothing.
3. **Release-candidate author (R50).** Is distinct from both prior roles.
   Reads and rehashes exact `P48`; first creates
   `paper/main_release_candidate.pdf` as an exclusive raw byte copy of
   `paper/main_round1.pdf`; then writes only strict-canonical
   `paper/FINAL_RELEASE_MANIFEST.json`; stops.
4. **Terminal-build evidence author (Q51).** Is distinct from all preceding
   roles. Reads exact `R50`; builds only in two fresh root-owned mode-0700
   roots generated independently from `/tmp/paper22-terminal-A.XXXXXX` and
   `/tmp/paper22-terminal-B.XXXXXX`; writes only strict-canonical
   `paper/TERMINAL_REBUILD_RECEIPT.json`; retains both roots unchanged for
   independent review; stops.
5. **Sole terminal-integrity reviewer (T52).** Is fresh, distinct from all
   four prior roles, and authored none of `Q51`. Reads and rehashes exact
   `Q51`, both live terminal roots, all ten `E216` top-level objects, and all
   absent assertions. It independently verifies governance, source,
   theorem, bibliography, build, JSON, PDF, visual, anonymity, security,
   private-provenance, stage-order, and external-effect gates. Only after
   every audit passes may it clean the exact legacy and terminal evidence by
   the bounded method below, then create `paper/reviews` and write only
   `paper/reviews/final_integrity_review.md`, whose last two nonempty lines
   are exactly `FINAL_INTEGRITY_PASS` and `RELEASE_CONFIRMED`.

Every role begins only after its predecessor has stopped and the complete
predecessor state has been freshly rehashed. A role may not review or repair
its own output. A failure grants no downstream authority.

## 7. Canonical JSON and downstream schemas

The lock, release manifest, and terminal receipt use UTF-8 strict recursive-
canonical JSON: Unicode code-point key ordering at every depth, compact
separators, no BOM/CR/NUL, no insignificant whitespace, no duplicate keys,
no nonfinite numbers, exactly one terminal LF, and a byte-identical strict
decode/re-encode round trip under duplicate-aware Python and an independent
custom Node parser/encoder. Every self-referential artifact records its safe
path, null `sha256`, null `bytes`, and the reason for self-exclusion; circular
self-identity claims are forbidden.

- The current lock schema is exactly `paper22-finalization-lock-v1`; its
  state and status are exactly
  `FINALIZATION_STAGE_LOCKED_PENDING_INDEPENDENT_FINALIZATION_REVIEW`.
- The finalization review's sole success terminal is exactly
  `FINALIZATION_STAGE_PASS`.
- The release manifest schema is exactly
  `paper22-final-release-manifest-v1`; its status is exactly
  `LOCAL_ANONYMOUS_RELEASE_CANDIDATE_PENDING_TERMINAL_REBUILD_AND_FINAL_INTEGRITY_REVIEW`.
  It externally binds every completed non-self path in exact `R50`, records
  the candidate's raw-copy provenance and complete dependency DAG, and
  leaves every external effect false.
- The terminal receipt schema is exactly
  `paper22-terminal-rebuild-receipt-v1`; its status is exactly
  `TERMINAL_REBUILD_PASS_PENDING_INDEPENDENT_ROOT_AUDIT`. It records both
  literal roots, complete snapshots, command streams, exit vectors,
  diagnostics, PDF audits, equality checks, and null self identity.
- The final review path and exact two-line terminal are fixed by Section 6.

## 8. Release-copy and terminal-rebuild contract

The release-candidate copy is exclusive and all-or-nothing. It must be a raw
byte copy from `paper/main_round1.pdf` to
`paper/main_release_candidate.pdf`, with no compile, transformation,
metadata rewrite, rendering, signing, linearization, optimization, hard link,
or overwrite. Its required identity is the frozen PDF identity in Section 3.
The candidate is not a submission and receives no external effect.

Each terminal root receives only independent ordinary-file copies of the
frozen source trio. The terminal builder clears the inherited environment and
sets exactly:

| Variable | Value |
|---|---|
| `PATH` | `/usr/bin:/bin` |
| `SOURCE_DATE_EPOCH` | `1787529600` |
| `FORCE_SOURCE_DATE` | `1` |
| `TZ` | `UTC` |
| `LC_ALL` | `C` |
| `LANG` | `C` |

In each root it runs exactly once, without `latexmk`, retry, cleanup build,
fifth pass, engine substitution, shell escape, or source-side command:

1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
2. `bibtex main`
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`

Both exit vectors must be exactly `0,0,0,0`. The source trio, four command
logs, and six outputs must correspond byte for byte across terminal A/B and
to the accepted R0-repair/R1 identities. The PDF equality is exactly
six-way:

`terminal-A/main.pdf = terminal-B/main.pdf = paper/main.pdf =
paper/main_round0.pdf = paper/main_round1.pdf =
paper/main_release_candidate.pdf`.

The common PDF must remain SHA-256
`5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7`,
471,647 bytes, 2,649 LF, valid PDF 1.5, 26 US-Letter pages, unencrypted, and
fully readable. The body, Limitations, Conclusion, and six-entry References
end on page 26, with no appendix; this satisfies the frozen 26.5-page target
convention, preferred 24--28 band, and hard 22--30 band. Final command 4 and
`main.log` must have zero fatal, undefined-citation, undefined-reference,
rerun/changed, package-warning, LaTeX-warning, and overfull events, and
exactly three nonblocking underfull hboxes at source line 944 with badness
`6316,10000,6316`.

All 28 fonts must be embedded, subsetted, and Unicode mapped. There must be
zero raster/page images, attachments, embedded files, forms, widgets,
signatures, JavaScript, launch/submit/import/external-GoTo/file-spec/rich-
media/movie/sound actions, encryption, dangerous object, or identity leak.
The only actions are the audited ordinary GoTo navigation and eight ordinary
bibliographic URI actions. The visible author remains exactly `Anonymous`.
The PDF title is the public title above; PDF Author, Creator, Producer,
Subject, and Keywords remain empty; CreationDate and ModDate remain exactly
`D:20260824000000Z`. All text, metadata, outlines, objects, and renders must
remain free of placeholders, unresolved markers, private paths, governance
tokens, hashes, identities, or provenance.

## 9. Mathematical, citation, and anti-claim fidelity

The terminal review must compare source, extracted text, and fresh renders to
the source/publication locks and proof lineage. The headline theorem retains
characteristic zero; `r >= 4`, `g >= 2r+1`, `h=g-1`, `m=r-2`; the fixed word
`F=T` after `S`; `C=BA`; `M=2 11^T-I`; the exact endpoint row replacements,
cone and strict selectors; the recurrences; leading-form survival without a
coefficient-positivity assumption; last-coordinate visibility for `n>=1`
with the tied `n=0` case separate; exact degree and Perron-radius identities;
the invariant direct sum and `(r-3)`-dimensional semisimple unit sector; the
displayed `Q_(m,h)` and exact cubic factor; exact algebraic and geometric unit
multiplicity `r-3`; the scalar recurrence and its initial values; the
`g=2r` seed/selected-face boundary; formal `r=3` consistency only; and the
four arbitrary nonzero coefficients on the fixed supports.

The sufficient cone is not claimed maximal, necessary, unique, exact, or
classificatory. The cubic is an annihilator, not uniformly minimal or
irreducible, and no uniform algebraic-degree-three claim is made. The
boundary is not a global failure theorem and does not classify dynamics at
or below `g=2r`; formal `r=3` substitution is not an `r=3` theorem. No
arbitrary-Hamiltonian, positive-characteristic, topological, metric,
arithmetic, entropy, or hyperbolicity claim is authorized.

The bibliography remains exactly six unique entries and the source retains
exactly the six keys `BlancVanSanten2021`, `ShaoSun2025`, `Deserti2016`,
`DangFavre2021`, `Rangarajan2002`, and `FujiokaKogawaLiShudo2023` in four
citation commands. Citations provide adjacent context only and transfer no
proof of the new selector, cone, carry, leading-form, matrix, visibility,
cubic, multiplicity, boundary, coefficient, or threshold statements.

## 10. Exact cleanup authority and method

Only the sole terminal-integrity reviewer, after all `Q51`, live-root,
temporary-evidence, build, PDF, visual, and governance audits have passed,
may clean evidence. Its cleanup targets are exactly the ten live `E216`
top-level paths recorded in Section 4 plus the two literal terminal roots
recorded by the terminal receipt. It must first revalidate each target by
literal absolute path and `lstat`, confirm its real parent is `/tmp`, confirm
the complete lock/receipt inventory, type, owner, mode, hashes, no symlink or
special entry, no unlisted descendant, and no hard-linked regular file.

For a standalone regular-file target, it performs one no-follow identity
check and unlinks that literal file. For a directory target, it opens the
literal directory with no-follow directory semantics, revalidates each exact
named descendant, unlinks only enumerated regular files, and removes each
now-empty enumerated directory with `rmdir` from deepest to shallowest,
ending with the top-level root. Recursive deletion commands, `rm -r`, globs,
wildcards, unresolved variables, command substitutions, broad prefixes,
symlink traversal, deletion-by-discovery, and deletion of any project path
are forbidden. Every absence assertion, including R2 scratch, removed R1
staging/render paths, and literal `XXXXXX` templates, must remain absent and
is never a deletion target.

Cleanup occurs before the terminal review's sole project write and may not
change any `Q51` byte. Any mismatch blocks cleanup and final-review writing;
it does not authorize repair, partial cleanup, or a blocker artifact.

## 11. Terminal local effect

The only possible terminal effect, and only after the independent final
review passes, is `LOCAL_ANONYMOUS_RELEASE_ONLY`. Submission, upload, public
hosting, repository push, network transport, external messaging, identity
disclosure, and every other external effect remain false and unauthorized.

## 12. Zero-write review block and same-path governance recovery

The first fresh independent finalization-stage reviewer honored the lock's
`WRITE_NOTHING` blocker disposition: it created zero project files, changed
zero project bytes, and left
`notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md` absent. Its exact sole
blocker was the normative chronology sentence formerly in Section 3. That
sentence called its source/publication lineage “in order” while placing
`PAPER_PLAN_PASS` after publication scope, `PUBLICATION_STAGE_PASS`, the
publication lock, and `PUBLICATION_LOCK_PASS`, even though the immutable plan
review, publication scope, publication lock, and this lock's already-correct
`authoritative_chain` prove that `PAPER_PLAN_PASS` precedes publication scope.

Every other review class passed: the exact 45-file `F45` bindings; the exact
47-file/four-directory/zero-symlink `G47` path universe; both root-ledger
fences; duplicate-aware Python and independent handwritten-Node strict-
canonical lock parsing; all 216 `E216` nodes, comprising 201 regular files
and 15 directories with 72,033,301 regular-file bytes; all 16 absence
assertions; historical terminal `R0_BLOCKED`; frozen source and PDF
identities; role separation and downstream counts; terminal commands and
equality requirements; bounded cleanup authority; and denial of every
external effect.

The superseded governance pair was exactly:

| Artifact | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `notes/FINALIZATION_STAGE_SCOPE.md` | `999b121be5cf83c6f19d2c61fd595f7a3314cc8d3f834861a516638418471b0f` | 23,825 | 386 |
| `experiments/finalization_lock.json` | `97fb27d9df15af822159484b03e4a05d8f30e145f6b0b7226594672714a547b0` | 99,054 | 1 |

The exact recovery-start root ledgers were
`BATCH_06_STATUS.md` at SHA-256
`7831ecdbd66ebba735f321aa43e051c0fd321936ef0ccf85782be60e381f40e6`,
41,433 bytes, 635 LF, gate
`PAPER22_FINALIZATION_GOVERNANCE_RECOVERY_OPEN` and Paper 22 queue
`FINALIZATION_SCOPE_ORDER_BLOCKED_PENDING_GOVERNANCE_RECOVERY`; and
`BATCH_06_IDEA_REPORT.md` at SHA-256
`0907031ca8c6e026dc729fa60bf1c5f7b498317558756bc2cf282c85689a4b1b`,
52,317 bytes, 1,013 LF. These are recovery-opening provenance, not future
ledger requirements.

This bounded recovery replaces only the same two governance paths, first this
scope and then the lock, and creates no new project path. The exact corrected
ordering is source-design review, source lock, `SOURCE_LOCK_PASS`,
`PAPER_PLAN_PASS`, publication scope, `PUBLICATION_STAGE_PASS`, publication
lock, `PUBLICATION_LOCK_PASS`, followed by the unchanged later source and
build lineage. It changes no `F45` path or byte, no `E216` path, stat, hash,
or byte, and no science, theorem, proof, source, bibliography, build command,
build root, log, output, PDF, role, stage count, cleanup permission, or
external-effect permission. The `G47` file/directory/link universe remains
47/4/0; only the two governance identities are superseded in place.

The failed review grants no downstream authority and cannot be converted into
a pass. A fresh independent finalization-stage reviewer must rehash the
complete recovered `G47`, both recovery-start ledgers, live `E216`, and every
absence assertion, and may pass only the corrected governance identities.

FINALIZATION GOVERNANCE SCOPE AUTHOR STOP
