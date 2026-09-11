# UGR independent execution and artifact receipt

2026-09-06 UTC. These are actual candidate-review executions, not archived
hash checks, author-code reruns or manuscript-review acceptances.

## New producer and independent representation

`verify_gate.cpp` takes no command-line parameters and reads no files.
It uses direct ternary comparisons on all 13-letter local words; a fresh
81-state four-height overlap graph for U^2 fixed points; direct cyclic
functional-graph walks; a newly implemented formula read from the prior
TCSD proof to sum all sign strata; and explicit seed profiles. It neither
imports nor runs author code, old pilot code, old verifiers or canonical
data. The source and all mathematical checks use deterministic ordering.

The complete cyclic boxes remain n=3,...,10, exactly 88,560 states.
The n=4,...,64 work is a single predeclared seed per length, not a larger
complete-box experiment. The graph traces through degree 81 certify a
fixed finite matrix identity, not an inferred larger cyclic atlas.

`record_gate.py` is a new standard-library Python harness. It compiles
the producer from source, captures every stream, runs either the initial
canonical producer or two new producers, and invokes actual raw `cmp`.
Each output directory must be new. It will not overwrite the canonical.
Compiler was g++ 11.4.0 and the harness runtime was Python 3.12.3;
platform and complete command vectors are recorded in the JSON receipts.

## Actual successful commands and outputs

From the workspace root:

```text
python3 -B docs/papers204_208_sequence/scouting/word_local/UGR_GATE/record_gate.py canonical_run --canonical
python3 -B docs/papers204_208_sequence/scouting/word_local/UGR_GATE/record_gate.py replay_pair_01
```

The cold compiler command in each directory is
`g++ -std=c++17 -O2 -Wall -Wextra -Werror verify_gate.cpp -o NEW_DIR/verifier`,
with absolute paths in the actual receipt. Both successful compiles exited
zero. The canonical producer and both new replay children exited zero.
Each of the two replay-to-canonical raw comparisons exited zero, with
empty stdout and stderr. Every run had 2,638,324 assertions.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `verify_gate.cpp` | 12,925 | `dda534f27a47161b4d38e2294c00876a080088ac36d6fd55169ce6c11c91aa1c` |
| Each successful compiled verifier | 74,280 | `d086a3f4d9695bffb7ddf508919757f1a9e0df781123ab523f42b86d31c069b3` |
| `CANONICAL.jsonl` and each successful stdout | 6,184 | `6beafa58167d74b9db85ca8001b8a54043ad6ffbe493901a6046ead5485e2cb5` |
| Each successful child stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The canonical contains the full declared census: every local witness
class count; all 81 exact graph traces; every cyclic box's image/core,
height and eventual-period histograms, maximum and complete maximizer
list, and multiple-sign-stratum census; witness scope; and assertions by
kind. The eventual-period histogram counts **source/basin states**, not
cycles. Detailed per-case outcomes contribute to an ordered FNV-1a
diagnostic `8297652872254188400`; it is not a cryptographic substitute
for the full stdout SHA-256.

The two complete new execution records and comparator streams are in
`replay_pair_01/receipt.json` and its named sibling files. For root's
pair, copy the pinned producer, canonical and harness into a new root-owned
QA directory and run that exact copied harness with a new subdirectory
name, preserving this closed package and all its prior receipts.
No current root replay is claimed by this assessor's package.

## Preserved failure and limits

The first C++ compile failed under `-Werror=misleading-indentation` on
three dense formatting lines, before any mathematical execution. The
exact pre-fix source is `verify_gate.failed_compile_v1.cpp`. The original
tool console was observed with exit 1; a later actual recompilation of
that preserved source also exited 1 and its complete output and command
are retained in `FAILED_COMPILE_V1_REPRODUCTION.json`. That JSON clearly
identifies a reproduction, not an invented original raw-stream receipt.
The final source separates/braces those lines and uses stamped visitation
arrays for the functional-graph walks; no mathematical premise changed.
No failed mathematical execution of this independent verifier is hidden.

The author's earlier local-cone conjecture counterexamples and initial
core-checker failure remain in its unchanged, pinned author package.
They were read and are not reclassified as passing tests. The final
radius-six lemma and full neighbour-equation proof do not use them.

Nineteen workspace-root-relative input pins record scientific and source
dependencies. The original UGR author manifest has 27 nonself entries.
Actual final checks are retained in `INTEGRITY_CHECK.json`; the package
`MANIFEST.sha256` is directory-relative and contains every regular file
except itself. Its check is performed after creation, not self-listed.
No builds, PDF views, manuscript freezes, accepted deltas or external
reviews are implied by this candidate-level receipt.
