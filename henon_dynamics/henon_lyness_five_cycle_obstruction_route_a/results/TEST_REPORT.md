# C173 test report

All tests were run with Python 3.12 against source commit
`ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f`.

| Gate | Result |
|---|---:|
| canonical producer | pass; 100 rational rows, (n\le50) ledger |
| independent checker | pass; 891 assertions |
| SymPy reconstruction | pass; 207 exact checks |
| byte-for-byte replay | pass; 65,293 bytes |
| repaired-hash mutations | pass; 49/49 rejected |
| stale-hash mutation | pass; 1/1 rejected |

The independent checker does not import producer code.  The SymPy script
rederives all five iterates, the invariant-density identity, the inverse and
reversor, and 155 coefficient identities for the five cyclic spectral
projections.  The mutation suite changes semantic content and recomputes the
payload hash before invoking the checker, so checksum verification alone
cannot pass the suite.

PDF compilation, font, layout, snapshot, and manifest results are recorded
in `paper/COMPILE_REPORT.md` and `C173_RELEASE_MANIFEST.json` after the
deterministic release build.
