# C279 results

For every maximal plateau `B=[l,r]`, the independently reconstructed velocity
is

```text
v_B=(s_r-s_{l-1})/|B|.
```

The exact event implementation therefore uses only rational affine motion and
joint block unions.  On the frozen exhaustive grid:

- all 19,530 inputs in `{-2,-1,0,1,2}^n`, `1<=n<=6`, passed;
- 62,802 distinct event times and 74,220 adjacent-pair mergers were audited;
- 9,880 event times merged more than one adjacent pair simultaneously;
- the largest event count at dimension `n` was exactly `n-1`;
- every mass, subgradient, no-splitting, ROF KKT, dissipation, final-mean, and
  consensus-bound violation counter is zero;
- five rational stresses of dimensions 8--12 contributed 30 event times and
  38 pair mergers.

The exhaustive ordered transcript SHA-256 is
`da46566b83355f273a883c632abd8fd474fab8d244edce5c613ad77396c88943`;
the stress transcript SHA-256 is
`da41a9d9cce93436425035832b315926eebc82fcc47498f074b343c67d38cb86`.

The independent checker reports 1,010,097 assertions, SymPy reports 3,707
symbolic identities and inequalities, replay is byte exact in two fresh trees,
and all 58 repaired-hash semantic mutations plus the stale-hash control are
rejected.  These computations audit the implementation; the all-real theorem
is carried by the proof in `THEOREM_PACKAGE.md`.  Release closure separately
requires the Steidl and Hoefling direct-owner tokens and the explicit
zero-originality boundary.
