# Independent Stage-2 audit handoff

## Frozen handoff status

```text
HOLD_FOR_INDEPENDENT_STAGE2_AUDIT
```

The auditor is asked to decide only whether the frozen theorem contract is
proved and correctly implemented.  No manuscript, numbering, installation,
priority, or broader reducible theorem is in scope.

## Audit order

1. Verify the immutable Stage-1 manifest hash and all entries recorded in
   `SOURCE_LOCK.md`.
2. Run `python -B verify_manifest.py` before regenerating anything.
3. Read `THEOREM_CONTRACT.md` and confirm that all hypotheses are typed:
   complete phase blocks, positive `a_j`, strict finite transience, exact
   composition totals, and unrestricted phase access only where declared.
4. Audit `PROOF_PACKAGE.md` in dependency order.
5. Run `python -B run_validation.py` twice and compare the five evidence
   hashes with `STAGE2_REPORT.md`.
6. Run `python -B build_manifest.py`, then `python -B verify_manifest.py`
   and `sha256sum -c SHA256SUMS.txt`.

## Proof checkpoints

- **C0:** Verify both liminf directions and the inequality for every
  discrete ball-radius interval; do not accept uniformity alone as a lower
  bound.
- **C1:** Check the backward index in `H_j` and the limit along every depth
  residue.
- **C2:** Check the exact feeder prefix count, the factor from
  `d|Delta_(n-1)|/|Delta_n|`, and the finite-union step.
- **C3:** Check that mean equality forces every residue equal and that the
  geometric circular kernel has no zero Fourier multiplier.
- **C4:** Check that necessity uses every nonzero Fourier mode of `c`; run
  the `p=4,d=2` counterexample before accepting any divisibility wording.
- **C5:** Check the `Delta=0` boundary separately from even/odd parity.
- **C6:** Check the exact denominator `d^L`, the embedding `m -> d m`, the
  balanced integer construction, the `O(d^(-L))` bound, and the general
  finite-`L` constant-convolution iff.
- **C7:** Check the displayed state order and adjacency directly; the proof
  must not invoke a BLW upper bound.

## Implementation checkpoints

- Confirm that `formula_engine.py` and `prefix_engine.py` import neither one
  another nor a shared mathematical implementation.
- Confirm that exact equality uses rational prime-log forms.
- Confirm that optimizer ordering clears rational denominators and compares
  exact integers; decimal evaluation is used only for serialized diagnostics.
- Recompute the actual recursive integer counts independently of the closed
  `H_j` formulas.
- Confirm exact enumeration totals and canonical stream digests.
- Confirm that all six mutation controls pass for the intended reason.

## Immediate STOP conditions

Return `STOP_STAGE2_DEFECT` if any of the following occurs:

1. a theorem equality needs a BLW primitive/equality clause;
2. a residue index or `d^L` denominator mismatch is found;
3. the saturation proof silently upgrades sufficiency to necessity without
   Fourier support;
4. the four-state dimension is not exactly `log(2)/2` for the full shift and
   `log(2)/3` for its cyclic core;
5. either implementation imports the other or an exact identity depends on
   decimal tolerance;
6. a canonical evidence hash changes on a clean deterministic rerun;
7. the manifest, cache, symbolic-link, regular-file, or immutable-input check
   fails;
8. any non-transient or incomplete-block claim is needed to complete C0--C7.

If none fires and every proof checkpoint passes, the appropriate response is
an independent Stage-2 audit receipt.  This handoff itself does not advance
the status beyond

```text
HOLD_FOR_INDEPENDENT_STAGE2_AUDIT
```
