# Self-check protocol

**Status:** `PASS / HOLD_EXTERNAL`.

The evidence is deterministic and uses only Python's standard library.

1. `verify_combinatorial_lane.py` exhausts the declared finite boxes for all
   twelve literal systems.  Its strongest checks compare literal PDD/RCS
   iteration against separately implemented all-time formulas, pointwise
   clocks, image criteria, and target-wise fibre counts.
2. `self_check.py` launches the verifier in **two fresh Python processes**.
   It requires both stdout byte streams to equal one another and the frozen
   `CANONICAL.txt`; any stderr is a failure.
3. It parses `SHA256SUMS`, requires exactly the documented lane files,
   excludes the manifest from hashing itself, and recomputes each digest.

The primary replay performs **23,150,803 explicit assertion calls**.  It
covers all `n^n` PDD words through `n=7`, all RCS subsets through `n=18`, all
DSR permutations through `S_9`, and the exact boxes declared in the
scout-and-kill ledger for the other nine systems.  No random sample
contributes to the count.

These finite checks support the written proofs but do not replace the
unbounded arguments.  They are not novelty or external-release evidence.

The sealed replay reports:

```text
P182_186_COMBINATORIAL_SELF_CHECK
fresh_runs=2
canonical_bytes=1279
canonical_sha256=ed5c9618a2a9b485c29bbf7e84a60e114312c8bd7c2b8d9c22adb9b99b4addad
manifest_entries=11
checks=16
RESULT=PASS
```

## Scope hygiene

- Only `docs/papers182_186_sequence/scouting/combinatorial_lane/` is written.
- No `papers/` manuscript or PDF is edited.
- No candidate is assigned P182--P186 in Stage 1.
- DSR remains reserve because its general clock and inverse are open.
- Direct and adjacent RGF/subset-transform owners are disclosed even where
  the literal iterative conjunction was not found.
