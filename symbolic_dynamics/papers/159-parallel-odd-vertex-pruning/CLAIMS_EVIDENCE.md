# Claims and evidence ledger — P159

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

The symbolic proof is dispositive.  Exact computation supplies bounded
counterexample pressure only.  The subtraction column prevents standard or
previously occupied ingredients from being counted as contributions.

| Claim interface | Symbolic evidence | Exact counterexample pressure | Zero-credit boundary |
|---|---|---|---|
| Recurrent states are exactly even graphs; maximum clock is `floor(n/2)` | Theorem 1(i), Section 2: handshaking, strict loss, path witness | every state and path through `n=6`; 112,319 clock/fixed assertions | handshaking, generic absorption, pruning clock, fixed-even locus |
| Strict predecessor exists iff positive rank loss `d` is even | Section 3: right-side parity of the connected incidence system | all target parity vectors with `s+d<=9`; part of 726 GF(2) assertions, plus all literal one-step fibres through `n=6` | incidence-image parity is standard |
| Fixed-`D` strict fibre is `2^[s(d-1)+binom(d-1,2)]` and independent of target edges | Section 3: connected incidence rank `s+d-1` and rank–nullity | 511 independent parity systems and every literal target/source-rank fibre | connected binary incidence rank and rank–nullity receive zero credit; their target-uniform application is retained |
| Labelled strict transfer is `B_n(s,m)` | choose `D` among `n-s` unused labels | 869,751 literal one-step/boundary assertions | binomial label choice is elementary |
| `d=0` and `s=0,d=2` boundaries | no deletion iff source is even and fixed; fixed pair forces `K_2` | explicit same-rank full fibres, every fixed pair, and aggregate `binom(n,2)` | no silent diagonal in strict `B_n` |
| Every-time fibres are `B_n^t` for non-even targets and `I+...+B_n^t` for even targets | Section 4: strict predecessors cannot wait; unique intermediates; first arrival at fixed target | every target, source rank, and time through stabilization and beyond; 2,184,715 all-time assertions | generic matrix multiplication and absorbing-chain language |
| Matrix orientation is row target / column source | Equation (4.1) and chain composition | `B_4(0,2)=6`, `B_4(2,0)=0`, `(B_4^2)(0,4)=24` | transpose is explicitly rejected |
| Time-`t` image iff target is even or `n-s>=2t`, for `t>=1` | positive even reverse increments; fixed self-predecessors | literal image sets and closed image counts at every audited time | `t=0` is separately the identity image |
| Phase, fixed, image, CDF, and exact shell formulas | target-label choice, complete-graph incidence kernel, and even-target fibre summation | exact phase/fixed counts, image counts, CDFs, and shell differences | even-graph cycle-space count is standard |

## Mandatory sentinels

- `n=0`: one fixed empty state, clock zero.
- `n=1`: empty and singleton states fixed, clock zero.
- `s=0,d=2`: one `K_2` for each deleted pair.
- `t=0`: identity fibre and full image.
- A geometric sum on a non-even target is false and is actively excluded.
- “Even graph” does not impose connectivity.

## Evidence hierarchy

1. `main.tex` and `PROOF_PACKAGE.md` prove the all-parameter result.
2. `verify_p159.py` is an independent tuple-based exact falsifier.
3. `SOURCE_VERIFICATION.md` supports metadata and subtraction only.
4. A bounded search non-hit supports no novelty, priority, ownership, or
   external-release conclusion.

Formal Review A returned zero findings.  Formal Review B found only the stale
lifecycle sentence replaced here; no mathematical or executable issue was
reported.
