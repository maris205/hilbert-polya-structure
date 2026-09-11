# KIP: exactly one bounded author pilot, with preserved runtime-audit failure

2026-09-08 UTC. **Science observations: all seven preregistered categories
passed in the sole authorized invocation. Strict observed-runtime prelock:
FAIL, preserved.** This is not paper admission, independent review,
novelty certification, a manuscript build, or a strict reusable replay.

## Result and exact scope

The original native child ran once for `n = 1,...,7`, covering all 2,353
nondecreasing maps, with 14,523 assertions. Its native exit was 0,
elapsed time 0.225527812 seconds, timeout false, stdout 731379 bytes,
and stderr 0 bytes. The 98 physically frozen input rows matched before and
after. These facts are recorded by `execution_01/NATIVE_RECEIPT.json`,
not inferred from this handoff. No science was rerun after that invocation.

| n | states | first-image states | fixed = recurrent | maximum observed height |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 |
| 2 | 3 | 2 | 2 | 1 |
| 3 | 10 | 5 | 4 | 2 |
| 4 | 35 | 13 | 8 | 2 |
| 5 | 126 | 34 | 16 | 3 |
| 6 | 462 | 89 | 32 | 3 |
| 7 | 1716 | 233 | 64 | 4 |

The seven assertion counts are: literal closure 2360; recurrence and
terminal state 2360; pointwise and sharp height 2360; complete first image
2353; every predecessor 2353; Laurent fibres and mass 2360; exact endpoint
peeling 377. Full canonical per-source rows and both observed and decoded
predecessor lists are retained in `execution_01/stdout.jsonl`.

Maximum-fibre summaries are descriptive only. They observe maximum
`2^(n-1)` uniquely at the constant-n target in these seven finite boxes;
there is no preregistered maximum-fibre assertion or all-n extremal theorem
in this pilot. Do not convert the observed pattern into a proved claim.

## Mathematics and attribution boundary

The unchanged author derivations and pre-pilot contract are the separately
sealed `../finite_semigroup_lane/PROOF_PACKAGE.md` and
`../finite_semigroup_lane/PREPILOT_CONTRACT.md`. Their complete sealed
package, including the manifest, is physically retained under `lock/desk/`.
The pilot evaluates exactly the prescribed map
`T(f) = e_X composed with e_(Y union {n})` on the full order-preserving
transformation carrier, and the prescribed target-gap inverse decoder.
Same-author literal and formula implementations are not independent review.

Root and the independent gate subsequently reported that Stein's
arXiv:2404.08075v2, Section 5.1, paragraph after Lemma 5.12, explicitly
owns the support balance `|A|-|X| in {0,1}` and unique support-pair
reconstruction. That published material must be credited and subtracted
in any later manuscript. Candidate novelty must be assessed only for the
target-gap inverse factorization and exact recomputed dynamics, not for
the underlying support coordinates or balance/reconstruction. The old
sealed desk was not rewritten to incorporate this later source finding;
the source-only reviewer/root records are authoritative for that audit.

No all-carrier conjugacy exclusion follows merely from the endpoint
peeling interpretation. Conversely, a generic deletion mechanism alone
does not constitute a proof of equivalence with an old paper. Final
novelty/value/admission judgments remain with the independent gate/root.

## Preserved audit failure and exact scope of diagnosis

The original frozen `lock/audit.py` failed after science, at the first
unfrozen observed runtime path. It has not been modified. A complete
posthoc comparison finds **two launcher-only** paths missing from the
original pre-execution pins:

1. `/usr/lib/locale/C.utf8/LC_CTYPE`.
2. `/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache`.

The launcher observed 54 runtime files. The scientific child observed 38
and the preflight import probe 52; all files in those latter two observed
sets match the original prelock. Observed-set agreement is not a claim
that dependencies were exhaustively captured. Original child/probe locale
settings were explicitly `LANG=C, LC_ALL=C`. The launcher inherited its
environment, but its contemporaneous environment values were not recorded.
Its saved mapped-file observation localizes the miss; it does not justify
reconstructing exact original locale-variable values after the fact.

`FAILED_ARTIFACT_ATTEMPTS.md` preserves truthful descriptions of both the
initial frozen audit failure and the first posthoc diagnostic's own
failed one-missing-file assumption. The latter source remains unchanged
as `artifact_closeout.py`. Neither of those initial interactive failures
is mislabelled as a retrospectively captured native receipt.

`artifact_closeout_v2.py collect` performed a NEW read-only invocation of
the original frozen audit, under an explicitly recorded C locale. It
again returned native exit 1, stdout 0 bytes, stderr 535 bytes, because
the audit checks the original receipt and retains the same LC_CTYPE
failure. Those actual bytes and native metadata are stored under
`postrun_diagnostic_v2/`. This command made zero scientific invocations.

No old input list was repaired, no absent runtime file was added to the
old freeze, and no scientific or canonical output was overwritten.
A future strict manuscript verification would need a separately
pre-frozen corrected runtime and separately authorized fresh execution;
that is outside this one-pilot authorization.

## Read-only archive verification

After the complete nonself manifest is sealed, the following command
verifies payload bytes, native stream bindings, old/frozen desk identity,
unchanged input pins, the recorded whole reverse-edge relation, counts,
and the complete two-path diagnosis without running science or the audit:

```sh
/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/scouting/finite_semigroup_pilot/artifact_closeout_v2.py verify
```

Its scope is archive integrity only, and its output deliberately retains
`strict_runtime_prelock_status: FAIL_PRESERVED`. It does not replace or
relax the original `lock/audit.py audit`, which remains failed. An
archive-integrity success must not be described as a blanket verifier pass.

The final complete `MANIFEST.json` excludes only itself. Its payload count
and byte total are machine-computed at sealing. The historical desk still
has its original 39 payloads / 519632 bytes. No central state, historical
manuscript, review, repository mirror, or Git path was edited by this task.
External release/contact/upload remains HOLD_EXTERNAL.
