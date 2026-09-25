# CS08 fixed-winner repair — independent implementation review

Scope: `ASFS-DISCOVERY-20260919-CS08`; execution: `CS08-REPAIR-FIXED-01`.
Reviewed 2026-09-18T23:35:57Z; research label 2026-09-19.
Status: `ANALYZED — STATIC REVIEW + EXECUTED NONNUMERICAL LOGGER TESTS`.
Decision: no blocking defect found in the reviewed frozen repair implementation.
This is not a numerical-run certificate or an independent reproduction of the search.

## Frozen sources and method

Read all 507 lines of [resume_fixed.py](../resume_fixed.py), the complete
[repair card](../repair-execution-card.md), original candidate contract, and
the reused propagation/readout/state/static/comparison helpers.

| Input | SHA256 |
| --- | --- |
| `resume_fixed.py` | `94e8f9a0a6435ad86f8bbe159782cd0a5fe6763e985f33c4da64e59154c8c1ce` |
| `repair-execution-card.md` | `c7a8c6fab098225e89b5da7c06957567e0be6bc047e7ecd61e8295cbefc5d83a` |
| `repair-input-locks.json` | `fe8c4cbb2a7b7fac5be90a2653d58191431b79e5c3f466f04d8a6c5c71dec397` |
| original `run_search.py` | `4c8a52f7b5f57519d09ef241e0a3c7e7633f35848b957857d1fc10bee05db763` |
| original winner identity | `5e28a599e29e1032b27f35ae91d81c362378d0c268cbb37c8a4d3ba58028583f` |
| failed-run inventory | `c4886ca3c58935ae1fcc2d2c3c1546a3335ec50d27e60d4a7a5545ae1091bf77` |

Executed `PYTHONDONTWRITEBYTECODE=1 python -` with an AST-only harness:
parse the exact SHA-bound source; compile only `utc`, `make_logger`, and
`logger_regression_test`; supply standard-library globals and forbidden
scientific/main-entry sentinels. Neither entire module nor either old runner
was imported. Separately AST-extracted only `sha` and `verify_inputs` for
read-only hashing: **34 repair locks, 16 original locks, and all 815 original
file memberships/sizes/SHA256 matched**. `run-2-fixed` was absent.
No forward, SVD/eigh, root solve, optimization, target generation, or scientific
array calculation was executed. No saved development targets were parsed.

## Actual logger regression, not inference from syntax

The source's four-case `logger_regression_test()` passed. An independent
StringIO stream additionally executed these exact historical keyword shapes
using inert metadata fixtures:

```python
event("winner_state_readout_start", name="winner-B-N511", not_a_propagation=True)
event("winner_state_readout_complete", name="winner-B-N511", counters={"fixture": 1})
event("propagation_start", stage="postfreeze", name="post-Q-N1023", form="Q",
      theta=[0, 0, 0, 0], N=1023, L=8.0, B=64, counters={"fixture": 1})
event("propagation_complete", stage="postfreeze", name="post-Q-N1023",
      status="VALID", counters={"fixture": 1})
```

All four JSON records retained the correct independent `event` and `name`,
including stage and other metadata; all UTC timestamps parsed with zero offset.
Both `event("x", event="override")` and `event("x", utc="override")` raised
`ValueError`, leaving the stream unchanged. Scientific-entry sentinel calls: 0.
The logger uses positional-only `event_type`, so `name=` cannot collide.
All 17 syntactic `event(...)` call sites were inspected; none passes reserved
`event`/`utc` metadata. The real runner repeats its own logger test before I/O
creation and saves `logger-regression.json` if subsequently launched.

## Fixed object, budget, and freeze ordering

- Lines 225–232 enforce the original scope, exact five member IDs and fixed Q
  primary, then save the original winner identity bytes. Manifest and training
  freeze both retain original/copy SHA; completion also compares them.
- Lines 317–371 perform precisely B/O/Q/U/D × N511/N639: 10 new reconstruction
  propagations, each one full SVD and one static readout. Lines 422–426 add the
  ten prescribed N1023/N1279 roles plus Q N1279/L8/B128 and N1599/L10/B64.
  Thus the sole path is 22 forwards, 22 full SVDs, 22 static readouts; zero
  optimizer calls and zero extra sigma-only decompositions or control reruns.
- The single syntactic SVD call uses `full_matrices=True`. The reused static
  helper has one full `eigh`, saves full H/all eigenvalues/first 320 states,
  and does not optimize. Separate attempted/completed counters increment
  around completed calls; helper root/eigh attempts are labelled separately.
- Reconstruction theta comes only from the frozen identity. Exact checks
  cover theta/form/N/L/B/beta, q/p/k, midpoint/schedule, W/meanW, minima and
  minimizers. Original readout/mask/validity are recalculated from original
  sigma and compared exactly. New minimum IDs have their own ledger; old IDs
  and their old-ledger path remain separately labelled.
- New full sigma must differ by at most 1e-12 and yield a valid reconstruction.
  New E/mask/prediction/scale are saved under `reconstruction_*`; all canonical
  selection sigma/E/mask/prediction/scale are copied back from run-1. No extra
  tail-energy gate, clipping, ranking change, or development reselection occurs.
- `add_states` then uses canonical original sigma for left/right equations and
  full-spectrum Frobenius moments. Full C and first 320 left/right states are
  saved; partial states are explicitly not a complete reconstruction.
- All ten heat NPZ/JSON and ten static NPZ/JSON files are saved and hashed
  before `training-arrays-frozen.json` and its hash event. Only then, at line
  387, are 101–320 ordinates parsed. Earlier input byte hashing is not a
  development fit. Old S0047 is loaded later solely as a fixed comparator.
- All five forms receive the four prescribed fit/G windows; Q receives fixed
  time/box comparisons, strict G<2% and each object's own E0 scale. Ordinary
  postcheck INVALID preserves evidence and makes linked comparisons
  unassessable; it does not change the primary or add a role.
- Locked helpers are imported under non-main names; no old `main`, optimizer,
  `forward`, or ranking routine is called and no old module global is changed.
  Input locks and the complete original inventory are checked at start and
  successful completion; implementation/consistency exceptions stop without retry.

## Operational and evidentiary limits

Exclusive new-output creation and per-write 1 GiB guard were inspected,
including event/root streams. Single-thread BLAS and 600s+10s termination
depend on the frozen external launch command; this review did not launch it.
If a run fails before final verification, its failure event may have
`end_verification=null`; the saved-result audit must recheck locks/inventory.
Failure/timeout behavior and numerical INVALID branches were not rehearsed.
The original static review missed the logger collision; it is preserved,
not retroactively replaced by this repair review. Its SHA remains
`5790b61aac65720ea66f6ac1b2b5621ee9f433be64d87655ca96b843dde57da3`;
the failed-run saved review remains
`2f3543c9e4833cfbd29ce7c1f866328e236316169794930e4ad341fb07552d25`.

ARS validation/reproducibility discipline was applied: distinguish the actual
logger tests from static analysis and unrun numerics; retain failure and all
fixed roles. The 11-fallacy screen is scoped accordingly: no p-values, causal
effects, population estimates, or infinite convergence claims are made;
supervised historical development data are not a blind validation set.
Remaining numerical status: `CANNOT_VERIFY — NOT_RERUN` before execution.
Same-object identity is intact in code; successful finite recovery would not
prove endogenous arithmetic, an infinite spectrum, or a Route result.
A0/A1/A2/T0–T3 not evaluated; formal `UNASSIGNED`; B `NOT INVOKED`.
Next allowed decision: the already authorized single fixed repair execution,
followed by saved-evidence review; any failure stops without automatic retry.
