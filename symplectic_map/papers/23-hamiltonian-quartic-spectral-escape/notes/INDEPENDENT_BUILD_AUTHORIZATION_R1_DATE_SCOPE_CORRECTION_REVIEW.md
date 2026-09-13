# Paper 23 — Independent R1 Date-Scope Correction Review

Date: 2026-08-25 UTC
Role: sole fresh independent correction reviewer
Disposition: PASS of the corrected date-scope authorization only

## 1. Scope, independence, and method

I am distinct from the date-scope correction author, the original R1
authorization author, the one-shot R1 builder, the old corrected-R0 reviewer,
the blocker adversary, the parent governance consumer, and every future
evidence-recovery, validator, and R2 role. I reviewed the correction under
Section 7 of notes/BUILD_AUTHORIZATION_R1_DATE_SCOPE_CORRECTION.md.

I read every one of the 50 opening project files and all three governance
roots through physical EOF and independently hashed, counted, and stated
them. I then byte-read and reconstructed complete regular-file manifests for
the four permitted retained roots. I did not access, enumerate, stat, glob,
open, hash, copy, link, or rename any excluded root.

I did not execute TeX, BibTeX, an old generator, an old validator, or either
private candidate. I did not compile, render, create a root or workspace,
edit source, edit governance, write a blocker, use a network, or cause an
external effect. The only project mutation is the exclusive creation of this
review after the complete read-only audit passed.

The correction itself was read through EOF and independently measured as:

| Path | SHA-256 | Bytes / LF | Mode / owner / device / inode / links |
|---|---|---:|---|
| notes/BUILD_AUTHORIZATION_R1_DATE_SCOPE_CORRECTION.md | f58b23173e72efffd3e0572fcc6e301b814e78026159aa65d1b44f9993c8d182 | 45,110 / 703 | 0644 / root:root / 2431 / 6444084951 / 1 |

Its final line is BUILD_AUTHORIZATION_R1_DATE_SCOPE_CORRECTION. The artifact
is internally consistent with the live state and changes only the false
decoded-stream date predicate; it does not weaken or replace any non-date
conjunct.

## 2. Opening project, governance, permissions, and absences

The independently generated, LC_ALL=C path-sorted nine-field opening
manifest contains exactly 50 LF-terminated rows and 7,003 bytes. Its SHA-256
is:

    77648ec39e3da73049284ea73f5c2d1c60b1966741a876a82a7bd4e6f4bf17f1

The project opening inventory is exactly 50 regular files, four child
directories, zero symlinks, zero other objects, and 2,068,390 regular-file
bytes. The project root and four child directories are ordinary root-owned
mode-0755 directories. All 50 files are ordinary root-owned mode-0644,
link-count-one regular files. Independent per-path rows reproduce the 49
rows frozen in Section 2 of the correction plus the correction identity
above; no row differed.

The three governance roots were independently read and measured:

| Governance root | SHA-256 | Bytes / LF | Mode / owner / device / inode / links |
|---|---|---:|---|
| BATCH_06_STATUS.md | 7ec4dc151e3046ea331e319087dd0341a90c0e5f6f96129a2604da62c9b46315 | 107,942 / 1,582 | 0644 / root:root / 2431 / 12439253850 / 1 |
| BATCH_06_IDEA_REPORT.md | 8b8c3433df5d04bccb44313790590113b4e6ae901ec0c60745d1d4743dbfed6f | 177,937 / 3,316 | 0644 / root:root / 2431 / 12439253853 / 1 |
| BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md | 27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4 | 8,524 / 245 | 0644 / root:root / 2431 / 12439253857 / 1 |

The live gate remains PAPER23_R1_DATE_SCOPE_CORRECTION_OPEN and the queue
remains R1_BUILD_BLOCKED_PENDING_DATE_SCOPE_CORRECTION. This is the correct
pre-parent-consumption state.

Immediately before this exclusive creation, each of the following was
absent under no-follow checks: this review path; paper/main_round1.pdf;
paper/BUILD_METADATA_R1.json; paper/BUILD_RECEIPT_R1.json;
notes/BUILD_R1_EVIDENCE_RECOVERY_BLOCKER.md; and
notes/INDEPENDENT_BUILD_R2_R1_EVIDENCE_RECOVERY_REVIEW.md. Effective
permission permits only this successful review write. Recovery execution,
R2, source change, retry, rebuild, finalization, release, Paper 24, network,
and every external effect remain unauthorized.

## 3. Retained-root custody and cross-round equality

I independently generated the complete nine-field manifest for each
permitted root:

| Root | Files / dirs / links / other | Regular bytes | Manifest bytes / LF / SHA-256 |
|---|---:|---:|---|
| /tmp/paper23-r1-noop-A.e2oejfix | 46 / 2 / 0 / 0 | 10,628,945 | 6,644 / 46 / c6ad905708bdb37fa48dc16992804fe6c20f00eaa772fb6f4d0c47b420b926e6 |
| /tmp/paper23-r1-noop-B.xc72gwxv | 13 / 0 / 0 / 0 | 648,698 | 1,515 / 13 / 5e04fb958c58b094762b121129b82494832424f903f2305ed061fad54fb9a27a |
| /tmp/paper23-r0-repair-correction-A.Er2f85 | 43 / 1 / 0 / 0 | 8,637,740 | 5,655 / 43 / 415f5d1d47828a25154f2dea5423d8259cdd40b3085a3b4c4d2140607f237b38 |
| /tmp/paper23-r0-repair-correction-B.tcCPcQ | 13 / 0 / 0 / 0 | 648,698 | 1,515 / 13 / 1d0e5a4a101f148a449dac5bd5499c5bf87daccb995ea27b42cf84eb7129a067 |

All four roots and their directories are private root-owned mode-0700
objects. No manifest, ownership, mode, link, or object-type discrepancy was
found.

Direct byte comparison across both retained R1 roots and both permitted
corrected-R0 roots gave equality for all 13 common paths:

| Path | SHA-256 | Bytes / LF |
|---|---|---:|
| main.tex | 1ac57197ff87b2c1c6ec2cea7cf644021e629e519e4215d4b32e9e4420aa46b0 | 67,408 / 1,776 |
| math_commands.tex | a69565204428ce95abbcab5afb3833290004110e2718c074fbc805f7d1bdcb0d | 420 / 13 |
| references.bib | ba0156abd7eb399de532b9bc1eefa81b3bb1be7868eed6ee4b42f8cd3371c782 | 2,812 / 99 |
| command-1.log | 1fcbc0319012bbeb4fd526dad9eef6a0ca9e86474e9c092ae766a70a4ef466ce | 18,124 / 597 |
| command-2.log | 7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9 | 158 / 4 |
| command-3.log | cba30ead0e25a854366d5bf7e9156ffadfb713fd4de7097a43b6f284e1d2db72 | 8,363 / 158 |
| command-4.log | ad3eb1bf23dd06e82b1683ccb3e66c34b142303fa24685f56f268f58368612b0 | 7,254 / 112 |
| main.aux | 2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb | 14,072 / 165 |
| main.bbl | baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9 | 2,881 / 73 |
| main.blg | be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34 | 900 / 46 |
| main.log | ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6 | 27,628 / 700 |
| main.out | 14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94 | 6,226 / 28 |
| main.pdf | ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37 | 492,452 / 2,724 |

Project paper/main.pdf and paper/main_round0.pdf have that same PDF identity.

The retained builder state has schema PAPER23_R1_BUILDER_LIVE_STATE_V1 and
records authority_consumed=true, retry_count=0, replacement_root_count=0,
source_edits=0, external_effects=0, and network_effects=0. Both roots record
the exact environment PATH=/usr/bin:/bin, SOURCE_DATE_EPOCH=1787616000,
FORCE_SOURCE_DATE=1, TZ=UTC, LC_ALL=C, LANG=C and the same four commands:
pdflatex -interaction=nonstopmode -halt-on-error main.tex; bibtex main; then
the same pdflatex command twice. Each command is recorded exactly once and
each A/B exit vector is [0,0,0,0].

Fresh read-only resolution and hashing, without executing either program,
gave:

| Invoked token | Resolved object | SHA-256 | Bytes / LF | Mode / owner / links |
|---|---|---|---:|---|
| pdflatex | /usr/bin/pdftex | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 | 1,802,504 / 4,629 | 0755 / root:root / 1 |
| bibtex | /usr/bin/bibtex.original | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f | 117,128 / 393 | 0755 / root:root / 1 |

The 17 recorded invocation-time executable observations are mutually stable
and agree with the fresh objects.

## 4. Independent two-method PDF date reconstruction

I applied both methods independently to each of retained A/main.pdf and
B/main.pdf.

Method 1 used PyMuPDF only as a PDF parser: each PDF has xref_length 640; I
opened objects 1 through 639, found 86 streams, and decoded all 86.

Method 2 was a separately written raw-byte parser. It located physical
object headers, parsed every direct declared Length, required exact stream,
endstream, and endobj boundaries, and Flate-decoded every one of the 86
streams. It found 87 physical objects. It separately decoded object streams
at xrefs 2, 188, 298, 411, 497, and 603 with N values 100, 100, 100, 100,
100, and 52, thereby restoring all 552 compressed objects. The physical and
compressed union is exactly 639 objects with no missing or duplicate xref.

Both methods, independently in A and B, reconstruct exactly 25
FontDescriptor objects at odd xrefs 521 through 569 and exactly 25 direct
FontFile targets at even xrefs 520 through 568. Every target has exactly one
reverse FontDescriptor reference, generation zero, under /FontFile; there
are no /FontFile2 or /FontFile3 cases. Each full decoded target begins with
the Type1 header shown below, contains exactly the shown DSC line, and has
the shown complete decoded-stream SHA-256. A and B agree row for row:

| Stream / descriptor | SHA-256 | Type1 header | Exact DSC line |
|---:|---|---|---|
| 520 / 521 | 3f2b2412ba793700eca46017f17600fb96ddd6574ab390d38ac695f214544df0 | %!PS-AdobeFont-1.0: LMRoman10-Bold 2.004 | %%CreationDate: 7th October 2009 |
| 522 / 523 | 7001c66d17731a3d6312ed5b604267a632121afb7422b3909bbae9046eec0564 | %!PS-AdobeFont-1.0: LMRoman12-Bold 2.004 | %%CreationDate: 7th October 2009 |
| 524 / 525 | f94fbf068d0b4963dbc0f67a47d1b27a795ae2e76e59bdce7a647f9b2e8b3558 | %!PS-AdobeFont-1.0: LMMathExtension10-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 526 / 527 | 6896d5158b3326198795d6ac86715a65e91e089ad6b79691e657867ad9f78da8 | %!PS-AdobeFont-1.0: LMMathItalic10-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 528 / 529 | fa1e434453c7e9693f45e8788cf9413c03727daba2c4073be91abf73ba38fcdb | %!PS-AdobeFont-1.0: LMMathItalic12-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 530 / 531 | 367a7d7f78fb0788173998ba3826863b65d78aa02d71f56e87d07ac04b6118db | %!PS-AdobeFont-1.0: LMMathItalic6-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 532 / 533 | 3d11294f1f6bee22d548a8aeb49957529d837b00830496af473f08cec15bbc67 | %!PS-AdobeFont-1.0: LMMathItalic7-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 534 / 535 | df85086add9c26fad855c759a7b11922d8219325646b65d14b17f1fb7a38316c | %!PS-AdobeFont-1.0: LMMathItalic8-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 536 / 537 | e665f919e8aca84d282d7388ecc94090e787b086ffde448e644d25a6e80a69ef | %!PS-AdobeFont-1.0: LMMathItalic9-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 538 / 539 | e615161a70103dfc5c8e2840e87f4c53d6b49ed5a53a84f38e8f2642a8078668 | %!PS-AdobeFont-1.0: LMRoman10-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 540 / 541 | 2a43d4520f1fed5d8fc6a3ac2ae86ffadff592722a8d668e7f2cbad21f4ebde7 | %!PS-AdobeFont-1.0: LMRoman12-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 542 / 543 | 81f086d7c4eff62aa5ac13e967f22f011af6f62624ae3d8e6ad65e19ba7cfa85 | %!PS-AdobeFont-1.0: LMRoman17-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 544 / 545 | 6386d6476b7788fb7df5c971a8aa361b95a303732f8563d036ea4e1e21511df5 | %!PS-AdobeFont-1.0: LMRoman5-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 546 / 547 | 203cba302577bff6edd2f346d1044579f97f1e1162f1716093c344f547400d2e | %!PS-AdobeFont-1.0: LMRoman6-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 548 / 549 | b895591fa37e4ddfbe73cb4dd9a70b045d7a3cc4dd858f96f4e6e097d3b5be2b | %!PS-AdobeFont-1.0: LMRoman7-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 550 / 551 | 94939c10dcdea65367717cd11a1be404c0185a50e9361f0c8518bd10a720b76c | %!PS-AdobeFont-1.0: LMRoman8-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 552 / 553 | d3510a81ca4f12d49bf99cdd7984ec2d912bcc492652565b18e8557460e0e0f9 | %!PS-AdobeFont-1.0: LMRoman9-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 554 / 555 | 42ef87168a474cf2375a5d95f81b0656a9f7cb0c1340ee216f3a558324baaa51 | %!PS-AdobeFont-1.0: LMRoman10-Italic 2.004 | %%CreationDate: 7th October 2009 |
| 556 / 557 | 5d2ef6743c585b4098d2229533731b340e837fdb59f0988c95a2df4d61513d9d | %!PS-AdobeFont-1.0: LMSans8-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 558 / 559 | 57c354b5d60cf35c259685831139b70ee79046a19f5c12f73665314ba5ee75d1 | %!PS-AdobeFont-1.0: LMMathSymbols10-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 560 / 561 | b2e42563676cedbc536688423b7dddfd23601f46b8cdf71d3410b5925372824d | %!PS-AdobeFont-1.0: LMMathSymbols6-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 562 / 563 | 8b05a113bcff07f424579b1a562cd8fd3c7a46680fd37af976cf4138f4e271b8 | %!PS-AdobeFont-1.0: LMMathSymbols8-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 564 / 565 | 00a02deed0ab52f21ac5ff4f4faf319b8f43a4e195752599974e4a717206c761 | %!PS-AdobeFont-1.0: LMMathSymbols9-Regular 1.200 | %%CreationDate: 16th September 2009 |
| 566 / 567 | 013dbf48070f76f9f49eb536ed3ac55ee4464d7c2988453f1eb91bac8e0e7bb7 | %!PS-AdobeFont-1.0: LMMono10-Regular 2.004 | %%CreationDate: 7th October 2009 |
| 568 / 569 | d78936dba7be30eb2701e1e1fad6abe8237e161133eb187ffb3cbe57bef812e9 | %!PS-AdobeFont-1.0: MSBM10 003.002 | %%CreationDate: Mon Jul 13 16:17:00 2009 |

The independently measured class cardinality in each PDF is exactly 25
occurrences in 25 distinct streams: 13 October 7 comments, 11 September 16
comments, and one July 13 comment.

The corrected hard-zero namespace passes independently in each PDF:

| Namespace or surface | CreationDate | ModDate | PDF D: date | Unclassified |
|---|---:|---:|---:|---:|
| raw PDF bytes | 0 | 0 | 0 | 0 |
| all raw/decoded object dictionaries, trailer, Catalog, pages, annotations, outlines, and Info | 0 | 0 | 0 | 0 |
| decoded streams outside the 25 exact Type1 rows | 0 | 0 | 0 | 0 |
| XMP/metadata streams | 0 | 0 | 0 | 0 |
| pdfinfo -rawdates and ordinary metadata API | 0 | 0 | 0 | 0 |
| visible/extracted manuscript text and links | 0 | 0 | 0 | 0 |

Info xref 638 contains no date key; its author, subject, creator, producer,
and keywords are empty. There is no metadata stream. The 25 classified
CreationDate strings occur only as the exact Type1 DSC provenance comments
above. ModDate is zero everywhere, document/build dates are zero everywhere,
and unclassified CreationDate is zero.

Lines 579–581 of
notes/INDEPENDENT_BUILD_R1_R0_REPAIR_CORRECTION_REVIEW.md are therefore
factually false as to decoded-stream dates and are noncredited. I did not use
that review, the retained ledger, the correction prose, governance prose, or
either candidate as proof of the date result.

## 5. Independent non-date conjunct audit

All original non-date conjuncts remain hard and passed:

- Logs and closure: A/B logs are byte-identical. Command 1 has the expected
  first-pass unresolved-reference and citation warnings; command 2 is clean;
  command 3 has no LaTeX warning and only the expected citation/rerun package
  warnings; command 4 and final main.log have zero error, fatal, undefined
  reference/citation, overfull, underfull, or hyperref warning. main.blg
  records nine entries and zero warning.
- Citations, labels, and bibliography: the source has nine distinct citation
  keys, the AUX has nine citation commands and nine bibcite keys, the BIB and
  BBL have the same nine items, and all sets agree. The source has 95 unique
  labels; AUX has the same 95 newlabels; all 116 source references resolve.
  Bibliography style plainnat and database references are correct.
- Structure: both PDFs are PDF 1.5, 492,452 bytes, 23 nonblank US-Letter
  pages at 612 by 792 points and rotation zero, xref length 640, 86 streams,
  trailer Size 640, Root 637, Info 638, and no repair or encryption.
- Security: zero JavaScript, Launch, SubmitForm, ImportData, embedded file,
  Filespec, AcroForm, XFA, signature, RichMedia, Movie, Sound, Screen, 3D,
  Collection, or image object; pdfdetach reports zero attachment. The
  ordinary OpenAction is an internal GoTo to page one.
- Fonts and links: pdffonts reports 31 Type1 rows, all embedded, subset, and
  Unicode-mapped. There are 136 links: 135 internal GoTo links and the sole
  URI https://arxiv.org/abs/2509.14584. No dangerous or private link exists.
- Identity and privacy: the visible title matches the source; Anonymous
  appears exactly once on page one; metadata author/creator/producer is
  empty; no email, ORCID, institutional identity, private marker, governance
  marker, digest, or agent text appears.
- Navigation and pagination: AUX/OUT/PDF agree on nine sections and 19
  subsections. All 28 bookmarks have the expected level, order, text, and
  destination. Abstract begins on page 1, Section 9 begins on page 20,
  Conclusion is on page 22, References begins on page 23, and there is no
  appendix. Substantive content occupies pages 1–22 and satisfies the hard
  22-page bound.
- Retained rendering: root A has exactly page-01.png through page-23.png,
  each a valid RGB 1700 by 2200 PNG. I inspected all 23 individually at
  original raster resolution. There is no clipping, overlap, collision,
  missing glyph, corrupt page, bad table, bad margin, or harmful page break.
- Mathematics: a new symbolic audit passed 29 of 29 checks: C_g=B_gA_g; all
  six principal 2-by-2 and four principal 3-by-3 minors; e2, e3, det A_g,
  det B_g, det C_g; the complete characteristic polynomial, coefficient
  factorization, R_g(1), and Cayley–Hamilton recurrence; both shifted
  kernels; all six cone-wall identities; both second-phase selector
  identities and the four seed margins; the g=9 boundary vector
  (1,0,-2,5); and positivity of the carry/visibility matrices at the lower
  endpoint. Independently exhaustive arithmetic over F5 gives values
  (1,4,2,4,3), no linear root, and zero solutions among all 625 ordered
  monic-quadratic coefficient tuples, proving the claimed exclusion.

## 6. Recovered-R0, no-op, quarantine, and historical outcome

The recovered-R0 model independently resolves exactly four corrected
executable-digest pointers: bibtex and pdflatex in each immutable original
metadata and receipt. Their old erroneous values and new live values match
the overlay. Exactly eight original acceptance pointers are suspended and
noncredited, exactly eight canonical-validation assertions are confined to
syntax of the immutable erroneous records, no fifth pointer is authorized,
and no physical or virtual patched JSON pair exists. The three negative
virtual hashes and all six prospective evidence artifacts agree with the
governed model. Original-R0 as-written PASS and old-contract compliance
remain false; there is no retroactive cure.

paper/SOURCE_REVISION_RECEIPT_R1.json has schema
PAPER23_SOURCE_REVISION_RECEIPT_R1_NO_OP_V1 and status
R1_NO_OP_REVISION_PASS. Its one revision window is consumed, one total, zero
remaining; required and cosmetic findings are both zero; changed paths and
hunks are empty; all change counters are zero; and the three source
identities before and after are exactly equal. The no-change ledger has
SHA-256 d632175aa1a9ab29d782e2b300b40c7f334021979e785def4deb4191c8de0e09,
15,558 bytes, 205 LF, and the correct terminal.

The two private R1 candidates remain quarantined and unaccepted. I hashed
but did not parse, copy, canonicalize, import, transform, or execute them:

| Candidate | SHA-256 | Bytes / LF | Mode / owner / links |
|---|---|---:|---|
| BUILD_METADATA_R1.candidate.json | c5cfbaff5b3e3362c9daccfa76d2ef0c79a104bd90083c614ec41a1d4154b031 | 189,974 / 1 | 0600 / root:root / 1 |
| BUILD_RECEIPT_R1.candidate.json | d0f7bd4e5e198bd032078a5116315aaa29ef551087be427d419938264d6e0e3d | 38,858 / 1 | 0600 / root:root / 1 |

Old generator and validator files were used only as opaque custody bytes for
the root manifest. None was executed, imported, copied, or treated as
evidence.

The original R1 authorization remains immutable, its authority remains
consumed, and notes/BUILD_R1_BLOCKER.md remains SHA-256
ce755d09cd57dc156c55fce94d1d2b68c54e7affd9ebb55c461f9a209930b55d,
11,251 bytes, 216 LF, with terminal R1_BUILD_BLOCKED. There was no retry,
replacement root, fifth command, source edit, candidate reuse, or success
persistence. The original invocation remains R1_BUILD_BLOCKED and receives
no retroactive PASS.

## 7. Disposition

Every hard conjunction in Section 7 passes and I found zero recorded or
unrecorded blockers. This correction is accepted only as a prospective,
append-only repair of the false date predicate. It does not amend the
historical blocked build, revive consumed authority, or authorize recovery.

Creation of this one review makes the project exactly 51 regular files, four
child directories, zero symlinks, and zero other objects. Recovery remains
closed until a separate parent reads this review and the correction through
EOF, binds their final identities in both governance ledgers, and explicitly
opens the evidence-only recovery gate. I stop here without parent
consumption, recovery execution, R2 review, or any external effect.

BUILD_AUTHORIZATION_R1_DATE_SCOPE_CORRECTION_PASS
