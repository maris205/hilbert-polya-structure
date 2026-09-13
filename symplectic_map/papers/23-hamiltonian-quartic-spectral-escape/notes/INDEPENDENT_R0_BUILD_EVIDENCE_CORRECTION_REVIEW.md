# Independent R0 build-evidence-correction review

## 1. Decision and deliberately narrow scope

I am the fresh reviewer of the Paper 23 append-only R0 build-evidence
correction. I am distinct from the correction author and from all builders. I
independently reviewed the correction layer, its human ledger, its provenance,
its canonical representation, its semantic precedence rules, and the delayed
recovery/quarantine exception. I find no blocking omission, contradiction,
unverifiable correction, ambiguous target, numeric-precision loss, circular
self-claim, temporal falsehood, causal overreach, or excess authority in that
layer.

This is therefore a PASS of only:

1. the truth and completeness of the four-pointer correction map;
2. the strict canonicality and independent reproducibility of the correction
   overlay;
3. the correction map's append-only factual precedence over those four
   immutable erroneous original fields;
4. the provenance and preservation evidence bound by the overlay; and
5. the sufficiency of the recovery exception for prospective custody and a
   wholly new corrected-R0 R1 audit.

This review does **not** certify the original receipt as PASS, historical
compliance with the old build authorization, any build command or build
result, PDF/visual/citation/theorem truth, any source revision, or
`BUILD_R1_R0_REPAIR_CORRECTION_PASS`. It does not authorize compilation,
rendering, cleanup, source mutation, R1 work, release, Paper 24 work, or an
external effect. Its only downstream consequence is that a later parent may
decide whether to open a wholly new corrected-R0 R1 audit.

## 2. Review universe and access boundary

I read all 43 opening project regular files through EOF. Textual files were
read as complete byte streams and decoded where appropriate. Binary PDFs and
PNGs were hashed and structurally identified as binary objects; I did not
render them and make no PDF or visual acceptance finding. I also read all
three current governance roots through EOF, both original JSON records, both
historical blockers, the authorization and correction-review history, the
complete ledger and overlay, both permitted correction roots and their full
manifests, the retained author-validator base, and the exact executable
objects `/usr/bin/pdftex` and `/usr/bin/bibtex.original`.

I did not access, list, stat, glob through, or touch any of the four excluded
roots named by the overlay. Literal names occurring in already-authorized
records were treated only as record contents.

The logical validator paths `author-private/validate_overlay.py` and
`author-private/validate_overlay.js` do not resolve physically from the
overlay itself. I resolved them solely under
`/tmp/paper23-evidence-correction-author-stage.Wi0tmI`, because the later
parent addendum in the current governance roots supplies that exact read-only
mapping for this review. This is a material provenance limitation: without
that external parent mapping, the overlay's two logical script identities
would not be independently locatable. The mapping cures only path resolution;
it neither changes an overlay fact nor grants any further filesystem or
downstream authority.

## 3. Frozen correction records

The human ledger is an ordinary root-owned mode-0644 regular file, link count
one, with these reproduced properties:

- path: `notes/R0_BUILD_EVIDENCE_CORRECTION.md`;
- SHA-256:
  `89e56bf502a2d40ecb831991b4d5edd5e2672fcd3c1f9149d6edb2222a8f5b01`;
- 31,005 bytes and 426 LF; and
- terminal line exactly `R0_BUILD_EVIDENCE_CORRECTION_AUTHOR_STOP`.

The machine overlay is an ordinary root-owned mode-0644 regular file, link
count one, with these reproduced properties:

- path: `paper/BUILD_EVIDENCE_CORRECTION_R0.json`;
- SHA-256:
  `257d37600e9c7498b3e801d08fce3391d6852c5ce34ba1d468c502e357de7bfd`;
- 41,366 bytes, exactly one physical line, and exactly one terminal LF;
- schema `PAPER23_R0_BUILD_EVIDENCE_CORRECTION_V1`; and
- status `R0_BUILD_EVIDENCE_CORRECTION_FROZEN_PENDING_INDEPENDENT_REVIEW`.

Both overlay self-identity members are null as required. The overlay bytes do
not contain their own SHA-256, and no non-null self-hash or self-size claim is
used to validate the overlay. The ledger was written before the overlay, the
two paths are the only additions to the opening 41-file project universe, and
the independent review path was absent at this review's opening.

## 4. Independent canonical validation

I implemented two new validators in separate project-external mode-0700
private temporary roots. They were authored independently of the correction
author's code and independently of each other:

- a Python duplicate-aware parser using an object-pairs hook, integer-only
  hooks, arbitrary-precision integers, Unicode-scalar normalization, and a new
  recursive Unicode-code-point encoder; and
- a Node validator using a custom recursive-descent parser, explicit duplicate
  detection, `BigInt` integer semantics, surrogate validation, a new
  Unicode-code-point comparator, and a new recursive encoder.

Each validator required strict UTF-8, valid Unicode scalars, integer-only JSON,
increasing Unicode-code-point object-key order at every depth, minimal
canonical escaping, one physical line, and one terminal LF. Each independently
rejected the same 35 adversarial cases, covering:

- root, nested, escape-equivalent, and astral-equivalent duplicate keys;
- ASCII and non-BMP key-order violations;
- fractions, exponents, leading zero, negative zero, plus sign, NaN, and
  positive/negative Infinity;
- BOM, invalid UTF-8, CRLF, embedded LF, missing/extra LF, NUL, raw control,
  trailing space/tab, a second record, and content after the terminal LF;
- unpaired high/low surrogates and a malformed pair; and
- noncanonical BMP, astral, and slash escapes plus array/object trailing
  commas.

Each also accepted five controls, including positive and negative integers far
beyond `2^53`, nested non-ASCII and astral strings, and canonical control
escapes. I counted 42 integer values beyond `2^53` in the overlay and preserved
all of them exactly. Both implementations reproduced the exact bytes of the
overlay and both originals. A separately designed length-delimited typed-tree
witness also agreed across Python and Node for all three documents, with these
tree SHA-256 values:

| Document | Typed-tree SHA-256 |
|---|---|
| overlay | `70937ed34224d49bd6d52aa6cdd6b25602a5702105d659d4c14039cf33f342c6` |
| original metadata | `eef140cc3f2e4576b39a06788229708bf55e649601632bd1f8f3511b4eee3509` |
| original receipt | `16a7818a1e8a7f39bb59a705c9c1d743dc3f608ab3ba63f7f91fa30e21535aee` |

Thus the result is not based on a permissive parse, JavaScript floating-point
rounding, or merely comparing two file hashes.

## 5. Author-validator provenance and independent audit

The retained validator base is a root-owned mode-0700 ordinary directory on
device 149, inode 9128038911, link count two. It contains exactly five direct
regular files, no child directories, no symlinks, and no other objects. Its
complete five-record manifest is 659 bytes and five LF, SHA-256
`21f25dcbdc32c8a6e42017b5a0286d0b9a67475e529cf473241d1586100b5825`.

The two resolved validator objects are root-owned mode-0644 ordinary regular
files with link count one:

| Logical path | Device/inode | Bytes/LF | SHA-256 |
|---|---:|---:|---|
| `author-private/validate_overlay.py` | 149/9128038899 | 6,056/197 | `e7582729b803e6ca1ea323a4f0bfe950ebd9a2b17fb83537f0d5b76857c2bc31` |
| `author-private/validate_overlay.js` | 149/9128038900 | 10,002/256 | `21d44d2ba515de2fea15d3b6aa14077929056d7cd2490067b29304f251c8e4be` |

I read both scripts completely, separately assessed their parser/encoder logic,
and invoked each on the overlay, original metadata, and original receipt. All
six executions reproduced exact canonical bytes, rejected all 22 of each
author validator's adversarial cases, and accepted its non-ASCII nested
control. I did not use those executions as a substitute for my own validators.

## 6. Exactly four factual corrections

I resolved every correction pointer against each immutable original value
tree. There are exactly four unique target/pointer entries and no fifth or
other factual correction:

| Target | JSON pointer | Exact old erroneous value | Exact new observed value |
|---|---|---|---|
| `paper/BUILD_METADATA_R0.json` | `/build/executable_identities/bibtex/sha256` | `c9ecb7182f287007d277d67a1537a721493f2d3b0c98d16006ba24493710618f` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `paper/BUILD_METADATA_R0.json` | `/build/executable_identities/pdflatex/sha256` | `01a7ab54dd9ca121cc8694f3bb656633682f2e2fd5fba6f9adcd8a9508336cf9` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `paper/BUILD_RECEIPT_R0.json` | `/build/executable_identities/bibtex/sha256` | `c9ecb7182f287007d277d67a1537a721493f2d3b0c98d16006ba24493710618f` | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `paper/BUILD_RECEIPT_R0.json` | `/build/executable_identities/pdflatex/sha256` | `01a7ab54dd9ca121cc8694f3bb656633682f2e2fd5fba6f9adcd8a9508336cf9` | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |

The two original records remain byte-for-byte unchanged:

- metadata: SHA-256
  `599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362`,
  70,889 bytes and one LF, device/inode 2431/3227322490; and
- receipt: SHA-256
  `70ad2b65c82201981488c5bcc4685f08f37529504082afb7e1778248c96cd590`,
  71,124 bytes and one LF, device/inode 2431/3227322494.

Their full modes, ownership, link counts, and atime/birth/ctime/mtime evidence
also matched every repeated target identity in the overlay. The staged copies
at the permitted A root have the same exact bytes as their corresponding
project originals and retain the overlay-recorded identities.

## 7. Executable evidence and causal defect

I independently streamed each exact executable through Python SHA-256, GNU
`sha256sum`, and OpenSSL `dgst -sha256`. All three methods agreed for each
object:

| Exact object | Device/inode | Mode/owner/links | Bytes/LF | Reproduced SHA-256 |
|---|---:|---|---:|---|
| `/usr/bin/pdftex` | 149/3829692913 | 0755, `root:root`, 1 | 1,802,504/4,629 | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `/usr/bin/bibtex.original` | 149/3829692848 | 0755, `root:root`, 1 | 117,128/393 | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |

`/usr/bin/pdflatex` resolves to the exact `pdftex` object, and
`/usr/bin/bibtex` resolves to the exact `bibtex.original` object. I reproduced
all four nanosecond timestamp fields recorded for both objects. In particular,
their births/ctimes are respectively
`2026-07-30 02:12:41.969305619 +0000` and
`2026-07-30 02:12:41.961305260 +0000`; both mtimes are
`2026-01-27 17:36:46.000000000 +0000`; and the recorded atimes also match.

The permitted A-root generator
`validation-pages/generate_candidates.py` is device/inode 149/10739843347,
35,751 bytes and 632 LF, SHA-256
`6acd07e156581831730bfbd5768f0d52fe2c99663151350b50d1c01d93e3a81e`.
Its physical lines 384 and 385 contain exactly the two erroneous static digest
literals. Complete source inspection confirmed the described route from the
common value tree through metadata/receipt deep copies and canonical
serialization. Complete inspection of the retained builder validators
confirmed that they checked candidate syntax/round trips but did not hash the
named executable objects. Canonical encoding therefore faithfully preserved
two false facts; canonicality did not make those facts true.

The historical blocker identities and terminal lines reproduce as follows:

| Blocker | SHA-256 | Bytes/LF | Birth UTC | Terminal |
|---|---|---:|---|---|
| `notes/BUILD_R0_BLOCKER.md` | `8d395e7fdeb2103370b1b1700c1bd54301f0f1206c5a3eea4352298cdd1c5384` | 8,900/180 | `2026-08-24 20:23:30.763348799 +0000` | `R0_BLOCKED` |
| `notes/BUILD_R0_REPAIR_BLOCKER.md` | `c05d9bb243bd28cd43dee4972f5ee829d01b165b73e7b9bef25a8c4f6940f472` | 11,493/223 | `2026-08-24 21:41:23.642849395 +0000` | `R0_REPAIR_BUILD_BLOCKED` |

Both blockers contain the actual executable hashes above and predate the two
permitted correction roots, whose shared birth is
`2026-08-24 22:32:59.485275005 +0000`. That chronology supports the overlay's
defect provenance and does not retroactively turn the old erroneous records
into compliant success records.

## 8. Suspended semantics and immutable original namespace

The overlay contains exactly eight unique suspended original pointers: the
Cartesian product of the two originals and these four pointers:

- `/acceptance/all_hard_conjuncts_pass` with original value `true`;
- `/acceptance/blocker` with original value `null`;
- `/acceptance/chosen_outcome` with original value `success`; and
- `/checks/success_paths_absent_before_complete_validation` with original
  value `true`.

Every pointer resolves to the stated original value and every pending state is
`suspended_not_credited`. The original receipt's `/status` value
`BUILD_R0_REPAIR_PASS` is only a suspended historical builder claim. The
metadata status `BUILD_METADATA_R0_REPAIR` is only an original-record label;
neither is an effective semantic PASS here.

The overlay separately contains exactly eight unique syntax-only validation
scope entries: the Cartesian product of the same two originals and these four
true-valued pointers:

- `/json_validation/candidate_hashes_recorded_before_persistence`;
- `/json_validation/candidate_round_trips_exact`;
- `/json_validation/two_value_trees_agree`; and
- `/json_validation/validation_completed_before_persistence`.

Those claims apply only to the immutable erroneous candidates' syntax,
canonical bytes, and original persistence chronology. They do not establish
semantic truth, executable identity truth, all hard conjuncts, overlay
validation, or a virtual patched document. Companion-candidate identity,
self-identity, staged-copy equality, these four candidate-validation claims,
persistence, the atomic nine-path claim, and original inventory all remain in
the immutable original-byte namespace. The overlay does not silently reinterpret
them as claims about corrected virtual documents.

## 9. Negative virtual checks and nonmaterialization

Using independent in-memory deep copies and my own canonical encoder, I first
changed only the two executable pointers in each original. I then separately
tested the forbidden fifth receipt companion correction. The exact results are:

| In-memory counterexample | Bytes | Reproduced SHA-256 |
|---|---:|---|
| four-pointer-pair virtual metadata member | 70,889 | `9a1864be2795df47a3f82855f2b1aef2aa51424809c7550767c466a7fc9a4493` |
| four-pointer-pair virtual receipt with old companion hash | 71,124 | `d675ef6aeca693c732f4f39601f5b68592f7dda2cab4ca7bf2bc956346397a15` |
| unauthorized fifth-companion-corrected virtual receipt | 71,124 | `3b6b6343dd1d07aa6106f07e9c61ee451cc8c4e74f0ad918d1d086fb11e5b67c` |

The four-pointer virtual receipt is intentionally internally inconsistent
because its immutable companion member still names the original metadata hash.
The fifth companion correction is not authorized. I found none of these three
hashes among any regular file in the project, either permitted correction
root, or the retained validator base. I created no virtual patched JSON file.
The overlay therefore defines factual pointer precedence only; it neither
defines nor materializes a patched JSON pair.

## 10. Custody, recovery exception, and zero-write R1 history

The old authorization
`notes/BUILD_AUTHORIZATION_R0_REPAIR.md` remains immutable at SHA-256
`d2af138c12d3abc59dce9d7950a7e53113e2b1f8c1b312a1d4803c3b5cc8d207`.
The recovery exception supersedes only its custody lines 320, 375, and
402--410, and only prospectively for recovery. The overlay expressly states,
and this review preserves, all of the following:

- the historical builder did not comply with those superseded old clauses;
- neither the correction author nor this reviewer may claim old compliance;
- the nine surviving paths are immutable in-situ quarantined evidence;
- the nine paths are not accepted success artifacts and confer no downstream
  authority; and
- a blocker leaves them in place and writes nothing; it does not trigger
  automatic cleanup, retry, or rebuild.

This delayed exception is sufficient for prospective custody because it gives
a fresh corrected-R0 R1 reviewer a stable evidence universe while explicitly
denying retroactive compliance. It would not be sufficient if read as a cure
of the old contract; the overlay forbids that reading.

The nine quarantined project identities all match the opening ledger:

| Path | Bytes/LF | SHA-256 |
|---|---:|---|
| `paper/BUILD_METADATA_R0.json` | 70,889/1 | `599a8c3e1578e79fee6dff197d0cd8d3bcb3cb06ab13ebd4b8e1c975ec951362` |
| `paper/BUILD_RECEIPT_R0.json` | 71,124/1 | `70ad2b65c82201981488c5bcc4685f08f37529504082afb7e1778248c96cd590` |
| `paper/main.aux` | 14,072/165 | `2748935c255778a4e40227c008adeb8c361a3933a9ff5f545407f04ae48c8eeb` |
| `paper/main.bbl` | 2,881/73 | `baa229dd7d35d96b27d7dfb18a844db73c98b752df3be4c008d748636f199cf9` |
| `paper/main.blg` | 900/46 | `be7e80a71c65ef8bbfcc2e43c3aadcc0b89cb8216e61a785ca24403ec6c04c34` |
| `paper/main.log` | 27,628/700 | `ab451da731a6ef13c7f1f83e9de463b4b2d71b0cb255e10b2d831a235aaa13f6` |
| `paper/main.out` | 6,226/28 | `14be6d78b541eb75e29cec5bf18d1e9a26bfb0c128ddaa5f4c26ab00d315bb94` |
| `paper/main.pdf` | 492,452/2,724 | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` |
| `paper/main_round0.pdf` | 492,452/2,724 | `ae37679ef3ee4fa0b86f41e073f374920499f4959a196e289829e654b3d12d37` |

The failed R1 review path
`notes/INDEPENDENT_BUILD_R1_R0_REPAIR_CORRECTION_REVIEW.md` remains absent.
Consistently with a zero-write event, the overlay assigns it no artifact
identity, bytes, hash, status, verdict, or terminal. I found no invented R1
review artifact.

## 11. Complete manifests and preservation

I independently regenerated manifests with C-locale bytewise relative-path
ordering and records of path, SHA-256, bytes, LF, mode, owner, device, inode,
and link count. Modes in the manifest records use `stat %a` form such as
`644`, while human identity tables display `0644`.

The opening 41-project-file manifest is exactly 5,663 bytes and 41 LF, SHA-256
`aed0c364be9af4ed1b8d0748a3a0b61246ac239d37da07287ee976c3a3e27164`.
Every one of its 41 path identities still matches. Before this review file was
created, the project contained exactly 43 regular files, four child
directories, zero symlinks, and zero other objects. All 43 regular files were
root-owned, mode 0644, link count one. The four exact child directories were
`experiments`, `notes`, `paper`, and `refine-logs`, each with the identity
bound in the overlay.

The two permitted correction roots remain ordinary root-owned mode-0700
directories with these complete inventories:

| Root | Device/inode/links | Files/dirs/links/other | Regular bytes | Manifest bytes/LF | Manifest SHA-256 |
|---|---:|---:|---:|---:|---|
| `/tmp/paper23-r0-repair-correction-A.Er2f85` | 149/6443678302/3 | 43/1/0/0 | 8,637,740 | 5,655/43 | `415f5d1d47828a25154f2dea5423d8259cdd40b3085a3b4c4d2140607f237b38` |
| `/tmp/paper23-r0-repair-correction-B.tcCPcQ` | 149/6981323841/2 | 13/0/0/0 | 648,698 | 1,515/13 | `1d0e5a4a101f148a449dac5bd5499c5bf87daccb995ea27b42cf84eb7129a067` |

For all 13 artifacts common to A and B, I reproduced the overlay-recorded
hash, byte count, LF count, and each root-specific inode. The staged originals,
all nine quarantined paths, all 41 opening paths, both permitted-root complete
manifests, and both executable-object identities stayed stable across the
review. This supports the overlay's preservation claims within the inspected
namespaces. It is not a new audit or acceptance of what the build outputs
mean.

## 12. Governance chain and precedence

The overlay's `governance.roots` object is an author-start snapshot, not a
claim that its old status/idea identities are the current files after the
parent review-gate transition. In particular, it binds:

- old `BATCH_06_STATUS.md` SHA-256
  `8b58f012f8751469f05696918f6ed840f00f85a9188c8b7c67bc5eddd9a2e5ba`,
  94,404 bytes and 1,387 LF;
- old `BATCH_06_IDEA_REPORT.md` SHA-256
  `24933399b24d94c781661f102205dd3f7de63d5fe588c348f2aabe15288f9d7a`,
  152,998 bytes and 2,889 LF; and
- the unchanged correction-review root SHA-256
  `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4`,
  8,524 bytes and 245 LF.

I reproduced the old idea-report snapshot exactly as the first 2,889 LF of the
current idea report. The current parent roots, read in full immediately before
this decision, are:

| Current governance root | Bytes/LF | SHA-256 |
|---|---:|---|
| `BATCH_06_STATUS.md` | 97,228/1,429 | `22d5fcd03c3abdd39ec93080def0548766a6c68e6b351a200907a59552d2c182` |
| `BATCH_06_IDEA_REPORT.md` | 158,596/2,987 | `f05540b8e5860f8b5123af8c823b6830e59f488400546a4adab866c168083487` |
| `BATCH_06_PAPER23_PUBLICATION_LOCK_REVIEW_CORRECTION.md` | 8,524/245 | `27615c425261aa72caa4c880b6bc7f54ecfa98c99399a2d7efc78ed19d8282c4` |

The current status and idea addenda accurately bind the frozen ledger and
overlay, supply the external validator-base mapping, open only gate
`PAPER23_R0_BUILD_EVIDENCE_CORRECTION_REVIEW_OPEN`, and retain queue status
`R0_BUILD_EVIDENCE_CORRECTION_FROZEN_PENDING_INDEPENDENT_REVIEW`. They also
keep Paper 24, corrected-R0 R1 review, builds, source changes, release, and
external effects closed. Treating the overlay snapshot as historical and the
current parent addendum as the sole review transition removes any apparent
root-identity or path-resolution ambiguity.

The precedence result is consequently precise: after this independent overlay
PASS, only the four listed executable-hash facts take semantic precedence, the
eight suspended original claims remain excluded from credit, all other
original fields retain their explicitly limited historical namespace, and no
patched pair comes into existence. The effective composite is only eligible
for a parent decision about a wholly new corrected-R0 R1 audit.

## 13. Final finding

The evidence correction is true, complete for the demonstrated defect,
strict-canonical, noncircular, provenance-bound, and authority-limited. The
four corrected facts are independently reproduced from the exact executable
objects; the old values and propagation path are independently located; the
semantic suspensions and syntax-only scopes are exact; the virtual negative
hashes and nonmaterialization claims reproduce; the historical records remain
immutable; and the recovery exception is sufficient only in its stated
prospective sense. No correction-layer blocker remains.

R0_BUILD_EVIDENCE_CORRECTION_PASS
