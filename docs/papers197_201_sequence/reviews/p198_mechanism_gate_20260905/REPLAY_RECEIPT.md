# P198 mechanism-gate replay

2026-09-05 UTC. Two fresh Python processes ran from the workspace root:
`python3 docs/papers197_201_sequence/reviews/p198_mechanism_gate_20260905/verify_mechanism.py`.
Both exited zero and complete stdout matched byte for byte. The unchanged
stdout is saved as CANONICAL.txt.

- Assertions per run: 3,257,004.
- Full sources and targets across odd n=3,...,25: 271,440 each.
- Verifier SHA-256: `807f6b7770ac32a3040375d56acc70fd78ef47796a6819dca47a391a4823b75d`.
- Canonical SHA-256: `57830c780dd9dc3cda2d384e7a6dfaedb9d03c248e9e51c8df4d8ef6bab40f20`.

All 11 input pins were checked from the workspace root. The verifier uses
only the Python standard library and imports no author or prior scout code.
It confirms the exact decomposition, not an external novelty statement.
The admission verdict is a contribution kill; PASS_EXACT_DECOMPOSITION
must not be read as a paper pass or zero-critical finding report.
