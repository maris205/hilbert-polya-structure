# C424--C428 tree and navigation preflight

2026-09-09 UTC. **PREFLIGHT_AND_ONE_DOCUMENT_DELTA_COMPLETE; NOT_A_SEAL.**
This is a coordinator-delegated read-only filesystem, path and navigation
preflight, not the final independent seal/member verification. It does
not certify mathematical correctness, final release membership, formal
evaluation acceptance, Git staging, synchronization or publication.

The only writes authorized for this task are this report and the later
explicitly authorized [historical navigation overlay](HISTORICAL_NAVIGATION.md).
No manuscript, old proof, source snapshot, review report, mathematical
program, release tool or Git object was changed. No mathematical or
LaTeX program, old release test, release inventory/check/seal/verify
action, project-code import, or archive extraction was run.

## 1. Actual snapshot and remaining gate

The main tree scan ran from **07:39:50.297613 to 07:39:50.559270 UTC**.
The delegated complete Markdown link refresh finished at **07:41:43 UTC**
and reproduced the same 227-Markdown-file snapshot. These are observations
of the then-current working tree, not a future sealed inventory.

| Observed item | Initial snapshot |
| --- | ---: |
| Regular files | 1149 |
| Descendant directories, excluding the batch root | 161 |
| Regular-file bytes | 81,894,992 |
| Markdown files | 227 |
| Git-tracked entries inside this batch | 0 |
| Git-ignored regular files, including all nested rules | 308 |
| Bytes in those ignored files | 15,587,485 |
| Regular files with executable bits | 0 |
| Files with zero bytes | 1 |
| Maximum single-file size | 463,423 bytes |
| Byte-content duplicate groups / member files | 191 / 642 |

The Git HEAD read was
`2895b07238d4cef2ed35faaad251e4cfceb08ec1`.
Only read-only Git discovery, ignore and attribute queries were used,
with optional locks disabled for the scripted Git calls. No index
write, commit, fetch, merge or push occurred.

At the initial scan the following did **not** exist:
`release/`, `PAYLOAD_LEDGER.json`, `MANIFEST.sha256`,
`REVIEW_ADJUDICATION.md`, root `FINAL_BUILD_REPORT.md`,
`EVALUATION_ADJUDICATION.md`, and
`continuation_round6/ROUND6_DECISION.md`. The coordinator was actively
preparing the root documents and release notes. Their absence was
**pending work, not evidence that they had already been completed**.
No parsed link in the initial existing Markdown pointed to one of
those absent coordinator outputs.

A later incidental read observed 1152 files and 230 Markdown files:
the coordinator had added three documents, including the review and
evaluation adjudications. That observation is not substituted for the
timestamped initial snapshot and not called a final delta. This report
and its navigation overlay also necessarily add members after the
initial count. The coordinator subsequently announced the six root/
decision documents ready; the single bounded delta is recorded in
Section 7. No initial or delta count is a final ledger count.

## 2. Path, type, empty-directory and alias checks

The unchanged fixed release implementation
[exact_payload.py](../../continuation_c414_c418_round2/release/exact_payload.py)
was read in full, not imported or executed. Its SHA-256 is
`529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f`.
Its relevant policy is:

- Lines 23 and 40--45 accept only nonempty slash-separated components
  matching ASCII `[A-Za-z0-9_.-]+`, excluding `.`, `..` and empty
  components.
- Lines 58--69 open the root and every ancestor without following links.
- Lines 75--126 inspect every member, including hidden and Git-ignored
  files; each non-directory must be regular and have link count one.
  The implementation uses no-follow opens and before/after metadata.
- Lines 133--138 reject empty or otherwise unrepresented directories.
- Its only root metadata names excluded from the payload entries are
  `PAYLOAD_LEDGER.json` and `MANIFEST.sha256`; metadata is bounded at
  16 MiB. This is not permission to ignore arbitrary caches or logs.

The independent preflight walk inspected the actual paths with
`lstat`, did not descend through links, and hashed ordinary files with
no-follow/nonblocking opens and before/after size/inode/mode/link/
timestamp checks. It did not call that release implementation.

| Check | Initial result |
| --- | --- |
| Unsafe or non-ASCII path component | 0 |
| Symlink member or symlink ancestor of the batch root | 0 |
| Special file: socket, device, FIFO or other nonregular member | 0 |
| Regular file with hard-link count other than one | 0 |
| Empty descendant directory | 0 |
| Dot-prefixed hidden member | 0 |
| Case-folded path collision | 0 |
| File or visited-directory change detected during the scan | 0 |

All ancestors from the batch directory through `/` were actual
directories. The longest relative path was 110 bytes:
`papers/C428_integer_period_spectrum/builds/round1_revised/baseline_source/sections/05_symbolic_certificate.tex`.
The longest component was 37 bytes. Maximum file depth was seven
components. No portability remedy is required by these observations.

The one empty regular file is
`papers/C425_fricke_return/build_initial_01/main.out`, a preserved
first-build output. A zero-byte ordinary file is accepted by the fixed
policy; it is not an empty directory and is not a reason to delete or
rewrite the historical receipt.

The tree was still under coordinator development. The local scan's
no-change result is not a globally quiescent final release assertion;
all writer-stop, exact-ledger and final independent gates remain.

## 3. Ignored-member risk and the coordinator's explicit disposition

The actual ignore query used `git check-ignore --no-index -v -z --stdin`
on all discovered regular paths; it returned 308 entries without an
error. `git ls-files --stage` returned zero batch entries at the initial
scan. An ordinary non-forced add or an ignore-respecting file listing
would therefore omit real batch members.

| Effective ignore source and line | Pattern | Initial file count |
| --- | --- | ---: |
| Repository `.gitignore`:13 | `**/build/` | 96 |
| Repository `.gitignore`:19 | `**/*.log` | 51 |
| `henon_dynamics/.gitignore`:12 | `*.aux` | 27 |
| `henon_dynamics/.gitignore`:13 | `*.bbl` | 26 |
| `henon_dynamics/.gitignore`:14 | `*.blg` | 26 |
| `henon_dynamics/.gitignore`:15 | `*.fdb_latexmk` | 27 |
| `henon_dynamics/.gitignore`:16 | `*.fls` | 27 |
| `henon_dynamics/.gitignore`:17 | `*.out` | 27 |
| `henon_dynamics/.gitignore`:3 | `**/__pycache__/` | 1 |

These counts partition the reported effective matches; for example,
files below C424's `build/` can match its directory rule before a
more specific extension rule is relevant. Exact present examples include:

- `papers/C424_integer_valued_quadratic/build/final_frozen_01/main.pdf`
  and the entire two C424 final build directories, including
  `main.log` and `latexmk.console.log`.
- `papers/C428_integer_period_spectrum/builds/final_02/compile.log`
  and the other preserved compiler/BibTeX/dependency receipts.
- `continuation_round6/arithmetic/__pycache__/check_integer_periods.cpython-312.pyc`,
  6936 bytes, mode 0644, link count one, SHA-256
  `26d59b5833e6cda61d4cf768cbbbfe0818ba3b6fb2e6196d3c38f779b295fb87`.

After being informed of the cache, the coordinator explicitly decided
to **retain every actual historical member, including this existing
bytecode file**, and include ignored members in the final ledger and
exact stage. The coordinator identified it as an earlier execution
artifact, not a new mathematical run. This preflight only inspected
its metadata and bytes; it did not import, deserialize, regenerate,
execute or delete it. The provenance attribution in this paragraph is
the coordinator's disposition, not a newly reconstructed execution.

The remaining actionable integration requirement is to carry the
approved full filesystem set, including these ignored files, through
ledger generation, exact staging and Git-blob byte comparison. A bare
ignore-respecting add is insufficient. No ignore rules were changed,
and the requirement is not marked executed here. A whole-tree release
cannot silently exclude the retained cache or compiler outputs.

## 4. All initial Markdown navigation

The delegated read-only audit used the actual
`rg --files --hidden --no-ignore` Markdown members and installed
`markdown-it` CommonMark tokens. It excluded fenced, indented and
inline code. Supplemental raw scans found no reference-definition
links, HTML navigation, placeholder destinations, `.MD` or
`.markdown` variants requiring a separate pass.

| Initial navigation observation | Count |
| --- | ---: |
| Parsed local-link occurrences | 640 |
| Existing literal filesystem targets | 600 |
| Literal destination misses | 40 |
| Missing active README navigation | 0 |
| Absolute local Markdown destinations / `file://` destinations | 0 / 0 |
| HTML `href` or `src` destinations | 0 |
| Relative link occurrences outside the batch but inside this repository | 68 |
| Distinct targets of those repository-external-to-batch links | 55 |

The 40 literal misses are fully enumerated, with an actual working
target for every row, in [HISTORICAL_NAVIGATION.md](HISTORICAL_NAVIGATION.md):

- 36 are in the six byte-identical C424 scout/proof provenance copies.
  Their original base is `arithmetic_maps/`; the copied prose was
  intentionally not rewritten. The preflight author independently
  repeated the six direct byte comparisons before making the overlay.
- Two are `main.pdf` links in archived C426/C428 source-only
  `baseline_source/README.md` files. The overlay routes to each
  preserved initial handoff PDF, verified equal to its initial build,
  and clearly distinguishes it from the current final PDF.
- One is the paper-local byte-identical C428 second-review copy at
  line 17, with `../round1/C428_REVIEW.md` relative to its old base.
  The canonical first report exists under `manuscript_reviews/round1/`.
- One is `REVIEW_OUTLINE.md`:84, `BATCH_PLAN.md:150`.
  The plan exists. A literal CommonMark/GitHub navigation treats the
  suffix as filename text, whereas an IDE-style renderer may interpret
  a line number. The overlay gives a portable file link with the
  historical line reference in prose; it does not claim to have tested
  the user's actual renderer.

No old snapshot or copied report was repaired in place. The misses
remain real literal misses at their original locations, with a new
navigation overlay rather than a false claim that they now resolve.
No genuine missing current README entry was found in this initial pass.

The 68 links to 55 existing targets outside this batch all stayed inside
the repository. They include prior Hénon batches, source theorem
packages, registries/current state, skill instructions, and the
unchanged Route A evaluator. Their presence is legitimate repository
context but is **not a standalone-payload inclusion certificate**:
a batch-only archive needs its dependency scope stated and the
repository checkout available for those links.

Historical absolute paths found in commands and execution receipts
are provenance strings, not Markdown link destinations. Agent/task
names beginning `/root/` are also not filesystem navigation. No path
string was rewritten merely for being historical or host-specific.

Three fragment-bearing links were checked against the intended heading
text under ordinary GitHub-style slugging. No browser rendering or
universal anchor compatibility was tested. Network-link availability,
Markdown inside tar files, arbitrary path strings in code/prose, and
mathematical reasoning were outside the link audit.

## 5. Duplicate bytes, archives and size constraints

All initial regular files were streamed for SHA-256 and byte length.
There were 191 repeated-content groups containing 642 files: 451 copies
beyond one member per group, representing 32,105,877 repeated bytes.
This leaves 698 distinct size/SHA-256 content groups. These are content
identity statistics, not additional mathematical executions or newly
certified proof results.

The largest repeated PDF groups were:

| PDF content | Copies | Bytes per copy | Meaning |
| --- | ---: | ---: | --- |
| C424 accepted PDF | 8 | 463423 | Initial/final build outputs, no-change round aliases and preserved baseline |
| C428 accepted revised PDF | 6 | 389314 | Actual revision/final builds and reviewed aliases |
| C425 accepted revised PDF | 6 | 378223 | Actual revision/final builds and reviewed aliases |
| C427 accepted revised PDF | 6 | 346694 | Actual revision/final builds and reviewed aliases |
| C426 accepted revised PDF | 6 | 343725 | Actual revision/final builds and reviewed aliases |

The bulk of the tree is the paper directories: 80,157,522 bytes,
approximately 97.88% of the initial tree. Preserved PDFs total
21,585,875 bytes across 56 files; page PNGs total 49,717,488 bytes across
265 files. Duplicated page images, source copies and historical PDFs
are expected evidence of separate actual stages. Do not delete them
or replace them with symbolic/hard links for deduplication: that would
alter the evidence and violate the fixed link policy. No file was deleted.

A read-only tar-header pass inspected all 19 archives, totaling
1,280,000 archive bytes and 257 regular members with 932,334 unpacked
regular bytes. The headers contained only regular files and directory
entries; no duplicate member names, unsafe member path, symlink,
hard link or special entry was found. Nothing was extracted and no
archived code was executed. This supplemental container check does
not redefine the outer payload policy: each tar itself is an ordinary
payload file, and archived Markdown was not counted in the link scan.

The largest single file in the initial tree is the C424 PDF at
463,423 bytes, under 0.45 MiB. No file exceeds 50 MiB or 100 MiB.
Read-only `git check-attr filter` on the initial file set found no
active content filter or LFS assignment.

The configured remote is a GitHub repository. GitHub's current official
documentation, checked during this preflight, warns at files above
50 MiB and blocks regular-Git files above 100 MiB. None of these batch
files approaches those thresholds. See the
[GitHub file-size documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

GitHub also documents a 2 GiB single-push limit in its
[push-limit documentation](https://docs.github.com/en/get-started/using-git/troubleshooting-the-2-gb-push-limit).
The initial 78.10 MiB unpacked batch tree is not an actual Git pack
measurement. No claim is made about the eventual push size, unrelated
repository history, remote branch protection, quotas or successful
synchronization; those require the coordinator's actual integration.

## 6. Required follow-through, without enlarging this preflight

1. Preserve the forty original navigation exceptions and expose their
   working routes through the new overlay; do not rewrite frozen copies.
2. Preserve all actual historical members, including the existing pyc,
   and include the approved ignored members in exact ledger/stage work.
3. The six notified coordinator documents and this task's one delta
   are now complete as recorded below. The separate integration reviewer
   must still finish its authorized report before final writer stop.
4. Only after every writer has stopped, perform the separately authorized
   fixed-tool inventory/pinned-ledger/check/seal/verify procedure and the
   final independent member/byte/manifest audit. This preflight is none
   of those actions and does not award their PASS.
5. Integrate only the approved exact paths and verify the actual staged
   bytes and subsequent synchronization under the coordinator's authority.

No filesystem path/type defect or missing initial active README target
requires an in-place repair. The outstanding issues are transparent
historical routing, exact inclusion of ignored evidence, and not
mistaking an evolving preflight snapshot for a final sealed payload.

## 7. Coordinator-triggered final-document delta

The coordinator announced its six in-tree root/decision documents ready
and temporarily frozen. After the user's explicit continuation, the
preflight resumed from the completed initial scan and navigation work;
it did not restart mathematics, compilation or the original tree-hash
pass. Exactly one final-document delta ran from
**10:43:38.782064 to 10:43:38.925592 UTC** on 2026-09-09.

The six notified documents were actually read in full (602 lines in
total) and their local links parsed. This task's two then-written
reports were included in the same link check. All 125 parsed local
link occurrences in the eight selected files resolved to existing
targets. Every one of the forty working-route links in the historical
overlay is included in that count. No genuine missing new active
entry was found, and none of the old forty literal misses was rewritten.

| Notified coordinator document | Lines | Local-link occurrences | SHA-256 at delta |
| --- | ---: | ---: | --- |
| `README.md` | 174 | 31 | `3515a443dde50ef4a862414a4ace37069fe904f036e3abfa2268c9b18b854b12` |
| `REVIEW_ADJUDICATION.md` | 94 | 17 | `3411681c4efb21c1d72a1f26f76b47dd97ff1798a036e91402d793275dd9df05` |
| `FINAL_BUILD_REPORT.md` | 97 | 13 | `62a50a9cfe31473958d2874109caf8a7321eb6f9e29dec083803c6784f70ebdd` |
| `EVALUATION_ADJUDICATION.md` | 86 | 4 | `38903b42303ca9b4af83fe4e264a8c9cbc50193c010723685cbd3b8ac77d572f` |
| `release/README.md` | 79 | 2 | `f94d5db06709261f9a05a79c6f61ff465ba7d2b303e08cbbd9996fb078b646d5` |
| `continuation_round6/ROUND6_DECISION.md` | 72 | 8 | `04ba718e64c5fb0b02b4b12899ab822b08d7ba4eecd612cfe86974447657b8a8` |

The other two selected files contained 3 local links in this report
and 47 in the historical overlay; all resolved. These selected-file
counts do not relabel the initial 640 occurrences as a new complete
tree-wide link review. The six new/updated coordinator documents
properly distinguish final papers/builds from pending seal/sync and
preserve explicit historical-status boundaries. Their scientific and
registry integration is assigned to the separate integration reviewer,
not re-adjudicated by this filesystem/navigation preflight.

A metadata-only walk in that same delta observed **1156 regular files,
162 descendant directories and 81,957,831 regular-file bytes**. It
found no unsafe path, special/symlink member, multi-linked regular
file, empty directory, hidden member or case-folded collision. This
count includes the initial versions of the two preflight reports,
before writing this delta section; therefore it is deliberately not
the final byte total or final payload approval. No repeated-content
or mathematical-input hash pass was repeated for this delta.

`release/REVIEW_INTEGRATION.md` did **not** yet exist at the delta.
The coordinator identified its separate assigned reviewer as the
remaining authorized report writer. It is **PENDING_WRITER**, not
missing historical evidence, not an automatically excluded payload
member, and not already reviewed here. The eventual final inventory
must include it if it is present. Both root `PAYLOAD_LEDGER.json`
and `MANIFEST.sha256` were also absent; no seal/check/verify PASS was
claimed. No later appearance or revision is silently certified by
this receipt.

The coordinator reported a successful fetch and unchanged remote/HEAD;
this preflight did not repeat a remote operation or independently
re-attest that network result. All historical members, including the
existing ignored bytecode, retain the coordinator's preserve/include
disposition. No old report, snapshot, manuscript, mathematical input
or ignored member was modified by this task.

After the two reports are fully read back and hashed, this preflight
writer stops. The coordinator owns the remaining integration-review
closure, final writer stop, full exact inventory, externally pinned
ledger, actual seal/verify, independent membership audit and exact Git
integration. This completed preflight grants none of those later gates.
