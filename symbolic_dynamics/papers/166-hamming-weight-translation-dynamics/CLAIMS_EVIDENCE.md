# P166 claims and evidence

Status: `ROUND2_INTERNAL_ACCEPT / REVIEWS A-B 0C-0M-0m / HOLD_EXTERNAL`.

| ID | Formal claim | Proof engine in `main.tex` | Exact control | Scope ceiling |
|---|---|---|---|---|
| A | On every diagonal orbit, `T(X_j)=X_{j+m_j}`; for every target/time, `|(T^t)^-1(y)|=#{j:g_m^t(j)=0}` | direct weight calculation plus invariance of coordinate differences, Theorem 1 | every target for `2<=n<=7`, every `0<=t<=2n` | target-local `n`-phase oracle only |
| B | Every nontrivial phase cycle exhausts all occupancy mass and is the clockwise gap cycle | positive cycle increments sum to a bounded multiple of `n`, Lemma 2 | all weak compositions through `n=10`; deterministic larger-modulus samples | generic functional-graph facts and compositions receive zero credit |
| C | `P_(n,1)=1+(n-1)^n`; `P_(n,k)=k!S(n,k)` for `2<=k<=n`; recurrent count, fixed-iterate census, and zeta follow | gap composition plus labelled multinomial lift, Theorem 3 | complete literal functional graphs through `n=7` | Stirling identities and zeta conversion receive zero credit |
| D | Complete exact-depth census `D_(n,d)`; no depth beyond `n-2` | strictly increasing no-wrap partial sums plus free-bin multinomial sum, Theorem 4 | every depth layer through `n=7`; every profile tail through `n=10` | no asymptotic or probabilistic claim |
| E | Sharp depth `n-2`, complete equality profile/phase classification, last shell `(n-1)n!/2` | equality analysis in the no-wrap proof | full profiles through `n=10`; literal states through `n=7` | `n=2` explicitly has depth zero |
| F | Exact one-step fibre for every target, including integer-weight branches `0` and `n` | enumerate the `n` possible diagonal sources, Theorem 5 | every target through `n=7` | no claim of a closed global all-time fibre census |
| G | Marked EGF for all indegrees and exact image extraction | independent multinomial marking of occupancy bins | coefficient expansion agrees with full target distribution through `n=7` | classical EGF manipulation receives zero credit |
| H | Maximum fibre is `1` for `n=2` and `1+h_n` for `n>=3`, with exact equality criterion | triangular mass budget and explicit nonhit-bin construction | equality classified for all profiles through `n=10`; witnesses checked for every `3<=n<=128` | the exact binary member receives zero credit |

## Independence of the two main axes

- Claims B--E are temporal: they classify cycles and transient paths of
  composition phase maps.
- Claims F--H are inverse: they enumerate diagonal source shifts of a fixed
  target and then aggregate their occupancy constraints.
- Claim A is the shared literal interface.  Neither main axis proves the
  other, and the paper does not use executable enumeration as proof.

## Gate-A scope repairs already built into Round 0

1. `n=2` is identified as the exact Meyer--Pommersheim binary map and is
   assigned zero contribution credit.
2. The every-time statement is consistently called a target-local
   `n`-phase oracle, never a closed global all-time fibre census.

## Hostile Review A closure

Independent Review A re-derived Claims A--H without importing the author
verifier.  Its frozen control reports `11,795,304` assertions and two
byte-identical replays.  The verdict was `ACCEPT` with
`0 Critical / 0 Major / 0 minor`; consequently no claim, proof, source,
code, or PDF changed between Round 0 and Round 1.

## Hostile Review B closure

Fresh Review B again started from the literal map and independently checked
Claims A--H, the anchor-factor cancellation, all-zero EGF correction,
triangular remainder construction, direct-owner subtraction, and portfolio
firewall.  It reports `14,005,344` assertions, two byte-identical process
replays, and `ACCEPT_INTERNAL` with `0 Critical / 0 Major / 0 minor`.
Round 2 is therefore another no-change freeze.  External status remains
`HOLD_EXTERNAL`.
