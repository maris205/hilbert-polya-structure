# Executed test report

All commands below were actually run with Python -B and exited zero.
The saved evidence is deterministic and the checker imports no producer code.

| Lane | Actual receipt |
|---|---|
| producer | 64 layers; 27,833 cycle points; payload 728d8d154d78e6e3706204fb9436d6602a8a34429d33614cecfb88eba3fb913b |
| independent checker | all 55,666 exact two-scale step controls; 27,833 matrices; 320 repetitions; 16 walls; 128 fixed-iterate rows |
| symbolic | 14 universal matrix identities; 256 exact layer checks |
| numerical control | 65 checks at 90 decimal digits; explicitly not certified intervals |
| two-directory replay | identical bytes, evidence bac2638210aa6d58c1d1f51ea295cf0ad262c7edc2c44b316c4c700820fc8169 |
| repaired-hash hostile | 50/50 refused; 36 semantic, 2 JSON, 6 YAML-checker and 6 actual-write tests |
| smoke unittest | 3/3 passed; includes all six entrypoints under both -O and -OO |
| PDF construction | three rounds, two unrelated build directories per round, two passes each, byte identical |

The strict YAML parser rejects duplicate keys, unknown fields, scalar-type
drift and altered dates, with semantic and raw SHA pins. Literal false flags
cannot become integer zero. These checks do not prove the universal theorem;
the proof establishes that independently of the finite evidence range.

The release script reruns every lane and fresh PDF comparison in both write
and nonwrite modes. The self-excluding manifest stores the reconstructed
terminal receipts and exact physical membership, not an unchecked PASS label.
