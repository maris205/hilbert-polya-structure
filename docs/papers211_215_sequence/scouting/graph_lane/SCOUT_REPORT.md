# Initial graph lane — compact closed slate

2026-09-08 UTC. **FOUR_PROPOSALS / ONE_TINY_PILOT / NO_PROMOTION /
ZERO_RESERVES / ZERO_PAPER_IDS / HOLD_EXTERNAL**.
Author and proof contributor: `/root/round211_graph_scout`.

| Literal | Proved all-parameter result | Independent-axis boundary | Disposition |
|---|---|---|---|
| CBF: $G\mapsto K_n\setminus B(G)$ | Complete recurrent classification; sharp height $0$ for $n\le2$, $1$ at $n=3$, $3$ for $n\ge4$; extra six $P_4$ complement cycles only at $n=4$; unique $K_n$ core for $n\ge5$ | Image exactly complements of forests; full prescribed-bridge/block-partition fibre sum; unique maximum target $K_n$ for $n\ge3$. This is classical bridge decomposition with which datum is fixed exchanged. | `MATH_CLOSED / VALUE_THIN_SHORT_IMAGE_CORE / NO_PROMOTION` |
| ZFW: retain only the newly forced white vertices | $W^2(S)\subseteq S$; complete matching-cut recurrent criterion; height at most $n$; exact reciprocal-pair intake followed by fixed Boolean erosion | On connected graphs, unique global maximum empty fibre $2^n-n$ at $K_n$; nonempty maximum $2^{n-1}-1$ at a star center, all equality cases. No sharp clock or full target census. | `KILL_FIXED_EROSION_ADAPTER / NO_PROMOTION` |
| MCS: lex-tied minimum-cut Seidel switch | Exact confinement to the classical cut-space switching class; preserved triangle parity | Only a generic inverse cut-candidate test; no evaluated fibres, full recurrent theorem or justified Lyapunov sign | `HOLD_PROOF / NO_PROMOTION` |
| CII: graph of chromatic implicit identities | Exact cluster-graph image; unique empty/complete two-cycle; sharp height two for $n\ge3$ | Bell image is static equivalence encoding; arbitrary-target inverse not closed | `KILL_CANONICAL_KERNEL_COLLAPSE / NO_PROMOTION` |

All four literal definitions, including degenerate orders, tie rules and
ZFW's discarded old black set, are in [INTAKE](INTAKE.md). Full deductive
arguments and explicit missing claims are in [PROOF_PACKAGE](PROOF_PACKAGE.md).
The [source/collision record](SOURCE_AND_COLLISION.md) identifies actual
internal proofs/code and directly read primary definitions. These local
handles are not four certified fresh independent mechanisms.

## Actual single-pilot result

Only CBF was executed, on every labelled simple graph for $n=0,\ldots,6$.
One native subprocess exited zero in 12.373431921005249 seconds with empty
stderr. It made 270,731 assertions over 33,868 states. The complete raw
stdout contains every source's successor, depth, period and indegree, plus
all box summaries; it is not an excerpt or normalized summary.

| $n$ | States | Image | Maximum depth | Maximum fibre |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 | 1 |
| 2 | 2 | 2 | 0 | 1 |
| 3 | 8 | 7 | 1 | 2 |
| 4 | 64 | 38 | 3 | 15 |
| 5 | 1,024 | 291 | 3 | 314 |
| 6 | 32,768 | 2,932 | 3 | 13,667 |

Producer: [pilot_cbf.py](pilot_cbf.py). The actual capture is
[execution_01/receipt.json](execution_01/receipt.json), with full
[stdout](execution_01/stdout.jsonl) and [stderr](execution_01/stderr.txt).
The stdout has 2,864,468 bytes and SHA-256
`07954320dc05b3180abb6f1a037e9f8f5f69990e0200a5f663a9e43f959d1770`.
The source, intake, relevant initial originals and executable were pinned
before and after and unchanged. The runtime record explicitly does not
capture full standard-library/dynamic-loader closure; this scout is **not**
a strict terminal replay or reusable manuscript-review execution. There was
no second run, no byte-comparison claim, no ZFW/MCS/CII pilot and no enlarged
cutoff. The finite census pressures the proofs but does not establish them.

The later [read-only artifact check](ARTIFACT_CHECK.json) actually exited
zero: 135,522 checks, 13 current historical input pins and every one of the
33,876 raw JSONL records verified. It ran [audit_artifacts.py](audit_artifacts.py),
not the scientific producer. No additional scientific execution is implied.
The first document-capture patch had a context mismatch; its failure and
the corrected context are disclosed in that receipt, with science unchanged.

## Handoff

No candidate admission, manuscript review or completed-paper claim follows.
All output is new and confined to this directory; no old manuscript,
accepted review, failed evidence, index or Git object was changed. CBF/ZFW
proof familiarity permanently disqualifies this author from independently
reviewing a resulting manuscript. Root integrates any lane reception.
