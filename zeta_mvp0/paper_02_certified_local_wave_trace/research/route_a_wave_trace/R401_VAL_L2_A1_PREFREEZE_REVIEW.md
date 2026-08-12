# R401-VAL-L2-A1 independent pre-freeze review

Review status: **ACCEPTED FOR CONSTRUCTION OF THE MAIN FREEZE ONLY**.  
Protocol: `R401-VAL-L2-A1`.  
Independent review completed: 2026-08-07T06:10:34Z.  
Repository baseline: `caf03bd4391074924becbe081cb1762ac3b70e0f`.

## 1. Scope, independence, and data-access boundary

I reviewed the final pre-freeze implementation and evidence as an independent,
read-only reviewer.  Except for replacing this review file after the audit was
complete, I did not modify the producer, checker, release builder, tests,
protocol, machine record, public replay evidence, CAPD checkout, evaluator, or
any result archive.

I did not initialize or execute the held-out A1 generation, invoke the CAPD
evaluator, read a held-out A1 slab result, or inspect any prospective A1
scientific outcome.  The only numerical archive read was the already public,
accepted six-tree `R401-VAL-L2-S0` archive, through the dedicated read-only
adapter.  All newly generated archives exercised by the tests were synthetic
mock archives.

This review addresses implementation fitness, provenance closure, and
pre-freeze reproducibility.  It does not report or predict the held-out
scientific result.

## 2. Audited worktree and byte scope

The audited repository HEAD was
`caf03bd4391074924becbe081cb1762ac3b70e0f`.  The worktree was intentionally
not clean: it contained exactly four modified tracked files and eleven
expected untracked pre-freeze artifacts.

Modified tracked files:

- `scripts/run_r401_val_l2_all_slabs.py`
- `scripts/check_r401_val_l2_all_slabs_independent.py`
- `tests/test_r401_val_l2_all_slabs_scheduler.py`
- `tests/test_r401_val_l2_all_slabs_checker_contract.py`

Expected untracked artifacts:

- `research/route_a_wave_trace/R401_VAL_L2_A1_MACHINE_FREEZE.json`
- `research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_REVIEW.md`
- `research/route_a_wave_trace/R401_VAL_L2_A1_PREFREEZE_TESTS.json`
- `research/route_a_wave_trace/R401_VAL_L2_A1_PROTOCOL.md`
- `research/route_a_wave_trace/R401_VAL_L2_A1_RELEASE_PROVENANCE_CONTRACT.md`
- `research/route_a_wave_trace/R401_VAL_L2_A1_S0_COMPATIBILITY_REPLAY.json`
- `scripts/build_r401_val_l2_a1_release_provenance.py`
- `scripts/replay_r401_val_l2_s0_through_a1_checker.py`
- `tests/test_r401_val_l2_a1_release_provenance.py`
- `tests/test_r401_val_l2_all_slabs_adversarial_e2e.py`
- `validated/bin/capd_r401_local_complement_mp_a1`

`git diff --check` passed.  A full project scan found no symbolic links and no
authoritative file with multiple hard links.  Targeted scans found no private
key header, GitHub/OpenAI/AWS/Slack-style token, bearer credential, SSH private
key path, or assignment-shaped API-key/password secret in the audited source
and evidence scope.  No unexpected path was present in the Git status.

The formal main freeze
`research/route_a_wave_trace/R401_VAL_L2_A1_FREEZE.json` did not exist, and the
formal result generation `results/r401_val_l2_all_slabs` did not exist.  No
alternative A1/all-slab result directory was found.

## 3. Frozen implementation and test hashes

I recomputed these hashes from the final bytes after all independent test
runs.  They were unchanged by the tests and agree with
`R401_VAL_L2_A1_PREFREEZE_TESTS.json`.

| Role | SHA-256 |
|---|---|
| producer | `ac8d64b8f14e4938de5566c1a8517223dea74c603d2ccc1456317c1b02bf08e7` |
| independent checker | `a03ba2e352e28db434b036f70c9d78a2f04852104a4247393315d28e06775c66` |
| final release builder | `17d345ed663d1650fa7973681a468f297d120602bca6cfbc9630235c71e6a1e6` |
| public-S0 adapter | `32844ebb999461d09a2106e6ddd0008d030af505551b2ff6554b37f1c4ad7383` |
| scheduler tests | `d111d7912b7fbaa221965d4d1ae93383ab34198ea7d3115946c51b7dae65dfe2` |
| checker-contract tests | `36cae4c132c915e4d2e4d3229f7acb0972d135c683e14cfb5a8803e320c61be3` |
| release-contract tests | `c1e3931bf129a741fcb96f2f5b213a92530664504cb153c96238c330f94ed308` |
| adversarial end-to-end tests | `3a4e5374787144605679a1f24a89fd36595d467267a2630bb14e9d6e25bf1980` |

The evidence and protocol hashes were:

| Evidence | SHA-256 |
|---|---|
| formal protocol | `817b8005591f87a89b839d1be01f5629789ff60be5e443614f3eb3365ccd0ea5` |
| machine freeze | `b9291716b859da9651a2549832581cf85b1852b725bcf285539dea47eb7cbef4` |
| pre-freeze test record | `d4889d9e58afd847c03fabb1e8fcb0c4aecfeea779199d9aab22deb1f4dc0ef9` |
| release-provenance contract | `161bee7cd80ffa739335d59d5a43cd275cc585375d52cf3e92d7f3db9ab3e172` |
| public-S0 replay evidence | `959aa94e155cb88a1ad4727dfe5938b92cb3a161f648cbe78ae27ce8aa36e506` |
| CAPD dependency lock | `74ace207ca6322004ee061fe7c47dcc96c34c421446a47b1c6c9f3d29e470d4b` |
| L1 final plan | `a27ca53bee45ccf3bad2aff1fa93949376a522d1f54525c9be8aae9ecc297664` |

The accepted upstream L1 five-object chain rehashed to:

- release provenance:
  `141131916c3a23e38bf2bd3b66a152c1dc6590881bc52baf51818fd988d3200b`;
- summary:
  `e9a71dfd61d26396d05b62a848f49577fdabdf3722101432455435d32bb7503c`;
- manifest:
  `3c653e50042050e69a8928dd1fc7dac3464b6ae8e7ea8d47c70a03e970ece860`;
- independent checker:
  `a6c0db0fc2190013c221d0ecdd71ac6f86895fbaecad735e1f2814ea232280c2`;
- postcheck:
  `83726312ea975ad9741bf2c802bb03fd0898c76646587c2012eb24401537aaf6`.

Each retained `final_status` equal to null, and the five-object chain retained
the accepted `PASS_CONTIGUOUS_LOCAL_BRANCH` local milestone namespace.

## 4. Formal namespace and frozen-input DAG

The producer, checker, and release builder independently declare the same
exact 17-path mandatory input union.  I imported the three final modules in a
diagnostic process, extracted their constants, compared the sets, and obtained
`unions_exact = True`, with 17 unique entries in each implementation.  The
union contains the producer, checker, evaluator source, CAPD dependency lock,
L1 plan, formal protocol, machine record, this independent review, S0 replay,
S0 adapter, release builder, release contract, and the complete five-object L1
chain.

All three parsers reject duplicate JSON keys and non-finite/exponent-overflow
numbers.  Canonical JSON comparison distinguishes booleans, integers, and
floats.  The gates reject noncanonical bound paths, traversal, normalization
aliases, unexpected JSON, symlinked authoritative components, schema/key-set
extensions, and conflicting or nested authority fields.  The review gate
requires exactly one undecorated accepted decision marker; decorated,
escaped, entity-encoded, table, list, quote, dash, full-width punctuation, and
additional-marker variants are covered by regression tests.

The release builder additionally reopens every tree payload and manifest,
recomputes tree statistics and the ordered manifest root, rehashes all five L1
objects, uses same-byte semantic/hash snapshots, checks all open inputs for
mutation, and publishes write-once output from an open inode through a pinned
directory descriptor.  Duplicate-key inputs, numeric type aliases, arbitrary
status fields, raw-byte noncanonical releases, path/hard-link aliases, TOCTOU
swaps, and temporary-name replacement races have explicit regression tests.

A second independent release-contract reviewer audited the same final bytes
and reported no remaining release blocker at producer
`ac8d64b8...`, checker `a03ba2e3...`, builder `17d345ed...`, contract
`161bee7c...`, and release tests `c1e3931b...`.  That review independently
reported 118 release tests, 203 producer/checker tests, and five adversarial
tests passing with hashes stable after execution.

## 5. Matrix, geometry, split rule, and evaluator ABI

The exact matrix extracted independently from both producer and checker has
102 unique ordered entries:

```text
128:S000, ..., 128:S050, 256:S000, ..., 256:S050
```

I exact-parsed all 51 L1 protected boxes.  Every protected interval is
strictly inside the frozen four-dimensional local box.  For each slab, the
producer's Decimal construction and the checker's independent Fraction
construction produced the same eight ordered shells
`C0L,C0U,...,C3L,C3U`, for 408 root shells across the 51 slabs.  The prefix
construction exhausts
`B_loc` minus the interior of the protected box: a point outside the protected
interior belongs to the shell at its first coordinate outside the protected
open interval, with only the intended shared closed faces.

A separate exact diagnostic replayed 25 successive producer splits through
the checker.  At every level, both selected the same maximum normalized-width
coordinate, the same frozen coordinate tie order, the same exact rational
midpoint, and the same two child boxes.  A representative root task produced
exactly 12 string arguments: binary, precision, two epsilon endpoints, and
eight box endpoints.  The checker reconstructs that ABI rather than trusting
the archived invocation.

The prospective main freeze is required to bind exactly:

```text
max_depth                 48 per tree
max_nodes                 20000 per tree
workers                   24
max_inflight_per_tree     1
node_timeout_seconds      7200
global_scientific_budget  null
scheduler_policy          deterministic_round_robin_barrier_batches_v1
```

The fair queue inspects each active tree at most once per barrier.  A
per-barrier reservation is made before evaluator submission, so a second node
from the same tree cannot become in-flight in that barrier and parallel
workers cannot race through a tree's node budget.  Completed futures are
committed in canonical matrix/depth/node order.  The adversarial suite confirms
one-inflight behavior, atomic budget admission, completion-delay hash
invariance, crash-after-parent-commit resume, and whole-generation quarantine
without binding mixture.

## 6. Machine, persistent CAPD build, evaluator, and runtime

I independently re-read the live cgroup and filesystem state after the test
runs:

- scheduler-visible CPUs: 32;
- CPU affinity and cpuset: `128-159`;
- CFS quota/period: `3200000/100000`, equal to 32 CPUs;
- memory limit: `64424509440` bytes, exactly 60 GiB;
- memory failure count: 0;
- swap devices: 0;
- open-file limit: 1,048,576;
- production filesystem: XFS mounted at `/root/autodl-tmp`;
- filesystem total: `375809638400` bytes;
- filesystem available: `373412601856` bytes.

The available storage exceeded the frozen 100-GiB launch minimum and the
150-GiB operational pause threshold.  The machine record itself rehashed to
`b9291716...` and contains the same CPU, memory, storage, and threshold values.

The persistent checkout
`/root/autodl-tmp/zeta/dependencies/capd-r401-a1` was clean at commit
`731079217a9254ea2948d742df2b170895effe7f`.  Its frozen components rehashed
as follows:

| Component | SHA-256 |
|---|---|
| `CAPDVersion.txt` | `e59e67e2e32c5518cca1d14a2500a1dc59fe261367371e81006e1f1a94234a58` |
| `capd-config` | `c758bc9101beb9c633817b0402df9168c6dea9f652d36833101af3273c50338a` |
| `CMakeCache.txt` | `8be735de4b2b2443397b589d0735408f677ebc5dff8bde9fda7ece1e2388ab15` |
| `libcapd.a` | `970088d4ba5024c1b59124299d5e46df41f19936ba53446a5a40a0671968b086` |
| `libfilib.a` | `51c40a22a2405faec793d97a0396022212d7a32f4cca4bf38b994adacaf9be85` |

The current `capd-config --cflags` and `--libs` outputs reproduce the frozen
ordered C++17, MPFR, FILIB, directed-rounding, include, library-path, and link
flags.  The evaluator source hash is
`8eabb022f92c712805c401fb07e2b741e4af4e927bc43702c95125b2a4338bd2`.
The A1 binary is a regular, single-link, mode-0755 x86-64 ELF file of 2,446,080
bytes with hash
`b768de84247cd847a3c1b518ec08a7bcfc766e31c20c01bcdd0c75b06d319d53`.
It is byte-identical, by both `cmp` and SHA-256, to the accepted public-S0
binary.

The live tool hashes matched the machine record:

- Python: `9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101`;
- g++: `d7122fd9a7a8fe12d12c00c54d3a6fbebcb3e9285cf675709674e751d900fc63`;
- CMake: `fd22547781b64bb2db04370970b93db1f3fada1e41e60873b015ee0747009fc0`;
- Git: `fd7c9389e200d626b46551835e5233bbde49a6a2326f9ebb85c70ed235861001`.

The resolved runtime-library hashes also matched exactly:

| Library | SHA-256 |
|---|---|
| `libmpfr.so.6.1.0` | `ce9a4f2b97522cea4a4cf89cbe8a5fd5e1cc44ef25ef71d161ac109eac9bdcc6` |
| `libstdc++.so.6.0.30` | `41c4cd10be11160dec736958a59eb0553357ad77008e9ba56250d4fd8698b8ec` |
| `libm.so.6` | `2877e828e386ca225c14ec01cb2d7f07e61dbc025ffb15e524c100a1e9ab3070` |
| `libgcc_s.so.1` | `39c9bb846d8491ec41e89b7d34b824e7b6e7ff37d7b9de549305a15c2f7a6cf7` |
| `libc.so.6` | `c662f0eb3e4b8da67692edd53934263e9e4807105d4228b0c12c3d93dca49fd3` |
| `libgmp.so.10.4.1` | `4dc20a901c6951e678e216e959da2534bcef7053e6efdf1492509baf142282b0` |
| ELF loader | `8c7e2990d2847ca210d6f716d4b9aa62997c2fd2acfcda587c1ec398ed364618` |

## 7. Independent commands and results

The first attempted GNU timing wrapper stopped before launching pytest because
`/usr/bin/time` is not installed.  I then used Bash's timing builtin.  No test
result depends on the failed wrapper attempt.

Executed validation commands and outcomes:

| Command | Independent outcome |
|---|---|
| `python -m py_compile scripts/run_r401_val_l2_all_slabs.py scripts/check_r401_val_l2_all_slabs_independent.py scripts/build_r401_val_l2_a1_release_provenance.py scripts/replay_r401_val_l2_s0_through_a1_checker.py` | pass |
| `pytest -q tests/test_r401_val_l2_all_slabs_scheduler.py tests/test_r401_val_l2_all_slabs_checker_contract.py` | 203 passed in 2.82 s; shell wall 3.870 s |
| `pytest -q tests/test_r401_val_l2_a1_release_provenance.py` | 118 passed in 18.78 s; shell wall 21.469 s |
| `pytest -q tests/test_r401_val_l2_all_slabs_adversarial_e2e.py` | 5 passed in 46.14 s; shell wall 48.286 s |
| `pytest -q` | 353 passed in 72.90 s; shell wall 74.706 s |
| `python scripts/replay_r401_val_l2_s0_through_a1_checker.py` piped to exact byte comparison against the frozen replay JSON | pass; shell wall 24.465 s |
| `pytest --collect-only -q` on the four formal test files | 92 scheduler, 111 checker, 118 release, and 5 adversarial tests collected |
| standalone exact-geometry Python audit | 51 slabs, 408 root shells, 102 matrix entries, 12-string ABI, and 25 split levels passed |
| internal evidence-hash Python audit | all 19 implementation/evidence/S0 bindings matched current bytes |
| `git diff --check`, `git status --short --untracked-files=all`, symbolic-link/hard-link scans, and targeted secret scans | pass with only the expected scope listed in section 2 |

The final expanded suite supersedes the earlier pre-hardening minima of 124
formal contract tests, 11 release tests, and 167 full-project tests.  The
producer's immutable pre-freeze record independently reports 92 scheduler,
111 checker, 203 combined, 118 release, 5 adversarial, and 353 complete-suite
passes.  Its hash and every implementation/test hash recorded inside it agree
with current bytes.

## 8. Public S0 read-only compatibility replay

The dedicated adapter contains no archive write, rename, deletion, or
evaluator invocation.  It strict-parses and rehashes the accepted S0 release,
manifest, and postcheck; adapts each old tree in memory; exact-replays the shell
and split DAG; and replays every transcript through the current A1 checker.

My rerun was byte-for-byte identical to the frozen evidence and returned:

```text
status                    PASS_S0_READ_ONLY_COMPATIBILITY_REPLAY
tree_count                6
node_count                3016
manifest_hash_checks      6055
ENERGY_EXCLUDED           183
RETURN_EXCLUDED           1349
UNKNOWN                   1484
```

The ordered per-tree totals were also exact: `128:S000=486`,
`128:S025=546`, `128:S050=574`, `256:S000=436`, `256:S025=488`, and
`256:S050=486`.  Current checker and adapter hashes, plus the three actual S0
object hashes, were rebound rather than trusted as strings.  The S0 release,
manifest, and postcheck hashes were respectively `5b7397bac1d5...`,
`e7cf17df2e91...`, and `df7a2439d421...`.

## 9. Authority separation and claim boundary

The producer leaves `milestone_status`, `theorem_status`, and `final_status`
null in the run config, node records, tree objects, tree manifests, aggregate
objects, quarantine record, scheduler state, and operational-storage record.
It cannot assign the all-slab milestone.  Only the frozen independent checker
can assign `PASS_LOCAL_COMPLEMENT_ALL_SLABS`, after exact replay of all 102
trees and their complete provenance DAG; `final_status` still remains null.

The licensed statement is restricted to pointwise reduced-root uniqueness in
the frozen local `P_+=0` chart over the frozen 51 L1 slabs.  It is not a full
periodic-orbit phase cover, an energy-shell or global uniqueness result, a
primitive-period result, a trace formula, an arithmetic-prime result, a
Hilbert--Polya operator, a zeta-zero reconstruction, the Riemann hypothesis,
or progress implying RH.  Nothing in this pre-freeze review promotes any of
those claims.

## 10. Remaining mandatory conditions

No implementation blocker remains in the audited byte set.  Acceptance is
nevertheless conditional on the following sequencing and immutability rules:

1. The main freeze must be generated only after this file reaches its final
   bytes.  It must bind this file's newly computed SHA-256 and all other exact
   hashes above, the 17-input union, the ordered 102 matrix, the fixed
   `48/20000` per-tree limits, the `24/1/7200/null` scheduler values, exact
   machine requirements, evaluator object, closed status/return-code
   whitelist, logical thresholds, and claim boundary.  This review does not
   certify a main freeze that did not yet exist during review.
2. Any change to a reviewed implementation, test, protocol, machine, CAPD,
   evaluator, runtime, S0, upstream-L1, or review byte requires a new hash
   binding and renewed independent review before dispatch.
3. The operator must run the formal `--initialize-only` gate first, inspect
   the sealed run config and initialization state, and only then begin
   `--execute` with the same exact freeze and CLI binding.  This review alone
   does not authorize held-out dispatch.
4. A later passing checker and release would establish only the local milestone
   described in section 9.  A resource stop is inconclusive, a root candidate
   is a preserved route failure, and neither outcome may be converted by
   post-hoc domain or budget tuning.

Subject to those prospective conditions, the implementation and evidence are
sufficiently closed, reproducible, fail-closed, and independently tested to
construct the formal main freeze.

Verdict: ACCEPT_FOR_FREEZE
