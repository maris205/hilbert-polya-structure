# Paper 23 — Independent Corrected R0-Repair Build-Authorization Review

Review date: 2026-08-25 UTC

## Verdict, role, and boundary

Verdict: **PASS**. I acted as a fresh independent reviewer of the corrected
build authorization. I authored none of the 31 opening project files, the
three governing roots, the old authorization, the old failure blocker, or the
correction. I read all 31 project files and all three roots through EOF and
audited the correction from the frozen source and publication contract rather
than inheriting an earlier verdict.

This was a local authorization review only. I did not compile or run TeX or
BibTeX, create or inspect a build root, read or reuse an excluded root, edit
source, mutate an existing project file or root, browse, communicate
externally, or cause any other external effect. This report is the sole write.

## Governing roots and opening custody

All three governing roots were regular mode-0644 root:root files with link
count one and were stable at opening and immediately before this write:

| Root | SHA-256 | Bytes | LF | Exact controlling fact |
|---|---|---:|---:|---|
| `BATCH_06_STATUS.md` | `8edb73af2264332f05a05d2d97a167801fd4b30df06f2adc1b95993c26f37641` | 85,140 | 1,255 | gate `PAPER23_R0_REPAIR_AUTHORIZATION_CORRECTION_REVIEW_OPEN` |
| `BATCH_06_IDEA_REPORT.md` | `481e17aa04e83a577831ca94608975391e2301f43ea4266fc55324cbb3891710` | 136,761 | 2,609 | corrected-authorization frozen-review custody |
| `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` | `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4` | 8,524 | 245 | terminal `PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTED_PASS` |

The Paper 23 queue was exactly
`R0_REPAIR_AUTHORIZATION_CORRECTION_FROZEN_REVIEW_OPEN`. The opening project
inventory was exactly 31 regular files, the four child directories
`experiments`, `notes`, `paper`, and `refine-logs`, zero symbolic links, and
zero other objects. The present review path, the corrected failure-blocker
path, and all nine success paths were absent.

Every opening file was a single-link, root:root-owned regular non-symlink of
mode 0644, valid UTF-8, LF-only, with exactly one terminal LF and no BOM, CR,
or NUL. This is the complete opening ledger:

| Relative path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `b37132e282cceeb04a36723d75f48c4af6f3361836067850496cf52b8ad603e8` | 6,015 | 151 |
| `experiments/EXPERIMENT_TRACKER.md` | `85724a53e161bfbbb45af305af66454a757771330157694ff5d7f85215ffcb31` | 2,927 | 55 |
| `experiments/publication_lock.json` | `6f1830f14413c49cad0945facc7b10c081be1a36d4884e5768205273fce200c4` | 51,578 | 1 |
| `experiments/source_lock.json` | `5956a7e6c2e12a9be287b2ead2922e135c4a64da738757a0b55884e16974b248` | 32,889 | 1 |
| `notes/BUILD_AUTHORIZATION_R0_REPAIR.md` | `d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207` | 25,966 | 428 |
| `notes/BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION.md` | `0bddcd479cb82406888de2ca837f7e5c39ba5b6b2acbd12b365971f50aa5e48e` | 31,040 | 491 |
| `notes/BUILD_R0_BLOCKER.md` | `8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384` | 8,900 | 180 |
| `notes/BUILD_R0_REPAIR_BLOCKER.md` | `c05d9bb243bd28cd43dee4972f5ee829d01b165b73e7b9bef25a8c4f6940f472` | 11,493 | 223 |
| `notes/CITATION_VERIFICATION.md` | `fcf71a2364fe6b1624ac99189dd61a6655551928989a75bd2b338cea3d059da6` | 7,269 | 90 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `e3d6165b7429880cbe4407c6918ce25d6d8872ee05a48dfe457b5559f4df48c6` | 7,107 | 123 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `d491d6fa2fe3ca0d5b03195006f86021f65f6cf56529f592b46730086504b2d9` | 22,954 | 651 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` | `b8c62343aa9d893d9dcc0bf73e24755d92833c294c4f4a790cd1238c886f2636` | 21,240 | 465 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `aad55320dc0645931be2c0019327cd4255aaa56d77f94cd48e1a3702b10fb9bb` | 30,329 | 785 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md` | `075b9b6e7cc271f8abec29b08d28509df5ce7c8b6e0951753051d14a6b36c653` | 21,535 | 425 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `0ecfdc71a2de08e37311cb4683e393e397bb8e87854b01eb021a7db7f4d46dec` | 23,481 | 633 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `8711ba1e5e6daaef5c008f773cd5a5a0751eb1794b8595befc4c8bd5e4df88fb` | 15,589 | 483 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `c6ae173c45d0e8fbe073395abf366a33e3f4b24bf97c1ab97ad39cdb245e356e` | 17,851 | 441 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `8828364af81e829ee13201e5e8c63b1b92cb33df462c598ec3b615057545ec8c` | 23,668 | 586 |
| `notes/NOVELTY_ASSESSMENT.md` | `3ba35e3a336360e22f054c4821801c9b55e61dd4e9bc50e6aa57150dbca59dca` | 6,992 | 141 |
| `notes/PROOF_PACKAGE.md` | `0d0ffb5a7d540c987d37a93ec38c7a7736ac8445f6a82c5096e471ebcc34c040` | 24,560 | 1,184 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `fa0aef81669da75eacbe604614d86ae4a18610ef2ce70ba58391a47657f29b31` | 44,575 | 1,269 |
| `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `a0fe52acf07aed30dc8571b86a48602e74dc7cd15105ea4d69cd701f2e80bbe4` | 15,841 | 222 |
| `notes/RESEARCH_QUESTION.md` | `3cd1e22973e443c47a1672a82431c14c3b86ceba685330234d19085e65acdb5c` | 5,492 | 135 |
| `notes/SOURCE_R1_ABSTRACT_INTEGER_REPAIR.md` | `f5bea1184027da2afe9c1cc6810c000b72fb058cc6cb527a30222866b521ef3b` | 8,168 | 136 |
| `paper/PAPER_PLAN.md` | `fa7e5a7ea6693b0d8ef10651da317d253f5a1ba199e3b026a3b92c8104b6c974` | 44,881 | 799 |
| `paper/main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 | 1,776 |
| `paper/math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 |
| `paper/references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 | 99 |
| `refine-logs/FINAL_PROPOSAL.md` | `aa1221ef198ed1fe8c21da2e24107efb5671cc0f4fb70a7cd657a21c73e1f47b` | 5,531 | 185 |
| `refine-logs/INITIAL_PROPOSAL.md` | `485fd5b98e69338aae9a681548ac906e698d98adcd3af8dbf9e42622df9471b4` | 5,158 | 146 |
| `refine-logs/REVIEW_SUMMARY.md` | `c02b85e92727134a2cd65789c4034bbef7c047811d3e03314c9e598e5a054bf3` | 4,395 | 101 |

## Corrected precedence and date intent

The immutable old authorization is the mode-0644 object
`d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207`,
25,966 bytes and 428 LF, ending exactly and uniquely
`BUILD_AUTHORIZATION_R0_REPAIR`. The immutable old failure blocker is
`c05d9bb243bd28cd43dee4972f5ee829d01b165b73e7b9bef25a8c4f6940f472`,
11,493 bytes and 223 LF, ending exactly and uniquely
`R0_REPAIR_BUILD_BLOCKED`. The controlling correction is the mode-0644 object
`0bddcd479cb82406888de2ca837f7e5c39ba5b6b2acbd12b365971f50aa5e48e`,
31,040 bytes and 491 LF, ending exactly and uniquely
`BUILD_AUTHORIZATION_R0_REPAIR_CORRECTED`.

The correction has explicit precedence only for two conflicting rule
families. First, the old requirement that raw `CreationDate` and `ModDate`
each be present with value `D:20260825000000Z` is replaced by a hard complete
absence requirement. Second, the old consumed-with-no-replacement clause is
replaced only by eligibility for one distinct corrected invocation, after
this review and after a separate parent consumption. Necessary blocker,
inventory, gate, and queue consequences follow from those two replacements.
Every other old hard clause remains incorporated without weakening.

This is not a waiver or retrospective PASS. The old invocation remains failed,
its blocker remains immutable and required, and its roots remain excluded.
The old blocker independently records why the conflict was real: both
deterministic candidate PDFs omitted `CreationDate` and `ModDate` in
`pdfinfo -rawdates`; decoded metadata was empty; all 639 nonzero xrefs had no
date key or old value; the Info object contained the exact title and empty
identity fields but no dates; and no metadata stream existed. It failed only
because the old authorization demanded the opposite result.

The frozen source confirms that omission is intentional. `paper/main.tex` is
SHA-256 `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0`,
and its first three lines are exactly:

```tex
\ifdefined\pdfinfoomitdate
  \pdfinfoomitdate=1
\fi
```

Those three complete line bytes have SHA-256
`92bae6ee3706267421b56d22b63d8cf0ade4fa6addb23cd08a5388642a45fba2`.
The publication contract freezes an empty source date through `\date{}`, no
visible date, the exact public title, `Anonymous`, and empty PDF Author,
Creator, and Producer fields. The source preamble's explicit deterministic
date omission is therefore the implementation of the locked no-date identity,
not accidental missing evidence.

Accordingly a corrected build must show complete date absence in
`pdfinfo -rawdates`, decoded metadata, every nonzero xref and trailer, every
`/Info` reference and object dictionary, raw PDF bytes, metadata streams and
XMP, annotations, outlines, attachments and other objects, and visible and
extracted text. Neither date key, `D:20260825000000Z`, an alternate or
conflicting build date, nor a visible date may occur. `SOURCE_DATE_EPOCH`
remains fixed; it controls reproducibility but does not authorize date
presence.

## Retained hard-clause audit

The corrected authorization retains the exact source trio and nothing else:

| Source | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67,408 | 1,776 |
| `math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 |
| `references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2,812 | 99 |

It retains all of the following conjuncts:

1. A future builder must use exactly two newly created, independent,
   mode-0700 root-owned fresh roots, copy the exact trio independently into
   each, and run exactly eight processes under the exact six-variable
   environment: `PATH=/usr/bin:/bin`,
   `SOURCE_DATE_EPOCH=1787616000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`,
   `LC_ALL=C`, and `LANG=C`.
2. In each root, the exact command sequence is
   `pdflatex -interaction=nonstopmode -halt-on-error main.tex`, `bibtex main`,
   and that same `pdflatex` command twice more. Both exit vectors must be
   `(0,0,0,0)`. There is no fifth command, second BibTeX, retry, replacement
   builder, engine or flag change, `latexmk`, cache reuse, source generation or
   edit, network access, or external effect.
3. The four historical roots `/tmp/paper23-r0-A.DyWKGR`,
   `/tmp/paper23-r0-B.dsQvTx`, `/tmp/paper23-r0-repair-A.BzlBNd`, and
   `/tmp/paper23-r0-repair-B.TVRci7` are excluded absolutely: they may not be
   read, reused, written, copied, cached, linked, renamed, or treated as fresh.
   The corrected authorization is consumed when the first new build root is
   created. A mismatch before root creation requires a new governance decision,
   not an automatic retry.
4. Source copies, command logs, AUX/BBL/BLG/LOG/OUT closure, final outputs, and
   all deterministic identities must agree within and across roots. The final
   logs must contain no fatal error, unresolved citation or reference, multiply
   defined label, forbidden hyperref diagnostic, or overfull box; every
   underfull box must be individually documented and visually cleared.
5. The bibliography must resolve exactly nine citations and exactly these nine
   keys: `BergerTuraevHamiltonianMaps`,
   `BlancVanSantenAffineTriangular`, `DangFavreSpectralInterpretations`,
   `DesertiDegreeGrowthExamples`, `ForstnericComplexSymplectic`,
   `HenonOpenProblems`, `KochLomeliStraightLineFlows`,
   `RangarajanPolynomialSymplectic`, and `ShaoSunDimensionFour`. The safe
   bookmark must be exactly `The restricted boundary at g=9`.
6. Each PDF must be valid, unencrypted, action-safe, and free of JavaScript,
   Launch actions, attachments, forms, XFA, RichMedia, images, and identity or
   governance leakage. It must use Letter pages with rotation zero; every font
   must be embedded, subset, and Unicode-mapped with nonzero coverage. The PDF
   title must be the exact frozen title, the visible author must be exactly
   `Anonymous`, and Author, Creator, and Producer metadata must be empty.
7. The PDF must have exactly 23 physical pages. The abstract begins on page 1;
   the corrected subsection and Section 9 are on page 20; the Conclusion begins
   and ends on page 22; References begins on page 23; there is no appendix; and
   substantive content occupies pages 1--22. Every page, all three tables, and
   every long display receive full visual review. The truthful page flags are
   `hard_band_pass=true`, preferred-band pass false, and planning-target pass
   false: 22 substantive pages pass the hard 22--30 band, miss 24--28, and miss
   the 26-page target by four.
8. `BUILD_METADATA_R0.json` and `BUILD_RECEIPT_R0.json` must each be a
   one-record, one-line, exactly-one-terminal-LF canonical JSON file with
   recursive Unicode-code-point key ordering, compact encoding, duplicate-key
   rejection at every depth, canonical finite-number encoding, no trailing record,
   and exact `self_identity={"bytes":null,"sha256":null}`. A strict
   duplicate-aware Python implementation and a separately written custom Node
   recursive-descent parser and encoder must independently reproduce the
   bytes; native `JSON.parse`/`JSON.stringify` alone is insufficient. Their
   top-level statuses remain exactly `BUILD_METADATA_R0_REPAIR` and
   `BUILD_R0_REPAIR_PASS`, and their evidence must bind the correction, this
   review, all roots, all checks, and the corrected invocation.
9. Success persistence remains all-or-nothing and consists of exactly these
   nine project paths: `paper/BUILD_METADATA_R0.json`,
   `paper/BUILD_RECEIPT_R0.json`, `paper/main.aux`, `paper/main.bbl`,
   `paper/main.blg`, `paper/main.log`, `paper/main.out`, `paper/main.pdf`, and
   `paper/main_round0.pdf`. No subset may persist. Failure instead creates no
   success path and permits only
   `notes/BUILD_R0_REPAIR_CORRECTION_BLOCKER.md`, ending exactly and uniquely
   `R0_REPAIR_CORRECTION_BUILD_BLOCKED`. The immutable old blocker remains
   present in either outcome.

No retained clause admits a source edit, date waiver, old-root reuse,
diagnostic weakening, partial persistence, retrospective acceptance, or a
retry after either success or failure.

## Authority conclusion and inventory effects

This PASS does not itself run or consume the build. Only a later, separate
parent transition may consume it and open exactly the future gate
`PAPER23_DETERMINISTIC_R0_REPAIR_CORRECTION_BUILD_OPEN` with queue
`R0_REPAIR_CORRECTION_BUILD_AUTHORIZED` for one corrected invocation. The
reviewer and parent roles may not collapse, and no second correction or second
corrected invocation is authorized.

The inventory arithmetic is exact: correction-author stop 31 files; reviewed
prebuild state 32; successful persistence 41; failed persistence 33. Creation
of this sole report changes only the project inventory from `31/4/0/0` to
`32/4/0/0`. All 31 opening files and all three roots remain immutable. The new
failure blocker and all nine success paths remain absent until a separately
authorized corrected build chooses exactly one atomic outcome.

Every identity, precedence, source-intent, retained-clause, path, inventory,
role-separation, and no-external-effect conjunct passes. No ambiguity grants a
retry or waives a hard check.

BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION_PASS
