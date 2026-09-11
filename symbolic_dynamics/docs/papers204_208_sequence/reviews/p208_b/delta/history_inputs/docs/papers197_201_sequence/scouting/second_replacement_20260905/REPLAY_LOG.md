# Two actual fresh replays

Working directory: `/root/autodl-tmp/symbolic_dynamics`.
Command, used without imports from historical author/gate code:

```sh
PYTHONDONTWRITEBYTECODE=1 python docs/papers197_201_sequence/scouting/second_replacement_20260905/verify_second_replacement.py
```

| Run | Start UTC | Finish UTC | Process exit | Wall time | Assertions |
|---|---|---|---:|---:|---:|
| Replay 1 | 2026-09-05 06:49:53 | 2026-09-05 06:49:57 | 0 | 3.940079586 s | 218,213 |
| Replay 2 | 2026-09-05 06:49:57 | 2026-09-05 06:50:01 | 0 | 4.002170715 s | 218,213 |

The two captured stdout strings were compared directly and were **byte
identical** before saving. REPLAY_1.txt, REPLAY_2.txt and CANONICAL.txt are
the actual captured stdout, not reconstructed expected output. Their
matching SHA-256 is

```text
49375b9363b8d335e8cb760ce0979492f2002bbe6398510f92014d3b1fd89e4f
```

Verifier SHA-256 at both replays:

```text
08fd853d64eb3a342778368b2ce25da5fd1348cf8d32027183ae0d919bcf51ed
```

Scope is exactly the intake boxes: both graph maps on every graph for
n=0,...,6; CCW on every ordered triple for p=3,5. There is no random seed,
sampled mathematical test, larger graph box, larger prime or GPU use.
Each replay covers 84,090 state-map instances and counts 218,213 explicit
assertions. These are verifier units, not independent proofs or systems.

Representation checks include graph bitmask versus set-neighborhood ND1,
graph bitmask versus shortest-path-distance D2G, CCW linear center versus
equal-distance identities, every-target geometric source sets versus actual
inverse lists, closed fibre formula and all maximum equality targets,
reflection inverse within the CCW core, and geometric depth classes versus
an independently traversed functional graph. The functional census is an
exact finite diagnostic, not a source of all-parameter proofs.

Earlier live exploratory invocations existed during derivation. They are
not counted as the frozen pair: their assertion totals were 164,258,
216,317 and 216,325 as checks were added. The unchanged final script then
ran a smoke check with 218,213 before the two runs above. No mathematical
assertion failed in those invocations. The proposed ND1 union injection
was intentionally falsified in a separate diagnostic and is a permanent
negative test in the final script.

Final canonical status is `SCOUTING_ONLY_NO_ADMISSION`. It is not a Stage-1
PASS or paper-review verdict. The two final runs use the same configured
model's author-side code; no independent gate or cross-model review is
manufactured from replay repetition.
