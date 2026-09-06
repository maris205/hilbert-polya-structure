# Fourteenth bounded handoff — NO_PROMOTION

Date: 2026-09-06 UTC. Author: `batch197_fifth_scout`.
Six literal maps on four carrier types were fixed in [intake](INTAKE.md).
Only SNC, RCI and RRM were executed, in exactly the original **12 complete
boxes / 155,707 states per run**. DCS, TLS and DPM were killed analytically
before code. All six close **NO_PROMOTION**, with no reserve, paper number,
manuscript, independent gate or automatic next slate.

## Exact finite census

Here `length:count` counts cycles, not periodic states. H is maximum entrance
time. Every maximum-fibre target in the table is unique. Matrix and magma
encodings are row-major base-p/base-n; point subsets use lexicographic point
indices as binary bit positions. The SNC sink is encoded after all matrices.

| Rule / full box | States | Image | Core | Cycle length:count | H | Maximum fibre / target |
|---|---:|---:|---:|---|---:|---|
| SNC 2x3, p=5 | 15,626 | 110 | 32 | 1:32 | 3 | 10,426 / sink 15,625 |
| SNC 2x3, p=7 | 117,650 | 320 | 86 | 1:56, 2:15 | 4 | 62,966 / sink 117,649 |
| RCI p=3, d=0 | 2 | 1 | 1 | 1:1 | 1 | 2 / empty |
| RCI p=3, d=1 | 8 | 4 | 4 | 1:4 | 1 | 5 / empty |
| RCI p=3, d=2 | 512 | 202 | 100 | 1:100 | 2 | 179 / empty |
| RCI p=5, d=1 | 32 | 16 | 16 | 1:16 | 1 | 7 / empty |
| RCI p=7, d=1 | 128 | 64 | 64 | 1:36, 2:14 | 1 | 9 / empty |
| RCI p=11, d=1 | 2,048 | 804 | 694 | 1:100, 2:143, 20:11, 22:4 | 2 | 13 / empty |
| RRM n=0 | 1 | 1 | 1 | 1:1 | 0 | 1 / empty table |
| RRM n=1 | 1 | 1 | 1 | 1:1 | 0 | 1 / table 0 |
| RRM n=2 | 16 | 9 | 5 | 1:5 | 2 | 5 / left projection 3 |
| RRM n=3 | 19,683 | 5,096 | 256 | 1:174, 2:41 | 6 | 136 / left projection 377 |

The complete canonical additionally records image chains, mapping digests,
longest cycles and maximal-tail witnesses. It is the unmodified full stdout,
not a summary generated after execution.

## Theorem-level progress and exact failure boundaries

- **SNC:** [proof §1](PROOF_AND_DISPOSITION.md) evaluates the sink fibre for
  every two-row width c>=2 and odd prime p not dividing 2c, and proves it
  is the unique maximum. Every nonsink fibre is an exact torus-linear-system
  count times `(p-1)^2`; that remaining count is not called an evaluated
  all-target atlas. Row/column scaling, the scalar chart and static margin
  counting are deducted. The observed two-cycle at p=7 and tails 3/4 do not
  supply a prime-uniform core or a new exact clock.
- **RCI:** [proof §2](PROOF_AND_DISPOSITION.md) proves the unique empty-target
  maximum `v + sum_(p divides j) binom(v,j)` in dimensions 0, 1 (odd p)
  and 2 (p=3 mod 4). In particular the line maximum is p+2. The exact
  nonempty inverse constraint reconstructs a source from its centroid and
  optional centre point. On the line its derivative-root statistic is
  literally the cardinality of the older CRS output, as documented in the
  [collision report](SOURCE_AND_COLLISION.md). No all-target closed root
  enumeration is claimed. Fixed-centre involutivity is deducted; the actual
  p=11 box has periods 20 and 22 and no uniform temporal classification is
  proved. Isotropic forms are outside this inverse theorem, without changing
  the original literal definition.
- **RRM:** [proof §3](PROOF_AND_DISPOSITION.md) preserves the n=3 two-cycle
  and six-step tail. Analytically, the already deducted leftoid slice on
  Z/5 has the exact four-cycle `mu_a(x,y)=x+a`, with a=1,2,4,3. This is
  not an n=5 execution or a new retained mechanism. The finite 136 return-law
  count at n=3 does not prove an all-n maximum or recurrent atlas.
- **DCS / TLS / DPM:** the complete intake arguments are respectively
  metabelian commutator collapse, characteristic-three line-sum erasure and
  exact unary-power pullback. Each is a zero-credit temporal adapter, with
  zero executions. The excluded P175 and crossed Bin(X)-square proposals
  are not seventh/eighth candidates and were never executed.

## Actual execution and preservation

The [initial actual pair](execution_pair_v1/PAIR_RECEIPT.json) ran
`/root/miniconda3/bin/python -I -B .../pilot.py` twice, each in a distinct
new empty output directory. Both exited 0 with **474,763 assertions**;
all three declared input hashes remained unchanged. An actual `cmp`
returned 0, and the recorder independently compared complete raw bytes.
Both raw stdout hashes are
`56ecdf1f21342c9c6ea0d0802c1ce8d0839efcb052e8188b5ed4a603e65a55ea`.
The pilot has direct/alternative rule identities plus independent image-chain
and functional-graph consistency checks. Its census structure was adapted
from the author's twelfth pilot; this is disclosed reuse, not cold review.

After the inverse proofs were written, a distinct self-contained
[inverse checker](inverse_check.py) recomputed SNC and RCI mappings and
compared every target fibre with (S1)–(S2), (I1)–(I3), their bounds and
unique maxima. It imports no scientific code. RCI forward inversion is
reconstructed by solving the defining equation over all original points;
the line derivative check uses the direct product rule, not reciprocals.
Original canonical data is read only for digest/census comparison.

The [new inverse pair](inverse_pair_v1/PAIR_RECEIPT.json) used exactly the
**eight original SNC/RCI boxes / 136,006 states**, not enlarged cutoffs and
not an extra rule. Each fresh isolated process exited 0 with **371,638
assertions**. Nine before/after input pins, including both original raw
outputs and the written proof, were unchanged; actual raw `cmp` returned 0.
Both complete stdout hashes are
`1c33f00dbee59d26a0e05ecd8fc17333474df11acc1dac8ef16a3b3f2e43f2e3`.
Every recomputed mapping digest agrees with the original full-box digest.
Both pairs preserve actual commands, runtime probes, stdout, stderr,
exit statuses, elapsed times and input pins. Assertion optimization is zero,
isolation is one and bytecode writing is disabled. No failed producer run,
numerical repair or deleted execution exists in this slate.

These are author execution pairs in separate processes, not process-separated
review by a noncontributor. The inverse proof is a genuine mathematical
addition and therefore received new affected checks; original intake,
producers, output directories and receipts remained unchanged.

## Handoff and seal interpretation

The package's `SHA256SUMS` is complete and directory-relative, excluding
itself. `CONTEXT_INPUTS.sha256` is workspace-root-relative and pins the
eleven selected historical/provenance files identified in the source report.
Initial execution pins cover three immutable sources; inverse execution
pins cover nine. Historical pins do not claim newly replayed old experiments,
and web URLs/read scopes are not claimed as frozen local web copies.

The only writes were inside this owned fourteenth directory. No central
state, Git, historical manuscript, accepted review, OFS/P208 evidence or
other scout directory was changed. Root must inspect originals and decide
central integration. All scientific, source and allocation limitations
remain explicit: **NO_PROMOTION / HOLD_EXTERNAL**.
