# Official Validation Report

Verdict: `PASS_WITH_FROZEN_FINITE_ABSENCE_AND_OPEN_ALL_PERIOD_EQUALITY`

## Validation scope

This P5 audit validates the provenance, one-shot lifecycle, exact-period
semantics, dual-engine agreement, controls, and stated classification of the
frozen registered artifacts. It does not independently re-prove the proof
package, rerun the candidate, add periods, or promote finite evidence to an
all-period theorem.

## Artifact and lifecycle chain

| Artifact or binding | Validated state | SHA-256 |
|---|---|---|
| `experiments/source_lock.json` | source lock v2, frozen `n=2,...,7` | `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1` |
| `notes/PROOF_PACKAGE.md` | provable as stated; equality open for `n>=4` | `9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9` |
| reviewed code tree | Round-4 independent deployment pass | `7a5ea42ea52d35bf4d6608b1175a43ab81ceaa9ed8fbfd0e35e183920dbdd27a` |
| `results/CODE_REVIEW.md` | exactly one V4 pass after preserved V1--V3 failures | `ac8bc40bc863613260486106ef7d46ea0370bea326019de1b3b1a83d488c6109` |
| `results/PRE_EXECUTION_AUDIT.json` | `AUTHORIZED_FOR_REGISTERED_EXECUTION` | `2d8580805f57168a7cfcc3eeb8ae4a7f4c036d5222bea8a2d7f7a71b6152c948` |
| `results/registered_run.claim.json` | immutable `STARTED`, count 1 | `b118f2ae60e3317a45d026ac004997e6629bef35ae5c133f441a2af6a1202ed0` |
| `results/EXPERIMENT_RESULTS.json` | all frozen periods complete, no hit | `847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6` |
| `results/registered_run.json` | `COMPLETED_NO_HIT` | `06215794b323552bc953c3ea8935d76c15b205bc7df13c170e448c0562b0b7b9` |
| `results/pytest.xml` | 38 tests; 0 failures/errors/skips | `4e38e3197ec588edceac43c8292630a61f018f4f03f36bb3c8606723bbd0f237` |
| `results/result_manifest.json` | manifest v2 `pass=true` | `6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8` |

The claim and terminal ledger agree on candidate id, source-lock hash,
reviewed-tree hash, review-file hash, pre-execution audit hash, target set,
registered period set, run id, and registered-run count. The terminal ledger
binds the result artifact hash and records all six periods as both started and
completed, with no stopped period or failure code.

## Gate validation

| Gate | Result | Evidence boundary |
|---|---|---|
| Source lock and upstream bindings | PASS | Frozen lock plus all four upstream hashes matched. |
| Executable isolation | PASS | Closed-world inventory and static scanner reported no forbidden access. |
| Proof contract | PASS | Frozen identities and scope markers matched the proof package; this is not a substitute for the proofs. |
| Controls | PASS | Both equality signs, a negative target, exact-period pollution, and upstream semantics were exercised. |
| Independent deployment review | PASS | Round 4 is bound to the executed code tree and source lock; V1--V3 failure history is preserved. |
| Registered lifecycle | PASS | Exactly one immutable claim and one terminal `COMPLETED_NO_HIT` ledger exist. |
| Tests | PASS | JUnit reports 38 tests and zero failures, errors, or skips. |
| Strict result manifest | PASS | No missing, unsafe, extra, nested, symlink, unsupported, or semantic-error entry is recorded. |

## Scientific validation checks

1. The exact-period object in every candidate record is the frozen monic
   radical/set-difference component, not an uncertified formal-dynatomic
   substitute. All six components are squarefree, have degrees divisible by
   their periods, and give integer cycle counts `1,2,3,6,9,18`.
2. The normalized cycle product is invariant modulo every exact-period
   component.
3. For each of twelve sign/period pairs, the gcd engine returns the constant
   polynomial one, the independently reduced target resultant has nonzero
   exact rational field norm, and `gcd_resultant_norm_agree=true`.
4. No target hit occurred, so there is no extraction certificate and no
   target-triggered early halt. All predeclared periods completed.
5. The finite result is disclosed as development-seen reproduction because
   periods 2--7 were seen before lock. `new_blind_periods=[]` and no hidden
   validation/test claim is permitted.

## Evidence-versus-inference decision matrix

| Statement | Basis | Decision |
|---|---|---|
| `w(Lambda_C)=n*w(2)` for all exact `n>=2` | Theorems A--B | `EXACT_2ADIC_VALUATION_ALL_PERIODS_CERTIFIED_BY_PROOF` |
| `B_C!=+/-1` at `n=2,3` | Lemma D local obstruction | `BASE2_EQUALITY_ABSENT_N2_N3_BY_LOCAL_THEOREM` |
| `B_C!=+/-1` for frozen `n=2,...,7` records | Twelve agreeing exact target certificates | `BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN` |
| `B_C!=+/-1` for every `n>=4` | Neither proof nor finite ledger suffices | `BASE2_EQUALITY_ALL_PERIODS_OPEN_N_GE_4` |
| Route status | Frozen scope | `ROUTE_A_NOT_ADVANCED / ROUTE_B_NOT_OPENED` |

The exact 2-adic valuation theorem concerns local valuation. It does not by
itself exclude rational equality `Lambda_C=+/-2^n`. Likewise, the rational
equality audit does not decide modulus-only equality or
characteristic-exponent equality.

## Integrity and prohibited-data declaration

- No blind periods were present and no post-null period was added.
- No candidate numerical run was performed; the official run used exact
  symbolic arithmetic only.
- No approximate orbit matching, parameter fitting, sign selection, or cutoff
  selection was performed.
- No external prime table, Riemann-zero data, or network resource was
  accessed by the registered run or P5 analysis.
- The manifest was treated as immutable during P5. A read-only post-write
  verification reconfirmed `pass=true`, empty `missing`, `unsafe`, and
  `semantic_errors`, passing result-tree closure, and equality of every
  listed file hash.

## Closure and next step

P5 is complete. There is no further candidate experiment authorized by this
source lock. The scientifically meaningful continuation is proof work on the
`n>=4` equality residue, especially stronger constraints on the unramified
norm or the cycle-polynomial special values. Any new computation must be a
separately source-locked project and must not retroactively create a blind
period here.

