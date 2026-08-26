# C178 test report

All exact tests target source commit
`100e5f601a0196710d53784bdeef40d2bff89fa8`.

| Gate | Result |
|---|---:|
| canonical producer | pass; 3,583 finite sentinel rows |
| producer-independent checker | pass; 26,271 assertions |
| separate SymPy reconstruction | pass; 10,465 exact checks |
| byte-for-byte replay | pass; 931,603 bytes |
| repaired-hash mutations | pass; 64/64 rejected |
| stale-hash mutation | pass; 1/1 rejected |

The canonical payload SHA-256 is
`91b74dc7381ff6b7ceea0792ae4d03c4d8f58727e0f406660bb9111f027ef4e9`;
the released evidence-file SHA-256 is
`69087059465060c7c0b8536807d8192ff4db3c914e9ad1791474053ea35b12ba`.

The checker does not import producer code.  SymPy reconstructs the rotation
group, reversor, Hamiltonian invariance, oscillator commutators, generalized
Laguerre orthogonality, phase arithmetic, exact irrational controls, and the
metaplectic \(2\pi\) sign/\(4\pi\) return for exact real-time representatives.
Mutation tests recompute the payload hash after changing semantic content,
so checksum checking alone cannot pass the suite.

PDF build, page, font, layout, snapshot, and manifest results are recorded in
`paper/COMPILE_REPORT.md` and `C178_RELEASE_MANIFEST.json`.
