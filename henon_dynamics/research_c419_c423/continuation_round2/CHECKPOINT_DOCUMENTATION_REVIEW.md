# Continuation-round-2 documentation and static-code checkpoint review

Date: 2026-09-07 UTC. Status: **PASS within the stated documentation and
static-code scope**. Final state was checked only after the coordinator's
explicit completion notice: **3/5 admitted contracts, 0 new manuscripts,
0 new PDFs, 0 new formal evaluations**. Two complete contracts are still
missing. This audit does not itself admit a paper or certify mathematics.

## Scope and authority

This is a bounded documentation/static-code audit of this
`continuation_round2/` snapshot. Its only write target is this report.
The audit does not rerun a mathematical program, import a submitted
module, build a manuscript, modify Git, or re-review the mathematical
claims. It is not a sealed release or an exhaustive security audit.

The final ADMISSION, README and CURRENT state surfaces were deliberately
excluded from the first pass while the coordinator updated them. Stage 2
below records their actual completed contents. The initial hold and the
preliminary scanner limitation remain documented, rather than being
retrospectively described as a completed first pass.

Reviewer provenance: current internal arithmetic-lane agent. I authored
the arithmetic-lane artifacts and the earlier IR1 lemma review, so those
parts receive author-side static/document checks here, not a falsely
claimed independent author-blind review. No external model or human
review was invoked in this audit.

## Stage 1: completed static-code checks

The five new Python files below were read completely: **757 source
lines total**. Each was processed by Python's `ast.parse`, followed by
`compile(tree, filename, 'exec', dont_inherit=True, optimize=0)` in
memory. No resulting code object was executed. No submitted module was
imported; `sympy` was not imported for this audit; no bytecode file was
written. All five passed this syntax/compilation check.

| Python input | Lines | Assert statements | Explicit file-writing call sites |
|---|---:|---:|---|
| [check_joint_mod16.py](elliptic_dynamics/check_joint_mod16.py) | 93 | 0 | None |
| [certify_ir1_core.py](integral_return/certify_ir1_core.py) | 139 | 6 | Two `write_text` calls for author JSONL/JSON evidence |
| [check_symbolic_families.py](integral_return_review/check_symbolic_families.py) | 66 | 0 | None |
| [independent_ir1_core.py](integral_return_review/finite_core/independent_ir1_core.py) | 325 | 0 | Two `write_text` calls for independent JSONL/JSON evidence |
| [semigroup_probe.py](solenoid_boundary/semigroup_probe.py) | 134 | 1 | None |

The remaining four files use standard-library imports. The symbolic
checker additionally imports `sympy` and constructs symbols/family
expressions at module scope. Its main computation is guarded, but
importing it would still run that initialization; this audit did not do
so. No network client, subprocess launcher, dynamic `exec`/`eval`, or
destructive deletion call was seen in these five inspected source files.
That is a source observation, not a guarantee about external dependencies
or all possible runtime effects.

The producing/review tasks already recorded actual ordinary-mode runs:
the author and independent core each ran once; the coordinator's symbolic
check and the two bounded diagnostics likewise have actual receipts.
Those executions were **not** repeated for this audit. The future-mode
and output-writing limitations below do not invalidate a recorded
ordinary-mode result, and were not used to request rewriting passed code.

### Static risks and scope limitations retained

**S1 — Optimization removes assertion-based guards.** The author core
script uses `assert` at source lines 48, 50, 51, 80, 81 and 118 for cycle,
bound and partition checks. The semigroup probe uses `assert` at line
107 for an SCC invariant. Under `python -O` or `PYTHONOPTIMIZE`, those
guards are removed. The independent core and the two other checkers use
explicit raised exceptions for their inspected failure checks. This is
a limitation of future invocation modes; it is **not** a claim that a
recorded normal-mode run failed or ran under optimization. No mutation
or failure-path execution was performed here, and no source was changed.

**S2 — Semigroup state-cap status is not an error exit code.** On hitting
its 250,000-state cap, `semigroup_probe.py` returns a structured
`STATE_CAP` result, prints it, and breaks out of the loop normally.
Consumers must inspect that status and the reached levels; exit code 0
alone is not evidence that every requested graph completed. This is a
statically inspected branch, not a newly observed cap event. The code's
own finite-graph/spectral-extrapolation boundary remains material.

**S3 — Evidence-pair writes are not atomic or recoverable sealing.** If
executed, each core program writes its JSONL file and then its summary
using ordinary `write_text`. Existing files at those explicit sibling
paths would be overwritten, and interruption between the two writes
could leave an inconsistent pair. The independent script captures author
inputs and checks byte stability before writing, but that is a run-time
snapshot check, not immutable storage. This audit executes neither
writer; it does not claim transactional output, release sealing, or
recovery guarantees.

**S4 — Static compilation is not a proof or a runtime test.** The core
walks rely on their separately reviewed mathematical finite-state and
injectivity arguments for termination. The symbolic checker explicitly
does not establish exhaustion or minimality. The ED1 checker is bounded
to censored congruence distributions. No PASS in this document promotes
one of those boundaries to a stronger scientific claim, tests dependency
availability, or certifies resource use.

### Python input hashes for the completed static pass

```text
aeea1f16e1f110e3d94f884d380a11a3e3bb44fd3eba93c5862e74f0c59e797d  elliptic_dynamics/check_joint_mod16.py
750b4dbb54cacd1df11cc3929ed436cf8de9877048545f212cecc9bc03b75330  integral_return/certify_ir1_core.py
be9ca47f3b7c8f94b43b25d6857f823f35f004407eff71807770dadf6dac40bd  integral_return_review/check_symbolic_families.py
8bd343b599f9ed6c605b255dfe60b544a81375975083fd5d7ffb2b18a1d6c7c3  integral_return_review/finite_core/independent_ir1_core.py
96a8ddbde573c95ad70f99e5a0fccab7ed9775e825da0733e74b274804660357  solenoid_boundary/semigroup_probe.py
```

These identify the bytes inspected. They are not a manifest seal, a Git
baseline, or a promise that a concurrently editable file never changes.

## Stage 1: stable-lane preliminary link check

Eleven Markdown documents were checked in the four already stable lanes:
`elliptic_dynamics/`, `new_charp/`, `solenoid_boundary/`, and
`congruence_towers/`. The preliminary scanner considered same-line
simple Markdown inline links outside fenced code blocks. It found
**28 local-link occurrences, all existing; 0 broken; 19 HTTPS occurrences
skipped**. These are deliberately preliminary counts: wrapped/multiline
labels were not included by that first scanner and will be included in
the final bounded scanner. That parsing limitation is retained here
rather than describing the initial pass as complete Markdown coverage.

For every local target found, only filesystem existence was checked.
External linked historical files were not opened or executed by this
link test. HTTPS/HTTP availability, redirects, source contents and
scientific applicability were not tested. Fragment anchors, including
headings within existing local files, are **not validated**. Bare URLs,
reference-style links, images' actual rendering, and arbitrary Markdown
syntax are outside the simple-inline-link check.

Stable-lane Markdown input hashes:

```text
d4472dbe425bf314d22a7170b84b2f5861be4b7f30bbfd32dfa376f73fe308f3  elliptic_dynamics/FROZEN_CONTRACTS.md
176bc9bfa07191dc1eec31801073c856ab63f231bc9d77fa5493c46b3a624c7e  elliptic_dynamics/SCOUT_REPORT.md
c586be46bee3e4327262965aaf81655bbc23bb5bb47534b0cb8be1151dbb99f8  elliptic_dynamics/SOURCE_AUDIT.md
886a3b83d28aaa39e4663cef0c37c503b4d19dc14ce45a520ef0296f1ad61ab1  new_charp/FROZEN_CONTRACTS.md
5eb746ed5e575ebbe8ae0ffcaaca1f719a328af6f9e02cece05849f7d0fa15a1  new_charp/SCOUT_REPORT.md
6d1e07a71a7974cb924e526fc6ce90c0ab92b290e9ae8428389146cab861a7c9  new_charp/SOURCE_AUDIT.md
9244603e9553b99983697eaf4de8785e997eb4fb09e9304a1d3c813df5cde1ad  solenoid_boundary/DIAGNOSTIC_RECEIPT.md
96c8fb87cdc3122721a3b8f07a2a256e09c0480503aa48936a708940a954f950  solenoid_boundary/FROZEN_CONTRACT.md
ae3af7be647461ec03539183c0e0c9bbe07d5e142d48a70b36cb271a665d2829  congruence_towers/FROZEN_CONTRACT.md
f55a7571df14154eb990f619556e8fbed82cec71f205d12297d7b261ed439bdb  congruence_towers/PROOF_PACKAGE.md
2522fcd9de6d017ccfe9568da0456a53babbdd88106dc5daaec4a87be0f1342a  congruence_towers/SOURCE_AUDIT.md
```

## Stage 2: final scoped link and state check

The coordinator explicitly reported that global updates were complete
before this pass. The main scan inspected **23 round-2 Markdown files
excluding this report**, plus the batch README, ADMISSION_DECISIONS and
the CURRENT C419–C423 prefix: **26 input scopes**. The prefix ends before
`## C414–C418 五篇完成状态（历史批次）` and is exactly **65 lines** in
the checked version. Only that prefix participates in the state/link
check. An initial bounded display of the first 105 CURRENT lines exposed
the following historical heading and opening context; the older state
was not audited, and the full historical file was not scanned.

The actual round-2 inventory at this snapshot is **33 files**:
**24 Markdown (including this report), 5 Python, 2 JSON and 2 JSONL**.
It is not an assumed 35-document inventory. There are no TeX, PDF or
formal-evaluation artifacts in that round-2 inventory. The three added
state scopes are not counted as new round-2 files.

The completed scanner allows wrapped/multiline labels for simple inline
links, while ignoring fenced code blocks. It found:

| Main-scan item | Actual count |
|---|---:|
| Existing local-link occurrences | 104 |
| Broken local-link occurrences | 0 |
| Unique resolved local targets | 53 |
| HTTPS occurrences skipped | 51 |
| HTTP / other-scheme / anchor-only occurrences encountered | 0 |
| Local occurrences resolving outside round-2 | 39 |
| Unique targets outside round-2 | 25 |

The additional historical targets were checked for existence only.
Neither their content nor their old code was reopened by this link scan.
The five Python hashes and eleven stable-lane Markdown hashes agree
with Stage 1; no changed Python input or new Python file was found, so
there was no reason to repeat compilation or a mathematical run.

The link parser remains deliberately limited: it does not validate
fragments/anchors, reference-style links, full Markdown rendering,
nested-parenthesis target syntax or remote availability. All 51 HTTPS
occurrences were skipped, including remote anchors. The wrapped-label
limitation of the preliminary pass is now closed within this larger
simple-inline scope; its earlier 28/19 counts are not added to the final
104/51 counts, because they overlap.

### Documentary status consistency

The following current authorities were actually read after the notice:

- [Round-2 handoff](README.md).
- [Batch handoff](../README.md).
- [Batch admissions](../ADMISSION_DECISIONS.md).
- [CURRENT state](../../CURRENT_RESEARCH_STATE.md), current-batch prefix only.
- [IR1 coordinator adjudication](integral_return_review/COORDINATOR_REVIEW.md),
  compared with the scoped verdicts in the
  [lemma review](integral_return_review/REVIEW_LEMMAS.md) and
  [finite-core review](integral_return_review/finite_core/REVIEW.md).

They agree on the following documentary facts: M1 and AS2 retain their
previous admissions; IR1 promotes the original NG1 question and adds
exactly one contract; the cumulative count is 3/5 with two missing;
there are zero new manuscripts, PDFs or formal evaluations and no
assigned C-numbers. Neither seven bounded work items, individual
channels, exceptional cycles, a period bound nor a zeta formula is
counted as another contract. The finite review's conditional analytic
premise is explicitly discharged in the coordinator's adjudication;
the repaired Section 2 sign and Minor W1 closure are recorded as closed.
This compares the reviewed documents' statuses; it does not reproduce
their mathematical or computational verification.

The first-pass 2/5 section in ADMISSION_DECISIONS is explicitly historical,
and its NG1 disposition is expressly superseded by IR1. Authored
classification/scout snapshots retaining pending-review language are
identified as historical by the current README and adjudication. The
current-authority chain therefore does not turn those old qualifiers
into a contradictory live admission state or a retroactively rerun
certificate.

### D1 — Launch-plan count could be mistaken for the current count: CLOSED

Initial observation: the round-2 plan began with “three independent
substantial contracts are still missing” without an explicit launch-
snapshot label. This was a minor recovery-entry ambiguity, not an
incorrect original plan or a mathematical defect.

The coordinator added four lines under the plan title identifying it
as the initial scope snapshot, stating that launch counts are historical,
and linking the current 3/5, zero-manuscript result. At **09:59:57 UTC**
I read that exact addition and checked its new `README.md` target.
The link exists and the status agrees with the current authorities.
The [repaired plan](SCOUT_PLAN.md) hash is
`ed2bc9bc914ca6a04377b4f4ed8ced4e54101c5c5ebaee74ad0ebc66474150b1`.
The repair was already present in the main scan's bytes and its link
is already included in the 104 count; it is not counted twice. No
whole-tree rescan or mathematical rerun was performed for this closure.

## Final main-scan input identifiers

The following are checkpoint content identifiers, not a release manifest.
The CURRENT hash covers only the explicitly delimited prefix; the other
hashes cover their named files. This report's own later local-link check
is separate to avoid a self-referential report hash.

```text
492464fecc75ce182e886d24f53920e770ee6fdf32b127c66ee92da843c6d5eb  henon_dynamics/research_c419_c423/continuation_round2/README.md
ed2bc9bc914ca6a04377b4f4ed8ced4e54101c5c5ebaee74ad0ebc66474150b1  henon_dynamics/research_c419_c423/continuation_round2/SCOUT_PLAN.md
ae3af7be647461ec03539183c0e0c9bbe07d5e142d48a70b36cb271a665d2829  henon_dynamics/research_c419_c423/continuation_round2/congruence_towers/FROZEN_CONTRACT.md
f55a7571df14154eb990f619556e8fbed82cec71f205d12297d7b261ed439bdb  henon_dynamics/research_c419_c423/continuation_round2/congruence_towers/PROOF_PACKAGE.md
2522fcd9de6d017ccfe9568da0456a53babbdd88106dc5daaec4a87be0f1342a  henon_dynamics/research_c419_c423/continuation_round2/congruence_towers/SOURCE_AUDIT.md
d4472dbe425bf314d22a7170b84b2f5861be4b7f30bbfd32dfa376f73fe308f3  henon_dynamics/research_c419_c423/continuation_round2/elliptic_dynamics/FROZEN_CONTRACTS.md
176bc9bfa07191dc1eec31801073c856ab63f231bc9d77fa5493c46b3a624c7e  henon_dynamics/research_c419_c423/continuation_round2/elliptic_dynamics/SCOUT_REPORT.md
c586be46bee3e4327262965aaf81655bbc23bb5bb47534b0cb8be1151dbb99f8  henon_dynamics/research_c419_c423/continuation_round2/elliptic_dynamics/SOURCE_AUDIT.md
993a32b6dbd60951e64b2b9e903372a55a6c28c5c3c5d42e8e0628f7b72298ca  henon_dynamics/research_c419_c423/continuation_round2/integral_return/FROZEN_CONTRACTS.md
e07855ea457056387c471677fffe0c0414bb6773e3583a3bfb1eb4a4f58a5336  henon_dynamics/research_c419_c423/continuation_round2/integral_return/IR1_CLASSIFICATION.md
5dcc9c6a84e4219a24fa177399ee1e7292e7217d8b83ab3dda4a90ceebd17e5d  henon_dynamics/research_c419_c423/continuation_round2/integral_return/IR1_PROOF.md
7ff81090bb39749d77adddf7f139243f4174823cbd120783d4c3d6d6f9ed6bec  henon_dynamics/research_c419_c423/continuation_round2/integral_return/SCOUT_REPORT.md
457d66c2c49ecf5b54304a466fdb915b8e0020d32ff857031b31ce9571763e94  henon_dynamics/research_c419_c423/continuation_round2/integral_return/SOURCE_AUDIT.md
fb1ce2d2a0acc8eaedeefa6fcb8f7882b039e7bf781a8724ede06368b894ba20  henon_dynamics/research_c419_c423/continuation_round2/integral_return_review/COORDINATOR_REVIEW.md
4dfcf0c86ebdc2b1b3c85330fc771d6094c39c4d4d72989b44c0398a16814064  henon_dynamics/research_c419_c423/continuation_round2/integral_return_review/REVIEW_LEMMAS.md
978903148b96b28dc5e7cb3f5545f1d71ac38d1bcb4f7ff3af0ab457c63694cb  henon_dynamics/research_c419_c423/continuation_round2/integral_return_review/SOURCE_AUDIT.md
68756fd37e79c5617ab4f35d0b98056b226e63a9f8c6efb199c95c2847ffa006  henon_dynamics/research_c419_c423/continuation_round2/integral_return_review/finite_core/REVIEW.md
5d773ce8b0230868ebd0804c68aa56e089468fedb75a8c2f908ff8071cceaa3e  henon_dynamics/research_c419_c423/continuation_round2/integral_return_review/finite_core/REVIEW_PLAN.md
886a3b83d28aaa39e4663cef0c37c503b4d19dc14ce45a520ef0296f1ad61ab1  henon_dynamics/research_c419_c423/continuation_round2/new_charp/FROZEN_CONTRACTS.md
5eb746ed5e575ebbe8ae0ffcaaca1f719a328af6f9e02cece05849f7d0fa15a1  henon_dynamics/research_c419_c423/continuation_round2/new_charp/SCOUT_REPORT.md
6d1e07a71a7974cb924e526fc6ce90c0ab92b290e9ae8428389146cab861a7c9  henon_dynamics/research_c419_c423/continuation_round2/new_charp/SOURCE_AUDIT.md
9244603e9553b99983697eaf4de8785e997eb4fb09e9304a1d3c813df5cde1ad  henon_dynamics/research_c419_c423/continuation_round2/solenoid_boundary/DIAGNOSTIC_RECEIPT.md
96c8fb87cdc3122721a3b8f07a2a256e09c0480503aa48936a708940a954f950  henon_dynamics/research_c419_c423/continuation_round2/solenoid_boundary/FROZEN_CONTRACT.md
625a45c2628e3c28b14c953bb04680316b4619773a3827fd5c6a02a220e8fa7c  henon_dynamics/research_c419_c423/README.md
e0a20d45986299789f2a3e8f9bf4ef084e6fc2cb2159a6711a1ae2ed5ca739e6  henon_dynamics/research_c419_c423/ADMISSION_DECISIONS.md
8f1046b3786900ebcd6443b007bed8faf77eb0a8d484d9adc4e659843d39333e  henon_dynamics/CURRENT_RESEARCH_STATE.md [C419-C423 prefix only]
```

## Final limits and handoff

No broken simple local target or unresolved documentary state correction
was found in the completed scope. S1–S4 remain visible usage/risk limits,
not claims of newly observed failures. No change was made to submitted
code, author evidence, old snapshots, global state, Git or a manuscript
by this audit. No remote or Git freshness check was performed here;
worktree/commit descriptions are documentary status, not a new clean-tree
or synchronization attestation. The snapshot remains editable and unsealed.

After assembling this report, its own local inline links were checked
once separately. At **10:02:25 UTC**, the report-only check found
**13 local occurrences, 13 unique targets, 0 broken, and 0 remote or
anchor-only targets**. It imported/executed no mathematical program.
Together with the disjoint main-scan source files, this gives **27
document scopes and 117 existing local-link occurrences**, with the
same 51 HTTPS occurrences skipped. The main scan's unique-target count
is not added to the report's because those target sets may overlap.

After that self-check, one stray leading `+` before the first displayed
hash was removed and this receipt was appended. Neither edit changes
a link, so no redundant link scan or whole-tree pass was performed.
