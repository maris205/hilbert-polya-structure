# R401-VAL-L1-MG-V2 release freeze

The threshold \(D_M>3\) is inherited from the earlier frozen R401-VAL hard
gate.  V2 was prospectively re-frozen after an audit found that the V1
Markdown report rendered exact fractions through nearest binary-float
decimals.  The exact-rational determinant calculation is unchanged; V2
requires exact numerator/denominator storage and 18-place decimal floor/ceil
rendering, independently replayed before release.

## Frozen components

| Component | SHA-256 |
|---|---|
| `research/route_a_wave_trace/R401_VAL_L1_MONODROMY_GAP_PROTOCOL.md` | `760fc64f8d240edb352782272b95f0ce2fc4e78faefc643d2e4956aae25b138a` |
| `scripts/run_r401_val_l1_monodromy_gap.py` | `40b84dd6cc0fa8507b88640e52520e7bb80153d6b89d06d16b578566dbd6f0c0` |
| `scripts/check_r401_val_l1_monodromy_gap_independent.py` | `e089626cc9c605722f53c98fe3e3c36e58efe1cc1e73b59fa99fa4a5eaaf2b49` |
| `tests/test_r401_val_l1_contract.py` | `6bad252aaa9471c2df188c0b9dfe90ed47f392e9d9380c2e00c76ce701e9afdd` |
| `results/r401_val_l1_monodromy_gap/summary.json` | `0b2962cd9247537a9a2cb2fbec390837abbe77b8afaa22b8dbb69e55e68babaf` |
| `results/r401_val_l1_monodromy_gap/manifest.json` | `da2d050000f7aaffbbac86dddf3c9bd103442923d4da3ddbb5523f633f9062b8` |
| `results/r401_val_l1_monodromy_gap/independent_checker.json` | `29f70ea17a54057812a5d1d71ffa27abaedecac9818f4d3ee36d86a3521206c5` |
| `results/r401_val_l1_monodromy_gap/POSTCHECK_STATUS.json` | `70ff90e48e90e2cfa19d948afcdce5b90411e59406e0af4098f6aa8de3d6d6d4` |
| `results/r401_val_l1_monodromy_gap/R401_VAL_L1_MONODROMY_GAP_REPORT.md` | `64a7af8dad79f6e44aacc5ca87fb540a087fb6d59673a5fa2f130a6af539ada0` |

## Directed displayed bounds

The authoritative 128-bit minimum lower endpoint is

\[
 \frac{479499075830964647977619704227032239226154693}
 {125000000000000000000000000000000000000000000},
\]

whose rigorous 18-place downward display is
`3.835992606647717183`.  The authoritative 256-bit minimum lower endpoint is

\[
 \frac{385074196894579469387613658291110538545744780951414621536980801422153198627515135319}
 {100000000000000000000000000000000000000000000000000000000000000000000000000000000000},
\]

whose rigorous downward display is `3.850741968945794693`.

The corresponding rigorous upward displays of the maximum interval widths
are `0.054493101512001146` at 128 bits and
`0.025036862429395394` at 256 bits.  Their authoritative fractions remain in
`summary.json`.  The inherited all-job phase-slope lower endpoint has
authoritative value

\[
 \frac{111938012055954323433615300299077846499814991}
 {12500000000000000000000000000000000000000000}
\]

and rigorous downward display `8.955040964476345874`.

The independent checker passes 202 determinant replays, 202 phase-slope
replays, all 815 exact-fraction decimal payloads, and 8302 aggregate checks.
The positive phase slope proves regularity of \(K_\epsilon=1\) and
transversality of the \(P_+=0\) event.  The invariant quotient
\(\operatorname{span}(X_K)\subset\ker(dK)\) proves
\(\chi_M=(t-1)^2\chi_{D\Pi}\) without a semisimplicity assumption.

The authorized status is `PASS_LOCAL_MONODROMY_GAP` under protocol
`R401-VAL-L1-MG-V2`, with `final_status: null`.  The interval widths are far
larger than \(2^{-30}\), so this release does not claim the final independent
event-projected determinant identity or Taylor-model residual gate.
