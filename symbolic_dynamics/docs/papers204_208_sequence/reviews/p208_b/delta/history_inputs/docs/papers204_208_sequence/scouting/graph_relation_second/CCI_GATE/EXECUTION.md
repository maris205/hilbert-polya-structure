# CCI independent execution and integrity record

2026-09-05 UTC. Working directory:
`/root/autodl-tmp/symbolic_dynamics`. Runtime: Python 3.12.3, standard
library only; Bash for the byte-comparison process substitutions. `-B`
disables bytecode output. There are no seeds, optional dependencies, author
imports, data reads, network calls or nondeterministic output fields.

## Direct executions

The following command was actually executed twice in fresh Python processes:

```sh
python -B docs/papers204_208_sequence/scouting/graph_relation_second/CCI_GATE/verify_gate.py
```

Both direct executions completed with exit zero and no error output. Each
produced the complete JSON object preserved in CANONICAL.json, including
its final LF. The entire object was returned by the execution interface,
not a truncated excerpt. Its status was
`PASS_INDEPENDENT_BOUNDED_CCI_GATE`, with 7,530,194 assertions.

Actual canonical size: **5,375 bytes**. Actual SHA-256:
`da851425b43c4ef7d27b56f29d9fb5a6d5091435f26aed795da463dd7f876783`.
Its enumeration digest is separately
`93584703f8491bb0fb9d8e7273fdb38134f049c759937d0df0806a0db7972a6f`.
The latter describes records visited by the verifier; it is not a substitute
for the full canonical or its raw-byte comparison.

## Two actual raw-byte canonical replays

After the saved canonical existed, the following command was launched twice
in separate Bash executions, each spawning a new Python interpreter:

```sh
cmp docs/papers204_208_sequence/scouting/graph_relation_second/CCI_GATE/CANONICAL.json <(python -B docs/papers204_208_sequence/scouting/graph_relation_second/CCI_GATE/verify_gate.py)
```

| Replay | Consumer exit | Complete stdout/stderr |
|---|---:|---|
| Fresh canonical comparison 1 | 0 | empty |
| Fresh canonical comparison 2 | 0 | empty |

These are comparisons of new executions with actual archived raw bytes,
not normalized JSON equality or a comparison between archived hashes.
Process-substitution producer statuses are not independently surfaced by
`cmp`; the two direct runs above separately provide actual producer exit-zero
evidence. The verifier prints only after all checks complete and has no
subsequent computation that is being hidden by the consumer status.

## Coverage and independent representations

- All labelled simple graphs on n=0,…,5 at q=3, n=0,…,4 at q=4, and
  n=0,…,3 at q=5 and q=7: **275,093** complete source states and the same
  number of target source-set comparisons. Literal arrows are enumerated
  first; functional-graph leaf peeling provides h and eventual period.
- Initial coloured edge weights are independently closed with all-pairs
  Floyd recurrence. Every source is literally followed through the uniform
  entrance bound plus a full palette period. The all-time coordinate and
  permanent-activation controls each make **2,765,281** checks.
- Every target's exact brute source list is compared with a held-set decoder
  (independent set, surviving internal neighbor, successor closure), dual to
  the author's active masks. No count-only agreement substitutes for source
  identity. Every graph/target extremizer is checked.
- Every simple graph through six vertices: **33,868** static cover counts,
  upper bounds and complete graph equality tests via independent-complement
  masks. These small graphs pressure, but do not prove, the all-order lemma.
- **117** explicit path constructions, n=2,…,14 and q=3,…,11, directly
  verify oriented distances and literal sharp trajectories. The three
  decoder-condition ablations, unweighted/reversed arrival errors, a CCA
  literal separator and a nonconstant recurrent state are recorded controls.

No verifier imports or adapts the author's implementation. Only mathematical
definitions/statements were shared. The full script hash is
`aaca2596d081f879ec021d9648680e11ab0e972004309d5fd5cca7d3ae61c502`.

## Pins, manifests and interpretation

INPUTS.sha256 has eleven workspace-root-relative documentary input pins:
the closed seven-file author/provenance selection plus four actual internal
originals used for collision tests. All eleven were checked with

```sh
sha256sum -c docs/papers204_208_sequence/scouting/graph_relation_second/CCI_GATE/INPUTS.sha256
```

and returned `OK`, exit zero. SHA256SUMS is separate and gate-directory
relative; it covers every local evidence file except itself. It does not
pretend to replace the author's parent-directory manifest or to include
unrelated parallel scouting work. Its complete check and local Markdown
link check are run after all gate files exist.

These receipts establish independent bounded proof pressure and unchanged
inputs. They are not all-parameter proofs, external owner certification,
manuscript reviews, PDF builds, visual page checks, formal numbering or
five-paper completion. The deductive audit and scope-limited GO are in
CANDIDATE_GATE.md; the positive source deductions and accepted claim-framing
boundary are in SOURCE_GATE.md and AUTHOR_RESPONSE.md.
