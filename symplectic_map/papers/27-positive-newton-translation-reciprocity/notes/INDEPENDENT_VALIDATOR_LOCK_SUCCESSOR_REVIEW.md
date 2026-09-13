# Independent Paper 27 successor corrected validator-lock review

review_status: PASS
controlling_event: B07-E0271-P27-SUCCESSOR-CORRECTED-VALIDATOR-LOCK-AUTHOR-STOP-AND-SECOND-FRESH-REVIEW-AUTHORIZATION
review_role: second-wholly-fresh-independent-paper27-successor-validator-lock-reviewer
external_effect: none

## 1. Independence, firewall, and method

I had no earlier Batch 07 author, reviewer, builder, recovery, audit,
candidate, project, disposition, coordination, manifest, source, profile,
dependency, validator, terminal-integrity, E0269-review, or E0270-correction
role.  I did not delegate and did not use author, failed-reviewer, or
corrective-auditor reasoning as proof.  The earlier review artifacts were
treated only as frozen inputs whose identities and stated boundaries had to
be rederived against the source.

I opened only the eleven E0271 review paths and performed an exact absence
check on the one authorized review-create path.  I used fixed no-bytecode
Python only for no-follow stat/byte/text/hash checks, `ast.parse`, and static
AST/literal extraction.  I did not import, compile, execute, simulate, or
invoke the validator.  I did not list or search the workspace, enumerate a
parent, follow a pathname symlink, probe a build/evidence/system/dependency
candidate, run a compiler, BibTeX, a PDF tool, CAS or scientific code, use the
network, or create a temporary or bytecode file.  No source, lock, status,
build, evidence, or other path was written.

The review was source-first.  I independently reconstructed constants and
maps from the AST, followed every call and data lifetime through the source,
and then tested every lock statement against that reconstruction and the
profile.  Closure prose and author/auditor censuses were not accepted as
proof.

## 2. Opening and closing identities

The review path was absent at opening and remained absent through the final
pre-write close check.  Every opened path was a stable strict-UTF-8 regular
file with BOM=0, CR=0, NUL=0, exactly one terminal LF, mode 0644, and link
count one.  The exact tuple in each row is both its independently observed
opening identity and its final pre-write closing identity; no reviewed byte
drifted.

| Exact path | Opening and closing bytes/LF/SHA-256 | Exact terminal line |
|---|---|---|
| `BATCH_07_STATUS.md` | `1168908 / 15872 / 5ff0a3ffd195f8c4509cf41363c12974b40c4ef98bb3e67db887d1a39b78ccbb` | `BATCH07_P27_SUCCESSOR_CORRECTED_VALIDATOR_LOCK_SECOND_FRESH_REVIEW_AUTHORIZED` |
| `notes/BUILD_PROFILE_SUCCESSOR.md` | `45627 / 816 / 2e608faaa05e3063352c193869b92d5a305cc3de956ad18624d457b303787bec` | `BATCH07_P27_BUILD_PROFILE_SUCCESSOR_AUTHOR_STOP` |
| `notes/DEPENDENCY_LOCK_SUCCESSOR.md` | `30145 / 215 / 66c96cc6b40658370cc129e3bf828bcd08a7e69f7f2462ebea084cc77ce6ed17` | `BATCH07_P27_DEPENDENCY_LOCK_SUCCESSOR_AUTHOR_STOP` |
| `notes/INDEPENDENT_DEPENDENCY_LOCK_SUCCESSOR_REVIEW.md` | `12687 / 231 / b37e361c1cb8e7340c7a2e4af5b207de40df935ced707043c63c1e0f7017df35` | `BATCH07_P27_DEPENDENCY_LOCK_SUCCESSOR_REVIEW_PASS` |
| `notes/INDEPENDENT_BUILD_PROFILE_SUCCESSOR_SYMLINK_POLICY_REVISION_REVIEW.md` | `19942 / 353 / d8f8c82c722d00dcf419e6878cbcda3b3f784ed734ebb91dc33502271ceb2893` | `BATCH07_P27_BUILD_PROFILE_SUCCESSOR_SYMLINK_POLICY_REVISION_REVIEW_PASS` |
| `notes/INDEPENDENT_STATIC_SOURCE_SUCCESSOR_REVIEW.md` | `31760 / 704 / 7745af4b80e4e5ff35134e9279b7d2493f9b063bac0110bab115199bae3114ae` | `BATCH07_P27_STATIC_SOURCE_SUCCESSOR_REVIEW_PASS` |
| `paper/main.tex` | `55063 / 1681 / d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e` | `\end{document}` |
| `paper/math_commands.tex` | `601 / 17 / 34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` | `\newcommand{\PairGaps}{\mathsf{PairGaps}_{e}}` |
| `paper/references.bib` | `6610 / 217 / a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` | `}` |
| `notes/BUILD_VALIDATOR_SUCCESSOR.py` | `398248 / 9360 / 27c8f1e6535602f3cdc734eb8bf89ad28889493532d9628c31d9d95e78faffc1` | `# BATCH07_P27_BUILD_VALIDATOR_SUCCESSOR_AUTHOR_STOP` |
| `notes/VALIDATOR_LOCK_SUCCESSOR.md` | `57684 / 1061 / c770bdba165b60953253c50b0050537b00ea2c4bbd7322140cb372f319f37d65` | `BATCH07_P27_VALIDATOR_LOCK_SUCCESSOR_AUTHOR_STOP` |

The validator-lock machine frame occurs once, has its begin/end markers once,
and gives exactly `398248` bytes, `9360` LF, mode `0644`, nlink `1`, source
SHA-256 `27c8f1e6535602f3cdc734eb8bf89ad28889493532d9628c31d9d95e78faffc1`,
and the exact validator terminal above.  It equals the independently rebound
source identity.

## 3. Static source and path derivation

`ast.parse` succeeded.  I counted 267 top-level functions, ten nested helpers,
277 functions total, two exception classes, and nine lambdas.  The only
imports, in order, are `fcntl`, `hashlib`, `math`, `os`, `re`, `resource`,
`stat`, `sys`, and `zlib`; there is no `ImportFrom`, dynamic import, built-in
`eval`, `exec`, or `compile`, subprocess, shell, network, glob, recursive walk,
realpath/resolve, clock, randomness, or filesystem deletion, rename,
replacement, truncation, or cleanup call.

The literal path derivation closes exactly on project `P`, build parent,
evidence root `E`, roots `R0/R1`, stages `S0/S1`, cross stage `X`, the five
controls, the three source paths, the validator source/lock/copy, ten regular
tools, four tool symlinks, and the embedded dependency universe.  Every
ordinary leaf operation is under a held no-follow component chain or the
shared-prefix identity pool.  The only direct proc endpoints are
`/proc/self/fd` and `/proc/self/exe`.  Enumerated ordinary-directory names are
never converted into paths.

There is one bounded `os.scandir(fd)` artifact-census site and one two-pass
`os.listdir(scan_fd)` proc-FD site.  Ordinary census rewinds the exact held
descriptor, consumes only `DirEntry.name`, rejects a name over 255 bytes,
unknown name, or duplicate immediately, and closes on the finite exact set.
The proc census rewinds before both passes, admits only canonical decimal
descriptor names at most ten digits and at most 2147483647, ignores entries
that are no longer live, and requires the same exact live allowlist twice.
The soft `RLIMIT_NOFILE` is finite and in `[1024,4096]`.

The base mode-wide identity plan independently expands to 12 regulars, one
symlink, and 12 prefix-directory descriptors: 25 descriptors.  `ABSENT` and
`REPLAY` expand to 107 distinct regulars, six symlinks, and 68 prefix
directories: 181 descriptors, below the static 512 ceiling.  Held bytes,
stat keys, symlink raw targets/canonical hops, prefixes, and pathname bindings
are rechecked at all hold checkpoints.

The dependency literal is byte-for-byte equal to the dependency-lock row
stream: 23,408 bytes, 87 LF, SHA-256
`2855b5fe4a859552fc581eb3c06b11c68008b8eb67351d37f2a44c57a91adf87`.
It has 87 unique logical rows, 85 zero-hop regular rows, two exact one-hop
symlink rows, and 86 distinct regular finals.  The shared final and both raw
symlink targets/canonical hops agree with the lock.  Every final is exact-size,
mode-0644, link-one, chunk-hashed through a held FD, EOF-probed, re-read, and
pathname-rebound; no dependency candidate was probed during this review.

The source trio independently yields the exact title, eight ordered sections,
five theorem clauses, six ordered module anchors, six fixture IDs, seven
boundary rows, and unique conclusion anchor used by the validator.  The main
source has 20 citation occurrences with 20 distinct keys; the bibliography
has 20 distinct entries; both sets equal the exact expected-key tuple.

## 4. Modes, argv, receipts, writes, and universes

`MODE_ARITY`, `MODE_HANDLERS`, and `VALIDATOR_RESULT_FIELDS` have the same
exact 15 keys.  Static expansion gives this complete 74-row argv census:

| Mode | Arity | Rows |
|---|---:|---:|
| ABSENT | 2 | 2 |
| REPLAY | 2 | 16 |
| SNAPSHOT | 4 | 22 |
| MANIFEST | 3 | 10 |
| RECORDER | 3 | 6 |
| R033LIVE | 3 | 2 |
| BIB | 5 | 2 |
| LOGBIB | 7 | 2 |
| PDFINFO | 3 | 2 |
| PDFTEXT | 3 | 2 |
| PDFRAW | 2 | 2 |
| SOURCEFINAL | 1 | 2 |
| CROSS | 1 | 1 |
| STAGEINV | 2 | 2 |
| EVIDENCE | 2 | 1 |

The two root/stage pairs, eight replay checkpoints per root, 11 snapshot and
five manifest destinations per root, three recorder snapshots per root, all
root-local final arguments, and the literal cross/stage/evidence rows agree
exactly with the lock.  No unlisted alias, relative path, basename, argument,
or destination reaches a mode handler.

The 50 pre-inventory root-stage IDs and 51-ID timeline independently match.
The 36-entry validator-receipt map is exactly the 35 pre-inventory validator
IDs plus `I066`; the 27 second-field bindings are the eight replay, eleven
snapshot, five manifest, and three recorder IDs.  Static reconstruction of
the sorted exact-name frames gives:

| Frame | Names | Bytes | SHA-256 |
|---|---:|---:|---|
| root stage pre-I066 | 166 | 2188 | `978bc704ad9d6aa48dedccc799d540c5266902c48c5dde89f41579a92d7b158a` |
| root stage with empty I066 streams | 168 | 2212 | `3b8e6e3c8967800e227ee9894250c9938e81739074997bfb857d59efd4a30225` |
| root stage post-I066 | 169 | 2224 | `ff59cd1d01a709db334b2c631509cd781315e1538ee210ed4b00f217c8682c87` |
| final evidence root | 16 | 190 | `fdf7265843cb9d94f1d40636fa7d97fcdd9ed7813f2f0addd0675cd64c452cc3` |
| root-0 ABSENT evidence | 8 | 104 | `fcfb786df5f7515f180712ab94df53b53528c980b7ecaaad75df8e554ef15231` |
| root-1 ABSENT evidence | 12 | 143 | `c1233539586dab7650ecc67a650f58a8b727be4d943af64474b71295f37861c8` |
| X001--X008 complete | 24 | 288 | `f7955686bbf2ec63609cb2f62ff3232c8d1124eeedced5c9ccc3dac16b409dae` |
| X009 empty in-flight | 26 | 312 | `c2336c6ccdee97ad87e6e900d78cea7c13c44dda2e2af010e19d26736e938db1` |
| X009 complete | 27 | 324 | `5a555210ef205d8abe3802f360d1a8ab3bdeeaf409e8a20fa5b1d1e467d9c7a9` |
| X010 empty in-flight | 29 | 348 | `030998e8dedc74d1707d23265d532c639ca42eae31e03fe03d32e811cb7b7902` |
| X010 complete | 30 | 360 | `b4eb3603cba6c9260db671175c0c549a25dfd8fde928f1d40f4da32ca629ae64` |

The only filesystem payload writer is `_exclusive_write`, reached only by
the exact snapshot and manifest maps.  It anchors the selected stage and
literal basename, requires absence, and uses
`O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC`, mode 0600, bounded chunks,
file `fsync`, stat rebinding, close/reopen, full reread, and exact comparison.
It has no rename, overwrite, retry, cleanup, or parent-directory-fsync claim.
The only other `os.write` site is the short-write-safe FD-1 result loop.

The receipt guard binds precreated distinct empty mode-0600 link-one stdout
and stderr leaves to write-only, non-append, offset-zero FDs 1 and 2, holds
read FDs and the stage chain, keeps status absent, and checks exact names,
bytes, offsets, stat identities, and created payload state around emission and
at close.  Pre/post-handler holds cover previous manifests, recorder/BIB
snapshots, every R060/R062 companion triplet required by LOGBIB/PDF modes,
R054, and each newly created payload.  Root, stage, evidence, cross, absence,
and identity holds survive terminal recomputation, emission, receipt-final,
and final hold checks.

The universe reconstruction confirms the E0268 corrections: every RECORDER
holds its phase-correct live root; every REPLAY holds its live root and
phase-correct evidence set; root-1 ABSENT/REPLAY additionally holds completed
S0; PDFINFO, PDFTEXT, and PDFRAW keep all semantically read receipt leaves;
CROSS and EVIDENCE hold both final roots and both complete root stages; and
EVIDENCE holds the final evidence root and pre-X010 cross universe.  No
directory entry discovered at runtime selects a path.

## 5. Complete resource mapping

All KiB/MiB values below are binary and inclusive.  The exact direct build-root
caps are `main.tex=256 KiB`, `math_commands.tex=64 KiB`,
`references.bib=256 KiB`, `main.log=8 MiB`, `main.aux=4 MiB`,
`main.fls=8 MiB`, `main.pdf=64 MiB`, `main.bbl=2 MiB`, and
`main.blg=512 KiB`.

The complete stage/evidence role mapping is:

- every admitted status is 2 bytes and every stderr is 0 bytes;
- R009/R024/R033/R044/R054 manifests are 256 KiB;
- R021/R041/R051 log snapshots are 8 MiB, R022/R042/R052 AUX snapshots
  4 MiB, R023/R043/R053 recorder snapshots 8 MiB, R031 BBL snapshot
  2 MiB, and R032 BLG snapshot 512 KiB;
- stdout is 0 for R000--R008, X001--X008, and E001/E010/E011/E012;
- stdout is 4 MiB for R020/R030/R040/R050, 64 KiB for R060, and 8 MiB
  for R062;
- stdout is 1 MiB for X009/X010 and the complete validator set
  `A000 R009 V020P V020Q R021 R022 R023 C023 R024 V030P V030Q R031`
  `R032 B032 L033 R033 V040P V040Q R041 R042 R043 C043 R044 V050P`
  `V050Q R051 R052 R053 C053 R054 F055 F061 F063 F064 F065 I066`;
- the evidence validator copy is mode 0500 and capped at 1 MiB; every other
  direct evidence regular is mode 0600 and receives its exact receipt cap.

The four complete direct-regular aggregates and their exact scopes are:

| Container | Limit | Independently verified scope |
|---|---:|---|
| held R0 or R1 | 96 MiB | every direct regular after its root-role cap; five cache children skipped |
| held S0 or S1, or `_inventory_stage` | 128 MiB | completed S0 for root-1 ABSENT/REPLAY; both stages for CROSS/EVIDENCE; selected STAGEINV; each inventory including supplied in-flight streams |
| held X | 4 MiB | CROSS/X009 and EVIDENCE/X010 direct regulars |
| held E | 2 MiB | ABSENT, REPLAY, and EVIDENCE direct regulars; r0/r1/cross-root children skipped |

Each is a nonrecursive sum of actual direct-regular `st_size` values after the
individual role cap.  Mutable stdout/stderr must be empty when its universe
opens and therefore contribute zero then.  The same hold deliberately does
not recompute its aggregate after emission; later `_inventory_stage` includes
the completed receipt's actual bytes under 128 MiB.  Exact content, offset,
identity, name-set, and receipt checks continue across that interval.  The
corrected lock states this timing without claiming a recursive quota or a
post-emission aggregate recomputation that the source does not perform.

The pre-materialization text ceilings also agree: validator lock
`1 MiB/10000 LF/64 KiB`, validator source `1 MiB/100000 LF/64 KiB`, manifest
`256 KiB/1024 LF/16 KiB`, recorder `8 MiB/200000 LF/16 KiB`, AUX
`4 MiB/100000 LF/16 KiB`, BBL `2 MiB/50000 LF/16 KiB`, BLG
`512 KiB/1024 LF/4096 bytes`, log `8 MiB/200000 LF/4096 bytes`, and PDFTEXT
`8 MiB/200000 LF bytes/64 KiB per LF-delimited segment`.  AUX longtable and
BBL item subframes are each bounded to 4096 lines and 256 KiB, BBL items to
six `newblock` controls, and BLG to the closed 46-line schema.  The retained
pure-underfull warning set is at most 4096 lines and its LF-inclusive frame at
most 256 KiB before hexadecimal expansion.

PDFINFO timing was checked adversarially.  `_parse_pdfinfo` first applies the
64-KiB total-byte and terminal/framing constraints, then performs the bounded
LF split.  It enforces the 4096-byte physical-line limit while consuming that
list and closes on 18 required plus zero-to-four optional ordered unique
fields, hence exactly 18--22 lines.  The corrected lock accurately separates
this timing from roles whose physical-line/count preflight occurs before list
materialization; it does not repeat the former inaccurate timing claim.

## 6. Semantic, parser, cache, and terminal review

I traced all fifteen handlers, their terminal second pass, and their cached
receipt/result bindings.  ABSENT and REPLAY rebind controls, tools, all
dependencies, validator source/copy, sources/root copies, and exact root and
evidence state.  SNAPSHOT and MANIFEST alone create payloads and terminally
rebind source/destination or regenerated root/destination/transition.
RECORDER admits only its closed PWD/INPUT/OUTPUT grammar and the frozen
dependency union.  BIB/LOGBIB close the 20-key source/AUX/BBL/BLG order and
schema, exact final products, log sentinel/pages/bytes, rejected diagnostics,
and reversible warning frame.

PDFINFO closes the exact PDF 1.5 metadata/size/page/letter/rotation/date field
schema.  PDFTEXT closes form-feed/page census, strict UTF-8/control grammar,
reference page, nonblank proof pages, title/anonymous/abstract, eight ordered
headings, six ordered module anchors, five theorem clauses, six fixture IDs,
seven boundary rows, conclusion, 20 visible references, provenance/path
tokens, and email rejection.

PDFRAW is bounded by one 64-MiB PDF and an independently bounded structural
copy.  I rederived the unique direct-object/stream spans, generation-zero
object grammar, 100000-object bound, two distinct 2000000-token budgets,
4096-byte atoms/names, 64-KiB strings, depth 64, 256-KiB stream dictionary,
16/32-MiB object-stream limits, one current traditional-xref or XRef-stream
closure, startxref/EOF closure, reachability partition, acyclic exact page
tree, rational MediaBox/rotation, exact stream-role partition and inbound
multiplicities, and 16/64-MiB content-stream plus 2000000 content-token
budgets.  Actions, unclassified streams, inline images, forbidden raw/decoded
tokens, and hidden compressed-object variants fail closed.

The font closure is Type1 only: resource Font objects, descriptors,
FontName/BaseFont, and exactly one FontFile binding agree; each unique shared
stream is validated once.  Per-program, clear/eexec/tail bounds are
16 MiB/1 MiB/16 MiB/64 KiB as applicable.  PFB segment order/count/length and
PFA partitioning are exact.  PDF-wide Type1 budgets are 64 MiB decoded,
4000000 lexical tokens, 2000000 CharString tokens, 4000000 concrete steps,
and 4000000 abstract steps.  Each font has at most 512 Subrs, 4096 glyphs,
16 MiB Subr-plus-glyph bytes, a 24-value stack, depth 16, and 100000 concrete
steps per glyph; the local abstract fixpoint adds a 2000000-step and
4096-state cap.  Macro family/timing, closed PostScript names and dictionary
occupancy, dynamic-name/exec rejection, lenIV binary ownership, reachable
concrete Subrs, and unreachable existential stack-I/O contracts all match
the source and lock.

Stage inventory preflights every completed and supplied in-flight file under
its exact cap and the 128-MiB aggregate, caches bytes and identity rows once,
validates every receipt/snapshot/manifest/recorder/BIB/replay/source-final
binding, and then clears the bulk cache.  Only bounded R060/R062 data survives
into final semantic recomputation; those entries are consumed before the live
PDF read.  CROSS releases recorder/normalized and manifest pairs per
iteration and compares eight raw products, three normalized recorders, five
manifest projections, both full semantic summaries, final roots/R054, and all
eight cmp receipts initially and terminally.  EVIDENCE serializes its bounded
stage inventories while retaining only its separately bounded evidence and
cross caches and repeats initial, terminal, and ultimate bindings.

Before encoding PASS, SNAPSHOT and MANIFEST use their special nonwriting
terminal recomputation and every other mode reruns its complete handler; the
second detail must equal the first.  The exact single-line ordered result
parser then closes every field.  PASS is fsynced, followed by runtime,
validator/source/copy/lock/control, ABSENT/REPLAY tool/dependency, universe,
identity, receipt, and hold checks.  Success alone returns 0.  Predicate
failure returns 1; usage/internal failure returns 2.  A guarded pre-PASS FAIL,
an unguarded early write attempt, a guard-open failure, partial write, or a
post-emission failure has exactly the nonzero/possibly partial semantics stated
by the lock.  Acceptance is exit/status zero plus exact stdout plus empty
stderr and all receipt bindings, never PASS text alone.

## 7. E0267 boundary triad and non-weakening result

The corrected lock now states all three mandatory boundaries exactly and as
additional premises:

1. The externally sealed launcher/build capsule, not the Python program, is
   the trust root for process creation, the loader, already-loaded standard
   library/shared objects, and the pre-main interpreter/source/copy/lock
   namespace.  Source import and runtime checks make no pre-main
   self-authentication claim.
2. The capsule supplies one immutable no-concurrent-writer namespace over the
   validator, lock, controls, source trio, tools, dependency targets, and
   governed parents across process creation and every separate compiler,
   BibTeX, PDF-tool, and validator interval.  Validator holds prove only the
   state admitted from `main` onward within one invocation and do not claim
   cross-process continuity.
3. PDFRAW proves bounded closed PDF/Type1 structure and name consistency, and
   CROSS proves two-root raw and semantic equality, but neither compares an
   embedded FontFile or glyph outline with a frozen dependency PFB.  That
   provenance remains an external obligation supplied by the frozen
   dependency capsule, deterministic two-root build, and continuity premise.

The source identity is unchanged from the E0269 freeze.  I found no current
source predicate removed, bypassed, contradicted, or replaced by any external
premise.  The corrected lock preserves the original modes, argv rows, path and
write restrictions, receipts, holds, semantic parsers, cache lifetimes,
terminal recomputation, and result/exit grammar while adding the triad, the
complete resource mapping, mutable-aggregate timing, and the accurate PDFINFO
timing qualification.  It makes no new self-authentication, cross-process, or
font-lineage overclaim.

## 8. Finding census and disposition

Blocker: 0
Major: 0
Minor: 0
Ambiguity: 0

review_disposition: PASS
review_pass_basis: independent exhaustive static source/lock/profile agreement on unchanged opening and closing identities
artifact_format: strict UTF-8; BOM=0; CR=0; NUL=0; LF-only; exactly one terminal LF; mode=0644; nlink=1

BATCH07_P27_VALIDATOR_LOCK_SUCCESSOR_REVIEW_PASS
