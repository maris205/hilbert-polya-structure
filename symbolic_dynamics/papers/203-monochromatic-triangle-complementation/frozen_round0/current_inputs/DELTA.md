Decision: **SELECT_INTERNAL_AMBER**.

Date: 2026-09-05 UTC. Candidate Stage1 disposition only. No manuscript
Review A/B, paper number, completed paper, or external release is granted.

## Actual finding MCT-PIN-1: missing historical author-code bytes

Severity: **Minor, non-blocking archival defect retained**. It is not
reported as repaired or as a passing original dependency check.

The original temporal package's own 10-entry manifest passes. Its four
external input pins now give **3 PASS / 1 FAIL**: the mutable author
`probe.py` path changed after the temporal package froze and before the
author package's final freeze. The earlier digest is
`7672dea68f66714f1415fec3a507ea06b1ca1beb18c03ac65fc51753f3fea1f7`;
the final author digest is
`1e40d08722268ab476a8687d1f0204a5dd3f5b2dc6c7046eb0d887c63d36b937`.
No authentic intermediate bytes have been supplied. Reconstructing them
from memory or later code would not restore historical evidence.

The append-only response is
`../mct_temporal_pin_supplement_20260905/PROVENANCE_RECEIPT.md`, exact SHA
`6d1b1eaa25d18ce5ed0e036ab73f054476244117214da2ecacb37cd3332144af`.
Its 12-item manifest and 12 new version-specific input pins pass. The
unchanged temporal proof, code, canonical and old manifest are separately
identified; two supplementary fresh temporal runs match its original
canonical. These statements have not been used to infer availability of
the missing version. Both original packages remain unmodified.

**Adjudication:** the defect is bounded for this gate because the frozen
temporal mathematical proof is standalone, was fully inspected, and invokes
no program as a lemma. The frozen temporal verifier has no runtime author
dependency according to its contributor's explicit source/AST receipt;
the gate does not claim to have read that code. More importantly, this
gate wrote and ran its own entirely separate literal, SCC, inverse and
equality checks. Its current proof and dependency pins are complete.
Admission does not require trusting an unavailable early author probe.
The missing intermediate bytes remain a real archival caveat; any claim
requiring that exact historical program is excluded.

## Mathematics and value findings

No Critical or Major mathematical finding remains. The temporal author's
original all-parameter proof is valid without the gate's root-zero
observation; that observation is an alternative audit route, not a repair
or hidden coauthorship contribution. No author mathematical statement was
modified. Every-target inverse, small ranks, sharp witnesses, and the
star/top equality crossover survive independent proof scrutiny and the
two fresh exact replays.

Johnson clique number/classification, generic least-involution machinery,
source undo, induced complementation and Ramsey facts are fully deducted.
The all-parameter no-return clock and literal complete target certificates
remain a sufficiently separate conjunction for internal amber selection.
No whole-owner transfer was established in the bounded history/primary
scope. This is not a theorem that none exists.

Final gate findings: **Critical 0, Major 0, Minor 1** (the disclosed,
non-blocking archival defect above). The verifier's zero finding counters
refer only to failed finite assertions; they do not overwrite this report.
External state remains **OWNER_AMBER / HOLD_EXTERNAL**.
