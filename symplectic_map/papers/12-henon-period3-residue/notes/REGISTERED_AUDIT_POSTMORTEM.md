# Registered Audit Postmortem: Proof-Only Redisposition

## Disposition

- Proof-only lifecycle ID: `henon_period3_residue_proof_note_v1`
- Consumed implementation candidate: `henon_period3_residue_v1`
- Consumed run ID: `R100`
- Exact v1 disposition:
  `REGISTERED_AUDIT_TERMINAL_FAIL / NO_RERUN / NO_RAW_RESULT / NO_RESULT_PASS`
- v1 manuscript disposition: **withheld**
- Replacement path: proof-only specialist note, pending a fresh independent
  proof-only handoff review

This postmortem is a provenance record, not a scientific result. It does not
repair, rerun, or reinterpret the consumed registered audit. No registered
coefficient value is reported, reconstructed, or used.

## Immutable evidence bindings

All paths below are relative to
`papers/12-henon-period3-residue`.

| Artifact | SHA-256 | Evidentiary role |
|---|---|---|
| `experiments/source_lock.json` | `2fa930f697f6040cb16916d2b4dba7ec591a712882c108848e9eecf53608e1c2` | frozen source-design authority |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `5e66edcd7f33769f748c8b6bd6582aa7e05b3325329839c46bf3627945803d11` | independent `SOURCE_LOCK_PASS` |
| `notes/PROOF_PACKAGE.md` | `36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9` | proof-only theorem authority |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `5630610bb637e155fa631eb2d9c4b36c6ea334ae976a6ef39a53dd733b8c62de` | atomic claim and nonclaim boundary |
| `notes/NOVELTY_ASSESSMENT.md` | `c497dc4e2c404fbbfc3c89450991964d1049f06288a051bc647a15005a66146a` | bounded novelty and positioning boundary |
| `preexecution/INDEPENDENT_DEPLOYMENT_REVIEW.json` | `23000b3478e325271be5f06148037c053bd002befe17345d7f532dfb36183f0c` | historical pre-run deployment authority only |
| frozen code tree | `3c625fd5357bae97a4ee990443b0a59aa79e7f2d82d5986a5b5b2d8769acd521` | forensic object only; forbidden manuscript input |
| `runtime/candidate_v1/official/durable_claim.json` | `3b7075f7d5b1b3199c213ae34327f2c80c9f03396b5a792c086416ce99d581c0` | proves the one-shot budget was consumed |
| `runtime/candidate_v1/official/terminal.json` | `1e0896af17907e41f7028a71c056e02d5f8fb4ddf63d3d033063979e0b1d802d` | terminal failure authority |

The deployment review passed before the run. That fact does not imply that a
registered result exists or that any scientific comparison passed.

## Facts established by durable records

1. The durable claim records one registered audit, one registered candidate,
   and zero rerun budget after start. The claim state is `STARTED`.
2. The terminal record has state `REGISTERED_AUDIT_TERMINAL_FAIL` and failure
   code `POST_CLAIM_RUNTIMEERROR`.
3. The terminal record sets `rerun_permitted` to `false`.
4. The terminal record has both `result_path` and `result_sha256` equal to
   `null`. No `raw_result.json` exists in the official runtime inventory.
5. There is therefore no registered result, no result-integrity verdict, and
   no result-level manuscript authority.
6. The sole registered transaction is consumed. A patch followed by another
   execution would be a prohibited rerun, not a repair of this record.

These facts require the exact lifecycle statement:

> `REGISTERED_AUDIT_TERMINAL_FAIL / NO_RERUN / NO_RAW_RESULT / NO_RESULT_PASS`

## Forensic attribution, explicitly marked as inference

### Static observations

The following observations come from read-only inspection of the frozen code
tree; no candidate module was imported or run.

1. Track Q's decorated-tuple component has an endpoint branch at
   `j == m + 1` that returns the scalar integer `0`.
2. Its immediate caller iterates through that endpoint and unconditionally
   performs a two-target unpack of the return value as a value--pattern pair.
3. Consequently, the frozen endpoint is a deterministic scalar-versus-pair
   contract defect: reaching the endpoint raises before Track Q can seal its
   output envelope.
4. The bootstrap launches Q before R and before adjudication. The preserved
   staging directories contain no sealed Q output, no R output, and no
   adjudicated scientific record.
5. The parent process captures child stdout and stderr, but on nonzero exit it
   persists only a generic capability-process failure. The child's traceback
   and stderr were not retained in the durable terminal artifact.

### Attribution

**Forensic inference, not a runtime-record fact:** the deterministic Track Q
scalar-versus-pair endpoint defect is the cause of the observed post-claim
failure, with approximate attribution confidence **0.98**.

The confidence is high because the endpoint is necessarily reached by the
frozen Q loop, the type mismatch is unconditional there, Q is the first
scientific child, and the predicted child failure matches the durable generic
failure class. It is not 1.00 because the child traceback/stderr was lost and
the one-shot policy forbids reproduction.

This attribution must never be restated as an observed traceback, a recovered
child log, or a rerun-confirmed diagnosis.

## Scientific interpretation boundary

- No Q/R scientific comparison was reached or durably recorded.
- No scientific mismatch was observed or recorded.
- The absence of a recorded mismatch is **not** evidence of agreement.
- No Track R result, adjudicator result, raw result, or result manifest exists.
- No value of `D8`, `D9`, `E8`, or `E9` is present in this postmortem, and no
  such value may be inferred from it.
- The failure does not falsify the source proof, but neither does it
  computationally confirm any theorem.
- The source proof and its independent R2 review remain the only scientific
  authorities available to a proof-only manuscript.

The appropriate classification is an implementation/lifecycle failure before
scientific adjudication, not a theorem counterexample and not a successful
audit with a cosmetic wrapper error.

## No-patch and no-rerun rule

For `henon_period3_residue_v1` and `R100`:

- no code patch is authorized;
- no wrapper patch is authorized;
- no child-stderr recovery run is authorized;
- no second registered claim is authorized;
- no replacement raw result may be synthesized;
- no post hoc value extraction from staging or memory is authorized; and
- no result-pass or dual-engine-agreement language is authorized.

A future implementation experiment would require a new scientific candidate,
a new prospective design, and new authority. It cannot retroactively repair
or supplement v1, and it is outside this proof-only redisposition.

## Proof-only redisposition

The new lifecycle `henon_period3_residue_proof_note_v1` is deliberately
noncomputational. It may use only the source-locked proof, independently
reviewed source package, bounded novelty/citation material, this transparent
postmortem, and the accompanying proof-only scope. It must set
`registered_evidence_used=false`.

The proof-only note is not yet authorized. Its handoff package must receive a
fresh independent review at
`notes/INDEPENDENT_PROOF_ONLY_HANDOFF_REVIEW.md`. Until that review returns
the required pass verdict, `manuscript_authorized=false` and
`finalization_authorized=false` remain mandatory.

