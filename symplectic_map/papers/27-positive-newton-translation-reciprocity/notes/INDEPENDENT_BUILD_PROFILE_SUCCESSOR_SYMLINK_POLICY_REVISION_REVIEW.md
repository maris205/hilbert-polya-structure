# Independent Paper 27 successor build-profile symlink-policy revision review

review_disposition: PASS
finding_census: Blocker=0; Major=0; Minor=0; Ambiguity=0
reviewer_role: wholly fresh independent Paper27 successor build-profile symlink-policy revision reviewer
controlling_event: B07-E0256-P27-SUCCESSOR-BUILD-PROFILE-SYMLINK-POLICY-REVISION-STOP-AND-FRESH-REVIEW-AUTHORIZATION
reviewed_profile: notes/BUILD_PROFILE_SUCCESSOR.md
external_effect: none

## 1. Independence, authority, and read firewall

I performed this review as a wholly fresh reviewer with no earlier Batch07
role of any kind, including either earlier Paper27 successor build-profile
review role.  I did not delegate any part of the review and did not reuse
another reviewer's private reasoning.  The earlier profile PASS is treated
only as an immutable review of the old 44,036-byte profile and supplies no
acceptance conclusion for the revised bytes.

At the final pre-write recheck, `BATCH_07_STATUS.md` was a regular mode-0644,
link-one file with 1,019,776 bytes, 14,670 LF bytes, and SHA-256
`23e63c2b748f5ccb533305fc6e516c25e4920c79866d62917abc15545cb36278`.
Its first 1,010,967 bytes independently hashed to
`f8495160cbf49d765cf26f346ebe4ddfd8752196c99ca5c668030a15213d05f5`,
the exact E0256 parent binding.  Its physical EOF was the exact complete
line
`BATCH07_P27_SUCCESSOR_BUILD_PROFILE_SYMLINK_POLICY_REVISION_FRESH_REVIEW_AUTHORIZED`.

Every read was confined to E0256's exact `opening_paths`.  I did not list a
directory, expand a glob or wildcard, recurse, search the workspace, probe
an absent or future path, inspect an unnamed build/evidence/release/later-
paper path, or open any of the other 79 dependency candidates.  In
particular, neither canonical target learned from E0254 was opened,
`lstat`ed, `stat`ed, readlinked, resolved, or hashed in its returned-target
role.  I invoked no compiler, BibTeX, `kpsewhich`, PDF tool, formatter, CAS,
scientific program, network action, or external effect.  This report is the
sole write.

## 2. Frozen revised profile and exact source binding

The reviewed profile was directly rebound as a regular mode-0644, link-one,
strict-UTF-8 file with 45,627 bytes, 816 LF bytes, no BOM, CR, or NUL byte,
exactly one terminal LF, and SHA-256
`2e608faaa05e3063352c193869b92d5a305cc3de956ad18624d457b303787bec`.
Its unique complete terminal line is
`BATCH07_P27_BUILD_PROFILE_SUCCESSOR_AUTHOR_STOP`.  These facts exactly match
E0256's frozen post-revision identity.

The bound anonymous source trio was independently rebound:

| Path | Bytes | LF | Mode | Links | SHA-256 |
|---|---:|---:|---:|---:|---|
| `paper/main.tex` | 55,063 | 1,681 | 0644 | 1 | `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e` |
| `paper/math_commands.tex` | 601 | 17 | 0644 | 1 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6,610 | 217 | 0644 | 1 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |

All three are regular, link-one, strict-UTF-8/LF files with one terminal LF.
The controlling static-source review independently matched its declared
31,760-byte, 704-LF, mode-0644, link-one identity and SHA-256
`7745af4b80e4e5ff35134e9279b7d2493f9b063bac0110bab115199bae3114ae`,
with an all-zero census and terminal marker
`BATCH07_P27_STATIC_SOURCE_SUCCESSOR_REVIEW_PASS`.

Direct source checks confirmed the exact 11-point article class, eight
package declarations, sole `math_commands.tex` input, anonymous author,
empty date, exact title, eight ordered sections, `plain` style, and
`references` database.  `main.tex` has no `PairGaps` invocation.  Its unique
`\clearpage` and unique semantic reference sentinel are adjacent and
immediately precede the bibliography calls; only those calls and document
termination follow.  The five theorem-clause names, P1--P3 and Q1--Q3,
seven boundary-row names, and the exact conclusion anchor after ASCII-
whitespace collapse all occur before the sentinel.  The source and
bibliography contain the same exact twenty distinct citation keys.

## 3. Independent historical dependency derivation

I derived the historical dependency strings only from the two exact named
`main.fls` files.  Their direct identities were:

| Recorder | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `build/r0-rev1-20260830/main.fls` | 23,262 | 355 | `573ac913b7ffaadb0fb58d02dff8832664c82b54f45f996606c6136c1dfc20cd` |
| `build/r1-rev1-20260830/main.fls` | 23,262 | 355 | `46ede3c9acb4d81854a9c85734ac31d9d77bc7d9aeacdd546ec266633cc62353` |

Each recorder yielded exactly 86 distinct literal absolute external
`INPUT ` strings.  The two byte-sorted sets were identical; their
terminal-LF framing independently hashed to
`d3bb1680de85151d4d691378107320b67be4738f0fc4acb9cd151fa431e8e474`.
The profile block contains exactly 87 distinct lines in strict byte order.
Removing only the prospective literal
`/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst` string makes it
byte-identical to either 86-line derivation.  That prospective candidate was
not opened.

The two exact historical `main.blg` files were each 906 bytes, 46 LF bytes,
and SHA-256
`76792d7f67dc314358a53f43894e619c7da0a51af611ecb3e7ba161b38ee2f92`.
Each contains exactly one `The style file: plain.bst` fact and exactly one
`Database file #1: references.bib` fact.  I used those as basename/database
facts only, not as existence or absolute-path evidence.

The old r0 and r1 source copies are identical 33,811-byte files.  Each old
source and the successor source have an identical 549-byte prefix before
the title command, with SHA-256
`ea61ad1f6c60bb78ee880a1cd0ebffc6b56e6712a9c8ab7fb5df4beeec0b1f52`.
Both old command files and both old bibliography files are byte-identical
to the successor counterparts.  The successor is ASCII-only, while the old
source exercised UTF-8.  The common class/package/theorem/layout prefix and
the historical recorder's roman, italic theorem/emphasis, bold furniture,
mathematical italic, calligraphic, blackboard-bold, symbol, and operator-
roman size closure cover every successor font demand without claiming a
candidate outside the frozen superset.

## 4. Literal proof of the revised symlink policy

I used only the two raw target rows physically printed in E0254.  The
literal calculation is:

| Logical symlink | Raw bytes | Raw hexadecimal | Strict-UTF-8 literal | Canonical hop |
|---|---:|---|---|---|
| `/usr/share/texmf/web2c/texmf.cnf` | 40 | `2e2e2f2e2e2f7465786c6976652f7465786d662d646973742f77656232632f7465786d662e636e66` | `../../texlive/texmf-dist/web2c/texmf.cnf` | `/usr/share/texlive/texmf-dist/web2c/texmf.cnf` |
| `/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map` | 15 | `7064667465785f646c31342e6d6170` | `pdftex_dl14.map` | `/var/lib/texmf/fonts/map/pdftex/updmap/pdftex_dl14.map` |

For the first row, the relative accumulator begins with the logical parent
components `usr`, `share`, `texmf`, `web2c`; the two literal `..` components
pop `web2c` and `texmf` exactly once each, after which the remaining
components append literally.  For the second row, the relative accumulator
begins with the seven logical-parent components through `updmap`, and the
single literal component appends.  Both results are strict descendants of
exactly one allowed root.  No filesystem fact was used in either
calculation.

The policy is byte-preserving and fail-closed.  It freezes raw bytes,
hexadecimal, strict-UTF-8 literal text, and the canonical hop together.  A
zero-length target, invalid UTF-8, NUL, CR, LF, or tab fails before target-
role access.  Absolute targets start from an empty accumulator; relative
targets start from the absolute logical parent.  Empty components and `.`
are ignored; every `..` pops exactly one accumulated component, and a pop
at the empty accumulator fails.  Emission is exactly one leading slash plus
single-slash-joined accumulated components.  Thus an empty final
accumulator, an allowed root itself, and any path outside all four roots
fail the strict-descendant test.  The four roots are pairwise nonoverlapping,
and all 87 predeclared logical strings independently match exactly one of
them.

This is a purely lexical byte/component operation.  It contains no
`realpath`, stat-follow, directory traversal, prefix discovery, existence
inference, or content read.  E0254's failure is preserved rather than
waived: after this review, a new event must restart logical-role observation
of all 87 candidates and may not reuse E0254 metadata as current lock
evidence.

The stage separation is complete.  The event that learns a raw target may
only freeze the raw target and canonical hop in a physical ledger STOP.  A
later event must make a fresh target-role no-follow `lstat`/`readlink` of the
exact canonical path.  Even if that canonical string is independently one
of the 87 logical strings, its same-stage logical-role observation supplies
no chain evidence and is not reused.  This directly covers the first E0254
target, whose identical logical string remained unopened here in its target
role.

Every canonical path is compared against the path sequence already present
in its own chain; a repetition, including return to the starting logical
path, is a cycle and fails.  At most eight symlink edges may be accepted;
encountering a ninth symlink or any dangling, directory, special, or wrong-
mode terminal fails closed.

The policy is compatible with hashing, the dependency-lock row, and later
rebinding.  Physical STOPs bind each raw edge label and canonical hop;
`chain-with-=>` binds the canonical path sequence; `target_path`, byte count,
mode, link count, and SHA-256 bind the final regular target.  Content hashing
is authorized only after every chain has terminated and a later ledger event
has predeclared every logical path, hop, and final target.  The reviewed
dependency table is then reproduced in the build's exact-path authority.
Before and after each publication command, every logical path and hop is
rebound without following and every terminal regular target is rehashed.
Read together with the mandatory exact raw-target freeze, “rebound” requires
the literal readlink edge as well as its canonical result; a validator that
accepted a different raw target merely because it canonicalized to the same
hop would violate this profile and fail its separate validator-lock review.
No chain evidence is supplied by path aliasing or by a prior logical-role
observation.

## 5. Direct no-follow tool and anchor identity audit

The fixed tool chains matched exactly:

- `/usr/bin/pdflatex` is a 6-byte mode-0777 link-one symlink with literal
  target `pdftex`; `/usr/bin/pdftex` is a 1,802,504-byte mode-0755 link-one
  regular target with SHA-256
  `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9`.
- `/usr/bin/bibtex` is a 24-byte mode-0777 link-one symlink to
  `/etc/alternatives/bibtex`, itself a 24-byte mode-0777 link-one symlink to
  `/usr/bin/bibtex.original`; that regular target is 117,128 bytes,
  mode 0755, link one, with SHA-256
  `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`.
- `/root/miniconda3/bin/python3` is a 10-byte mode-0777 link-one symlink with
  literal target `python3.12`; its declared regular target is 30,626,264
  bytes, mode 0755, link one, with SHA-256
  `9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101`.

All eight exact package anchors were regular mode-0644, link-one files with
the profile's exact bytes and SHA-256: `amsmath.sty` 87,648/
`027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83`,
`amssymb.sty` 13,829/
`70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986`,
`amsthm.sty` 12,594/
`8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626`,
`mathtools.sty` 59,397/
`e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7`,
`booktabs.sty` 6,078/
`3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc`,
`array.sty` 12,694/
`1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157`,
`longtable.sty` 12,892/
`196f2a7038e1727c4088a015bf11cac88abfedc5b7ee5eca65f44ab91dbac415`,
and `enumitem.sty` 51,697/
`a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3`.

The remaining fixed mode-0755, link-one administrative targets also matched
exactly: `/usr/bin/env` 43,976/
`85036540673319c6c2f54233fd2b9e45a8a71246b51cc96c4e6ab8ee6c419eb0`,
`/usr/bin/bash` 1,396,520/
`59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4`,
`/usr/bin/mkdir` 68,104/
`bd2f081ac37d653181332bd27f35a6041dbf215a7957f65838a9cbec9e64928b`,
`/usr/bin/install` 145,944/
`519a00d199d07da6028ec5a9800d92c562934582a2ea1793b2cbc378a85c1439`,
`/usr/bin/cmp` 43,408/
`b355472d3c90ea94d11ebb8b750e6946ccd348edc6fca4aefc1235c3994ef791`,
`/usr/bin/pdfinfo` 59,928/
`8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e`,
and `/usr/bin/pdftotext` 43,544/
`7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d`.
No executable above was invoked for its build/PDF function.

## 6. Environment, roots, receipts, manifests, and containment

The three inner environment tables are byte-sorted and have unique names:
11 rows for `PUBLICATION_ENV(<root>)`, four for `ADMIN_ENV`, and ten for
`VALIDATOR_ENV`.  Their payload partition is exhaustive and disjoint:
pdflatex/BibTeX use only publication environment; mkdir/install/cmp/pdfinfo/
pdftotext use only administrative environment; and the bound Python uses
only validator environment.  The outer `env -i`, startup-free Bash, and
inner `env -i` close inherited state.  Every displayed shell operation
other than the two fixed `env` launches is a Bash builtin, assignment,
control construct, or redirection, so there is no implicit fourth payload
class.

The profile reserves one exact evidence child and two fresh equal-length
certified-root names without probing them.  Root 1 is not probed or created
until root 0 has completed and its evidence inventory is bound.  Evidence
bootstrap has a physical-ledger receipt; every later stage/root creation,
initialization operation, validator, publication command, snapshot, and
manifest has distinct absent-before-use stdout/stderr/status receipts under
the already created evidence tree.  `set -C`, mode-0600 link-one receipt
requirements, exclusive snapshot creation, fixed literal paths, and
stop-on-missing/nonzero/unexpected-stream semantics prevent overwrite or
silent repair.

Each root has exactly nine initialization operations, five empty mode-0700
cache/config/tmp directories, and three exact mode-0644 source copies.  The
publication sequence is exactly TeX--BibTeX--TeX--TeX with IDs R020, R030,
R040, and R050, one execution each and no fifth pass.  The R021--R023,
R031--R032, R041--R043, and R051--R053 snapshots freeze every pre-overwrite
state required by the profile.  R009, R024, R033, R044, and R054 freeze the
opening and four post-command no-follow root manifests.  Failure stops
without retry, cleanup, root reuse, cross-root seeding, or deletion.

The final root universe is closed to the source trio, five empty
directories, and exactly `main.aux`, `main.bbl`, `main.blg`, `main.fls`,
`main.log`, and `main.pdf` as mode-0600, link-one regular files.  Every
other entry or object type fails.  Publication writes are root-local; the
evidence receipts/snapshots/manifests, exact parent metadata changes, ledger
appends, and sole later evidence record are the exhaustive administrative
exceptions.  Time-indexed recorder snapshots and after-command root
manifests, rather than only the final recorder, bind all four commands.

## 7. Acceptance, PDF, and cross-root determinism

The log/bibliography contract is conjunctive and fail-closed: one positive
reference sentinel; 24--28 proof-content pages; all and only the twenty
frozen citation keys in source, bibliography, aux, and bbl; the exact
style/database facts; resolved references/citations; zero overfull boxes;
rejection of every enumerated TeX, font, rerun, destination, and missing-file
class; and verbatim census and disposition of every residual warning or
underfull line.  Equality between roots cannot waive a root-local failure.

The PDF contract independently binds raw size and page count, version,
epoch dates, creator/producer, encryption and active-content flags, uniform
letter portrait pages, embedded non-Type3 fonts, successful strict-UTF-8
text extraction, title/anonymous/abstract visibility, all eight headings,
five clauses, six fixtures, seven boundary rows, conclusion, sentinel-
aligned reference start, and twenty visible reference labels.  Raw and
decoded provenance, identity, path, governance, and email firewalls are
explicit.  The checks are mechanical and conjunctive; no subjective visual
waiver is available.

Cross-root comparison requires raw identity of the source trio, PDF, aux,
bbl, blg, and log and sole-root-prefix-normalized identity of R023, R043,
and R053 recorder pairs.  The five raw root manifests remain immutable.
R009 compares raw; each later pair first requires identical non-recorder
bytes and identical non-hash fields for the sole `main.fls` row.  The
time-correct rebind is R024/R033 to R023, R044 to R043, and R054 to R053,
with the extra live-recorder equality check before R033 closing the BibTeX
interval.

Only after those raw checks does the in-memory projection replace the sole
64-lowercase-hex `main.fls` raw-SHA field by the hash of the corresponding
already rebound, exact-root-prefix-normalized recorder.  It creates no
projection file.  Therefore it accepts only selected-root-prefix recorder
variance: any other row byte, recorder byte, non-SHA field, stale recorder,
or identity difference survives an earlier check and fails.  No PDF/log/
manifest rewriting, sorting, deletion, or secondary normalization is
permitted.

## 8. Separate downstream gates and final findings

The profile review opens no build action by itself.  A new complete
dependency observation and lock must stop and receive a wholly fresh
all-zero review.  The exact validator source and validator lock are then a
separate bounded author gate and wholly fresh review.  Only a later build
authorization may bootstrap evidence and run the two ordered roots.  The
complete preserved evidence then receives a wholly fresh build review, and
release integrity remains separately authored and reviewed.  No gate may
reuse E0254 observations, an old profile PASS, later cross-root equality, or
an unreviewed validator as a substitute for its own evidence.

| Review class | Findings |
|---|---:|
| Authority, independence, frozen profile, and source/review binding | 0 |
| Historical 86-path derivation, 87-string list, BLG facts, and source comparability | 0 |
| Raw preservation, strict UTF-8/control checks, and lexical normalization | 0 |
| Absolute/relative accumulators, empty/dot handling, `..` pop, and root underflow | 0 |
| Four strict roots and zero filesystem resolution during canonicalization | 0 |
| Physical STOP, logical/target role separation, and fresh target-role observation | 0 |
| Cycle detection, eight-edge bound, chain hashing, lock rows, and rebinding | 0 |
| Tool chains, eight anchors, and administrative identities | 0 |
| Environments, roots, receipts, snapshots, raw manifests, and containment | 0 |
| Log, citations, sentinel, PDF, font, security, anonymity, and determinism | 0 |
| Dependency, validator, build-review, and release-gate separation | 0 |
| Prohibited read, write, execution, network, or external effect | 0 |
| Blocker | 0 |
| Major | 0 |
| Minor | 0 |
| Ambiguity | 0 |
| **Total** | **0** |

The all-zero census permits this single review artifact and no other write.
It grants no dependency-path, dependency-lock, validator, build, PDF,
release, cleanup, later-paper, network, submission, upload, messaging,
identity, or external-effect authority.

BATCH07_P27_BUILD_PROFILE_SUCCESSOR_SYMLINK_POLICY_REVISION_REVIEW_PASS
