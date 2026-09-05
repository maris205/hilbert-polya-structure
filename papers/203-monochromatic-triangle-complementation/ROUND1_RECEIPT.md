# P203 accepted repaired Round1

2026-09-05 UTC. ROUND1_FROZEN / REVIEW_B_NEXT / OWNER_AMBER / HOLD_EXTERNAL.

Root was actual manuscript reviewer A, distinct from mathematical contributors
batch197_fifth_scout and batch197_lzk_gate. Its earlier candidate adjudication
and preparatory control are disclosed, not counted as manuscript rounds.
Review directory: docs/papers197_201_sequence/reviews/p203_a/.
Decision ACCEPTED_REPAIR; Open findings: Critical 0, Major 0, Minor 0.

Actual Minor A-M1 required a visible HOLD_EXTERNAL/scope paragraph in the
manuscript. The author supplied revision_a/ and A_RESPONSE.md. Root inspected
the exact one-addition source diff and unchanged math, bibliography, verifier
and canonical; it performed new source-only builds and viewed all four pages
of both the original and repaired PDFs. The repaired PDF remains four pages.
The distinct historical missing-intermediate-code Minor1 remains unrepaired
and explicitly disclosed; no missing bytes were reconstructed or old failed
pin silently fixed. This paper uses complete physical current inputs and
does not invoke the unavailable intermediate program as a proof dependency.

Two real formal fresh A executions each produced 1,498,484 assertions and
byte-identical full stdout, as recorded in A/REPLAY_LOG.md. After sealing A,
root's package gate (actual session25824, exit0) checked complete recursive
review coverage, all28 input pins, zero-open finding and accepted-delta rules,
then executed two further fresh exact canonical comparisons. Its stdout ended
P203_A_PACKAGE_GATE_PASS. Finite replays are not substitutes for the proof.

| Accepted input | SHA-256 |
|---|---|
| main.tex | 70c22a62adc3b6218278a6fd91b08dfa8d02efddf03ba7cc115bd35a3ab6de54 |
| references.bib | 2a7c888ff6158f11e00a45f6231f628e575515d1f1c0713f93f90592ea88f78a |
| verify_p203.py | 77e7be9b6dc57a156010c6543ff41415415f833119e5a7116ffcef53cc5e1d7d |
| CANONICAL.txt | 6a672bcfa97f09c1575aa89bb4e2ca52aa8284315706ec90abbd6d35995dbf00 |
| main_round1.pdf | 0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d |
| A verifier | 66a12b737eaa8428389f00ec951e0fb2e844dfa96b3491ef8d8e37138b466d67 |
| A canonical | 0a05cc3f14a56db28afa6084cac6301d06d1b957d1119d387c8dc367df518d9a |
| A top manifest | 0299cf848039e58e1847a808c22362892d90e1eed88a1ae1becc761303789cfa |

frozen_round1/ is a new physical copy of the36-file frozen_round0 payload,
with only main.tex and main.pdf replaced by the accepted revision_a bytes;
its nonself manifest is refreshed for precisely these two changes. Copied
Round0 companion labels remain historical author records. This receipt,
not those old labels, identifies the Round1 transition. The separate
main_round1.pdf equals the accepted repaired PDF and current main.pdf.
Original Round0, revision_a, author response and accepted A package are
preserved unchanged. A wrong-base manual SHA invocation checked current
live main/PDF against old Round0 hashes and correctly failed on those two;
the corrected invocation inside frozen_round0 checked all36 originals PASS.
That invocation mistake is not recorded as a successful integrity check.

Review B may now start from these frozen accepted inputs. It is assigned to
batch197_fosp_gate, distinct from A and both proof contributors. Its earlier
Stage1 gate is not Review B; any reuse of its independent control must be
disclosed, with actual fresh manuscript-proof/source/build work and two new
runs. No Round2, terminal QA, five-paper completion or external release is
implied by this freeze.
