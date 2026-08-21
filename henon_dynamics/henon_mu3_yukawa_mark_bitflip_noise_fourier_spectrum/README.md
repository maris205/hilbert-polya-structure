# HCS-C82 bit-flip noise and Walsh spectrum

C82 studies the Boolean full-core predicate on the 16 named labels:

```text
F(A)=1 iff A contains S9 and meets at least two of
      [S1], [S16], [S7,S15], [S3,S4,S8,S11,S12].
```

The truth table is enumerated on all 65536 retained supports and transformed
by an exact integer Walsh--Hadamard transform.  There are 30400 ones, 1024
nonzero Walsh coefficients, and maximum Fourier degree 10.  The ordered-pair
Hamming autocorrelation by distance is

```text
[30400,445696,3068864,13137152,39054016,85341312,141543616,
 181366144,180954240,140539776,84251904,38278400,12756480,
 2943488,420480,28032,0].
```

The canonical evidence SHA-256 is
`6fc49cad02956f463b1e37d017506f437edce6717414da74770ad94913ccefa1`.
The complete prefreeze file binding is recorded in
[C82_PREFREEZE_MANIFEST.json](C82_PREFREEZE_MANIFEST.json).
The independent checker verifies the C78 boundary mask-by-mask; a separate
SymPy multilinear calculation uses the ten active coordinates with the six
dummies integrated as a factor 64; replay and 13 hostile mutations pass.

This is an exact finite Boolean/noise statistic.  It makes no arithmetic,
local, Euler-factor, root-number, automorphy, full Burnside-ring/table-of-
marks, or Hilbert--Polya claim.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
