# P170 claims-to-evidence ledger

**Lifecycle:** `ROUND0 AUTHOR FREEZE / HOLD_EXTERNAL`  
**Rule:** finite computation pressures the claims but does not replace the
uniform proofs or establish ownership.

| Claim | Uniform argument in `main.tex` | Independent author pressure |
|---|---|---|
| Literal path identity | iteration of the intersection update, Eq. `pathwise` | histories are advanced directly from enumerated fixed sets |
| Every-time/every-endpoint kernel, including `t=0` | inclusion--exclusion on labels lost from `A`, Theorem 1(i) | all labelled source/target pairs through `n=7`, times `0..5` |
| Complete positive-time support | derangement, outside transposition, and identity constructions | every labelled pair in the same boxes |
| Boolean containment eigenbasis | prescribed fixed labels plus explicit Boolean Möbius inverse | every basis vector and inverse entry through `n=7` |
| Only terminal rank eigenvalue collision | strict factorial descent except `1!=0!` | ranks through `n=7` |
| Absorption CDF and survival | empty-target specialization | exact endpoint counts and rational checks through `n=12` |
| Mean, second moment, and PGF | finite spectral tail sums | independently solved size-projected absorbing chain over `Fraction` |
| `n=1,2,3` boundary split | direct specialization; ranks 2 and 3 coincide at `n=3` | exact checks through time 14; scale separation checked for `4<=n<=64` |
| Every-endpoint cycle-marked polynomial | weighted inclusion--exclusion using prescribed-fixed cycle polynomial | coefficientwise literal history multiplication through `n=6`, time 3 |
| Nonnegative marked coefficients | literal history definition | every coefficient in all marked boxes |
| Sharp lowest degree | fixed `B` plus one complement cycle each epoch | literal coefficients and constructive witnesses |
| Sharp highest degree | moved-support/cycle-deficit inequality and parity-split constructions | all literal boxes; size triples through `n=18`; witnesses through `n=64` |
| Exact conditional cycle expectation | logarithmic derivative at `u=1` | coefficient derivatives and exact rationals in every supported box |

## Author verifier freeze

```text
program: verify_p170.py
standard library only: yes
imports scouting/gate/paper code: no
fresh process replays: 2/2
byte-identical stdout: yes
assertions: 481,935
payload SHA-256: e8f7f38c9e8bf14c2a35aba8b3eb9280127ec71374253056927290a65a5cdb8e
program SHA-256: 2a9b9167d0ba8cf36dcf76cd93e6f58f5c2bb0002f21bd2a8c6d25d13427aed8
stdout SHA-256: 985941e0a8b363fcf954d503cf825867e54548dd8fcf416ee105a4cbbac2ba13
decision: AUTHOR_ROUND0_PASS
external status: HOLD_EXTERNAL_OWNER_THIN
```

## Contribution subtraction

The following are necessary inputs but receive zero contribution credit:
common fixed sets of independent permutations; fixed-set laws and prescribed
fixed labels; ordinary inclusion--exclusion; Boolean zeta/Möbius inversion;
semilattice-walk spectra; standard absorption tail algebra; and the ordinary
symmetric-group cycle polynomial.  The retained ceiling is the complete
endpoint-conditioned marked-history package, including its two sharp degree
extrema and conditional mean.  No novelty or priority inference is made from
the bounded owner-search non-hit.
