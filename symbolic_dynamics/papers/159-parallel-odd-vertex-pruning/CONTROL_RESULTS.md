# Exact control results — P159

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Frozen command

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p159.py
```

The deterministic output is frozen in `verification_output.txt`.  Two fresh
replays on 2026-09-02 UTC matched it byte for byte, and no `__pycache__` was
created.

```text
P159 parallel odd-vertex pruning exact verifier
GF2 incidence rank/nullity: 726
all-time fibres/images/CDF: 2184715
clock/fixed census: 112319
literal one-step fibres/boundaries: 869751
matrix orientation/nilpotence: 14
order_n=0 states=1 fixed=1 height=0 terminal_cdf=1
order_n=1 states=2 fixed=2 height=0 terminal_cdf=2
order_n=2 states=5 fixed=4 height=1 terminal_cdf=5
order_n=3 states=18 fixed=9 height=1 terminal_cdf=18
order_n=4 states=113 fixed=27 height=2 terminal_cdf=113
order_n=5 states=1450 fixed=140 height=2 terminal_cdf=1450
order_n=6 states=40069 fixed=1590 height=3 terminal_cdf=40069
parity_system_cases=511
total_enumerated_states=41658
orientation_B4_0_2=6 orientation_B4_2_0=0 square_B4_0_4=24
assertions=3167525
arithmetic=integer_and_GF2_exact
enumeration_is_not_proof=1
owner_clearance=0
external_status=HOLD_EXTERNAL
PASS
```

Transcript SHA-256:
`363d77a151dfa0b1d6b4ded84700d01dd249ed242573bff98fa38d490a1d4879`.

Verifier SHA-256:
`ffb7e464f665731a2dcb2dc3fabff724594d7420eea8edded64d33e13b413c5d`.

## Audited boxes

- Carrier: every simple labelled graph on every subset of `[n]`, for
  `0<=n<=6`; 41,658 states in total.
- Literal update: odd vertices reconstructed by edge-incidence toggling;
  closure, strict even rank loss, and fixed-state identity checked per state.
- One-step fibres: every fixed target and every source rank compared with
  `B_n`; the complete `d=0` branch checked separately.
- `s=0,d=2`: every ambient label pair is checked as the unique `K_2` source,
  together with aggregate `binom(n,2)`.
- GF(2) lane: all 511 combinations of target size, positive deleted size, and
  attainable target parity vector with total order at most nine; coefficient
  rank, augmented rank, consistency iff even `d`, and nullity are exact.
- Matrix direction: `B_4(0,2)=6`, `B_4(2,0)=0`, and
  `(B_4^2)(0,4)=24`; nilpotence checked for `0<=n<=10`.
- All times: every target/source-rank fibre, image set, image count, CDF, and
  exact shell through stabilization and two extra epochs.
- Forward boundaries: explicit paths, fixed counts, and `n=0,1` carriers.

## Independence and limits

The paper-local verifier imports neither phase-one verifier.  Its states are
immutable labelled vertex/edge tuples; its transfer matrix and row reducer are
separate formula lanes.  It uses only Python's standard library, exact
integers, and GF(2) bit rows.  There is no floating point, random seed, network
request, or third-party package.

Finite enumeration does not prove the all-parameter theorem; exhaust source
owners; establish novelty, priority, or external readiness; or validate any
asynchronous, random, directed, multigraph, weighted, or unlabelled extension.
