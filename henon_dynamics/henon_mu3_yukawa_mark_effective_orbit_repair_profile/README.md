# HCS-C81 effective-1920 repair-profile orbit quotient

C81 quotients the finite repair observables by the faithful label action.  The
C75 ambient lift has order `11520`, with a six-element kernel on labels; C81
uses the effective `1920`-element action recorded by C76.  For every deletion
mask, the repair profile is

```text
(rho(D), W(D), |Phi(L\\D)|,
  threshold histograms grouped by the 8 distinct subgroup orders).
```

The threshold histograms are formed from C80's twenty target values, so target
rows that an automorphism permutes are deliberately summarized by subgroup
order.  All 65536 masks split into exactly 3024 effective-group orbits.  The
orbit-size spectrum is

```text
1:128, 2:256, 4:416, 5:128, 8:192, 10:384,
16:16, 20:672, 40:608, 80:208, 160:16.
```

The receipt records every orbit representative, stabilizer order, profile,
and the 14 distinct profile classes.  A weighted orbit polynomial recovers
`(1+x)^16`, and the fixed-support cycle spectrum gives the integer identity
`sum_g 2^{cycles(g)}/1920=3024`.

The canonical evidence hash is
`c3cc35f45e1c8f7c9d4ecaecca820bf9dbc4db1c6a5769c20c75bad21f32fd9f`.  The
complete prefreeze file binding is recorded in
[C81_PREFREEZE_MANIFEST.json](C81_PREFREEZE_MANIFEST.json).  The checker explicitly preserves the distinction between the 11520
ambient lift and the 1920 effective label action.  No full Burnside ring,
table of marks, arithmetic/local, Euler-factor, root-number, automorphy, or
Hilbert--Polya claim is made.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
