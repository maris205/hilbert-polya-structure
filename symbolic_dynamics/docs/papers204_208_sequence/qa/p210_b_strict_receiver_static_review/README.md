# Independent static review of the P210 B strict-pair receiver

Reviewed source: 232 lines, SHA256
`7234bba399e556b5d22560412785f2d64886471642baf53b7544ae9b41d6053a`,
physically retained as [the before-followup source](inspect_p210_b_strict_pair.before_root_followup.py).
The current B runner is 623 lines, SHA256
`bacc8bf0351bdfbcc2bc671cd61131d6382fe5caccd00f02e3988afbf1d066d1`.

[Actual static checks](STATIC_REVIEW.actual.json) passed 18 AST/documentary
conditions with native exit 0; [the complete native return](STATIC_NATIVE_RETURN.actual.json)
retains command/stdout. Seven named input files were read, including B's existing
canonical as data; its 6 MB body is not duplicated here. Eight A helper functions
are unchanged and only `main` is adapted. The static script did not execute or
import an inspector, runner, verifier, old A auditor or scientific program,
regenerate host inventories, or modify root's sources.

No incorrect field name was found in the receipt, settlement and observed-child
consumer groups: the actual producer contains every literal field consumed.
The corrected owned-session fields, single-element scientific argv/sibling
parameter locator, B representation/edge fields, 51,129 checks, 4,095 state rows,
265 triangular rows and mass box 1..12 match the actual source/data.

The following are **concrete root original-reception obligations before first
inspector execution**, not manuscript findings, scientific failures, fabricated
pair outcomes, or instructions to rerun any science. Root owns any new inspector
revision; this original/static review remains unchanged.

## 1. Reconstruct all ten native argv, not just their labels

Use P = absolute B review package, O = absolute `root_replays/p210_b_strict_pair_01`,
S = absolute `p210_b_strict_preparation`, Q = `/usr/bin/python3.10`.
Let E be the sorted resource names starting `/usr/lib/python3.10/` and ending
`.so`, exactly as runner lines 498–499. Compare the actual argv for each label:

| Label | Exact argv |
|---|---|
| 00_cmp_runner_source | ['/usr/bin/cmp', '--', S+'/run_pair.py', O+'/sources/run_pair.py'] |
| 01_cmp_verifier_source | ['/usr/bin/cmp', '--', P+'/verify.py', O+'/sources/verify.py'] |
| 01a_cmp_parameters_source | ['/usr/bin/cmp', '--', P+'/PARAMETERS.json', O+'/sources/PARAMETERS.json'] |
| 02_ldd_before / 06_ldd_after | ['/usr/bin/ldd', Q, '/usr/bin/cmp'] + E |
| 03_verify_N, N in 01,02 | [Q, '-I', '-S', '-B', '-X', 'pycache_prefix='+O+'/unused_child_'+N+'_cache', O+'/sources/run_pair.py', 'child', N, 'p210_b'] |
| 04_cmp_canonical_N, N in 01,02 | ['/usr/bin/cmp', '--', O+'/commands/03_verify_'+N+'/stdout.raw', P+'/CANONICAL.json'] |
| 05_cmp_pair | ['/usr/bin/cmp', '--', O+'/commands/03_verify_01/stdout.raw', O+'/commands/03_verify_02/stdout.raw'] |

Every ATTEMPT has `stdin='DEVNULL'`, `new_owned_session_requested=True`,
`status='ATTEMPTED'`, `exit_code=None`, exact ENV/cwd, and timeout 300 for
03_verify labels, 60 for every other label. Compare **all** immutable attempt
fields with receipt fields. Receipt success is `status='COMPLETED'`,
`interrupted=False`, integer native/wrapper exits 0, existing success/quiescence
conditions, and parseable `ended_utc >= started_utc`. Owned pgid/sid must be the
same positive integer; zombie-only remaining members keep their actual identities.
Do not replace the real command/stream/session records with this expected table.

Current inspector lines 175–191 check labels and cross-record consistency,
but not exact per-label argv, expected timeout, explicit completed/interrupted
state, or chronological ordering. These are source-defined checks, not requests
for new external process evidence.

## 2. Reconstruct the complete known/configuration key sets

Current inspector lines 157–170 validate all supplied keys and current listed
resources, but do not reconstruct the generator's complete expected known set
or exact configuration-name set. The runner's set formula (lines 484–489) is:

```python
base = set(package_files) | set(preparation_files) | set(resources)
base |= set(INPUT_PINS['inputs'])
base |= {row['copy'] for row in source_only_initial.values()}
base |= {name for name, row in configuration.items() if row['is_file']}
expected_known = base | {str(Path(name).resolve(strict=True)) for name in base}
assert set(INPUTS_BEFORE) == set(INPUTS_AFTER) == expected_known
```

Here package_files is every one of the 407 B manifest payload paths plus the
B seal; preparation_files is the four preparation payload paths plus its seal;
copies are exactly the three source capsule files. Preserve both lexical and
resolved names. In particular compare every expected resource/configuration file
to its known rich key, not merely to an independently listed resource name.

Rebuild configuration independently using the exact source-defined
`configuration()` at runner lines 200–233: LIB_ROOTS + DATA_ROOTS + STDLIB;
sysconfig Makefile/config-header names; the literal loader/locale/NSS/shell/SSL/
zip/venv/path-injection names listed there; four `._pth` names under each of
`/usr/bin` and `/usr/lib`; the path `/usr/lib/` + value + `._pth` for each
nonempty LDLIBRARY/INSTSONAME value; and exact loaders parsed from
the pinned ldd RTLDLIST. Compare the exact name set as well as every presence,
resolution, symlink and existing-file key. Do not execute/import the runner
to obtain the configuration. The current source's explicit-absence checks
(no preload/system zip/._pth/pyvenv) remain source-defined requirements.
No old A 120k ledger expansion is needed.

## 3. Parse the three generated records currently only read under the seal

These exact records are emitted by the runner but are absent as parsed inputs
from the reviewed inspector source; their bytes are currently protected only
by the complete 59-payload manifest.

- `RUN_ENTERED.json` (runner 466): status
  `ENTERED_NOT_A_PRESPAWN_RECEIPT`, actual parseable started_utc, exact parent
  argv and interpreter_argv, environment/cwd, rich source key of S/run_pair.py.
  Match argv/interpreter_argv to the actual root launch, including parent
  `-I -S -B -X pycache_prefix=O/unused_parent_cache`, run mode, role and prep seal.
  It explicitly remains an entry record, not reconstructed pre-spawn evidence.
- `SOURCE_ONLY_INITIAL.json` (481): exactly run_pair.py, verify.py and PARAMETERS.json;
  each value has actual origin, exact O/sources copy, SHA256 and bytes matching
  source/copy originals. The origin/copy pair must be prescribed, not merely
  internally self-consistent.
- `COMMAND_CLOSURE.json` (569): command_count 10, native_streams_rechecked 20,
  and the actual declared scope string. Independently rechecking the actual
  commands/streams is still required.

Also compare the full PACKAGE_AND_PREPARATION_CLOSURE before/after object with
freshly reconstructed preflight values, including exact preparation_files and
manifest/science/parameter keys, not only its package_files set. Bind the two
RESULT.results rows (numbers 01/02, 51,129 checks each, actual stdout keys)
to the verified original streams and actual native parent summary.

## 4. Retain complete actual stdout/session handling

Runner line 400 can emit a one-line `ROOT_B_OWNED_NATIVE_RUNNING` heartbeat after
a command wait exceeds 30 seconds; it subsequently emits the final pretty JSON.
The reviewed inspector's lines 139–145 require empty launch output and one JSON
object in completion output. This is a **conditional transport boundary**, not
an observed source failure: no strict pair or receiver was run by this review.
Root must examine and preserve the actual complete segmented return. If heartbeat
text actually occurs, distinguish and validate it plus the final object without
discarding bytes or inventing session IDs. Do not presume that it occurred.

The review does not revise the exact scientific contract or authorize B delta,
Round2, terminal builds/views, five-paper acceptance, Git actions or external
release. `OWNER_AMBER / HOLD_EXTERNAL` remains in force.
