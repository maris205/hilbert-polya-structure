# Root's actual CRC3 candidate replay pair

2026-09-05 UTC; Python 3.12.3 standard library, -B, no random input.
An initial command incorrectly combined workspace-relative paths with the
gate-directory working directory. The Python producer exited 2 before any
check: it could not find the duplicated script path. The redirected empty
stdout and mistakenly created directory were moved intact to
`failed_path_attempt/`; none is counted as a successful execution, and the
gate package was restored without changing its original files.

The corrected command ran from `/root/autodl-tmp/symbolic_dynamics`:

```sh
python -B docs/papers204_208_sequence/scouting/word_local/CRC3_GATE/verify_gate.py > docs/papers204_208_sequence/qa/admission_replays/crc3/run1.stdout
cmp docs/papers204_208_sequence/scouting/word_local/CRC3_GATE/CANONICAL.json docs/papers204_208_sequence/qa/admission_replays/crc3/run1.stdout
python -B docs/papers204_208_sequence/scouting/word_local/CRC3_GATE/verify_gate.py > docs/papers204_208_sequence/qa/admission_replays/crc3/run2.stdout
cmp docs/papers204_208_sequence/scouting/word_local/CRC3_GATE/CANONICAL.json docs/papers204_208_sequence/qa/admission_replays/crc3/run2.stdout
```

Both fresh producers and raw byte comparisons exited zero, combined exit
zero. Each has 721,397 assertions and all 88,572 target source-set checks
in the stated n=1..10 boxes. Both full stdout files have SHA256
`6ead393b4a0c46d641f0ce7a7d83381ad4e0ae704afca21cb81b11f2e1fe1a01`.
The original gate's five nonself manifest entries were separately checked
at exit zero. Mathematical all-parameter validity comes from the proof,
not the finite enumeration. Admission is a separate root decision.
