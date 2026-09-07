# P209 manuscript-A root pair preparation

Status: `PREPARED_NOT_EXECUTED`. This is infrastructure only. No root
producer, build, scientific comparison, manuscript review or delta has been
run or accepted by this preparation. Root must first read all adapter lines
and the exact diff, inspect A's original mathematical/source evidence, and
verify that A's complete initial package is sealed. Do not execute before
those obligations are complete.

## Familiarity and exact provenance

The preparer is the P209 manuscript author, previously the P208 B reviewer
and a P208 artifact-infrastructure contributor. That familiarity makes the
preparer ineligible to review P209. This task read the full actual A
recorder (693 lines) and launcher (145 lines), not the independent A
mathematical verifier or bootstrap bodies. It makes no new mathematical
claim and supplies no independent review. The prior
`qa/p209_author_root_preparation/` was inspected as an infrastructure model;
the current wrappers are adapted directly from the actual A originals.

The two physical original copies are exact:

- `original_snapshot/record_review.py`:
  `e4bd771c173c08330ac3cc678241e340911b4a37bd47ca3e18871310f4cbacf2`.
- `original_snapshot/launch_review.py`:
  `e41c97b8bc91c57be614412bd3e839595b40fffd549f79f1ccbdfadd3461ed1d`.

The root wrappers are:

- `root_record_pair.py`, 697 lines:
  `3222c60b9e7c7b3815a048598dcc770e700945b349b7c3312d3b3346a140954f`.
- `root_launch_pair.py`, 164 lines:
  `8baa2ead5896bc7ede9f39ec6afb449feeafafe91b36d77f3e11a89cf3a66193`.

`ADAPTATION.diff` is the complete concatenation of the two actual ordinary
unified-diff outputs, 13,770 bytes:
`00783032215477b1c07eef1f80607af269674f488b86026c11cc04aaf8635f39`.

## Exact restricted behavior

`PAPER` denotes the immutable reviewer input directory
`docs/papers204_208_sequence/reviews/p209_a/`, not the manuscript author's
directory. The full `papers/209-ordered-fibre-threading/frozen_round0/`
remains an input: 1,989 payloads and its existing nonself manifest, SHA256
`0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba`.
The original complete-freeze check, independent payload schema and
n=0..5 / 3,414-state guards are unchanged.

Only the exact invocation `pair root_a_pair_01` is allowed. It may later
create the pair at
`qa/root_replays/p209_a_strict/root_a_pair_01/` and its separate outer
stream receipt at
`qa/root_replays/p209_a_strict/launcher_root_a_pair_01/`, both under the
current batch. Preparation created neither the output root nor these
execution directories. Existing paths, output-root aliases and existing
cache prefixes are refused; this wrapper does not authorize another label.

Changes are limited to fixed path/role settings, the exact pair-only entry
guards, adding both new wrappers to initial inputs, and the mandatory
existing-canonical/no-adoption restriction. Both wrapper layers additionally
enforce the supplied exact A recorder and launcher hashes above, plus:

- A's unchanged `verify.py`:
  `28fad641f3928907c9dca259b3360000f0c9063edee7005148ed9a5fc10779af`.
- A's existing, read-only `CANONICAL.json`:
  `9dd6229968748e2caf0e3fe74b802603b6dc51f37704bdf098dbdfb969433b36`.

Root must pin this preparation and its new launcher before use. The new
launcher pins itself, the new recorder, original A infrastructure, the
unchanged verifier/bootstrap, parameters, existing canonical and its named
launch executables before copying or launching the recorder. Copied code
bytes are checked against those initial pins. The recorder includes both
new wrapper sources in its pre-child scientific/provenance input set.
No old recorder is imported. Fresh scientific capsules still contain only
the two unchanged A code files; no mathematical implementation or cutoff
was edited.

All canonical-writing/adoption branches are removed. Existing-canonical
initial-pin protection, final full-input closure and the three raw
comparisons (pair, run1/canonical, run2/canonical) remain. The inherited
diagnostic label `ADOPTED_CANONICAL_BYTES` and false-valued
`canonical_adopted` field are retained to minimize the diff; neither
permits adoption.

The original runtime/configuration/initial-pin inventories, isolation,
pre-spawn command attempts, full streams, failed-process cleanup,
incremental failure evidence, dynamic-link/observed-input closure and
complete nonself seals remain. All 20 recorder function bodies outside
`science`, `pair` and `main` are byte-identical source blocks; notably
the complete build helper is unchanged and unreachable through the
pair-only entry guard. Launcher `pin` and `save` are unchanged; only
`check_closed_recorder` and `main` change. Imports are identical.

## Actual preparation-only checks

The following commands were actually run from
`/root/autodl-tmp/symbolic_dynamics`. These are source-copy/diff checks,
not scientific execution. The two `cmp` commands had no output. Each
`diff` returned the expected 1 for an intentional difference; its complete
output is retained in the corresponding section of `ADAPTATION.diff`.

- Exit 0, output 0 bytes: `/usr/bin/cmp -- docs/papers204_208_sequence/reviews/p209_a/record_review.py docs/papers204_208_sequence/qa/p209_a_root_preparation/original_snapshot/record_review.py`
- Exit 0, output 0 bytes: `/usr/bin/cmp -- docs/papers204_208_sequence/reviews/p209_a/launch_review.py docs/papers204_208_sequence/qa/p209_a_root_preparation/original_snapshot/launch_review.py`
- Exit 1, output 7681 bytes: `/usr/bin/diff -u --label original_snapshot/record_review.py --label root_record_pair.py docs/papers204_208_sequence/qa/p209_a_root_preparation/original_snapshot/record_review.py docs/papers204_208_sequence/qa/p209_a_root_preparation/root_record_pair.py`
- Exit 1, output 6089 bytes: `/usr/bin/diff -u --label original_snapshot/launch_review.py --label root_launch_pair.py docs/papers204_208_sequence/qa/p209_a_root_preparation/original_snapshot/launch_review.py docs/papers204_208_sequence/qa/p209_a_root_preparation/root_launch_pair.py`

The following static-only program was actually executed with
`/usr/bin/python3.10 -I -S -B -c`. It imports no infrastructure or
scientific implementation and performs no subprocess launch:

```python
import ast, hashlib, json
from pathlib import Path
base = Path("docs/papers204_208_sequence/qa/p209_a_root_preparation")
review = Path("docs/papers204_208_sequence/reviews/p209_a")
expected = {
    "record_review.py": "e4bd771c173c08330ac3cc678241e340911b4a37bd47ca3e18871310f4cbacf2",
    "launch_review.py": "e41c97b8bc91c57be614412bd3e839595b40fffd549f79f1ccbdfadd3461ed1d",
    "verify.py": "28fad641f3928907c9dca259b3360000f0c9063edee7005148ed9a5fc10779af",
    "CANONICAL.json": "9dd6229968748e2caf0e3fe74b802603b6dc51f37704bdf098dbdfb969433b36",
}
assert all(hashlib.sha256((review/n).read_bytes()).hexdigest() == h for n,h in expected.items())
rows=[]
for original, adapted, allowed in (
    ("record_review.py", "root_record_pair.py", {"science","pair","main"}),
    ("launch_review.py", "root_launch_pair.py", {"check_closed_recorder","main"})):
    old = (base/"original_snapshot"/original).read_text()
    new = (base/adapted).read_text()
    assert old.encode() == (review/original).read_bytes()
    old_ast, new_ast = ast.parse(old), ast.parse(new)
    old_funcs = {n.name:n for n in old_ast.body if isinstance(n,ast.FunctionDef)}
    new_funcs = {n.name:n for n in new_ast.body if isinstance(n,ast.FunctionDef)}
    assert old_funcs.keys() == new_funcs.keys()
    changed = {n for n in old_funcs if ast.dump(old_funcs[n]) != ast.dump(new_funcs[n])}
    assert changed == allowed, changed
    for name in old_funcs.keys()-allowed:
        a,b=old_funcs[name],new_funcs[name]
        assert old.splitlines(keepends=True)[a.lineno-1:a.end_lineno] == new.splitlines(keepends=True)[b.lineno-1:b.end_lineno]
    assert [ast.dump(n) for n in old_ast.body if isinstance(n,(ast.Import,ast.ImportFrom))] == [ast.dump(n) for n in new_ast.body if isinstance(n,(ast.Import,ast.ImportFrom))]
    rows.append({"original":original,"adapted":adapted,"changed_functions":sorted(changed),"unchanged_function_source_blocks":len(old_funcs)-len(changed),"lines":len(new.splitlines())})
freeze=Path("papers/209-ordered-fibre-threading/frozen_round0/SHA256SUMS")
assert hashlib.sha256(freeze.read_bytes()).hexdigest() == "0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba"
assert len(freeze.read_text().splitlines()) == 1989
assert not Path("docs/papers204_208_sequence/qa/root_replays/p209_a_strict").exists()
print(json.dumps({"status":"PASS_STATIC_PREPARATION_ONLY","original_pins":expected,"function_checks":rows,"round0_payloads":1989,"replay_output_root_absent":True,"scientific_executions":0},sort_keys=True))
```

Actual exit 0 and complete stdout:

```json
{"function_checks": [{"adapted": "root_record_pair.py", "changed_functions": ["main", "pair", "science"], "lines": 697, "original": "record_review.py", "unchanged_function_source_blocks": 20}, {"adapted": "root_launch_pair.py", "changed_functions": ["check_closed_recorder", "main"], "lines": 164, "original": "launch_review.py", "unchanged_function_source_blocks": 2}], "original_pins": {"CANONICAL.json": "9dd6229968748e2caf0e3fe74b802603b6dc51f37704bdf098dbdfb969433b36", "launch_review.py": "e41c97b8bc91c57be614412bd3e839595b40fffd549f79f1ccbdfadd3461ed1d", "record_review.py": "e4bd771c173c08330ac3cc678241e340911b4a37bd47ca3e18871310f4cbacf2", "verify.py": "28fad641f3928907c9dca259b3360000f0c9063edee7005148ed9a5fc10779af"}, "replay_output_root_absent": true, "round0_payloads": 1989, "scientific_executions": 0, "status": "PASS_STATIC_PREPARATION_ONLY"}
```

All supplied current original hashes still matched after preparation.
No A file, manuscript, frozen input, active-review evidence, central index
or Git state was changed. No replay output directory was created.

## Root execution after sealed-original inspection

First verify all six payloads in this preparation's complete nonself
`SHA256SUMS`, pin the wrapper sources, and finish the original-evidence
inspection described above. From the workspace root, the only allowed
command is shown below for later root use. It was not executed by the
preparer.

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/root_replays/p209_a_strict/launcher_root_a_pair_01/never_created_launcher_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p209_a_root_preparation/root_launch_pair.py pair root_a_pair_01
```

An eventual `PASS_ROOT_REVIEW_A_PAIR` means root executed A's unchanged
verifier, not a new independent reviewer or accepted manuscript delta.
Keep all failures. The original outer `UNCLOSED_NO_SEAL` policy refuses
settled-stream hashes, a final seal or PASS when the recorder lacks a
verifiable completed receipt/seal. It does not infer that all descendants
have exited. Before-invocation setting/hash failures also authorize no
scientific execution or success claim. Any needed future retry requires
an explicitly disclosed new scope; do not overwrite these sealed wrappers
or an existing execution directory.

Evidence remains bounded early/late modules/maps and direct-child map
sampling plus conservative inventories, not continuous tracing,
grandchild capture or an OS-hermetic reconstruction. The project research
skill controls this separation of preparation from execution and the
preservation of original evidence. External actions remain
`HOLD_EXTERNAL`.
