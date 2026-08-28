# C220 test report

All commands below were run from the package root with Python 3 and `-B`
(fixed epoch `1787875200`):
source/code lock `86c7bb8a39cdd1b8e941e45833b068170ca06287`.

| gate | command | expected |
|---|---|---|
| producer | `python3 -B code/c220_tasep_producer.py` | PASS: 200 interior, 40 boundary, 7 phase rows; payload `82def8f1358aa47442bb4af9cdf412952f2cbe562d3ff0814e2f740a98ccf1ed` |
| checker | `python3 -B code/c220_tasep_checker.py` | PASS: 3597 assertions; 150 SymPy-nullspace rows |
| symbolic | `python3 -B code/c220_tasep_sympy_crosscheck.py` | PASS: 576 checks (321 word-algebra) |
| replay | `python3 -B code/c220_tasep_replay.py` | PASS: byte-identical, 441439 bytes |
| mutations | `python3 -B code/c220_tasep_mutation.py` | PASS: 28 repaired-hash + 1 stale-hash rejections (29 total) |
| manifest | `python3 -B code/c220_release_manifest.py` | PASS: 27 payload files + self-excluded manifest |

The checker is independent of the producer, exact nullspaces are rebuilt with
SymPy, and all generated sidecars are excluded before the manifest audit.

Evidence file SHA-256: `811f7238aa5b1f44dae8da54dcacbf84b4db699b65e47da9fb85dbb0ec558396`.
The checker does not import the producer; replay compares the complete JSON
bytes.  The hostile mutations include repaired hashes, stale hashes, schema
shape, boundary, phase, current, nullity, citation, and scope-lock edits.
The phase ledger has seven rows, with `CRIT_CORNER` explicitly recording
\(\alpha=\beta=1/2\) as the multicritical phase-boundary junction.
The `COEXISTENCE` row is checked as `0<alpha=beta<1/2`; `(0,0)` is reserved
for the zero-rate boundary branch.
