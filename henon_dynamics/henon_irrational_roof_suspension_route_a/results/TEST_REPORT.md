# C130 test report

| Test | Result |
|---|---|
| exact producer | PASS |
| independent standard-library checker | PASS, 139 assertions |
| checker independence | PASS, imports neither producer nor SymPy |
| fresh SymPy reconstruction | PASS, 110 checks |
| canonical byte replay | PASS |
| repaired-hash semantic mutations | PASS, 43/43 rejected |
| stale-hash gate mutation | PASS, 1/1 rejected |
| hostile mutations total | PASS, 44/44 rejected |
| fixed-epoch isolated PDF build A/B | PASS, byte-identical to final |
| embedded fonts and final-log scan | PASS |
| rendered-page inspection | PASS, all pages |
| release-manifest exact closure | PASS, 27 payload files plus manifest |

The finite replay contains 2,046 rooted closed words, 226 primitive cycles,
and 65 clock sectors through period 10.  The independent checker also expands
the primitive product modulo total degree 10 and obtains exactly `1-u-v`.

Forty-three semantic hostile mutations were rehashed after mutation, so their
rejection cannot be attributed to a stale checksum.  One separate mutation
leaves the forged hash stale and tests the checksum gate itself.
