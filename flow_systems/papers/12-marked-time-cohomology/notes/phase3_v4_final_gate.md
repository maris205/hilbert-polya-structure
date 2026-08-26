# Paper 12 Phase-3 v4 final design/source gate

Date: **2026-08-15 (Asia/Shanghai)**

Verdict: **PASS — C0/M0/m0; TARGETED V4 PROOF AND CONTROLS AUTHORIZED**

## 1. Exact content tuple

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `e72aa3b82f916a3687ef2366df535599db5ab26e28e2bce66f4a54110b9850f7` |
| `notes/candidate_lock.md` | `7b6b6e97ced6e5b3f39e7da44f852fb1aeea06826fc0a79f807eaf16579b4700` |
| `notes/pipeline_state.md` | `be98619a4e116dc35eb90c77962798a298099ac2740b8f28fa013517bf273107` |
| `notes/phase3_v4_design_gate.md` | `ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a` |
| `notes/phase3_standalone_amendment_v4.md` | `5d9ca4357639bc1e290ca5b85b540a28bfb2a4452ab81826ee9106ae147f0809` |

## 2. Independent zero-finding reviews

| Review | SHA-256 | Verdict |
|---|---|---|
| `notes/phase3_v4_methodology_relock.md` | `c31e1c6d6b21eb4d9de0c698fcbd10bbd2516a7e8a3e477eba591e88de7bfb81` | `PASS C0/M0/m0` |
| `notes/phase3_v4_devils_advocate.md` | `9a9a87fa621b0d0434fb2f0ece635e45a4b721a2f65c238ef4ca441f69aea190` | `PASS C0/M0/m0` |
| `notes/phase3_v4_source_novelty_audit.md` | `cf985db1270bb6b1480f0b29a7770e0865a627ea2412adfc6c4476eeba439c22` | `PASS C0/M0/m0` |

All three reports bind the same final tuple.  The source audit records
`DIRECT_EXACT_PACKAGE_PRECEDENT_FOUND=false` only under the permitted wording
`SUPPORTED_WITHIN_SEARCH`; it does not grant priority or a standalone
decision before proof.

## 3. Authorized work

The following narrowly scoped work may begin:

1. a direct v4 proof of common-stabilizer orbitwise standardization,
   `Std_coprod`/`Indisc`, the automorphism exact sequence, standardized
   `H_cnv^1=R^Q`, the pullback diagonal, and the strict-automorphism invariant
   characterization;
2. the exact new deterministic control artifact and tests frozen in the v4
   amendment; and
3. independent proof, controls, source-boundary, and standalone re-review of
   the stable v4 artifacts.

No Route YAML, composition, manuscript, or release work is authorized by this
gate.  `STANDALONE_PASS` remains ungranted until the prior routine-reduction
Major is independently closed on the proved v4 theorem.  Failure leaves
`NOTE_OR_MERGE` binding.

