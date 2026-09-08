# C419–C423 research-checkpoint documentation and static-code audit

2026-09-07 UTC. This is a bounded checkpoint audit, not a manuscript
release, mathematical certification, formal evaluation or admission.

## Outcome

The checked local link paths, Python syntax/static compilation and JSON
syntax pass. No current fixed-input execution defect was identified by
the code reading. Three small documentation findings were reported and
then closed by a targeted reread of the coordinator's fixes at
**07:06:58 UTC**. The two invocation limitations below are not failures
of the recorded normal-mode mathematical runs.

This reviewer authored the CM arithmetic diagnostic and the AS2 principal
and parity proof notes. Review of those authored artifacts is **self-review**,
not a separate nonauthor mathematical review. The four other Python files
were read by a nonauthor. The pending assembled-AS2 theorem review remains
a different gate performed by a reviewer who did not coauthor that theorem.

## Actual scope, commands and time boundary

The repository was resolved as `/root/autodl-tmp/hilbert-polya-structure`.
Read the root and Hénon `AGENTS.md`, the current C419–C423 state prefix,
batch plan and admission decisions, and the relevant current/historical
AS2 status entries. All five new Python files were read completely,
607 lines in total. Markdown inspection used `rg --files`, targeted
`rg -n`, and `sed -n`/`nl -ba` reads; it was not a reread of every
mathematical proof or of every cited external source.

Exactly one bounded standard-library checker was launched from that
repository with **`python -B -`**, supplied as an inline stdin program.
It recursively enumerated existing `.md`, `.py` and `.json` files under
`henon_dynamics/research_c419_c423`, then:

- removed fenced code and inline code from explicit Markdown-link scanning;
  parsed balanced inline destinations and reference-definition/angle-link
  forms; URL-decoded local paths and checked their resolved existence;
- parsed every Python source with `ast.parse`, and called
  `compile(source, str(path), 'exec', dont_inherit=True, optimize=0)`;
- parsed the one JSON file with `json.loads`;
- recorded input sizes/hashes and compared the enumerated membership and
  size/mtime metadata before and after the check.

No compiled object was executed. No project module, diagnostic script or
SymPy code was imported. Installed SymPy version information was obtained
only through standard-library distribution metadata. No bytecode, checker
script, result JSON or other audit artifact was written by the program.

Actual run interval: **06:54:00.035609–06:54:00.108176 UTC** on
2026-09-07. Command exit: **0**. Environment:

- Python `3.12.3`, Anaconda build, GCC `11.2.0`;
- Linux `5.15.0-78-generic`, x86-64, glibc `2.35`;
- SymPy distribution metadata `1.14.0`; `sys.dont_write_bytecode=True`.

This was a live research tree. No member addition/removal or size/mtime
change was observed during the short checker interval, but that is not
an atomic filesystem snapshot, release seal, or guarantee against later
edits. The newly added `AS2_PROOF_INDEX.md` was already included. The
future `non_author_review/` outputs, final checkpoint README, and this
audit report did not exist in the enumerated input set and are not
pre-certified by these counts.

## Link and syntax results

| Check | Actual result |
|---|---:|
| Enumerated input files | 38 |
| Markdown files | 32 |
| Python files | 5 |
| JSON files | 1 |
| Local-link occurrences | 115 |
| Distinct resolved local targets | 62 |
| Local-link occurrences outside this checkpoint | 39 |
| Missing local paths | 0 |
| Malformed parsed destinations | 0 |
| Local fragment destinations | 0 |
| Excluded HTTPS-link occurrences | 113 |
| Other external schemes | 0 |
| Reference definitions found | 0 |
| Python AST and static compilation | 5/5 PASS |
| JSON syntax | 1/1 PASS |
| Changed/added/removed members during checker interval | 0/0/0 |

The 39 outside-checkpoint occurrences include links to immutable older
Hénon proof/manuscript dependencies and the existing evaluation authority.
Only their path existence was checked; no old payload was modified,
executed or re-sealed. Directory links were allowed as directory links.
The 113 HTTPS targets were deliberately **not fetched or validated**.
Bare path/URL literals and code examples are not counted as explicit
Markdown-link destinations. This is a path-existence audit, not a browser
rendering test, a full CommonMark parser certification, or a theorem audit
of linked content.

## Current status consistency

The coordinator's updated [admission decisions](../ADMISSION_DECISIONS.md),
[plan](../SCOUT_PLAN.md), [AS2 index](../arithmetic_spectral/AS2_PROOF_INDEX.md)
and the current-state prefix were read after their status update.
They consistently report **1/5 admitted contracts, zero new manuscripts,
no assigned paper numbers and no formal Route A evaluations**.

The positive-word classification is one admitted contract, not several
papers. The three scouting lanes recommend no additional admissions.
AS1's two real singularities are distinguished from the unclosed full
secondary circle, so AS1 has no slot. AS2 has a complete assembled author
proof under nonauthor review, not a recorded admission. The old five-paper
release described later in the global state is explicitly labelled the
historical C414–C418 batch, not completion of C419–C423.

No false five-paper completion, new evaluation, target-Euler/root-number
claim or automatic AS2 admission was found in these active status entries.
The superseded AS2 conjectures are retained as failed branches. The single
outdated follow-up paragraph identified below has now received a routing
correction; the frozen mathematical claim was not altered.

## Documentation findings sent to the coordinator — closed

These are prose/rendering fixes in new checkpoint files, not reasons to
rerun mathematical checks or touch an immutable predecessor.

1. **Stale follow-up status** —
   [AS2_CONJECTURE.md](../arithmetic_spectral/AS2_CONJECTURE.md),
   lines 42–44 at inspection: the first repair is still described as
   “under investigation” and “not yet proved”, although its linked file
   correctly marks its analytic claim false at level 100. Keep the
   original conjecture unchanged; update only this follow-up paragraph
   to route readers to the refuted first repair and the current
   parity-sensitive proof-under-review index.
2. **Extra Markdown table delimiters** —
   [nonlinear scout](../nonlinear_geometry/SCOUT_REPORT.md), line 20:
   the absolute-value notation for the bound on `k` contains two raw
   vertical bars within a table cell. Use `abs(k)<=4` or `\lvert k\rvert`
   there to prevent spurious cells.
3. **Extra Markdown table delimiters** —
   [mapping-class review](../mapping_class_review/REVIEW_PROOF_AND_INCREMENT.md),
   line 65: the absolute-value notation for `d` likewise uses two raw
   vertical bars inside a table cell. `\lvert d\rvert` preserves the
   mathematical statement without changing the table's column count.

These three findings were present before the initial report. The
coordinator subsequently changed only the affected prose, and the auditor
directly reread the three affected fragments at **07:06:58 UTC**:
the first repair is now explicitly refuted at level 100 and routes to
the current proof index; the nonlinear table uses `abs(k)<=4`; the
mapping-class table uses `\lvert d\rvert`. All three findings are closed.
The new proof-index link targets a file already present in the original
check. No code or mathematical input changed, and no global link/static
check or mathematical run was repeated. The auditor has not edited the
three owner files.

## Python reading and invocation limitations

| Script | Lines | AST asserts | Review role and static result |
|---|---:|---:|---|
| [CM diagnostic](../arithmetic/cm_density_diagnostic.py) | 103 | 2 | Author self-review; syntax PASS; fixed finite-field graph and elliptic-count convention diagnostic only |
| [Principal oldform probe](../arithmetic_spectral/AS2_oldform_probe.py) | 66 | 0 | Nonauthor code reading; syntax PASS; reports finite commutator support without asserting all-level validity |
| [Level-50 check](../arithmetic_spectral/independent_review/exact_check.py) | 88 | 5 | Nonauthor code reading; syntax PASS; exact bounded reconstruction and commutator assertions |
| [Nonlinear checks](../nonlinear_geometry/exact_checks.py) | 93 | 15 | Nonauthor code reading; syntax PASS; identities and explicit native witnesses only |
| [Positive-characteristic screen](../positive_characteristic/exact_screen.py) | 257 | 0 | Nonauthor code reading; syntax PASS; explicit `require` failures and bounded truncations/field domains |

Two nonblocking invocation limitations should remain visible:

- **Assertions require normal Python mode.** The level-50 and nonlinear
  scripts use `assert` for result verification and then print some fixed
  PASS fields. Running them with `-O` or nonzero `PYTHONOPTIMIZE` would
  remove those assertions. The CM script also has two domain assertions,
  although its substantive mismatch collection uses ordinary conditions.
  The documented runs are normal-mode runs, not optimized-mode claims;
  this static observation does not invalidate those recorded results.
  Do not treat an optimized invocation as equivalent. If these scripts
  later become reusable automation, explicit failures or an optimization
  guard would be appropriate in that separately scoped change.
- **CM exit status is not its verdict.** In the self-authored CM script,
  `run()` returns JSON status `FAIL` and a populated `failures` list on
  a detected mismatch, but the main block only prints that object and
  would normally exit 0. Consumers must inspect the JSON status and
  failures, not equate exit 0 with mathematical PASS. The recorded JSON
  was inspected and has `status=PASS` with an empty failure list; no
  contrary execution is asserted. The principal probe is likewise an
  output-producing falsifier, not a fail-on-counterexample CI runner.

The script loops, cutoffs and domains are finite and explicit. No network,
subprocess, file deletion, artifact overwrite or project-script import was
found in their source. No standalone dependency installation or claim to
test behavior under another SymPy version was made.

Checked Python SHA256 values, in table order:

```text
dff3ea4465cd2a692efe2a458c60418deda184dddfbf2f0d3cc1932f20733542
230be210f913b0b77197e0ea0bf571cb384b83f67696cd3266f5867a3605cbca
954fb7a59e1e63a1802419219de9f08cb56e40bf8396a043a882a5a417034ffc
15f7566753d20747b5db0202d5f089b91f554a14b305d985ba51ad1cddf363dd
1b3d38ba72b230dece174438d96f0d004483b45a6743eb0dc2b1b8f87c77aca5
```

## Handoff boundary

Only this report was created by the checkpoint audit. No existing report,
code, proof, manuscript, evaluation, registry or Git state was edited.
No successful mathematical check, 40-cell oldform grid, experiment or
census was rerun. No final release readiness or frozen-snapshot PASS is
claimed. The three prose findings are closed. The coordinator should
check only newly added or changed link-bearing files as subsequent
checkpoint material is assembled; the later README and nonauthor-review
outputs remain outside the earlier automated scan.
