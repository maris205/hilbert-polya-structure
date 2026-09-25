# Batch Z mechanical verification — strict PASS

Batch: `PRE-P0-STRUCTURE-20260925-Z`; exactly 475–479, no 480.
Context date: 2026-09-25, not independently established chronology.
Review calibration: `NOT_CALIBRATED`.

## Actual strict result and authority

**PASS — the first authorized strict execution exited 0 with pending: [].**
Root supplied DISTINCT FINALREADY after reporting all five final reviews
fully read, all final scientific surfaces frozen and all evidence receipts
integrated. Those personal scientific-read claims remain root's provenance;
this QA result independently checks the stated mechanical byte predicates,
not mathematics or private reading history. No gate or source was changed.

Executed from the `arithmetic_symplectic_flow` repository directory:

```sh
python3 papers/475-proper-divisor-tail-admission/tools/verify_batch.py --brief
```

Actual first strict stdout:

```json
{
  "result": "PASS",
  "scope": "Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.",
  "reviewCalibration": "NOT_CALIBRATED",
  "batch": "PRE-P0-STRUCTURE-20260925-Z",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 1211,
  "frozenPrefixes": 6,
  "preservedPackages": 127,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "candidateIDCollisionChecks": 5,
  "pending": []
}
```

The required post-edit strict rerun follows this record's final edit and
complete self-read, because its Markdown is itself an input. Its actual
result and the final record byte receipt are delivered separately; neither
a future result nor a recursive self-hash is inserted here in advance.
Root's later completion-metadata/log changes require root's own final strict
run. This record does not certify those later bytes or authorize new research.

## Historical PREP stage and execution

The PREP stage was **PENDING** after one authorized pre-handoff run, not PASS.
Root fully read and accepted the 410-line source before separately releasing
this single readiness run. The process exited 0; its result was
`PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL`.
There were 47 pending entries. No strict execution had occurred at that stage.

Executed from the `arithmetic_symplectic_flow` repository directory:

```sh
python3 papers/475-proper-divisor-tail-admission/tools/verify_batch.py --pre-handoff --brief
```

Source: [verify_batch.py](../tools/verify_batch.py), 410 LF lines, 20949 bytes.
SHA-256: `e7bd6eebf03d64bde8b1b45e38a14425aef64bce22d677ee63d4eba67df3fb43`.

Exact readiness stdout:

```json
{
  "result": "PRE_HANDOFF_CHECKS_COMPLETE_NOT_FINAL",
  "scope": "Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.",
  "reviewCalibration": "NOT_CALIBRATED",
  "batch": "PRE-P0-STRUCTURE-20260925-Z",
  "packages": 5,
  "identitySurfaces": 8,
  "statusSurfaces": 0,
  "markdown": 12,
  "relativeLinks": 1108,
  "frozenPrefixes": 6,
  "preservedPackages": 127,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 0,
  "boundEvidenceReceipts": 0,
  "boundSurfaceReceipts": 0,
  "candidateIDCollisionChecks": 5,
  "pending": [
    "Final Outcome field/receipt pending: papers/475-proper-divisor-tail-admission/candidate-card.md",
    "Final Outcome field/receipt pending: papers/476-maximal-divisor-chain-rewrite/README.md",
    "Final Outcome field/receipt pending: papers/476-maximal-divisor-chain-rewrite/candidate-card.md",
    "Final Outcome field/receipt pending: papers/476-maximal-divisor-chain-rewrite/claim-ledger.md",
    "Final Outcome field/receipt pending: papers/476-maximal-divisor-chain-rewrite/paper.md",
    "Final Outcome field/receipt pending: papers/477-periodic-clock-measure-support/candidate-card.md",
    "Final Outcome field/receipt pending: papers/478-count-factor-return/candidate-card.md",
    "Final Outcome field/receipt pending: papers/479-arithmetic-prefix-permutation/candidate-card.md",
    "Final evidence receipt pending: 475-proper-divisor-tail-admission",
    "Final evidence receipt pending: 476-maximal-divisor-chain-rewrite",
    "Final evidence receipt pending: 477-periodic-clock-measure-support",
    "Final evidence receipt pending: 478-count-factor-return",
    "Final evidence receipt pending: 479-arithmetic-prefix-permutation",
    "Final outcome receipt pending: 475-proper-divisor-tail-admission",
    "Final outcome receipt pending: 476-maximal-divisor-chain-rewrite",
    "Final outcome receipt pending: 477-periodic-clock-measure-support",
    "Final outcome receipt pending: 478-count-factor-return",
    "Final outcome receipt pending: 479-arithmetic-prefix-permutation",
    "Missing final artifact: papers/475-proper-divisor-tail-admission/README.md",
    "Missing final artifact: papers/475-proper-divisor-tail-admission/batch-summary.md",
    "Missing final artifact: papers/475-proper-divisor-tail-admission/claim-ledger.md",
    "Missing final artifact: papers/475-proper-divisor-tail-admission/evidence/independent-raw.md",
    "Missing final artifact: papers/475-proper-divisor-tail-admission/evidence/review.md",
    "Missing final artifact: papers/475-proper-divisor-tail-admission/evidence/verification.md",
    "Missing final artifact: papers/475-proper-divisor-tail-admission/paper.md",
    "Missing final artifact: papers/476-maximal-divisor-chain-rewrite/evidence/independent-raw.md",
    "Missing final artifact: papers/476-maximal-divisor-chain-rewrite/evidence/review.md",
    "Missing final artifact: papers/477-periodic-clock-measure-support/README.md",
    "Missing final artifact: papers/477-periodic-clock-measure-support/claim-ledger.md",
    "Missing final artifact: papers/477-periodic-clock-measure-support/evidence/independent-raw.md",
    "Missing final artifact: papers/477-periodic-clock-measure-support/evidence/review.md",
    "Missing final artifact: papers/477-periodic-clock-measure-support/paper.md",
    "Missing final artifact: papers/478-count-factor-return/README.md",
    "Missing final artifact: papers/478-count-factor-return/claim-ledger.md",
    "Missing final artifact: papers/478-count-factor-return/evidence/independent-raw.md",
    "Missing final artifact: papers/478-count-factor-return/evidence/review.md",
    "Missing final artifact: papers/478-count-factor-return/evidence/scope-review.md",
    "Missing final artifact: papers/478-count-factor-return/paper.md",
    "Missing final artifact: papers/479-arithmetic-prefix-permutation/README.md",
    "Missing final artifact: papers/479-arithmetic-prefix-permutation/claim-ledger.md",
    "Missing final artifact: papers/479-arithmetic-prefix-permutation/evidence/independent-raw.md",
    "Missing final artifact: papers/479-arithmetic-prefix-permutation/evidence/review.md",
    "Missing final artifact: papers/479-arithmetic-prefix-permutation/evidence/scope-review.md",
    "Missing final artifact: papers/479-arithmetic-prefix-permutation/paper.md",
    "New overview handoff not yet prepended: papers/README.md",
    "New overview handoff not yet prepended: readme.md",
    "Pre-handoff mode: rerun without --pre-handoff for final handoff"
  ]
}
```

The zero reconstructed-archive count is expected here: both overviews still
equalled their complete opening bytes, so pre-handoff recorded the two missing
new prepend blocks as pending instead of counting archive reconstruction.
The 127 old bundles and five immutable anchors were checked successfully.

The initial PREP record was created AFTER that run: 221 LF lines, 13306 bytes,
SHA-256 `ad7e20b36ddc0059734393aee00c982470758293493be4bcd598d2c9d7fb5aa0`.
Its then-missing path in stdout is an honest historical observation, not a
claim that it remained absent. Concurrent author work could also change
readiness inputs. No updated count was inferred at that stage, and no second
readiness run occurred. The full historical stdout above is retained unchanged.

## Frozen identity and byte contracts

| Package | Candidate ID | Prefix lines | SHA-256 |
| --- | --- | ---: | --- |
| 475-proper-divisor-tail-admission | ANG-20260925-DTA01 | 102 | 3dd499d784edceaa61fb3dd4d2853fd458f9e56ca6f7faa4101de3348d07307c |
| 475-proper-divisor-tail-admission | ANG-20260925-DTA01 | 110 | b6f84995856bfdb16e2ec2703a620d1c1d5e22fd4688d4e5078d42b9707e4dcd |
| 476-maximal-divisor-chain-rewrite | ANG-20260925-MCR01 | 105 | 7bc0a9f67479b8a5b1f51f2fa752d96d8269a176d0697238733f1ff8f7076a77 |
| 477-periodic-clock-measure-support | ANG-AUDIT-20260925-PCS01 | 107 | 268785812acefa8584806e1969a4b7781fb0d1b3bac353febba3aca8ead671ba |
| 478-count-factor-return | ANG-20260925-CFR01 | 103 | 0ed468c07a3ccf3f84806aa5bfbabe89ad12b08cc716c465e3bc0093e012fc03 |
| 479-arithmetic-prefix-permutation | ANG-20260925-APP01 | 103 | dee878be33686a7a14383adefb27c0228aea00ff05f9da1d894e20a11dd7086d |

These are five original prefixes plus the separate clarified 475 prefix:
six byte locks, not six candidates. The original 102 lines of 475 remain
protected alongside its 110-line clarification. Final whole-card hashes are
also bound to the final review, including the final Outcome appendix.

The expected final Markdown inputs are the five packages' four scientific
surfaces and three evidence files, plus this record, the first package's
batch log and batch summary: 38 required files. The pre-handoff result did not
assert final completeness; the separately authorized strict result now checks
their required existence and bindings.

Scientific surfaces: `candidate-card.md`, `paper.md`, `README.md`,
`claim-ledger.md`. Evidence: `scope-review.md`, `independent-raw.md`,
`review.md`. The root-owned [batch log](../batch-log.md) supplies the five
canonical Outcome rows and fifteen exact scope/raw/review SHA receipts.

Strict mode requires 20 matching surface IDs, 20 explicit Outcome fields,
15 evidence hash receipts, 20 current final-surface hashes in the final
reviews, CP2/CP3 PASS markers, five bounded ID-declaration ownership checks,
six frozen prefixes and two exact recovered overview archives. Outcomes
are taken from the log, not predetermined by this checker. Review PASS is
not candidate-target, theorem or formal Route success.

Checks include scoped Markdown LF/final newline, supported fence balance
and local link destinations; symlinks and unexpected non-Markdown package
artifacts are rejected. The sole permitted new non-Markdown package artifact
is this exact verifier. The candidate-ID declaration scan uses the first
20 lines of package cards; scientific body references are not collisions.

## Opening protection

Opening measurement before any Z write matched inherited 348–469:
122 packages / 956 files. Fresh 470–474 added 39 files, giving
**127 protected old packages, 348–474 inclusive, 995 files**.
Both the readiness run and the first strict run checked all protected bundle
file counts and hashes against the opening contracts.

Bundle encoding: sort regular-file relative POSIX paths, concatenate
`relative path + TAB + lowercase SHA256(file bytes) + LF`, encode UTF-8,
then SHA-256 the whole string. Reject symlinks and compare exact file counts.
Archived verifier source is parsed as DATA, never executed or imported.

| Fresh protected Y package | Files | Bundle SHA-256 |
| --- | ---: | --- |
| 470-gcd-memory-register | 11 | 47e12b38c187206a574f69e20eab851c86984ded6f3de740f361322c6511a8fb |
| 471-factor-word-return-skeleton | 7 | f4e9d378be20a504014a8408f5ff66e70aa5843fa27ac264530be4cd846f489c |
| 472-circle-radix-carry | 7 | cb38c54aab84e6b792c529115346091ef1c9d677412195446bb3d40234a0db5c |
| 473-divisor-jacobi-perron | 7 | d65b15c59061b276af622efbe913164a7fd5d0264bc76d72cdde670c4faf34ff |
| 474-divisor-prefix-compression | 7 | b942bed624413185f9291e7ffec05c7a32e72a3bd04b927bb67ea51c6a528418 |

| Fixed anchor | SHA-256 |
| --- | --- |
| AGENTS.md | 86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d |
| plan.md | 9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0 |
| docs/prior_work/README.md | d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd |
| papers/paper-template.md | ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b |
| papers/283-nonlinear-residue-clock-screen/paper.md | 50429784fc1f634da86aa6aae1aac1b0e109b7fcc82a6169a68bb80a5bf95d38 |

| Complete opening overview | Bytes | LF lines | SHA-256 |
| --- | ---: | ---: | --- |
| readme.md | 270990 | 2828 | 95c58cf3510e4504f87b8e45d0e5b8e6738ba1137beacf3b4b8426a4b49f7e37 |
| papers/README.md | 252336 | 2604 | fb2948da16c87180c718d098c81578f9a181aaded4c7dc567a1133e90db28f5f |

Strict archive recovery removes only the new Z prepend and reverses the
old Y Current-to-Preceding heading demotion, retaining its 2026-09-25 date
and every other old byte. Both complete reconstructed hashes now matched.
The new blocks must link all five READMEs and contain the handoff date and
5/5 marker; this does not independently validate their scientific prose.

## Exposure, limitations and next gate

QA fully read old Y source as adaptation data and new Z source 1–220 /
221–410 EOF. Static AST/literal parsing and prefix-byte checks matched all
five card identity declarations and six frozen prefixes. These static
operations did not execute a verifier. The readiness execution above was
separately authorized and remains the ONLY pre-handoff run. The later strict
execution followed a distinct FINALREADY release, as recorded above.

Opening work hashed old files and overviews, rather than interpreting old
scientific manuscripts. New card reads for this QA used identity metadata
and frozen bytes; no proof or review was read for mathematical judgment.
The readiness program read available scoped Markdown/evidence and overview
bytes; strict execution read the final available inputs for mechanical
predicates. Neither constitutes a mathematical full-read by this agent.

The same-model helper `/root/measured_history_qa/python_verifier_review`
checked immediate 475–479 path names during opening, then separately fully
read the new 410-line source and compared old Y source as text. It reported
no concrete adaptation discrepancy or weakened gate and returned to HOLD.
It did not execute verifiers, read science or write files. At that PREP stage,
it did not review the later readiness output or record. Any subsequent
record-only consistency assistance is disclosed in the separate handoff.

ARS reproducibility and read-exposure rules inform this bounded mechanical
adaptation. No full scholarly pipeline or calibrated/external peer review
is claimed. Byte equality does not establish mathematical correctness,
novelty, clock ownership, chronology, genuine private reading, blindness or
independent errors. Link checks do not cover remote availability, fragments
or all CommonMark syntax; identity substrings are not semantic owner proofs.
No infinite/global conclusion or Route coordinate follows from these checks.

QA wrote only this record after the readiness run and updated only this record
after the first strict result; the accepted source remained unchanged.
No old verifier execution, scientific edit, Git mutation, network request,
PDF, publication or sixth research round was performed. The observed first
strict counts are 38 package Markdown files and 1211 local link occurrences
across those files and both overviews, with all required bindings and an empty
pending list. These are artifact observations, not scientific proof.
The post-edit rerun is required for this changed record, not an unchanged-input
ritual. Its actual result is delivered separately after execution, along with
this record's complete-read and byte receipt.

EOF — actual strict PASS recorded; historical PREP output preserved.
