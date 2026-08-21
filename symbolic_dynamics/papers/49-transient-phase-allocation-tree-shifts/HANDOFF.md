# Paper 49 writer handoff

## Exact status

`HOLD_FOR_INDEPENDENT_WRITER_AUDIT`

Sole active writer root:
`/tmp/paper49_writer_candidate/FINAL_WRITER_OVERLAY`

This writer closure is not an installation or independent-audit verdict.

## Active anchors

- PDF `main.pdf`:
  `aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4`
- self-excluding `PAPER_MANIFEST.tsv`:
  `7339a573f0312b99689d2b92d313811c30523911e20875863e6e27b524022ab5`
- `WRITER_REPORT.md`:
  `59741ef245debd2d03ad25c5273552a767935b7191c573cbc76a916aa193840f`
- portable protected-tree manifest:
  `b5f6e48c3e6b61ca0fbf3bdb76153d93930f1b383c005dc102fd71c0724b8e22`
- protected Stage-A replay:
  `d8d7c57457e567774783deea98a6bac4a87b8d7b787101d7b9b4e48a2fff9715`
- two-lane independent replay:
  `9408e1125e41f6d7fbd4c3bebe582c238c34ea215e3ef262f9ef8464651e546c`
- path-neutral strict PDF QA:
  `c29e590845092312b0c05c6593bee8646822bf7ff952aa0c8ccfcd933c5dca51`
- independent-audit anchor ledger:
  `ab70bd5d8c2eca1d2a5f0c941bf201ee5fb2535fc13dd04853f6e2a53ed94b6c`
- normal/hostile replay-isolation regression:
  `5f37918ef21f7f4db6e5403717a374c2095bef3f782e8a0f84f466129ea85f01`
- withdrawn writer-anchor ledger:
  `a25130862caf2484c52f29f61d0b4f4b649bc182f6facb1821ea7ea8e3498aca`

`WRITER_SEAL.json` is the final closure node and binds this handoff, the
report, manifest, PDF, protected-tree receipts, replay receipt, and PDF QA.
There is intentionally no overlay `STATUS.txt`: that path belongs to the
protected Stage-A namespace, and the active writer status is bound here, in
`WRITER_REPORT.md`, and in the seal.

## Read-only verification

From the active root, an independent auditor can run:

```text
python3 -I -B tools/capture_protected_stagea.py --check
python3 -I -B tools/replay_overlay.py --check --scratch /tmp/p49_overlay_reaudit
python3 -I -B tools/build_paper_manifest.py --check
python3 -I -B tools/build_writer_seal.py --check
```

The scratch path for replay must not already exist.  No command writes the
active overlay in check mode.  The replay runner constructs a minimal child
environment and strips `PYTHONPATH` and `PYTHONHOME`; its hostile-caller
regression is bound above.  Historical files outside this overlay are not
active inputs.
