# Batch Y mechanical verification — strict PASS

Batch: `SYMBOLIC-RETURN-20260925-Y`.
Scope: exactly papers 470–474; no 475.
Context date: 2026-09-25; not independently established event chronology.
Review calibration: `NOT_CALIBRATED`.

## Current result and authority

**PASS — the first authorized strict execution exited 0 with pending: [].**
This is a mechanical artifact result, not a scientific verdict, completed
root integration handoff, or authorization for another research round.
Root supplied DISTINCT FINALREADY after reporting all five final reviews
fully read and the scientific surfaces frozen. Root owns that scientific
review and integration; this QA role owns only the verifier and this record.

Historical PREP record: 149 LF lines, 8512 bytes, SHA-256
`3bbfe39d5ce2087c30036939836b4717fa2efb6cbfe242e932eee62597518668`.
It correctly recorded PENDING and no verifier execution at that stage.
No pre-handoff run occurred. The present strict result supersedes that pending
execution status without rewriting its provenance.

The new verifier was fully read through line 407 / EOF and checked statically.
Its Python syntax parsed, and all five frozen card prefixes and declared IDs
matched their supplied metadata. Those bounded checks did not execute either
the new verifier or an archived verifier. They are not a substitute for the
strict artifact audit recorded below.

## Exact executable and command

Source: [verify_batch.py](../tools/verify_batch.py).
Read from the `arithmetic_symplectic_flow` repository directory.
Current source: 407 LF lines, 20713 bytes, SHA-256:

`e6c344c609be81c09b582505f4cc933e0e664faba86b6d29a3326bdea94e1f82`

Executed strict command, exit code **0**:

```sh
python3 papers/470-gcd-memory-register/tools/verify_batch.py --brief
```

Default mode is strict. Optional `--pre-handoff` never reports final PASS.
Actual first strict stdout:

```json
{
  "result": "PASS",
  "scope": "Mechanical byte/identity/status/link/receipt checks only; not mathematical proof.",
  "reviewCalibration": "NOT_CALIBRATED",
  "batch": "SYMBOLIC-RETURN-20260925-Y",
  "packages": 5,
  "identitySurfaces": 20,
  "statusSurfaces": 20,
  "markdown": 38,
  "relativeLinks": 1190,
  "frozenPrefixes": 5,
  "preservedPackages": 122,
  "preservedAnchors": 5,
  "preservedOverviewArchives": 2,
  "boundEvidenceReceipts": 15,
  "boundSurfaceReceipts": 20,
  "candidateIDCollisionChecks": 5,
  "pending": []
}
```

The required second strict execution follows this record's final edit and
complete self-read, because its Markdown is itself an input. Its actual result
and this record's final byte receipt are delivered separately, avoiding any
self-hash recursion or claim about a run before it occurs. Root's subsequent
completion-metadata changes require root's final strict rerun; this record
does not certify those later bytes in advance.

## Input and binding contract

The five packages and original immutable card prefixes are:

| Package | Candidate ID | Frozen lines | Prefix SHA-256 |
| --- | --- | ---: | --- |
| 470-gcd-memory-register | ANG-20260925-GMR01 | 111 | 6dee0423864ea121b7b475c302e1f3dd7fa06f4c9e5c953ab7e53bdc771b0f50 |
| 471-factor-word-return-skeleton | ANG-20260925-FWR01 | 101 | 5f7989f2062a2fbb66a251b20d8646e010b3d94e4788e00a72be5dc1a3218820 |
| 472-circle-radix-carry | ANG-20260925-CRC01 | 102 | b7b36a6ad4028bc6fb5c50224dca33198400b99775438bd768fbc25194eafade |
| 473-divisor-jacobi-perron | ANG-20260925-DJP01 | 93 | 3d20f511c63b244d324f87c20e7cf9bc4f68d541d3bca291ca65df64d6b6b7f0 |
| 474-divisor-prefix-compression | ANG-20260925-DPC01 | 98 | 595b1751966b2edd700669757ec791437664f80636752dbe08ca1b26f6977e87 |

Required final inputs comprise 38 Markdown files: four scientific surfaces
per package, three evidence files per package, and the first package's
batch log, batch summary and this verification record. Scientific surfaces
are `candidate-card.md`, `paper.md`, `README.md`, and `claim-ledger.md`.
Evidence filenames are `scope-review.md`, `independent-raw.md`, and `review.md`.
The [batch log](../batch-log.md) supplies canonical outcomes and exact evidence
receipts; the [batch summary](../batch-summary.md) remains root-owned.

Strict mode requires all 20 surface identities, all 20 explicit Outcome fields
matching the five log rows, all 15 scope/raw/review SHA receipts, and all 20
current scientific-surface SHA bindings in the final reviews. Card Outcomes
are checked beyond the frozen prefix; other Outcomes must be in the first
20 lines. Outcomes are not predetermined by QA. CP2/CP3 PASS markers are
review-status metadata, not candidate-target or Route success.

All scoped package Markdown and the two root overviews are checked for LF,
final newline, balanced supported fences and existing local link destinations.
The only permitted new non-Markdown package artifact is this exact verifier.
Five bounded candidate-ID declaration checks examine declaration fields in
the first 20 lines of package cards; body references are not ID collisions.

## Opening preservation receipts

Before new Y writes, a separate read-only opening measurement matched the
inherited 117 packages / 917 files and freshly captured X's 39 files:
**122 preserved packages, 348–469 inclusive, containing 956 files.**
The authorized strict run now rechecked all bundle file counts and hashes,
five fixed anchors and both recovered overview archives successfully.
No old scientific file was opened for mathematical interpretation.

Bundle algorithm: recursively enumerate regular files, reject symlinks,
sort relative POSIX paths, concatenate `path + TAB + file SHA-256 + LF`,
encode UTF-8 and hash the concatenation. File count must also match.
Historical verifier literals are read as DATA, never executed or imported.

| Freshly added protected X package | Files | Bundle SHA-256 |
| --- | ---: | --- |
| 465-gcd-hyperbolic-exchange | 11 | ebbee5500dc55ef1071d23a72f6b8d30162802cbf49d4ff6800ae9d22e523b04 |
| 466-divisor-chord-retroreflection | 7 | df9359a45132c2310a3e9174114ef034f2339e0bd180560bac733eb36bb90b6c |
| 467-divisor-vector-cross | 7 | 9d8f3423cf5e4613c4a70bbbdd00d59c0106704eedc01fda804c6479f6a47e7a |
| 468-divisor-inertial-secant | 7 | 91c6698b054f2d488a2f8f1522bbe2491fcc446ed54fb598f8e595bd454aade9 |
| 469-divisor-normalized-register | 7 | 9cfa1c4a4b54881702c7a946a619bb3ba403ac1a116f9026ea1a2cf5aa6a9cdb |

| Fixed immutable anchor | SHA-256 |
| --- | --- |
| AGENTS.md | 86b8d64302321ae0b1b4adc7ac8fc513e5c9c6bc8b1292dab11841188302438d |
| plan.md | 9fa4aade2ca5e71077a70b3aa78b82378795d25fbb1007158f0d21297c1431a0 |
| docs/prior_work/README.md | d2287008387388ac5968288ea4093d630ff0a913f6013547e43e769389a73cfd |
| papers/paper-template.md | ec6caabcd6acdda7d5e1c628b117b7084d266dcb4b0326bec1d25d4a1dfd5a3b |
| papers/283-nonlinear-residue-clock-screen/paper.md | 50429784fc1f634da86aa6aae1aac1b0e109b7fcc82a6169a68bb80a5bf95d38 |

The complete opening overview bytes are protected as follows:

| Overview | Opening bytes | LF lines | Opening SHA-256 |
| --- | ---: | ---: | --- |
| readme.md | 269831 | 2812 | e165c84c3c82a0390447529379dd88ff2efee4bda3b3ceed4350a8bf78d6ba8f |
| papers/README.md | 251175 | 2587 | 664259ec6cf9c193d7acf2ab31ddcadc097b61de9c12dd08d0426ee1b66e3924 |

Recovery removes the newly prepended Y block and reverses only the old X
heading's Current-to-Preceding demotion, keeping its 2026-09-25 date and all
other old bytes. SHA equality then verifies the complete recovered archive.
The new block must contain the handoff date, 5/5 marker and all five README
links; this is not an independent judgment of the prose's scientific truth.

## Read exposure, provenance and limitations

QA fully read the X source as adaptation data and the new Y source to EOF.
Opening reads hashed old package bytes, five anchors and full overview bytes;
they did not rederive old proofs. PREP metadata reads covered the initial
batch log and targeted card identity/header matches; prefix checks hashed
the frozen card bytes without scientific adjudication. Strict execution read
the scoped Markdown, evidence and overview bytes programmatically for the
specified mechanical predicates. It is not an agent-level mathematical
full-read: current reviews and manuscripts were not interpreted by this QA
role for scientific judgment, and root's personal read history is not proven
by these byte checks.

The same-model helper `/root/measured_history_qa/python_verifier_review`
performed a bounded read-only static comparison: all 407 new source lines,
the old X source as text, and initial Y log lines 1–91. It found no concrete
adaptation mismatch or weakened gate and returned to HOLD. It did not execute
a verifier, read scientific reviews, or write files. Its earlier opening
assistance checked only immediate 470–474 path-name collisions.
It also fully read the historical 149-line PREP record and hashed the current
source, finding no material inconsistency; it did not run the verifier or
change files and again returned to HOLD.

ARS reproducibility and exposure rules inform this mechanical adaptation;
no full scholarly pipeline, calibrated peer review or external validation is
claimed. Hashes bind bytes, not correctness, chronology, genuine private read
history, blindness or independent errors. Existing local destinations are
checked, not remote availability, Markdown fragments or full CommonMark
semantics. A substring identity check is not semantic owner equivalence.
The script does not rerun mathematics or establish infinite/global claims,
novelty, endogenous clock ownership, Route coordinates or next-batch authority.

No old verifier execution, scientific rewrite, Git mutation, network request,
PDF, publication or sixth-round work is included. Date labels do not resolve
previously disclosed environment/container clock discrepancies.
The first strict audit measured 38 package Markdown files and 1190 local
destination occurrences across those files and both overviews; all required
bindings closed with an empty pending list. These are observed counts, not
theorem checks or a prediction of later metadata edits.

EOF — actual first strict PASS recorded; post-edit rerun receipt is external.
