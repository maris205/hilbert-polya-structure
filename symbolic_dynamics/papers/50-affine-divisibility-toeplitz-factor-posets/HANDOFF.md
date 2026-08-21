# Paper 50 independent-writer-audit handoff

Status: `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.

Audit only the exact overlay at
`/tmp/paper50_writer_candidate/FINAL_WRITER_OVERLAY`.  This writer-side
handoff does not claim CLEAN and grants no installation, publication,
authority-write, Git, README, or mirror permission.

## Sole active anchors

- active PDF:
  `bf0c9ea39d55596fab6d873a4062a836451c0a65113d2d245b0a7d94e3243736`;
- self-excluding paper manifest:
  `34dfb4c803bd2a96eda24272e5b70b0b1c42e7b255f73c17da00a7bbfcfdb876`;
- writer report:
  `f962f9ca5db37a70607aba3b1d69d1750bde08e86d2e3f360c6966ad107aaf11`;
- portable protected Stage-A manifest:
  `0c045bef614862e1d583ad1b72a407d4981db0cd9ce0d93281d56458bb2563ef`;
- protected independent-method replay receipt:
  `0c2d7f4c81effe852b876518db8b9cdff01c1c0d0445511a3455a47e810e153c`;
- final two-lane overlay replay:
  `f0682986a85922ba549bb72b5aa47e93ab0c529816e5dd2d579af64892fa2c72`;
- active PDF QA:
  `0b6d71529012a662e8a597118b1562e5549d61616cf0a246bce083a2cad1fbc9`;
- independent post-output result/report:
  `9c08d2719d4b63a503c572dce37f812042ff483f91ba05b9673033251e4d2e0d`
  / `ef3b13baf948711484fd15846d285835bc60728831d9e4658682a1b31e760039`;
- fresh independent writer re-audit result/report:
  `9f57242d10556afa4a826cd0a7f7dbe6bec4cd2848add6cb1bb70add9e53c8f2`
  / `2edc7bf112a44de36c0a11aa8d3c58dcc01585380ef31bcfc3c7eb771a026f0b`.

Use the externally transmitted raw `WRITER_SEAL.txt` SHA-256 as the final
closure anchor.  The seal is written last and self-excluded; this handoff does
not depend on its hash.

## Required read-only replay

From the overlay root, require:

```text
python3 -I -B scripts/build_writer_manifest.py --root /tmp/paper50_writer_candidate/FINAL_WRITER_OVERLAY --check
python3 -I -B scripts/check_pdf_qa.py --check
python3 -I -B scripts/replay_writer_overlay.py --root /tmp/paper50_writer_candidate/FINAL_WRITER_OVERLAY --check
python3 -I -B scripts/capture_protected_statea.py --authority /root/autodl-tmp/hilbert-polya-structure/symbolic_dynamics/papers/50-affine-divisibility-toeplitz-factor-posets --stage0 /tmp/p50_stage0_candidate --postoutput-result /tmp/p50_authority_independent_postoutput_audit/AUDIT_RESULT.json --postoutput-report /tmp/p50_authority_independent_postoutput_audit/reports/INDEPENDENT_POSTOUTPUT_AUDIT.md --writer-reaudit-result /tmp/p50_writer_fresh_reaudit/AUDIT_RESULT.json --writer-reaudit-report /tmp/p50_writer_fresh_reaudit/reports/AUDIT_REPORT.md --writer-root /tmp/paper50_writer_candidate/FINAL_WRITER_OVERLAY --check
```

Expected manifest closure is 45 content rows, 49 final regular files, and 11
directories including the root.  Every file must be mode 0644; every directory
must be mode 0755; no symlink, nonregular, cache, bytecode, auxiliary,
review/round/history tree, temporary lane, Git path, README, or extra node may
exist.

The independent auditor should additionally:

1. independently hash and parse the raw writer seal before trusting embedded
   fields;
2. capture the live protected tree twice and compare the relative portable
   manifest without invoking live integration;
3. independently verify the exact nine-file/four-directory output delta and
   external post-output result/report anchors;
4. build two fresh overlay copies at epoch 1787270400 and require exact PDF,
   preview, table, log, and BBL hashes;
5. repeat all six fail-closed extractors, strict raw XML parsing, fonts,
   citations, 17-page A4 geometry, and visual checks;
6. check the theorem/proof/source/nonclaim boundary independently; and
7. confirm candidate, authority, Git, README, and mirror before=after.

Machine checks and external dispositions are evidence, not theorem proofs or
writer-side CLEAN claims.  A positive independent audit may recommend a later
root-controlled action, but this handoff itself authorizes none.

**STOP**
