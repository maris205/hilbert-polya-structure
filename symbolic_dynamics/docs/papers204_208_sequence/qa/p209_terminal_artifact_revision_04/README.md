# P209 artifact infrastructure: revision04 preparation only

2026-09-07 UTC. `PASS_STATIC_PREPARATION_ONLY_NOT_ARTIFACT_GATE`.
Root still must inspect the actual original evidence, exact source diff and
static checks, then decide whether to run the prepared `initial_05` command.
No `initial_05`, lifecycle helper, verifier, build, render or page-view call
was executed by this preparation. No central index, original paper, review,
freeze, historical failure, Git path or external endpoint was changed.

## Two exact defects, separately disclosed

1. Actual `initial_04` failed at revision03 `audit_p209.py:937` with
   `KeyError: 'page_count'`. The original root view record instead has
   `measured_page_count: 4`. The new `root_page_views` function differs only
   in that exact key. Its original schema/status/reviewer, four ordered page
   entries, actual-view booleans, nonempty observations, PNG/PDF/seal hashes,
   diagnostic branch and external hold were checked against actual originals.
   No default field, synthetic attestation or weaker page-count check is used.
2. The new complete remaining-predicate check found four real semantic-origin
   conflicts in `pages_and_links`: A's response and root initial-inspection
   Markdown copies in both `delta_check_01` and `delta_check_02`. Round2's
   unchanged-file input aliases identify each copy with itself; they are not
   alternative document origins. The sealed A source/copy tables state the
   real origins. The added block recognizes exactly those four named roles,
   requires their exact source paths and hashes and the previous origin equal
   to the copy itself, then uses the table's original source. The original
   general origin-equality check remains intact. No generic bypass or digest
   search was added, and no original table was edited.

[EXACT_FOUR_A_ORIGIN_ROLES.json](EXACT_FOUR_A_ORIGIN_ROLES.json) records each
original path, copy path, digest, previous alias-derived origin, correct source
origin, original source/copy table and complete Round2 unchanged-file role.
The two unique digest values are `3b84c6c6…` for the A response and
`c095b736…` for the root initial-inspection Markdown. All 1,534 resolved
links across 219 original documents are identical with and without the named
origin correction; the correction prevents rejection of those four proven
roles and does not redirect any other link. All 779 frozen-link table rows
and their actual hash referents are retained in the documentary checks.

I authored revision03 and its preflight. That preflight missed this precise
view predicate despite its `REMAINING_SCHEMA_INSPECTION.md` report. Its
`inspect_originals.py` merely called `obj(P209_TERMINAL_ROOT_VIEWS.actual.json)`:
it recorded the object's shape, but did not evaluate the `page_count` lookup.
The same limited shape intake did not expose the four origin-equality
conflicts. The earlier report is preserved, not rewritten or presented as
successful predicate coverage. This work is source-familiar documentary
checking, not independent mathematical or manuscript review.

## Exact source delta

- Auditor: only `root_page_views`, `pages_and_links` and the appended fourth-
  failure preservation layer change; 32 functions remain byte-identical.
  The current PREPARATION path and returned revision label become revision04.
  All pre-existing statements before the old failure function's final return
  remain structurally identical. The added layer checks the sealed 47-payload
  revision03, the actual eight-payload `initial_04`, both executed source
  snapshots, full 16-input maps, actual exit 1, 652-byte original stderr,
  empty stdout and full root failure wrapper.
- Recorder: only `main` changes; its three helpers remain byte-identical.
  The exclusive future attempt is `initial_05`, with 19 required pins;
  every prior preparation/attempt/full root failure wrapper remains pinned.
- Lifecycle helper: only the top-level PREPARATION path changes. All 36
  functions and every lifecycle guard/body remain byte-identical. It is not run.

The three complete native diffs are `audit_p209.py.diff`,
`record_audit.py.diff` and `lifecycle_audit.py.diff`. `SOURCE_EDITS.json`
contains the exact replace-once recipe; `SOURCE_FUNCTION_CHECKS.json` and
`STATIC_RESULT.json` bind every changed/unchanged function and source hash.

Prepared sources:

| File | Bytes | SHA-256 |
|---|---:|---|
| audit_p209.py | 76,851 | `9fdb19017322689e7f222d4ad89f38d7e59364c52e94474314990a68775bfd31` |
| record_audit.py | 5,305 | `418b133fb4a89f6f6407843be6651978a7fc34a44538d30cf68c8b26a016798c` |
| lifecycle_audit.py | 33,703 | `bcd8c981f716cc1a6caa15bbe1aff4ecbe0e680777d39e7a7ab879773c756e23` |

## Actual documentary commands and preserved failures

Every `commands/<label>/` has its true native invocation, environment,
timing, child exit, full raw streams, entire before/after input maps and
actual executing helper/recorder snapshots. The new recorder writes an
ATTEMPT record before subprocess launch and the result only after completion.

| Command | Actual exit | Native inputs unchanged | Meaning |
|---|---:|---:|---|
| scope01 | 1 | 19 fixed discovery seeds | Found the four actual original origin conflicts; full discovery first-read/after map has 8,435 paths |
| inspect01 | 0 | 8,445 | Complete discovered input set pinned before launch; checked originals, exact four known conflicts and named correction; 19 fresh native copy comparisons |
| prepare01 | 0 | 8,475 | Created only exact new source copies and three complete native diffs |
| validate01 | 1 | 8,496 | New validator typo: compared `initial_01` with actual `initial_01/SHA256SUMS` strings; target sources were correct and unchanged |
| validate02 | 0 | 8,510 | Corrected exact literal set; 8,433 original paths rechecked, 19 new native copy comparisons and three full diff comparisons passed |

Both new failed commands and their executing code remain unchanged. The
validator retry writes separately named `static02_…` comparison outputs;
its earlier partial diff outputs are retained. `CODE_HISTORY_ROLES.json`
records only the two exact mutable-helper historical identities and their
own genuine command snapshots. No source/failure receipt is reconstructed
or overwritten. The discovery's first-read pins are not misrepresented as
pre-discovery input pins; the later inspection has a complete native
before/after scope.

The project research skill's change-sensitive verification and immutable-
failure requirements drove this exact original-data check and preservation.
`ORIGINAL_PREDICATE_INSPECTION.json` contains all original values, checks,
pin roles, views, links, final-flow inventory and source predicates.
`LIFECYCLE_INPUT_CONTRACT.json` makes the future boundary explicit:
current ROOT_LIFECYCLE remains pending and the 8,231-payload whole-paper
rollup is unchanged. Root acceptance JSON/report, a successful audit stdout
ledger, package rollup/report, pre-update preservation directory and final
QA do not yet exist. Their exact required scalars are requirements only,
not synthetic successful inputs. Future runtime/resource and lifecycle
predicates cannot yet be evaluated or claimed passed.

## Root-only next execution, not run here

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_04/record_audit.py initial_05
```

This path/command is offered only for root's independent inspection and
subsequent decision. The final local `SHA256SUMS` covers every nonself file,
including all new failures and actual command outputs. Its genuine final
native checksum result is returned in the handoff, not circularly written
inside the manifest it checks. A checksum or static preparation does not
complete P209 or the five-paper batch. `OWNER_AMBER / HOLD_EXTERNAL`.
