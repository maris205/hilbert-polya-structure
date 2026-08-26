# C185 exact-validation plan

The executable work is a deterministic theorem regression, not a numerical
experiment and not a substitute for the all-size proof.

| Gate | Exact test | Kill condition |
|---|---|---|
| G1 orbit/Lyapunov | rational orthogonal samples for every `2<=n<=7`; trace powers, skew Lax generator, symmetric velocity, and `dF=||[H,N]||^2` | any rational residual is nonzero |
| G2 equilibria | enumerate all `n!` permutations through `n=7` | count differs from 5,912 or sorted/reversed extrema are not unique |
| G3 pair modes | reconstruct every `(i,j)` rate and its sign | any rate disagrees with the closed formula or any simple-spectrum zero mode occurs |
| G4 Morse ledger | compare positive rates with inversions | unstable dimension or Morse index differs from `inv(pi)` |
| G5 boundary | repeated source and repeated target `3x3` sentinels | the expected collapsed equilibrium count, zero mode, or non-diagonal commuting family is absent |
| G6 independence | checker imports no producer; SymPy rebuilds symbolic identities | hidden producer import or symbolic residual |
| G7 integrity | byte replay and repaired-hash semantic attacks | replay drift or any attacked artifact is accepted |

## Frozen finite range

- dimensions: `2<=n<=7`;
- source sentinel: `lambda_i=i`;
- target sentinel: `nu_i=i^2`;
- permutations: 5,912;
- pair modes: 118,004;
- exact rational orbit samples: six.

The theorem itself allows every ordered simple real source spectrum and every
strictly increasing real target diagonal.  No finite cutoff, floating-point
integration, prime table, or target-zero table enters the proof.

## Arithmetic and proves-too-much controls

The same proof survives irrational spectra, random relabeling, reversal, and
prime or composite dimension.  This robustness is evidence against A0, not in
favor of it: the mechanism is generic matrix geometry.  Repeated spectra are a
boundary control, not a neighboring member of the main theorem.
