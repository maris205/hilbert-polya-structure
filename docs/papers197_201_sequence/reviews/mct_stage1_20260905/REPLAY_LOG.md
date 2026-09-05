# Independent MCT exact replay receipt

Two fresh processes ran the final verifier, after an initial falsifier and
an expanded exploratory run. Only the two fresh final runs below constitute
the final reproducibility receipt. No author or temporal-pressure code was
read, imported, or invoked by this verifier.

Command for both:

```sh
python3 -B -u docs/papers197_201_sequence/reviews/mct_stage1_20260905/verify_independent.py
```

- **Replay 1:** process launched after the UTC clock reading
  `2026-09-05 07:31:39 UTC`; exit code 0 and complete output observed by
  `2026-09-05 07:32:21 UTC`. Raw stdout is `REPLAY1.txt`.
- **Replay 2:** process launched after the UTC clock reading
  `2026-09-05 07:32:55 UTC`; exit code 0 and complete output observed by
  `2026-09-05 07:37:18 UTC`. Raw stdout is `REPLAY2.txt`.

These are orchestration observation bounds, **not measured process running
times**; other audit work occurred before completion polling. Both were
new actual processes. Captured output was saved verbatim with apply_patch,
then checked using both exact string equality and the shell `cmp` command.
The outputs are **byte-identical**, and `CANONICAL.txt` is the same byte
sequence, not a hand-written table or reconstructed summary.

Final verifier SHA-256:

`d2b69d2991681ff3105ccd90d9a5ed0930808ebe005e447a90de3ccce3f39013`

SHA-256 shared by Replay 1, Replay 2, and CANONICAL:

`feaaf94a5f68857cf897563a77308934c7bc6ab4ac12ce5added722e1abe5c19`

Each run performs **1,383,555 assertions**. It exhausts the full carriers
for $n=0,\ldots,6$, totalling **33,868 MCT states**. The Q01 historical
control is separately computed for $n=3,\ldots,6$ and is not counted as a
new candidate. The sharp temporal family is directly run for $n=3$ through
$80$; both explicit inverse witness families and both colours are checked
for $n=4$ through $24$. There is no full $n=7$ enumeration, sampling
claim, extrapolation, or use of finite runs as an all-parameter proof.

## Implementation separation

| Evidence producer | Literal representation | Actual temporal graph control | Inverse control |
|---|---|---|---|
| Frozen author, as disclosed by author | Lex-edge integer masks plus a dense matrix control | Direct per-state orbit dictionaries | Undo target triangles, check earlier selectors; D/C and local certificates |
| Frozen temporal collaborator, as disclosed by collaborator | Tuple-edge sets | Indegree peeling | No inverse claims |
| This gate, code personally implemented | Symmetric row strings; integer indices only enumerate/store states | Generic Kosaraju SCC discovery, then reverse BFS from the discovered cycle states | Target forbidden-equality clauses without running a source selector; separate simultaneous star/top certificates |

The gate compares every actual incoming source set against its target-only
reconstruction, including empty fibres and fixed targets. It verifies the
iff for **every potential star and every four-set**, not just maximizers;
then checks all maximum-fibre equivalences. Actual SCC distances test exact
entrance time, periods, strict-trace no-return, root zero after one move,
and the sharp maximum. The graph-degree parity check is an old invariant,
included only as a literal-update sanity check.

Canonical `status=PASS` and zero severity counts describe failed finite
assertions, not a universal proof or literature clearance. The separate
gate report contains the provenance finding and its disposition.

## Finite silhouettes for root replays

At $n=4,5,6$, the images have sizes $46,594,19034$, respectively.
The depth distributions are $(46,18)$, $(544,424,56)$, and
$(17740,13620,1362,46)$. Maximum-fibre target counts are $2,26,418$.
At $n=6$ there are 158 certified-star targets and 260 certified-top
targets, with no overlap. These are verified finite observations only;
no general census formula is asserted.

No manuscript exists in this gate, so PDF compilation and page-viewing QA
are not applicable here. Later paper Review A/B and physical cold builds
are not replaced by this candidate check. HOLD_EXTERNAL was maintained.
