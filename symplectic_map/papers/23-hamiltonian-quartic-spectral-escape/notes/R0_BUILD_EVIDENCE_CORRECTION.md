# Paper 23 R0 Build-Evidence Correction — Append-Only Author Ledger

Correction date: 2026-08-25 UTC

## 1. Role, authority, and zero-write opening boundary

I acted only as the sole distinct append-only R0 build-evidence correction
author for Paper 23. I did not author the manuscript, the R0 build, either
original build JSON, either historical blocker, any prior review, or any
governing root. I did not compile, render, edit source, inspect an excluded
root, clean a build root, revise a build output, or cause an external effect.

The post-clarification authority is exactly:

- gate: `PAPER23_R0_BUILD_EVIDENCE_CORRECTION_OPEN`;
- queue:
  `R0_REPAIR_CORRECTION_BUILD_R1_REVIEW_BLOCKED_EVIDENCE_CORRECTION_OPEN`;
- first authorized project path:
  `notes/R0_BUILD_EVIDENCE_CORRECTION.md`;
- second authorized project path:
  `paper/BUILD_EVIDENCE_CORRECTION_R0.json`;
- future independent-review path:
  `notes/INDEPENDENT_R0_BUILD_EVIDENCE_CORRECTION_REVIEW.md`;
- future independent-review terminal:
  `R0_BUILD_EVIDENCE_CORRECTION_PASS`.

The two authorized targets and the future review path were absent as both
directory entries and symlinks at opening. Creation is no-follow,
no-overwrite, ledger first, overlay second, and all-or-nothing. A defect before
commit requires zero project write. No other project or root path is writable.

The clarified governing roots read through EOF are:

| Path | SHA-256 | Bytes | LF | Mode | Owner | Device | Inode | Links |
|---|---|---:|---:|---:|---|---:|---:|---:|
| `BATCH_06_STATUS.md` | `8b58f012f8751469f05696918f6ed840f00f85a9188c8b7c67bc5eddd9a2e5ba` | 94404 | 1387 | 0644 | `root:root` | 2431 | 12439253850 | 1 |
| `BATCH_06_IDEA_REPORT.md` | `24933399b24d94c781661f102205dd3f7de63d5fe588c348f2aabe15288f9d7a` | 152998 | 2889 | 0644 | `root:root` | 2431 | 12439253853 | 1 |
| `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` | `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4` | 8524 | 245 | 0644 | `root:root` | 2431 | 12439253857 | 1 |

The status and idea roots include both governing clarifications: an
append-only overlay may support a present corrected evidence conjunction only
after independent overlay review and cannot make pre-persistence semantic
validation true retroactively; the nine already persisted paths may remain
only as immutable quarantined evidence under a narrow recovery-custody
exception, not as accepted success artifacts.

## 2. Complete 41-file opening ledger

At re-preflight the project contained exactly 41 ordinary regular files, four
ordinary child directories (`experiments`, `notes`, `paper`, and
`refine-logs`), zero symlinks, and zero other objects. Every file was mode
0644, owner `root:root`, link count one, and device 2431. The complete ledger
is bytewise sorted by project-relative path:

| Path | SHA-256 | Bytes | LF | Mode | Owner | Device | Inode | Links |
|---|---|---:|---:|---:|---|---:|---:|---:|
| `experiments/EXPERIMENT_PLAN.md` | `b37132e282cceeb04a36723d75f48c4af6f3361836067850496cf52b8ad603e8` | 6015 | 151 | 0644 | `root:root` | 2431 | 5913543619 | 1 |
| `experiments/EXPERIMENT_TRACKER.md` | `85724a53e161bfbbb45af305af66454a757771330157694ff5d7f85215ffcb31` | 2927 | 55 | 0644 | `root:root` | 2431 | 5913543620 | 1 |
| `experiments/publication_lock.json` | `6f1830f14413c49cad0945facc7b10c081be1a36d4884e5768205273fce200c4` | 51578 | 1 | 0644 | `root:root` | 2431 | 5913543623 | 1 |
| `experiments/source_lock.json` | `5956a7e6c2e12a9be287b2ead2922e135c4a64da738757a0b55884e16974b248` | 32889 | 1 | 0644 | `root:root` | 2431 | 5913543616 | 1 |
| `notes/BUILD_AUTHORIZATION_R0_REPAIR.md` | `d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207` | 25966 | 428 | 0644 | `root:root` | 2431 | 6443708207 | 1 |
| `notes/BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION.md` | `0bddcd479cb82406888de2ca837f7e5c39ba5b6b2acbd12b365971f50aa5e48e` | 31040 | 491 | 0644 | `root:root` | 2431 | 6443704696 | 1 |
| `notes/BUILD_R0_BLOCKER.md` | `8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384` | 8900 | 180 | 0644 | `root:root` | 2431 | 6443678303 | 1 |
| `notes/BUILD_R0_REPAIR_BLOCKER.md` | `c05d9bb243bd28cd43dee4972f5ee829d01b165b73e7b9bef25a8c4f6940f472` | 11493 | 223 | 0644 | `root:root` | 2431 | 6443708204 | 1 |
| `notes/CITATION_VERIFICATION.md` | `fcf71a2364fe6b1624ac99189dd61a6655551928989a75bd2b338cea3d059da6` | 7269 | 90 | 0644 | `root:root` | 2431 | 6443323389 | 1 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `e3d6165b7429880cbe4407c6918ce25d6d8872ee05a48dfe457b5559f4df48c6` | 7107 | 123 | 0644 | `root:root` | 2431 | 6443323390 | 1 |
| `notes/INDEPENDENT_BUILD_AUTHORIZATION_R0_REPAIR_CORRECTION_REVIEW.md` | `b34e35c7877870b40354d66b59ec7f816010a2470bc863b34f730e548a01ba53` | 15505 | 235 | 0644 | `root:root` | 2431 | 6443678300 | 1 |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `d491d6fa2fe3ca0d5b03195006f86021f65f6cf56529f592b46730086504b2d9` | 22954 | 651 | 0644 | `root:root` | 2431 | 6443323789 | 1 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_R0_REPAIR_REVIEW.md` | `b8c62343aa9d893d9dcc0bf73e24755d92833c294c4f4a790cd1238c886f2636` | 21240 | 465 | 0644 | `root:root` | 2431 | 6443678298 | 1 |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_REVIEW.md` | `aad55320dc0645931be2c0019327cd4255aaa56d77f94cd48e1a3702b10fb9bb` | 30329 | 785 | 0644 | `root:root` | 2431 | 6443658252 | 1 |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_R0_REPAIR_REVIEW.md` | `075b9b6e7cc271f8abec29b08d28509df5ce7c8b6e0951753051d14a6b36c653` | 21535 | 425 | 0644 | `root:root` | 2431 | 6443678301 | 1 |
| `notes/INDEPENDENT_PUBLICATION_LOCK_REVIEW.md` | `0ecfdc71a2de08e37311cb4683e393e397bb8e87854b01eb021a7db7f4d46dec` | 23481 | 633 | 0644 | `root:root` | 2431 | 6443323778 | 1 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `8711ba1e5e6daaef5c008f773cd5a5a0751eb1794b8595befc4c8bd5e4df88fb` | 15589 | 483 | 0644 | `root:root` | 2431 | 6443334570 | 1 |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | `c6ae173c45d0e8fbe073395abf366a33e3f4b24bf97c1ab97ad39cdb245e356e` | 17851 | 441 | 0644 | `root:root` | 2431 | 6443323385 | 1 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `8828364af81e829ee13201e5e8c63b1b92cb33df462c598ec3b615057545ec8c` | 23668 | 586 | 0644 | `root:root` | 2431 | 6443323386 | 1 |
| `notes/NOVELTY_ASSESSMENT.md` | `3ba35e3a336360e22f054c4821801c9b55e61dd4e9bc50e6aa57150dbca59dca` | 6992 | 141 | 0644 | `root:root` | 2431 | 6443323391 | 1 |
| `notes/PROOF_PACKAGE.md` | `0d0ffb5a7d540c987d37a93ec38c7a7736ac8445f6a82c5096e471ebcc34c040` | 24560 | 1184 | 0644 | `root:root` | 2431 | 6443323776 | 1 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `fa0aef81669da75eacbe604614d86ae4a18610ef2ce70ba58391a47657f29b31` | 44575 | 1269 | 0644 | `root:root` | 2431 | 6443323790 | 1 |
| `notes/R0_HYPERREF_SOURCE_REPAIR.md` | `a0fe52acf07aed30dc8571b86a48602e74dc7cd15105ea4d69cd701f2e80bbe4` | 15841 | 222 | 0644 | `root:root` | 2431 | 6443678299 | 1 |
| `notes/RESEARCH_QUESTION.md` | `3cd1e22973e443c47a1672a82431c14c3b86ceba685330234d19085e65acdb5c` | 5492 | 135 | 0644 | `root:root` | 2431 | 6443323388 | 1 |
| `notes/SOURCE_R1_ABSTRACT_INTEGER_REPAIR.md` | `f5bea1184027da2afe9c1cc6810c000b72fb058cc6cb527a30222866b521ef3b` | 8168 | 136 | 0644 | `root:root` | 2431 | 6443457781 | 1 |
| `paper/BUILD_METADATA_R0.json` | `599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362` | 70889 | 1 | 0644 | `root:root` | 2431 | 3227322490 | 1 |
| `paper/BUILD_RECEIPT_R0.json` | `70ad2b65c82201981488c5bcc4685f08f37529504082afb7e1778248c96cd590` | 71124 | 1 | 0644 | `root:root` | 2431 | 3227322494 | 1 |
| `paper/PAPER_PLAN.md` | `fa7e5a7ea6693b0d8ef10651da317d253f5a1ba199e3b026a3b92c8104b6c974` | 44881 | 799 | 0644 | `root:root` | 2431 | 3227277695 | 1 |
| `paper/main.aux` | `2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb` | 14072 | 165 | 0644 | `root:root` | 2431 | 3227322495 | 1 |
| `paper/main.bbl` | `baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9` | 2881 | 73 | 0644 | `root:root` | 2431 | 3227332992 | 1 |
| `paper/main.blg` | `be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34` | 900 | 46 | 0644 | `root:root` | 2431 | 3227332993 | 1 |
| `paper/main.log` | `ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6` | 27628 | 700 | 0644 | `root:root` | 2431 | 3227332994 | 1 |
| `paper/main.out` | `14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94` | 6226 | 28 | 0644 | `root:root` | 2431 | 3227332995 | 1 |
| `paper/main.pdf` | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` | 492452 | 2724 | 0644 | `root:root` | 2431 | 3227332996 | 1 |
| `paper/main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67408 | 1776 | 0644 | `root:root` | 2431 | 3227298198 | 1 |
| `paper/main_round0.pdf` | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` | 492452 | 2724 | 0644 | `root:root` | 2431 | 3227332997 | 1 |
| `paper/math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 | 0644 | `root:root` | 2431 | 3227298196 | 1 |
| `paper/references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2812 | 99 | 0644 | `root:root` | 2431 | 3227298197 | 1 |
| `refine-logs/FINAL_PROPOSAL.md` | `aa1221ef198ed1fe8c21da2e24107efb5671cc0f4fb70a7cd657a21c73e1f47b` | 5531 | 185 | 0644 | `root:root` | 2431 | 6980649942 | 1 |
| `refine-logs/INITIAL_PROPOSAL.md` | `485fd5b98e69338aae9a681548ac906e698d98adcd3af8dbf9e42622df9471b4` | 5158 | 146 | 0644 | `root:root` | 2431 | 6980649941 | 1 |
| `refine-logs/REVIEW_SUMMARY.md` | `c02b85e92727134a2cd65789c4034bbef7c047811d3e03314c9e598e5a054bf3` | 4395 | 101 | 0644 | `root:root` | 2431 | 6980649943 | 1 |

For independent reproduction, the canonical opening-manifest byte stream is
41 LF-terminated records sorted under `LC_ALL=C`; each record is
`path<TAB>sha256<TAB>bytes<TAB>LF<TAB>mode<TAB>owner<TAB>device<TAB>inode<TAB>links`.
It is 5663 bytes, 41 LF, SHA-256
`aed0c364be9af4ed1b8d0748a3a0b61246ac239d37da07287ee976c3a3e27164`.

## 3. Immutable original JSONs, staged copies, and zero-write R1 review

The original canonical JSONs remain immutable historical evidence:

| Object | SHA-256 | Bytes | LF | Inode | Historical status |
|---|---|---:|---:|---:|---|
| `paper/BUILD_METADATA_R0.json` | `599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362` | 70889 | 1 | 3227322490 | `BUILD_METADATA_R0_REPAIR` |
| `paper/BUILD_RECEIPT_R0.json` | `70ad2b65c82201981488c5bcc4685f08f37529504082afb7e1778248c96cd590` | 71124 | 1 | 3227322494 | `BUILD_R0_REPAIR_PASS` builder claim only |

Both are device-2431 mode-0644 root-owned regular files with link count one.
The metadata atime is `2026-08-24 22:58:13.317406832 +0000`, mtime and
birth are `2026-08-24 22:58:13.301406799 +0000`, and ctime is
`2026-08-24 22:58:13.305406808 +0000`; all four whole-second epochs are
1787612293. The receipt atime is
`2026-08-24 22:58:13.317406832 +0000`, while mtime, ctime, and birth are
`2026-08-24 22:58:13.305406808 +0000`; all four whole-second epochs are
1787612293. These external identities and timestamps are repeated in the
overlay and attached to every correction target by target path.

Their A-root staged copies are byte-identical to the respective project
objects and retain the same hashes and sizes. The staged metadata inode is
6443678273 and the staged receipt inode is 6443678274, both device 149, mode
0644, owner `root:root`, and link count one. Each of the four original/staged
objects contains each erroneous executable digest exactly once. No original
or staged byte is edited, replaced, or virtually rehashed by this recovery.

The fresh corrected-R0 R1 reviewer found the hard semantic defect before
rendering and obeyed its zero-write rule. Therefore
`notes/INDEPENDENT_BUILD_R1_R0_REPAIR_CORRECTION_REVIEW.md` is absent, the
41-file universe is unchanged, and no R1 PASS exists. The two clarified
governing roots above are the immutable record of that zero-write outcome;
this author does not fabricate a missing review artifact. In particular, the
absent R1 review has no SHA-256, byte count, terminal, status, or verdict to
bind. Its evidence is exactly the final governing-root identities plus the
required review-path absence.

## 4. Exact causal defect and four factual corrections

The defect is a static-literal transcription error in the retained A-root
candidate generator, not a compiler, executable, canonical-encoding, copy, or
filesystem-replacement event. The generator is
`validation-pages/generate_candidates.py`, SHA-256
`6acd07e156581831730bfbd5768f0d52fe2c99663151350b50d1c01d93e3a81e`,
35751 bytes, 632 LF, mode 0644, device 149, inode 10739843347. Its physical
lines 384--385 hard-code the two erroneous strings inside the common value
tree instead of calling its `digest()`/`identity()` helpers on the resolved
executables. Deep copies of that common tree propagated both literals into
the metadata and receipt; canonical serialization, staged-copy equality, and
the no-overwrite persistence transaction then faithfully preserved the wrong
facts. The two original strict validators checked grammar, duplicate keys,
canonical bytes, and tree equality, but did not independently hash the named
executables. Canonical JSON can encode a false fact canonically.

Only these four RFC 6901 fact pointers receive corrected-value precedence:

| Immutable target | RFC 6901 pointer | Erroneous historical value | Observed value |
|---|---|---|---|
| `paper/BUILD_METADATA_R0.json` | `/build/executable_identities/bibtex/sha256` | `c9ecb7182f287007d277d67a1537a721493f2d3b0c98d16006ba24493710618f` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `paper/BUILD_METADATA_R0.json` | `/build/executable_identities/pdflatex/sha256` | `01a7ab54dd9ca121cc8694f3bb656633682f2e2fd5fba6f9adcd8a9508336cf9` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `paper/BUILD_RECEIPT_R0.json` | `/build/executable_identities/bibtex/sha256` | `c9ecb7182f287007d277d67a1537a721493f2d3b0c98d16006ba24493710618f` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `paper/BUILD_RECEIPT_R0.json` | `/build/executable_identities/pdflatex/sha256` | `01a7ab54dd9ca121cc8694f3bb656633682f2e2fd5fba6f9adcd8a9508336cf9` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |

No other factual pointer is corrected. Every other original field is carried
forward byte-for-byte as historical evidence, subject to the suspended
acceptance semantics below and to later independent review; this author does
not silently re-review or newly certify those carried-forward conclusions.

## 5. Three-method executable identity and timestamp proof

Resolution is `/usr/bin/pdflatex -> pdftex -> /usr/bin/pdftex` and
`/usr/bin/bibtex -> /etc/alternatives/bibtex ->
/usr/bin/bibtex.original`. The resolved targets are ordinary regular files:

| Resolved path | Device | Inode | Bytes | Mode | Owner | Links | atime UTC / epoch | mtime UTC / epoch | ctime UTC / epoch | birth UTC / epoch |
|---|---:|---:|---:|---:|---|---:|---|---|---|---|
| `/usr/bin/pdftex` | 149 | 3829692913 | 1802504 | 0755 | `root:root` | 1 | `2026-08-24 06:23:03.778959322 +0000` / 1787552583 | `2026-01-27 17:36:46.000000000 +0000` / 1769535406 | `2026-07-30 02:12:41.969305619 +0000` / 1785377561 | `2026-07-30 02:12:41.969305619 +0000` / 1785377561 |
| `/usr/bin/bibtex.original` | 149 | 3829692848 | 117128 | 0755 | `root:root` | 1 | `2026-08-24 06:23:11.543261065 +0000` / 1787552591 | `2026-01-27 17:36:46.000000000 +0000` / 1769535406 | `2026-07-30 02:12:41.961305260 +0000` / 1785377561 | `2026-07-30 02:12:41.961305260 +0000` / 1785377561 |

Three independently invoked hashing paths agree exactly:

| Method | `/usr/bin/pdftex` | `/usr/bin/bibtex.original` |
|---|---|---|
| Python 3.12.3 `hashlib.sha256`, 1 MiB streaming reads | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| GNU coreutils 8.32 `sha256sum` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| OpenSSL 3.6.2 `dgst -sha256` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |

Both target births and ctimes precede the successful roots' common birth at
`2026-08-24 22:32:59.485275005 +0000` (epoch 1787610779) and the staged JSON
births at epoch 1787612148. Device, inode, byte count, mode, owner, and link
count agree with the non-digest executable fields in both original JSONs.
Moreover, immutable `notes/BUILD_R0_BLOCKER.md` (SHA-256
`8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384`,
8900 bytes, 180 LF, terminal `R0_BLOCKED`) and
`notes/BUILD_R0_REPAIR_BLOCKER.md` (SHA-256
`c05d9bb243bd28cd43dee4972f5ee829d01b165b73e7b9bef25a8c4f6940f472`,
11493 bytes, 223 LF, terminal `R0_REPAIR_BUILD_BLOCKED`) already record the
same observed digests. Binary replacement cannot explain the mismatch.

## 6. Authorized live roots and build-output custody

Only the successful roots below were read. The four contract-excluded roots
`/tmp/paper23-r0-A.DyWKGR`, `/tmp/paper23-r0-B.dsQvTx`,
`/tmp/paper23-r0-repair-A.BzlBNd`, and
`/tmp/paper23-r0-repair-B.TVRci7` were not accessed, stated, or cleaned.

| Root | Mode | Owner | Device | Inode | Links | Birth UTC | Regular files | Child dirs | Links / other | Regular bytes |
|---|---:|---|---:|---:|---:|---|---:|---:|---:|---:|
| `/tmp/paper23-r0-repair-correction-A.Er2f85` | 0700 | `root:root` | 149 | 6443678302 | 3 | `2026-08-24 22:32:59.485275005 +0000` | 43 | 1 | 0 / 0 | 8637740 |
| `/tmp/paper23-r0-repair-correction-B.tcCPcQ` | 0700 | `root:root` | 149 | 6981323841 | 2 | `2026-08-24 22:32:59.485275005 +0000` | 13 | 0 | 0 / 0 | 648698 |

For each root, a complete regular-file manifest uses the same nine-field,
TAB-separated, relative-path-sorted format defined in Section 2. Root A's
manifest is 5655 bytes, 43 LF, SHA-256
`415f5d1d47828a25154f2dea5423d8259cdd40b3085a3b4c4d2140607f237b38`;
root B's is 1515 bytes, 13 LF, SHA-256
`1d0e5a4a101f148a449dac5bd5499c5bf87daccb995ea27b42cf84eb7129a067`.
Root A's sole child directory `validation-pages` is mode 0700, owner
`root:root`, device 149, inode 10739810258, link count two. Those complete
manifest bindings include all retained validation scripts and all 23 PNGs.

The thirteen source/command/output identities are pairwise equal across A/B:

| Artifact | SHA-256 | Bytes | LF | A inode | B inode |
|---|---|---:|---:|---:|---:|
| `main.tex` | `1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0` | 67408 | 1776 | 6443704693 | 6981323845 |
| `math_commands.tex` | `a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d` | 420 | 13 | 6443704694 | 6981323850 |
| `references.bib` | `ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782` | 2812 | 99 | 6443704695 | 6981323851 |
| `command-1.log` | `1fcbc0319012bbeb4fd526dad9eef6a0ca9e86474e9c092ae766a70a4ef466ce` | 18124 | 597 | 6443704697 | 6981323852 |
| `command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 | 6443704702 | 6981323857 |
| `command-3.log` | `cba30ead0e25a854366d5bf7e9156ffadfb713fd4de7097a43b6f284e1d2db72` | 8363 | 158 | 6443708172 | 6981323860 |
| `command-4.log` | `ad3eb1bf23dd06e82b1683ccb3e66c34b142303fa24685f56f268f58368612b0` | 7254 | 112 | 6443708173 | 6981323864 |
| `main.aux` | `2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb` | 14072 | 165 | 6443704699 | 6981323854 |
| `main.bbl` | `baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9` | 2881 | 73 | 6443708171 | 6981323859 |
| `main.blg` | `be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34` | 900 | 46 | 6443704703 | 6981323858 |
| `main.log` | `ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6` | 27628 | 700 | 6443704698 | 6981323853 |
| `main.out` | `14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94` | 6226 | 28 | 6443704700 | 6981323855 |
| `main.pdf` | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` | 492452 | 2724 | 6443704701 | 6981323856 |

Root A additionally retains byte-identical staged copies of the two original
JSONs and `main_round0.pdf`, whose PDF identity is the same as `main.pdf`.
The seven project build-output paths remain byte-identical to their accepted
root-A sources. This correction performs no source/output truth re-review;
the identities are custody facts and all original substantive conclusions
remain for a fresh build R1 reviewer.

## 7. Suspended acceptance semantics and non-retroactive recovery

The four fact corrections above are the only changed factual values in the
effective view. They do not authorize treating either immutable original JSON
as true “as written.” Pending independent overlay review, the following four
pointers are suspended in each original JSON:

- `/acceptance/all_hard_conjuncts_pass`;
- `/acceptance/blocker`;
- `/acceptance/chosen_outcome`;
- `/checks/success_paths_absent_before_complete_validation`.

The receipt's top-level `/status` value `BUILD_R0_REPAIR_PASS` is also
suspended as an effective verdict and remains only a historical builder
claim. The metadata's top-level `/status` value `BUILD_METADATA_R0_REPAIR`
remains solely a historical record label in the original-byte namespace; it
does not certify semantic correctness or supply an effective PASS. None of
these immutable bytes is rewritten. In particular,
`/checks/success_paths_absent_before_complete_validation` cannot become true
retroactively: semantic executable-identity validation had not completed
before persistence. The parent clarification supersedes that old timing
conjunct only enough to permit this transparent delayed recovery; the overlay
records the real hashes after persistence and does not pretend otherwise.

The originals' `/json_validation/candidate_hashes_recorded_before_persistence`,
`/json_validation/candidate_round_trips_exact`,
`/json_validation/two_value_trees_agree`, and
`/json_validation/validation_completed_before_persistence` may be carried
forward only with the narrow meaning that hashes of the original candidates,
strict syntactic parsing, recursive canonical encoding, candidate round-trip
equality, and original value-tree/byte equality completed before persistence.
None supplies semantic validation of the executable digest facts or all hard
conjuncts, and none applies to this later overlay or to any hypothetical
patched document. The receipt's `/companion_candidate` continues to hash and
stat the original erroneous A-root metadata candidate, not a corrected
virtual object. Both original null `/self_identity` objects and all project/A
staged-copy equalities likewise refer only to the immutable erroneous bytes.

This recovery is a semantic precedence map and evidence conjunction. It does
not materialize, define, hash, or authorize a four-pointer-patched metadata or
receipt pair. In particular, there is no virtual corrected canonical JSON,
the receipt companion pointer is not changed, no unauthorized fifth factual
pointer exists, and no new candidate-before-persistence assertion is made.

The negative counterexample is explicit. Naively applying only the four
factual replacements in memory and canonically re-encoding would produce a
non-authorized virtual metadata byte string of 70889 bytes and SHA-256
`9a1864be2795df47a3f82855f2b1aef2aa51424809c7550767c466a7fc9a4493`,
and a virtual receipt of 71124 bytes and SHA-256
`d675ef6aeca693c732f4f39601f5b68592f7dda2cab4ca7bf2bc956346397a15`.
That virtual receipt would still bind original metadata SHA-256
`599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362`
through `/companion_candidate`, so the pair would be internally false.
Changing that companion SHA would be an unauthorized fifth factual pointer
and would produce yet another non-authorized virtual receipt SHA-256
`3b6b6343dd1d07aa6106f07e9c61ee451cc8c4e74f0ad918d1d086fb11e5b67c`.
None of the three virtual byte strings is written or treated as evidence.

All original companion, null-self, staged-copy, persistence, atomic-nine-path,
and inventory statements stay exclusively in the immutable original-byte and
physical-history namespace. They describe what bytes and paths existed and
how the nine-path transaction physically ran; they do not establish that the
old acceptance branch was authorized or that the overlay was validated before
that transaction. This correction is a separate append-only 41-to-43-file
transaction, not a continuation, replay, or repair-in-place of the original
nine-path transaction.

Before a fresh overlay PASS, there is no effective corrected build PASS and
no R1 review authority. After, and only after, a distinct reviewer creates the
authorized review ending in the prescribed PASS terminal, the present
evidence view is the conjunction

`immutable originals excluding the suspended semantic claims`

AND

`this correction ledger plus its strict-canonical overlay`

AND

`the fresh independent overlay PASS`.

That conjunction is only eligible to reopen a brand-new corrected-R0 build
R1 review. It neither retrospectively validates the original receipt nor
accepts the build. A later R1 reviewer must treat all carried-forward build,
log, citation, PDF, font, pagination, visual, permission, and acceptance
conclusions as unproved and may not say either original JSON was true as
written. Every original field outside the four corrected factual pointers and
the suspended semantic set is preserved as carry-forward historical evidence,
not independently recertified by this author.

The recovery-custody exception expressly supersedes only old-authorization
lines 320 and 375 and lines 402--410 enough to leave the already persisted
nine paths in place. Those clauses had forbidden persistence before all hard
conjuncts passed and required a false or missing fact to select failure with
no retained success path. Because that historical procedure was not obeyed,
neither this author nor the overlay reviewer may certify old-contract
compliance. The nine paths may not be edited, replaced, recopied, deleted,
cleaned, or re-persisted. They confer no R1 or downstream authority. An
overlay reviewer certifies only overlay truth, completeness, canonicality,
append-only precedence, and provenance. If authoring or overlay review finds
a blocker, it writes nothing and leaves the nine paths quarantined; no cleanup,
blocker artifact, retry, or rebuild follows automatically.

## 8. Overlay, validators, and final inventory contract

The strict-canonical overlay uses schema
`PAPER23_R0_BUILD_EVIDENCE_CORRECTION_V1`, artifact ID
`paper23_r0_build_evidence_correction`, status
`R0_BUILD_EVIDENCE_CORRECTION_FROZEN_PENDING_INDEPENDENT_REVIEW`, and null
self bytes/hash. It externally binds this human ledger, both original JSONs,
both staged copies, both blockers, both live roots and complete manifests,
all build-output custody identities, the three-method executable evidence,
the four corrections, the suspended semantics, the clarified governing
roots, the opening ledger, and the exact future review boundary.

The overlay's eight-condition coverage is explicit:

1. four and only four corrections bind target external identity, RFC 6901
   pointer, old/new value, resolved executable path, full stat/timestamps, and
   all three reproduced hashes;
2. both originals' four acceptance/check pointers are suspended, receipt PASS
   and metadata status are historical only;
3. the four original JSON-validation claims are scoped only to original
   erroneous syntax/canonical bytes, never semantic truth;
4. no patched pair is materialized, and all three negative virtual hashes and
   the forbidden fifth companion correction are recorded;
5. companion, self, staged-copy, persistence, atomic-nine, and original
   inventory facts remain in the original-byte/physical-history namespace,
   while this is a separate 41-to-43 transaction;
6. the delayed-recovery/quarantine exception binds old-authorization lines
   320, 375, and 402--410 without claiming historical compliance;
7. the zero-write R1 event has no invented artifact identity or terminal and
   is bound only by final roots plus path absence; and
8. the future reviewer is restricted to overlay/provenance PASS and a later
   parent alone may open a wholly new R1 audit.

Two fresh validators, authored independently of the builder's retained
validators, must reproduce the exact overlay bytes and the same value tree:

1. a duplicate-aware Python parser with a separately implemented recursive
   Unicode-code-point encoder; and
2. a custom Node recursive-descent parser with duplicate rejection and a
   custom recursive Unicode-code-point encoder.

Each validator requires exactly one physical line and one terminal LF,
recursively increasing Unicode-code-point key order, integer-only numeric
tokens, valid UTF-8 scalar strings, and no duplicate key, BOM, CR, NUL, float,
nonfinite token, unpaired surrogate, leading-zero integer, negative zero,
trailing whitespace, or trailing record. Each independently rejects at least
18 adversarial cases and accepts a non-ASCII nested control object.

At successful author stop the only additions are the mode-0644 ledger and
mode-0644 overlay, both ordinary regular root-owned link-count-one files.
The project must then be exactly 43 regular files, four child directories,
zero symlinks, and zero other objects. The 41 opening paths, three governing
roots, two live successful roots, and every executable byte must remain
unchanged. The future review path remains absent.

A fresh reviewer may create only that future review path after rehashing all
43 project files, all three roots, both permitted live roots, both
executables, the ledger, overlay, pointers, suspended semantics, canonical
bytes, validator behavior, quarantine exception, permissions, and
inventories. It must independently reproduce all four pointer old/new pairs,
all three executable hash methods and target stat/timestamp identities, both
historical-blocker bindings, every suspended-set member, the exact overlay
round trip, and every adversarial rejection. It must verify that all 41
opening paths and both permitted roots stayed stable and that final inventory
is exactly 43/4/0/0. That reviewer may certify only overlay truth,
completeness, canonicality, precedence, provenance, and recovery-exception
sufficiency—not the old receipt PASS, old-contract compliance, or a build R1
PASS. Only a later parent transition may open a wholly new corrected-R0 R1
audit. A blocker makes zero write. Corrected-R0 R1 review, source edit, R1 authorization/build,
release, Paper 24, submission, upload, transport, messaging, identity
disclosure, and every external effect remain unauthorized.

R0_BUILD_EVIDENCE_CORRECTION_AUTHOR_STOP
