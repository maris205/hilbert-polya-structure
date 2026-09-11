# Root replay of the four new candidate-gate packages

2026-09-05 UTC. These are candidate checks, not manuscript Review A/B.
Root ran each named independent verifier in a fresh subprocess and compared
captured stdout byte for byte with its frozen canonical transcript. Every
process exited zero and had empty stderr. Every non-self package manifest
passed. Input pin resolution is detailed below; no proof files changed.

| Gate | Input pins | Assertions per verifier run | stdout SHA-256 | Seconds |
|---|---:|---:|---|---:|
| FOSP | 15 | 1,496,779 | baade2cc4fb29d31fb0a5b2d5560de283959e901faeb1a44b3c69fc2fe43de06 | 4.671 |
| LZK kill | 10 | 459,463 | 09ceb3da76aeb6af0ddcb5540f9cc74dd6d47aec8c7f2cb8753f0729e5526cce | 1.347 |
| CPD/CSPD owner transfer | 4 | 140,348 | e962713da80dc9b9d550fb98a13ce1ea52c392a2a005f7e4547f517486d42ea1 | 0.744 |
| LFAS re-entry | 10 | 3,595,488 | d1c0119a74fccecf1f3721c01e24d8a7d6f251b680cdb4ed287bf4e8a459c197 | 14.789 |

## Historical recovery-index pins

The first ordinary `sha256sum -c` invocation on FOSP inputs reported two
mismatches: SYMBOLIC_DYNAMICS_STATE.md and this batch's PIPELINE_STATE.md.
Both are live recovery indexes that root had updated after the candidate
decisions. The other 13 FOSP inputs matched the working files. The review's
original pins are preserved rather than changed to today's index bytes.

Root retrieved these two exact Git objects from the private mirror:

```
34d136cd8301448f2cc5d9d52f395e59a28c5b5f:SYMBOLIC_DYNAMICS_STATE.md
34d136cd8301448f2cc5d9d52f395e59a28c5b5f:docs/papers197_201_sequence/PIPELINE_STATE.md
```

Their SHA-256 values respectively match the original review pins:

```
ae6b68f9792b71f1041cb12b303d4b57b6e799d2379d8c904ed2d72bca3d1f89
2a80b360d71059e0e82882a97f485eed5fbcd41b19d473f1413baa6a522cbb2c
```

All inputs for the other three packages matched current working bytes.
This is an explicit immutable-Git resolution for historical context, not a
waiver for changed theorem inputs or permission to rewrite accepted review
versions. Future replay should use the named Git bytes for these two index
pins. The FOSP source supplement is separately pinned by DELTA_ACCEPTANCE.md.
