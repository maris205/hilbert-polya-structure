# LNR inverse author execution receipt

2026-09-06 UTC. Python 3.12.3, standard-library only. All invocations below
were actual fresh executions from `/root/autodl-tmp/symbolic_dynamics`.
This is author corroboration, not independent review. No checker reads a
repository file, the pilot, root's code, or a canonical file. Raw `cmp`
runs separately after each replay producer succeeds.

## Inputs and original production

`verify_inverse.py` SHA-256:
`fdf51545aad549c3c0c59816da2a573e92384143698060e047ae8295923c271c`.
No auxiliary input datasets or nonstandard Python libraries.

An initial unredirected execution completed with exit zero (process session
51758); its console display was truncated by the display budget and is not
the canonical artifact. A separate fresh production captured the complete
stdout, without display truncation, using exactly:

```sh
python3 docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/verify_inverse.py > docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/CANONICAL.json 2> docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/canonical.stderr
```

That process session 20343 actually completed with exit zero.
`CANONICAL.json` is 31,904 bytes, SHA-256
`3299035544028faccc6ad082bcffe2df1aaa8b4f9ff19671639236806e7b21da`;
`canonical.stderr` is empty. This original canonical remains unchanged.

## Two additional fresh raw-canonical replays

Replay 1 (process session 43580), exact command:

```sh
python3 docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/verify_inverse.py > docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay1.stdout 2> docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay1.stderr && cmp docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay1.stdout docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/CANONICAL.json > docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay1.cmp.stdout 2> docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay1.cmp.stderr
```

Replay 2 (process session 9291), exact command:

```sh
python3 docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/verify_inverse.py > docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay2.stdout 2> docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay2.stderr && cmp docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay2.stdout docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/CANONICAL.json > docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay2.cmp.stdout 2> docs/papers204_208_sequence/scouting/word_local/LNR_INVERSE_WORK/replay2.cmp.stderr
```

Both sessions actually completed with exit zero. Because of `&&`, each
producer exited zero and each raw-byte comparator exited zero. Both stdout
files are 31,904 bytes with the canonical SHA-256 above. All six replay
stderr/comparator output files are empty. No failed checker version or
canonical rewrite occurred.

## What each complete execution checks

- All 9,828 labelled sources and all 9,828 possible labelled targets for
  $n=3,\ldots,8$: edge-oriented literal inverse sets equal the complete
  zero-block decoded source sets; every matrix count equals their size;
  all maximum targets, including empty fibres and $n=3$, agree exactly.
- All positive source strings and exterior heights for run lengths one
  through six: 1,134 local source/boundary attempts, full source-set list
  agreement and all evaluated table entries. Lengths five and six give
  no positive run; the all-length exclusion is deductive in the proof.
- All 88,569 words in $A,J,B$ of lengths two through ten: exact integer
  trace bounds and complete equality/strictness checks. This is a check
  of the proof's reduced mixed-kernel lemma, not a new full-system cutoff.
- Integer $A$-power/Lucas identities, one-$B$ trace identities and strict
  dominated-kernel traces for exponents two through 100; exact rational
  certificates for the scalar constants, without floating-point tests.
- The full source-set independent-set bijection for alternating target
  lengths four, six, eight and ten. The length-ten box checks only this
  explicitly classical adapter and is not used to infer a new extremum.

Each run reports **220,564 passing assertions**, status `PASS`, and checked
record-stream SHA-256
`86a3321c3c86e04a77f5704c051d4c80c689e1eeefe73a4d755c14c5bd91dc29`.
The complete canonical contains every printed result, including all
labelled maximizing targets in the six full inverse boxes and the entire
mixed-kernel census. The digest commits to the ordered detailed records;
the script actually compares full source sets, not merely digests.

## Scope and handoff

The earlier `probe.py` and `PROBE_CANONICAL.json` are preserved discovery
artifacts, not imported by this checker. The mathematical all-$n$ warrant
is [PROOF_PACKAGE.md](PROOF_PACKAGE.md), not any finite cutoff. Source
access limits and explicit classical deductions are in
[SOURCE_BOUNDARY.md](SOURCE_BOUNDARY.md). Root must inspect original
evidence and arrange a nonauthor candidate gate before any admission.
No paper build, manuscript review, candidate acceptance, external clearance
or Git synchronization is claimed by this receipt.
