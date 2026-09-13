# Independent Review of the R4 Retained Dual Build

Date: 2026-08-26

## Verdict and review authority

I performed a fresh, independent, zero-write-first retained-build review under
the parent gate `PAPER25_R4_RETAINED_BUILD_REVIEW_OPEN`.  I did not author or
review the manuscript or publication locks, design or execute any Paper 25
build, or participate in an earlier Paper 25 role.  I found zero blocker, zero
major issue, zero minor issue, and zero ambiguity.

The review was confined to the frozen Paper 25 project, the two governing
ledgers, installed frozen tools and TeX resources, and read-only operations on
the two exact R4 retained roots.  I ran no TeX or BibTeX command, performed no
continuation, retry, repair, rewrite, normalization, copy, chmod, rename,
cleanup, or deletion, and created no temporary file.  I did not access a Paper
23 or Paper 24 temporary root, any Paper 25 R0--R3 retained root, Paper 26, the
network, or a release or finalization surface.  The only write after all checks
passed is this review node.

## Opening universe and effective contract

The two opening ledgers were exact mode-0644, one-link, terminal-LF regular
files:

- `BATCH_06_STATUS.md`: 329,245 bytes, 4,630 LF, SHA-256
  `52a50618da8fe027c95098d6ce9cb46d42581fa36a41197f887be3a7b6b46085`;
- `BATCH_06_IDEA_REPORT.md`: 482,213 bytes, 8,769 LF, SHA-256
  `b71a5111e0bfdbe68724cd954346dbc7de2494b19204e7702a2a2098d4279490`.

Each ledger contains exactly one retained-build-review gate.  The future review
path was ENOENT and not a symlink.  The project was exactly L32: 32 regular
files, four subdirectories, zero symlinks, zero other nodes, 862,706 content
bytes, 10,820 LF, and 1,165 UTF-8 bytes across regular-file relative paths.  I
read and independently checked every L32 descriptor.  Every L30 descriptor,
the corrected R4 supplement, and its independent review matched type, mode,
link count, byte count, LF count, SHA-256, UTF-8 and terminal state.  The R4
review is 19,589 bytes / 123 LF / SHA-256
`ce730831c79c7eef86eb4f01c74754a8bd27056a65ee76331a4ff9701fdc78ec`
and has its unique required EOF terminal.

I parsed all five JSON files with duplicate-rejecting, float- and nonfinite-
rejecting logic and verified strict recursive canonical serialization.  A
newly parsed deep copy of the 69,835-byte base lock was replayed through the
exact R1, R2, corrected R3, and corrected R4 operation lists.  The effective
identities are respectively:

| Effective layer | Canonical bytes | SHA-256 |
|---|---:|---|
| R1 | 75,264 | `8c92a2469a415736de6658ebed4710a19b8f59cedfa1c4dbd60f9a3f9ca15aaa` |
| R2 | 81,582 | `341c9fdb89602befa7dc02c4185d68452e8e6e8d076f8324e6fe9a81dee54d98` |
| corrected R3 | 84,176 | `6b5265809ad32f8e3dabd9aa51f42ce76a9f9aa7f6635061b7d7aa3e64112d96` |
| corrected R4 | 94,439 | `5561c3506afb3a2495c07c6928beb64bc49a6c3cc8f1eba90ecaddefd9d6f86f` |

The corrected R4 supplement itself is 66,018 bytes / one LF / SHA-256
`7ddb5dd5a9428008672feb4b12698a67f2a0c9db9bf502328c19aa2c4c184e9e`.
All ten ordered R4 operations and value hashes match, including the exact
twelve-file inventory, the three raw-log snapshots, and the pass-scoped AX
exception.  The three frozen source identities remain 76,043 bytes /
`4d8ac648...60eea2`, 393 bytes / `c748e0cd...edf0`, and 3,450 bytes /
`159acd56...ad99d`.  I also reconstructed the prescribed L30 binary frame at
778,683 bytes / `a9fa9fffec8b138d2b16e4e1838faaf0913085620fba56b8873490f38c4c385e`.

All 13 command binaries, the frozen Python binary, and the installed
`fitz/__init__.py` matched their bound hashes and version fingerprints.  Under
the exact isolated TeX search map, all 19 direct class, package, style, and
engine resources resolved from system locations and matched their bound
hashes.  The canonical environment, pass-order, inspection-command,
source/input-audit, and system-resource hashes also match their inherited
bindings.

## Retained roots and independent staging

The two authorized retained roots are
`/var/tmp/paper25-r4-publication-build-A` and
`/var/tmp/paper25-r4-publication-build-B`.  Each is an actual mode-0700
directory; their device/inode pairs are `(149, 539527919)` and
`(149, 1089172155)`, so they are distinct.  Each contains exactly twelve ASCII-
named regular children, all mode 0644 and link count one, with no `main.out`,
subdirectory, symlink, or other node.  Each root totals 744,137 content bytes,
8,323 LF, and 141 filename bytes.  The complete opening metadata/content
manifest digests are `c1e1c7b1f2889997483632808ae375f956313d0e661792f13d24e9a64eed490b`
for A and `a6890bf39a65b9c3e9122d4c9dc41c5a233f7e54767a6e579834d6267fac8036`
for B.

Every child inode is distinct within a root and from every child inode in the
other root.  For each source basename, the project, A, and B copies have three
distinct device/inode pairs and identical bytes.  The project source device is
2431 while both build roots are on device 149; all six staged files have
ordinary allocated blocks, mode 0644, and link count one.  The builder's
disclosed `cp --reflink=never` staging therefore produced independent ordinary
copies to the full extent observable through read-only filesystem semantics.
The effective contract fixes the staging result but does not prescribe or
freeze a staging executable; its frozen command stack begins with the three
pdfLaTeX and one BibTeX passes plus the separately exact capture commands.
Thus use of `cp` for this bounded pre-pass staging is permitted and does not add
a build or inspection pass.

The current ledgers contain a contemporaneous execution receipt for the
ordered non-following A then B ENOENT probes, one-time mode-0700 creation, and
independent staging.  The final STATUS receipt slice beginning with the R4
builder return is 4,913 bytes / 69 LF / SHA-256
`573951b5397e73262e02b0b48ada9fbd5a2e4520bd9fdaf8edc57b2f52af2238`;
the corresponding IDEA section is 2,372 bytes / 36 LF / SHA-256
`20c34b4ed53900eeebfba86e61347998f4af59f72a5db954e1a264bc6703df52`.
Freshness is a historical event rather than a property that can be rerun on a
retained root.  The exact receipts, one-time root inodes, ordered file times,
complete inventory, and absence of any contradictory artifact jointly close
that obligation without pretending to repeat the probes.

## Raw snapshots and pass-policy reconstruction

The embedded capture program independently reproduces 1,507 ASCII bytes, 38
LF, terminal LF, and SHA-256
`b15f1871efe580e1d6ce93534ec6b4a8f105bd719266c1c5e3c58c1a2a453a99`.
It parses and compiles as Python and has exactly the declared `os`, `stat`, and
`sys` imports.  Its exact isolated argv, source `lstat` and no-follow open,
exclusive mode-0644 destination creation, link/inode/stability checks, complete
short-write-safe loop, size check, `fsync`, and closure paths all match the R4
contract.

All six retained snapshots are regular mode-0644, one-link files.  Snapshot
inodes are mutually distinct; corresponding A/B snapshots are byte-identical;
and each final live log is byte-identical to, but inode-distinct from, its
pass-three snapshot.  Full-byte parsing of every physical line, rather than a
grep census, gave:

| Pass | Bytes / LF / SHA-256 | Complete events in each root |
|---|---|---|
| 1 | 30,964 / 853 / `b2683be47075b21a82b1c35a3ce8cc94ddcb7bf96171bd5899f68f0bae53b761` | 49: 32 citations, 12 references, missing aux 1, missing bbl 1, plural summary 1, label rerun 1, references destination fallback 1 |
| 2 | 30,054 / 812 / `ef3dc2d5d25dc4baa3c9694530474d4de5c03f6f6635a73f4dbcc8581f3033ab` | 35: 32 citations, plural summary 1, label rerun 1, AX Underfull 1 |
| 3 | 27,442 / 694 / `c9aaf6015f517b9f67545be745afe0f605359f83004b409f73ac46968415e36c` | exactly the AX Underfull event |

Pass 1 contains eight citation and three reference joins at physical width 79
and the exact destination join at width 77.  Pass 2 contains the same eight
citation joins.  The canonical citation multiplicity vector is 192 bytes /
`2de243d572e002ed4df314f7c2dad7fabad1cbca44ab454826409edc395f508c`:
`AX`, `BT`, `BvS`, `DF`, `Des`, `HS`, `KL`, and `SS` occur three times;
the four standard-source keys occur 1, 2, 4, and 1 times in their declared
order.  Pass 2 has zero singular undefined references; pass 3 has zero other
warning, rerun, destination, citation, reference, box, error, or fatal event.

The snapshot and generated-file times have the strict order staged sources,
pass-one snapshot, BibTeX outputs, pass-two snapshot, final TeX outputs, then
pass-three snapshot in both roots.  Every snapshot contains exactly one TeX
banner, one `**main.tex`, and one PDF-output record.  The output progression is
26 pages / 443,789 bytes, 27 pages / 449,996 bytes, and 27 pages / 450,430
bytes.  Final `main.log` equals the pass-three snapshot, and the direct PDF and
log predate the exclusive pass-three capture.  Together with the persisted
capture-before-interpretation receipt, exclusive snapshot creation, and lack
of any post-capture log change, this excludes a continued or retried pass and
supports exactly the locked three-pdfLaTeX/one-BibTeX history.

## Bibliography, AX conjunction, and input closure

The two `main.aux` files are byte-identical at SHA-256
`40326fe603dc93aafb25fdb688021bbac7ac17dd484b11a3a5d36c30e1b7cc47`.
They contain 32 citations with the exact source vector, only `plain` as style,
only `references` as database, and exactly twelve `bibcite` records.  Each
`main.bbl` is 2,908 bytes / 79 LF / SHA-256
`a3d83191db0fc3c7f77656c685c215255140db72eea0746bf51e5696f8eb6fe0`
and has exactly those twelve items in the aux order.  Each `main.blg` is 902
bytes / 46 LF / SHA-256
`dff08b4e31e23bf58f0730012fcf4f6f1f004e6310ed2f3a0a7d7ab376632a61`,
records one BibTeX invocation, `main.aux`, `plain.bst`, `references.bib`, twelve
used entries, and `warning$ -- 0`, with no `Warning--`, error, or fatal text.

The exact AX project slice remains 181 bytes / six LF /
`359fcd6a061689e9c652641e4df10862818fc1a020a6e3d38e3f8c19b1e7b929`.
In the bound bbl, `\bibitem{AX}` is line 3 and is the unique nearest preceding
bibliography item for every reported paragraph line 4 through 7.  The exact
normalized header is the required 57-byte
`Underfull \hbox (badness 1215) in paragraph at lines 4--7`.  Header, bbl
identity, line ownership, source slice, pass, and count therefore satisfy the
conjunctive exception exactly.

The final FLS in each root is 61,357 bytes / 933 LF with 929 INPUT and three
OUTPUT records.  A's raw hash is
`a1ff0c185c02f824dcd17f2c539018c3410d21ab7e276ed3b192bfeb5489c769`;
B's is `66d918c4847cadc577aa00d5b53fd831dbc7c4c3071176624d081b822288b6ef`.
Replacing the sole exact PWD root prefix with `<R4_ROOT>` gives byte-identical
61,327-byte streams with SHA-256
`cc343f16ec4ff68f51507a335f0283182eb58e14ba0f05bd93653a7def30ba19`.
The only local inputs are `main.tex`, `math_commands.tex`, generated
`main.aux`, and generated `main.bbl`; the outputs are only `main.log`,
`main.aux`, and `main.pdf`.  There is no `main.out`, source bibliography,
snapshot, private, workspace, home, or network input.  The 162 unique absolute
inputs resolve to system-owned regular files, and all 18 direct TeX resources
expected in a pdfLaTeX pass occur.

Earlier FLS byte streams were normally overwritten by the next pdfLaTeX pass.
I therefore treat their builder-recorded boundary hashes as contemporaneous
receipts, not as retained bytes that I independently rehashed.  This does not
leave a contract gap: R4 requires retained raw-log snapshots, not FLS
snapshots.  The complete pass-one, pass-two, and pass-three log load traces
each contain the same 18 frozen direct resources, source imports, and no
private or snapshot path; source text admits no other import; pass-one records
the missing bbl; passes two and three load the generated bbl; BibTeX closure is
fixed by the blg; and final FLS closure is directly reproduced.  Snapshot
outputs could not have preexisted the exclusive captures, and their unchanged
times plus final FLS exclude TeX writes to them.  Thus every retained-state
input and snapshot-exclusion obligation is independently closed while the
nonretained boundary hashes are described no more strongly than their evidence
permits.

## Direct PDFs and locked inspections

Both direct pass-three PDFs are exactly 450,430 bytes and SHA-256
`0d071918dd6dc186681b651d71e0f008885a740739dc8a30346ab23d011acc73`.
The locked PDF comparison and all three locked snapshot comparisons return
zero.  I reran all fourteen per-root inspection commands with their exact argv
and applicable root as cwd.  Every command returned zero with empty stderr,
and corresponding stdout is byte-identical across A and B.  The ordered
stdout SHA-256 vector, serialized as compact JSON, hashes to
`8cff24309325a431b5366a55c0d0bb644d6de2ce3edc50ef9b9c5d669a65415f`.

Ghostscript accepts the file without structural error.  Both layout and raw
UTF-8 extraction preserve the full title, visible `Anonymous`, Theorem H,
mathematical symbols, accented names, all section text, citations, and twelve
references without replacement glyphs, unresolved markers, or private data.
Splitting the locked layout stream on form feeds gives exactly 27 pages.  Pages
1--26 are nonempty; page 1 contains Abstract front matter; page 26 contains the
numbered standalone `8.4 Conclusion`; and the first and only standalone
`References` heading is on page 27.

There are exactly 23 font records, all embedded, subset, ToUnicode-enabled,
and non-Type-3.  `pdfimages -list` has zero image rows.  PyMuPDF reports 27
unrotated, nonempty pages, zero attachment, zero non-link annotation, 44 named
internal links (32 citations and 12 internal structural references), and 49
public outline nodes: one exact-title root, eight sections, 39 subsections, and
References in exact source order.  There is no external URL, JavaScript,
launch/file action, encryption, incremental revision, raster image, or hidden
attachment.

PDF information and PyMuPDF metadata have the exact title and semantically
empty Author, Subject, Keywords, Creator, Producer, creation date, and
modification date fields.  The XMP packet hashes to
`ed7ee37653af1ffea14d94515cdae3c56ed4ee935dd9588bf17d890cb88b4a34`.
It has the exact Dublin Core title, empty Producer and Keywords, and no actual
CreateDate, ModifyDate, MetadataDate, DocumentID, InstanceID, UUID, local path,
machine identity, or governance datum.  Direct binary inspection finds one
header, one `startxref`, one terminal EOF, no trailer ID, date, encryption,
embedded-file, JavaScript, launch, remote-go-to, previous-revision, URI, or
private-path token.  The final FLS PDF output, final log's exact 450,430-byte
output record, pass-three snapshot equality, and file-time order establish
that this is the direct third-pdflatex output and was not rewritten.

## Adversarial review and disclosed assertion corrections

I reran negative in-memory checks for missing, duplicate, renamed, and extra
inventory members; `main.out`; wrong type, mode, or link count; dropped or
extra pass events; a changed citation vector or AX count; snapshot bytes added
to FLS; a one-byte PDF mutation; metadata identity/date injection; private-path
injection; and A/B mismatch.  Every hostile state was rejected.  Full source
inspection also confirms the exact class/package order, only
`glyphtounicode.tex` and `math_commands.tex` inputs, only the `plain` /
`references` bibliography pair, eight sections, 39 subsections, one table,
zero figure or appendix, 26 citation commands / 32 mentions / twelve keys,
nine labels / twelve reference uses, metadata suppression, no shell escape,
and no private source comment or `[VERIFY]` marker.

The builder disclosed three narrowed read-only assertion corrections.  Each is
sound and none masks output drift:

1. The AX owner is the nearest preceding item declaration on bbl line 3 for
   the reported paragraph lines 4--7; the contract says nearest preceding, not
   that the item declaration itself must lie in the reported range.
2. The page contract expressly accepts the public Conclusion heading in its
   numbered subsection form.  The corrected anchored check matches exactly
   `8.4 Conclusion` on page 26 and no false location.
3. A PDF's count of literal LF bytes is not a contract field.  The retained
   binaries happen to contain 2,718 LF bytes each, while their required byte
   count, SHA-256, direct-output provenance, structural validity, page count,
   and A/B identity all match.  Correcting a discarded LF assertion required
   no output operation.

Snapshot O_EXCL creation, distinct inodes, ordered mtimes, one TeX banner and
one output record per retained pass, final-log equality, final-PDF identity,
the exact root inventory, and the two frozen ledger receipts together show no
extra pass, retry, repair, cleanup, or root-byte mutation associated with
these assertion corrections.

## Closing stability and finding ledger

Immediately before this sole review-file creation, I repeated both ledger
identities and gate counts, every L32 descriptor and aggregate, review-path
absence, and both complete root metadata/content manifest digests.  They were
byte-for-byte identical to opening.  The retained roots remain evidence and
were not changed by any inspection.  This review authorizes no PDF copy,
finalization, release, submission, Paper 26 action, or later gate.

- Blockers: 0
- Major findings: 0
- Minor findings: 0
- Ambiguities: 0

PAPER25_R4_BUILD_REVIEW_PASS
