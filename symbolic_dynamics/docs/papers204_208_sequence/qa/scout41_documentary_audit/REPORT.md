# Scout41 independent documentary audit

2026-09-07 UTC. Auditor: `/root/scout41_documentary_desk`, assigned by root.
Result: `PASS_DOCUMENTARY_ONLY`. Target disposition remains
`NO_PROMOTION / HOLD_EXTERNAL`; this is not mathematical review, admission,
source novelty clearance, or completion of the five-paper batch.

## Exact target and verified counts

The sealed target is
`docs/papers204_208_sequence/scouting/finite_systems_forty_first/`.
Its directory-relative `SHA256SUMS` is exactly
`3d71f6f995f6b1b6f8cdd56c5e385613743c0b6be9bb752f0c1a454e9bd5053d`.
Independent enumeration found exactly 196 payloads, no missing/unlisted
payload, no repeated/escaping/self entry and no symlink. Every payload hash
matched, and an actual native `sha256sum -c SHA256SUMS` exited 0. Full
196-line output is [preserved](target_sha256sum_check.stdout.raw).

All 31 `commands/*/receipt.json` files, both input lists for each command,
and both complete raw streams for each command were checked. Before/after
maps agree, counts agree, all named input identities resolve to matching
bytes, every receipt stream digest matches, timestamps are ordered, and
exit codes have their original values. The 30 commands preceding
`08_documentary_audit` comprise exactly:

| Native program | Original command count |
|---|---:|
| `cp` | 1 |
| `sed` | 10 |
| `rg` | 6 |
| `curl` | 5 |
| `pdfinfo` | 4 |
| `pdftotext` | 4 |

Those 30 original before-input dictionaries contain exactly 199 pin
occurrences and 134 distinct `(original absolute path, SHA-256)` identities.
The historical outer auditor's 303 paths were independently reconstructed
as its 190 then-present local files plus the resolved historical input
union, deduplicated by actual path. This equals its complete recorded
303-path input map, not just its reported count. The later closure note,
five outer auditor command artifacts, and final manifest are not falsely
treated as original pre-execution inputs. Including the outer auditor,
all 31 native records contain 502 pin occurrences / 305 historical
path/hash identities. These are different accounting universes, not
contradictory totals.

The two exact aliases in `CONTROL_ROLES.json` were checked by original
path, copied path, role and independently specified digest:

- `SYMBOLIC_DYNAMICS_STATE.md` → target `controls/SYMBOLIC_DYNAMICS_STATE.md`,
  digest `736e3f648bc6dda583254dcc58f49fc764043c30ea464ec524fac04f2ec67265`.
- `docs/papers204_208_sequence/PIPELINE_STATE.md` → target
  `controls/PIPELINE_STATE.md`, digest
  `70de1375b0b55339408b7399178a17f91f3058b3f068faa7c395ab633e525b47`.

They are the explicitly disclosed post-navigation, pre-packaged-read
physical control copies. No historical input was silently substituted by
a live index. This audit additionally pins both current central indexes
and confirms their bytes unchanged through its own actual execution.

## Fresh documentary comparisons and original source records

This audit actually executed all ten archived `sed` argv lists. Each fresh
stdout and stderr was compared to its corresponding archived raw stream
by a separate native `cmp`, with all twenty comparator exits 0. In
particular, command 02 retains concatenated `1,70p` semantics; it is not
misdescribed as seventy lines of each control file.

The four successful primary PDF bodies were actually re-extracted using
`pdftotext -layout BODY -`. Each fresh stdout was compared by native `cmp`
to the stored `body.txt`, and each stderr to the original extraction's
empty stderr. All eight comparator exits were 0. Thus there are fourteen
fresh documentary producer calls and twenty-eight actual raw comparator
calls, with full individual stdout/stderr stored flat in this audit folder.
No historical helper or scientific producer was imported or executed.

For each acquired PDF, the original request URL, download argv and complete
HTTP summary, headers, body signature/size/hash, original `pdfinfo` page
count, extracted text and all command streams were checked. The original
page counts are 21 / 137 / 15 / 31 for Schüle / synchronism arXiv / Fukś /
Powley, and body sizes are 983421 / 2879210 / 200359 / 278199 bytes. These
are archived metadata, not new `pdfinfo` executions or visual inspections.

The real `synchronism_download` curl exit 35 remains unchanged. Its exact
stderr is `curl: (35) Recv failure: Connection reset by peer`, followed by
a newline; its `sources/synchronism/body.raw` is absent, and its request
and headers remain present. The separate successful arXiv fallback is
intact. This audit did not retry any network request or convert the failed
route into a body/source read.

The full saved 939-path filename inventory was parsed without rereading
the denied file bodies. An independent transcription of the documented
path/basename/depth exclusions reproduces all 111 selected paths and every
denial count. The full body-query argv equals that ordered selected list.
All 34 stored matching lines were located at their actual pinned
path/line/content positions. This is reconstruction from the archived
inventory and original pinned bodies, not a fresh filename or `rg` search.

All seven saved browser request/result batches were parsed: three initial
four-query searches, two later two-query searches, one open and one click.
Their precise requests, files and hashes are in the detail output. This
checks the archived objects and native source acquisition evidence, not
independent authentication of a remote browser session or a new literature
search. The source's own selected-read limits remain in effect.

## Inspected original paths and helper-code limits

The auditor read the full target `record.py`, `discover.py`, `primary.py`
and `audit.py`, plus `INTAKE.md`, `SCOUT_REPORT.md`, `CLOSURE.md`,
`SOURCE_AND_HISTORY.md`, `CONTROL_ROLES.json`, and the full original outer
auditor stdout/receipt and failed curl receipt/stderr. The original
command/source/input/output census and every resolved input path are in
[DETAIL.actual.json](DETAIL.actual.json), not an abbreviated chat table.
All sealed bytes, including `PROOF_PACKAGE.md`, are integrity-checked;
theorem correctness and source-context interpretation are reserved to
root's separately assigned inspection, not certified by this audit.

The original native recorder includes its own source and explicit inputs;
the original outer audit additionally pins the documentary helper code,
source outputs and historical input union. Its ten sed and four extraction
comparisons use Python byte equality after subprocess capture, not a
native `cmp`, and do not retain each inner output in a new standalone
file. This audit does not relabel those historical assertions as native
comparator receipts: it supplies its own fourteen fresh full stream pairs
and twenty-eight actual `cmp` receipts. Neither package supplies a strict
full linked-runtime capsule. This audit pins its resolved executable bytes
but does not certify scientific replay reuse or infer such a claim from
command success.

The project `symbolic-dynamics-research` skill and its full workflow were
used for documentary evidence boundaries, historical preservation and
change-sensitive verification. AGENTS, current recovery/batch navigation,
batch scope and artifact-role contract were consulted. No mathematical
review skill, scientific code, manuscript build, renderer or image viewer
was invoked. No source/review/build body from P209 or another lane was
edited; root's active controls were held unchanged. The only writes are
new source/report files and actual execution outputs in this owned folder.

## Actual execution, preserved diagnostic, and handoff

The sole actual checker run was invoked from the workspace root by:

```text
/root/miniconda3/bin/python -B docs/papers204_208_sequence/qa/scout41_documentary_audit/capture.py run
```

It exited 0 with empty stderr. [Native receipt](receipt.actual.json)
records the child argv, invocation, cwd, epochs and stream digests. All
326 captured input paths are identical in [before](input_pins_before.json)
and [after](input_pins_after.json). The complete parent
[stdout](audit.stdout.raw) and [stderr](audit.stderr.raw), full child
commands/streams in `DETAIL.actual.json`, and [checker](check.py) /
[recorder](capture.py) are the evidence. The tool display of the completed
large stdout was truncated; the complete stored stdout and structured
detail, not that display, support this report.

Before that run, a diagnostic `ls /usr/bin/rg ... && ...capture.py run`
exited 2 because `rg` is supplied on Codex's PATH rather than `/usr/bin`.
The short-circuit prevented checker execution. The exact native combined
output is preserved in [PREFLIGHT_FAILURE.json](PREFLIGHT_FAILURE.json)
with its transcription provenance and the absence of separately captured
streams disclosed. PATH resolution was corrected before the sole real
checker run; no failed checker/scientific execution is invented or erased.

The nonself audit `SHA256SUMS` is generated after this report. Its final
native check and digest are returned to root without appending an unlisted
post-seal artifact. The sealed Scout41 target is unchanged. No child lane,
central index update, Git operation, paper number, old-hold reopening,
public upload or specialist contact occurred. Root alone decides central
documentary integration; `NO_PROMOTION / HOLD_EXTERNAL` is unchanged.
